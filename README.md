# AI Evals Course - July 2025

This repository contains materials for an AI evaluations course focused on building and evaluating a customer support chatbot using Braintrust. You'll learn how to generate synthetic data, create evaluation tasks, and measure the performance of AI systems.

## Getting Started

### 1. Sign up for Braintrust

First, create your Braintrust account using this link: [Sign up for Braintrust](https://braintrust.dev/signup?utm_source=online_course&utm_medium=course_promo&utm_campaign=evals_course_signup).

If this is your first time using Braintrust, you'll need to create a default organization (e.g., can be anything but typical values are the name of your business or team).

### 2. Set up API Keys

You'll need to obtain and configure the following API keys:

- **BRAINTRUST_API_KEY**: Go to Settings > API Keys to create.
- **ANTHROPIC_API_KEY**: Get this from [Anthropic Console](https://console.anthropic.com/)
- **OPENAI_API_KEY**: Get this from [OpenAI Platform](https://platform.openai.com/api-keys)

Create a `.env` file in the project root and add your API keys:

```bash
BRAINTRUST_API_KEY=your_braintrust_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Configure AI Providers in Braintrust

If you want to use Anthropic and OpenAI models with Braintrust Loop:

1. Go to your Braintrust dashboard
2. Navigate to **Settings > AI Providers**
3. Add your Anthropic and OpenAI API keys there

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for fast Python package management. Follow these steps to set up your development environment:

### 1. Create and activate virtual environment

```bash
# Create virtual environment with Python 3.12+
uv venv --python 3.12

# Activate the virtual environment

# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
# Install all project dependencies
uv sync

# Install with development dependencies (recommended)
uv sync --group dev
```

## Running Recipe Bot

```python
uvicorn backend.main:app --reload
# Open http://127.0.0.1:8000
```

See the [AI Evaluations Course Recipe Chatbot repo](https://github.com/ai-evals-course/recipe-chatbot) for more info on this project.

## Braintrust Projects

### 01 - Braintrust Intro

In this section, you'll build and evaluate a **customer support chatbot** for a municipal government. The bot will help citizens get information about city services, report issues, and navigate local government processes. You'll learn how to:

- Generate high-quality synthetic training and evaluation data
- Create robust evaluation tasks and metrics
- Measure and improve AI system performance
- Use Braintrust for comprehensive AI evaluation workflows

#### Notebooks

Navigate to the `01-braintrust-intro` folder and run the following notebooks in order:

##### 1. [01_generate_data.ipynb](./01-braintrust-intro/01_generate_data.ipynb)

**Generate Synthetic Data for Customer Support**

In this notebook, you'll learn how to:

- Create realistic customer support scenarios and queries
- Generate diverse conversation examples covering different city departments
- Use AI to create high-quality synthetic datasets
- Structure data for effective evaluation workflows
- Review and curate generated data for quality assurance

##### 2. [02_tasks_and_evals.ipynb](./01-braintrust-intro/02_tasks_and_evals.ipynb)

**Building Evaluation Tasks and Running Evals**

This notebook covers:

- Setting up evaluation tasks in Braintrust
- Defining metrics for customer support quality (accuracy, helpfulness, tone)
- Running systematic evaluations on your chatbot
- Analyzing results and identifying areas for improvement
- Comparing different model configurations and prompting strategies

### 02 - Homework 1 & 2

In this section, you'll learn how to instrument your recipe chatbot to log traces to Braintrust with LiteLLM. You'll build **synthetic query generation** capabilities and perform **initial error analysis** using systematic coding methods. You'll learn how to:

- Generate high-quality synthetic queries using dimensional analysis
- Create realistic query variations with different typing styles and formats
- Perform open coding to identify patterns in AI system failures
- Use axial coding to define failure mode taxonomies
- Build comprehensive error analysis datasets for systematic improvement

#### Notebooks

Navigate to the `02-hw_1_2` folder and run the following notebooks in order:

##### 1. [01_hw2_generate_initial_queries.ipynb](./02-hw_1_2/01_hw2_generate_initial_queries.ipynb)

**Generate Synthetic Data with Dimensional Analysis**

In this notebook, you'll learn how to:

- Define key dimensions of user query space for systematic variation
- Generate unique combinations of dimension values as tuples
- Create natural language queries from dimensional specifications
- Add realistic typing variations (typos, capitalization, text speak)
- Manage and curate synthetic datasets through human review workflows

##### 2. [02_hw_2_initial_error_analysis.ipynb](./02-hw_1_2/02_hw_2_initial_error_analysis.ipynb)

**Systematic Error Analysis with Open and Axial Coding**

This notebook covers:

- Running your bot on synthetic queries to generate traces
- Performing open coding to identify failure patterns without preconceived categories
- Using axial coding to define systematic failure mode taxonomies
- Building error analysis datasets with LLM-assisted failure mode identification
- Visualizing failure mode distributions and planning systematic improvements

### 03 - Homework 3

In this section, you'll develop and calibrate **LLM-as-Judge** evaluation systems for your recipe bot. You'll learn how to create robust evaluation metrics, align judges with human annotations, and measure system performance with statistical confidence. You'll learn how to:

- Create balanced train/validation/test splits from labeled data
- Develop LLM judge prompts that align with human evaluations
- Calculate True Positive Rate (TPR) and True Negative Rate (TNR) metrics
- Use statistical methods to estimate true performance on unlabeled data
- Calibrate LLM judges for reliable automated evaluation

#### Notebooks

Navigate to the `03-hw_3` folder and run the following notebooks in order:

##### 1. [01_hw_3_llm_judge_align.ipynb](./03-hw_3/01_hw_3_llm_judge_align.ipynb)

**LLM Judge Development and Validation**

In this notebook, you'll learn how to:

- Split labeled trace data into balanced train/validation/test datasets
- Develop LLM judge prompts using Braintrust Loop for iterative refinement
- Calculate TPR/TNR metrics across different datasets to validate judge performance
- Run evaluations on unlabeled traces using calibrated LLM judges
- Use the `judgy` library to estimate true success rates with confidence intervals

### 04 - Homework 4

In this section, you'll build and evaluate **Retrieval-Augmented Generation (RAG)** systems for your recipe bot. You'll create adversarial evaluation datasets, implement retrieval systems, and make your bot truly agentic with tool-calling capabilities. You'll learn how to:

- Create challenging retrieval evaluation datasets with adversarial examples
- Build and evaluate BM25-based retrieval systems
- Compare query rewriting strategies against raw user queries
- Implement agentic capabilities with tool-calling and retrieval workflows
- Measure retrieval performance with Recall@K and MRR metrics

#### Notebooks

Navigate to the `04-hw_4` folder and run the following notebooks in order:

##### 1. [01_hw_4_rag.ipynb](./04-hw_4/01_hw_4_rag.ipynb)

**Retrieval System Evaluation and Agent Implementation**

In this notebook, you'll learn how to:

- Create document embeddings and similarity-based adversarial test cases
- Build comprehensive retrieval evaluation datasets with ground truth
- Implement and evaluate BM25 retrieval systems with multiple metrics
- Compare performance of query rewrite agents vs. direct user queries
- Transform your recipe bot into an agentic system with retrieval tools

### 05 - Homework 5

In this section, you'll perform advanced **agent error analysis** using failure transition analysis. You'll instrument multi-step agent workflows, implement online scoring, and build comprehensive failure analysis tools. You'll learn how to:

- Capture and trace multi-step agent workflows in Braintrust
- Implement online scorers for real-time agent step evaluation
- Build failure transition datasets from agent execution logs
- Create failure transition heat maps to visualize agent breakdown patterns
- Analyze agent failure modes to identify systematic improvement opportunities

#### Notebooks

Navigate to the `05-hw_5` folder and run the following notebooks in order:

##### 1. [01_hw_5_agent_error_analysis.ipynb](./05-hw_5/01_hw_5_agent_error_analysis.ipynb)

**Agent Workflow Analysis and Failure Transition Mapping**

In this notebook, you'll learn how to:

- Instrument agentic workflows to capture individual step performance
- Configure online scorers for real-time evaluation of agent steps
- Extract and analyze agent execution logs from Braintrust
- Build failure transition datasets showing success-to-failure patterns
- Create heat map visualizations to identify critical failure transition points

## Dependencies

This project uses the following key libraries:

- **braintrust**: AI evaluation platform and workflows
- **anthropic**: Anthropic's Claude API client
- **openai**: OpenAI API client
- **pydantic**: Data validation and serialization

See `pyproject.toml` for the complete dependency list.
