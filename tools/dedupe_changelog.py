#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/dedupe_changelog.py — CHANGELOG.md 条目去重与分类归并。

解决 issue #321 中两个可自动化的问题：

  1. squash/merge 双份条目
     同一个 PR 合并后，release-please 会同时记录 squash commit 与 merge
     commit 的 subject，导致同一变更出现两条（仅 commit SHA 不同）。
     例：#295 的 0105637 与 a64f6b0。

  2. 早期非标准分类
     `### Changed` / `### Notes` / `### 清理` 等不在 release-please-config.json
     的 changelog-sections 中，与当前配置矛盾。

用法：
  python3 tools/dedupe_changelog.py           # 原地修复 CHANGELOG.md
  python3 tools/dedupe_changelog.py --check   # 仅检查（CI 用，需要修复返回 exit 2）
  python3 tools/dedupe_changelog.py --dry-run # 打印将做的改动，不写文件

退出码：
  0  无需修复 / 已修复
  1  错误
  2  --check：检测到需要修复的问题
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG_MD = ROOT / "CHANGELOG.md"
CONFIG_JSON = ROOT / "release-please-config.json"

# 非标准分类 → 标准分类映射。
# 标准分类来自 release-please-config.json 的 changelog-sections（"section" 字段）。
# 非标准分类 → 标准分类映射。
# 标准分类来自 release-please-config.json 的 changelog-sections（"section" 字段），
# 当前为：新增 / 修复 / 性能优化 / 重构 / 文档 / 样式 / 测试 / 构建 / CI / 其他 / 回滚。
# 注意：必须直接映射到最终目标，不要链式（Changed→变更→修复 不会生效，
# 因为每行只会查一次表）。
SECTION_ALIASES = {
    "Changed": "修复",
    "Notes": "其他",
    "⚠ BREAKING CHANGES": "回滚",
    "修复（首页设计系统规范合规性）": "修复",
    "变更": "修复",
    "清理": "其他",
    "维护": "其他",
    "许可证": "其他",
}

# 条目行：* **scope:** subject ([hash](url)) 或 - **scope:** subject ([#N](url))
# 列表标记可能是 '*'（release-please 生成）或 '-'（早期手工条目）。
ENTRY_RE = re.compile(r"^[*-]\s+\*\*(?P<scope>[^*]+)\*\*\s*:?\s*(?P<subject>.*)$")
# 提取条目中的 commit SHA（40 位十六进制或 7 位短 SHA）
SHA_RE = re.compile(r"\((?:\[[^\]]*\]\([^)]*\)\s*)?\[([0-9a-f]{7,40})\]\([^)]*\)")


def load_standard_sections() -> set[str]:
    """从 release-please-config.json 读取标准分类名。"""
    try:
        cfg = json.loads(CONFIG_JSON.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        print(f"[ERROR] 无法读取 {CONFIG_JSON}: {e}", file=sys.stderr)
        sys.exit(1)
    return {s["section"] for s in cfg.get("changelog-sections", [])}


def entry_signature(line: str) -> str | None:
    """返回条目的去重签名：scope + subject（去掉 commit SHA 与链接）。

    同一 PR 的 squash 与 merge commit subject 相同，仅 SHA 不同，
    因此用 scope+subject 作为身份判据。
    """
    m = ENTRY_RE.match(line.strip())
    if not m:
        return None
    scope = m.group("scope").strip().rstrip(":").strip()
    subject = m.group("subject")
    # 去掉各类链接引用，只留可读文本
    subject = re.sub(r"\(\[[^\]]*\]\([^)]*\)\s*\)", "", subject)
    subject = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", subject)
    subject = re.sub(r"\s+", " ", subject).strip()
    if not subject:
        return None
    return f"{scope}:{subject}"


def find_version_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """返回每个版本块的 (起始行索引, 结束行索引)（结束不含）。"""
    starts = [i for i, l in enumerate(lines) if l.startswith("## [")]
    blocks = []
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else len(lines)
        blocks.append((s, e))
    return blocks


def process(lines: list[str], std_sections: set[str]) -> tuple[list[str], list[str]]:
    """返回 (新行列表, 变更说明列表)。"""
    changes: list[str] = []
    out: list[str] = []
    blocks = find_version_blocks(lines)
    # 不在任何版本块内的行（文件头）原样保留
    first_block_start = blocks[0][0] if blocks else len(lines)
    out.extend(lines[:first_block_start])

    for (bs, be) in blocks:
        block = lines[bs:be]
        version = re.match(r"## \[([\d.]+)\]", block[0])
        version = version.group(1) if version else "?"

        # ── 1. 分类归并 ──────────────────────────────────────────────
        new_block: list[str] = []
        for line in block:
            m = re.match(r"^###\s+(.+?)\s*$", line)
            if m:
                sec = m.group(1).strip()
                if sec in SECTION_ALIASES:
                    target = SECTION_ALIASES[sec]
                    changes.append(f"[{version}] 分类归并: ### {sec} → ### {target}")
                    new_block.append(f"### {target}\n")
                    continue
                if sec not in std_sections:
                    # 未登记且无映射：保留但报告，避免静默丢失信息
                    changes.append(f"[{version}] ⚠ 未登记分类保留: ### {sec}")
            new_block.append(line)
        block = new_block

        # ── 2. 条目去重（同版本内） ──────────────────────────────────
        seen: dict[str, int] = {}
        deduped: list[str] = []
        for line in block:
            sig = entry_signature(line)
            if sig is None:
                deduped.append(line)
                continue
            if sig in seen:
                sha_new = SHA_RE.search(line)
                sha_old = SHA_RE.search(deduped[seen[sig]])
                # 保留信息更全的那条（有 SHA 的优先）；两者都有 SHA 时保留先出现的
                if sha_new and not sha_old:
                    deduped[seen[sig]] = line
                changes.append(
                    f"[{version}] 去重: {sig[:60]}"
                    + (f" (sha {sha_old.group(1)[:7]})" if sha_old else "")
                )
                continue
            seen[sig] = len(deduped)
            deduped.append(line)

        # ── 3. 清理归并后遗留的空分类节 ─────────────────────────────
        # 注意：条目列表标记可能是 '*' 或 '-'（早期手工条目用 '-'），
        # 只认 '*' 会把真实条目误判为空节而删除。
        final: list[str] = []
        i = 0
        while i < len(deduped):
            line = deduped[i]
            if re.match(r"^###\s+", line):
                # 向前看：该分类节下是否有条目
                j = i + 1
                has_entry = False
                while j < len(deduped) and not re.match(r"^###\s+", deduped[j]):
                    if re.match(r"^\s*[*-]\s+", deduped[j]):
                        has_entry = True
                        break
                    j += 1
                if not has_entry:
                    sec_name = re.match(r"^###\s+(.+?)\s*$", line).group(1)
                    changes.append(f"[{version}] 移除空分类节: ### {sec_name}")
                    i += 1
                    continue
            final.append(line)
            i += 1

        out.extend(final)

    return out, changes


def main() -> int:
    ap = argparse.ArgumentParser(description="CHANGELOG.md 条目去重与分类归并")
    ap.add_argument("--check", action="store_true", help="仅检查，需要修复时返回 exit 2")
    ap.add_argument("--dry-run", action="store_true", help="打印改动但不写文件")
    args = ap.parse_args()

    std_sections = load_standard_sections()
    original = CHANGELOG_MD.read_text(encoding="utf-8")
    lines = original.splitlines(keepends=True)

    new_lines, changes = process(lines, std_sections)

    if not changes:
        print("[OK] CHANGELOG.md 无需修复（无重复条目、无非标准分类）")
        return 0

    print(f"检测到 {len(changes)} 处待修复：")
    for c in changes:
        print(f"  {c}")

    if args.check:
        print("\n[ERROR] CHANGELOG.md 需要修复，请运行：python3 tools/dedupe_changelog.py", file=sys.stderr)
        return 2

    if args.dry_run:
        print("\n(--dry-run，未写入文件)")
        return 0

    CHANGELOG_MD.write_text("".join(new_lines), encoding="utf-8")
    print(f"\n[OK] 已修复 {len(changes)} 处 → {CHANGELOG_MD.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
