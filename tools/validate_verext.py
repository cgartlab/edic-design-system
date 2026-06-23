#!/usr/bin/env python3
"""validate_verext.py — 扩展版本一致性校验

检查项（独立于 validate_versions.py 的 HTML ?v= 检查）：
  1. tokens.json "version" 字段与 VERSION 文件一致
  2. package.json "version" 字段与 VERSION 文件一致
  3. scripts.js 中对 styles.css?v= 的引用与 VERSION 一致
  4. scripts.js 自身是否有 ?v= 版本查询串（WARNING if missing）
  5. scripts.js 是否声明了 VERSION 常量/变量及其值是否一致
  6. 所有扫描到的 ?v= 值与 VERSION 不一致时报告 ERROR
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
SCRIPTS_FILE = ROOT / "scripts.js"

SEMVER_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?$")
QV_RE = re.compile(r"\?v=([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?)")
# Files that are exempt from ?v= reference checks (JS files don't self-reference ?v=)
SKIP_FROM_VVERSION_CHECK = {"scripts.js"}
# 匹配 scripts.js 中对 CSS/JS 资源的 src引用（含 ?v=）
SRC_REF_RE = re.compile(r'(?:href|src)="([^"?]+\.(?:css|js))\?v=([^"]+)"')
# 匹配 VERSION 常量或变量声明
VERSION_DECL_RE = re.compile(
    r"\b(?:const|let|var)\s+VERSION\s*[=:]\s*[\x27\x22]([^\x27\x22]+)[\x27\x22]"
)


def get_expected_version() -> str | None:
    """从 VERSION 文件读取期望版本。"""
    if not VERSION_FILE.exists():
        return None
    lines = VERSION_FILE.read_text(encoding="utf-8").strip().splitlines()
    return lines[0].strip() if lines else None


def check_tokens_version(expected: str, verbose: bool) -> list[tuple[str, str, str]]:
    """检查 tokens.json version 字段。返回 [(level, file:loc, msg)]。"""
    issues: list[tuple[str, str, str]] = []
    if not TOKENS_FILE.exists():
        issues.append(("ERROR", "tokens.json", "文件不存在"))
        return issues

    try:
        text = TOKENS_FILE.read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as e:
        issues.append(("ERROR", "tokens.json", f"读取或解析失败: {e}"))
        return issues

    # 尝试多个路径
    ver: str | None = None
    ver_path = ""
    if "version" in data:
        ver = data["version"]
        ver_path = "tokens.json.version"
    elif (
        "info" in data and isinstance(data["info"], dict) and "version" in data["info"]
    ):
        ver = data["info"]["version"]
        ver_path = "tokens.json.info.version"

    if ver is None:
        issues.append(
            (
                "ERROR",
                "tokens.json",
                "未发现 version 字段（尝试了 .version 和 .info.version）",
            )
        )
        return issues

    if ver != expected:
        issues.append(
            ("ERROR", ver_path, f"version={ver!r}，与 VERSION {expected!r} 不一致")
        )
    elif verbose:
        issues.append(("OK", ver_path, f"version={ver!r}"))

    return issues


def check_package_version(expected: str, verbose: bool) -> list[tuple[str, str, str]]:
    """检查 package.json version 字段。"""
    issues: list[tuple[str, str, str]] = []
    if not PACKAGE_FILE.exists():
        issues.append(("ERROR", "package.json", "文件不存在"))
        return issues

    try:
        text = PACKAGE_FILE.read_text(encoding="utf-8")
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as e:
        issues.append(("ERROR", "package.json", f"读取或解析失败: {e}"))
        return issues

    ver = data.get("version") if isinstance(data, dict) else None
    if ver is None:
        issues.append(("ERROR", "package.json", "未发现顶层 version 字段"))
        return issues

    if ver != expected:
        issues.append(
            (
                "ERROR",
                "package.json.version",
                f"version={ver!r}，与 VERSION {expected!r} 不一致",
            )
        )
    elif verbose:
        issues.append(("OK", "package.json.version", f"version={ver!r}"))

    return issues


def check_scripts_version_refs(
    expected: str, verbose: bool
) -> tuple[list[tuple[str, str, str]], bool]:
    """检查 scripts.js 中对 styles.css 和 scripts.js 的 ?v= 引用。"""
    if SCRIPTS_FILE.name in SKIP_FROM_VVERSION_CHECK:
        return [], False
    issues: list[tuple[str, str, str]] = []
    has_own_qv = False

    if not SCRIPTS_FILE.exists():
        issues.append(("ERROR", "scripts.js", "文件不存在"))
        return issues, False

    text = SCRIPTS_FILE.read_text(encoding="utf-8", errors="replace")

    # 检查 scripts.js 自身是否有 ?v=
    if QV_RE.search(text):
        has_own_qv = True
    else:
        issues.append(("WARN", "scripts.js", "scripts.js 自身未使用 ?v= 版本查询串"))

    # 检查引用的资源 ?v=
    css_qv_found = False
    js_qv_found = False

    for match in SRC_REF_RE.finditer(text):
        resource = match.group(1)
        ver = match.group(2)
        lineno = text[: match.start()].count("\n") + 1
        ref = f"scripts.js:{lineno}"

        if resource == "styles.css":
            css_qv_found = True
            if ver != expected:
                issues.append(
                    (
                        "ERROR",
                        ref,
                        f"styles.css?v={ver}，与 VERSION {expected!r} 不一致",
                    )
                )
            elif verbose:
                issues.append(("OK", ref, f"styles.css?v={ver}"))

        elif resource == "scripts.js":
            js_qv_found = True
            if ver != expected:
                issues.append(
                    (
                        "ERROR",
                        ref,
                        f"scripts.js?v={ver}，与 VERSION {expected!r} 不一致",
                    )
                )
            elif verbose:
                issues.append(("OK", ref, f"scripts.js?v={ver}"))

    if not css_qv_found:
        issues.append(("WARN", "scripts.js", "未发现对 styles.css?v= 的引用"))

    return issues, has_own_qv


def check_scripts_version_decl(
    expected: str, verbose: bool
) -> list[tuple[str, str, str]]:
    """检查 scripts.js 中 VERSION 常量/变量声明。"""
    if SCRIPTS_FILE.name in SKIP_FROM_VVERSION_CHECK:
        return []
    issues: list[tuple[str, str, str]] = []

    if not SCRIPTS_FILE.exists():
        return issues

    text = SCRIPTS_FILE.read_text(encoding="utf-8", errors="replace")

    for match in VERSION_DECL_RE.finditer(text):
        ver = match.group(1)
        lineno = text[: match.start()].count("\n") + 1
        ref = f"scripts.js:{lineno}"

        if ver != expected:
            issues.append(
                ("WARN", ref, f"VERSION={ver!r}，与 VERSION 文件 {expected!r} 不一致")
            )
        elif verbose:
            issues.append(("OK", ref, f"VERSION={ver!r}"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="扩展版本一致性校验")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="显示所有检查项（含 OK）"
    )
    args = parser.parse_args()

    expected = get_expected_version()
    print("─── 扩展版本一致性校验 ───")
    if expected:
        print(f"期望版本（来自 VERSION）: {expected}")
    else:
        print("[ERROR] 未发现 VERSION 文件或内容为空")
        return 1

    errors = 0
    warnings = 0

    # 1. tokens.json version
    for level, loc, msg in check_tokens_version(expected, args.verbose):
        print(f"[{level}] {loc} {msg}")
        if level == "ERROR":
            errors += 1
        else:
            warnings += 1

    # 2. package.json version
    for level, loc, msg in check_package_version(expected, args.verbose):
        print(f"[{level}] {loc} {msg}")
        if level == "ERROR":
            errors += 1
        else:
            warnings += 1

    # 3 &4. scripts.js ?v= 引用
    script_issues, has_own_qv = check_scripts_version_refs(expected, args.verbose)
    for level, loc, msg in script_issues:
        print(f"[{level}] {loc} {msg}")
        if level == "ERROR":
            errors += 1
        else:
            warnings += 1

    # 5. scripts.js VERSION 声明
    for level, loc, msg in check_scripts_version_decl(expected, args.verbose):
        print(f"[{level}] {loc} {msg}")
        if level == "ERROR":
            errors += 1
        else:
            warnings += 1

    print()
    print(f"错误: {errors}  警告: {warnings}")
    if errors:
        return 1
    if warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
