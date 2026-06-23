# Makefile — EDIC Design System
# 跨平台任务编排（GNU Make）
# 用法：make <target>

SHELL := /bin/sh
.DEFAULT_GOAL := help
.PHONY: help lint build validate validate-tokens validate-naming validate-html validate-a11y validate-versions validate-links validate-cssref validate-darkmode validate-verext validate-hardcode validate-size stamp-version sync-versions sync-versions:check release-please serve clean serve-py serve-node generate-pdfs icons icons-check test skill-package release-package

PYTHON ?= python3
NODE ?= node
PORT ?= 8000

help:  ## 显示帮助
	@echo "EDIC Design System — Makefile"
	@echo ""
	@echo "用法：make <target>"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ─── 统一入口 ──────────────────────────────────────────────
lint:  ## 运行统一 lint（聚合 10 个验证器）
	$(PYTHON) scripts/lint.py

build:  ## 完整构建（lint → stamp → icons → PDFs → SKILL）
	$(PYTHON) scripts/build.py

# ─── 验证 ──────────────────────────────────────────────────
# AGENTS.md 退出码契约：0 = pass / 1 = 阻塞错误 / 2 = 仅警告（非阻塞）
# ci.yml 已将 exit 2 映射为 0；本地 `make validate` 也应如此——逐个运行所有验证器，
# 仅在出现 exit 1 时失败，exit 0/2 视为通过。
validate:  ## 全部验证（聚合 10 个验证器；exit 1 阻塞，exit 0/2 通过）
	@fail=0; \
	for t in validate-tokens validate-naming validate-html validate-a11y validate-versions validate-links validate-cssref validate-darkmode validate-verext validate-hardcode; do \
	  script="tools/validate_$$(echo $$t | sed 's/^validate-//').py"; \
	  $(PYTHON) $$script > /tmp/ds-validate-$$t.raw 2>&1; \
	  ec=$$?; \
	  grep -v '^make\[' /tmp/ds-validate-$$t.raw > /tmp/ds-validate-$$t.log 2>/dev/null || true; \
	  rm -f /tmp/ds-validate-$$t.raw; \
	  case $$ec in \
	    0) ;; \
	    1) echo "  ✗ $$t FAILED (exit 1, blocking)"; \
	       sed 's/^/    /' /tmp/ds-validate-$$t.log; \
	       fail=1 ;; \
	    2) echo "  ⚠ $$t warnings (exit 2, non-blocking)"; \
	       sed 's/^/    /' /tmp/ds-validate-$$t.log ;; \
	    *) echo "  ? $$t exit $$ec (unexpected)"; \
	       sed 's/^/    /' /tmp/ds-validate-$$t.log; \
	       fail=1 ;; \
	  esac; \
	done; \
	rm -f /tmp/ds-validate-*.log; \
	if [ $$fail -eq 0 ]; then \
	  echo ""; \
	  echo "✓ 全部验证通过"; \
	else \
	  echo ""; \
	  echo "✗ 验证失败（上方 ✗ 项为阻塞错误）"; \
	  exit 1; \
	fi

validate-tokens:  ## 校验 tokens.json ↔ styles.css 一致性
	$(PYTHON) tools/validate_tokens.py

validate-naming:  ## 校验 BEM / token 命名规范
	$(PYTHON) tools/validate_naming.py

validate-html:  ## 校验 HTML 结构
	$(PYTHON) tools/validate_html.py

validate-a11y:  ## 校验可访问性
	$(PYTHON) tools/validate_a11y.py

validate-versions:  ## 校验资源 ?v= 版本号同步
	$(PYTHON) tools/validate_versions.py

validate-links:  ## 校验链接与引用
	$(PYTHON) tools/validate_links.py

validate-cssref:  ## 校验 HTML class 在 styles.css 中有定义
	$(PYTHON) tools/validate_cssref.py

validate-darkmode:  ## 校验暗色模式 token 完整性
	$(PYTHON) tools/validate_darkmode.py

validate-verext:  ## 校验 tokens.json / package.json 版本一致性
	$(PYTHON) tools/validate_verext.py

validate-hardcode:  ## 校验硬编码颜色值（应使用 --ds-* token）
	$(PYTHON) tools/validate_hardcode.py

validate-size:  ## 校验 CSS/JS gzip 体积是否超过阈值
	$(PYTHON) tools/validate_size.py

stamp-version:  ## 将 VERSION 同步到所有 HTML / MD 资源
	$(PYTHON) tools/stamp_version.py

sync-versions:  ## 将 VERSION 同步到 tokens.json、package.json 及 HTML/MD
	$(PYTHON) tools/sync_versions.py

sync-versions:check:  ## 检查版本一致性（不修改文件）
	$(PYTHON) tools/sync_versions.py --check

# ─── 发布自动化 ────────────────────────────────────────────
release-please:  ## 触发 release-please workflow（需要 GitHub CLI）
	@if command -v gh > /dev/null 2>&1; then \
	  gh workflow run release-please.yml; \
	else \
	  echo "GitHub CLI (gh) 未安装。请通过以下方式触发："; \
	  echo "  GitHub → Actions → Release Please → Run workflow"; \
	fi

# ─── 本地预览 ──────────────────────────────────────────────
serve: serve-py  ## 本地启动 HTTP 服务器（默认 8000）

serve-py:  ## Python http.server (LAN accessible via 0.0.0.0)
	@echo "启动 Python HTTP 服务器 (http://0.0.0.0:$(PORT))"
	@echo "局域网地址请查看本机 IP"
	$(PYTHON) -m http.server $(PORT) --bind 0.0.0.0

serve-node:  ## npx serve（备选）
	@echo "启动 Node serve (http://localhost:$(PORT))"
	npx serve -l $(PORT) .

# ─── 资源生成 ──────────────────────────────────────────────
generate-pdfs:  ## 重新生成示例 PDF
	$(PYTHON) tools/generate_pdfs.py

icons:  ## 从 scripts.js 的 ICONS 数组生成 icons.svg sprite
	$(PYTHON) tools/generate_icons.py

icons-check:  ## 校验 icons.svg 是否与 scripts.js 的 ICONS 数组同步（CI 用）
	$(PYTHON) tools/generate_icons.py --check

skill-package: icons generate-pdfs stamp-version  ## 重新打包 SKILL.zip（stamp → icons → PDFs → SKILL）
	$(PYTHON) scripts/package_skill.py

release-package: stamp-version icons generate-pdfs skill-package  ## 完整打包发行 ZIP（stamp → icons → PDFs → SKILL → release ZIP）
	$(PYTHON) scripts/package_release.py

# ─── 测试 ──────────────────────────────────────────────────
test: validate  ## 运行所有测试（当前等价于 validate）
	@echo "✓ 测试完成"

# ─── 清理 ──────────────────────────────────────────────────
clean:  ## 清理临时文件
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -exec rm -rf {} +
	@echo "✓ 已清理"
