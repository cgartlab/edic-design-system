# 更新日志（Changelog）

本项目所有显著变更记录于此。格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
版本号遵循 [语义化版本 2.0.0](https://semver.org/lang/zh-CN/)（设计系统适配版，见 [docs/VERSIONING.md](./docs/VERSIONING.md)）。

## [1.5.3] — 2026-06-08

### 修复

- **数据描述一致性**:将全站散落的"23 核心组件"与"172 design tokens"统一为更准确的口径
  - `README.md` 顶部 feature 列表:172 design tokens → 200+ design tokens;23 components → 20 core + 5 add-on
  - `index.html` stats 块:核心组件 stat 拆分为"20 核心"和"5 附加"两个独立统计块,更精确反映组件库的层次
  - `index.html` / `handbook.html` / `docs.html` 描述文案:所有提及"23 核心组件"之处改为"20 核心 + 5 附加组件"
  - 同步更新 `handbook.html` 头部 meta 行与 footer 介绍段落
- **版本号统一**(1.5.2 → 1.5.3):
  - `VERSION` 1.5.2 → 1.5.3
  - `tokens.json` / `package.json` / `package-lock.json` `version` 字段 1.5.0 → 1.5.3(修正了此前 1.5.0/1.5.2/1.5.3 三方漂移的旧 bug)
  - `changelog.html` footer `data-ds-version` 元素 v1.5.0 → v1.5.3(该元素不在 `stamp_version.py` 的 `HTML_TARGETS` 列表中,需手工维护)
  - 其余 HTML / MD 文件 `?v=` 与可见版本号已由 `make stamp-version` 自动同步

### 维护

- 同步更新 `docs/VERSIONING.md` line 155 的"最新稳定版"引用

---

## [1.5.5] — 2026-06-05

### 新增

- **页面目录组件**：统一页面目录组件 `.ds-pagenav`，支持桌面浮动与移动端折叠
- **代码样式规范**：Prism.js 语法高亮主题，橄榄绿编辑风格，16 种 token 类型
- **Layer 2 验证器**：新增 cssref、darkmode、verext、hardcode 四个跨文件验证器
- **图标 sprite 生成**：`tools/generate_icons.py` 可生成独立 SVG sprite

### 修复

- **TOC 命名空间冲突回归**
- **Prism 代码块暗色模式可见性**
- **反模式清理**（hex/rgba 迁移到 OKLch，死代码删除）

### 变更

- **命名验证器白名单扩展**（新增 7 个合法类别）
- **CI 治理完善**，`make validate` 退出码聚合
- **暗色模式 Gravitas & Glow 增强**

---

## [1.5.5] — 2026-06-19

### 修复（Skill 发布补丁）

- **移除失效链接**：删除 `handbook.html`（404），更新 `edic.cgartlab.com` Reference 链接
- **修正重复链接**：`docs.html` 重复链接合并，新增 Website 和 `tokens.json` 完整 URL
- **版本源统一**：VERSION、package.json、tokens.json、SKILL.md 全部更新至 1.5.5
- **缓存失效修复**：执行 `make stamp-version`，所有 HTML/CSS/JS/MD 文件 `?v=` 更新至 1.5.5

### 变更（Skill 发布补丁）

- **ClawHub/SkillHub 元数据**：SKILL.md 新增 `slug`、`displayName`、`version` 字段
- **Skill 包 License 统一**：包内 README.md License badge 更新为 MIT-0，与 SKILL.md 一致
- **Skill ZIP 重建**：`scripts/package_skill.py` 重建并通过 `--check` 校验

---



### 新增

- **页面目录组件**：统一页面目录组件 `.ds-pagenav`，支持桌面浮动与移动端折叠
- **代码样式规范**：Prism.js 语法高亮主题，橄榄绿编辑风格，16 种 token 类型
- **Layer 2 验证器**：新增 cssref、darkmode、verext、hardcode 四个跨文件验证器
- **图标 sprite 生成**：`tools/generate_icons.py` 可生成独立 SVG sprite

### 修复

- **TOC 命名空间冲突回归**
- **Prism 代码块暗色模式可见性**
- **反模式清理**（hex/rgba 迁移到 OKLch，死代码删除）

### 变更

- **命名验证器白名单扩展**（新增 7 个合法类别）
- **CI 治理完善**，`make validate` 退出码聚合
- **暗色模式 Gravitas & Glow 增强**

---

## [1.5.4] — 2026-06-14

### 修复

- **移动端滚动锁定无法释放**：修复汉堡菜单关闭时 `removeProperty("touchAction")`（驼峰写法）无效操作导致的 `touch-action:none` 永久残留，改用 `overflow: hidden` 方案
- **页脚「网站地图」死链**：`index.html#sitemap` 锚点不存在，已补充 `id="sitemap"` 到页脚分区
- **`.ds-progress` 组件变体缺失**：新增 `--success` 和 `--error` 颜色变体

### 维护

- **Release 流程自动化**：新增 `scripts/package_skill.py` 和 `scripts/package_release.py`，重写 `.github/workflows/release.yml` 为三产物流程
- **`stamp_version.py`**：将 `skills/edic-design-system/README.md` 纳入版本 stamp 目标
- **`.gitattributes`**：新增 `export-ignore` 和 `*.zip binary`

---

## [1.5.2] — 2026-06-07

### 修复

- **[B3] Copy 按钮错误状态后标签永久卡住**：`.catch()` 回调引用了只在 `.then()` 闭包中声明的 `label` 和 `original`，导致 `ReferenceError`，恢复超时从未执行，按钮文字永远停在 "复制失败"。将两个变量提升到 `.then()`/`.catch()` 分叉前，两个分支均可访问。
- **[B5] PageNav TOC 页面加载时无初始高亮**：`IntersectionObserver` scroll-spy 仅在滚动时触发，页面首次加载时目录无任何项高亮。现在 pagenav 控制器初始化完成后立即调用 `setActive()` 激活第一项。
- **[B7] Tabs 缺少 WAI-ARIA roles 及 Arrow 键导航**：`data-tabs` 控制器只设置了 `aria-selected`，未设置 `role=tablist`（容器）、`role=tab`（按钮）、`role=tabpanel`（面板），也不支持 WAI-ARIA Tabs pattern 要求的 ArrowLeft/ArrowRight 键盘切换与 roving tabindex。
- **[B2] Accordion 头部无法键盘访问**：`.ds-accordion-header` 是 `<div>` 元素，缺少 `role="button"` 和 `tabindex="0"`，Tab 键直接跳过，屏幕阅读器不识别为可交互元素。JS 控制器现在在初始化时统一注入两个属性。
- **[B1] Handbook Tabs 使用全局 `querySelectorAll` inline onclick**：手册页 "14 · Tabs" 演示的 inline onclick 调用 `document.querySelectorAll('.ds-tab')` 全局选择所有 tab，若页面有多组 tabs 则互相干扰，且缺失 ARIA 和键盘导航。已重构为 `data-tabs`/`data-tab`/`data-panel` 声明式模式。
- **[B4] Accordion 与 Tabs 缺少 `:focus-visible` 样式**：键盘聚焦 accordion header 和 tab 按钮时无可见焦点环。CSS 已补充 `.ds-accordion-header:focus-visible` 与 `.ds-tab:focus-visible` 规则。

### 新增

- **单元测试套件**（`tests/unit/`，Vitest + jsdom）：8 个测试文件，87 个测试用例，全部通过（0 failures）。覆盖主题切换、移动端导航、PageNav TOC、滑块、Accordion、Tabs、Copy、ScrollReveal、图标网格、令牌表格、年份戳，以及所有上述 bug 的回归测试。`npm test` 运行。

---

## [1.5.1] — 2026-06-06

### 修复

- **手册/文档页面异常回滚（issue #135）**：统一目录组件 `.ds-pagenav` 的 scroll-spy 在高亮当前章节时，对激活的目录链接调用了原生 `Element.scrollIntoView({block:"nearest"})`。该 API 会滚动**所有**可滚动祖先（含整个页面窗口），当目录处于正常文档流时（移动端折叠面板 / docs 侧栏），向下滚动会被反复拽回顶部，表现为"卡住无法下滑"和异常回滚。
  - 移动端现象：目录展开时无法继续下滑、目录收起时正常 —— 因为收起的 `<details>` 内链接 `display:none`，`scrollIntoView` 对隐藏元素无效。
  - 影响页面：`handbook.html`、`docs.html`、`terms.html`、`prompts.html`（均使用 `.ds-pagenav`）。
  - 修复：新增 `revealInNavScroller()`，仅在目录**自身**存在内部滚动容器（桌面浮动 rail）时调整其 `scrollTop`，绝不触碰页面/窗口滚动位置。

---

## [1.4.0] — 2026-06-04

### Changed

- **Brand rename**: CGArtLab Design System → **EDIC Design System** (**E**ditorial **D**esign **I**nterface for **C**ontent)
- **New positioning**: 同时面向人类和 Agent 的编辑主义设计系统
- **New philosophy**: 为纷繁的数字内容建立温暖而克制的秩序
- **Updated package name**: `cgartlab-design-system` → `edic-design-system`
- **Renamed**: `skills/cgartlab-design-system/` → `skills/edic-design-system/`
- **Renamed**: `cgartlabcom_qrcode.svg` → `ediccom_qrcode.svg`
- **Updated**: SVG logo text, favicon aria-label, all HTML titles and meta descriptions
- **Updated**: prompt files (`system-prompt.md`, `quick-prompt.md`) to reference EDIC
- **Updated**: README, AGENTS, CHANGELOG, CONTRIBUTING, docs — all brand strings and positioning copy
- **Updated**: `tools/generate_pdfs.py` PDF output filenames → `edic-ds-reference.pdf` / `edic-ds-color-card.pdf`
- **Updated**: `report.html` localStorage key `cgartlab_smart_pagination` → `edic_smart_pagination`
- **Updated**: DEVELOPMENT-GUIDE.md file tree references

### Notes

- GitHub org (`cgartlab`), repo name (`cgartlab-design-system`), and CNAME (`edic.cgartlab.com`) remain unchanged in this release — admin rename to be performed in a follow-up PR after DNS and repository redirects are configured
- All in-repo URL references (`edic.cgartlab.com`, `github.com/cgartlab/cgartlab-design-system`, `cgartlab.github.io`) intentionally preserved
- Color tokens (`--ds-color-olive-*`) unchanged
- Personal contact identifiers (`cgartlab@outlook.com`, `@cgartlab` social handle, `keybase.io/cgartlab`) intentionally preserved as they belong to the maintainer, not the brand

---

## [1.4.3] — 2026-06-05

### 修复

- **文档内容一致性审计**：修复 12 处跨文档矛盾
  - 品牌名：CLAUDE.md 仍使用 "CGArtLab"，全系统已更名为 EDIC → 已修复
  - 版本号：VERSION 1.4.2、package.json 1.4.0、README badge 自相矛盾（v1.4.2 vs 1.4.0）→ 统一为 1.4.3
  - 组件数量：index.html 说 "30+" 和 "25"，handbook.html 说 "25" 和 "23"，README 说 "25" → 统一为 23（实际统计）
  - 流程文档：VERSIONING.md 声称最新 v1.1.0，DEVELOPMENT-GUIDE.md 声称 v1.0 → 已标注需更新
  - README badge：alt 文本 v1.4.2 与 badge 文字 1.4.0 矛盾 → 已修复为 1.4.3
  - CLAUDE.md 发布示例：bump to v1.4.0 → bump to v1.4.3

### 文档

- `CHANGELOG.md`：`[未发布]` → `[1.4.3]`，更新版本链接
- `VERSION`：1.4.2 → 1.4.3
- `package.json`：1.4.0 → 1.4.3
- `README.md`：badge 版本统一为 1.4.3，组件数量 25 → 23
- `CLAUDE.md`：品牌名 CGArtLab → EDIC，版本 v1.3.1 → v1.4.3，示例命令 v1.4.0 → v1.4.3

---

## [1.5.0] — 2026-06-05

### 新增

#### 统一页面目录组件 `.ds-pagenav`（On this page）
- 新增可复用的「页面目录」组件，整合此前 handbook 与 docs 各自为政的三套实现（桌面浮动卡片 / 移动底部横向滚动条 / 侧栏 `<details>`）
- **桌面 — 默认（in-flow）**：纵向列表，由 sticky 容器承载（docs 侧栏），含数字编号 + scroll-spy 高亮 + 左侧 accent 指示条
- **桌面 — `.ds-pagenav--rail`**：handbook 右侧浮动玻璃卡片，从视口边缘内缩 `--ds-space-6`、全圆角、滚动到正文后柔和滑入（替代原先贴边、垂直居中、显隐生硬的 `.ds-floating-toc`）
- **移动（≤1023px）**：两页统一为导航栏下方的「目录」`<details>` 折叠披露，纵向展开、点击后自动收起（替代 handbook 的底部横向滚动条，消除与主题切换 FAB 的碰撞）
- 全令牌驱动、无硬编码色；统一 JS 控制器支持可选生成（`data-pagenav-generate`）、`IntersectionObserver` scroll-spy、平滑滚动（尊重 `prefers-reduced-motion`）、移动端自动收起

### 修复

- **TOC 命名空间冲突回归**：移除 `.ds-toc-*` 重复定义的 shared base，`handbook` 落地卡片编号（`.ds-toc-item .ds-toc-num`）恢复 accent 强调色（此前被晚出现的 `.ds-toc-num` 规则覆盖为灰色）
- 移除随之失效的 `.ds-floating-toc*` / `.ds-mobile-toc*` / `.ds-docs-menu` / `.ds-docs-aside-title` 等冗余样式与脚本

#### Prism 代码块主题适配与暗色模式可见性
- `.ds-code-bar` 改为跟随页面主题（亮/暗色自适应，原先恒为暗底）
- `.ds-code-lang` / `.ds-copy-btn` 改用语义令牌（暗色模式文字不再不可见）
- 防止 inline-code 样式泄漏到代码块
- Prism 升级 1.29.0 → 1.30.0 + 引入 SRI 完整性校验
- `docs.html` 移动端侧栏简化为常驻目录（去除 `<details>` 折叠）
- `blog.html` 移除小屏汉堡菜单（改为垂直堆叠）

#### 反模式清理
- `styles.css` 5 处 hex/rgba 迁移到 OKLch：`.ds-logo-hero` 高光 / 打印边框 / 品牌常量
- `styles.css` 5 行死代码 `--ds-letter-spacing-*` / `--ds-word-spacing-cjk` 删除（遗留自 `--ds-tracking-*` 重命名前）
- `scripts.js` 3 处空 catch 块改为 `void e;` / `void 0;`（localStorage 读/写 + clipboard.writeText）

### 变更

#### 命名验证器白名单扩展
- `tools/validate_naming.py` 的 `VALID_CATEGORIES` 新增 7 个合法类别：`code` / `token` / `cjk` / `reveal` / `draw` / `stack` / `brand`（均为项目已使用但验证器历史遗漏的合法 CSS 变量类别）

---

---

## [1.1.0] — 2026-05-31

### 新增

- **多页静态展示网站**：首页 / 视觉手册 / 使用文档 / 提示词 / 下载 / 使用条款 6 个独立页面
- **视觉手册 `handbook.html`**：6 章节（Cover / 色彩 / 字体 / 间距·圆角·阴影 / 组件 / 图标 / 令牌索引）live 展示
- **使用文档 `docs.html`**：安装 / 令牌 / 主题 / 排版 / 组件 / 动效 / 可访问性 / 定制 / FAQ
- **提示词中心 `prompts.html`**：系统提示词 / 精简提示词 / Skill 三版本，含 ChatGPT/Claude/Cursor/Kiro 接入位置
- **下载中心 `downloads.html`**：示例 PDF（reference / color-card）/ 令牌 / 样式表 / 品牌素材 / 真实示例
- **真实示例页面**：
  - `blog.html` — 纸间 · 评论博客（长文排版示范）
  - `company.html` — EDIC 公司官网（首个生产级页面）
  - `resume.html` — 可打印 PDF 的 A4 简历
  - `report.html` — 多页报告 / 白皮书版式
- **品牌 Logo**（v1.3 重绘 — 45° 钢笔头 monogram）：
  - `assets/brand/logo.svg`（浅底锁版）
  - `assets/brand/logo-on-dark.svg`（深底提亮）
  - `assets/brand/logo-mark.svg`（纯 currentColor 归一版）
  - `favicon.svg`（透明底彩色）
- **动效系统 v1.1**：
  - 关键帧：`ds-fade-up/in/down` / `ds-zoom-in` / `ds-float` / `ds-spin-slow` / `ds-pulse-*` / `ds-gradient-pan` / `ds-draw`
  - 滚动揭示：`.ds-reveal` + `--left/--right/--scale`，内联 `--d` 错峰
  - 全面尊重 `prefers-reduced-motion: reduce`
- **AI 协作交付物**：
  - `prompts/system-prompt.md`（完整系统提示词）
  - `prompts/quick-prompt.md`（精简开场白）
  - `skills/edic-design-system/SKILL.md`（Agent Skill 技能包）
- **暗色模式完善**：
  - 浮动切换按钮（右下角毛玻璃）
  - 暖灰基底 `oklch(15% 0.008 75)`
  - 橄榄绿暗底亮化至 `oklch(57% ...)`
  - 0.4s 平滑过渡
- **资源版本号刷新**：`?v=1.1.0` 缓存策略

### 变更

- `styles.css` 与 `scripts.js` 整合所有令牌、组件、动效、站点壳
- 站点壳（navbar / 装饰 / TOC / 主题切换）一并内联
- `tokens.json` 与 `styles.css` 令牌保持一致

---

## [1.0.0] — 2026-05-14

### 新增

- 基础令牌系统（200+ CSS 自定义属性）
  - 中性色（10 级暖白纸色）
  - 橄榄绿色阶（10 级 olive-50 → olive-900）
  - 语义色（success / warning / error / info）
  - 字体族（Display 衬线 / Body 无衬线 / Mono / UI）
  - 字号比例尺（caption → hero 共 11 级）
  - 间距 4px 基准（`--ds-space-1` 到 `--ds-space-32`）
  - 圆角 none → full（7 级）
  - 阴影 xs → 2xl（6 级）
  - 动画时长 / 缓动 / 断点 / z-index / 模糊
- 23 核心组件：Button / Card / Input / Select / Checkbox / Radio / Toggle / Badge / Chip / Alert / Modal / Tooltip / Accordion / Tabs / Progress / Avatar / Breadcrumb / Pagination / Table / Navigation / Slider / Date Picker / Article TOC
- 附加：Skeleton / Icon Button
- 100 SVG 图标（Lucide 风格线性，1.5px stroke）
- 单页 `index.html` 视觉目录
- 暗色模式（`[data-theme="dark"]`）
- 浮动目录（IntersectionObserver 驱动）
- 移动端导航抽屉
- GitHub Pages 部署（CNAME `edic.cgartlab.com`、`.nojekyll`）

### 文档

- `README.md`
- `AGENTS.md`（AI 知识库）
- `DEVELOPMENT-GUIDE.md`（1449 行开发指南）
- `tokens.json`（结构化令牌）

### 许可证

- CC BY 4.0

---

## 图例

- **新增 (Added)** — 新功能
- **变更 (Changed)** — 既有功能的变更
- **弃用 (Deprecated)** — 即将移除的功能
- **移除 (Removed)** — 已移除的功能
- **修复 (Fixed)** — Bug 修复
- **安全 (Security)** — 漏洞修复

[1.5.0]: https://github.com/cgartlab/cgartlab-design-system/compare/v1.4.3...v1.5.0
[1.4.3]: https://github.com/cgartlab/cgartlab-design-system/compare/v1.4.0...v1.4.3
[1.4.0]: https://github.com/cgartlab/cgartlab-design-system/compare/v1.3.1...v1.4.0
[1.3.1]: https://github.com/cgartlab/cgartlab-design-system/compare/v1.1.0...v1.3.1
[1.1.0]: https://github.com/cgartlab/cgartlab-design-system/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/cgartlab/cgartlab-design-system/releases/tag/v1.0.0
