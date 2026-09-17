#!/usr/bin/env python3
"""validate_visual_baseline.py - lightweight visual regression baseline.

This is intentionally browser-free. It verifies that the static assets that
drive EDIC visual previews still match the checked-in baseline and retain the
signals required by 2.0 component documentation.

Exit codes:
  0 = pass
  1 = blocking error (missing baseline, missing asset, mismatch, missing signal)
  2 = warnings only
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / "tests" / "fixtures" / "visual" / "baseline.json"


def canonical_line_endings(data: bytes) -> bytes:
    """Normalize Windows line endings so local and CI hashes stay comparable."""
    return data.replace(b"\r\n", b"\n")


def sha256(path: Path) -> str:
    return hashlib.sha256(canonical_line_endings(path.read_bytes())).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="校验或更新视觉回归基线")
    parser.add_argument(
        "--update",
        action="store_true",
        help="重新计算各资产 sha256 并写回 baseline.json（供 post-merge-stamp 在 stamp 后刷新，不做校验）",
    )
    args = parser.parse_args()

    if not BASELINE.exists():
        print("[ERROR] 缺少视觉回归基线文件: tests/fixtures/visual/baseline.json")
        return 1

    if args.update:
        try:
            baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"[ERROR] 视觉回归基线 JSON 解析失败: {exc}", file=sys.stderr)
            return 1
        assets = baseline.get("assets")
        if not isinstance(assets, list) or not assets:
            print("[ERROR] baseline.assets 必须是非空数组", file=sys.stderr)
            return 1
        for entry in assets:
            if not isinstance(entry, dict) or not entry.get("path"):
                print("[ERROR] baseline.assets 每一项必须包含 path", file=sys.stderr)
                return 1
            asset_path = ROOT / entry["path"]
            if not asset_path.exists():
                print(f"[ERROR] 基线资产不存在: {entry['path']}", file=sys.stderr)
                return 1
            entry["sha256"] = sha256(asset_path)
        BASELINE.write_text(json.dumps(baseline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"✓ baseline.json 已更新（{len(assets)} 个资产）。")
        return 0

    errors: list[str] = []

    if not BASELINE.exists():
        print("[ERROR] 缺少视觉回归基线文件: tests/fixtures/visual/baseline.json")
        return 1

    try:
        baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[ERROR] 视觉回归基线 JSON 解析失败: {exc}")
        return 1

    assets = baseline.get("assets")
    if not isinstance(assets, list) or not assets:
        errors.append("baseline.assets 必须是非空数组")
        assets = []

    print("─── 视觉回归基线校验 ───")

    for entry in assets:
        if not isinstance(entry, dict):
            errors.append("baseline.assets 每一项必须是对象")
            continue

        path_name = entry.get("path")
        if not path_name:
            errors.append("baseline.assets 缺少 path")
            continue

        asset_path = ROOT / path_name
        if not asset_path.exists():
            errors.append(f"基线资产不存在: {path_name}")
            continue

        digest = sha256(asset_path)
        if digest != entry.get("sha256"):
            errors.append(f"视觉基线不匹配: {path_name}（运行 generate_visual_baseline.py 重建）")

        text = asset_path.read_text(encoding="utf-8", errors="replace")
        missing = [signal for signal in entry.get("signals", []) if signal not in text]
        if missing:
            errors.append(f"{path_name} 缺少视觉回归信号: {', '.join(missing)}")

    print(f"扫描资产: {len(assets)} 个")

    for message in errors:
        print(f"[ERROR] {message}")

    if not errors:
        print("[OK] 视觉回归基线完整且关键信号存在")

    print()
    print(f"错误: {len(errors)}  警告: 0")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
