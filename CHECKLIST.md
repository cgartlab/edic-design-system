# EDIC Design System 2.0 执行清单

> 初始化状态：本清单已基于当前仓库通读生成，用户已确认直接执行，无需逐项批准。
>
> 执行授权：后续子任务直接推进；不要执行 `git commit` / `git push`，由用户审查结果后自行提交。
>
> 当前版本：`2.0.0`。当前资产：`tokens.json` 276 项，`edic-manifest.json` 39 个组件家族，`icons.json` / `icons.svg` 209 枚图标，`npm run audit` 通过。

## 执行原则

- [x] P0 | S | 依赖：无。确认 2.0 总目标、核心约束与最终验收口径。
  保持编辑主义设计语言、OKLch、框架无关、零运行时依赖、向后兼容；新增内容只允许增量扩展，不删除既有令牌、组件或图标。

- [x] P0 | S | 依赖：无。建立 2.0 工作分支与版本策略。
  新增 `dev-v2-infrastructure` 或等价分支；确定 `VERSION`、`tokens.json.version`、`package.json.version` 的同步时机；暂不提前 bump 到 `2.0.0`，除非所有 P0 均完成。

- [x] P0 | S | 依赖：无。补齐 `npm run audit` 入口。
  当前 `package.json` 没有 `audit` 脚本；新增 `audit` 聚合命令，等价覆盖现有 validators、单元测试、图标同步、视觉基线和新增 2.0 检查。

## A. 设计令牌扩展

- [x] P0 | M | 依赖：P0 工作分支。令牌 2.0 命名审计。
  盘点 `styles.css`、`tokens.json`、`scripts.js` TOKENS 表中的类别缺口；输出分类矩阵：color、font、text、space、radius、border、shadow、motion、z-index、opacity、grid、layout、icon、depth、state。

- [x] P0 | M | 依赖：令牌审计。补齐动效与延迟令牌。
  新增或规范化 `--ds-duration-*`、`--ds-ease-*`、`--ds-delay-*`、`--ds-motion-*`，同步暗色语义如需要，并更新 `tokens.json` 与文档预览。

- [x] P0 | S | 依赖：令牌审计。补齐层级与深度令牌。
  新增或规范化 `--ds-z-*`、`--ds-depth-*`、`--ds-shadow-*` 语义别名，确保 modal、toast、popover、drawer、sticky nav 有明确层级。

- [x] P0 | M | 依赖：令牌审计。补齐边框与栅格令牌。
  新增 `--ds-border-width-*`、`--ds-border-style-*`、`--ds-radius-*` 语义别名、`--ds-grid-*`、`--ds-gutter-*`、`--ds-breakpoint-*`；保持 CSS-only 可用。

- [x] P0 | M | 依赖：边框/栅格令牌。补齐透明度与状态令牌。
  新增 `--ds-opacity-*`、`--ds-disabled-*`、`--ds-focus-*`、`--ds-overlay-*`、`--ds-skeleton-*` 等语义令牌，避免组件内硬编码 alpha。

- [x] P0 | L | 依赖：所有新增类别。建立语义别名层。
  添加 `--ds-color-surface-primary`、`--ds-color-text-primary`、`--ds-color-border-default` 等语义别名映射原始值；保留所有 1.x 令牌不破坏兼容。


- [x] P0 | L | 依赖：语义别名层。升级 `tokens.json` schema。
  将现有 flat token 数据结构扩展为结构化描述：`name`、`value`、`category`、`description`、`aliases`、`dark`、`deprecated`、`status`；提供兼容读取路径，避免 validator 立即断裂。

- [x] P0 | M | 依赖：tokens.json schema。令牌同步校验增强。
  修改或新增 validator，检查 `tokens.json` ↔ `styles.css` 双向完整同步；要求所有新增 token 都有类别、描述、暗色策略或豁免理由。

## B. 组件库扩展

- [x] P0 | M | 依赖：P0 工作分支。组件审计与缺口清单。
  基于 `docs.html`、`styles.css`、`skills/.../SKILL.md` 审计现有 25 个核心组件，标注已有、部分已有、缺失；形成 `docs/component-gap-audit.md`。


- [x] P1 | M | 依赖：组件审计。补齐数据展示组件。
  新增或规范化 Table、Description List、Stat、Timeline；每个组件含 default/hover/focus/active/disabled、暗色模式、ARIA、键盘行为、示例代码。


- [x] P1 | M | 依赖：组件审计。补齐导航组件。
  新增或规范化 Breadcrumb、Pagination、Sidebar Navigation、Steps；确保当前页、键盘顺序、`aria-current`、折叠/展开状态可用。


- [x] P1 | M | 依赖：组件审计。补齐反馈组件。
  新增或规范化 Toast、Alert、Progress、Skeleton；Toast 和 Skeleton 需要无 JS 静态示例与可选 `scripts.js` 交互说明。


- [x] P1 | M | 依赖：组件审计。补齐输入组件。
  新增或规范化 Select、Combobox、Date Picker、Slider、Switch、Radio Group；每个组件有 label、hint、error、disabled、focus-visible、ARIA roles。


- [x] P1 | L | 依赖：组件审计。补齐覆盖层组件。
  新增或规范化 Popover、Tooltip、Drawer、Command Palette；Command Palette 必须支持键盘搜索、Esc 关闭、焦点回收，保持纯静态可选增强。


- [x] P1 | L | 依赖：各类新组件。建立独立组件示例页。
  在 `examples/components/` 下创建每个新增组件的 `.html` 示例页，链接 `styles.css`，展示所有状态、变体、代码块和可访问性说明。


- [x] P1 | M | 依赖：独立示例页。更新 docs.html 组件目录。
  将 2.0 组件纳入 `#visual-components` 与侧边目录；保证组件总数达到 50+，且所有示例在 docs 页面中可交互。


- [x] P1 | M | 依赖：组件扩展。组件级测试补充。
  为新增交互组件增加 Vitest/jsdom 测试，覆盖 DOM 初始化、键盘行为、ARIA 状态切换和 disabled 行为。

## C. 图标系统扩展

- [x] P0 | M | 依赖：P0 工作分支。图标审计与分类规范。
  审计当前 100 枚图标语义类别；定义命名规范 `{category}-{name}-{style}`，例如 `action-search-outline`，并给旧图标建立兼容别名。


- [x] P1 | L | 依赖：图标规范。扩展图标至 200+。
  补充语义类别，覆盖 action、nav、status、data、media、communication、commerce、system、editorial、AI/agent 等；新增到 `scripts.js` ICONS 数组并运行 `make icons`。

- [x] P0 | S | 依赖：图标扩展。图标 sprite 同步。
  运行 `make icons` 与 `make icons-check`，确保 `icons.svg` 使用 `<symbol>` + `<use>` 模式并包含全部图标。

- [x] P0 | M | 依赖：图标扩展。生成 `icons.json` manifest。
  每个图标包含 `name`、`category`、`style`、`keywords`、`viewBox`、`aliases`、`deprecated`；建立 validator 检查 manifest 与 `icons.svg` symbol 数量一致。


- [x] P1 | M | 依赖：icons.json。图标检索与文档展示。
  更新 `docs.html` 图标库，支持分类筛选和关键词搜索；保持无新增运行时依赖，仅使用现有脚本或轻量静态逻辑。

## D. 文档与开发者体验


- [x] P0 | M | 依赖：P0 工作分支。docs.html 信息架构重构。
  将单页文档升级为可搜索、可导航的完整文档站；保留现有 URL 锚点兼容，新增侧边栏分组：Quick Start、Tokens、Components、Icons、AI、Migration、Reference。


- [x] P1 | L | 依赖：docs.html 重构。组件文档模板化。
  为每个组件生成用法说明、API 表格、HTML/CSS 示例、ARIA 说明、状态矩阵、暗色模式说明；优先覆盖新增组件，再补齐旧组件。


- [x] P1 | M | 依赖：组件文档。快速开始指南。
  添加 HTML、React、Vue、Svelte、Email 接入指南；说明如何链接 `styles.css`、使用语义类、处理主题、避免运行时框架依赖。


- [x] P1 | M | 依赖：tokens.json schema。设计令牌参考页。
  添加可视化 token reference，支持按类别筛选，展示 light/dark 值、语义别名、类别说明与复制代码。


- [x] P1 | M | 依赖：2.0 实现进度。1.x 到 2.0 迁移指南。
  添加 `docs/MIGRATION-2.0.md` 并同步到 docs.html；说明非破坏性默认路径、可选语义别名迁移、新增组件替换建议、deprecated 清单。


- [x] P1 | M | 依赖：docs 示例。可复制示例校验。
  建立 validator，抽取 docs 中关键组件代码块，检查其引用的 `ds-*` class 已在 `styles.css` 定义，并可通过空白 HTML 片段直接渲染。

## E. AI 协作能力

- [x] P0 | L | 依赖：tokens.json、组件审计、icons.json。生成 `edic-manifest.json`。
  结构化描述系统能力：tokens、components、icons、patterns、constraints、files、validators、version；Agent 读取一次即可理解使用方式。

- [x] P0 | M | 依赖：edic-manifest.json。编写 `AGENT-GUIDE.md`。
  说明 Agent 使用 EDIC 的硬规则：不要覆盖 token、优先语义 token、禁止硬编码、必须 ARIA、必须暗色兼容、保持 BEM 命名、不引入框架依赖。

- [x] P1 | M | 依赖：AGENT-GUIDE.md。升级 Codex/Claude Skill。
  更新 `skills/edic-design-system/SKILL.md` 和 references，使 Codex 检测到 EDIC 项目时自动加载 2.0 manifest、组件清单、token 类别和反模式。


- [x] P1 | M | 依赖：AGENT-GUIDE.md。AI 空白上下文验收。
  用空白上下文 Agent 测试 `AGENT-GUIDE.md`：要求生成表单页、按钮卡片页、暗色模式页面；检查是否使用 token、ARIA、dark mode、无运行时依赖。

- [x] P1 | M | 依赖：edic-manifest.json。AI manifest 校验。
  新增 validator 检查 manifest 路径存在、组件/图标/令牌引用有效、约束条目完整、版本与 `VERSION` 一致。

## F. 质量与一致性

- [x] P0 | M | 依赖：P0 工作分支。视觉回归基线工具。
  建立轻量 HTML 截图对比机制，不引入重型框架；优先用 Playwright 仅作为 devDependency 或可选脚本，运行时仍保持零依赖。

- [x] P0 | S | 依赖：令牌审计。令牌命名一致性检查。
  扩展 validator，检查所有新增 2.0 token 遵循 `--edic-{category}-{name}` 或当前兼容 `--ds-{category}-{name}`；需明确 2.0 命名策略。

- [x] P0 | M | 依赖：组件审计。组件 ARIA 检查。
  新增 validator，扫描示例页面与 docs 中的交互组件，验证必要 `role`、`aria-*`、label、heading、keyboard 说明。

- [x] P0 | M | 依赖：组件审计。暗色模式覆盖率检查。
  新增或增强 validator，验证每个组件的 CSS 类存在暗色相关 token 使用或明确豁免；覆盖 `[data-theme="dark"]` 与 `prefers-color-scheme: dark`。


- [x] P0 | M | 依赖：全部新增 validator。`npm run audit` 聚合。
  `npm run audit` 必须覆盖 validators、Vitest、图标同步、视觉回归、manifest、ARIA、dark mode、token sync；失败时返回非零退出码。

## G. 发布前收口

- [x] P0 | M | 依赖：所有 P0/P1 子任务。版本同步到 2.0。
  更新 `VERSION`、`tokens.json.version`、`package.json.version` 至 `2.0.0`；运行 stamp/version validators，同步 HTML `?v=`。

- [x] P0 | M | 依赖：版本同步。发布文档更新。
  更新 README、AGENTS、CONTRIBUTING、docs/TESTING、DEVELOPMENT-GUIDE、release checklist，反映 2.0 新能力和验证命令。

- [x] P0 | L | 依赖：发布文档。完整验证通过。
  运行 `npm run audit`、`make validate`、`make icons-check`、单元测试、版本同步检查；全部通过后在清单顶部标记 2.0 完成。

## 完成标记

- [x] EDIC Design System 2.0 完成：所有 P0/P1 子任务勾选，P2 项明确接受或转为后续 backlog，`npm run audit` 全部通过。
