"""Config discovery, parsing, and rule resolution."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .color_codes import color_manager
from .themes import BUILTIN_THEMES

try:
    import tomllib as toml_loader  # type: ignore[import-not-found]
except ModuleNotFoundError:  # pragma: no cover
    import tomli as toml_loader  # type: ignore[import-not-found]


class ConfigError(ValueError):
    """Raised when a config file is invalid."""


def discover_config_path(
    explicit_path: Path | None = None,
    cwd: Path | None = None,
    user_config_path: Path | None = None,
) -> Path | None:
    """Discover the highest-precedence config path."""
    if explicit_path is not None:
        return explicit_path

    search_cwd = cwd or Path.cwd()
    candidates = [
        search_cwd / "pipetint.toml",
        search_cwd / ".pipetint.toml",
        user_config_path or Path.home() / ".config" / "pipetint" / "config.toml",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _normalize_rule(rule: dict[str, Any]) -> dict[str, Any]:
    """Validate and normalize one rule definition."""
    name = rule.get("name")
    pattern = rule.get("pattern")
    colors = rule.get("colors")
    if not isinstance(name, str) or not name:
        raise ConfigError("Rule is missing a valid name")
    if not isinstance(pattern, str) or not pattern:
        raise ConfigError(f"Rule '{name}' is missing a valid pattern")
    if not isinstance(colors, list) or not colors:
        raise ConfigError(f"Rule '{name}' must define at least one color")
    for color_name in colors:
        if (
            not isinstance(color_name, str)
            or color_manager.get_color_code(color_name) is None
        ):
            raise ConfigError(f"Unknown color '{color_name}' in rule '{name}'")
    return {
        "name": name,
        "pattern": pattern,
        "colors": colors,
        "case_sensitive": bool(rule.get("case_sensitive")),
        "replace_all": bool(rule.get("replace_all")),
        "description": rule.get("description", ""),
    }


def load_config(path: Path) -> dict[str, Any]:
    """Load and validate a TOML config file."""
    try:
        raw = toml_loader.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"Config file not found: {path}") from exc
    except toml_loader.TOMLDecodeError as exc:
        raise ConfigError(f"Invalid config syntax in {path}: {exc}") from exc

    version = raw.get("version")
    if version != 1:
        raise ConfigError("Config version must be 1")

    rules_map: dict[str, dict[str, Any]] = {}
    for raw_rule in raw.get("rules", []):
        normalized = _normalize_rule(raw_rule)
        if normalized["name"] in rules_map:
            raise ConfigError(f"Duplicate rule name '{normalized['name']}'")
        rules_map[normalized["name"]] = normalized

    themes_map: dict[str, dict[str, Any]] = {}
    for theme_name, theme in raw.get("themes", {}).items():
        theme_rules = theme.get("rules", [])
        if theme_name in themes_map:
            raise ConfigError(f"Duplicate theme name '{theme_name}'")
        if not isinstance(theme_rules, list):
            raise ConfigError(f"Theme '{theme_name}' must define a rules list")
        for rule_name in theme_rules:
            if rule_name not in rules_map:
                raise ConfigError(
                    f"Theme '{theme_name}' references undefined rule '{rule_name}'"
                )
        themes_map[theme_name] = {
            "description": theme.get("description", ""),
            "rules": theme_rules,
        }

    return {
        "version": version,
        "default_theme": raw.get("default_theme"),
        "default_rules": raw.get("default_rules", []),
        "rules": rules_map,
        "themes": themes_map,
    }


def _theme_rule_map(config: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    """Build a combined theme map with config overrides applied."""
    themes = {
        name: {
            "description": theme["description"],
            "rules": [rule["name"] for rule in theme["rules"]],
        }
        for name, theme in BUILTIN_THEMES.items()
    }
    if config is not None:
        themes.update(config.get("themes", {}))
    return themes


def _rule_catalog(config: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    """Build a combined rule catalog with config overrides applied."""
    catalog: dict[str, dict[str, Any]] = {}
    for theme in BUILTIN_THEMES.values():
        for rule in theme["rules"]:
            catalog[rule["name"]] = dict(rule)
    if config is not None:
        catalog.update(config.get("rules", {}))
    return catalog


def resolve_selected_rules(
    config: dict[str, Any] | None,
    theme_name: str | None = None,
    selected_rule_names: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Resolve selected theme and rule names into ordered rule definitions."""
    themes = _theme_rule_map(config)
    catalog = _rule_catalog(config)
    resolved: list[dict[str, Any]] = []

    effective_theme = theme_name or (config or {}).get("default_theme")
    if effective_theme is not None:
        if effective_theme not in themes:
            raise ConfigError(f"Unknown theme: {effective_theme}")
        resolved.extend(
            catalog[rule_name] for rule_name in themes[effective_theme]["rules"]
        )

    for rule_name in (config or {}).get("default_rules", []):
        if rule_name not in catalog:
            raise ConfigError(f"Unknown rule: {rule_name}")
        resolved.append(catalog[rule_name])

    for rule_name in selected_rule_names or []:
        if rule_name not in catalog:
            raise ConfigError(f"Unknown rule: {rule_name}")
        resolved.append(catalog[rule_name])

    return resolved
