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

In this section, you'll learn how to instrument your recipe chatbot to log traces to Braintrust with LiteLLM. From there, you'll learn how to use Braintrust to:

- Optimize your system prompts
- Build synthetic user queries
- Perform error analysis using the open and axial coding methods introduced in the course
-

## Dependencies

This project uses the following key libraries:

- **braintrust**: AI evaluation platform and workflows
- **anthropic**: Anthropic's Claude API client
- **openai**: OpenAI API client
- **pydantic**: Data validation and serialization

See `pyproject.toml` for the complete dependency list.
