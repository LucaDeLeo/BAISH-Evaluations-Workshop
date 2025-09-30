# GEMINI.md

## Project Overview

This project is a Python-based system for evaluating AI models for behavioral "quirks." It uses an LLM (Large Language Model) judge to detect whether a model's responses exhibit specific, predefined quirky behaviors. The core of the project is the `evaluation_agent.py`, which orchestrates the evaluation process.

The main components are:

*   **`evaluation_agent.py`**: The main agent that runs the evaluations. It uses an LLM judge to evaluate model responses for quirks.
*   **`models.py`**: A wrapper class for interacting with different LLM APIs (OpenAI and Anthropic).
*   **`quirky_prompts.py`**: Defines the quirky behaviors to be tested, including the system prompts that are used to elicit the behavior and a description of the quirk.
*   **`test_*.py`**: A suite of tests for the system.

The project is designed to be run from the command line. It takes a quirk name as input and then runs an evaluation to determine how reliably the quirk can be detected in a model's responses.

## Building and Running

### Setup

1.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2.  Create a `.env` file with your API keys. You can use the `.env.template.txt` file as a starting point:

    ```bash
    cp .env.template.txt .env
    ```

    Then, edit the `.env` file to add your API keys.

### Running Evaluations

The main entry point for running evaluations is the `LLMJudgeEvaluationAgent` class in `evaluation_agent.py`. You can run a comprehensive evaluation of all quirks by calling the `run_comprehensive_evaluation` method.

To run a single evaluation, you can use the `run_evaluation` method, passing in the name of the quirk you want to test.

Example:

```python
from evaluation_agent import LLMJudgeEvaluationAgent

agent = LLMJudgeEvaluationAgent()

# Run a comprehensive evaluation
agent.run_comprehensive_evaluation()

# Run a single evaluation
agent.run_evaluation("pirate")
```

### Testing

The project includes a suite of tests in the `test_*.py` files. You can run the tests using `pytest`:

```bash
pytest
```

## Development Conventions

*   **Code Style**: The project follows the PEP 8 style guide for Python code.
*   **Testing**: All new features should be accompanied by tests. The project uses `pytest` for testing.
*   **Dependencies**: All Python dependencies are managed in the `requirements.txt` file.
