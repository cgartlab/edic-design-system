# 测试策略（Testing Strategy）

> 零运行时依赖 ≠ 零测试。本项目采用**轻量、可独立运行**的验证脚本，
> 覆盖设计系统的**核心契约**。

## 测试金字塔（适配设计系统）

```
        ┌─────────┐
        │ Visual  │  (可选：浏览器视觉回归)
        │ Snapshots│
        └─────────┘
      ┌─────────────┐
      │ Integration │  (CI：链接、版本号同步)
      └─────────────┘
   ┌───────────────────┐
   │  Static / Lint    │  (CI：令牌、命名、HTML、a11y)
   └───────────────────┘
```

## 工具栈

| 工具 | 作用 | 语言 | 依赖 |
|------|------|------|------|
| `validate_tokens.py` | tokens.json ↔ styles.css 一致性 | Python 3.11+ | stdlib |
| `validate_naming.py` | BEM / token 命名规范 | Python 3.11+ | stdlib |
| `validate_html.py` | HTML 标签闭合、属性合法性 | Python 3.11+ | stdlib |
| `validate_a11y.py` | 基础可访问性（alt / aria / 标题层级） | Python 3.11+ | stdlib |
| `validate_versions.py` | 资源 `?v=` 与最新版本号同步 | Python 3.11+ | stdlib |
| `validate_links.py` | 内部链接、锚点、CSS / JS 引用有效性 | Python 3.11+ | stdlib |
| `validate_cssref.py` | HTML class → CSS 定义交叉引用验证 | Python 3.11+ | stdlib |
| `validate_darkmode.py` | 暗色模式 token 完整性验证 | Python 3.11+ | stdlib |
| `validate_verext.py` | tokens.json / package.json 版本一致性 | Python 3.11+ | stdlib |
| `validate_hardcode.py` | 硬编码颜色检测（强制使用 token） | Python 3.11+ | stdlib |
| `validate_manifest.py` | `edic-manifest.json` 结构与引用完整性 | Python 3.11+ | stdlib |
| `validate_manifest_css.py` | manifest 核心组件在 CSS 中存在 | Python 3.11+ | stdlib |
| `validate_components.py` | 组件覆盖、ARIA 契约与示例完整性 | Python 3.11+ | stdlib |
| `validate_icons.py` | icons.json / scripts.js / icons.svg 同步 | Python 3.11+ | stdlib |
| `validate_visual_baseline.py` | 视觉基线快照检查 | Python 3.11+ | stdlib |
| **CI 自动化** | 上述全部 | GitHub Actions | 无（除 Python） |

> 工具都是**纯 Python stdlib**，无 `pip install` 需求，保持项目"零运行时依赖"特性。

## 运行方式

### 全部校验

```bash
npm run validate
# 或
make validate
# 发布前完整审计
npm run audit
# 单元测试
npm test
```

### 单项校验

```bash
npm run validate:tokens
npm run validate:naming
npm run validate:html
npm run validate:a11y
npm run validate:versions
npm run validate:links
npm run validate:cssref
npm run validate:darkmode
npm run validate:verext
npm run validate:hardcode
npm run validate:manifest
npm run validate:manifest-css
npm run validate:components
npm run validate:icons
npm run validate:visual-baseline
```

### 在 CI 中

`.github/workflows/ci.yml` 在 PR 与 push 时自动跑全部校验。
失败会阻塞 PR 合并。

## 各工具详细规范

### 1. `validate_tokens.py`

**目标**：确保 `tokens.json` 与 `styles.css` 同步。

**规则**：

- ✅ `tokens.json` 中每个 token 必须在 `styles.css` 中定义
- ✅ `styles.css` 中所有 `--ds-color-*` 应在 `tokens.json` 有对应条目
- ✅ 颜色值必须用 OKLch 表达（不强制覆盖所有 token 类别，但至少 `colors` 必查）
- ✅ 浅色 / 暗色 token 必须成对存在

**示例输出**：

```
[OK] tokens.json ↔ styles.css 同步 (208 tokens)
[WARN] tokens.json 缺少 --ds-color-surface-sunken（建议补全）
[ERROR] styles.css 中 --ds-color-olive-400 与 tokens.json 不一致
```

### 2. `validate_naming.py`

**目标**：强制 BEM / token 命名规范。

**规则**：

- ✅ 组件 class 必须 `ds-{component}` 或 `ds-{component}--{variant}`
- ✅ Token 必须 `--ds-{category}-{name}`
- ✅ 类别前缀必须在白名单中（`color / font / text / weight / ...`）
- ❌ 禁止 `as any` / `@ts-expect-error` / `@ts-ignore`（JS 注释检查）
- ❌ 禁止空 catch 块

### 3. `validate_html.py`

**目标**：HTML 结构合法性。

**规则**：

- ✅ `<html>` 必须有 `lang` 属性
- ✅ `<head>` 必须包含 `<meta charset>` 与 `<meta name="viewport">`
- ✅ `<link rel="stylesheet">` 引用的 CSS 文件存在
- ✅ `<script src>` 引用的 JS 文件存在
- ✅ 标签闭合（HTML5 容错模式只警告，不阻断）
- ✅ 重复 `id` 检测

### 4. `validate_a11y.py`

**目标**：基础可访问性合规。

**规则**：

- ✅ `<img>` 必有 `alt`（装饰性 `alt=""` 允许）
- ✅ 交互元素（`<a>` / `<button>`）必有可访问名称
- ✅ `<a>` 嵌套 `<a>` 警告
- ✅ `<button>` 不嵌套 `<button>` 警告
- ✅ 标题层级连贯（h1 → h2 → h3，不跳级）
- ✅ 页面至少一个 `<h1>`
- ✅ 暗色模式背景与文字对比度提示（基于 OKLch 推算简化模型）

> 完整 a11y 测试应使用 `axe-core`（可选 npx 集成，见 [未来工作](#未来工作)）。

### 5. `validate_versions.py`

**目标**：资源版本号同步。

**规则**：

- ✅ 所有 HTML 的 `styles.css?v=` 与 `scripts.js?v=` 一致
- ✅ `?v=` 值与 `CHANGELOG.md` 最新版本号（或 `VERSION` 文件）一致
- ✅ `?v=` 格式必须是 `X.Y.Z` 或 `X.Y.Z-{prerelease}`
- ✅ HTML / README / AGENTS 中无 `{{DS_VERSION}}` 占位符残留

### 6. `stamp_version.py`（stamp 工具）

**目标**：消除"改 VERSION → 改 6 个 HTML → 改 README → 改 AGENTS"的繁琐手动流程。

**机制**：源码中所有需要同步的位置都写成 `{{DS_VERSION}}` 占位符，stamp 工具
一次性替换为真实版本号。无构建步骤，GitHub Pages 仍可直接部署静态文件。

**使用**：

```bash
npm run stamp                 # 应用变更
npm run stamp:check           # 仅检查（CI 用）
npm run stamp:diff            # 预览 diff
```

**自动触发**：

- pre-commit hook（改 HTML/CSS/JS 时自动 stamp）
- `make stamp-version` / `make stamp-check` / `./scripts/dev.sh stamp`

### 7. `validate_links.py`

**目标**：链接与引用有效性。

**规则**：

- ✅ 内部链接（`href="#xxx"`）的目标 `id` 存在
- ✅ 跨页锚点（`href="page.html#xxx"`）目标存在
- ✅ `assets/...` 引用文件存在
- ⚠️ 外链仅做格式校验（不实际 HTTP 请求）

### 8. `validate_cssref.py`

**目标**：确保 HTML 中使用的 `ds-*` class 在 `styles.css` 中有对应样式定义。

**规则**：

- ✅ HTML 中每个 `ds-*` class 必须在 CSS 中有同名选择器
- ✅ 排除 Prism.js 动态类（`language-*`、`prism-*`、`token-*`）
- ✅ 排除 JS 钩子类（`querySelector('.xxx')` 引用的类）
- ✅ 排除 `<pre><code>` 和 `.ds-code` 代码块中的示例类名
- ✅ 支持复合选择器、`@media` 嵌套、后代选择器的类名提取

**示例输出**：

```
[ERROR] handbook.html:67 未定义的 class: ds-toc
[ERROR] handbook.html:657 未定义的 class: ds-body-sm
```

### 9. `validate_darkmode.py`

**目标**：确保每个颜色/前景/边框/背景 token 在暗色模式中有对应 override。

**规则**：

- ✅ 提取 `:root` 中所有 `--ds-color-*`、`--ds-fg-*`、`--ds-surface-*`、`--ds-border-*` token
- ✅ 与 `[data-theme="dark"]` 块中的 token 集合比对
- ✅ 缺失的 override → WARNING
- ✅ 检测暗色模式中使用纯黑 `oklch(0% 0 0)` → ERROR
- ✅ 排除不需要暗色覆盖的类别（shadow/duration/easing/breakpoints/spacing 等）
- ✅ 检测 orphan dark token（只在暗色块中存在，不在 `:root` 中）→ WARNING

**示例输出**：

```
[WARN] :root has --ds-color-overlay but [data-theme="dark"] is missing its override
[WARN] :root has --ds-blur-lg but [data-theme="dark"] is missing its override
```

### 10. `validate_verext.py`

**目标**：扩展版本一致性校验，覆盖 `validate_versions.py` 未检查的文件。

**规则**：

- ✅ `tokens.json` 的 `version` 字段必须匹配 `VERSION` 文件
- ✅ `package.json` 的 `version` 字段必须匹配 `VERSION` 文件
- ✅ `scripts.js` 是否包含 `?v=` 版本查询串（自身引用）
- ✅ `scripts.js` 中声明的版本常量是否与 `VERSION` 一致

**示例输出**：

```
[ERROR] tokens.json version='1.4.0'，与 VERSION '1.5.0' 不一致
[WARN] scripts.js 自身未使用 ?v= 版本查询串
```

### 11. `validate_hardcode.py`

**目标**：检测 HTML / CSS 中硬编码的颜色值，强制使用 `--ds-*` 设计令牌。

**规则**：

- ❌ 禁止在 CSS 规则中直接使用 `oklch()`、hex、`rgb()`、`hsl()`
- ❌ 禁止在 HTML `style=` 属性中硬编码颜色（WARNING）
- ✅ `--ds-*` 变量定义中的颜色值跳过（它们是 token 定义）
- ✅ `<pre><code>` / `<code>` 代码块中的示例颜色跳过
- ✅ `var(--ds-*)` 引用跳过（引用 token 是正确的）
- ✅ 动画 `@keyframes` 中的颜色跳过（不强制 token）
- ⚠️ SVG `fill=` / `stroke=` 属性中的硬编码颜色 → WARNING

**示例输出**：

```
[ERROR] report.html:59 bare oklch(48% 0.015 60) — use --ds-* token
[ERROR] resume.html:16 bare oklch(96.8% 0.008 95) — use --ds-* token
[WARN] report.html:2094 inline style contains bare oklch(75% 0.012 75) — use --ds-* token
```

## 测试夹具

位于 `tests/fixtures/`：

- `minimal.html` — 最小合法 HTML
- `with-errors.html` — 已知错误的 HTML（用于校验工具本身）
- `tokens-sample.json` — 合法 tokens.json 样本
- `tokens-bad.json` — 非法 tokens.json 样本

## 未来工作

### 短期

- [ ] `validate_a11y.py` 集成 `axe-core`（通过 `npx @axe-core/cli`）
- [ ] HTML 校验工具改用 `html5lib`（更严格）
- [ ] 将视觉基线检查扩展到更多浏览器视口组合
- [ ] 将 gzip 体积预算与 changelog 检查拆为独立 CI summary

### 中期

- [ ] 引入 Storybook-like 组件 playground
- [ ] 视觉测试：Chromatic / Percy（需付费，留作可选）
- [ ] 跨浏览器测试：BrowserStack（可选）

### 长期

- [x] 引入 Vitest，覆盖 JS 桥接与审计脚本
- [ ] 引入 Stylelint 自定义规则
- [ ] 引入 ESLint（针对 `scripts.js`）
- [ ] 引入 Lighthouse CI（性能 / SEO / a11y 综合评分）

## 不在范围内

- ❌ **端到端业务测试** — 当前 `scripts.js` 主要是 DOM 操作与渲染，业务逻辑有限
- ❌ **端到端测试（E2E）** — 项目是纯静态展示站，无业务逻辑
- ❌ **服务器端测试** — 项目无后端

## CI 集成

完整工作流见 [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml)。
简述：

1. **触发**：push 到 main、PR、weekly schedule
2. **环境**：`ubuntu-latest` + Node 20+ + Python ≥ 3.11
3. **步骤**：
   - checkout
   - 运行 `npm run validate`
   - 运行 `npm test`
   - 报告失败 → 阻塞合并

---

*本策略的代码实现见 [`tools/`](../../tools/) 目录。*
