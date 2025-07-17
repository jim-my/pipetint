# Colorize

A Python library for terminal text colorization and highlighting, inspired by the Ruby colorize gem. Now with a modern, production-safe API featuring Pathlib-inspired operator chaining!

![CI](https://github.com/jimmyyan/colorize/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/jimmyyan/colorize/branch/main/graph/badge.svg)](https://codecov.io/gh/jimmyyan/colorize)
[![PyPI version](https://badge.fury.io/py/colorize.svg)](https://badge.fury.io/py/colorize)
[![Python versions](https://img.shields.io/pypi/pyversions/colorize.svg)](https://pypi.org/project/colorize)

## ✨ Features

- **🔒 Production Safe**: No monkey patching or global state pollution
- **🎯 Multiple APIs**: Choose your preferred style - fluent, functional, or global
- **🔗 Pathlib-inspired**: Elegant operator chaining with `|` and `>>` operators
- **🌈 Comprehensive**: Support for all ANSI colors, backgrounds, and text styles
- **⚡ High Performance**: Efficient implementation with minimal overhead
- **🧪 Well Tested**: Comprehensive test suite with 100+ tests
- **📦 Zero Dependencies**: Pure Python implementation
- **🖥️ Cross Platform**: Works on Linux, macOS, and Windows
- **🛠️ CLI Tool**: Command-line interface for colorizing text

## 🚀 Installation

```bash
pip install colorize
```

## 🎨 Quick Start

### Modern Enhanced API (Recommended)

```python
from colorize import colored, C, txt, RED, GREEN, BLUE, BOLD, BG_WHITE, UNDERLINE

# Factory functions with method chaining
print(colored("Success").green().bold())
print(txt("Warning").yellow())

# Type-safe constants with operator chaining (RECOMMENDED)
print(colored("Error") | RED | BOLD | BG_WHITE)
print(txt("Info") >> BLUE >> UNDERLINE)

# Old way with string literals (error-prone)
print(colored("Error") | "red" | "typo")  # "typo" causes runtime error

# Global convenience object
print(C.green("✓ Tests passing"))
print(C.red("✗ Build failed"))
print(C("Processing...") | BLUE | BOLD)
```

### Real-World Examples

```python
from colorize import colored, C, txt, ColorString

# Log levels
print(C("DEBUG", "dim") + " - Application started")
print(colored("INFO").blue() + " - User logged in")
print(txt("WARNING") | "yellow" | "bright" + " - Memory usage high")
print(ColorString("ERROR").red().bold() + " - Database connection failed")

# CLI status indicators
print(f"{C.green('✓')} File saved successfully")
print(f"{C.yellow('⚠')} Configuration outdated")
print(f"{C.red('✗')} Permission denied")

# Complex chaining
alert = (colored("SYSTEM ALERT")
         .red()
         .bold()
         .bg_white()
         | "blink")
print(alert)
```

### Pattern Highlighting

```python
from colorize import colored

# Highlight search terms
text = "The quick brown fox jumps over the lazy dog"
highlighted = colored(text).highlight(r"(quick|fox|lazy)", ["red", "blue", "green"])
print(highlighted)

# Syntax highlighting
code = "def hello_world():"
result = colored(code).highlight(r"\b(def)\b", ["blue"])
print(result)
```

## 📋 Available Colors and Styles

### Foreground Colors
`red`, `green`, `blue`, `yellow`, `magenta`, `cyan`, `white`, `black`, `lightred`, `lightgreen`, `lightblue`, `lightyellow`, `lightmagenta`, `lightcyan`, `lightgray`, `darkgray`

### Background Colors
`bg_red`, `bg_green`, `bg_blue`, `bg_yellow`, `bg_magenta`, `bg_cyan`, `bg_white`, `bg_black`, `bg_lightred`, `bg_lightgreen`, `bg_lightblue`, `bg_lightyellow`, `bg_lightmagenta`, `bg_lightcyan`, `bg_lightgray`, `bg_darkgray`

### Text Styles
`bright`/`bold`, `dim`, `underline`, `blink`, `invert`/`swapcolor`, `hidden`, `strikethrough`

## 🔒 Type-Safe Color Constants (New!)

Use constants instead of error-prone string literals:

```python
from colorize import colored, RED, GREEN, BLUE, YELLOW, BOLD, BG_WHITE

# ✅ Type-safe with IDE autocompletion and error checking
error_msg = colored("CRITICAL") | RED | BOLD | BG_WHITE
success_msg = colored("SUCCESS") | GREEN | BOLD
warning_msg = colored("WARNING") | YELLOW

# ❌ Error-prone string literals  
error_msg = colored("CRITICAL") | "red" | "typo"  # Runtime error!
```

**Benefits:**
- 🔍 **IDE Autocompletion**: Get suggestions for valid colors
- 🛡️ **Type Checking**: Catch typos at development time  
- 📝 **Self-Documenting**: Clear, readable code
- 🔄 **Refactoring Safe**: Rename constants across codebase
- ⚡ **No Runtime Errors**: Invalid colors caught early

**Available Constants:**
- **Colors**: `RED`, `GREEN`, `BLUE`, `YELLOW`, `MAGENTA`, `CYAN`, `WHITE`, `BLACK`
- **Light Colors**: `LIGHTRED`, `LIGHTGREEN`, `LIGHTBLUE`, etc.
- **Backgrounds**: `BG_RED`, `BG_GREEN`, `BG_BLUE`, etc.
- **Styles**: `BOLD`, `BRIGHT`, `DIM`, `UNDERLINE`, `BLINK`, `INVERT`

## 🎭 API Styles

Choose the style that fits your needs:

### 1. Factory Functions
```python
from colorize import colored, txt

colored("hello").red().bold()
txt("world") | "blue" | "underline"
```

### 2. Global Object
```python
from colorize import C

C.red("hello")              # Direct color application
C("hello").red().bold()     # Factory with chaining
C("hello", "red")           # Direct colorization
```

### 3. Enhanced ColorString
```python
from colorize import ColorString

ColorString("hello").red() | "bold" | "bg_yellow"
```

### 4. Operator Chaining (Pathlib-inspired)
```python
# Using | operator (like Pathlib's /)
colored("Error") | "red" | "bright" | "bg_white"

# Using >> operator
txt("Success") >> "green" >> "bold" >> "underline"

# Mixing operators
((colored("Mixed") | "red") >> "bright") | "bg_yellow"
```

## 🛠️ Command Line Interface

```bash
# Basic usage
echo "hello world" | colorize 'l' red

# Pattern highlighting with groups
echo "hello world" | colorize '(h.*o).*(w.*d)' red blue

# List available colors
colorize --list-colors

# Case sensitive matching
echo "Hello World" | colorize --case-sensitive 'Hello' green
```

## 🔄 Legacy API (Still Supported)

The original API remains fully supported for backward compatibility:

```python
from colorize import Colorize, ColorizedString

# Original Colorize class
colorizer = Colorize()
print(colorizer.colorize("hello", "red"))

# Original ColorizedString
cs = ColorizedString("hello")
print(cs.colorize("blue"))
```

## 🧪 Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=colorize

# Run specific test file
pytest tests/test_enhanced.py
```

### Code Quality

```bash
# Format and lint
ruff format --preview .
ruff check --preview .

# Type checking
mypy src/

# Run pre-commit hooks
pre-commit run --all-files
```

## 📖 Examples

See the `examples/` directory for more comprehensive examples:

- `examples/quickstart.py` - Basic usage patterns
- `examples/enhanced_demo.py` - Full enhanced API demonstration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Make sure to:

1. Run the pre-commit hooks: `pre-commit run --all-files`
2. Add tests for new features
3. Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the Ruby [colorize](https://github.com/fazibear/colorize) gem
- Built with modern Python best practices
- Designed for production safety and developer experience
