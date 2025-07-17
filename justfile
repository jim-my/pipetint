# Tinty Development Justfile
# Run with: just <command>

# Show available commands
default:
    @just --list

# Development setup
setup:
    pip install -e ".[dev]"
    pre-commit install

# Development setup with Poetry
setup-poetry:
    poetry install --with dev
    poetry run pre-commit install

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

# Build package with Poetry
build-poetry: clean
    poetry build

# Build and check package
build-check: build
    twine check dist/*

# Build package with Poetry (check via regular build-check if needed)
build-check-poetry: build-poetry
    @echo "✅ Poetry build complete. Use 'just build-check' for validation if needed."

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

# Generate terminal screenshots for README
screenshots:
    @echo "📸 Generating terminal screenshots for README..."
    @mkdir -p docs/images
    @echo "Running basic colors example..."
    python -c "from tinty import colored, C, RED, GREEN, BLUE, YELLOW, BOLD; print(colored('Success') | GREEN | BOLD); print(colored('Warning') | YELLOW); print(colored('Error') | RED | BOLD); print(colored('Info') | BLUE)"
    @echo ""
    @echo "Running CLI pattern highlighting examples..."
    echo "hello world" | tinty 'l.*' yellow
    echo "hello world" | tinty '(ll).*(ld)' red,bg_blue blue,bg_red
    @echo ""
    @echo "Running complex styling example..."
    python -c "from tinty import colored, RED, BOLD, BG_WHITE, BLUE, YELLOW, DIM; print(colored('SYSTEM ALERT') | RED | BOLD | BG_WHITE); print(str(colored('DEBUG') | DIM) + ' - Application started'); print(str(colored('INFO') | BLUE) + ' - User logged in'); print(str(colored('WARNING') | YELLOW | BOLD) + ' - Memory usage high'); print(str(colored('ERROR') | RED | BOLD) + ' - Database connection failed')"
    @echo ""
    @echo "Running pattern highlighting example..."
    python -c "from tinty import colored; text = 'The quick brown fox jumps over the lazy dog'; highlighted = colored(text).highlight(r'(quick)|(fox)|(lazy)', ['red', 'blue', 'green']); print(highlighted)"
    @echo ""
    @echo "💡 To capture these as images:"
    @echo "1. Run: just screenshots > output.txt"
    @echo "2. Use a terminal screenshot tool like 'termshot' or manually capture"
    @echo "3. Save screenshots to docs/images/ folder"
    @echo "4. Update README.md image URLs to point to your screenshots"

# Generate screenshot images with termshot
screenshots-capture: screenshots-create-scripts
    @echo "📸 Capturing screenshots with termshot..."
    @echo "Capturing basic colors example..."
    termshot --filename docs/images/basic-colors.png --columns 80 python scripts/basic_colors.py
    @echo "Capturing CLI pattern highlighting examples..."
    termshot --filename docs/images/cli-examples.png --columns 80 scripts/cli_examples.sh
    @echo "Capturing complex styling example..."
    termshot --filename docs/images/complex-styling.png --columns 80 python scripts/complex_styling.py
    @echo "Capturing pattern highlighting example..."
    termshot --filename docs/images/pattern-highlighting.png --columns 80 python scripts/pattern_highlighting.py
    @echo "✅ Screenshots saved to docs/images/"

# Create script files for termshot
screenshots-create-scripts:
    @mkdir -p docs/images scripts
    @echo 'from tinty import colored, C, RED, GREEN, BLUE, YELLOW, BOLD\nprint(colored("Success") | GREEN | BOLD)\nprint(colored("Warning") | YELLOW)\nprint(colored("Error") | RED | BOLD)\nprint(colored("Info") | BLUE)' > scripts/basic_colors.py
    @echo '#!/bin/bash\necho "hello world" | tinty "l.*" yellow\necho "hello world" | tinty "(ll).*(ld)" red,bg_blue blue,bg_red' > scripts/cli_examples.sh
    @echo 'from tinty import colored, RED, BOLD, BG_WHITE, BLUE, YELLOW, DIM\nprint(colored("SYSTEM ALERT") | RED | BOLD | BG_WHITE)\nprint(str(colored("DEBUG") | DIM) + " - Application started")\nprint(str(colored("INFO") | BLUE) + " - User logged in")\nprint(str(colored("WARNING") | YELLOW | BOLD) + " - Memory usage high")\nprint(str(colored("ERROR") | RED | BOLD) + " - Database connection failed")' > scripts/complex_styling.py
    @echo 'from tinty import colored\ntext = "The quick brown fox jumps over the lazy dog"\nhighlighted = colored(text).highlight(r"(quick)|(fox)|(lazy)", ["red", "blue", "green"])\nprint(highlighted)' > scripts/pattern_highlighting.py
    chmod +x scripts/cli_examples.sh
