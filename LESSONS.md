# LESSONS — edic-design-system

> CGArtLab 设计系统（纯静态 HTML/CSS/JS，Vitest + `make validate` 10 个验证器，GitHub Pages 部署，release-please 自动发布）。
> 本仓库从真实失误沉淀的「教训→规则」清单。**会话开始先全文阅读并遵循其中所有规则**；出现新失误按 §维护 追加。
> 权威依据：Anthropic Claude Code memory/best practices（<200 行、具体可验证、第二次犯同样错即写入）；社区 lessons.md 惯例（Boris Cherny，Anthropic）。
> 来源：本仓库 AGENTS.md + 真实会话纠错记录（2026-08 至 2026-10）+ 已验证 fix 提交。

## 维护
- **触发**：用户纠正 / Agent 自查到的失误 / 非显而易见的 gotcha。
- **格式**：`### <主题>` 下，每条 = 失误（具体场景）→ 规则（最小可执行指令），一行可验证。
- **只记项目特有、不可从代码推断的**；通用最佳实践不写；含糊措辞（"小心""注意"）删掉。
- **重复出现** → 升级进 `AGENTS.md` 硬规则；**月度审阅**裁剪过期项；目标 < 200 行。

## 设计令牌（最高频违规）

### 禁裸色值，一律 `oklch(var(--ds-*))`
- 失误：直接写 `#3b82f6` / `rgb(...)` / `oklch(0.6 0.2 250)` 字面值 → 规则：颜色必须写成 `oklch(var(--ds-*) / <alpha>)` 引用令牌；`make validate` 会拦（见 AGENTS.md §设计令牌）

### 魔数尺寸改用间距令牌
- 失误：Argus 评审连续报 P1「魔数尺寸」→ 规则：间距/圆角/字号一律用 `--ds-space-*` / `--ds-radius-*` / `--ds-font-*`，不写字面 px（commit e02c84a）

### 令牌值漂移
- 失误：同一令牌在 `styles.css` 与 `tokens.json` 值不一致 → 规则：改令牌必须同改两侧并跑 `make validate`（commit 14b54b9）

### 暗色模式每次新增令牌都要覆盖
- 失误：新增令牌只在浅色定义，暗色下对比度不足 → 规则：任何新 `--ds-*` 必须在 `[data-theme="dark"]` 块内给出覆盖值；图表色需满足 WCAG 1.4.11（3:1）

### 图表禁止手写 SVG
- 失误：用裸 SVG 拼图表，无 X/Y 轴、无交互、配色饱和度过高、字号过小、横轴标签无间距 → 规则：图表必须走统一图表组件（有轴/图例/单位/交互），配色从设计系统取素雅同系色，不得裸 SVG（用户 2026-10 会话明确否决）

### 禁止孤字成行
- 失误：排版出现单个字或短词独占一行 → 规则：所有文本容器加 `text-wrap: pretty` / `balance` 或显式宽度约束，交付前逐页目视检查（用户明确要求「禁止出现一个字或词语短句单独占用一行」）

### CJK 排版
- 失误：中英混排间距、标题平衡失调 → 规则：CJK 文本用 `text-spacing` 与 `text-wrap: balance`；改排版后跑视觉回归（commit e1e527b，closes #310）

## 发布流程（多次翻车区）

### release-please 是唯一发布通道
- 失误：手工 tag 触发 `release.yml` 未触发、本地无 GPG 签名失败 → 规则：发布只走 release-please 自动模型（Release PR 合并 → 自动 tag + Release）；**不要手工打 tag**（commit 67db170）

### manifest 禁止预置未来版本
- 失误：`.release-please-manifest.json` 手动写成 1.10.0 但从未发布（远端无 v1.10.0 tag），导致 release-please 误判为已发布、跳过发布（「幽灵发布」）→ 规则：manifest 只写**已真实发布**的版本；回退见 commit ea4df69

### 版本文件三处必须同步
- 失误：`package.json` / `package-lock.json` / 文档里的版本示例彼此不一致 → 规则：改版本时三处同改，`make validate` 会校验（commit b454442）

### 发布后 Pages 部署要避开竞态
- 失误：post-merge-stamp 与 Pages 部署并发，导致双重部署/取消 → 规则：Pages 部署必须排在 stamp 之后，workflow 加 concurrency 保护（commit d418d27、5ee51c4）

### 发布后视觉基线要刷新
- 失误：发布后视觉回归因版本号差异全红 → 规则：stamp 后自动刷新视觉基线；release PR 上豁免 changelog 同步检查（commit 9c322b8）

### CI 表达式必须加引号
- 失误：`AUDIT_SKIP_VERSION_CHECKS` 表达式未加引号导致 YAML 解析失败 → 规则：workflow 中所有含冒号/特殊字符的表达式值都加引号（commit a72704a）

## 文档一致性

### 组件数量改一处必改全部
- 失误：站点与 skill 文档里的组件数不同步（39 vs 41）→ 规则：组件数量变更需同步站点文案 + skill 文档，`make validate` 校验（commit bedb87a）

### 表格单元格不换行
- 失误：令牌表格单元格自动换行，难以阅读 → 规则：表格单元格加 `white-space: nowrap`，改后附截图（commit 80cc3a5）

### 废弃文档要标记
- 失误：历史 CHECKLIST 被当作现行流程 → 规则：过期文档顶部标注「历史」并指向现行文档（commit b454442）
