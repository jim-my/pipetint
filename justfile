# Tinty Development Justfile
# Run with: just <command>

# Show available commands
default:
    @just --list

# Development setup
setup:
    pip install -e .
    pip install -r requirements-dev.txt || echo "No requirements-dev.txt found"
    pre-commit install

# Run tests
test:
    pytest

# Run tests with coverage
test-cov:
    pytest --cov=tinty --cov-report=html --cov-report=term

# Run type checking
typecheck:
    mypy src/

# Run linting and formatting
lint:
    ruff check --preview .

# Auto-fix linting issues
lint-fix:
    ruff check --preview --fix .

# Format code
format:
    ruff format --preview .

# Run all quality checks
check: lint typecheck test

# Run pre-commit hooks on all files
pre-commit:
    pre-commit run --all-files

# Clean build artifacts
clean:
    rm -rf build/ dist/ *.egg-info/
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Build package
build: clean
    python -m build

# Build and check package
build-check: build
    twine check dist/*

# Install package locally in development mode
install-dev:
    pip install -e .

# Run example scripts
example script="quickstart":
    python examples/{{script}}.py

# Run CLI help
cli-help:
    tinty --help

# Test CLI functionality
cli-test:
    echo "hello world" | tinty 'l' red

# Create a new release (requires version bump)
release: check build-check
    @echo "Ready to release! Run: just publish-test or just publish"

# Publish to test PyPI
publish-test: build
    twine upload --repository testpypi dist/*

# Publish to PyPI (PRODUCTION)
publish: build
    twine upload dist/*

# Show package info
info:
    @echo "Package: tinty"
    @echo "Version: $(python -c 'import tinty; print(tinty.__version__)' 2>/dev/null || echo 'not installed')"
    @echo "Location: $(python -c 'import tinty; print(tinty.__file__)' 2>/dev/null || echo 'not found')"

# Show available colors demo
demo:
    python -c "from tinty import C, RED, GREEN, BLUE, BOLD; print(C('✅ Tinty works!') | GREEN | BOLD)"
