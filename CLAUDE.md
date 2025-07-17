# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python library for terminal text colorization and highlighting, inspired by the Ruby colorize gem. It provides ANSI color code functionality for Python strings with a modern development setup.

## Architecture

The project follows modern Python packaging standards with the following structure:

- **src/colorize/**: Main package directory
  - `color_codes.py`: Core ANSI color code definitions and ColorManager class
  - `colorize.py`: Main Colorize class and ColorizedString implementation
  - `string_extensions.py`: String extension methods and monkey patching
  - `cli.py`: Command-line interface implementation
- **tests/**: Comprehensive test suite with pytest
- **examples/**: Demonstration scripts
- **pyproject.toml**: Modern Python project configuration

## Key Features

- **Color methods**: All standard ANSI colors available as methods (e.g., `"text".red`, `"text".bg_blue`)
- **Pattern highlighting**: `highlight(pattern, colors)` method for regex-based colorization
- **Color removal**: `remove_color` method to strip ANSI codes
- **Random colors**: `colorize_random` for random color selection
- **Position-based highlighting**: `highlight_at(positions, color)` for specific character positions
- **CLI interface**: Command-line tool compatible with original Ruby version

## Code Best Practices

### Naming Conventions
- Use descriptive variable names in all cases
- Exceptions for very small local scopes (2-3 lines):
  - Loop indices: `i`, `j`, `k`
  - Standard short names when context is clear: `item`, `user`, `result`
  - Avoid generic names like `tmp`, `temp`, `data` - be specific about what the variable contains

### Version Control & Workflow
- Always run pre-commit hooks before `git add`
- Use feature branches for all development (never commit directly to main/master)
- Follow modern GitHub workflow: ticket → feature branch → PR → GitHub Actions → merge → close ticket cycle
- Write clear commit messages and PR descriptions
- Make small, focused commits (single logical change per commit)

### Python Tooling (Modern Stack)
- **Formatting & Linting**: Use `ruff --preview` instead of Black + isort + flake8
- **Type Checking**: Use `mypy` for static type analysis
- **Package Management**: Prefer `poetry` or `uv` over `pip`

### General Development
- Follow TDD rhythm: Red → Green → Refactor
- Write tests for new features and bug fixes
- Use type hints where appropriate
- Follow language-specific style guides (PEP 8 for Python, etc.)
- Document complex logic with clear comments

## Development Workflow

### Pre-commit Requirements

**IMPORTANT**: Always run pre-commit hooks before staging changes:

```bash
# Run all pre-commit hooks (includes formatting, linting, security checks)
pre-commit run --all-files

# Then stage and commit
git add -A
git commit -m "Your commit message"
```

For faster workflow on changed files only:

```bash
# Run pre-commit on staged/changed files only
pre-commit run

# Then stage and commit
git add -A
git commit -m "Your commit message"
```

### Testing

Run the test suite:
```bash
pytest
```

With coverage:
```bash
pytest --cov=colorize
```

### Linting and Formatting

The project uses modern tooling:
- **Ruff**: For linting and formatting (replaces Black, isort, flake8)
- **MyPy**: For type checking
- **Bandit**: For security scanning
- **Pre-commit**: Automated quality checks

Run linting:
```bash
ruff check --preview .
ruff format --preview .
```

### Pre-commit Hooks

The project uses pre-commit hooks for quality assurance:
```bash
pre-commit run --all-files
```

## Installation and Usage

### As a Library

```python
from colorize import Colorize, ColorizedString

# Basic usage
colorizer = Colorize()
colored_text = colorizer.colorize("Hello", "red")

# String methods
cs = ColorizedString("Hello World")
result = cs.red
highlighted = cs.highlight(r"World", ["blue"])
```

### Command Line

```bash
# Basic usage
echo "hello world" | colorize 'l' red

# Pattern highlighting
echo "hello world" | colorize '(h.*o).*(w.*d)' red blue

# List available colors
colorize --list-colors
```

## Project Configuration

- **Python version**: 3.9+
- **Package manager**: pip/uv
- **Build system**: setuptools with setuptools_scm
- **Test framework**: pytest
- **Type checking**: MyPy
- **Code quality**: Ruff (preview mode enabled)
- **CI/CD**: GitHub Actions

## Development Notes

- Uses src/ layout for proper package structure
- Comprehensive type hints throughout
- Modern pyproject.toml configuration
- Pre-commit hooks ensure code quality
- Preview mode enabled for Ruff to access latest rules
- Per-file ignores configured for appropriate flexibility
