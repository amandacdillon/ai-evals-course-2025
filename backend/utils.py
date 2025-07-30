from __future__ import annotations

from socket import SYSPROTO_CONTROL

from litellm.constants import SYSTEM_MESSAGE_TOKEN_COUNT

"""Utility helpers for the recipe chatbot backend.

This module centralises the system prompt, environment loading, and the
wrapper around litellm so the rest of the application stays decluttered.
"""

import os

from typing import Dict, Final, List

import braintrust as bt
import litellm  # type: ignore

from dotenv import load_dotenv

# Ensure the .env file is loaded as early as possible.
load_dotenv(override=False)

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


# --- Agent wrapper ---------------------------------------------------------------


# Wayde: We use the `@bt.traced` decorator to automatically log the input and output of the function.
# We also use the `notrace_io=True` so that we can control the inputs/outputs logged (by default
# Braintrust will log the inputs into this method as the "input" and whatever it returns as the "output").
@bt.traced(notrace_io=True)
def get_agent_response(
    messages: List[Dict[str, str]],
    metadata: dict | None = None,
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

    completion = litellm_wrapper.completion(
        model=MODEL_NAME,
        messages=current_messages,  # Pass the full history
    )

    assistant_reply_content: str = completion["choices"][0]["message"]["content"].strip()  # type: ignore[index]

    # Append assistant's response to the history
    updated_messages = current_messages + [{"role": "assistant", "content": assistant_reply_content}]

    # Wayde: We log the input and output of the function as a span.
    # We also pass in the metadata for the row so that we can trace the row back to the original input.
    # Note: If you are good with the default logging, you can just use the `@bt.traced` decorator instead.
    bt.current_span().log(
        input=current_messages,
        output=[updated_messages[-1]],
        metadata=metadata,
    )
    return updated_messages
