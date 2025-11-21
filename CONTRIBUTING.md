# Contributing to PipeTint

Thank you for your interest in contributing to PipeTint! This document provides guidelines and instructions for contributing.

---

## 🎯 Quick Start

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/pipetint.git
cd pipetint

# 2. Set up development environment
poetry install --with dev
poetry run pre-commit install

# 3. Create a feature branch
git checkout -b feature/amazing-feature

# 4. Make your changes and add tests
# ... code code code ...

# 5. Run tests and quality checks
poetry run pytest
poetry run pre-commit run --all-files

# 6. Commit and push
git commit -m "feat: add amazing feature"
git push origin feature/amazing-feature

# 7. Create a Pull Request
# Go to GitHub and create a PR from your branch
```

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

This project adheres to a Code of Conduct that we expect all contributors to follow:

- **Be respectful**: Treat everyone with respect and kindness
- **Be constructive**: Provide helpful feedback and suggestions
- **Be collaborative**: Work together to improve the project
- **Be inclusive**: Welcome contributors of all backgrounds and skill levels

---

## 🤝 How Can I Contribute?

### Reporting Bugs

Before submitting a bug report:
- Check the [existing issues](https://github.com/jim-my/pipetint/issues)
- Try the latest version from `main` branch
- Collect information about your environment

**Good bug reports include**:
- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Code samples or test cases
- Environment details (OS, Python version, terminal)

**Bug report template**:
```markdown
**Description**
A clear description of the bug.

**To Reproduce**
Steps to reproduce:
1. Run command: `echo "test" | pipetint 'pattern' red`
2. Observe output: ...
3. Expected: ...

**Environment**
- OS: macOS 14.0
- Python: 3.11.5
- PipeTint: 1.0.0
- Terminal: iTerm2 3.4.19

**Additional Context**
Any other relevant information.
```

### Suggesting Features

Feature suggestions are welcome! Before submitting:
- Check the [roadmap](ROADMAP.md) for planned features
- Search existing feature requests
- Consider if it fits PipeTint's philosophy (simplicity, zero dependencies, Unix philosophy)

**Good feature requests include**:
- Clear use case and motivation
- Proposed API or CLI interface
- Examples of how it would be used
- Consideration of alternatives

### Improving Documentation

Documentation improvements are always appreciated:
- Fix typos or unclear explanations
- Add examples for existing features
- Improve README organization
- Write tutorials or guides
- Update docstrings

### Contributing Code

See the sections below for detailed guidelines on coding standards, testing, and the PR process.

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.9 or higher
- Poetry (recommended) or pip
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/jim-my/pipetint.git
cd pipetint

# Install with Poetry (recommended)
poetry install --with dev
poetry run pre-commit install

# Or with pip
pip install -e ".[dev]"
pre-commit install
```

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=pipetint --cov-report=html --cov-report=term

# Run specific test file
poetry run pytest tests/test_nesting.py

# Run specific test
poetry run pytest tests/test_nesting.py::TestColorNesting::test_nested_regex_groups_foreground
```

### Code Quality Checks

```bash
# Run all pre-commit hooks
poetry run pre-commit run --all-files

# Individual tools
poetry run ruff check --preview .       # Linting
poetry run ruff format --preview .      # Formatting
poetry run mypy src/                    # Type checking
poetry run bandit -r src/               # Security scanning
```

### Using Justfile

The project includes a `justfile` for common tasks:

```bash
# Show available commands
just

# Run tests with coverage
just test-cov

# Run all quality checks
just check

# Format and lint code
just lint-fix
just format

# Build package
just build-poetry
```

---

## 📏 Coding Standards

### Python Style

We follow modern Python best practices:

- **PEP 8** for code style
- **Type hints** for all functions and methods
- **Docstrings** for public APIs (Google style)
- **Ruff** for linting and formatting (with `--preview` flag enabled)

### Code Organization

```
pipetint/
├── src/pipetint/          # Main package
│   ├── pipetint.py       # Core colorization logic
│   ├── cli.py         # Command-line interface
│   ├── colors.py      # Color constants
│   └── enhanced.py    # Enhanced API
├── tests/             # Test suite
│   ├── test_pipetint.py
│   ├── test_nesting.py
│   └── ...
├── examples/          # Example scripts
└── docs/             # Documentation
```

### Naming Conventions

- **Functions/Variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_CASE`
- **Private**: `_leading_underscore`
- **Protected**: `_single_underscore`

### Type Hints

```python
# Good ✅
def colorize(text: str, color: str) -> str:
    """Colorize text with ANSI codes."""
    return f"\033[{color}m{text}\033[0m"

# Bad ❌
def colorize(text, color):
    return f"\033[{color}m{text}\033[0m"
```

### Docstrings

Use Google-style docstrings:

```python
def highlight(
    self, pattern: Union[str, re.Pattern], colors: Union[str, list[str]]
) -> "ColorizedString":
    """Highlight text matching pattern with given colors.

    Args:
        pattern: Regular expression pattern or compiled regex
        colors: Single color or list of colors for capture groups

    Returns:
        New ColorizedString with highlights applied

    Examples:
        >>> text = ColorizedString("hello world")
        >>> result = text.highlight(r'world', ['blue'])
        >>> print(result)
        hello \033[34mworld\033[0m
    """
    ...
```

---

## 🧪 Testing Guidelines

### Test Requirements

- **All new features** must have tests
- **All bug fixes** must have regression tests
- **Coverage** should not decrease (currently 90%+)
- **Tests must pass** before merging

### Test Structure

```python
"""Tests for color nesting functionality."""

import pytest
from pipetint import ColorizedString


class TestColorNesting:
    """Test color nesting with priority resolution."""

    def test_nested_regex_groups_foreground(self):
        """Inner groups should override outer groups in same channel."""
        cs = ColorizedString("hello world")
        result = cs.highlight(r'(h.(ll))', ['red', 'blue'])

        # "he" should be red, "ll" should be blue
        result_str = str(result)
        assert '\x1b[31m' in result_str  # Red ANSI code
        assert '\x1b[34m' in result_str  # Blue ANSI code
```

### Test Categories

- **Unit tests**: Test individual functions/methods
- **Integration tests**: Test feature interactions
- **CLI tests**: Test command-line interface
- **Edge cases**: Empty strings, special characters, etc.

### Writing Good Tests

```python
# Good ✅ - Clear, focused, well-named
def test_nested_groups_inner_wins(self):
    """Inner capture groups should have higher priority than outer groups."""
    result = ColorizedString("hello").highlight(r'(h(e)llo)', ['red', 'blue'])
    assert 'blue' in get_color_at_position(result, 1)  # 'e' is blue, not red

# Bad ❌ - Vague, multiple assertions, unclear
def test_colors(self):
    """Test colors."""
    result = ColorizedString("test").highlight(r'test', ['red'])
    assert result  # What are we actually testing?
```

---

## 📝 Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

### Examples

```bash
# Good ✅
feat(cli): add --theme flag for built-in color schemes
fix(nesting): correct priority calculation for nested groups
docs(readme): add examples for pipeline composition
test(nesting): add tests for triple-nested regex groups

# Bad ❌
update stuff
fix bug
WIP
asdf
```

### Detailed Example

```
feat(config): add YAML configuration file support

Implement .pipetintrc.yaml configuration file that allows users to save
common color patterns and reuse them without retyping commands.

Features:
- Config file discovery in standard locations
- Named rule sets
- Environment-specific overrides

Closes #42
```

---

## 🔄 Pull Request Process

### Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass: `pytest`
- [ ] Pre-commit hooks pass: `pre-commit run --all-files`
- [ ] Documentation is updated (if needed)
- [ ] CHANGELOG.md is updated (for features/fixes)
- [ ] Commit messages follow conventions

### PR Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Testing
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Manual testing performed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added that prove fix/feature works
- [ ] All dependent changes merged and published
```

### Review Process

1. **Automated checks** run (tests, linting, coverage)
2. **Maintainer review** (usually within 2-3 days)
3. **Feedback addressed** (if any)
4. **Approval and merge**

### What Happens After Merge

- PR is merged to `main` branch
- Automated tests run on `main`
- Changes included in next release
- Contributor added to CONTRIBUTORS list

---

## 🎓 Learning Resources

### Project-Specific

- [README.md](README.md) - Project overview and features
- [ROADMAP.md](ROADMAP.md) - Future plans and direction
- [Architecture Documentation](NESTING_DOCS.md) - Technical deep-dive

### Python Development

- [PEP 8](https://pep8.org/) - Python style guide
- [Type Hints](https://docs.python.org/3/library/typing.html) - Python typing
- [pytest](https://docs.pytest.org/) - Testing framework
- [Ruff](https://docs.astral.sh/ruff/) - Linting and formatting

### Terminal/ANSI

- [ANSI Escape Codes](https://en.wikipedia.org/wiki/ANSI_escape_code)
- [Terminal Colors](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797)

---

## 💬 Getting Help

- **Questions**: Open a [GitHub Discussion](https://github.com/jim-my/pipetint/discussions)
- **Bugs**: Open a [GitHub Issue](https://github.com/jim-my/pipetint/issues)
- **Chat**: Join our community (link TBD)

---

## 🏆 Recognition

Contributors are recognized in:
- [CONTRIBUTORS.md](CONTRIBUTORS.md) (automatically generated)
- GitHub contributors page
- Release notes for their contributions

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to PipeTint! 🎨**
