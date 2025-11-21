# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.1] - 2025-01-22

### Documentation

- Fixed remaining capitalized Tinty → PipeTint references in README and documentation
- Updated all GitHub repository URLs from jim-my/tinty to jim-my/pipetint
- Updated CHANGELOG comparison URLs to point to pipetint repository
- Updated README badges to point to pipetint repository

---

## [2.0.0] - 2025-01-22

### 💥 BREAKING CHANGES

This release renames the package from "tinty" to "pipetint" to avoid conflicts with existing projects and better reflect the tool's purpose.

**Migration Guide:**

1. **Uninstall old package:**
   ```bash
   pip uninstall tinty
   ```

2. **Install new package:**
   ```bash
   pip install pipetint
   ```

3. **Update imports:**
   ```python
   # Old
   from tinty import ColorizedString, colored

   # New
   from pipetint import ColorizedString, colored
   ```

4. **Update CLI usage:**
   ```bash
   # Old
   echo "test" | tinty 'pattern' red

   # New
   echo "test" | pipetint 'pattern' red
   ```

5. **Update git remote (for contributors):**
   ```bash
   git remote set-url origin git@github.com:jim-my/pipetint.git
   ```

### Changed

- Package renamed from `tinty` to `pipetint`
- CLI command renamed from `tinty` to `pipetint`
- GitHub repository renamed to `jim-my/pipetint`
- All imports changed from `from tinty` to `from pipetint`

**Note:** All functionality remains identical - this is purely a naming change.

---

## [1.0.0] - 2025-01-20

### 🎉 First Stable Release

This release marks PipeTint as production-ready with a stable API and unique features not found in any other terminal colorizer.

### ✨ Unique Features

- **Smart Color Nesting**: Automatic priority-based rendering without manual z-index configuration
- **Pipeline Composition**: Colors preserved across pipeline stages with intelligent priority resolution
- **Channel Isolation**: Foreground, background, and attributes work independently
- **ANSI-Aware Pattern Matching**: Patterns match original text, ignoring existing ANSI codes

### 🎯 Production Ready

- 143 comprehensive tests with full coverage
- Type hints throughout the codebase
- Zero dependencies - pure Python implementation
- Comprehensive documentation with real-world examples
- Published to PyPI and TestPyPI

### 📝 API Commitment

With v1.0.0, we commit to:
- Semantic versioning for all future releases
- Backwards compatibility for all public APIs
- Deprecation warnings before removing features
- Clear migration guides for breaking changes (if any in v2.0+)

---

## [0.2.0] - 2025-01-20

### Added

- **Color Nesting with Priority-Based Rendering** (#1)
  - Automatic priority calculation based on pipeline stage, nesting depth, and application order
  - Channel isolation (foreground, background, attributes)
  - Deferred rendering architecture with ColorRange dataclass
  - Nesting depth calculation for regex capture groups

- **ANSI Code Parsing for Pipeline Support**
  - Full ANSI escape sequence parsing to reconstruct ColorRange objects
  - Reverse mapping from ANSI codes to color names
  - Automatic pipeline stage incrementing for proper priority
  - Colors preserved across pipeline stages

- **Color Name Normalization**
  - Support for both `bg_red` and `red_bg` formats
  - Automatic normalization to standard format
  - Case-insensitive color name handling

- **--replace-all CLI Flag**
  - Explicit control to clear all previous colors before applying new ones
  - Useful for starting fresh in pipeline stages
  - Verbose mode shows when colors are cleared

### Documentation

- Comprehensive README updates with Advanced Color Nesting section
- Real-world use cases (log highlighting, syntax highlighting, multi-stage processing)
- CLI examples with nesting patterns
- Screenshot generation scripts
- NESTING_DOCS.md with detailed examples

### Tests

- 16 new tests for color nesting behavior
- 10 new tests for color name normalization
- 2 new tests for --replace-all flag
- All 143 tests passing (131 original + 12 new)

---

## [0.1.10] - 2024-XX-XX

### Changed

- Updated help message formatting
- Improved CLI error handling

---

## [0.1.9] - 2024-XX-XX

### Changed

- Version bump for distribution updates

---

## [0.1.4] - 2024-XX-XX

### Changed

- Version bump and version file generation fixes

---

## [0.1.3] - 2024-XX-XX

### Added

- Initial public release with basic colorization features
- CLI tool for pattern-based text colorization
- Python library with multiple API styles
- Type-safe color constants
- Pattern highlighting with regex support
- Comprehensive test suite

### Features

- Multiple APIs (fluent, functional, global)
- Pathlib-inspired operator chaining
- Support for all ANSI colors, backgrounds, and text styles
- Zero dependencies
- Cross-platform support

---

[2.0.1]: https://github.com/jim-my/pipetint/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/jim-my/pipetint/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/jim-my/pipetint/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/jim-my/pipetint/compare/v0.1.10...v0.2.0
[0.1.10]: https://github.com/jim-my/pipetint/compare/v0.1.9...v0.1.10
[0.1.9]: https://github.com/jim-my/pipetint/compare/v0.1.4...v0.1.9
[0.1.4]: https://github.com/jim-my/pipetint/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/jim-my/pipetint/releases/tag/v0.1.3
