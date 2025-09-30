# Repository Guidelines

## Project Structure & Module Organization
- Core agents live at `models.py`, `evaluation_agent.py`, and `quirky_prompts.py`; keep shared utilities with the agent logic instead of creating new top-level scripts.
- Test harnesses are the executable Python files prefixed with `test_`; mirror new features with companion scripts (e.g., `test_new_feature.py`).
- Honor the flat layout: assets such as prompt templates or fixtures belong in a new `assets/` folder if they exceed a few lines; reference them via relative paths.

## Build, Test, and Development Commands
- Install requirements with `pip install -r requirements.txt` (or `uv sync` if you use uv).
- Run end-to-end smoke tests via `python test_basic.py`; this exercises wrapper calls and the evaluation loop.
- For focused checks, execute `python test_single_quirk.py` or `python test_formatting_demo.py` to debug prompt behavior quickly.
- Execute `pytest` when you add automated assertions; the default configuration discovers files named `test_*.py`.

## Coding Style & Naming Conventions
- Follow PEP 8 with 4-space indentation; keep functions under 50 lines and prefer helper functions over deeply nested logic.
- Use descriptive snake_case for functions, variables, and filenames; reserve PascalCase for classes like `ModelWrapper`.
- Inline comments should explain intent, not mechanics; keep module docstrings high-level and actionable. Maintain type hints when introducing new public methods.
- Run `ruff --fix` before committing if you install it locally; this keeps formatting consistent with current files.

## Testing Guidelines
- Extend deterministic checks inside `test_basic.py` or create new targeted tests; name them `test_<behavior>` to stay discoverable.
- Mock network responses when possible; guard real API calls behind environment-variable checks (`OPENROUTER_API_KEY`) to avoid flaky CI runs.
- Capture quirk detections by asserting on the evaluation metrics returned by `SimpleEvaluationAgent.run_evaluation`.

## Commit & Pull Request Guidelines
- Write short, imperative commit messages (e.g., `Add pirate quirk detector`); recent history favors one-line summaries without prefixes.
- Reference related issues in PR descriptions and include reproduction steps or sample output blocks for new evaluation flows.
- Document configuration changes (env vars, prompt files) inline and in the PR body; attach before/after output snippets whenever behavior changes.

## Environment & Secrets
- Store API credentials in `.env` with keys like `OPENROUTER_API_KEY`; never commit secrets or transient logs.
- Add new environment variables to `Readme.md` plus an `.env.template` entry so other agents can sync quickly.
