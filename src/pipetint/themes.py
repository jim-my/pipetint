"""Built-in Pipetint themes."""

from __future__ import annotations

from typing import TypedDict


class RuleDefinition(TypedDict, total=False):
    """A named rule definition."""

    name: str
    pattern: str
    colors: list[str]
    case_sensitive: bool
    replace_all: bool
    description: str


class ThemeDefinition(TypedDict):
    """A theme description and rule list."""

    description: str
    rules: list[RuleDefinition]


BUILTIN_THEMES: dict[str, ThemeDefinition] = {
    "log-levels": {
        "description": "Common application log levels",
        "rules": [
            {
                "name": "critical-errors",
                "pattern": "CRITICAL|FATAL|ERROR",
                "colors": ["red", "bold"],
            },
            {
                "name": "warnings",
                "pattern": "WARN|WARNING",
                "colors": ["yellow"],
            },
            {
                "name": "timestamps",
                "pattern": "\\d{2}:\\d{2}:\\d{2}",
                "colors": ["blue"],
            },
        ],
    },
    "git-diff": {
        "description": "Git diff additions, removals, and hunk headers",
        "rules": [
            {"name": "diff-added", "pattern": "^\\+.*", "colors": ["green"]},
            {"name": "diff-removed", "pattern": "^-.*", "colors": ["red"]},
            {
                "name": "diff-header",
                "pattern": "^@@.*@@",
                "colors": ["cyan", "bold"],
            },
        ],
    },
    "pytest": {
        "description": "Pytest result output",
        "rules": [
            {"name": "pytest-failed", "pattern": "FAILED", "colors": ["red", "bold"]},
            {"name": "pytest-passed", "pattern": "PASSED", "colors": ["green"]},
            {"name": "pytest-error", "pattern": "ERROR", "colors": ["yellow", "bold"]},
        ],
    },
    "http-status": {
        "description": "HTTP status groups",
        "rules": [
            {"name": "http-2xx", "pattern": "\\b2\\d\\d\\b", "colors": ["green"]},
            {"name": "http-4xx", "pattern": "\\b4\\d\\d\\b", "colors": ["yellow"]},
            {"name": "http-5xx", "pattern": "\\b5\\d\\d\\b", "colors": ["red", "bold"]},
        ],
    },
    "timestamps": {
        "description": "Common HH:MM:SS timestamps",
        "rules": [
            {
                "name": "timestamps",
                "pattern": "\\d{2}:\\d{2}:\\d{2}",
                "colors": ["blue"],
            }
        ],
    },
}
