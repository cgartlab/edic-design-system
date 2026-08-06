# 组件开发指南（Component Development Guide）

> 配套 [SKILL.md](../../skills/edic-design-system/SKILL.md) 使用 — SKILL 是 AI 的快速参考，
> 本文是人类的完整工作流。

## 工作流概览

```text
1. 设计提案（Issue）      ── 设计目标 / 视觉草图 / 适用场景
        ↓
2. 令牌先行（必要时）     ── 评估是否需要新令牌，复用现有
        ↓
3. 组件原型               ── 在 docs.html 中加入预览
        ↓
4. 暗色 + 响应式验证      ── 多视口、键盘、屏幕阅读器
        ↓
5. 文档更新               ── DEVELOPMENT-GUIDE.md / AGENTS.md
        ↓
6. 提 PR                  ── 关联 Issue、截图、CI 全绿
```

## 1. 设计提案（Issue）

提交 [Component Request](../../issues/new?template=component_request.md)，包含：

- **组件名**（语义化，如 `Tooltip` 而非 `HoverBox`）
- **使用场景**（哪些页面 / 哪些交互）
- **视觉参考**（截图 / 线框 / 类似系统的链接）
- **API 草案**（HTML 结构草图、类名清单）
- **变体清单**（如 Button 的 primary/secondary/ghost）
- **状态清单**（default / hover / active / focus / disabled）

> 维护者会基于此讨论：是否需要？是否与现有组件重复？是否影响设计语言？

## 2. 令牌先行

新组件**优先复用现有令牌**。仅在确实需要新令牌时新增。

### 令牌命名规范

```
--ds-{category}-{name}[-{modifier}]

类别前缀（参考 SKILL.md 与 AGENTS.md）：
  color / font / text / weight / leading / tracking /
  space / radius / shadow / duration / ease / bp / z / blur / glass
```

### 必填的暗色对应

任何颜色令牌都**必须**有 `[data-theme="dark"]` 对应值。例如：

```css
:root {
  --ds-color-info: oklch(55% 0.08 240);
  --ds-color-info-bg: oklch(95% 0.02 240);
}
[data-theme="dark"] {
  --ds-color-info: oklch(70% 0.08 240);
  --ds-color-info-bg: oklch(25% 0.04 240);
}
```

### 同步更新位置

新增令牌需同步更新：

1. `styles.css` `:root` 与 `[data-theme="dark"]`
2. `tokens.json`（结构化数据）
3. `scripts.js` 的 `TOKENS` 数组（用于令牌表渲染）
4. `docs.html` 的 `#token-index` 章节（自动渲染）
5. `AGENTS.md` 令牌章节（如新增类别）
6. `CHANGELOG.md`（MINOR 条目）

## 3. 组件原型

### 命名规范（BEM）

```css
.ds-component           /* 基础类 */
.ds-component--variant  /* 变体修饰符 */
.ds-component-element   /* 子元素 */
```

### 模板：基础 + 变体

```css
/* ===== Tooltip ===== */
.ds-tooltip {
  position: relative;
  display: inline-block;
}

.ds-tooltip-bubble {
  position: absolute;
  bottom: calc(100% + var(--ds-space-2));
  left: 50%;
  transform: translateX(-50%);
  padding: var(--ds-space-2) var(--ds-space-3);
  background: var(--ds-color-fg-strong);
  color: var(--ds-color-surface-raised);
  font: var(--ds-font-ui) var(--ds-text-caption) / var(--ds-leading-body);
  border-radius: var(--ds-radius-md);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--ds-duration-150) var(--ds-ease-out);
  z-index: var(--ds-z-dropdown);
}

.ds-tooltip:hover .ds-tooltip-bubble,
.ds-tooltip:focus-within .ds-tooltip-bubble {
  opacity: 1;
}

.ds-tooltip--top .ds-tooltip-bubble { bottom: calc(100% + var(--ds-space-2)); top: auto; }
.ds-tooltip--bottom .ds-tooltip-bubble { top: calc(100% + var(--ds-space-2)); bottom: auto; }
```

### HTML 结构

```html
<span class="ds-tooltip">
  <button class="ds-btn ds-btn--primary">保存</button>
  <span class="ds-tooltip-bubble" role="tooltip">保存到草稿</span>
</span>
```

## 4. 质量检查清单

### 视觉

- [ ] 在浅色与暗色模式下都正常
- [ ] 移动端（375px）、平板（768px）、桌面（1440px）三档断点验证
- [ ] 与已有组件视觉协调（间距、圆角、字体一致）
- [ ] 无魔法值（所有颜色/间距/字号都引用 `var(--ds-*)`）

### 交互

- [ ] 键盘可达：Tab 进入、Enter/Space 触发、Esc 取消
- [ ] Focus 状态可见（用 `var(--ds-color-olive-400)` 焦点环）
- [ ] 鼠标交互：hover / active 状态有视觉反馈
- [ ] 触摸设备：触摸目标 ≥ 44×44px

### 可访问性

- [ ] 语义化标签：交互元素用 `<button>` / `<a>`，不用 `<div>`
- [ ] ARIA：必要时 `role` / `aria-*` 完整
- [ ] 图标按钮：`aria-label` 必填
- [ ] 装饰元素：`aria-hidden="true"`
- [ ] 屏幕阅读器：用 NVDA / VoiceOver 测过

### 性能

- [ ] 无内联 `style=`（除动态计算值）
- [ ] 无内联 `onclick`（用 `addEventListener`）
- [ ] 过渡用 `transform` / `opacity`（GPU 友好）
- [ ] 尊重 `prefers-reduced-motion: reduce`

## 5. 图标规范

```html
<!-- viewBox 必须 0 0 24 24 -->
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">
  <path d="..." />
</svg>
```

注册新图标到 `scripts.js`：

```js
{ id: "new-icon", svg: '<svg viewBox="0 0 24 24">...</svg>' }
```

## 6. 提交规范

### 文件改动清单

| 文件 | 何时改 |
|------|--------|
| `styles.css` | 新增/修改组件样式 |
| `scripts.js` | 新增/修改交互逻辑（含 ICONS、TOKENS 数组） |
| `tokens.json` | 同步令牌数据 |
| `docs.html` | 新增预览区块 |
| `AGENTS.md` | 更新组件清单 |
| `DEVELOPMENT-GUIDE.md` | 更新组件说明（如有） |
| `CHANGELOG.md` | 记录变更 |
| 所有 HTML | bump `?v=` 版本号 |
| `docs/COMPONENT-DEVELOPMENT.md` | 工作流更新 |

### 提交前自检

```bash
make validate           # 全部校验
make preview            # 启动本地服务器
# 浏览器中检查 docs.html 新组件
```

### PR 描述

- 关联 Issue（`Closes #N`）
- 截图 / 录屏（浅色 + 暗色 + 移动端）
- 标注破坏性变更（如果有）
- 勾选 CI 全部通过

## 7. 组件生命周期

```
draft → proposal → in-development → review → stable → deprecated → removed
  │         │            │             │         │           │          │
  │       Issue       PR (WIP)      PR 评审   merge       N 版本     N+1 版本
  │                                                                     移除
  └─ 不通过则 cancel
```

| 状态 | 含义 | 对应文档 |
|------|------|----------|
| draft | 个人想法 | 无 |
| proposal | Issue 已开，等评审 | Issue |
| in-development | 编码中 | dev-xxx 分支 |
| review | 提 PR | PULL_REQUEST_TEMPLATE |
| stable | 合并到 main | CHANGELOG |
| deprecated | 不推荐使用，未来移除 | DEPRECATED.md（待建） |
| removed | 移除 | CHANGELOG MAJOR |

## 8. 反模式（不要做的事）

- ❌ **不要**复制现有组件做"略不同的版本" — 优先扩展原组件
- ❌ **不要**引入新颜色色相（除 olive / 语义色外的色相）
- ❌ **不要**使用内联 `style=`（除错峰延迟 `--d` 等动态值）
- ❌ **不要**在 `styles.css` 中写死颜色（必须用 OKLch + 令牌）
- ❌ **不要**在 `data-theme="dark"` 下用纯黑 `oklch(0% 0 0)`
- ❌ **不要**省略 `prefers-reduced-motion` 处理
- ❌ **不要**直接修改 `company.html` 等示例页 — 那是生产级示例，改坏影响信誉
- ❌ **不要**提交未 bump `?v=` 的资源改动（CI 会拒）

## 9. 进阶：贡献给上游

当你想贡献一个组件给 EDIC 设计系统：

1. 先在 Issue 讨论设计方向
2. 维护者同意后，开 `dev-xxx` 分支开发
3. 完成后提 PR，附截图与说明
4. 至少 1 位维护者 LGTM + CI 全绿后合并
5. 进入下个 MINOR 版本发布

---

*本指南与 [DEVELOPMENT-GUIDE.md](../DEVELOPMENT-GUIDE.md) 互补：
DEVELOPMENT-GUIDE.md 是技术参考（已实现的细节），本文是开发流程。*

## 10. 新增图表类型

`ds-chart` 是统一 SVG 图表引擎，支持 bar / line / area / pie / donut / sparkline / combo / stacked / horizontal / multiline 等变体。添加新图表类型时需同步更新以下文件：

### 步骤清单

1. **`scripts.js`**
   - 编写 `renderXxx(config, container)` 渲染函数（SVG 字符串拼接）
   - 在 `renderChart(type, ...)` 的 `switch` 中添加新 case

2. **`styles.css`**
   - 添加 `.ds-chart--xxx` 变体类（布局、尺寸、对齐）
   - 如需新增 token，在 `:root` 中声明（暗色需在 `[data-theme="dark"]` 与 `@media (prefers-color-scheme: dark)` 两处覆盖）

3. **`docs.html`**
   - 在 `#visual-charts` 节添加新类型预览卡片
   - 用折叠代码块包裹（`.ds-accordion--code`），代码块 id 遵循 `chart-code-NN` 编号

4. **`tokens.json`**
   - 如有新增 token，按 dot-notation 同步（如 `"chart-xxx"`）
   - 更新 `"version"` 字段

5. **验证**
   - 运行 `make validate`（全量校验：OKLch 合规、暗色覆盖、token 同步）
   - 运行 `make stamp-version` 同步 HTML 缓存戳
