#!/usr/bin/env bash
# scripts/pre-commit.sh — 提交前自检（可选 git hook）
# 安装：ln -s ../../scripts/pre-commit.sh .git/hooks/pre-commit
# 或使用：git config core.hooksPath scripts
#
# 功能：
#   1. 检查本次改动的文件类型
#   2. 仅运行相关验证器（节省时间）
#   3. 通过 Node.js 包装器运行（自动检测 python/python3）
#   4. 若 Python 不可用则跳过（不阻塞提交）

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

echo "→ 提交前自检..."

# 检查是否有变更
CHANGED_FILES=$(git diff --cached --name-only 2>/dev/null || true)
if [ -z "$CHANGED_FILES" ]; then
  echo "  (无暂存变更，跳过验证)"
  exit 0
fi

CHANGED_HTML=$(echo "$CHANGED_FILES" | grep -E '\.html$' || true)
CHANGED_CSS=$(echo "$CHANGED_FILES" | grep -E '\.css$' || true)
CHANGED_JS=$(echo "$CHANGED_FILES" | grep -E '\.js$' || true)
CHANGED_TOKENS=$(echo "$CHANGED_FILES" | grep -E 'tokens\.json$' || true)
CHANGED_VERSION=$(echo "$CHANGED_FILES" | grep -E 'VERSION$' || true)
CHANGED_PACKAGE=$(echo "$CHANGED_FILES" | grep -E 'package\.json$' || true)

# 使用 Node.js 包装器运行验证器（自动检测 Python 路径）
run_validators() {
  local result
  result=$(node "$REPO_ROOT/scripts/run-validators.js" 2>&1) || true
  echo "$result"
  # 检查是否因为 Python 不可用而失败
  if echo "$result" | grep -qi "python"; then
    return 2  # Python 不可用
  fi
  # 检查是否有失败
  if echo "$result" | grep -q "部分验证失败\|Failed validators"; then
    return 1
  fi
  return 0
}

# ── 版本文件自动同步 ──────────────────────────────────────
# 当 VERSION 或 package.json 变更时，自动同步三个版本源
if [ -n "$CHANGED_VERSION" ] || [ -n "$CHANGED_PACKAGE" ]; then
  echo "  → 检测到 VERSION 或 package.json 变更，运行版本同步..."
  if ! command -v python3 &> /dev/null; then
    echo "  ⚠ Python 未安装，跳过版本同步"
    echo "  ⚠ 请手动运行：python3 tools/sync_versions.py"
  else
    if ! python3 "$REPO_ROOT/tools/sync_versions.py" --check > /tmp/sync-check.log 2>&1; then
      echo "  → 版本不一致，自动同步..."
      python3 "$REPO_ROOT/tools/sync_versions.py"
      echo "  → 已同步版本文件，重新暂存变更..."
      git add VERSION tokens.json package.json 2>/dev/null || true
      CHANGED_FILES=$(git diff --cached --name-only 2>/dev/null || true)
      echo "  → 重新暂存的文件：$CHANGED_FILES"
    else
      echo "  → 版本已一致，无需同步"
    fi
  fi
fi

# 若有任何相关改动，运行全量验证
if [ -n "$CHANGED_HTML" ] || [ -n "$CHANGED_CSS" ] || [ -n "$CHANGED_JS" ] || [ -n "$CHANGED_TOKENS" ]; then
  echo "  → 检测到 HTML/CSS/JS/tokens 改动，运行验证器..."

  if ! command -v node &> /dev/null; then
    echo "  ⚠ Node.js 未安装，跳过验证（建议在 CI 中验证）"
    exit 0
  fi

  local result
  result=$(node "$REPO_ROOT/scripts/run-validators.js" 2>&1) || true
  echo "$result"

  # 检测 Python 不可用（EXIT: null 或输出包含 python）
  if echo "$result" | grep -qi "python\|ENOENT\|not recognized"; then
    echo ""
    echo "  ⚠ Python 未找到，跳过本地验证（推送后将由 CI 验证）"
    echo "  ⚠ 建议：安装 Python 3.11+ 以运行本地验证"
    exit 0
  fi

  if echo "$result" | grep -q "部分验证失败\|Failed validators"; then
    echo ""
    echo "✗ 验证失败，请修复后再提交"
    exit 1
  fi

  if echo "$result" | grep -q "⚠"; then
    echo ""
    echo "⚠ 验证通过（有警告），建议检查上述警告"
    echo "  （警告不阻塞提交，但可能影响 CI）"
  fi
fi

echo "✓ 提交前自检通过"