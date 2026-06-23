#!/usr/bin/env python3
"""scripts/build.py — EDIC full build pipeline.

Run: python3 scripts/build.py

Steps:
  1. python3 scripts/lint.py   — abort if lint fails
  2. python3 tools/stamp_version.py   — sync version placeholders
  3. python3 tools/generate_icons.py   — regenerate icons.svg
  4. python3 tools/generate_pdfs.py    — generate PDF assets
  5. bash scripts/package-skill.sh     — package SKILL ZIP (optional)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
TOOLS = ROOT / "tools"


def run(cmd: list[str], label: str, cwd: Path | None = None) -> int:
    print(f"\n{'=' * 60}")
    print(f"  {label}")
    print(f"  $ {' '.join(str(c) for c in cmd)}")
    print(f"{'=' * 60}")
    result = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=False)
    if result.returncode != 0:
        print(f"\n[ABORT] {label} failed with exit {result.returncode}")
        return result.returncode
    print(f"[OK] {label}")
    return 0


def main() -> int:
    try:
        version = open(ROOT / "VERSION").read().strip().splitlines()[0].strip()
        if not version:
            raise ValueError("VERSION 文件为空")
    except (OSError, ValueError) as e:
        print(f"[ABORT] 无法读取 VERSION: {e}")
        return 1
    print(f"EDIC Build Pipeline · v{version}")
    print(f"Root: {ROOT}")

    # Step 1: lint
    rc = run(
        [sys.executable, str(SCRIPTS / "lint.py")], "Step 1: Lint (abort on failure)"
    )
    if rc != 0:
        return rc

    # Step 2: stamp version
    rc = run(
        [sys.executable, str(TOOLS / "stamp_version.py")],
        "Step 2: Stamp version placeholders",
    )
    if rc != 0:
        return rc

    # Step 3: generate icons
    rc = run(
        [sys.executable, str(TOOLS / "generate_icons.py")], "Step 3: Generate icons.svg"
    )
    if rc != 0:
        return rc

    # Step 4: generate PDFs
    rc = run(
        [sys.executable, str(TOOLS / "generate_pdfs.py")], "Step 4: Generate PDF assets"
    )
    if rc != 0:
        return rc

    # Step 5: package SKILL (optional — skip if script doesn't exist)
    skill_script = SCRIPTS / "package_skill.py"
    if skill_script.exists():
        rc = run([sys.executable, str(skill_script)], "Step 5: Package SKILL ZIP")
        if rc != 0:
            return rc
    else:
        print(f"\n[SKIP] {skill_script} not found — skipping SKILL packaging")

    print(f"""
{"=" * 60}
  Build complete · v{version}
{"=" * 60}
Generated artifacts:
  - icons.svg            (from scripts.js ICONS array)
  - assets/downloads/*.pdf (PDF reference cards)
  - assets/downloads/edic-design-system-skill-v{version}.zip (if package_skill.py ran)
""")
    return 0


if __name__ == "__main__":
    sys.exit(main())
