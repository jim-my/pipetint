"""Tests for built-in themes."""

from pipetint.color_codes import color_manager
from pipetint.themes import BUILTIN_THEMES


class TestBuiltInThemes:
    """Test built-in theme catalog."""

    def test_expected_themes_exist(self) -> None:
        """Initial built-in themes should be present."""
        assert "log-levels" in BUILTIN_THEMES
        assert "git-diff" in BUILTIN_THEMES
        assert "pytest" in BUILTIN_THEMES
        assert "http-status" in BUILTIN_THEMES
        assert "timestamps" in BUILTIN_THEMES

    def test_theme_rules_use_known_colors(self) -> None:
        """Built-in theme rules should only use valid color names."""
        for theme in BUILTIN_THEMES.values():
            for rule in theme["rules"]:
                assert rule["colors"]
                for color_name in rule["colors"]:
                    assert color_manager.get_color_code(color_name) is not None
