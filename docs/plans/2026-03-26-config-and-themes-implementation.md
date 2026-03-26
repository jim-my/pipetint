# Config And Themes Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add TOML-backed config rules, built-in themes, and preview-oriented CLI flow without changing existing highlighting semantics.

**Architecture:** Add a thin `config.py` loader/validator and `themes.py` data module, then resolve selected rules into the existing CLI processing path. Keep preview as a CLI mode over the same resolver, not a new subsystem.

**Tech Stack:** Python 3.9+, argparse, stdlib TOML via `tomllib` with `tomli` fallback, pytest

---

### Task 1: Add failing config and theme tests

**Files:**
- Create: `tests/test_config.py`
- Create: `tests/test_themes.py`
- Modify: `tests/test_cli.py`

**Step 1: Write the failing tests**

- config discovery order
- explicit `--config`
- invalid config handling
- built-in theme listing/showing
- theme/rule CLI execution

**Step 2: Run tests to verify they fail**

Run: `pytest tests/test_config.py tests/test_themes.py tests/test_cli.py -q`

**Step 3: Commit**

After implementation for this task is green, commit only relevant files.

### Task 2: Add config and theme modules

**Files:**
- Create: `src/pipetint/config.py`
- Create: `src/pipetint/themes.py`

**Step 1: Implement minimal parsing and validation to satisfy failing tests**

**Step 2: Run targeted tests**

Run: `pytest tests/test_config.py tests/test_themes.py -q`

### Task 3: Wire CLI flags and preview behavior

**Files:**
- Modify: `src/pipetint/cli.py`

**Step 1: Add parser flags and resolver flow**

**Step 2: Keep existing direct pattern/colors path unchanged**

**Step 3: Run targeted CLI tests**

Run: `pytest tests/test_cli.py -q`

### Task 4: Add regression coverage and final verification

**Files:**
- Modify: `tests/test_cli.py`
- Modify: `tests/test_nesting.py`
- Modify: `tests/test_core.py`

**Step 1: Add regression tests for nested priorities, pipeline behavior, and replace-all**

**Step 2: Run focused regression tests**

Run: `pytest tests/test_cli.py tests/test_nesting.py tests/test_core.py -q`

**Step 3: Run full suite**

Run: `pytest -q`
