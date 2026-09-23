#!/usr/bin/env python3
"""scripts/lint.py — Unified entry point for all EDIC validators.

Exit codes follow the AGENTS.md contract:
  0 = all pass
  1 = blocking errors found
  2 = warnings only (non-blocking)
"""
from __future__ import annotations

import subprocess
import sys
from io import TextIOWrapper
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = TextIOWrapper(
        sys.stdout.buffer,
        encoding="utf-8",
        errors="replace",
        line_buffering=True,
    )

VALIDATORS = [
    ("tokens",     "tokens.json ↔ styles.css consistency"),
    ("naming",     "BEM / token naming conventions"),
    ("html",        "HTML structure, landmarks, resources, and event contracts"),
    ("a11y",       "Accessibility checks"),
    ("versions",    "Resource ?v= sync with VERSION file"),
    ("links",       "Internal & cross-page anchor validation"),
    ("cssref",      "HTML classes defined in styles.css"),
    ("darkmode",    "Dark mode token completeness"),
    ("verext",      "Extended version consistency (tokens/pkg/VERSION)"),
    ("hardcode",    "Hardcoded color values (should use --ds-*)"),
    ("manifest",    "edic-manifest.json structure and reference integrity"),
    ("manifest_css","Manifest core components have CSS classes"),
    ("components",  "Component coverage and ARIA contract checks"),
    ("icons",       "icons.json ↔ scripts.js ↔ icons.svg sync"),
    ("visual_baseline", "Visual baseline snapshot checks"),
]

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"
BOLD = "\033[1m"


def run_validator(name: str, description: str) -> tuple[str, int, str]:
    script = TOOLS / f"validate_{name}.py"
    label = f"validate-{name}"
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    rc = result.returncode
    stdout = result.stdout
    stderr = result.stderr
    combined = (stdout + "\n" + stderr).strip()

    if rc == 0:
        status = f"{GREEN}[PASS]{RESET} {label}"
    elif rc == 1:
        status = f"{RED}[FAIL]{RESET} {label}"
    elif rc == 2:
        status = f"{YELLOW}[WARN]{RESET} {label}"
    else:
        status = f"{RED}[???]{RESET} {label} (exit {rc})"

    return status, rc, combined


def main() -> int:
    print(f"{BOLD}─── EDIC Lint · v{open(ROOT / 'VERSION').read().strip()} ───{RESET}")
    print(f"Python: {sys.executable}\n")

    fail_count = 0
    warn_count = 0
    pass_count = 0
    results: list[tuple[str, int, str]] = []

    for name, description in VALIDATORS:
        status, rc, output = run_validator(name, description)
        print(f"  {status} — {description}")
        if rc == 0:
            pass_count += 1
        elif rc == 1:
            fail_count += 1
        elif rc == 2:
            warn_count += 1
        results.append((name, rc, output))

    print()
    print("─── Summary ───")
    print(f"  {GREEN}passed{RESET}: {pass_count}")
    if warn_count:
        print(f"  {YELLOW}warnings{RESET}: {warn_count}")
    if fail_count:
        print(f"  {RED}failed{RESET}: {fail_count}")

    # Print failures/warnings details
    for name, rc, output in results:
        if rc == 1:
            print(f"\n{RED}=== {name} FAILED ==={RESET}")
            for line in output.splitlines()[:30]:
                print(f"  {line}")
        elif rc == 2:
            print(f"\n{YELLOW}=== {name} warnings ==={RESET}")
            for line in output.splitlines()[:10]:
                print(f"  {line}")

    print()
    if fail_count > 0:
        print(f"{RED}✗ Lint failed ({fail_count} blocking error(s)){RESET}")
        return 1
    if warn_count > 0:
        print(f"{YELLOW}⚠ Lint passed with warnings{RESET}")
    else:
        print(f"{GREEN}✓ All validators passed{RESET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
