<div align="center">

# EDIC Design System

**Editorial × Olive Green — A design system for humans and AI alike**

[![Release](https://img.shields.io/github/v/release/cgartlab/edic-design-system?style=flat-square&color=4a5e2a&label=release)](https://github.com/cgartlab/edic-design-system/releases/latest)
[![CI](https://img.shields.io/github/actions/workflow/status/cgartlab/edic-design-system/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/cgartlab/edic-design-system/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-6b7280?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![Site](https://img.shields.io/badge/site-edic.cgartlab.com-4a5e2a?style=flat-square)](https://edic.cgartlab.com)
[![Skill](https://img.shields.io/badge/AI%20Skill-Claude%20%2F%20Cursor%20%2F%20Kiro-5b6ee1?style=flat-square)](https://edic.cgartlab.com/prompts.html)

[English](#edic-design-system) · [中文](#edic-设计系统)

</div>

---

## What it is

EDIC (**E**ditorial **D**esign **I**nterface for **C**ontent) is a framework-agnostic design system that produces warm, restrained, typographically refined interfaces — built on OKLch color science and a comprehensive token architecture.

It ships as three static files: `styles.css`, `scripts.js`, and `tokens.json`. No build step. No runtime dependencies. Drop them in and it works — in React, Vue, plain HTML, email, or print.

**It is also the first design system built to be understood by AI.** A Claude Code Skill package, structured prompts, and a `references/` directory of on-demand component examples let any AI agent produce EDIC-compliant output without a design background.

---

## At a glance

| | |
|---|---|
| **Design tokens** | 200+ — color, typography, spacing, radius, shadow, motion |
| **Components** | 20 core + 5 add-on, all with dark-mode coverage |
| **Icons** | 100 SVG symbols, 1.5px stroke, `aria-hidden` |
| **Color system** | OKLch-only — perceptually uniform, no hex/rgb guesswork |
| **Dark mode** | `[data-theme="dark"]` + `prefers-color-scheme` media query |
| **CJK support** | Noto Sans/Serif SC, full-width punctuation, optimized tracking |
| **AI integration** | Claude Code Skill · Cursor rules · Kiro steering · Copilot instructions |
| **Engineering** | 10 CI validators, release-please automation, pre-commit hooks |

---

## Quick start

```html
<!doctype html>
<html lang="en" data-theme="">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <button class="ds-btn ds-btn--primary">Get started</button>
    <script src="scripts.js"></script>
  </body>
</html>
```

Full component reference → [edic.cgartlab.com/docs.html](https://edic.cgartlab.com/docs.html)

---

## AI usage

Install the Skill once; every subsequent prompt produces token-driven, accessible, dark-mode-ready output automatically.

**Claude Code**
```bash
mkdir -p .claude/skills/edic-design-system
# Unzip the Skill package from the Downloads page into this directory
```

**Cursor / GitHub Copilot / Kiro** — see [prompts.html](https://edic.cgartlab.com/prompts.html) for platform-specific setup.

**Any LLM** — paste the system prompt from [prompts.html](https://edic.cgartlab.com/prompts.html) into your Custom Instructions.

Skill package: [`skills/edic-design-system/`](./skills/edic-design-system/) · Downloads: [edic.cgartlab.com/downloads.html](https://edic.cgartlab.com/downloads.html)

---

## File layout

```
styles.css                      — tokens, components, dark mode, animations
scripts.js                      — icons, theme toggle, scroll reveal, copy
tokens.json                     — structured token data (machine-readable)

index.html                      — homepage
docs.html                       — component catalog + usage guide
prompts.html                    — AI prompts & Skill package
downloads.html                  — PDFs, token exports, brand assets

blog.html                       — article layout with TOC
company.html                    — company landing page
resume.html                     — printable A4 résumé
report.html                     — multi-page report layout

skills/edic-design-system/      — Claude Code Skill (SKILL.md + references/)
prompts/                        — system-prompt.md, quick-prompt.md
tools/                          — 10 Python validators
scripts/                        — build.py, lint.py, dev.sh, pre-commit.sh
docs/                           — VERSIONING, COMPONENT-DEVELOPMENT, TESTING, RELEASE-CHECKLIST
```

---

## Development

```bash
make serve      # http://localhost:8000
make lint       # all 10 validators (one command)
make build      # lint → stamp → icons → PDFs → Skill ZIP
make validate   # validators individually, with exit-code summary
```

CI runs on every PR and push. All blocking validators must pass before merge.

---

## Deploy

The repository is configured for GitHub Pages out of the box (`CNAME`, `.nojekyll`).

1. **Settings → Pages** — Source: branch `main`, directory `/`.
2. **DNS** — Add a CNAME record pointing to `cgartlab.github.io`.
3. Visit [edic.cgartlab.com](https://edic.cgartlab.com) once the certificate provisions.

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — free to use, modify, and redistribute with attribution.

---
---

<div align="center" id="edic-设计系统">

# EDIC 设计系统

**编辑主义 × 橄榄绿 — 同时面向人类与 AI 的设计系统**

[![Release](https://img.shields.io/github/v/release/cgartlab/edic-design-system?style=flat-square&color=4a5e2a&label=版本)](https://github.com/cgartlab/edic-design-system/releases/latest)
[![CI](https://img.shields.io/github/actions/workflow/status/cgartlab/edic-design-system/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/cgartlab/edic-design-system/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/许可证-CC%20BY%204.0-6b7280?style=flat-square)](https://creativecommons.org/licenses/by/4.0/)
[![Site](https://img.shields.io/badge/官网-edic.cgartlab.com-4a5e2a?style=flat-square)](https://edic.cgartlab.com)
[![Skill](https://img.shields.io/badge/AI%20Skill-Claude%20%2F%20Cursor%20%2F%20Kiro-5b6ee1?style=flat-square)](https://edic.cgartlab.com/prompts.html)

[English](#edic-design-system) · [中文](#edic-设计系统)

</div>

---

## 是什么

EDIC（**E**ditorial **D**esign **I**nterface for **C**ontent，内容编辑设计界面）是一套框架无关的设计系统，基于 OKLch 色彩科学和完整的令牌体系，输出温润克制、排版精良的界面。

它只有三个静态文件：`styles.css`、`scripts.js` 和 `tokens.json`。无需构建步骤，无运行时依赖。放进项目即可使用 — 支持 React、Vue、原生 HTML、邮件模板和打印输出。

**它也是第一套为 AI 理解而设计的设计系统。** Claude Code Skill 包、结构化提示词，以及包含按需加载组件示例的 `references/` 目录，让任何 AI Agent 无需设计背景，即可输出符合 EDIC 规范的界面。

---

## 核心数据

| | |
|---|---|
| **设计令牌** | 200+ — 颜色、字体、间距、圆角、阴影、动效 |
| **组件** | 20 核心 + 5 扩展，全部支持暗色模式 |
| **图标** | 100 个 SVG 符号，1.5px 描边，`aria-hidden` |
| **色彩系统** | 纯 OKLch — 感知均匀，告别 hex/rgb 猜测 |
| **暗色模式** | `[data-theme="dark"]` + `prefers-color-scheme` 媒体查询 |
| **中文支持** | Noto Sans/Serif SC，全角标点，优化字距 |
| **AI 集成** | Claude Code Skill · Cursor 规则 · Kiro Steering · Copilot 指令 |
| **工程治理** | 10 个 CI 验证器，release-please 自动化，pre-commit 钩子 |

---

## 快速开始

```html
<!doctype html>
<html lang="zh-CN" data-theme="">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <button class="ds-btn ds-btn--primary">开始使用</button>
    <script src="scripts.js"></script>
  </body>
</html>
```

完整组件手册 → [edic.cgartlab.com/docs.html](https://edic.cgartlab.com/docs.html)

---

## AI 使用

安装一次 Skill，后续每次提示都会自动输出令牌驱动、无障碍合规、暗色模式就绪的代码。

**Claude Code**
```bash
mkdir -p .claude/skills/edic-design-system
# 从下载页解压 Skill 包到此目录
```

**Cursor / GitHub Copilot / Kiro** — 见 [prompts.html](https://edic.cgartlab.com/prompts.html) 各平台安装说明。

**任意 LLM** — 将系统提示词粘贴到 Custom Instructions 中即可。

Skill 包：[`skills/edic-design-system/`](./skills/edic-design-system/) · 下载：[edic.cgartlab.com/downloads.html](https://edic.cgartlab.com/downloads.html)

---

## 文件结构

```
styles.css                      — 令牌、组件、暗色模式、动效
scripts.js                      — 图标、主题切换、滚动揭示、复制
tokens.json                     — 结构化令牌数据（机器可读）

index.html                      — 首页
docs.html                       — 组件目录 + 使用手册
prompts.html                    — AI 提示词与 Skill 包
downloads.html                  — PDF 参考、令牌导出、品牌资产

blog.html                       — 带目录的文章页布局
company.html                    — 企业官网布局
resume.html                     — A4 可打印简历
report.html                     — 多页报告布局

skills/edic-design-system/      — Claude Code Skill（SKILL.md + references/）
prompts/                        — system-prompt.md、quick-prompt.md
tools/                          — 10 个 Python 验证器
scripts/                        — build.py、lint.py、dev.sh、pre-commit.sh
docs/                           — 版本管理、组件开发、测试、发布清单
```

---

## 本地开发

```bash
make serve      # http://localhost:8000
make lint       # 全部 10 个验证器（一条命令）
make build      # 校验 → 版本戳 → 图标 → PDF → Skill ZIP
make validate   # 逐一运行验证器，输出退出码汇总
```

每次 PR 和推送都会触发 CI，所有阻塞性验证器通过后才允许合并。

---

## 部署

仓库已预配置 GitHub Pages（`CNAME`、`.nojekyll`）。

1. **Settings → Pages** — 来源：`main` 分支，目录 `/`。
2. **DNS** — 添加 CNAME 记录指向 `cgartlab.github.io`。
3. 证书签发后访问 [edic.cgartlab.com](https://edic.cgartlab.com)。

---

## 许可证

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — 可自由使用、修改和再分发，需注明来源。
