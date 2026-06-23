#!/usr/bin/env python3
"""tools/validate_size.py — Validate CSS/JS gzip sizes against configured limits.

This script checks that the gzip-compressed size of styles.css and scripts.js
does not exceed the thresholds defined in .size-limit.json.

Usage:
  python3 tools/validate_size.py          # validate
  python3 tools/validate_size.py --check   # check-only mode (CI)
"""

import gzip
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = ROOT / ".size-limit.json"
EXITCODE_CONFIG = {
    "warning": 0,  # within limit
    "exceeded": 1,  # over limit
    "missing": 2,  # file doesn't exist
}


def gzip_size(path: Path) -> int:
    """Return gzip-compressed size of a file in bytes, using compresslevel=9."""
    data = path.read_bytes()
    return len(gzip.compress(data, compresslevel=9))


def main() -> int:
    config = json.loads(CONFIG_FILE.read_text())
    problems = []

    for asset_key, cfg in config.items():
        file_path = ROOT / cfg["file"]
        if not file_path.exists():
            print(f"[MISSING] {cfg['file']} not found")
            problems.append((cfg["file"], "missing", 0, cfg["max_kb"] * 1024))
            continue

        size_kb = gzip_size(file_path) / 1024
        max_kb = cfg["max_kb"]

        if size_kb > max_kb:
            print(
                f"[FAIL] {cfg['file']}: {size_kb:.1f}KB > {max_kb}KB (limit exceeded)"
            )
            problems.append((cfg["file"], "exceeded", size_kb * 1024, max_kb * 1024))
        else:
            print(f"[OK]   {cfg['file']}: {size_kb:.1f}KB / {max_kb}KB")

    print()
    if problems:
        for name, status, actual, limit in problems:
            if status == "missing":
                print(f"[ERROR] {name}: file not found")
            else:
                pct = (actual / limit) * 100
                print(
                    f"[SIZE EXCEEDED] {name}: {actual / 1024:.1f}KB (limit: {limit / 1024:.0f}KB, {pct:.0f}% of limit)"
                )
        print(
            f"\nSize limit check FAILED. Update thresholds in .size-limit.json if intentional."
        )
        return 1

    print("All assets within size limits.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
