"""Tests for config loading and resolution."""

from pathlib import Path

import pytest

from pipetint.config import (
    ConfigError,
    discover_config_path,
    load_config,
    resolve_selected_rules,
)


def write_config(path: Path, content: str) -> None:
    """Write config content to a path."""
    path.write_text(content, encoding="utf-8")


class TestDiscoverConfigPath:
    """Test config file discovery."""

    def test_explicit_path_overrides_discovery(self, tmp_path: Path) -> None:
        """Explicit config path should win over implicit paths."""
        explicit = tmp_path / "explicit.toml"
        project = tmp_path / "pipetint.toml"
        user = tmp_path / "user.toml"
        write_config(explicit, "version = 1\n")
        write_config(project, "version = 1\n")
        write_config(user, "version = 1\n")

        result = discover_config_path(
            explicit_path=explicit,
            cwd=tmp_path,
            user_config_path=user,
        )

        assert result == explicit

    def test_project_config_overrides_user_config(self, tmp_path: Path) -> None:
        """Project config should win when no explicit path is set."""
        project = tmp_path / "pipetint.toml"
        user = tmp_path / "user.toml"
        write_config(project, "version = 1\n")
        write_config(user, "version = 1\n")

        result = discover_config_path(cwd=tmp_path, user_config_path=user)

        assert result == project


class TestLoadConfig:
    """Test config parsing and validation."""

    def test_load_config_parses_rules_and_themes(self, tmp_path: Path) -> None:
        """Valid config should load named rules and themes."""
        config_path = tmp_path / "pipetint.toml"
        write_config(
            config_path,
            """
version = 1
default_rules = ["timestamps"]

[[rules]]
name = "timestamps"
pattern = "\\\\d{2}:\\\\d{2}:\\\\d{2}"
colors = ["blue"]

[themes.log-levels]
description = "Common log levels"
rules = ["timestamps"]
""".strip()
            + "\n",
        )

        config = load_config(config_path)

        assert config["version"] == 1
        assert config["default_rules"] == ["timestamps"]
        assert config["rules"]["timestamps"]["colors"] == ["blue"]
        assert config["themes"]["log-levels"]["rules"] == ["timestamps"]

    def test_load_config_rejects_unknown_color(self, tmp_path: Path) -> None:
        """Unknown color names should raise a validation error."""
        config_path = tmp_path / "pipetint.toml"
        write_config(
            config_path,
            """
version = 1

[[rules]]
name = "bad-rule"
pattern = "ERROR"
colors = ["not_a_real_color"]
""".strip()
            + "\n",
        )

        with pytest.raises(ConfigError, match="Unknown color"):
            load_config(config_path)

    def test_load_config_rejects_missing_theme_rule(self, tmp_path: Path) -> None:
        """Themes should not reference undefined rule names."""
        config_path = tmp_path / "pipetint.toml"
        write_config(
            config_path,
            """
version = 1

[themes.log-levels]
rules = ["missing-rule"]
""".strip()
            + "\n",
        )

        with pytest.raises(ConfigError, match="undefined rule"):
            load_config(config_path)


class TestResolveSelectedRules:
    """Test selection order and explicit rule resolution."""

    def test_resolve_selected_rules_expands_theme_defaults_then_explicit(
        self, tmp_path: Path
    ) -> None:
        """Explicit rules should be appended after theme and defaults."""
        config_path = tmp_path / "pipetint.toml"
        write_config(
            config_path,
            """
version = 1
default_rules = ["timestamps"]

[[rules]]
name = "timestamps"
pattern = "\\\\d{2}:\\\\d{2}:\\\\d{2}"
colors = ["blue"]

[[rules]]
name = "errors"
pattern = "ERROR"
colors = ["red", "bold"]

[themes.log-levels]
rules = ["errors"]
""".strip()
            + "\n",
        )
        config = load_config(config_path)

        resolved = resolve_selected_rules(
            config,
            theme_name="log-levels",
            selected_rule_names=["timestamps"],
        )

        resolved_names = [rule["name"] for rule in resolved]

        assert resolved_names == ["errors", "timestamps", "timestamps"]

    def test_resolve_selected_rules_rejects_unknown_rule(self, tmp_path: Path) -> None:
        """Unknown selected rules should raise a clear error."""
        config_path = tmp_path / "pipetint.toml"
        write_config(
            config_path,
            """
version = 1

[[rules]]
name = "errors"
pattern = "ERROR"
colors = ["red"]
""".strip()
            + "\n",
        )
        config = load_config(config_path)

        with pytest.raises(ConfigError, match="Unknown rule"):
            resolve_selected_rules(config, selected_rule_names=["missing"])
