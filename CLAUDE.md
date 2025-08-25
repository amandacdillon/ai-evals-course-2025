# AI Evals Course 2025 - Claude Development Guide

This project is designed to set up comprehensive evaluations (evals) for two different AI applications: a customer support chatbot for municipal services and a recipe recommendation system. The course teaches systematic AI evaluation methodologies using modern tooling.

## Project Overview

This repository contains a complete AI evaluations course that covers:
- **Customer Support Bot**: Municipal government chatbot for citizen services
- **Recipe Bot**: Intelligent recipe recommendation and query system
- **Evaluation Framework**: Comprehensive testing and measurement systems for both applications

## Technology Stack

### Package Management
This project uses **UV** (Ultra-fast Python package manager) for dependency management:
- Install UV: `pip install uv` or follow [UV installation guide](https://docs.astral.sh/uv/)
- Create environment: `uv venv --python 3.12`
- Install dependencies: `uv sync --group dev`

### AI Evaluation Platform
The project is built around **Braintrust**, a comprehensive AI evaluation platform:
- Synthetic data generation and curation
- Evaluation task configuration and execution  
- Performance metrics and analysis dashboards
- Trace logging and debugging workflows
- LLM-as-Judge evaluation systems

### AI Models & APIs
- **Anthropic Claude**: Primary LLM for chatbot responses
- **OpenAI GPT**: Alternative model for comparison testing
- **LiteLLM**: Unified interface for multiple LLM providers
- **Sentence Transformers**: For embedding generation and retrieval

## Development Environment Setup

### 1. Prerequisites
- Python 3.12+
- UV package manager
- Git

### 2. Environment Setup
```bash
# Clone and navigate to project
cd ai-evals-course-2025

# Create virtual environment
uv venv --python 3.12

# Activate environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Install all dependencies
uv sync --group dev
```

### 3. API Keys Configuration
Create a `.env` file with required API keys:
```bash
BRAINTRUST_API_KEY=your_braintrust_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here  
OPENAI_API_KEY=your_openai_api_key_here
```

## Project Structure

### Course Modules
1. **01-braintrust-intro/**: Customer support bot evaluation basics
2. **02-hw_1_2/**: Synthetic data generation and error analysis
3. **03-hw_3/**: LLM-as-Judge systems and validation
4. **04-hw_4/**: RAG systems and retrieval evaluation
5. **05-hw_5/**: Advanced agent error analysis

### Application Components
- **backend/**: Recipe bot API with FastAPI
- **frontend/**: Simple HTML interface
- **data/**: Processed datasets and evaluation results

## Key Development Commands

### Running Applications
```bash
# Start recipe bot API
uvicorn backend.main:app --reload

# Access at http://127.0.0.1:8000
```

### Code Quality
```bash
# Lint code (Ruff configured in pyproject.toml)
ruff check .

# Format code
ruff format .

# Run pre-commit hooks
pre-commit run --all-files
```

### Working with Notebooks
All course content is delivered through Jupyter notebooks. Run notebooks in order within each module directory.

## Braintrust Integration

This project heavily integrates with Braintrust for:
- **Dataset Management**: Synthetic data generation and curation
- **Evaluation Tasks**: Automated testing of AI system performance
- **Trace Logging**: Detailed execution logging for debugging
- **Metrics Dashboard**: Performance visualization and analysis
- **LLM Judge Validation**: Automated evaluation system calibration

### Key Braintrust Workflows
1. Generate synthetic evaluation data
2. Create evaluation tasks with custom metrics
3. Log system traces during execution
4. Run systematic evaluations across model variations
5. Analyze results and identify improvement opportunities

## Testing & Evaluation

The project implements comprehensive evaluation methodologies:
- **Synthetic Data Generation**: Dimensional analysis for query space coverage
- **Error Analysis**: Open and axial coding for failure mode identification  
- **LLM-as-Judge**: Automated evaluation with human alignment validation
- **Retrieval Evaluation**: BM25 and embedding-based retrieval testing
- **Agent Analysis**: Multi-step workflow failure transition mapping

## Development Workflow

1. **Setup**: Install UV, create environment, configure API keys
2. **Explore**: Work through course notebooks sequentially
3. **Implement**: Build evaluation systems for your AI applications
4. **Evaluate**: Run systematic evaluations using Braintrust
5. **Iterate**: Analyze results and improve system performance

## Dependencies

Core evaluation and AI libraries:
- `braintrust>=0.2.0` - AI evaluation platform
- `anthropic>=0.57.1` - Claude API client
- `openai>=1.95.0` - OpenAI API client
- `litellm>=1.74.8` - Unified LLM interface
- `instructor>=1.9.2` - Structured LLM outputs
- `judgy>=0.1.0` - Statistical evaluation tools

See `pyproject.toml` for complete dependency list.

## Getting Started

1. Complete the environment setup above
2. Sign up for Braintrust account and get API key
3. Start with `01-braintrust-intro/01_generate_data.ipynb`
4. Work through course modules sequentially
5. Apply evaluation techniques to your own AI applications

This course provides production-ready evaluation frameworks that can be adapted for any AI application requiring systematic testing and improvement.