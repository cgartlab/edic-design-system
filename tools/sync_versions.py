#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_versions.py — 将 VERSION 同步到 tokens.json 和 package.json，
并可选调用 stamp_version.py 同步 HTML/MD 文件。

用途（开发者本地工具）：
  python3 tools/sync_versions.py                    # 从 VERSION 读取，同步所有文件
  python3 tools/sync_versions.py --set 1.6.0       # 指定版本并同步
  python3 tools/sync_versions.py --check           # 检查模式（不修改）
  python3 tools/sync_versions.py --dry-run 1.6.0   # 预览模式

退出码：
  0  成功或 dry-run
  1  错误（文件不存在、版本格式非法）
  2  检查模式发现不一致（需要同步）

用法（Makefile）：
  make sync-versions          # 从 VERSION 同步所有文件
  make sync-versions:check   # 检查版本一致性
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"
TOKENS_FILE = ROOT / "tokens.json"
PACKAGE_FILE = ROOT / "package.json"
STAMP_SCRIPT = ROOT / "tools" / "stamp_version.py"


# ─── 版本读取 ────────────────────────────────────────────────


def read_version_from_file() -> str:
    """从 VERSION 文件读取版本号（单行、去空白）。"""
    if not VERSION_FILE.exists():
        raise FileNotFoundError(f"VERSION 文件不存在: {VERSION_FILE}")
    text = VERSION_FILE.read_text(encoding="utf-8")
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
    if not lines:
        raise ValueError(f"VERSION 文件为空: {VERSION_FILE}")
    version = lines[0]
    if not re.match(r"^\d+\.\d+\.\d+(?:-[a-zA-Z0-9.]+)?$", version):
        raise ValueError(f"VERSION 文件内容非法（需 semver）: '{version}'")
    return version


# ─── 同步逻辑 ────────────────────────────────────────────────


def sync_tokens_json(version: str, dry_run: bool = False) -> bool:
    """同步 tokens.json 的 version 字段。返回是否需要变更。"""
    if not TOKENS_FILE.exists():
        print(f"  [WARN] tokens.json 不存在，跳过")
        return False

    content = TOKENS_FILE.read_text(encoding="utf-8")
    data = json.loads(content)
    current = data.get("version", "")

    if current == version:
        print(f"  tokens.json: 已是 v{version}，无需变更")
        return False

    if dry_run:
        print(f"  [DRY-RUN] tokens.json: v{current} → v{version}")
        return True

    data["version"] = version
    # 保持 2 空格缩进、保留顺序（近似原格式）
    TOKENS_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"  tokens.json: v{current} → v{version}")
    return True


def sync_package_json(version: str, dry_run: bool = False) -> bool:
    """同步 package.json 的 version 字段。返回是否需要变更。"""
    if not PACKAGE_FILE.exists():
        print(f"  [WARN] package.json 不存在，跳过")
        return False

    content = PACKAGE_FILE.read_text(encoding="utf-8")
    data = json.loads(content)
    current = data.get("version", "")

    if current == version:
        print(f"  package.json: 已是 v{version}，无需变更")
        return False

    if dry_run:
        print(f"  [DRY-RUN] package.json: v{current} → v{version}")
        return True

    data["version"] = version
    PACKAGE_FILE.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"  package.json: v{current} → v{version}")
    return True


def run_stamp_version(dry_run: bool = False) -> int:
    """调用 stamp_version.py 同步 HTML/MD 文件。返回 0=成功, 1=失败。"""
    if not STAMP_SCRIPT.exists():
        print(f"  [WARN] stamp_version.py 不存在，跳过 HTML/MD stamp")
        return 0

    import subprocess

    cmd = [sys.executable, str(STAMP_SCRIPT)]
    if dry_run:
        cmd.append("--diff")

    result = subprocess.run(cmd, capture_output=True, text=True)
    for line in result.stdout.splitlines():
        print(f"  {line}")
    if result.stderr:
        for line in result.stderr.splitlines():
            if line.strip():
                print(f"  [STDERR] {line}", file=sys.stderr)

    return result.returncode


# ─── 主入口 ──────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(
        description="同步 VERSION 到所有版本源文件（开发者本地工具）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--set",
        dest="version",
        metavar="X.Y.Z",
        help="指定版本号（覆盖 VERSION 文件内容，同时写入所有文件）",
    )
    group.add_argument(
        "--check",
        action="store_true",
        help="检查模式：验证所有版本是否一致，不修改任何文件",
    )
    group.add_argument(
        "--dry-run",
        dest="version",
        metavar="X.Y.Z",
        help="预览模式：显示需要变更的内容，不实际写入",
    )
    parser.add_argument(
        "--no-stamp",
        action="store_true",
        help="跳过调用 stamp_version.py（仅同步 JSON 版本字段）",
    )
    args = parser.parse_args()

    # ── 确定版本号 ──────────────────────────────────────────
    if args.check:
        mode = "check"
        try:
            version = read_version_from_file()
        except (FileNotFoundError, ValueError) as e:
            print(f"[ERROR] {e}", file=sys.stderr)
            return 1
    elif args.version:
        version = args.version
        if not re.match(r"^\d+\.\d+\.\d+(?:-[a-zA-Z0-9.]+)?$", version):
            print(f"[ERROR] 版本号格式非法: '{version}'（需 semver）", file=sys.stderr)
            return 1
        mode = "write"
    else:
        mode = "write"
        try:
            version = read_version_from_file()
        except (FileNotFoundError, ValueError) as e:
            print(f"[ERROR] {e}", file=sys.stderr)
            return 1

    dry_run = mode == "check"

    # ── 输出标题 ────────────────────────────────────────────
    print(f"─── sync_versions.py ───")
    print(f"模式: {mode}")
    print(f"VERSION: v{version}")
    print()

    # ── 同步 tokens.json ───────────────────────────────────
    tokens_changed = sync_tokens_json(version, dry_run=dry_run)

    # ── 同步 package.json ─────────────────────────────────
    package_changed = sync_package_json(version, dry_run=dry_run)

    # ── 可选：写入 VERSION 文件（--set 场景）───────────────
    version_file_changed = False
    if args.version and not args.check:
        try:
            current_file_version = read_version_from_file()
        except (FileNotFoundError, ValueError):
            current_file_version = None

        if current_file_version != version:
            if not dry_run:
                VERSION_FILE.write_text(version + "\n", encoding="utf-8")
                print(f"  VERSION: {current_file_version or '(空)'} → v{version}")
            else:
                print(
                    f"  [DRY-RUN] VERSION: {current_file_version or '(空)'} → v{version}"
                )
            version_file_changed = True
        else:
            print(f"  VERSION: 已是 v{version}，无需变更")

    # ── 检查模式：汇报结果 ─────────────────────────────────
    if mode == "check":
        changed = tokens_changed or package_changed
        if changed:
            print(f"\n✗ 版本不一致，需要运行: python3 tools/sync_versions.py")
            print(f"  （或指定版本：python3 tools/sync_versions.py --set X.Y.Z）")
            return 2
        else:
            print(f"\n✓ 所有版本文件一致（VERSION = v{version}）")
            if not args.no_stamp:
                stamp_rc = run_stamp_version(dry_run=True)
                if stamp_rc == 2:
                    print("⚠ HTML/MD 文件需要 stamp，建议运行: make stamp-version")
            return 0

    # ── 写入模式：调用 stamp ───────────────────────────────
    if not args.no_stamp and not dry_run:
        print()
        stamp_rc = run_stamp_version(dry_run=False)
        if stamp_rc not in (0, 2):
            print(f"[ERROR] stamp_version.py 失败（exit {stamp_rc}）")
            return 1

    # ── 汇总 ───────────────────────────────────────────────
    print()
    any_changed = tokens_changed or package_changed or version_file_changed
    if any_changed:
        print(f"✓ 同步完成：v{version}")
        print(f"  - VERSION:     v{version}")
        print(f"  - tokens.json: v{version}")
        print(f"  - package.json: v{version}")
    else:
        print(f"✓ 所有版本文件已是 v{version}，无需变更")
    return 0


if __name__ == "__main__":
    sys.exit(main())
