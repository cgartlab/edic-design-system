# 更新日志（Changelog）

本项目所有显著变更记录于此。格式基于 [Keep a Changelog](https://keepachangelog.com/en/2.0.0/)，
版本号遵循 [语义化版本 2.0.0](https://semver.org/lang/zh-CN/)（设计系统适配版，见 [docs/VERSIONING.md](./docs/VERSIONING.md)）。

## [1.10.2](https://github.com/cgartlab/edic-design-system/compare/v1.10.1...v1.10.2) (2026-08-14)


### 修复

* **audit:** 修复审计发现的 3 个问题 ([95ff86e](https://github.com/cgartlab/edic-design-system/commit/95ff86e1541710ebd5be0a94401305a3a67b1481))

## [1.10.1](https://github.com/cgartlab/edic-design-system/compare/v1.10.0...v1.10.1) (2026-08-14)


### 修复

* **release:** 发布流程改为 release-please 官方自动 tag 模型 ([88b4276](https://github.com/cgartlab/edic-design-system/commit/88b4276e6bcd2db0a30a13379940537fa2ad2f33))
* **release:** 发布流程改为 release-please 官方自动 tag 模型 ([67db170](https://github.com/cgartlab/edic-design-system/commit/67db17028635ae7b336a8a52ad6e0469bfa5cc47))
* **release:** 响应评审修复 P1/P2/P3（5 条） ([b45701c](https://github.com/cgartlab/edic-design-system/commit/b45701ccf767a4152445112d12e5f8409950a193))


### 文档

* **release:** 同步自动 tag 模型 + 修正版本引用 ([2355c51](https://github.com/cgartlab/edic-design-system/commit/2355c517c277af88ac4bf259dc584cdc4a6f02cc))

## [1.10.0](https://github.com/cgartlab/edic-design-system/compare/v1.9.1...v1.10.0) (2026-08-14)


### 新增

* **charts:** 添加统一 SVG 图表引擎，支持 10 种图表类型 ([9138b88](https://github.com/cgartlab/edic-design-system/commit/9138b88994fe410814f4434be949316887da84ea))
* **charts:** 添加统一 SVG 图表引擎，支持 10 种图表类型 ([2b3800e](https://github.com/cgartlab/edic-design-system/commit/2b3800e9c11c408074b7a97f904b09a7be8e2369))
* **skill:** add references/ directory for R dimension improvement ([#208](https://github.com/cgartlab/edic-design-system/issues/208)) ([afb1a88](https://github.com/cgartlab/edic-design-system/commit/afb1a8813dec328406f077845ead8fdefbe8d19d))
* **skill:** improve TRACE dimensions A/C/E for SkillHub evaluation ([#207](https://github.com/cgartlab/edic-design-system/issues/207)) ([2cd9753](https://github.com/cgartlab/edic-design-system/commit/2cd975343e9779fe8430d8da5290aaf4c8190165))
* **skill:** R2 reliability — patterns, recipes, self-check, bug fixes ([424794f](https://github.com/cgartlab/edic-design-system/commit/424794f148d737394631c2a0eea5e63dd67da552))
* **skill:** R2 reliability — patterns, recipes, self-check, bug fixes ([3fbe59a](https://github.com/cgartlab/edic-design-system/commit/3fbe59a00de2b13f3eb070a0e215e2fa7a359fdc))
* **skill:** R2 reliability — patterns, recipes, self-check, bug fixes ([d55f96f](https://github.com/cgartlab/edic-design-system/commit/d55f96fbeb2aae36bf503ef7bafa8551cba6cff3))
* **skill:** R2 reliability — patterns, recipes, self-check, bug fixes ([d3ce640](https://github.com/cgartlab/edic-design-system/commit/d3ce64019d6f5c59f1e11144a54e2a6024b15c26))
* **skill:** R2 reliability — patterns, recipes, self-check, bug fixes ([5c31735](https://github.com/cgartlab/edic-design-system/commit/5c31735d7175e0d19a138370d6dcbc833701104d))
* **skill:** R2 reliability — PATTERNS, RECIPES, self-check, bug fixes ([5443055](https://github.com/cgartlab/edic-design-system/commit/544305500b1277257999430e91b1e9f47e8a7179))


### 修复

* **blog:** remove inline styles and hardcoded values ([ee61287](https://github.com/cgartlab/edic-design-system/commit/ee6128747f3fb70fdcc2ef48ad3b7cdf16cc924a))
* **blog:** remove inline styles and hardcoded values to comply with design system ([12758ea](https://github.com/cgartlab/edic-design-system/commit/12758ea87b340576a9d96c9d40a7a5eefb61eed3))
* **charts:** aria-label 无标签时用 String(v) 兜底三元表达式 ([a1e6de5](https://github.com/cgartlab/edic-design-system/commit/a1e6de55ea78488d56f3d17ffd2a8cbb5e9ac523))
* **css:** add missing ds-body-lg utility class, fix blog.html class ref ([239cdb0](https://github.com/cgartlab/edic-design-system/commit/239cdb09c279c473f9790f5c9a5e049d10d7d18c))
* **css:** add missing ds-body-lg utility class, fix blog.html class ref ([c527310](https://github.com/cgartlab/edic-design-system/commit/c5273103f00e9febafa2569e3ad37c5e7fabd38f)), closes [#216](https://github.com/cgartlab/edic-design-system/issues/216)
* **pages:** restore section bottom padding ([dfa64a5](https://github.com/cgartlab/edic-design-system/commit/dfa64a57fe2786168bc2410861fa3457cbdf28ef))
* **release:** post-merge-stamp detect gate 改为 manifest（修复 P1 阻断） ([f55da87](https://github.com/cgartlab/edic-design-system/commit/f55da8772366e1e5eb63624dd506af4d0f425627))
* **release:** 修复 post-merge-stamp gate + 同步 AGENTS.md ([3a0c0b3](https://github.com/cgartlab/edic-design-system/commit/3a0c0b3bbce20ee8ae21ae5c088145ada24afc58))
* **release:** 回退 skip-github-release 为 true，恢复手工 tag 发布 ([b3c5954](https://github.com/cgartlab/edic-design-system/commit/b3c595493365d5404e61c812a8f429220d516a61))
* **release:** 回退 skip-github-release 为 true，恢复手工 tag 发布 ([c862400](https://github.com/cgartlab/edic-design-system/commit/c86240013ab5dd54152f7b8d897550953354caf1))
* **release:** 回退幽灵发布 + 简化 post-merge-stamp detect 逻辑 ([ea4df69](https://github.com/cgartlab/edic-design-system/commit/ea4df699516374650420379a21c7658025bd0d77))
* **release:** 清理死 outputs + 同步文档为手工 tag 流程 ([e153cd9](https://github.com/cgartlab/edic-design-system/commit/e153cd9665a1079da0731aea4449c5b17c13bc5e))
* **skill:** correct TOKENS.md version ref; replace 64px with --ds-space-16 in RECIPES.md ([f41065d](https://github.com/cgartlab/edic-design-system/commit/f41065d9885821d932b807ed0d0fe4eda4c3969d))
* **skill:** correct TOKENS.md version ref; replace 64px with --ds-space-16 in RECIPES.md ([83dac31](https://github.com/cgartlab/edic-design-system/commit/83dac3153bddd407a4ff0aa583a8655027a758a5))
* **tooltip:** add JS interaction + ARIA + role=tooltip, replace inline style with class, remove dead CSS, token padding/z-index/gap (closes [#213](https://github.com/cgartlab/edic-design-system/issues/213)) ([93a727b](https://github.com/cgartlab/edic-design-system/commit/93a727b4ba54160c111d0e46f586e702f54f96b6))
* **tooltip:** add JS interaction + ARIA support (closes [#213](https://github.com/cgartlab/edic-design-system/issues/213)) ([4c50a97](https://github.com/cgartlab/edic-design-system/commit/4c50a973cf0862495ad2146109002f1224f12ef8))
* **tooltip:** add JS interaction + ARIA support (closes [#213](https://github.com/cgartlab/edic-design-system/issues/213)) ([5823fa2](https://github.com/cgartlab/edic-design-system/commit/5823fa2798fe13e94337f792106862b4cac06138))


### 文档

* rewrite README — bilingual layout + professional badges ([#209](https://github.com/cgartlab/edic-design-system/issues/209)) ([6f8b336](https://github.com/cgartlab/edic-design-system/commit/6f8b33670761cb9af1fa66695ebf58ae05ab7ed9))

## [Unreleased]

### 新增

### 修复

### 性能优化

### 重构

### 文档

### 样式

## [1.9.1](https://github.com/cgartlab/edic-design-system/compare/v1.9.0...v1.9.1) (2026-06-25)

### 修复

* **version:** 同步 manifest / VERSION 至 1.9.1（版本发布校准）

## [1.9.0](https://github.com/cgartlab/edic-design-system/compare/v1.8.1...v1.9.0) (2026-06-24)


### 新增

* **release:** 手工 tag 触发发布策略 + 自动 changelog 页生成 ([#202](https://github.com/cgartlab/edic-design-system/issues/202)) ([864717c](https://github.com/cgartlab/edic-design-system/commit/864717ca76c505e114b32e9e2f6b08e89c2cf21d))


### 修复

* **release:** add post-upload URL guard to prevent orphaned 'untagged-' asset URLs ([#200](https://github.com/cgartlab/edic-design-system/issues/200)) ([f59c8f5](https://github.com/cgartlab/edic-design-system/commit/f59c8f5a09e077b8f8d38497a0ff02c1e9d249eb))


### 重构

* **changelog:** single-source from CHANGELOG.md + fix Argus review issues ([#204](https://github.com/cgartlab/edic-design-system/issues/204)) ([0db61d6](https://github.com/cgartlab/edic-design-system/commit/0db61d623ed92467d1333a1e8f0a92d822cf4623))

## [1.8.1](https://github.com/cgartlab/edic-design-system/compare/v1.8.0...v1.8.1) (2026-06-24)


### 修复

* **ci:** read release version from manifest in validate_release_notes.py ([6deb3ad](https://github.com/cgartlab/edic-design-system/commit/6deb3ad701e8abcbb1f435f67ee4d7034e11cf0e))
* **release:** sync VERSION from tag name before packaging ([38f817b](https://github.com/cgartlab/edic-design-system/commit/38f817be58023208440a28d09103de8dfaaf9806))
* **skill:** version skill ZIP filename for consistent release naming ([2aac8ba](https://github.com/cgartlab/edic-design-system/commit/2aac8ba735341fbfcc8865212d1e318f1a610ca5))


### 文档

* **prompts:** clarify Step 2 wording in AI collaboration guide ([#195](https://github.com/cgartlab/edic-design-system/issues/195)) ([4bd787b](https://github.com/cgartlab/edic-design-system/commit/4bd787b0ee7a59789ae0914a1ead2f5b2e4a77a1))

## [1.8.0](https://github.com/cgartlab/edic-design-system/compare/v1.7.0...v1.8.0) (2026-06-23)


### 新增

* **automation:** Phase 1+3 — stamp placeholders + changelog generation system ([43da364](https://github.com/cgartlab/edic-design-system/commit/43da364918e7600116348854f6a42eba382816be))


### 修复

* **ci:** skip version validators on Release PR + add post-merge-stamp failure alert ([12c7488](https://github.com/cgartlab/edic-design-system/commit/12c74886ef5d4bef28cae9b28c46cfa2b768c660))
* **templates:** correct version impact table + add fatigue/screenshot warnings ([d2a993f](https://github.com/cgartlab/edic-design-system/commit/d2a993f583ad3fb75faa0a7af7c8f0cd309d5906))

## [1.7.0](https://github.com/cgartlab/edic-design-system/compare/v1.6.1...v1.7.0) (2026-06-23)


### 新增

* add Layer 2 cross-file validators (cssref, darkmode, verext, hardcode) ([#136](https://github.com/cgartlab/edic-design-system/issues/136)) ([cde1c58](https://github.com/cgartlab/edic-design-system/commit/cde1c5867ddb797c41d2b5e4ce4e2ab3a9891de5))
* **automation:** add release-please automated release pipeline ([91098a0](https://github.com/cgartlab/edic-design-system/commit/91098a062411a033d8541ba14745517bbf846ba5))
* brand rename — CGArtLab Design System → EDIC Design System ([#109](https://github.com/cgartlab/edic-design-system/issues/109)) ([#122](https://github.com/cgartlab/edic-design-system/issues/122)) ([241eab0](https://github.com/cgartlab/edic-design-system/commit/241eab0181338308d2a186f90d1cd1074bb4cd93))
* CC BY 4.0 使用条款全面修订 - 法律合规性审查 ([c9b2447](https://github.com/cgartlab/edic-design-system/commit/c9b2447e249849acdc0ae12d223df666366a32bd))
* CGArtLab Design System v1.0 ([5483b25](https://github.com/cgartlab/edic-design-system/commit/5483b2513bb63184d6c16bc61e6751e163f0ffb2))
* **changelog:** add update log page and fix footer links ([8f23b22](https://github.com/cgartlab/edic-design-system/commit/8f23b224084fe57e61c1ac8d149784623cccb63d))
* **changelog:** add update log page and fix footer links ([#144](https://github.com/cgartlab/edic-design-system/issues/144)) ([c268f70](https://github.com/cgartlab/edic-design-system/commit/c268f709b0298be5ef4dbaba5f7897b206a32acf))
* **code:** add Prism.js syntax highlighting + editorial olive-green theme ([add21ed](https://github.com/cgartlab/edic-design-system/commit/add21ed7b46203a72bb67d79885cc466caa6d7ba))
* **code:** add Prism.js syntax highlighting with editorial olive-green theme ([#92](https://github.com/cgartlab/edic-design-system/issues/92)) ([93b00db](https://github.com/cgartlab/edic-design-system/commit/93b00db511558edf6aeaa22efcedc39ede64182f))
* **css:** dark-mode gravitas & glow (v1.5.0) — warm olive undertone layer ([#132](https://github.com/cgartlab/edic-design-system/issues/132)) ([0e96ec8](https://github.com/cgartlab/edic-design-system/commit/0e96ec8d15e1f70b97b6197e138cd2753dad23b1))
* **governance:** add engineering governance layer (v1.3.1) ([#24](https://github.com/cgartlab/edic-design-system/issues/24)) ([ebafaf4](https://github.com/cgartlab/edic-design-system/commit/ebafaf48eb3ffd1cc9242de9a5ae4efb8d1933df))
* **hero:** sliding word cycle, infinite scroll carousel, unified buttons ([#185](https://github.com/cgartlab/edic-design-system/issues/185)) ([#187](https://github.com/cgartlab/edic-design-system/issues/187)) ([4a9bdc4](https://github.com/cgartlab/edic-design-system/commit/4a9bdc420cf0e513432343cfa3c2786adb9f0ad0))
* **icons:** add icons.svg sprite generator with full dev entrypoint integration ([66274c3](https://github.com/cgartlab/edic-design-system/commit/66274c3bb09a493ef6fb73fcdbb1de75206f5ee1))
* **icons:** generate icons.svg sprite file (100 symbols, XML-valid) ([0771b06](https://github.com/cgartlab/edic-design-system/commit/0771b06a9ee75c5cd82c1920406ce4fb7749d8bd))
* implement all 5 open issues ([#147](https://github.com/cgartlab/edic-design-system/issues/147) [#148](https://github.com/cgartlab/edic-design-system/issues/148) [#149](https://github.com/cgartlab/edic-design-system/issues/149) [#150](https://github.com/cgartlab/edic-design-system/issues/150) [#151](https://github.com/cgartlab/edic-design-system/issues/151)) ([#165](https://github.com/cgartlab/edic-design-system/issues/165)) ([8c77952](https://github.com/cgartlab/edic-design-system/commit/8c779522bc2c779102f545faaa4a6d5db565ad1f))
* **mobile-nav:** fullscreen overlay menu — rewrite from scratch ([1cac693](https://github.com/cgartlab/edic-design-system/commit/1cac693bed0ca082c747961443bbc17618c72df8))
* **mobile-nav:** rewrite from scratch — fullscreen overlay menu ([dba64dc](https://github.com/cgartlab/edic-design-system/commit/dba64dced65ec6b464f4aa52a24769f8e9dcfd5d))
* **nav:** frosted-acrylic glass navbar + mobile drawer (dark-mode aware) ([ef817dd](https://github.com/cgartlab/edic-design-system/commit/ef817dde975d1d1ebe981ca3c69fc45124009a09))
* **nav:** frosted-acrylic glass on navbar + mobile drawer (dark-mode aware) ([9101866](https://github.com/cgartlab/edic-design-system/commit/9101866f41c88ea1b2c91553dfde20efb356fa8c))
* **opencode:** add Argus auto PR review workflow ([72be2f4](https://github.com/cgartlab/edic-design-system/commit/72be2f4d5754cd191992e09ba687b72089a50315))
* **opencode:** add Argus GitHub App workflow ([989d14a](https://github.com/cgartlab/edic-design-system/commit/989d14ad0cf358af00c03b8d2d2317bd35c49763))
* **opencode:** add Argus GitHub App workflow ([8f4bae6](https://github.com/cgartlab/edic-design-system/commit/8f4bae602ceab0d3bf1436ac3774fc658674c5e5))
* **opencode:** add auto PR review trigger + app token fix ([4beaeae](https://github.com/cgartlab/edic-design-system/commit/4beaeaef2983db093ac799a1e04784c8ac2f66e1))
* overhaul mobile navigation menu ([48a34bb](https://github.com/cgartlab/edic-design-system/commit/48a34bbbbe68c6feeef104896bbb2f5d9335b13d))
* overhaul mobile navigation menu ([b6941ef](https://github.com/cgartlab/edic-design-system/commit/b6941efb7b287236529f6f3f9d6051c225f12344))
* **toc:** unify handbook/docs/terms TOC into .ds-pagenav component ([#128](https://github.com/cgartlab/edic-design-system/issues/128)) ([96dd95b](https://github.com/cgartlab/edic-design-system/commit/96dd95bb2ea7887a9c8fe9a84e8f8df463a25f9a))
* **tokens:** expand tokens.json from ~30% to ~80% coverage — dark mode colors, breakpoints, z-index, duration, easing, shadow, tracking, leading, weight scales (closes [#38](https://github.com/cgartlab/edic-design-system/issues/38), [#45](https://github.com/cgartlab/edic-design-system/issues/45)) ([4ce6f0d](https://github.com/cgartlab/edic-design-system/commit/4ce6f0dadec75695f49c0b8efbe6974d8d0abff8))
* **tools:** add icons.svg generator from scripts.js ICONS array ([55e8e07](https://github.com/cgartlab/edic-design-system/commit/55e8e07106f5cc3169b534d4453be520b832b4ee))
* **tools:** add stamp_version.py and dynamic VERSION reading in PDF ([cf872c6](https://github.com/cgartlab/edic-design-system/commit/cf872c6061b9cab0959d69fc3f848516c7cfaf81))
* unify version stamping across all project files ([#180](https://github.com/cgartlab/edic-design-system/issues/180)) ([7395b6a](https://github.com/cgartlab/edic-design-system/commit/7395b6a817e6b55f1ddf69872ab76a66ba30281a))
* v1.1 — multi-page showcase website, brand logo, motion system, AI prompts & Skill ([c9b6dbc](https://github.com/cgartlab/edic-design-system/commit/c9b6dbc24dd2eb528b696651679b893b6beb4fae))
* v1.1 — 展示网站 + 品牌 Logo + 动效 + AI 提示词/Skill ([11cc375](https://github.com/cgartlab/edic-design-system/commit/11cc375ee1aa0b14bbe1d962e203d4e7af4916e4))
* **versions:** apply stamp_version to all HTML and MD resources ([57007da](https://github.com/cgartlab/edic-design-system/commit/57007da1ad328d00e7594a241f2bca6806127e3d))
* **versions:** introduce stamp_version.py for centralized version sync ([0cf1e0c](https://github.com/cgartlab/edic-design-system/commit/0cf1e0c4bfe1ec00c46e4f33c33617df6083d2ac))
* 合并视觉手册内容到文档页面 ([#164](https://github.com/cgartlab/edic-design-system/issues/164)) ([375db30](https://github.com/cgartlab/edic-design-system/commit/375db300e6ad57a9ce2abbf55e770b7a9fc84ef5))
* 完成设计系统v1.0正式版本发布 ([321aae6](https://github.com/cgartlab/edic-design-system/commit/321aae6c393ca6e95b0b118c74d71246aac380b6))
* 新增公司官网第二版本页面及关联配置文件 ([f43a18d](https://github.com/cgartlab/edic-design-system/commit/f43a18d1e7567b480df4c981340e46313544701e))
* 重构主题切换按钮，整合到导航栏并优化移动端体验 ([5e33f28](https://github.com/cgartlab/edic-design-system/commit/5e33f289602ec7d67952df5cbf22d8141341f557))


### 修复

* **#124:** 下载页面核心资源板块改为两排三列布局 ([#133](https://github.com/cgartlab/edic-design-system/issues/133)) ([618aa46](https://github.com/cgartlab/edic-design-system/commit/618aa46dcbc6ada6d27d658c6e9e4fc4f44b029a))
* **#167 #175:** replace bare oklch in company.html + styles.css with tokens ([#177](https://github.com/cgartlab/edic-design-system/issues/177)) ([bf1e0af](https://github.com/cgartlab/edic-design-system/commit/bf1e0af92f2fec4e958f510813ea2de60079d084))
* **#168 #169 #170:** add changelog.html to stamp targets, scripts.js version placeholder, footer-end div ([#178](https://github.com/cgartlab/edic-design-system/issues/178)) ([4791ea4](https://github.com/cgartlab/edic-design-system/commit/4791ea47b4c4028bc768bd4877a12d219d3ebd14))
* **#174:** Fix validate_hardcode.py bugs and replace bare oklch in styles.css ([#176](https://github.com/cgartlab/edic-design-system/issues/176)) ([fb1c693](https://github.com/cgartlab/edic-design-system/commit/fb1c693cef49510fe0d2e481dc7d42198cd6da4e))
* **#hero:** remove hero background glow, enable LAN serve, add preview workflow docs ([#182](https://github.com/cgartlab/edic-design-system/issues/182)) ([93cb008](https://github.com/cgartlab/edic-design-system/commit/93cb008f170bb507ca133c1f1901e2b1e88ac290))
* **a11y:** add :focus-visible to .ds-toc-item for keyboard navigation (closes [#75](https://github.com/cgartlab/edic-design-system/issues/75)) ([c65faa6](https://github.com/cgartlab/edic-design-system/commit/c65faa6570e99b1de4384ed0ec5e624fdf667427))
* **a11y:** add forced-colors rule for .ds-gradient-text to fix WHCM visibility (closes [#70](https://github.com/cgartlab/edic-design-system/issues/70)) ([8349072](https://github.com/cgartlab/edic-design-system/commit/8349072ae2276eba9cfa068199bf84cb5e77c6d4))
* **a11y:** add main landmark + fix skip-link target across 5 pages (closes [#73](https://github.com/cgartlab/edic-design-system/issues/73)) ([a8e841b](https://github.com/cgartlab/edic-design-system/commit/a8e841b3f3a00b4ff3731e10fedc32c903c3659f))
* **a11y:** add prefers-color-scheme: dark CSS fallback for dark-system users before JS loads (closes [#54](https://github.com/cgartlab/edic-design-system/issues/54)) ([dbe4996](https://github.com/cgartlab/edic-design-system/commit/dbe4996c977f8e9c5cf8db3d3efe2203ef872b6c))
* **a11y:** restructure resume.html cards to fix nested anchor/block-level invalid HTML (closes [#59](https://github.com/cgartlab/edic-design-system/issues/59)) ([2b53381](https://github.com/cgartlab/edic-design-system/commit/2b53381e4750a05792abe6c22273ac472e755679))
* add meta descriptions to 4 HTML files ([#114](https://github.com/cgartlab/edic-design-system/issues/114)) ([766a83c](https://github.com/cgartlab/edic-design-system/commit/766a83c59e62b02b5d658fd72e45adf454fd04eb))
* bump asset cache-busting version 1.1.5 -&gt; 1.2.0 ([3ca9c65](https://github.com/cgartlab/edic-design-system/commit/3ca9c65182f0e05ebb733f0ff4f06cefc0ec187c))
* bump asset version v1.1.5 -&gt; v1.2.0 (cache-bust the mobile nav) ([b869844](https://github.com/cgartlab/edic-design-system/commit/b869844a158829878e042eb8e1d83f6809f14bab))
* **ci:** align release.yml checkout action to [@v5](https://github.com/v5) matching ci.yml (closes [#43](https://github.com/cgartlab/edic-design-system/issues/43)) ([665ef2d](https://github.com/cgartlab/edic-design-system/commit/665ef2d88989bb253b9f8285e2c5110de8bd7b52))
* **CI:** exclude continue-on-error validators from blocking check + improve pre-commit hook ([09463a7](https://github.com/cgartlab/edic-design-system/commit/09463a727d124a97d26e46f300098890ecfed30a))
* **ci:** lock playwright version in CI workflow for reproducible builds ([#88](https://github.com/cgartlab/edic-design-system/issues/88)) ([583315a](https://github.com/cgartlab/edic-design-system/commit/583315a017fa991b19419ae6a3181f278fc25c41))
* **ci:** root cause - replace bash ternary with if/elif exit code handling ([#127](https://github.com/cgartlab/edic-design-system/issues/127)) ([0629392](https://github.com/cgartlab/edic-design-system/commit/0629392a470a7b5ea0b52cdcc6af02ddf730fbf5))
* **code:** Prism code-block theming + OKLch migration of pre-existing anti-patterns ([#110](https://github.com/cgartlab/edic-design-system/issues/110)) ([f088a5b](https://github.com/cgartlab/edic-design-system/commit/f088a5bca69bea1f52b05bc6b0120534077197ce))
* correct CC BY 4.0 adapter-license freedom per Codex review ([01b94b2](https://github.com/cgartlab/edic-design-system/commit/01b94b2b23f228e9b5acae560cbc47d91ccf379c))
* **critical-c4:** add auto-dismiss functionality to Toast component ([#161](https://github.com/cgartlab/edic-design-system/issues/161)) ([28eb3e6](https://github.com/cgartlab/edic-design-system/commit/28eb3e6f6403a9032aadfa69b08e8e0002170175))
* **css:** .ds-table-wrap 健壮性 — a11y 焦点环 + overflow-y 显式声明 ([#121](https://github.com/cgartlab/edic-design-system/issues/121)) ([56a3eab](https://github.com/cgartlab/edic-design-system/commit/56a3eabbe7b96e8baddf92a63af9a46815ba1715))
* **css:** add min-width:0/max-width:100% to .ds-compat-item for narrow-viewport overflow fix (closes [#71](https://github.com/cgartlab/edic-design-system/issues/71)) ([f263cbd](https://github.com/cgartlab/edic-design-system/commit/f263cbdb192bcf4668b44d78b5dccc9ed0e96f3a))
* **css:** make .ds-footer-brand span full width at tablet breakpoint (closes [#77](https://github.com/cgartlab/edic-design-system/issues/77)) ([728f9ba](https://github.com/cgartlab/edic-design-system/commit/728f9baa6516030f818266b008ce474df4b9bdf6))
* **css:** remove ::before/::after pseudo-elements from .ds-hero-meta for IE compatibility (closes [#69](https://github.com/cgartlab/edic-design-system/issues/69)) ([6f75e29](https://github.com/cgartlab/edic-design-system/commit/6f75e29aecca24518df655010e0b43a842520ce9))
* **css:** remove body duplicate transition, page-btn white token, report.html meta (closes [#53](https://github.com/cgartlab/edic-design-system/issues/53), [#55](https://github.com/cgartlab/edic-design-system/issues/55), [#57](https://github.com/cgartlab/edic-design-system/issues/57)) ([7de4249](https://github.com/cgartlab/edic-design-system/commit/7de4249d1c297dd64f093def263f6d9f4f6c36a3))
* **css:** remove duplicate overflow-wrap from .ds-text-cjk to fix self-override (closes [#36](https://github.com/cgartlab/edic-design-system/issues/36)) ([e0a1a40](https://github.com/cgartlab/edic-design-system/commit/e0a1a407c84871d3fb383e48225bed01944f4758))
* **css:** touch-safe hover for .ds-feature-card + responsive .ds-stat-num clamp (closes [#72](https://github.com/cgartlab/edic-design-system/issues/72), [#74](https://github.com/cgartlab/edic-design-system/issues/74)) ([f388d2e](https://github.com/cgartlab/edic-design-system/commit/f388d2eedf43c8714d227be680a9538f62b4858f))
* **css:** unify handbook pagenav spacing, fix responsive overflow and stale versions ([#134](https://github.com/cgartlab/edic-design-system/issues/134)) ([ac7b8b9](https://github.com/cgartlab/edic-design-system/commit/ac7b8b9c9058297567e702fab516ca9f70f0ec3d))
* **css:** 桌面端浮动 TOC 重设计 + 移动端 TOC 不再遮挡主题切换按钮 ([#123](https://github.com/cgartlab/edic-design-system/issues/123)) ([739b91b](https://github.com/cgartlab/edic-design-system/commit/739b91bd3a6f9f1da893988170688d64b71ff893))
* **design-system:** replace bare oklch in report.html and resume.html with --ds-* tokens ([#173](https://github.com/cgartlab/edic-design-system/issues/173)) ([1e3b066](https://github.com/cgartlab/edic-design-system/commit/1e3b0667ce3870e37756bcfa804162e530f90bd2)), closes [#166](https://github.com/cgartlab/edic-design-system/issues/166)
* **design-system:** resolve all verified style inconsistencies and hardcoded values ([#172](https://github.com/cgartlab/edic-design-system/issues/172)) ([6bfb5fc](https://github.com/cgartlab/edic-design-system/commit/6bfb5fc5515500bb296bf1194d8f154f5883d93b))
* div balance in handbook + add skip-to-content, robots.txt, sitemap, og:image ([d7f116a](https://github.com/cgartlab/edic-design-system/commit/d7f116a2c136463e0ca178c9aed348f0124cfe5b))
* **docs:** resolve 16 cross-document contradictions for v1.4.3 ([#131](https://github.com/cgartlab/edic-design-system/issues/131)) ([d6352dc](https://github.com/cgartlab/edic-design-system/commit/d6352dc6388e4e5eeda365d8f41bd9ba8f5d368a))
* **docs:** 冒烟测试 fix 触发 release-please ([8432100](https://github.com/cgartlab/edic-design-system/commit/84321001648d78b342332574457205269a74f1c4))
* **footer:** replace h3 with semantic p.ds-footer-col-heading ([6ed7378](https://github.com/cgartlab/edic-design-system/commit/6ed7378bf1e72905b231191e05277382c16e9887))
* **footer:** update copyright to CGArtLab, add blog link, move sitemap under 关于 ([fc80606](https://github.com/cgartlab/edic-design-system/commit/fc806064000579a94764469941c68677ce56b7d8))
* **footer:** update copyright to CGArtLab, add blog link, move sitemap under 关于 ([665ac08](https://github.com/cgartlab/edic-design-system/commit/665ac08761e9dd973e738363b167f5f21f9814bd))
* **footer:** 替换 h3 为语义化 p.ds-footer-col-heading ([#145](https://github.com/cgartlab/edic-design-system/issues/145)) ([477e441](https://github.com/cgartlab/edic-design-system/commit/477e44115e2b41d1c6172e4fcea21d43b1456d71))
* **handbook:** close 640-1023px TOC dead zone, fix mobile active state, unify base ([#125](https://github.com/cgartlab/edic-design-system/issues/125)) ([891d715](https://github.com/cgartlab/edic-design-system/commit/891d7158edde6a1cc65022048ee4ad48e0ad7822))
* **handbook:** extract timeline/contact into standalone sections for TOC navigation ([e7c969a](https://github.com/cgartlab/edic-design-system/commit/e7c969a17b42f486800572922af909e2ab8ef8d3))
* **handbook:** extract timeline/contact into standalone sections for TOC navigation ([#129](https://github.com/cgartlab/edic-design-system/issues/129)) ([58be16f](https://github.com/cgartlab/edic-design-system/commit/58be16ff9ac45151e705ecdc10cc6e84672edf3d))
* **handbook:** mobile overflow protection for #typography inline-style tables ([#117](https://github.com/cgartlab/edic-design-system/issues/117)) ([6bc734c](https://github.com/cgartlab/edic-design-system/commit/6bc734c0078b229769bab474be7cbeab2778a19c))
* **handbook:** mobile spacing — cover eyebrow gap 24→16px, pagenav top margin 16px ([#137](https://github.com/cgartlab/edic-design-system/issues/137)) ([0950f1d](https://github.com/cgartlab/edic-design-system/commit/0950f1d913b615d3dcd90fbf4e6f3c8ca23e7a9a))
* **handbook:** remove C,G subtitle and add TOC top margin on mobile ([8294b71](https://github.com/cgartlab/edic-design-system/commit/8294b719741e587fb943072364b67bf4e55cd13d))
* **handbook:** remove hidden pagenav from mobile layout — eliminates blank gap ([7272c1e](https://github.com/cgartlab/edic-design-system/commit/7272c1eb698c50c2507f04a59cdff5d90d61cb16))
* **html:** add scripts.js to blog.html to enable theme/dark mode and all progressive enhancements (closes [#41](https://github.com/cgartlab/edic-design-system/issues/41)) ([8a1cab2](https://github.com/cgartlab/edic-design-system/commit/8a1cab200b34ba1cfda82f016cc0672a75a59410))
* **html:** rename duplicate theme-toggle-btn id to theme-toggle-btn-fixed on floating buttons (closes [#31](https://github.com/cgartlab/edic-design-system/issues/31)) ([5ecfcb8](https://github.com/cgartlab/edic-design-system/commit/5ecfcb82679ccf1046dfe659c4b1f1e0efb32c77))
* **icons:** add presentation attributes to SVG sprite symbols ([a7c8281](https://github.com/cgartlab/edic-design-system/commit/a7c8281ce1bdecd9e3bfd1e99e83f49d2a10eeee))
* increase mobile drawer glass opacity to 92-94% + cache-bust CSS/JS ([f407c1a](https://github.com/cgartlab/edic-design-system/commit/f407c1a45c0d21b506f063aed4af3c1325c86b78))
* **index:** differentiate CTA button hierarchy - primary/secondary/ghost ([#76](https://github.com/cgartlab/edic-design-system/issues/76)) ([f689417](https://github.com/cgartlab/edic-design-system/commit/f689417d7118cdae98d8151a95413eafc2a8e3b2))
* **index:** spec compliance — 8 issues across styles.css & index.html (v1.6.2) ([#191](https://github.com/cgartlab/edic-design-system/issues/191)) ([eef3991](https://github.com/cgartlab/edic-design-system/commit/eef3991740a99cfc14e5bc2519e5ba401992f60a))
* **index:** widen CTA container and remove measure constraint to prevent single-character orphan ([#91](https://github.com/cgartlab/edic-design-system/issues/91)) ([5bf1145](https://github.com/cgartlab/edic-design-system/commit/5bf11458938300adc24735d7ec47e3fda5069af0))
* **interactions:** 5 UI/a11y bugs + 87-test unit suite (v1.5.2) ([#159](https://github.com/cgartlab/edic-design-system/issues/159)) ([7fdbc1b](https://github.com/cgartlab/edic-design-system/commit/7fdbc1b4936cc5d33cf384173f0da817dce03fe2))
* **interactions:** a11y, copy feedback, memory leaks, and AGENTS.md rewrite ([8365173](https://github.com/cgartlab/edic-design-system/commit/8365173b93f462672d33595b375e2ec5b776f311))
* **interactions:** a11y, copy feedback, memory leaks, and AGENTS.md rewrite ([#141](https://github.com/cgartlab/edic-design-system/issues/141)) ([05d2e17](https://github.com/cgartlab/edic-design-system/commit/05d2e17281f1ac581cb8c0e4dbd8b63714e8bf86))
* **js:** cycleTheme reads data-theme-mode instead of parsing Chinese aria-label (closes [#34](https://github.com/cgartlab/edic-design-system/issues/34)) ([5d0e95f](https://github.com/cgartlab/edic-design-system/commit/5d0e95fdeec49b2b142d7db7d43004a433aca56c))
* **js:** TOC IntersectionObserver picks topmost section, adds 16ms debounce to prevent rapid flicker (closes [#58](https://github.com/cgartlab/edic-design-system/issues/58)) ([3ffb7ce](https://github.com/cgartlab/edic-design-system/commit/3ffb7cef378b05c062d3f4725c91ba9de3fee7ff))
* **makefile:** use cross-platform clean with -delete for .pyc files ([#80](https://github.com/cgartlab/edic-design-system/issues/80)) ([f4fe514](https://github.com/cgartlab/edic-design-system/commit/f4fe514e0bd4a779fae8e03798b4e35e2af7c0ee))
* **misc:** bump stale v1.0 version comments to v1.3.1 in styles.css and scripts.js (closes [#47](https://github.com/cgartlab/edic-design-system/issues/47)) ([8e5d782](https://github.com/cgartlab/edic-design-system/commit/8e5d7820ea55906b12ca250e07ad5bc11d51eee3))
* **mnav:** let mobile menu links navigate without aborting page load ([#154](https://github.com/cgartlab/edic-design-system/issues/154)) ([22cd13f](https://github.com/cgartlab/edic-design-system/commit/22cd13faed57987f237b1469c7f75f0340defaa9))
* mobile drawer — revert to solid background, remove backdrop-filter ([85745ac](https://github.com/cgartlab/edic-design-system/commit/85745acd0d322f1f71e0e1afafe45602b0b9cf7a))
* mobile nav drawer solid background + document mobile nav spec ([f52c293](https://github.com/cgartlab/edic-design-system/commit/f52c293089d58e1e4ab2d28a3c034303becaaafa))
* mobile nav drawer uses frosted glass (blur-xl + 78% opacity) ([7f2396b](https://github.com/cgartlab/edic-design-system/commit/7f2396b54bcfdb458370e2ff67d335eee38146cc))
* mobile navbar fully opaque + hamburger button with visible border ([7bd507c](https://github.com/cgartlab/edic-design-system/commit/7bd507c51ecf10b8ad3cc101ea0eddabc116eb29))
* **mobile-nav:** 3-bar hamburger, slide-in drawer with backdrop dimming ([075b503](https://github.com/cgartlab/edic-design-system/commit/075b503d20048341a7bf6408fdd589f4d684edd5))
* **mobile-nav:** cohesive solid menu + fix backdrop stacking-context bug ([83f7348](https://github.com/cgartlab/edic-design-system/commit/83f7348b1732af34872d4e5684f281f8b8c528d0))
* **mobile-nav:** cohesive solid menu, fix backdrop stacking over drawer ([9a791aa](https://github.com/cgartlab/edic-design-system/commit/9a791aa27b13c5e69f6db0db648dabecc08f61d4))
* **mobile-nav:** double rAF delay to override iOS Safari scroll restoration ([d97e2db](https://github.com/cgartlab/edic-design-system/commit/d97e2dbd316cf85965c1a885450fb386b5fcc179))
* **mobile-nav:** improve menu interaction and scroll behavior ([73b7fc7](https://github.com/cgartlab/edic-design-system/commit/73b7fc70bd033ad5f956e0c996c6f4f7d2ae3712))
* **mobile-nav:** include trigger button in focus trap ([a0180a8](https://github.com/cgartlab/edic-design-system/commit/a0180a8ded8eaeb7edc88bb4e18320ef73c346ba))
* **mobile-nav:** overhaul mobile drawer UI ([304d55f](https://github.com/cgartlab/edic-design-system/commit/304d55f8c765de6bc6e63526bcfb7e9f56888733))
* **mobile-nav:** overhaul mobile drawer UI — overlay blur, divider lines, hover slide, cleaner hamburger ([cf66e72](https://github.com/cgartlab/edic-design-system/commit/cf66e72d5de14b7a84393c8c632627a73ad68adc))
* **mobile-nav:** proper scroll locking and version bump to v1.5.1 ([14c8e59](https://github.com/cgartlab/edic-design-system/commit/14c8e5919d9762a749cc977e2b0c51b8e20d5a83))
* **mobile-nav:** reconcile PR[#9](https://github.com/cgartlab/edic-design-system/issues/9)/[#10](https://github.com/cgartlab/edic-design-system/issues/10) into one coherent best version ([c5a1f44](https://github.com/cgartlab/edic-design-system/commit/c5a1f44b3605b155a65f54cf19eaea9022077a7d))
* **mobile-nav:** reconcile PR[#9](https://github.com/cgartlab/edic-design-system/issues/9)/[#10](https://github.com/cgartlab/edic-design-system/issues/10) merge into one coherent best version ([316db72](https://github.com/cgartlab/edic-design-system/commit/316db7293c3eac5aa3da70d5bb5d4fffeca2c5f2))
* **mobile-nav:** remove dialog role from desktop nav, save/restore body overflow styles ([94b5fa3](https://github.com/cgartlab/edic-design-system/commit/94b5fa3ab3618e53147baeab942a5d5f17641e8c))
* **mobile-nav:** remove dialog role from desktop nav, save/restore body overflow styles, add aria-label ([b05cb27](https://github.com/cgartlab/edic-design-system/commit/b05cb27c72e9e111562d0e27e6ed320bcdda2fb0))
* **mobile-nav:** replace position:fixed with overflow:hidden approach ([d32bbcc](https://github.com/cgartlab/edic-design-system/commit/d32bbcce7dd189fc1a987d9883270190a5c86212))
* **mobile-nav:** resolve Codex review residual issues ([58e37c5](https://github.com/cgartlab/edic-design-system/commit/58e37c534b5431f830df43dfd72cb94cbe158138))
* **mobile-nav:** restore saved body overflow unconditionally, add align-items:stretch ([6b87efb](https://github.com/cgartlab/edic-design-system/commit/6b87efb518a6fa172134169e4a4fe800eaba984d))
* **mobile-nav:** set scroll position BEFORE removing position:fixed ([53ad3eb](https://github.com/cgartlab/edic-design-system/commit/53ad3eb1ee99fd1c027a012e31335365248fb55b))
* **mobile-scroll:** add explicit touch-action to TOC disclosure on mobile ([0a4468f](https://github.com/cgartlab/edic-design-system/commit/0a4468f1631e0d0b9a23ee2aa8dee97dc18cf62b))
* **mobile-scroll:** change ds-pagenav-disclosure overflow to visible on mobile ([ecb3e0f](https://github.com/cgartlab/edic-design-system/commit/ecb3e0f66a0717714883936de08bfbe7f28ff19c))
* **mobile-scroll:** use overscroll-behavior contain on disclosure and list ([31bb921](https://github.com/cgartlab/edic-design-system/commit/31bb92130af72a13a9f2392c33efdf3f829d115c))
* **mobile:** release scroll lock reliably; fix sitemap dead link ([236da9c](https://github.com/cgartlab/edic-design-system/commit/236da9cd304b9d29eb2e2a92104d911c11dc16e8))
* **mobile:** release scroll lock reliably; fix sitemap dead link ([#142](https://github.com/cgartlab/edic-design-system/issues/142)) ([3a3a552](https://github.com/cgartlab/edic-design-system/commit/3a3a5520965fbd2798d31eb3bad25982859e33ca))
* **opencode:** add git identity config ([f91e6d1](https://github.com/cgartlab/edic-design-system/commit/f91e6d172c0ad9cd6333458eca7cefd4dc48caf4))
* **opencode:** add git identity config for Argus bot ([2fd42d9](https://github.com/cgartlab/edic-design-system/commit/2fd42d9db1bf793b25fb229fe24e8e5f2c5bfb4a))
* **opencode:** add git identity config, fix CRLF corruption ([95dd4c9](https://github.com/cgartlab/edic-design-system/commit/95dd4c9c23d0a4dcf94e08353c49c12881189ef7))
* **opencode:** add git remote with app token for push permissions ([451fe77](https://github.com/cgartlab/edic-design-system/commit/451fe77fc33f049dafed4f8cdd59a4486bd85f47))
* **opencode:** add guoxue and fix git push permissions via x-access-token URL ([e37c29c](https://github.com/cgartlab/edic-design-system/commit/e37c29c6c01aa23ac4a57669dc7747198e1c48d4))
* **opencode:** add id-token:write, remove invalid token input, skip synchronize ([9cc4634](https://github.com/cgartlab/edic-design-system/commit/9cc46343397b4b776af844a507fe680153ca4831))
* **opencode:** persist-credentials false + app token remote ([c63fdd9](https://github.com/cgartlab/edic-design-system/commit/c63fdd900b4c95721546d282e4e76ad4e5ff66a8))
* **opencode:** persist-credentials false + x-access-token remote ([962d770](https://github.com/cgartlab/edic-design-system/commit/962d77084e15608e9d405a003e49a6cb864893c9))
* **opencode:** remove persist-credentials false, keep remote override ([12b3c6f](https://github.com/cgartlab/edic-design-system/commit/12b3c6fe3a24bc708efa763139e79055ec3f27ac))
* **opencode:** use credential helper store instead of remote URL token ([88710ef](https://github.com/cgartlab/edic-design-system/commit/88710ef9eb06b804f4f043854d3e3767d8e580a7))
* **opencode:** use token input instead of use_github_token for PR auto-review ([cfbd9a7](https://github.com/cgartlab/edic-design-system/commit/cfbd9a771979e3bfceb2944a81f84f4cdfabdd61))
* **pagenav:** stop scroll-spy from yanking the whole page (issue [#135](https://github.com/cgartlab/edic-design-system/issues/135)) ([be09bed](https://github.com/cgartlab/edic-design-system/commit/be09bed64e4247e23583c2ed73706de330078062))
* **pagenav:** stop scroll-spy from yanking the whole page (issue [#135](https://github.com/cgartlab/edic-design-system/issues/135)) ([#143](https://github.com/cgartlab/edic-design-system/issues/143)) ([5a7602e](https://github.com/cgartlab/edic-design-system/commit/5a7602eb2f295148a8f0d16d4f3d4fe7cf8d73bf))
* **pages:** migrate to workflow-based Pages + restore v1.6.0 stamp ([dbd26c2](https://github.com/cgartlab/edic-design-system/commit/dbd26c28a80fdcb2dbfbc574e5542a8f5b3df693))
* prepend the trigger to the focusable elements array so Tab ([a0180a8](https://github.com/cgartlab/edic-design-system/commit/a0180a8ded8eaeb7edc88bb4e18320ef73c346ba))
* prevent Argus self-triggering, add concurrency, upgrade actions ([6b42cc3](https://github.com/cgartlab/edic-design-system/commit/6b42cc3759e56deb1beaa136b80416fdd890bf7e))
* **release:** add include-component-in-tag: false to prevent duplicate tag prefix ([29b36c7](https://github.com/cgartlab/edic-design-system/commit/29b36c78aba9256558bcc578426984587476b76b))
* remove dark overlay when mobile menu opens ([ffa2597](https://github.com/cgartlab/edic-design-system/commit/ffa2597e39b28fb8a196117a85b28fb83206f60b))
* replace href=# with javascript:void(0) in blog.html nav links (closes [#50](https://github.com/cgartlab/edic-design-system/issues/50)) ([46bf6a1](https://github.com/cgartlab/edic-design-system/commit/46bf6a171195cfa2707edc0aa452922f23db18ea))
* resolve 19 heading hierarchy jumps across 7 HTML files ([#113](https://github.com/cgartlab/edic-design-system/issues/113)) ([1396473](https://github.com/cgartlab/edic-design-system/commit/139647388185e780c7cca91717e638e1c1fcc0bb))
* resolve 3 P0 mobile issues ([#107](https://github.com/cgartlab/edic-design-system/issues/107)) ([76913ac](https://github.com/cgartlab/edic-design-system/commit/76913ac4c537a7b10266313ab7be5c6e81e0ecab)), closes [#93](https://github.com/cgartlab/edic-design-system/issues/93) [#94](https://github.com/cgartlab/edic-design-system/issues/94) [#95](https://github.com/cgartlab/edic-design-system/issues/95)
* restore CNAME for GitHub Pages custom domain (designsystem.cgartlab.com) ([f118c5c](https://github.com/cgartlab/edic-design-system/commit/f118c5cd02d86af2a41725bd23473250223a1576))
* rewrite mobile nav from working version f52c293 ([78999e4](https://github.com/cgartlab/edic-design-system/commit/78999e414160d7d508f19251bcde74f7d180aa2a))
* **styles:** add --d animation-delay CSS variable default (0ms) in :root ([#86](https://github.com/cgartlab/edic-design-system/issues/86)) ([0326453](https://github.com/cgartlab/edic-design-system/commit/032645387a1010ae149c64f63a60c8e9b4a2e503))
* **styles:** replace ch-unit max-width on hero-lead with min(660px, 100%) for CJK correctness ([#81](https://github.com/cgartlab/edic-design-system/issues/81)) ([60b9db2](https://github.com/cgartlab/edic-design-system/commit/60b9db28dfa4176009224a071c4057ab5ac274ff))
* **tokens:** sync scripts.js letter-spacing and font-stack values with styles.css (closes [#39](https://github.com/cgartlab/edic-design-system/issues/39), [#40](https://github.com/cgartlab/edic-design-system/issues/40)) ([4e23f27](https://github.com/cgartlab/edic-design-system/commit/4e23f2773aa15109ab2bd73cdd1fadb9050c6e88))
* **tokens:** sync version to 1.3.1 (closes [#46](https://github.com/cgartlab/edic-design-system/issues/46)) ([6d74201](https://github.com/cgartlab/edic-design-system/commit/6d74201da6ec2c379e52baadec206b5656830986))
* **tools:** exclude string literal braces from function depth count in validate_naming.py ([#87](https://github.com/cgartlab/edic-design-system/issues/87)) ([0fb6c59](https://github.com/cgartlab/edic-design-system/commit/0fb6c592e709606ea2c4e50583f45d8e8787b918))
* **tools:** implement accurate OKLch-&gt;sRGB conversion in generate_pdfs.py ([#84](https://github.com/cgartlab/edic-design-system/issues/84)) ([e0120cb](https://github.com/cgartlab/edic-design-system/commit/e0120cb9f7f2227edf8cf2292139157c461de86a))
* **tools:** validate_a11y.py — fix has_h1 dead code and _has_accessible_name text check (closes [#32](https://github.com/cgartlab/edic-design-system/issues/32), [#33](https://github.com/cgartlab/edic-design-system/issues/33)) ([81beae7](https://github.com/cgartlab/edic-design-system/commit/81beae7e98e3ebf3d69918936c28d277da9f0282))
* **tools:** validate_html checks description/title; validate_links checks script src (closes [#48](https://github.com/cgartlab/edic-design-system/issues/48), [#49](https://github.com/cgartlab/edic-design-system/issues/49)) ([f87e022](https://github.com/cgartlab/edic-design-system/commit/f87e022aa0aa42ec3524a0b744ba72cc2074aa28))
* **tools:** validate_tokens.py uses brace-depth scanner for :root blocks to handle nested [@media](https://github.com/media) (closes [#37](https://github.com/cgartlab/edic-design-system/issues/37)) ([6203c46](https://github.com/cgartlab/edic-design-system/commit/6203c46b5b3037a3a9704478fe6e171c94c3d938))
* unify handbook TOC with docs/terms sidebar style and fix mobile nav rollback ([8e65e0e](https://github.com/cgartlab/edic-design-system/commit/8e65e0e903da7e3b236faa2147103480ebfb3047))
* unify section spacing to 64px across all pages ([#152](https://github.com/cgartlab/edic-design-system/issues/152)) ([f6dc2e7](https://github.com/cgartlab/edic-design-system/commit/f6dc2e781e6883d807337e42456c7555850ac275))
* update Reference links to valid edic.cgartlab.com URLs (v1.5.5) ([#186](https://github.com/cgartlab/edic-design-system/issues/186)) ([97ba160](https://github.com/cgartlab/edic-design-system/commit/97ba160c7bbc6e13c71d04bf5e36bce86ec6d6f8))
* validator false positives + responsive mobile overrides + mobile TOC ([#116](https://github.com/cgartlab/edic-design-system/issues/116)) ([29b7c6b](https://github.com/cgartlab/edic-design-system/commit/29b7c6bc52036be25914da3934d375128ffe324d))
* **version-sync:** address Codex review P1/P2 feedback on PR [#26](https://github.com/cgartlab/edic-design-system/issues/26) ([e94eacf](https://github.com/cgartlab/edic-design-system/commit/e94eacfc8ad826b4b75010b5538ca562cbc3041e))
* 修复 system 模式跟随系统变化 + 为 company.html 添加主题按钮 ([cb6ae92](https://github.com/cgartlab/edic-design-system/commit/cb6ae92538b8ed4ffb5c61a3518978b6d0327f15))
* 动画结束后移除 stroke 描边，保持与 logo-mark 一致 ([a0ebfcc](https://github.com/cgartlab/edic-design-system/commit/a0ebfcc5ea4bddab7c6ed378e3541f4184e4777f))


### 重构

* **footer:** unify footer layout, update copyright, and add site map ([066a805](https://github.com/cgartlab/edic-design-system/commit/066a8058209a9ea072e390800dc5fe7a36d77dad))
* **footer:** unify footer layout, update copyright, and add site map ([85331ac](https://github.com/cgartlab/edic-design-system/commit/85331ac00ed9792bafec266b211bcd69e26431e1))
* **js:** replace all var with const/let in scripts.js per project coding rules (closes [#56](https://github.com/cgartlab/edic-design-system/issues/56)) ([0e01c92](https://github.com/cgartlab/edic-design-system/commit/0e01c9290ef9e0598979f61a8ca55e2cb8856631))
* mobile nav aligned with design system tokens & patterns ([6cb45d1](https://github.com/cgartlab/edic-design-system/commit/6cb45d1c36dc5a092c6c8daaf5e955b457c84d6a))
* replace 22 inline onclick handlers with event delegation ([#112](https://github.com/cgartlab/edic-design-system/issues/112)) ([fa2c431](https://github.com/cgartlab/edic-design-system/commit/fa2c431d78f7e1fbb30a9c9710f4c6953864dabf))
* **resume:** 重写简历模板与个人信息 ([78b7cd0](https://github.com/cgartlab/edic-design-system/commit/78b7cd0a83cce600b731ad342993dc9c8f3515ae))
* 重构暗色模式切换功能，统一主题按钮样式和逻辑 ([b284b25](https://github.com/cgartlab/edic-design-system/commit/b284b25a9e7e9cd5ae5ccc14830d18a1fe579c3e))


### 文档

* add CLAUDE.md for Claude Code guidance ([3e6b0e9](https://github.com/cgartlab/edic-design-system/commit/3e6b0e9970fefd2e8ecaab6429621c229819eee9))
* add CLAUDE.md for Claude Code guidance ([#130](https://github.com/cgartlab/edic-design-system/issues/130)) ([f33efc9](https://github.com/cgartlab/edic-design-system/commit/f33efc917b1f2a9c1142d33ed24ce93248628537))
* **AGENTS.md:** update doc generation time and add notes ([b180821](https://github.com/cgartlab/edic-design-system/commit/b1808218ed939f0edccdea87dfdefc572776074e))
* **changelog:** add code style specification entry under [Unreleased] ([96122eb](https://github.com/cgartlab/edic-design-system/commit/96122eb28be6b06a81a16fa74f47760d2432a1be))
* **changelog:** add code style specification entry under [Unreleased] ([e0cd97f](https://github.com/cgartlab/edic-design-system/commit/e0cd97f2cdd51e51df9617dacd66a1e919dbb5e8))
* comprehensive v1.5.0 sync — domain, tokens, prompts, SKILL, README rewrite ([a2afe90](https://github.com/cgartlab/edic-design-system/commit/a2afe90dd4f872ec5a312190fb01fce3b34836cf))
* comprehensive v1.5.0 sync — domain, tokens, prompts, SKILL, README rewrite ([#140](https://github.com/cgartlab/edic-design-system/issues/140)) ([e9f0bd2](https://github.com/cgartlab/edic-design-system/commit/e9f0bd240d716e5ddb16e3be58160af43fd449ff))
* document icons.svg generator in AGENTS and CHANGELOG ([5187a1c](https://github.com/cgartlab/edic-design-system/commit/5187a1c64e912371e9024c8d67589abf875bb01f))
* fix handbook timeline fiction and sync tokens/SKILL/validator ([717900c](https://github.com/cgartlab/edic-design-system/commit/717900c752b2ac2c779f255030b49ad271bbe504))
* fix prompts.html/system-prompt.md accuracy and restore CNAME ([18a71bf](https://github.com/cgartlab/edic-design-system/commit/18a71bf778312a6cb102f5849d2ba4991871311d))
* **readme:** rewrite — no emoji, concise, accurate v1.5.0 ([b0056c8](https://github.com/cgartlab/edic-design-system/commit/b0056c85ed5217f1918ca3b45cfc8375dc5c9f6c))
* **sync:** align all documentation with v1.5.0 codebase ([cd4ebbe](https://github.com/cgartlab/edic-design-system/commit/cd4ebbe3d09a1d329aae944733171d5c7078dda9))
* update AGENTS.md date to 2026-06-04 ([b27086b](https://github.com/cgartlab/edic-design-system/commit/b27086b424135a79705a47fd93158ae830bc6da0))
* update AGENTS.md generation date to 2026-05-29 ([a9c596a](https://github.com/cgartlab/edic-design-system/commit/a9c596afda65069738cb89a1b1f49f96fe79b15a))
* **workflow:** document stamp_version.py tool and updated release flow ([e81c4a9](https://github.com/cgartlab/edic-design-system/commit/e81c4a9114ad7b64adfddb1dbb9073c9a9446f2d))
* 更新 README.md，反映最近的代码变更 ([78a5ac2](https://github.com/cgartlab/edic-design-system/commit/78a5ac26013f2cb85e387a23a286e4c48fe4d67d))
* 添加极度详细的网站开发指南文档 ([a209def](https://github.com/cgartlab/edic-design-system/commit/a209defcb957f249f2f41aa4889d841b038f15b1))
* 添加极度详细的网站开发指南文档 ([5f86b51](https://github.com/cgartlab/edic-design-system/commit/5f86b513be5dc7e979ff2249a0300eec75ef4026))
* 统一品牌描述，强调面向非设计师用户 ([#155](https://github.com/cgartlab/edic-design-system/issues/155)) ([e50984d](https://github.com/cgartlab/edic-design-system/commit/e50984dede974294af6ba82d2059ffd43d236c78))


### 样式

* **hero:** 重新设计首页 Hero 区域版式 ([#25](https://github.com/cgartlab/edic-design-system/issues/25)) ([21c63e2](https://github.com/cgartlab/edic-design-system/commit/21c63e28a88d3cbc4f7c28f1560e5a52e4bc9547))
* 完善中文排版规范与细节优化 ([ba4674f](https://github.com/cgartlab/edic-design-system/commit/ba4674fe5b30c43debe9836b1ac537aef7c6e4c3))

## [1.6.2] — 2026-06-22

### 修复（首页设计系统规范合规性）

- **[P0] `ds-stat-num`/`ds-stat-label` 双重 CSS 定义**：`styles.css` 中存在两套同名规则，第二套（旧 `.ds-stat-grid` 体系）覆盖第一套（`.ds-stats-grid` 体系），导致首页统计数字 `display:block` 丢失、字号异常、标签样式错误。移除第二套中的重复选择器，旧体系仅保留布局类。
- **[P0] `ds-eyebrow` `letter-spacing` 被 `!important` 强制覆盖**：全局 CJK 基线层将 `.ds-eyebrow` 的字间距 `!important` 压至 `tracking-wider`（0.08em），而组件定义规定 `tracking-widest`（0.12em）。从 `!important` 规则中移除 `.ds-eyebrow`，令组件定义正常生效。
- **[P1] Hero 区域语义标签**：`<header class="ds-hero-section">` 改为 `<section aria-label="Hero">`，避免页面出现两个 `banner` landmark 混淆屏幕阅读器。
- **[P1] `ds-hero-section` 补充分隔线**：加入 `border-bottom: 1px solid var(--ds-color-border)`，融入全站 section 分隔线节奏。
- **[P1] `.ds-step-body` 标题层级统一**：三步骤中第 1 步误用 `<h3>`，其余用 `<h4>`，且 CSS 只定义 `h4` 样式；统一改为 `<h4>`。
- **[P1] Footer CC BY 4.0 链接移除 inline style**：`style="color:var(--ds-accent);text-decoration:none"` 改为 class `ds-text-accent ds-footer-cc`（新增 `.ds-footer-cc` 工具类）。
- **[P2] Hero 主操作层级**：Hero 区块 4 个 CTA 按钮全用 `ds-btn--secondary`；首个按钮「浏览视觉手册」改为 `ds-btn--primary`，明确核心转化路径。
- **[P2] 卡片内标题语义**：Features（8 张）、System TOC（8 张）、Examples（4 张）共 20 处非文档结构性卡片标题从 `<h3>` 改为 `<p class="ds-card-heading">`，新增 `.ds-card-heading` 工具类，视觉不变但不再污染文档大纲。CSS 中 `ds-feature-card` 和 `ds-toc-item` 的选择器同时兼容 `h3` 与 `.ds-card-heading`。

---

## [1.6.1](https://github.com/cgartlab/edic-design-system/compare/edic-design-system-v1.6.0...edic-design-system-v1.6.1) (2026-06-22)


### 修复

* **pages:** migrate to workflow-based Pages + restore v1.6.0 stamp ([dbd26c2](https://github.com/cgartlab/edic-design-system/commit/dbd26c28a80fdcb2dbfbc574e5542a8f5b3df693))

## [1.6.0](https://github.com/cgartlab/edic-design-system/compare/edic-design-system-v1.5.5...edic-design-system-v1.6.0) (2026-06-22)


### 新增

* add Layer 2 cross-file validators (cssref, darkmode, verext, hardcode) ([#136](https://github.com/cgartlab/edic-design-system/issues/136)) ([cde1c58](https://github.com/cgartlab/edic-design-system/commit/cde1c5867ddb797c41d2b5e4ce4e2ab3a9891de5))
* **automation:** add release-please automated release pipeline ([91098a0](https://github.com/cgartlab/edic-design-system/commit/91098a062411a033d8541ba14745517bbf846ba5))
* brand rename — CGArtLab Design System → EDIC Design System ([#109](https://github.com/cgartlab/edic-design-system/issues/109)) ([#122](https://github.com/cgartlab/edic-design-system/issues/122)) ([241eab0](https://github.com/cgartlab/edic-design-system/commit/241eab0181338308d2a186f90d1cd1074bb4cd93))
* CC BY 4.0 使用条款全面修订 - 法律合规性审查 ([c9b2447](https://github.com/cgartlab/edic-design-system/commit/c9b2447e249849acdc0ae12d223df666366a32bd))
* CGArtLab Design System v1.0 ([5483b25](https://github.com/cgartlab/edic-design-system/commit/5483b2513bb63184d6c16bc61e6751e163f0ffb2))
* **changelog:** add update log page and fix footer links ([8f23b22](https://github.com/cgartlab/edic-design-system/commit/8f23b224084fe57e61c1ac8d149784623cccb63d))
* **changelog:** add update log page and fix footer links ([#144](https://github.com/cgartlab/edic-design-system/issues/144)) ([c268f70](https://github.com/cgartlab/edic-design-system/commit/c268f709b0298be5ef4dbaba5f7897b206a32acf))
* **code:** add Prism.js syntax highlighting + editorial olive-green theme ([add21ed](https://github.com/cgartlab/edic-design-system/commit/add21ed7b46203a72bb67d79885cc466caa6d7ba))
* **code:** add Prism.js syntax highlighting with editorial olive-green theme ([#92](https://github.com/cgartlab/edic-design-system/issues/92)) ([93b00db](https://github.com/cgartlab/edic-design-system/commit/93b00db511558edf6aeaa22efcedc39ede64182f))
* **css:** dark-mode gravitas & glow (v1.5.0) — warm olive undertone layer ([#132](https://github.com/cgartlab/edic-design-system/issues/132)) ([0e96ec8](https://github.com/cgartlab/edic-design-system/commit/0e96ec8d15e1f70b97b6197e138cd2753dad23b1))
* **governance:** add engineering governance layer (v1.3.1) ([#24](https://github.com/cgartlab/edic-design-system/issues/24)) ([ebafaf4](https://github.com/cgartlab/edic-design-system/commit/ebafaf48eb3ffd1cc9242de9a5ae4efb8d1933df))
* **hero:** sliding word cycle, infinite scroll carousel, unified buttons ([#185](https://github.com/cgartlab/edic-design-system/issues/185)) ([#187](https://github.com/cgartlab/edic-design-system/issues/187)) ([4a9bdc4](https://github.com/cgartlab/edic-design-system/commit/4a9bdc420cf0e513432343cfa3c2786adb9f0ad0))
* **icons:** add icons.svg sprite generator with full dev entrypoint integration ([66274c3](https://github.com/cgartlab/edic-design-system/commit/66274c3bb09a493ef6fb73fcdbb1de75206f5ee1))
* **icons:** generate icons.svg sprite file (100 symbols, XML-valid) ([0771b06](https://github.com/cgartlab/edic-design-system/commit/0771b06a9ee75c5cd82c1920406ce4fb7749d8bd))
* implement all 5 open issues ([#147](https://github.com/cgartlab/edic-design-system/issues/147) [#148](https://github.com/cgartlab/edic-design-system/issues/148) [#149](https://github.com/cgartlab/edic-design-system/issues/149) [#150](https://github.com/cgartlab/edic-design-system/issues/150) [#151](https://github.com/cgartlab/edic-design-system/issues/151)) ([#165](https://github.com/cgartlab/edic-design-system/issues/165)) ([8c77952](https://github.com/cgartlab/edic-design-system/commit/8c779522bc2c779102f545faaa4a6d5db565ad1f))
* **mobile-nav:** fullscreen overlay menu — rewrite from scratch ([1cac693](https://github.com/cgartlab/edic-design-system/commit/1cac693bed0ca082c747961443bbc17618c72df8))
* **mobile-nav:** rewrite from scratch — fullscreen overlay menu ([dba64dc](https://github.com/cgartlab/edic-design-system/commit/dba64dced65ec6b464f4aa52a24769f8e9dcfd5d))
* **nav:** frosted-acrylic glass navbar + mobile drawer (dark-mode aware) ([ef817dd](https://github.com/cgartlab/edic-design-system/commit/ef817dde975d1d1ebe981ca3c69fc45124009a09))
* **nav:** frosted-acrylic glass on navbar + mobile drawer (dark-mode aware) ([9101866](https://github.com/cgartlab/edic-design-system/commit/9101866f41c88ea1b2c91553dfde20efb356fa8c))
* **opencode:** add Argus auto PR review workflow ([72be2f4](https://github.com/cgartlab/edic-design-system/commit/72be2f4d5754cd191992e09ba687b72089a50315))
* **opencode:** add Argus GitHub App workflow ([989d14a](https://github.com/cgartlab/edic-design-system/commit/989d14ad0cf358af00c03b8d2d2317bd35c49763))
* **opencode:** add Argus GitHub App workflow ([8f4bae6](https://github.com/cgartlab/edic-design-system/commit/8f4bae602ceab0d3bf1436ac3774fc658674c5e5))
* **opencode:** add auto PR review trigger + app token fix ([4beaeae](https://github.com/cgartlab/edic-design-system/commit/4beaeaef2983db093ac799a1e04784c8ac2f66e1))
* overhaul mobile navigation menu ([48a34bb](https://github.com/cgartlab/edic-design-system/commit/48a34bbbbe68c6feeef104896bbb2f5d9335b13d))
* overhaul mobile navigation menu ([b6941ef](https://github.com/cgartlab/edic-design-system/commit/b6941efb7b287236529f6f3f9d6051c225f12344))
* **toc:** unify handbook/docs/terms TOC into .ds-pagenav component ([#128](https://github.com/cgartlab/edic-design-system/issues/128)) ([96dd95b](https://github.com/cgartlab/edic-design-system/commit/96dd95bb2ea7887a9c8fe9a84e8f8df463a25f9a))
* **tokens:** expand tokens.json from ~30% to ~80% coverage — dark mode colors, breakpoints, z-index, duration, easing, shadow, tracking, leading, weight scales (closes [#38](https://github.com/cgartlab/edic-design-system/issues/38), [#45](https://github.com/cgartlab/edic-design-system/issues/45)) ([4ce6f0d](https://github.com/cgartlab/edic-design-system/commit/4ce6f0dadec75695f49c0b8efbe6974d8d0abff8))
* **tools:** add icons.svg generator from scripts.js ICONS array ([55e8e07](https://github.com/cgartlab/edic-design-system/commit/55e8e07106f5cc3169b534d4453be520b832b4ee))
* **tools:** add stamp_version.py and dynamic VERSION reading in PDF ([cf872c6](https://github.com/cgartlab/edic-design-system/commit/cf872c6061b9cab0959d69fc3f848516c7cfaf81))
* unify version stamping across all project files ([#180](https://github.com/cgartlab/edic-design-system/issues/180)) ([7395b6a](https://github.com/cgartlab/edic-design-system/commit/7395b6a817e6b55f1ddf69872ab76a66ba30281a))
* v1.1 — multi-page showcase website, brand logo, motion system, AI prompts & Skill ([c9b6dbc](https://github.com/cgartlab/edic-design-system/commit/c9b6dbc24dd2eb528b696651679b893b6beb4fae))
* v1.1 — 展示网站 + 品牌 Logo + 动效 + AI 提示词/Skill ([11cc375](https://github.com/cgartlab/edic-design-system/commit/11cc375ee1aa0b14bbe1d962e203d4e7af4916e4))
* **versions:** apply stamp_version to all HTML and MD resources ([57007da](https://github.com/cgartlab/edic-design-system/commit/57007da1ad328d00e7594a241f2bca6806127e3d))
* **versions:** introduce stamp_version.py for centralized version sync ([0cf1e0c](https://github.com/cgartlab/edic-design-system/commit/0cf1e0c4bfe1ec00c46e4f33c33617df6083d2ac))
* 合并视觉手册内容到文档页面 ([#164](https://github.com/cgartlab/edic-design-system/issues/164)) ([375db30](https://github.com/cgartlab/edic-design-system/commit/375db300e6ad57a9ce2abbf55e770b7a9fc84ef5))
* 完成设计系统v1.0正式版本发布 ([321aae6](https://github.com/cgartlab/edic-design-system/commit/321aae6c393ca6e95b0b118c74d71246aac380b6))
* 新增公司官网第二版本页面及关联配置文件 ([f43a18d](https://github.com/cgartlab/edic-design-system/commit/f43a18d1e7567b480df4c981340e46313544701e))
* 重构主题切换按钮，整合到导航栏并优化移动端体验 ([5e33f28](https://github.com/cgartlab/edic-design-system/commit/5e33f289602ec7d67952df5cbf22d8141341f557))


### 修复

* **#124:** 下载页面核心资源板块改为两排三列布局 ([#133](https://github.com/cgartlab/edic-design-system/issues/133)) ([618aa46](https://github.com/cgartlab/edic-design-system/commit/618aa46dcbc6ada6d27d658c6e9e4fc4f44b029a))
* **#167 #175:** replace bare oklch in company.html + styles.css with tokens ([#177](https://github.com/cgartlab/edic-design-system/issues/177)) ([bf1e0af](https://github.com/cgartlab/edic-design-system/commit/bf1e0af92f2fec4e958f510813ea2de60079d084))
* **#168 #169 #170:** add changelog.html to stamp targets, scripts.js version placeholder, footer-end div ([#178](https://github.com/cgartlab/edic-design-system/issues/178)) ([4791ea4](https://github.com/cgartlab/edic-design-system/commit/4791ea47b4c4028bc768bd4877a12d219d3ebd14))
* **#174:** Fix validate_hardcode.py bugs and replace bare oklch in styles.css ([#176](https://github.com/cgartlab/edic-design-system/issues/176)) ([fb1c693](https://github.com/cgartlab/edic-design-system/commit/fb1c693cef49510fe0d2e481dc7d42198cd6da4e))
* **#hero:** remove hero background glow, enable LAN serve, add preview workflow docs ([#182](https://github.com/cgartlab/edic-design-system/issues/182)) ([93cb008](https://github.com/cgartlab/edic-design-system/commit/93cb008f170bb507ca133c1f1901e2b1e88ac290))
* **a11y:** add :focus-visible to .ds-toc-item for keyboard navigation (closes [#75](https://github.com/cgartlab/edic-design-system/issues/75)) ([c65faa6](https://github.com/cgartlab/edic-design-system/commit/c65faa6570e99b1de4384ed0ec5e624fdf667427))
* **a11y:** add forced-colors rule for .ds-gradient-text to fix WHCM visibility (closes [#70](https://github.com/cgartlab/edic-design-system/issues/70)) ([8349072](https://github.com/cgartlab/edic-design-system/commit/8349072ae2276eba9cfa068199bf84cb5e77c6d4))
* **a11y:** add main landmark + fix skip-link target across 5 pages (closes [#73](https://github.com/cgartlab/edic-design-system/issues/73)) ([a8e841b](https://github.com/cgartlab/edic-design-system/commit/a8e841b3f3a00b4ff3731e10fedc32c903c3659f))
* **a11y:** add prefers-color-scheme: dark CSS fallback for dark-system users before JS loads (closes [#54](https://github.com/cgartlab/edic-design-system/issues/54)) ([dbe4996](https://github.com/cgartlab/edic-design-system/commit/dbe4996c977f8e9c5cf8db3d3efe2203ef872b6c))
* **a11y:** restructure resume.html cards to fix nested anchor/block-level invalid HTML (closes [#59](https://github.com/cgartlab/edic-design-system/issues/59)) ([2b53381](https://github.com/cgartlab/edic-design-system/commit/2b53381e4750a05792abe6c22273ac472e755679))
* add meta descriptions to 4 HTML files ([#114](https://github.com/cgartlab/edic-design-system/issues/114)) ([766a83c](https://github.com/cgartlab/edic-design-system/commit/766a83c59e62b02b5d658fd72e45adf454fd04eb))
* bump asset cache-busting version 1.1.5 -&gt; 1.2.0 ([3ca9c65](https://github.com/cgartlab/edic-design-system/commit/3ca9c65182f0e05ebb733f0ff4f06cefc0ec187c))
* bump asset version v1.1.5 -&gt; v1.2.0 (cache-bust the mobile nav) ([b869844](https://github.com/cgartlab/edic-design-system/commit/b869844a158829878e042eb8e1d83f6809f14bab))
* **ci:** align release.yml checkout action to [@v5](https://github.com/v5) matching ci.yml (closes [#43](https://github.com/cgartlab/edic-design-system/issues/43)) ([665ef2d](https://github.com/cgartlab/edic-design-system/commit/665ef2d88989bb253b9f8285e2c5110de8bd7b52))
* **CI:** exclude continue-on-error validators from blocking check + improve pre-commit hook ([09463a7](https://github.com/cgartlab/edic-design-system/commit/09463a727d124a97d26e46f300098890ecfed30a))
* **ci:** lock playwright version in CI workflow for reproducible builds ([#88](https://github.com/cgartlab/edic-design-system/issues/88)) ([583315a](https://github.com/cgartlab/edic-design-system/commit/583315a017fa991b19419ae6a3181f278fc25c41))
* **ci:** root cause - replace bash ternary with if/elif exit code handling ([#127](https://github.com/cgartlab/edic-design-system/issues/127)) ([0629392](https://github.com/cgartlab/edic-design-system/commit/0629392a470a7b5ea0b52cdcc6af02ddf730fbf5))
* **code:** Prism code-block theming + OKLch migration of pre-existing anti-patterns ([#110](https://github.com/cgartlab/edic-design-system/issues/110)) ([f088a5b](https://github.com/cgartlab/edic-design-system/commit/f088a5bca69bea1f52b05bc6b0120534077197ce))
* correct CC BY 4.0 adapter-license freedom per Codex review ([01b94b2](https://github.com/cgartlab/edic-design-system/commit/01b94b2b23f228e9b5acae560cbc47d91ccf379c))
* **critical-c4:** add auto-dismiss functionality to Toast component ([#161](https://github.com/cgartlab/edic-design-system/issues/161)) ([28eb3e6](https://github.com/cgartlab/edic-design-system/commit/28eb3e6f6403a9032aadfa69b08e8e0002170175))
* **css:** .ds-table-wrap 健壮性 — a11y 焦点环 + overflow-y 显式声明 ([#121](https://github.com/cgartlab/edic-design-system/issues/121)) ([56a3eab](https://github.com/cgartlab/edic-design-system/commit/56a3eabbe7b96e8baddf92a63af9a46815ba1715))
* **css:** add min-width:0/max-width:100% to .ds-compat-item for narrow-viewport overflow fix (closes [#71](https://github.com/cgartlab/edic-design-system/issues/71)) ([f263cbd](https://github.com/cgartlab/edic-design-system/commit/f263cbdb192bcf4668b44d78b5dccc9ed0e96f3a))
* **css:** make .ds-footer-brand span full width at tablet breakpoint (closes [#77](https://github.com/cgartlab/edic-design-system/issues/77)) ([728f9ba](https://github.com/cgartlab/edic-design-system/commit/728f9baa6516030f818266b008ce474df4b9bdf6))
* **css:** remove ::before/::after pseudo-elements from .ds-hero-meta for IE compatibility (closes [#69](https://github.com/cgartlab/edic-design-system/issues/69)) ([6f75e29](https://github.com/cgartlab/edic-design-system/commit/6f75e29aecca24518df655010e0b43a842520ce9))
* **css:** remove body duplicate transition, page-btn white token, report.html meta (closes [#53](https://github.com/cgartlab/edic-design-system/issues/53), [#55](https://github.com/cgartlab/edic-design-system/issues/55), [#57](https://github.com/cgartlab/edic-design-system/issues/57)) ([7de4249](https://github.com/cgartlab/edic-design-system/commit/7de4249d1c297dd64f093def263f6d9f4f6c36a3))
* **css:** remove duplicate overflow-wrap from .ds-text-cjk to fix self-override (closes [#36](https://github.com/cgartlab/edic-design-system/issues/36)) ([e0a1a40](https://github.com/cgartlab/edic-design-system/commit/e0a1a407c84871d3fb383e48225bed01944f4758))
* **css:** touch-safe hover for .ds-feature-card + responsive .ds-stat-num clamp (closes [#72](https://github.com/cgartlab/edic-design-system/issues/72), [#74](https://github.com/cgartlab/edic-design-system/issues/74)) ([f388d2e](https://github.com/cgartlab/edic-design-system/commit/f388d2eedf43c8714d227be680a9538f62b4858f))
* **css:** unify handbook pagenav spacing, fix responsive overflow and stale versions ([#134](https://github.com/cgartlab/edic-design-system/issues/134)) ([ac7b8b9](https://github.com/cgartlab/edic-design-system/commit/ac7b8b9c9058297567e702fab516ca9f70f0ec3d))
* **css:** 桌面端浮动 TOC 重设计 + 移动端 TOC 不再遮挡主题切换按钮 ([#123](https://github.com/cgartlab/edic-design-system/issues/123)) ([739b91b](https://github.com/cgartlab/edic-design-system/commit/739b91bd3a6f9f1da893988170688d64b71ff893))
* **design-system:** replace bare oklch in report.html and resume.html with --ds-* tokens ([#173](https://github.com/cgartlab/edic-design-system/issues/173)) ([1e3b066](https://github.com/cgartlab/edic-design-system/commit/1e3b0667ce3870e37756bcfa804162e530f90bd2)), closes [#166](https://github.com/cgartlab/edic-design-system/issues/166)
* **design-system:** resolve all verified style inconsistencies and hardcoded values ([#172](https://github.com/cgartlab/edic-design-system/issues/172)) ([6bfb5fc](https://github.com/cgartlab/edic-design-system/commit/6bfb5fc5515500bb296bf1194d8f154f5883d93b))
* div balance in handbook + add skip-to-content, robots.txt, sitemap, og:image ([d7f116a](https://github.com/cgartlab/edic-design-system/commit/d7f116a2c136463e0ca178c9aed348f0124cfe5b))
* **docs:** resolve 16 cross-document contradictions for v1.4.3 ([#131](https://github.com/cgartlab/edic-design-system/issues/131)) ([d6352dc](https://github.com/cgartlab/edic-design-system/commit/d6352dc6388e4e5eeda365d8f41bd9ba8f5d368a))
* **docs:** 冒烟测试 fix 触发 release-please ([8432100](https://github.com/cgartlab/edic-design-system/commit/84321001648d78b342332574457205269a74f1c4))
* **footer:** replace h3 with semantic p.ds-footer-col-heading ([6ed7378](https://github.com/cgartlab/edic-design-system/commit/6ed7378bf1e72905b231191e05277382c16e9887))
* **footer:** update copyright to CGArtLab, add blog link, move sitemap under 关于 ([fc80606](https://github.com/cgartlab/edic-design-system/commit/fc806064000579a94764469941c68677ce56b7d8))
* **footer:** update copyright to CGArtLab, add blog link, move sitemap under 关于 ([665ac08](https://github.com/cgartlab/edic-design-system/commit/665ac08761e9dd973e738363b167f5f21f9814bd))
* **footer:** 替换 h3 为语义化 p.ds-footer-col-heading ([#145](https://github.com/cgartlab/edic-design-system/issues/145)) ([477e441](https://github.com/cgartlab/edic-design-system/commit/477e44115e2b41d1c6172e4fcea21d43b1456d71))
* **handbook:** close 640-1023px TOC dead zone, fix mobile active state, unify base ([#125](https://github.com/cgartlab/edic-design-system/issues/125)) ([891d715](https://github.com/cgartlab/edic-design-system/commit/891d7158edde6a1cc65022048ee4ad48e0ad7822))
* **handbook:** extract timeline/contact into standalone sections for TOC navigation ([e7c969a](https://github.com/cgartlab/edic-design-system/commit/e7c969a17b42f486800572922af909e2ab8ef8d3))
* **handbook:** extract timeline/contact into standalone sections for TOC navigation ([#129](https://github.com/cgartlab/edic-design-system/issues/129)) ([58be16f](https://github.com/cgartlab/edic-design-system/commit/58be16ff9ac45151e705ecdc10cc6e84672edf3d))
* **handbook:** mobile overflow protection for #typography inline-style tables ([#117](https://github.com/cgartlab/edic-design-system/issues/117)) ([6bc734c](https://github.com/cgartlab/edic-design-system/commit/6bc734c0078b229769bab474be7cbeab2778a19c))
* **handbook:** mobile spacing — cover eyebrow gap 24→16px, pagenav top margin 16px ([#137](https://github.com/cgartlab/edic-design-system/issues/137)) ([0950f1d](https://github.com/cgartlab/edic-design-system/commit/0950f1d913b615d3dcd90fbf4e6f3c8ca23e7a9a))
* **handbook:** remove C,G subtitle and add TOC top margin on mobile ([8294b71](https://github.com/cgartlab/edic-design-system/commit/8294b719741e587fb943072364b67bf4e55cd13d))
* **handbook:** remove hidden pagenav from mobile layout — eliminates blank gap ([7272c1e](https://github.com/cgartlab/edic-design-system/commit/7272c1eb698c50c2507f04a59cdff5d90d61cb16))
* **html:** add scripts.js to blog.html to enable theme/dark mode and all progressive enhancements (closes [#41](https://github.com/cgartlab/edic-design-system/issues/41)) ([8a1cab2](https://github.com/cgartlab/edic-design-system/commit/8a1cab200b34ba1cfda82f016cc0672a75a59410))
* **html:** rename duplicate theme-toggle-btn id to theme-toggle-btn-fixed on floating buttons (closes [#31](https://github.com/cgartlab/edic-design-system/issues/31)) ([5ecfcb8](https://github.com/cgartlab/edic-design-system/commit/5ecfcb82679ccf1046dfe659c4b1f1e0efb32c77))
* **icons:** add presentation attributes to SVG sprite symbols ([a7c8281](https://github.com/cgartlab/edic-design-system/commit/a7c8281ce1bdecd9e3bfd1e99e83f49d2a10eeee))
* increase mobile drawer glass opacity to 92-94% + cache-bust CSS/JS ([f407c1a](https://github.com/cgartlab/edic-design-system/commit/f407c1a45c0d21b506f063aed4af3c1325c86b78))
* **index:** differentiate CTA button hierarchy - primary/secondary/ghost ([#76](https://github.com/cgartlab/edic-design-system/issues/76)) ([f689417](https://github.com/cgartlab/edic-design-system/commit/f689417d7118cdae98d8151a95413eafc2a8e3b2))
* **index:** widen CTA container and remove measure constraint to prevent single-character orphan ([#91](https://github.com/cgartlab/edic-design-system/issues/91)) ([5bf1145](https://github.com/cgartlab/edic-design-system/commit/5bf11458938300adc24735d7ec47e3fda5069af0))
* **interactions:** 5 UI/a11y bugs + 87-test unit suite (v1.5.2) ([#159](https://github.com/cgartlab/edic-design-system/issues/159)) ([7fdbc1b](https://github.com/cgartlab/edic-design-system/commit/7fdbc1b4936cc5d33cf384173f0da817dce03fe2))
* **interactions:** a11y, copy feedback, memory leaks, and AGENTS.md rewrite ([8365173](https://github.com/cgartlab/edic-design-system/commit/8365173b93f462672d33595b375e2ec5b776f311))
* **interactions:** a11y, copy feedback, memory leaks, and AGENTS.md rewrite ([#141](https://github.com/cgartlab/edic-design-system/issues/141)) ([05d2e17](https://github.com/cgartlab/edic-design-system/commit/05d2e17281f1ac581cb8c0e4dbd8b63714e8bf86))
* **js:** cycleTheme reads data-theme-mode instead of parsing Chinese aria-label (closes [#34](https://github.com/cgartlab/edic-design-system/issues/34)) ([5d0e95f](https://github.com/cgartlab/edic-design-system/commit/5d0e95fdeec49b2b142d7db7d43004a433aca56c))
* **js:** TOC IntersectionObserver picks topmost section, adds 16ms debounce to prevent rapid flicker (closes [#58](https://github.com/cgartlab/edic-design-system/issues/58)) ([3ffb7ce](https://github.com/cgartlab/edic-design-system/commit/3ffb7cef378b05c062d3f4725c91ba9de3fee7ff))
* **makefile:** use cross-platform clean with -delete for .pyc files ([#80](https://github.com/cgartlab/edic-design-system/issues/80)) ([f4fe514](https://github.com/cgartlab/edic-design-system/commit/f4fe514e0bd4a779fae8e03798b4e35e2af7c0ee))
* **misc:** bump stale v1.0 version comments to v1.3.1 in styles.css and scripts.js (closes [#47](https://github.com/cgartlab/edic-design-system/issues/47)) ([8e5d782](https://github.com/cgartlab/edic-design-system/commit/8e5d7820ea55906b12ca250e07ad5bc11d51eee3))
* **mnav:** let mobile menu links navigate without aborting page load ([#154](https://github.com/cgartlab/edic-design-system/issues/154)) ([22cd13f](https://github.com/cgartlab/edic-design-system/commit/22cd13faed57987f237b1469c7f75f0340defaa9))
* mobile drawer — revert to solid background, remove backdrop-filter ([85745ac](https://github.com/cgartlab/edic-design-system/commit/85745acd0d322f1f71e0e1afafe45602b0b9cf7a))
* mobile nav drawer solid background + document mobile nav spec ([f52c293](https://github.com/cgartlab/edic-design-system/commit/f52c293089d58e1e4ab2d28a3c034303becaaafa))
* mobile nav drawer uses frosted glass (blur-xl + 78% opacity) ([7f2396b](https://github.com/cgartlab/edic-design-system/commit/7f2396b54bcfdb458370e2ff67d335eee38146cc))
* mobile navbar fully opaque + hamburger button with visible border ([7bd507c](https://github.com/cgartlab/edic-design-system/commit/7bd507c51ecf10b8ad3cc101ea0eddabc116eb29))
* **mobile-nav:** 3-bar hamburger, slide-in drawer with backdrop dimming ([075b503](https://github.com/cgartlab/edic-design-system/commit/075b503d20048341a7bf6408fdd589f4d684edd5))
* **mobile-nav:** cohesive solid menu + fix backdrop stacking-context bug ([83f7348](https://github.com/cgartlab/edic-design-system/commit/83f7348b1732af34872d4e5684f281f8b8c528d0))
* **mobile-nav:** cohesive solid menu, fix backdrop stacking over drawer ([9a791aa](https://github.com/cgartlab/edic-design-system/commit/9a791aa27b13c5e69f6db0db648dabecc08f61d4))
* **mobile-nav:** double rAF delay to override iOS Safari scroll restoration ([d97e2db](https://github.com/cgartlab/edic-design-system/commit/d97e2dbd316cf85965c1a885450fb386b5fcc179))
* **mobile-nav:** improve menu interaction and scroll behavior ([73b7fc7](https://github.com/cgartlab/edic-design-system/commit/73b7fc70bd033ad5f956e0c996c6f4f7d2ae3712))
* **mobile-nav:** include trigger button in focus trap ([a0180a8](https://github.com/cgartlab/edic-design-system/commit/a0180a8ded8eaeb7edc88bb4e18320ef73c346ba))
* **mobile-nav:** overhaul mobile drawer UI ([304d55f](https://github.com/cgartlab/edic-design-system/commit/304d55f8c765de6bc6e63526bcfb7e9f56888733))
* **mobile-nav:** overhaul mobile drawer UI — overlay blur, divider lines, hover slide, cleaner hamburger ([cf66e72](https://github.com/cgartlab/edic-design-system/commit/cf66e72d5de14b7a84393c8c632627a73ad68adc))
* **mobile-nav:** proper scroll locking and version bump to v1.5.1 ([14c8e59](https://github.com/cgartlab/edic-design-system/commit/14c8e5919d9762a749cc977e2b0c51b8e20d5a83))
* **mobile-nav:** reconcile PR[#9](https://github.com/cgartlab/edic-design-system/issues/9)/[#10](https://github.com/cgartlab/edic-design-system/issues/10) into one coherent best version ([c5a1f44](https://github.com/cgartlab/edic-design-system/commit/c5a1f44b3605b155a65f54cf19eaea9022077a7d))
* **mobile-nav:** reconcile PR[#9](https://github.com/cgartlab/edic-design-system/issues/9)/[#10](https://github.com/cgartlab/edic-design-system/issues/10) merge into one coherent best version ([316db72](https://github.com/cgartlab/edic-design-system/commit/316db7293c3eac5aa3da70d5bb5d4fffeca2c5f2))
* **mobile-nav:** remove dialog role from desktop nav, save/restore body overflow styles ([94b5fa3](https://github.com/cgartlab/edic-design-system/commit/94b5fa3ab3618e53147baeab942a5d5f17641e8c))
* **mobile-nav:** remove dialog role from desktop nav, save/restore body overflow styles, add aria-label ([b05cb27](https://github.com/cgartlab/edic-design-system/commit/b05cb27c72e9e111562d0e27e6ed320bcdda2fb0))
* **mobile-nav:** replace position:fixed with overflow:hidden approach ([d32bbcc](https://github.com/cgartlab/edic-design-system/commit/d32bbcce7dd189fc1a987d9883270190a5c86212))
* **mobile-nav:** resolve Codex review residual issues ([58e37c5](https://github.com/cgartlab/edic-design-system/commit/58e37c534b5431f830df43dfd72cb94cbe158138))
* **mobile-nav:** restore saved body overflow unconditionally, add align-items:stretch ([6b87efb](https://github.com/cgartlab/edic-design-system/commit/6b87efb518a6fa172134169e4a4fe800eaba984d))
* **mobile-nav:** set scroll position BEFORE removing position:fixed ([53ad3eb](https://github.com/cgartlab/edic-design-system/commit/53ad3eb1ee99fd1c027a012e31335365248fb55b))
* **mobile-scroll:** add explicit touch-action to TOC disclosure on mobile ([0a4468f](https://github.com/cgartlab/edic-design-system/commit/0a4468f1631e0d0b9a23ee2aa8dee97dc18cf62b))
* **mobile-scroll:** change ds-pagenav-disclosure overflow to visible on mobile ([ecb3e0f](https://github.com/cgartlab/edic-design-system/commit/ecb3e0f66a0717714883936de08bfbe7f28ff19c))
* **mobile-scroll:** use overscroll-behavior contain on disclosure and list ([31bb921](https://github.com/cgartlab/edic-design-system/commit/31bb92130af72a13a9f2392c33efdf3f829d115c))
* **mobile:** release scroll lock reliably; fix sitemap dead link ([236da9c](https://github.com/cgartlab/edic-design-system/commit/236da9cd304b9d29eb2e2a92104d911c11dc16e8))
* **mobile:** release scroll lock reliably; fix sitemap dead link ([#142](https://github.com/cgartlab/edic-design-system/issues/142)) ([3a3a552](https://github.com/cgartlab/edic-design-system/commit/3a3a5520965fbd2798d31eb3bad25982859e33ca))
* **opencode:** add git identity config ([f91e6d1](https://github.com/cgartlab/edic-design-system/commit/f91e6d172c0ad9cd6333458eca7cefd4dc48caf4))
* **opencode:** add git identity config for Argus bot ([2fd42d9](https://github.com/cgartlab/edic-design-system/commit/2fd42d9db1bf793b25fb229fe24e8e5f2c5bfb4a))
* **opencode:** add git identity config, fix CRLF corruption ([95dd4c9](https://github.com/cgartlab/edic-design-system/commit/95dd4c9c23d0a4dcf94e08353c49c12881189ef7))
* **opencode:** add git remote with app token for push permissions ([451fe77](https://github.com/cgartlab/edic-design-system/commit/451fe77fc33f049dafed4f8cdd59a4486bd85f47))
* **opencode:** add guoxue and fix git push permissions via x-access-token URL ([e37c29c](https://github.com/cgartlab/edic-design-system/commit/e37c29c6c01aa23ac4a57669dc7747198e1c48d4))
* **opencode:** add id-token:write, remove invalid token input, skip synchronize ([9cc4634](https://github.com/cgartlab/edic-design-system/commit/9cc46343397b4b776af844a507fe680153ca4831))
* **opencode:** persist-credentials false + app token remote ([c63fdd9](https://github.com/cgartlab/edic-design-system/commit/c63fdd900b4c95721546d282e4e76ad4e5ff66a8))
* **opencode:** persist-credentials false + x-access-token remote ([962d770](https://github.com/cgartlab/edic-design-system/commit/962d77084e15608e9d405a003e49a6cb864893c9))
* **opencode:** remove persist-credentials false, keep remote override ([12b3c6f](https://github.com/cgartlab/edic-design-system/commit/12b3c6fe3a24bc708efa763139e79055ec3f27ac))
* **opencode:** use credential helper store instead of remote URL token ([88710ef](https://github.com/cgartlab/edic-design-system/commit/88710ef9eb06b804f4f043854d3e3767d8e580a7))
* **opencode:** use token input instead of use_github_token for PR auto-review ([cfbd9a7](https://github.com/cgartlab/edic-design-system/commit/cfbd9a771979e3bfceb2944a81f84f4cdfabdd61))
* **pagenav:** stop scroll-spy from yanking the whole page (issue [#135](https://github.com/cgartlab/edic-design-system/issues/135)) ([be09bed](https://github.com/cgartlab/edic-design-system/commit/be09bed64e4247e23583c2ed73706de330078062))
* **pagenav:** stop scroll-spy from yanking the whole page (issue [#135](https://github.com/cgartlab/edic-design-system/issues/135)) ([#143](https://github.com/cgartlab/edic-design-system/issues/143)) ([5a7602e](https://github.com/cgartlab/edic-design-system/commit/5a7602eb2f295148a8f0d16d4f3d4fe7cf8d73bf))
* prepend the trigger to the focusable elements array so Tab ([a0180a8](https://github.com/cgartlab/edic-design-system/commit/a0180a8ded8eaeb7edc88bb4e18320ef73c346ba))
* prevent Argus self-triggering, add concurrency, upgrade actions ([6b42cc3](https://github.com/cgartlab/edic-design-system/commit/6b42cc3759e56deb1beaa136b80416fdd890bf7e))
* remove dark overlay when mobile menu opens ([ffa2597](https://github.com/cgartlab/edic-design-system/commit/ffa2597e39b28fb8a196117a85b28fb83206f60b))
* replace href=# with javascript:void(0) in blog.html nav links (closes [#50](https://github.com/cgartlab/edic-design-system/issues/50)) ([46bf6a1](https://github.com/cgartlab/edic-design-system/commit/46bf6a171195cfa2707edc0aa452922f23db18ea))
* resolve 19 heading hierarchy jumps across 7 HTML files ([#113](https://github.com/cgartlab/edic-design-system/issues/113)) ([1396473](https://github.com/cgartlab/edic-design-system/commit/139647388185e780c7cca91717e638e1c1fcc0bb))
* resolve 3 P0 mobile issues ([#107](https://github.com/cgartlab/edic-design-system/issues/107)) ([76913ac](https://github.com/cgartlab/edic-design-system/commit/76913ac4c537a7b10266313ab7be5c6e81e0ecab)), closes [#93](https://github.com/cgartlab/edic-design-system/issues/93) [#94](https://github.com/cgartlab/edic-design-system/issues/94) [#95](https://github.com/cgartlab/edic-design-system/issues/95)
* restore CNAME for GitHub Pages custom domain (designsystem.cgartlab.com) ([f118c5c](https://github.com/cgartlab/edic-design-system/commit/f118c5cd02d86af2a41725bd23473250223a1576))
* rewrite mobile nav from working version f52c293 ([78999e4](https://github.com/cgartlab/edic-design-system/commit/78999e414160d7d508f19251bcde74f7d180aa2a))
* **styles:** add --d animation-delay CSS variable default (0ms) in :root ([#86](https://github.com/cgartlab/edic-design-system/issues/86)) ([0326453](https://github.com/cgartlab/edic-design-system/commit/032645387a1010ae149c64f63a60c8e9b4a2e503))
* **styles:** replace ch-unit max-width on hero-lead with min(660px, 100%) for CJK correctness ([#81](https://github.com/cgartlab/edic-design-system/issues/81)) ([60b9db2](https://github.com/cgartlab/edic-design-system/commit/60b9db28dfa4176009224a071c4057ab5ac274ff))
* **tokens:** sync scripts.js letter-spacing and font-stack values with styles.css (closes [#39](https://github.com/cgartlab/edic-design-system/issues/39), [#40](https://github.com/cgartlab/edic-design-system/issues/40)) ([4e23f27](https://github.com/cgartlab/edic-design-system/commit/4e23f2773aa15109ab2bd73cdd1fadb9050c6e88))
* **tokens:** sync version to 1.3.1 (closes [#46](https://github.com/cgartlab/edic-design-system/issues/46)) ([6d74201](https://github.com/cgartlab/edic-design-system/commit/6d74201da6ec2c379e52baadec206b5656830986))
* **tools:** exclude string literal braces from function depth count in validate_naming.py ([#87](https://github.com/cgartlab/edic-design-system/issues/87)) ([0fb6c59](https://github.com/cgartlab/edic-design-system/commit/0fb6c592e709606ea2c4e50583f45d8e8787b918))
* **tools:** implement accurate OKLch-&gt;sRGB conversion in generate_pdfs.py ([#84](https://github.com/cgartlab/edic-design-system/issues/84)) ([e0120cb](https://github.com/cgartlab/edic-design-system/commit/e0120cb9f7f2227edf8cf2292139157c461de86a))
* **tools:** validate_a11y.py — fix has_h1 dead code and _has_accessible_name text check (closes [#32](https://github.com/cgartlab/edic-design-system/issues/32), [#33](https://github.com/cgartlab/edic-design-system/issues/33)) ([81beae7](https://github.com/cgartlab/edic-design-system/commit/81beae7e98e3ebf3d69918936c28d277da9f0282))
* **tools:** validate_html checks description/title; validate_links checks script src (closes [#48](https://github.com/cgartlab/edic-design-system/issues/48), [#49](https://github.com/cgartlab/edic-design-system/issues/49)) ([f87e022](https://github.com/cgartlab/edic-design-system/commit/f87e022aa0aa42ec3524a0b744ba72cc2074aa28))
* **tools:** validate_tokens.py uses brace-depth scanner for :root blocks to handle nested [@media](https://github.com/media) (closes [#37](https://github.com/cgartlab/edic-design-system/issues/37)) ([6203c46](https://github.com/cgartlab/edic-design-system/commit/6203c46b5b3037a3a9704478fe6e171c94c3d938))
* unify handbook TOC with docs/terms sidebar style and fix mobile nav rollback ([8e65e0e](https://github.com/cgartlab/edic-design-system/commit/8e65e0e903da7e3b236faa2147103480ebfb3047))
* unify section spacing to 64px across all pages ([#152](https://github.com/cgartlab/edic-design-system/issues/152)) ([f6dc2e7](https://github.com/cgartlab/edic-design-system/commit/f6dc2e781e6883d807337e42456c7555850ac275))
* update Reference links to valid edic.cgartlab.com URLs (v1.5.5) ([#186](https://github.com/cgartlab/edic-design-system/issues/186)) ([97ba160](https://github.com/cgartlab/edic-design-system/commit/97ba160c7bbc6e13c71d04bf5e36bce86ec6d6f8))
* validator false positives + responsive mobile overrides + mobile TOC ([#116](https://github.com/cgartlab/edic-design-system/issues/116)) ([29b7c6b](https://github.com/cgartlab/edic-design-system/commit/29b7c6bc52036be25914da3934d375128ffe324d))
* **version-sync:** address Codex review P1/P2 feedback on PR [#26](https://github.com/cgartlab/edic-design-system/issues/26) ([e94eacf](https://github.com/cgartlab/edic-design-system/commit/e94eacfc8ad826b4b75010b5538ca562cbc3041e))
* 修复 system 模式跟随系统变化 + 为 company.html 添加主题按钮 ([cb6ae92](https://github.com/cgartlab/edic-design-system/commit/cb6ae92538b8ed4ffb5c61a3518978b6d0327f15))
* 动画结束后移除 stroke 描边，保持与 logo-mark 一致 ([a0ebfcc](https://github.com/cgartlab/edic-design-system/commit/a0ebfcc5ea4bddab7c6ed378e3541f4184e4777f))


### 重构

* **footer:** unify footer layout, update copyright, and add site map ([066a805](https://github.com/cgartlab/edic-design-system/commit/066a8058209a9ea072e390800dc5fe7a36d77dad))
* **footer:** unify footer layout, update copyright, and add site map ([85331ac](https://github.com/cgartlab/edic-design-system/commit/85331ac00ed9792bafec266b211bcd69e26431e1))
* **js:** replace all var with const/let in scripts.js per project coding rules (closes [#56](https://github.com/cgartlab/edic-design-system/issues/56)) ([0e01c92](https://github.com/cgartlab/edic-design-system/commit/0e01c9290ef9e0598979f61a8ca55e2cb8856631))
* mobile nav aligned with design system tokens & patterns ([6cb45d1](https://github.com/cgartlab/edic-design-system/commit/6cb45d1c36dc5a092c6c8daaf5e955b457c84d6a))
* replace 22 inline onclick handlers with event delegation ([#112](https://github.com/cgartlab/edic-design-system/issues/112)) ([fa2c431](https://github.com/cgartlab/edic-design-system/commit/fa2c431d78f7e1fbb30a9c9710f4c6953864dabf))
* **resume:** 重写简历模板与个人信息 ([78b7cd0](https://github.com/cgartlab/edic-design-system/commit/78b7cd0a83cce600b731ad342993dc9c8f3515ae))
* 重构暗色模式切换功能，统一主题按钮样式和逻辑 ([b284b25](https://github.com/cgartlab/edic-design-system/commit/b284b25a9e7e9cd5ae5ccc14830d18a1fe579c3e))


### 文档

* add CLAUDE.md for Claude Code guidance ([3e6b0e9](https://github.com/cgartlab/edic-design-system/commit/3e6b0e9970fefd2e8ecaab6429621c229819eee9))
* add CLAUDE.md for Claude Code guidance ([#130](https://github.com/cgartlab/edic-design-system/issues/130)) ([f33efc9](https://github.com/cgartlab/edic-design-system/commit/f33efc917b1f2a9c1142d33ed24ce93248628537))
* **AGENTS.md:** update doc generation time and add notes ([b180821](https://github.com/cgartlab/edic-design-system/commit/b1808218ed939f0edccdea87dfdefc572776074e))
* **changelog:** add code style specification entry under [Unreleased] ([96122eb](https://github.com/cgartlab/edic-design-system/commit/96122eb28be6b06a81a16fa74f47760d2432a1be))
* **changelog:** add code style specification entry under [Unreleased] ([e0cd97f](https://github.com/cgartlab/edic-design-system/commit/e0cd97f2cdd51e51df9617dacd66a1e919dbb5e8))
* comprehensive v1.5.0 sync — domain, tokens, prompts, SKILL, README rewrite ([a2afe90](https://github.com/cgartlab/edic-design-system/commit/a2afe90dd4f872ec5a312190fb01fce3b34836cf))
* comprehensive v1.5.0 sync — domain, tokens, prompts, SKILL, README rewrite ([#140](https://github.com/cgartlab/edic-design-system/issues/140)) ([e9f0bd2](https://github.com/cgartlab/edic-design-system/commit/e9f0bd240d716e5ddb16e3be58160af43fd449ff))
* document icons.svg generator in AGENTS and CHANGELOG ([5187a1c](https://github.com/cgartlab/edic-design-system/commit/5187a1c64e912371e9024c8d67589abf875bb01f))
* fix handbook timeline fiction and sync tokens/SKILL/validator ([717900c](https://github.com/cgartlab/edic-design-system/commit/717900c752b2ac2c779f255030b49ad271bbe504))
* fix prompts.html/system-prompt.md accuracy and restore CNAME ([18a71bf](https://github.com/cgartlab/edic-design-system/commit/18a71bf778312a6cb102f5849d2ba4991871311d))
* **readme:** rewrite — no emoji, concise, accurate v1.5.0 ([b0056c8](https://github.com/cgartlab/edic-design-system/commit/b0056c85ed5217f1918ca3b45cfc8375dc5c9f6c))
* **sync:** align all documentation with v1.5.0 codebase ([cd4ebbe](https://github.com/cgartlab/edic-design-system/commit/cd4ebbe3d09a1d329aae944733171d5c7078dda9))
* update AGENTS.md date to 2026-06-04 ([b27086b](https://github.com/cgartlab/edic-design-system/commit/b27086b424135a79705a47fd93158ae830bc6da0))
* update AGENTS.md generation date to 2026-05-29 ([a9c596a](https://github.com/cgartlab/edic-design-system/commit/a9c596afda65069738cb89a1b1f49f96fe79b15a))
* **workflow:** document stamp_version.py tool and updated release flow ([e81c4a9](https://github.com/cgartlab/edic-design-system/commit/e81c4a9114ad7b64adfddb1dbb9073c9a9446f2d))
* 更新 README.md，反映最近的代码变更 ([78a5ac2](https://github.com/cgartlab/edic-design-system/commit/78a5ac26013f2cb85e387a23a286e4c48fe4d67d))
* 添加极度详细的网站开发指南文档 ([a209def](https://github.com/cgartlab/edic-design-system/commit/a209defcb957f249f2f41aa4889d841b038f15b1))
* 添加极度详细的网站开发指南文档 ([5f86b51](https://github.com/cgartlab/edic-design-system/commit/5f86b513be5dc7e979ff2249a0300eec75ef4026))
* 统一品牌描述，强调面向非设计师用户 ([#155](https://github.com/cgartlab/edic-design-system/issues/155)) ([e50984d](https://github.com/cgartlab/edic-design-system/commit/e50984dede974294af6ba82d2059ffd43d236c78))


### 样式

* **hero:** 重新设计首页 Hero 区域版式 ([#25](https://github.com/cgartlab/edic-design-system/issues/25)) ([21c63e2](https://github.com/cgartlab/edic-design-system/commit/21c63e28a88d3cbc4f7c28f1560e5a52e4bc9547))
* 完善中文排版规范与细节优化 ([ba4674f](https://github.com/cgartlab/edic-design-system/commit/ba4674fe5b30c43debe9836b1ac537aef7c6e4c3))

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
