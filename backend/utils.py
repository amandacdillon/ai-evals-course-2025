from __future__ import annotations

from socket import SYSPROTO_CONTROL

from litellm.constants import SYSTEM_MESSAGE_TOKEN_COUNT

"""Utility helpers for the recipe chatbot backend.

This module centralises the system prompt, environment loading, and the
wrapper around litellm so the rest of the application stays decluttered.
"""

import inspect
import json
import os
import re

from pathlib import Path
from typing import Any, Callable, Dict, Final, List, get_type_hints

import braintrust as bt
import litellm  # type: ignore

from dotenv import load_dotenv

from backend.query_rewrite_agent import QueryRewriteAgent
from backend.retrieval import create_retriever

# Ensure the .env file is loaded as early as possible.
load_dotenv(override=False)

qwra = QueryRewriteAgent()

# Get the directory of the current file and construct paths relative to project root
current_dir = Path(__file__).parent
project_root = current_dir.parent
retriever = create_retriever(
    project_root / "backend" / "data" / "processed_recipes.json", project_root / "backend" / "data" / "bm25_index.pkl"
)

# Wayde: We initialize our Braintrust logger at module scope and wrap our Litellm client
# so that spans related to calling litellm are properly nested and usage metrics are logged.
bt.init_logger(os.environ.get("BRAINTRUST_PROJECT"))
litellm_wrapper = bt.wrap_litellm(litellm)  # type: ignore

# --- Constants -------------------------------------------------------------------

# Wayde: We default to using the versioned prompt we created in Braintrust if it exists
DEFAULT_SYSTEM_PROMPT: str = (
    "You are an expert chef recommending delicious and useful recipes. "
    "Present only one recipe at a time. If the user doesn't specify what ingredients "
    "they have available, assume only basic ingredients are available."
    "Be descriptive in the steps of the recipe, so it is easy to follow."
    "Have variety in your recipes, don't just recommend the same thing over and over."
    "You MUST suggest a complete recipe; don't ask follow-up questions."
    "Mention the serving size in the recipe. If not specified, assume 2 people."
)

try:
    bt_sys_prompt = bt.load_prompt(project=os.environ.get("BRAINTRUST_PROJECT"), slug="recipe-bot-prompt-ef37")
    SYSTEM_PROMPT = bt_sys_prompt.prompt.messages[0].content  # type: ignore
except Exception as e:
    print(f"Error loading system prompt: {e}")
    SYSTEM_PROMPT = DEFAULT_SYSTEM_PROMPT

# Fetch configuration *after* we loaded the .env file.
MODEL_NAME: Final[str] = os.environ.get("MODEL_NAME", "gpt-4o-mini")


# --- Utility functions -------------------------------------------------------


def format_llm_tools(*functions: Callable) -> List[Dict[str, Any]]:
    """Create properly formatted tools list from function definitions.

    Args:
        *functions: One or more function objects to convert to OpenAI tool format

    Returns:
        List of tool definitions in OpenAI format
    """
    tools = []

    for func in functions:
        # Get function signature and type hints
        sig = inspect.signature(func)
        type_hints = get_type_hints(func)

        # Extract description from docstring
        docstring = inspect.getdoc(func) or ""
        description = docstring.split("\n")[0] if docstring else f"Function {func.__name__}"

        # Build parameters schema
        properties = {}
        required = []

        for param_name, param in sig.parameters.items():
            # Skip self parameter
            if param_name == "self":
                continue

            # Get type annotation
            param_type = type_hints.get(param_name, str)

            # Convert Python types to JSON schema types
            if param_type == str:
                json_type = "string"
            elif param_type == int:
                json_type = "integer"
            elif param_type == float:
                json_type = "number"
            elif param_type == bool:
                json_type = "boolean"
            elif param_type == list or getattr(param_type, "__origin__", None) == list:
                json_type = "array"
            elif param_type == dict or getattr(param_type, "__origin__", None) == dict:
                json_type = "object"
            else:
                json_type = "string"  # default fallback

            # Extract parameter description from docstring Args section
            param_desc = f"Parameter {param_name}"
            if docstring:
                # Look for Args section and extract parameter description
                args_match = re.search(r"Args:\s*\n(.*?)(?:\n\n|\nReturns:|\nRaises:|\Z)", docstring, re.DOTALL)
                if args_match:
                    args_section = args_match.group(1)
                    param_pattern = rf"\s*{re.escape(param_name)}[:\s]+(.*?)(?:\n\s*\w+[:\s]+|\Z)"
                    param_match = re.search(param_pattern, args_section, re.DOTALL)
                    if param_match:
                        param_desc = param_match.group(1).strip()

            properties[param_name] = {"type": json_type, "description": param_desc}

            # Check if parameter is required (no default value)
            if param.default == inspect.Parameter.empty:
                required.append(param_name)

        # Build tool definition
        tool_def = {
            "type": "function",
            "function": {
                "name": func.__name__,
                "description": description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                    "additionalProperties": False,
                },
                "strict": True,
            },
        }

        tools.append(tool_def)

    return tools


# --- Agent wrapper ---------------------------------------------------------------


def _format_recipes_for_llm(recipes: List[Dict[str, Any]]) -> str:
    """Format a recipe for the LLM."""
    formatted_recipes = []
    for recipe in recipes:
        formatted_recipes.append(f"""
            -----              
            Name: {recipe["name"]}
            Description: {recipe["description"]}
            Minutes: {recipe["minutes"]}
            Ingredients: {recipe["ingredients"]}
            Steps: {recipe["steps"]}
            Nutrition: {recipe["nutrition"]}
            Tags: {recipe["tags"]}
            -----
            """)

    return f"Recipes matching the user's query:\n\n{'\n\n'.join(formatted_recipes)}"


@bt.traced
def find_matching_recipes(query: str) -> str:
    """Use this tool to fetch recipes related to the user's query to use as inspiration for the recipe you are recommending

    Args:
        query: The user's query

    Returns:
        A list of recipes that match the user's query
    """
    recipes = retriever.retrieve_bm25(query, 3)
    return _format_recipes_for_llm(recipes)


# Generate tools list automatically from function definitions
tools = format_llm_tools(find_matching_recipes)
tool_registry = {"find_matching_recipes": find_matching_recipes}


# Wayde: We use the `@bt.traced` decorator to automatically log the input and output of the function.
# We also use the `notrace_io=True` so that we can control the inputs/outputs logged (by default
# Braintrust will log the inputs into this method as the "input" and whatever it returns as the "output").
@bt.traced(notrace_io=True)
def get_agent_response(
    messages: List[Dict[str, str]],
    metadata: dict | None = None,
    query_rewrite: bool = True,
) -> List[Dict[str, str]]:  # noqa: WPS231
    """Call the underlying large-language model via *litellm*.

    Parameters
    ----------
    messages:
        The full conversation history. Each item is a dict with "role" and "content".

    Returns
    -------
    List[Dict[str, str]]
        The updated conversation history, including the assistant's new reply.
    """

    # litellm is model-agnostic; we only need to supply the model name and key.
    # The first message is assumed to be the system prompt if not explicitly provided
    # or if the history is empty. We'll ensure the system prompt is always first.
    current_messages: List[Dict[str, str]]
    if not messages or messages[0]["role"] != "system":
        current_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages
    else:
        current_messages = messages

    messages_len = len(current_messages)

    # If you want to use the query rewrite agent to "improve" the query, you can do so here.
    if query_rewrite:
        res_d = qwra.process_query(messages[-1]["content"])
        messages[-1]["content"] = res_d["processed_query"]

    # We always want to fetch the most relevant recipes based on the latest messages
    rsp = litellm_wrapper.completion(model=MODEL_NAME, messages=current_messages, tools=tools, tool_choice="auto")

    while True:
        tc = rsp.choices[0].message.tool_calls
        if not tc:  # no tool calls => final answer
            assistant_reply_content: str = rsp["choices"][0]["message"]["content"].strip()
            current_messages.append({"role": "assistant", "content": assistant_reply_content})
            break

        current_messages.append(rsp.choices[0].message.model_dump(exclude_none=True))
        for call in tc:
            fn = tool_registry[call.function.name]
            args = json.loads(call.function.arguments or "{}")
            result = fn(**args)
            current_messages.append(
                {"role": "tool", "tool_call_id": call.id, "content": json.dumps(result) if not isinstance(result, str) else result}
            )

        rsp = litellm_wrapper.completion(model=MODEL_NAME, messages=current_messages, tools=tools, tool_choice="auto")

    # Wayde: We log the input and output of the function as a span.
    # We also pass in the metadata for the row so that we can trace the row back to the original input.
    # Note: If you are good with the default logging, you can just use the `@bt.traced` decorator instead.
    bt.current_span().log(
        input=current_messages[:messages_len],
        output=current_messages[messages_len:],
        metadata=metadata,
    )

    # return just the initial messages and the final response as the output
    return current_messages[:messages_len] + [current_messages[-1]]
