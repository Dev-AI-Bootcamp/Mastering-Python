# CLAUDE.md — AI Assistant Guide for Mastering-Python

This file provides context and conventions for AI assistants (e.g., Claude Code) working in this repository.

## Project Overview

**Mastering Python for Professional Programmers** is a course/workshop repository demonstrating Python fundamentals and practical AI/API integrations. It is used as a hands-on reference for students learning Python in a professional context.

- Companion slides: [Google Slides](https://docs.google.com/presentation/d/1VgZEZZNt3h_ryVSUtsT-ov5YQWA65dL7m8SJXR0k3Jk/edit?usp=sharing)

---

## Repository Structure

```
Mastering-Python/
├── main.py          # Core Python examples: variables, functions, classes
├── kimi.py          # NVIDIA-hosted Kimi K2.5 LLM API example
├── pyproject.toml   # Project metadata and dependencies (uv/PEP 517)
├── installUV.sh     # One-liner to install the uv package manager
├── README.md        # Setup instructions and reference links
└── CLAUDE.md        # This file
```

### Key Files

| File | Purpose |
|---|---|
| `main.py` | Demonstrates type-annotated variables, functions, classes, and the `if __name__ == "__main__"` guard |
| `kimi.py` | Shows streaming and non-streaming chat completions via the NVIDIA inference API using `moonshotai/kimi-k2.5` |
| `pyproject.toml` | Declares the project (`mastering-python`, Python ≥3.11) and its runtime dependencies |
| `installUV.sh` | Bootstraps `uv` with a single `curl` command |

---

## Development Environment

### Package Manager: `uv`

This project uses [uv](https://docs.astral.sh/uv/) for virtual environment and dependency management. **Do not use `pip` directly.**

```bash
# Install uv (Linux/macOS)
bash installUV.sh
# Windows: Set-ExecutionPolicy RemoteSigned -Scope CurrentUser first

# Create virtual environment
uv venv

# Install dependencies
uv sync

# Activate the venv (follow the green output line, typically one of:)
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# Run a script
uv run main.py
uv run kimi.py
```

### Python Version

Requires **Python 3.11 or newer** (declared in `pyproject.toml`).

### Dependencies

| Package | Purpose |
|---|---|
| `openai >=2.18.0` | OpenAI-compatible SDK for LLM API calls |
| `python-dotenv >=1.2.1` | Load secrets from `.env` files |
| `requests >=2.32.5` | HTTP client for direct API calls (used in `kimi.py`) |

---

## Environment Variables

Secrets are loaded from a `.env` file in the project root via `python-dotenv`. **Never commit `.env` to version control.**

| Variable | Used in | Description |
|---|---|---|
| `NVIDIA_API_KEY` | `kimi.py` | API key for NVIDIA's inference endpoint |

Create a `.env` file:

```
NVIDIA_API_KEY=your_key_here
```

---

## Code Conventions

### Style
- Use **type annotations** on function signatures and module-level variables (see `main.py`).
- Follow PEP 8 naming: `snake_case` for functions and variables, `PascalCase` for classes.
- Avoid unused variables (e.g., `var_not_used` in `main.py` is a deliberate teaching example of what *not* to do).
- Use f-strings for string interpolation.
- Guard top-level script execution with `if __name__ == "__main__":`.

### AI/API Scripts
- Load all secrets via `os.getenv()` after calling `load_dotenv()`.
- Prefer streaming responses where the API supports it (see `kimi.py`'s `stream = True` pattern).
- Keep API payloads explicit — do not rely on provider defaults for temperature, max_tokens, etc.

---

## Common Tasks for AI Assistants

### Adding a new script
1. Create a new `.py` file at the project root.
2. Add any new third-party packages to `pyproject.toml` under `[project] dependencies`.
3. Run `uv sync` to update the lock file.
4. Load secrets from `.env`; never hard-code credentials.

### Modifying dependencies
- Edit `pyproject.toml` directly, then run `uv sync`.
- Do not manually edit `uv.lock` (if present).

### Running existing scripts
```bash
uv run main.py
uv run kimi.py
```

### Testing
There is no formal test suite yet. Manual execution is the current validation method. When adding tests, prefer `pytest` and add it to `pyproject.toml` as a dev dependency.

---

## Git Workflow

- Default branch: `main` (remote: `origin/main`)
- Feature branches follow the pattern: `claude/<description>-<id>`
- Commit messages are short and descriptive (imperative mood, e.g., "add kimi streaming example")
- Push with: `git push -u origin <branch-name>`

---

## What This Repo Is Not

- It is **not** a production application — scripts are illustrative examples for a course.
- It does **not** have CI/CD, linting configuration, or a test suite (yet).
- Avoid over-engineering: keep new examples simple and focused on the concept being demonstrated.
