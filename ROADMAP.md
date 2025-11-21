# Roadmap

This document outlines the planned features and future direction for Tinty.

---

## 🎯 Vision

Tinty aims to be the **most powerful and user-friendly terminal colorizer** with unique features like smart color nesting and pipeline composition, while maintaining simplicity and zero dependencies.

---

## ✅ Completed (v1.0.0)

- [x] Smart color nesting with automatic priority resolution
- [x] Pipeline composition with color preservation
- [x] Channel isolation (foreground/background/attributes)
- [x] ANSI-aware pattern matching
- [x] Type-safe color constants
- [x] Multiple API styles (fluent, functional, global)
- [x] Comprehensive documentation and examples
- [x] 143 tests with full coverage
- [x] CLI with standard options (--verbose, --case-sensitive, --replace-all)
- [x] Color name normalization (bg_red / red_bg)
- [x] Zero dependencies

---

## 🚀 Planned Features

### v1.1 - Configuration File Support (Q1 2025)

**Goal**: Allow users to save common patterns and reuse them without retyping.

**Features**:
- YAML configuration file (.pipetintrc.yaml)
- Standard locations: `~/.pipetintrc`, `./.pipetintrc`, `$XDG_CONFIG_HOME/pipetint/config.yaml`
- Named rule sets for different use cases
- Environment-specific overrides

**Example**:
```yaml
rules:
  - name: error-logs
    pattern: 'ERROR|CRITICAL'
    colors: [red, bold]

  - name: timestamps
    pattern: '\d{2}:\d{2}:\d{2}'
    colors: [blue]

  - name: ip-addresses
    pattern: '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    colors: [green]
```

**CLI Usage**:
```bash
# Use all rules from config
cat log.txt | pipetint --config

# Use specific rule set
cat log.txt | pipetint --rule error-logs,timestamps
```

---

### v1.2 - Built-in Themes (Q1 2025)

**Goal**: Provide ready-to-use color schemes for common use cases.

**Themes**:
- `log-levels` - ERROR=red, WARN=yellow, INFO=blue, DEBUG=gray
- `git-diff` - Added lines=green, removed=red, headers=cyan
- `python` - Basic Python syntax highlighting
- `json` - JSON structure highlighting
- `status-codes` - HTTP status codes (2xx=green, 4xx=yellow, 5xx=red)

**CLI Usage**:
```bash
# Use built-in theme
cat app.log | pipetint --theme log-levels

# List available themes
pipetint --list-themes

# Show theme details
pipetint --theme log-levels --show
```

**Python API**:
```python
from pipetint.themes import LogLevelsTheme

result = LogLevelsTheme().apply(log_text)
```

---

### v1.3 - TrueColor (24-bit RGB) Support (Q2 2025)

**Goal**: Support modern terminals with 24-bit color depth.

**Features**:
- Hex color codes: `#ff0000`, `#00ff00`, `#0000ff`
- RGB tuples: `rgb(255, 0, 0)`
- Color gradients: `gradient(#ff0000, #00ff00, #0000ff)`
- Fallback to 256-color for older terminals

**CLI Usage**:
```bash
# Hex colors
echo "gradient text" | pipetint 'gradient' '#ff0000,#00ff00,#0000ff'

# RGB colors
echo "colorful" | pipetint 'colorful' 'rgb(255,0,0)'

# Gradients
echo "rainbow" | pipetint '.' 'gradient(red, orange, yellow, green, blue, purple)'
```

**Python API**:
```python
from pipetint import ColorizedString

text = ColorizedString("rainbow")
result = text.highlight(r'.', gradient=['#ff0000', '#00ff00', '#0000ff'])
```

---

### v1.4 - Syntax Highlighting via Pygments (Q2 2025)

**Goal**: Professional syntax highlighting without manual regex patterns.

**Features**:
- Integration with Pygments library (optional dependency)
- Support for 500+ languages and file formats
- Customizable color schemes
- Auto-detect language from file extension

**CLI Usage**:
```bash
# Syntax highlight Python code
cat script.py | pipetint --syntax python

# Auto-detect from file
pipetint --syntax auto < script.py

# Custom color scheme
cat code.js | pipetint --syntax javascript --style monokai
```

**Python API**:
```python
from pipetint.syntax import highlight_code

result = highlight_code(code, language='python', style='monokai')
```

---

### v1.5 - Performance Optimizations (Q2 2025)

**Goal**: Optimize performance for large files and streaming data.

**Features**:
- Benchmarking suite vs. grep, ripgrep, colout
- PCRE2 regex engine support (optional, 2x faster)
- Pattern caching for repeated use
- Streaming mode for large files
- Parallel processing for multiple files

**CLI Usage**:
```bash
# Use PCRE2 for better performance
cat large.log | pipetint --engine pcre2 'pattern' red

# Streaming mode (don't buffer entire file)
tail -f app.log | pipetint --stream 'ERROR' red

# Benchmark against other tools
pipetint --benchmark
```

---

### v1.6 - Advanced Features (Q3 2025)

**Goal**: Add power-user features while maintaining simplicity.

**Features**:
- **Conditional coloring**: Color based on numeric thresholds
  ```bash
  # Color based on value ranges
  cat metrics.txt | pipetint --threshold 'cpu:\d+' '0-50:green,51-80:yellow,81-100:red'
  ```

- **Color interpolation**: Smooth gradients across text
  ```bash
  echo "gradient" | pipetint '.' --interpolate '#ff0000,#0000ff'
  ```

- **Named capture groups**: Reference groups by name
  ```bash
  echo "2025-01-20" | pipetint '(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})' 'year:blue,month:green,day:red'
  ```

- **Context-aware coloring**: Different colors based on surrounding text
  ```bash
  # Color "100" differently based on whether it's before "ms" or "GB"
  cat output.txt | pipetint --context
  ```

---

### v2.0 - Breaking Changes (Future)

**Note**: Only if absolutely necessary. We commit to maintaining v1.x backwards compatibility.

**Potential changes** (if community feedback suggests):
- API refinements based on user feedback
- Removal of deprecated features (with extensive migration guide)
- Performance improvements that require API changes

---

## 🔮 Ideas Under Consideration

These features are being evaluated but not yet committed:

- **Interactive mode**: Wrap interactive programs (like ChromaTerm)
  ```bash
  pipetint --interactive ssh user@host
  ```

- **Color picker**: Visual color selection tool
  ```bash
  pipetint --pick-color  # Opens TUI color picker
  ```

- **Export formats**: Export colored text to HTML, RTF, ANSI art
  ```bash
  cat code.py | pipetint --syntax python --export html > code.html
  ```

- **Plugin system**: Allow custom color processors
  ```python
  # Custom plugin for business logic
  from pipetint.plugins import ColorPlugin

  class CustomHighlighter(ColorPlugin):
      def process(self, text):
          # Custom highlighting logic
          return colored_text
  ```

- **Multi-language support**: Localized error messages and help text

- **GUI configuration tool**: Visual editor for creating .pipetintrc files

---

## 💬 Community Input

We welcome feedback on the roadmap! Please:

- 🌟 Star features you want to see prioritized
- 💡 Suggest new features via GitHub Issues
- 🐛 Report bugs and pain points
- 🤝 Contribute implementations

**Provide feedback**: https://github.com/jim-my/pipetint/issues

---

## 📊 Versioning Policy

- **Major version (v2.0)**: Breaking changes (rare, with migration guide)
- **Minor version (v1.x)**: New features, backwards compatible
- **Patch version (v1.1.x)**: Bug fixes, no API changes

---

## 🎯 Guiding Principles

All future development follows these principles:

1. **Simplicity First**: Features should be easy to use and understand
2. **Zero Dependencies**: Core functionality stays pure Python
3. **Backwards Compatible**: Don't break existing users
4. **Performance Matters**: Fast enough for real-time use
5. **Unix Philosophy**: Do one thing well, compose with other tools
6. **Community Driven**: Listen to user feedback and needs

---

**Last Updated**: 2025-01-20
