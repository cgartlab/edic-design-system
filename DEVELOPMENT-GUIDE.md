# EDIC Design System — 极度详细的网站开发指南

**版本:** v1.9.1  
**生成日期:** 2026-05-28  
**适用对象:** 任何大模型 AI 助手 / 前端开发者 / 设计师

---

## 目录

1. [项目总览与架构](#1-项目总览与架构)
2. [文件结构与依赖关系](#2-文件结构与依赖关系)
3. [设计令牌系统（Design Tokens）](#3-设计令牌系统design-tokens)
4. [色彩系统深度解析](#4-色彩系统深度解析)
5. [字体排版系统](#5-字体排版系统)
6. [间距系统与布局模型](#6-间距系统与布局模型)
7. [CSS 样式与视觉渲染的映射关系（核心警告）](#7-css-样式与视觉渲染的映射关系核心警告)
8. [组件库完整指南](#8-组件库完整指南)
9. [暗色模式机制](#9-暗色模式机制)
10. [响应式设计断点系统](#10-响应式设计断点系统)
11. [JavaScript 逻辑详解](#11-javascript-逻辑详解)
12. [视觉效果层（Overlay / Glass / Blur）](#12-视觉效果层overlay--glass--blur)
13. [修改代码时的陷阱与注意事项](#13-修改代码时的陷阱与注意事项)
14. [命名约定与扩展规则](#14-命名约定与扩展规则)
15. [性能与可访问性](#15-性能与可访问性)

---


## 1. 项目总览与架构

### 1.1 项目性质

这是一个 **纯静态单页设计系统文档站点**，没有任何构建工具、框架或打包器。所有代码为原生 HTML + CSS + Vanilla JavaScript。

### 1.2 设计哲学

- **编辑主义（Editorial）**：杂志质感的排版克制、大量留白、衬线标题 + 无衬线正文的经典搭配
- **橄榄绿强调色**：温暖、自信、不浮躁，避免高饱和度的互联网感
- **Token 驱动**：所有视觉属性通过 CSS 自定义属性（Custom Properties）定义，修改变量即可全局更新
- **Penpot 就绪**：图标和组件设计兼容开源设计工具 Penpot 的 SVG 导入

### 1.3 技术栈

| 技术 | 用途 |
|------|------|
| HTML5 | 语义化结构 |
| CSS3 (Custom Properties + OKLch) | 样式与令牌系统 |
| Vanilla JavaScript (ES5 兼容) | 交互逻辑 |
| SVG (内联) | 图标系统 |
| JSON | 结构化令牌数据 |

### 1.4 页面架构（垂直流）

```
┌─────────────────────────────────────────────┐
│ [Decorative Elements] 装饰层（fixed定位）     │
│   └─ 角落SVG线条 + 背景blob光晕              │
├─────────────────────────────────────────────┤
│ [Navbar] 粘性顶部导航（sticky + 毛玻璃）      │
├─────────────────────────────────────────────┤
│ [Floating TOC] 右侧浮动目录（fixed定位）      │
├─────────────────────────────────────────────┤
│ [Cover] 封面区域 — 系统名称 + 版本            │
├─────────────────────────────────────────────┤
│ [TOC Grid] 目录网格 — 快速跳转               │
├─────────────────────────────────────────────┤
│ [Section 01] 色彩系统                        │
│ [Section 02] 字体系统                        │
│ [Section 03] 间距·圆角·阴影                  │
│ [Section 04] 组件库                          │
│ [Section 05] 图标库                          │
│ [Section 06] Overlay & Blur                  │
│ [Section 07] 令牌索引                        │
├─────────────────────────────────────────────┤
│ [Footer] 页脚                               │
├─────────────────────────────────────────────┤
│ [Theme Toggle] 暗色模式切换按钮（fixed定位）   │
└─────────────────────────────────────────────┘
```

---


## 2. 文件结构与依赖关系

### 2.1 文件清单

```
edic-design-system/
├── index.html              # 主页面 — 设计系统视觉目录
├── styles.css              # 样式表 — Token + 组件CSS + 响应式
├── scripts.js              # 脚本 — 图标渲染 + 令牌表 + 交互
├── tokens.json             # 结构化令牌数据 — 程序化导入用
├── AGENTS.md               # AI 知识库 / 项目说明
├── blog.html               # 博客页面（使用设计系统）
├── company.html            # 公司页面
├── resume.html             # 简历页面
├── report.html             # 报告页面
├── docs.html               # 设计系统详情与组件手册
├── prompts.html            # AI 提示词与 Skill 包
├── downloads.html          # PDF 参考、令牌导出、品牌资产
├── CHANGELOG.md            # 更新日志（release-please 维护）
├── CONTRIBUTING.md         # 贡献指南
├── CLAUDE.md               # Claude Code 项目说明
├── DEVELOPMENT-GUIDE.md    # 技术参考指南
├── VERSION                 # 版本号（单一来源）
├── LICENSE                 # CC BY 4.0 许可证
├── prompts/                # system-prompt.md / quick-prompt.md
├── skills/edic-design-system/   # Claude Code SKILL 包
├── tools/                  # 验证脚本（validate_*.py）
├── tests/                  # 验证夹具
├── docs/                   # VERSIONING / COMPONENT-DEVELOPMENT / TESTING / RELEASE-CHECKLIST
├── scripts/                # 本地开发脚本（lint.py / build.py）
└── .github/                # Issue / PR 模板 / Workflows
```

### 2.2 依赖关系图

```
index.html
  ├── <link rel="stylesheet" href="styles.css">  ← 唯一的样式文件
  └── <script src="scripts.js">                   ← 唯一的脚本文件（底部加载）

styles.css
  └── 独立，无外部依赖（不引入Google Fonts等CDN资源）
      └── 字体依赖用户系统已安装字体（font-stack fallback）

scripts.js
  └── 独立，无外部库依赖（纯 Vanilla JS）
      └── 操作 DOM：#icon-grid, #token-tbody, #nav-toggle 等

tokens.json
  └── 独立数据文件，当前未被 JS 直接引用
      └── 用途：为未来的工程化构建（如 style-dictionary）提供数据源
```

### 2.3 加载顺序与时序

1. 浏览器解析 HTML `<head>` → 同步加载 `styles.css`（阻塞渲染）
2. 浏览器逐步解析 `<body>` 内容 → 渲染各 section
3. 到达 `<script src="scripts.js">` → 同步执行脚本
4. 脚本中的 IIFE 立即执行：
   - 渲染 100 个图标到 `#icon-grid`
   - 渲染令牌表到 `#token-tbody`
   - 初始化暗色模式（读取 localStorage / 系统偏好）
   - 绑定 Slider 同步事件
   - 绑定 Navbar 切换事件
   - 生成浮动目录并启动 IntersectionObserver

---


## 3. 设计令牌系统（Design Tokens）

### 3.1 什么是设计令牌

设计令牌是设计系统中所有视觉属性的 **单一来源**。它们以 CSS 自定义属性（`--ds-*`）形式定义在 `:root` 中，所有组件的样式都引用这些变量而非硬编码值。

### 3.2 令牌命名规则

```
--ds-{类别}-{名称}[-{修饰}]

示例：
--ds-color-olive-400    类别=color, 名称=olive, 修饰=400
--ds-space-12           类别=space, 名称=12
--ds-radius-xl          类别=radius, 名称=xl
--ds-leading-body       类别=leading(行高), 名称=body
--ds-tracking-wide      类别=tracking(字距), 名称=wide
```

### 3.3 令牌分类总览

| 类别 | 前缀 | 数量 | 说明 |
|------|------|------|------|
| 色彩 | `--ds-color-*` | ~36 | 中性色、橄榄绿色阶、语义色 |
| 强调色 | `--ds-accent*` | 4 | 主强调色及其变体 |
| 字体族 | `--ds-font-*` | 4 | Display/Body/Mono/UI |
| 字号 | `--ds-text-*` | 11 | caption 到 hero |
| 字重 | `--ds-weight-*` | 5 | 300-700 |
| 行高 | `--ds-leading-*` | 5 | tight/snug/body/relaxed/loose |
| 字距 | `--ds-tracking-*` | 7 | tight 到 widest + CJK专用 |
| 间距 | `--ds-space-*` | 20 | 0-32 (4px为单位) |
| 圆角 | `--ds-radius-*` | 7 | none 到 full |
| 阴影 | `--ds-shadow-*` | 7 | xs 到 2xl + inner |
| 动画时长 | `--ds-duration-*` | 8 | 50ms-1000ms |
| 缓动函数 | `--ds-ease-*` | 4 | out/in/in-out/spring |
| 断点 | `--ds-bp-*` | 5 | sm/md/lg/xl/2xl |
| z-index | `--ds-z-*` | 6 | base/above/dropdown/sticky/overlay/modal/toast |
| 模糊 | `--ds-blur-*` | 4 | sm/md/lg/xl |
| 玻璃效果 | `--ds-glass-*` | 3 | bg/border/shadow |
| 遮罩 | `--ds-color-overlay*` | 2 | 普通/轻量 |

### 3.4 令牌的层级关系

```
原始值（Primitive）           → 语义值（Semantic）          → 组件值（Component）
oklch(52% 0.08 115)          → --ds-color-olive-400       → --ds-accent
                                                           → .ds-btn--primary background
```

这意味着：
- 修改 `--ds-color-olive-400` 的值 → 所有引用 `--ds-accent` 的组件颜色同步变化
- 修改 `--ds-accent` 的引用对象 → 可以将强调色切换到另一个色阶

---


## 4. 色彩系统深度解析

### 4.1 OKLch 色彩空间

本系统所有颜色使用 **OKLch** 定义（而非传统的 hex/rgb/hsl），语法为：

```css
oklch(亮度% 彩度 色相)
oklch(52% 0.08 115)
       │    │    └─ 色相角度（0-360），115 = 橄榄绿/黄绿
       │    └─ 彩度/饱和度（0=灰，0.4=极高饱和）
       └─ 感知亮度（0%=黑，100%=白）
```

**为什么用 OKLch：**
- 感知均匀：同亮度值的不同色相看起来一样亮（传统HSL做不到）
- 可预测性：改变色相角度不影响感知亮度
- 暗色模式更精准：只需调整 L 值即可产生一致的暗色变体

### 4.2 中性色体系（Neutral Palette）

```
高亮度（背景层）                              低亮度（文字层）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
bg(97%) → surface(99%) → raised(100%)       muted(48%) → fg-subtle(35%) → fg(20%) → fg-strong(14%)
         ← 表面层 →                                      ← 文字层 →
```

**关键色相角度：80（暖黄）→ 60（暖棕）**

| Token | 亮度 | 彩度 | 色相 | 视觉效果 |
|-------|------|------|------|----------|
| `--ds-color-bg` | 97% | 0.012 | 80 | 微暖的"纸色"背景，不是纯白 |
| `--ds-color-surface` | 99% | 0.005 | 80 | 接近纯白但有微暖 |
| `--ds-color-surface-raised` | 100% | 0 | 0 | 纯白，用于弹出层 |
| `--ds-color-border-subtle` | 92% | 0.012 | 80 | 极浅分隔线 |
| `--ds-color-border` | 89% | 0.012 | 80 | 标准边框 |
| `--ds-color-border-strong` | 82% | 0.015 | 75 | 明显边框 |
| `--ds-color-muted` | 48% | 0.015 | 60 | 辅助文字（灰色） |
| `--ds-color-fg-subtle` | 35% | 0.018 | 60 | 次要文字 |
| `--ds-color-fg` | 20% | 0.02 | 60 | 正文主色 |
| `--ds-color-fg-strong` | 14% | 0.025 | 60 | 标题/强调文字 |

### 4.3 橄榄绿色阶（Olive Green）

色相角度固定为 **115**（黄绿），通过调整亮度和彩度产生 10 级色阶：

```
浅 ←─────────────────────────────────────→ 深
50    100   200   300   ★400   500   600   700   800   900
90%   82%   72%   62%   52%   45%   38%   30%   22%   15%  ← 亮度
.025  .035  .05   .065  .08   .085  .08   .07   .055  .04  ← 彩度
```

★ **Olive-400 是主强调色**（`--ds-accent`）：
- 亮度 52% 确保在白色背景上有足够对比度
- 彩度 0.08 保持克制、不刺眼

### 4.4 语义色

| 用途 | Token | 亮度 | 彩度 | 色相 | 说明 |
|------|-------|------|------|------|------|
| 成功 | `--ds-color-success` | 55% | 0.1 | 145 | 绿色系 |
| 警告 | `--ds-color-warning` | 65% | 0.1 | 85 | 黄橙色 |
| 错误 | `--ds-color-error` | 50% | 0.14 | 30 | 红色系 |
| 信息 | `--ds-color-info` | 55% | 0.08 | 240 | 蓝色系 |

每种语义色都有对应的 `*-bg` 浅色背景变体（用于 Alert 组件背景）。

### 4.5 色彩的实际视觉影响

> **⚠️ 重要警告：OKLch 的数值变化与视觉变化不是线性的**

- 亮度从 90% 降到 80%：视觉上变化很小（都是浅色）
- 亮度从 50% 降到 40%：视觉上变化显著（中间调最敏感）
- 彩度从 0.01 提到 0.03：几乎无感知差异
- 彩度从 0.06 提到 0.12：颜色饱和度变化明显
- 色相变化 10 度：在低彩度时几乎不可见，高彩度时明显

---


## 5. 字体排版系统

### 5.1 四种字体角色

| 角色 | CSS变量 | 字体栈 | 使用场景 |
|------|---------|--------|----------|
| **Display** | `--ds-font-display` | Iowan Old Style → Charter → Georgia → Noto Serif SC → Source Han Serif SC → serif | 大标题（Hero/H1-H4） |
| **Body** | `--ds-font-body` | Noto Sans SC → Source Han Sans SC → -apple-system → BlinkMacSystemFont → Segoe UI → system-ui → sans-serif | 正文内容 |
| **Mono** | `--ds-font-mono` | JetBrains Mono → IBM Plex Mono → Noto Sans Mono SC → ui-monospace → monospace | 代码、令牌值 |
| **UI** | `--ds-font-ui` | Noto Sans SC → Source Han Sans SC → -apple-system → BlinkMacSystemFont → Segoe UI → system-ui → sans-serif | 按钮、输入框、导航 |

**重要：** Body 和 UI 使用相同字体栈，区别在于 UI 通常字号更小、字重更重。

### 5.2 字号比例尺（Type Scale）

```
72px ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Hero     (4.5rem)
60px ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   Display  (3.75rem)
48px ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━         H1       (3rem)
36px ━━━━━━━━━━━━━━━━━━━━━━━━              H2       (2.25rem)
30px ━━━━━━━━━━━━━━━━━━━━━                 H3       (1.875rem)
24px ━━━━━━━━━━━━━━━━━━                    H4       (1.5rem)
20px ━━━━━━━━━━━━━━━                       H5/Lead  (1.25rem)
18px ━━━━━━━━━━━━━━                        Body LG  (1.125rem)
16px ━━━━━━━━━━━━━                         Body     (1rem)     ← 基准
14px ━━━━━━━━━━━━                          Body SM  (0.875rem)
12px ━━━━━━━━━                             Caption  (0.75rem)
```

### 5.3 行高（Line Height）与应用场景

| Token | 值 | 应用 | 视觉效果 |
|-------|-----|------|----------|
| `--ds-leading-tight` | 1.1 | Hero, Display, H1 | 行间紧凑，大字使用 |
| `--ds-leading-snug` | 1.25 | H2, H3, H4, Caption | 略紧凑，中标题用 |
| `--ds-leading-body` | 1.55 | Body, Body SM | 舒适阅读行高 |
| `--ds-leading-relaxed` | 1.7 | CJK 特别场景 | 中文行距更宽松 |
| `--ds-leading-loose` | 2 | 预留 | 极宽行距 |

**⚠️ 视觉陷阱：** 行高 1.1 和 1.55 的差异在小字号时几乎不可见，但在 72px Hero 字号时差距巨大（实际行间距差 = 72 × (1.55-1.1) = 32px）。

### 5.4 字距（Letter Spacing）

| Token | 值 | 应用 | 原因 |
|-------|-----|------|------|
| `--ds-tracking-tight` | -0.01em | Hero/Display/H1 | 大字需紧缩，否则字间显松散 |
| `--ds-tracking-normal` | 0.02em | H2-H4/Body/按钮 | 标准间距 |
| `--ds-tracking-wide` | 0.04em | Nav links, Buttons | UI 元素略宽 |
| `--ds-tracking-wider` | 0.08em | Caption, Eyebrow | 小字全大写需要更宽字距 |
| `--ds-tracking-widest` | 0.12em | 装饰性文字 | 极宽字距 |
| `--ds-tracking-cjk-body` | 0.03em | 中文正文 | CJK 字符需额外字距 |
| `--ds-tracking-cjk-heading` | 0.06em | 中文标题 | CJK 标题更宽 |

**⚠️ CJK 覆盖机制：** 在 `styles.css` 中，有专门的选择器将 CJK 字距应用到 body/p/li 等元素（覆盖默认的 tracking-normal）：
```css
body, p, li, .ds-wrapper, ... { letter-spacing: var(--ds-tracking-cjk-body) }
h1, h2, h3, h4, h5, h6, ...  { letter-spacing: var(--ds-tracking-cjk-heading) }
```

### 5.5 字重（Font Weight）

| Token | 值 | 使用场景 |
|-------|-----|----------|
| `--ds-weight-light` | 300 | 副标题（subtitle） |
| `--ds-weight-regular` | 400 | 正文 |
| `--ds-weight-medium` | 500 | 标签页、导航 |
| `--ds-weight-semibold` | 600 | H3/H4、表单标签、Caption |
| `--ds-weight-bold` | 700 | Hero/Display/H1/H2、品牌名 |

---


## 6. 间距系统与布局模型

### 6.1 间距比例尺（4px 基础）

所有间距值为 4px 的倍数：

| Token | rem | px | 典型用途 |
|-------|-----|-----|----------|
| `--ds-space-0` | 0 | 0 | 无间距 |
| `--ds-space-1` | 0.25rem | 4px | 微间距（图标与文字间） |
| `--ds-space-2` | 0.5rem | 8px | 元素内紧凑间距 |
| `--ds-space-3` | 0.75rem | 12px | 元素内标准间距 |
| `--ds-space-4` | 1rem | 16px | 组件内间距 |
| `--ds-space-5` | 1.25rem | 20px | 标题→正文间距 |
| `--ds-space-6` | 1.5rem | 24px | 段落间距、wrapper padding |
| `--ds-space-8` | 2rem | 32px | 组件预览区 padding |
| `--ds-space-12` | 3rem | 48px | section-header 底部 margin |
| `--ds-space-16` | 4rem | 64px | 大区块分隔 |
| `--ds-space-20` | 5rem | 80px | section 的垂直 padding |
| `--ds-space-24` | 6rem | 96px | 超大间距 |
| `--ds-space-32` | 8rem | 128px | Cover 顶部 padding |

### 6.2 布局容器

```css
.ds-wrapper {
  max-width: 1200px;     /* 内容最大宽度 */
  margin: 0 auto;         /* 水平居中 */
  padding: 0 var(--ds-space-6);  /* 左右 24px 安全边距 */
}
```

**视觉效果：** 在 1200px 以下屏幕，内容填满（左右各留 24px）；超过 1200px 后内容居中，两侧留白增加。

### 6.3 网格系统

本系统使用 CSS Grid 的 `auto-fill` + `minmax()` 模式，不是传统 12 栏网格：

| 类名 | 列宽 | Gap | 典型用途 |
|------|------|-----|----------|
| `.ds-grid-4` | `repeat(auto-fill, minmax(220px, 1fr))` | 24px | 色彩卡片、排版卡片 |
| `.ds-grid-6` | `repeat(auto-fill, minmax(150px, 1fr))` | 16px | 阴影展示 |
| `.ds-grid-icons` | `repeat(auto-fill, minmax(72px, 1fr))` | 8px | 图标网格 |
| `.ds-toc-grid` | `repeat(auto-fill, minmax(200px, 1fr))` | 24px | 目录卡片 |

**⚠️ 视觉陷阱：** `auto-fill` 意味着列数随视口宽度自动变化。在 1200px 宽度下：
- `.ds-grid-4` → 大约 4-5 列
- `.ds-grid-icons` → 大约 15 列
- 但在手机 375px 宽度下，`.ds-grid-4` 响应式被覆盖为 1 列

### 6.4 Section 布局模式

```css
.ds-section {
  padding: var(--ds-space-20) 0;        /* 上下各 80px */
  border-bottom: 1px solid var(--ds-color-border);  /* 章节分隔线 */
}
.ds-section:last-of-type {
  border-bottom: none;                   /* 最后一个章节无底线 */
}
```

每个 section 内部结构：
```html
<section class="ds-section" id="xxx">
  <div class="ds-wrapper">
    <div class="ds-section-header">     <!-- max-width: 600px -->
      <span class="ds-caption">01</span>
      <h2 class="ds-h2 ds-serif ds-mt-12">标题</h2>
      <p>描述</p>
    </div>
    <!-- 内容区域 -->
  </div>
</section>
```

### 6.5 工具类（Utility Classes）

| 类名 | 效果 |
|------|------|
| `.ds-mt-12` | margin-top: 3rem (48px) |
| `.ds-mt-20` | margin-top: 5rem (80px) |
| `.ds-mb-6` | margin-bottom: 1.5rem (24px) |
| `.ds-mb-8` | margin-bottom: 2rem (32px) |
| `.ds-mb-12` | margin-bottom: 3rem (48px) |
| `.ds-mb-16` | margin-bottom: 4rem (64px) |
| `.ds-flex-row` | display:flex; flex-wrap:wrap; gap:16px; align-items:center |
| `.ds-serif` | font-family: var(--ds-font-display) |
| `.ds-mono` | font-family: var(--ds-font-mono) |

---


## 7. CSS 样式与视觉渲染的映射关系（核心警告）

> **🚨 这是本指南最重要的章节。代码中修改一个 CSS 属性，不等于视觉上产生直观对应的变化。以下是需要深刻理解的映射陷阱。**

### 7.1 padding/margin 与视觉间距不等价

**现象：** 给一个元素增加 `padding-top: 20px` 不一定让它看起来下移了 20px。

**原因：**
- `padding` 增加的是内容与边框的距离，如果元素没有背景色/边框，视觉上不可见
- `margin` 在 block 元素间会发生 **margin collapse**（外边距折叠）
- 本系统使用 `box-sizing: border-box`（全局 reset），padding 包含在宽高内

**本系统的实际情况：**
```css
.ds-section { padding: var(--ds-space-20) 0; }
/* 上下各 80px 的 padding — 但视觉上只看到"章节间有大量留白" */
/* 实际"留白"= 上一个section的 padding-bottom(80px) + 下一个的 padding-top(80px) = 160px */
/* 但中间的 border-bottom 1px 打断了这个空间 */
```

### 7.2 font-size 与视觉大小不等价

**现象：** `font-size: 3rem` 的"A"和"中"看起来完全不同大小。

**原因：**
- `font-size` 定义的是 **em square**（字体设计框），不是字符实际渲染高度
- 西文字母的 ascender/descender 导致实际高度小于 font-size
- CJK 字符通常填满整个 em square，看起来"更大"
- 不同字体的 x-height 差异导致同 font-size 下视觉大小不同

**本系统的应对：**
- Display 字体（衬线）的视觉高度通常比 Body（无衬线）大
- 标题用衬线字体时，视觉占据空间大于其 CSS font-size 暗示的比例

### 7.3 line-height 的计算方式

```
实际行间距 = font-size × line-height - font-size
           = font-size × (line-height - 1)

示例：
- Hero 72px × line-height 1.1 → 行框高 79.2px → 行间距仅 7.2px
- Body 16px × line-height 1.55 → 行框高 24.8px → 行间距 8.8px
```

**⚠️ 陷阱：** Hero 字号虽然行高值 (1.1) 小于 Body (1.55)，但绝对行间距差异不大。视觉上 Hero 的行看起来"紧贴"是因为字符本身很大，相对间距小。

### 7.4 letter-spacing 在不同字号下的视觉差异

```css
--ds-tracking-tight: -0.01em;
/* 在 72px Hero 上 = -0.72px — 几乎不可见的紧缩 */
/* 在 12px Caption 上 = -0.12px — 完全不可见 */

--ds-tracking-wider: 0.08em;
/* 在 72px Hero 上 = 5.76px — 极度宽松！不应使用 */
/* 在 12px Caption 上 = 0.96px — 刚好的全大写字距 */
```

**结论：** `em` 单位的 letter-spacing 是相对的，必须搭配正确的字号使用。

### 7.5 border-radius 与元素尺寸的关系

```css
.ds-radius-full { border-radius: 9999px; }
/* 在 40×40px 的 Avatar 上 → 完美圆形 */
/* 在 200×40px 的 Button 上 → 胶囊形状（两端半圆） */
/* 在 300×200px 的 Card 上 → 仍然是胶囊形，但不是圆形 */

.ds-radius-xl { border-radius: 12px; }
/* 在 40×40px 的元素上 → 几乎变成圆形 */
/* 在 400×300px 的 Card 上 → 优雅的圆角矩形 */
```

### 7.6 box-shadow 的层叠与方向

本系统阴影全部为 **向下扩散**（y-offset 为正值）：

```css
--ds-shadow-md: 0 4px 6px oklch(0% 0 0 / 6%), 0 2px 4px oklch(0% 0 0 / 4%);
/*              x y blur                        x y blur                      */
```

- 第一层：大范围柔和阴影（6px 模糊）
- 第二层：小范围锐利阴影（4px 模糊）
- 双层阴影产生更自然的深度感

**⚠️ 暗色模式下阴影 opacity 大幅增加**（从 6% 增到 35%），因为暗底上低透明度阴影不可见。

### 7.7 `max-width` 不等于实际宽度

```css
.ds-input { max-width: 320px; width: 100%; }
/* 在 > 320px 的容器中 → 宽 320px */
/* 在 < 320px 的容器中 → 宽等于容器宽（100%） */
/* 视觉上：桌面端 input 是固定宽；手机端填满 */
```

### 7.8 `position: sticky` 的滚动行为

```css
.ds-navbar { position: sticky; top: 0; z-index: var(--ds-z-sticky); }
```

- Navbar 在页面顶部时正常流动
- 向下滚动超过其原始位置后，"粘"在视口顶部
- 配合 `backdrop-filter: blur()` 产生"内容从导航下方滑过"的视觉效果
- `scroll-padding-top: 72px` 确保锚点跳转时内容不被 Navbar 遮挡

### 7.9 `transform` 不触发重排

```css
.ds-swatch-color:hover { transform: scale(1.03); }
.ds-toggle-thumb { transition: transform .2s; }
.ds-toggle input:checked + .ds-toggle-track .ds-toggle-thumb { transform: translateX(16px); }
```

- `transform` 在 GPU 层合成，不影响文档流
- 使用 `scale(1.03)` 放大不会推开周围元素
- 使用 `translateX(16px)` 移动 Toggle thumb 不会改变布局

### 7.10 `backdrop-filter` 的视觉前提

```css
.ds-navbar { backdrop-filter: blur(var(--ds-blur-lg)); background: var(--ds-glass-bg); }
```

**生效条件：** 元素的 background 必须有透明度！`--ds-glass-bg` 是 `oklch(97% 0.012 80 / 0.55)` — 55% 不透明度。如果改为 100% 不透明，`backdrop-filter` 完全无效（因为没有可透过的区域）。

---


## 8. 组件库完整指南

### 8.1 组件命名规范

```
.ds-{组件名}           → 基础组件
.ds-{组件名}--{变体}   → BEM 修饰符
.ds-{组件名}-{子元素}  → BEM 子元素

示例：
.ds-btn               → 按钮基础
.ds-btn--primary      → 主按钮变体
.ds-btn--sm           → 小尺寸变体
.ds-card              → 卡片基础
.ds-card--hoverable   → 可悬浮卡片
.ds-modal-header      → 模态框头部子元素
```

### 8.2 按钮组件（Button）

**HTML 结构：**
```html
<button class="ds-btn ds-btn--primary">Primary</button>
<button class="ds-btn ds-btn--secondary">Secondary</button>
<button class="ds-btn ds-btn--ghost">Ghost</button>
<button class="ds-btn ds-btn--primary ds-btn--sm">Small</button>
<button class="ds-btn ds-btn--primary ds-btn--lg">Large</button>
<button class="ds-btn ds-btn--primary" disabled>Disabled</button>
```

**视觉尺寸与间距：**

| 变体 | padding | font-size | 视觉高度(约) |
|------|---------|-----------|-------------|
| 默认 | 10px 20px | 14px (body-sm) | 36px |
| `--sm` | 6px 12px | 12px (caption) | 26px |
| `--lg` | 12px 28px | 16px (body) | 42px |

**样式细节：**
- `display: inline-flex` + `align-items: center` → 图标和文字垂直居中
- `gap: 8px` → 图标与文字间距
- `border-radius: 4px` (radius-md) → 微圆角，不是圆润也不是直角
- `transition: all .15s` → 悬浮/点击有 150ms 的快速过渡
- `white-space: nowrap` → 文字不换行

**三种变体的视觉差异：**
- **Primary：** 实心橄榄绿底 + 白色文字 → 最突出的行动按钮
- **Secondary：** 透明底 + 灰色边框 + 正文色文字 → 次要操作
- **Ghost：** 完全透明 + 灰色文字 → 最低优先级操作

### 8.3 卡片组件（Card）

```css
.ds-card {
  background: var(--ds-color-surface-raised);  /* 纯白 */
  border: 1px solid var(--ds-color-border);    /* 浅灰边框 */
  border-radius: var(--ds-radius-xl);          /* 12px 圆角 */
  padding: var(--ds-space-6);                  /* 24px 内距 */
}
```

**三种变体：**
- **默认：** 白底 + 边框 → 标准内容容器
- **`--hoverable`：** 悬浮时出现 `box-shadow: var(--ds-shadow-md)` → 交互暗示
- **`--flat`：** 无边框 + `box-shadow: var(--ds-shadow-xs)` → 更轻量的卡片

### 8.4 输入框（Input）

```css
.ds-input {
  padding: 10px 14px;                          /* 内部空间 */
  background: var(--ds-color-surface-raised);  /* 白底 */
  border: 1px solid var(--ds-color-border);    /* 灰边框 */
  border-radius: var(--ds-radius-md);          /* 4px 圆角 */
  max-width: 320px;                            /* 最大宽度限制 */
  width: 100%;                                 /* 但可占满容器 */
}
.ds-input:focus {
  border-color: var(--ds-accent);              /* 聚焦时边框变绿 */
  box-shadow: 0 0 0 2px var(--ds-accent-soft); /* 外发光环 */
}
```

**错误状态：** `.ds-input--error` 将边框改为红色，focus ring 也变红色。

### 8.5 Toggle/Switch 组件

这是纯 CSS 实现的开关组件（无 JS）：

```html
<label class="ds-toggle">
  <input type="checkbox">
  <span class="ds-toggle-track">
    <span class="ds-toggle-thumb"></span>
  </span>
  Notifications
</label>
```

**工作原理：**
1. `<input>` 被 `display: none` 隐藏
2. `.ds-toggle-track` 是 36×20px 的椭圆轨道
3. `.ds-toggle-thumb` 是 16×16px 的圆形滑块，通过 `position: absolute` 定位
4. `input:checked + .ds-toggle-track` 改变轨道背景色为绿色
5. `input:checked + .ds-toggle-track .ds-toggle-thumb` 用 `transform: translateX(16px)` 滑动到右侧

### 8.6 手风琴（Accordion）

```html
<div class="ds-accordion-item open">
  <div class="ds-accordion-header" onclick="this.parentElement.classList.toggle('open')">
    <span>问题标题</span>
    <span class="ds-accordion-arrow">▾</span>
  </div>
  <div class="ds-accordion-content">回答内容</div>
</div>
```

**展开/收起机制：**
- `.ds-accordion-content` 默认 `display: none`
- `.ds-accordion-item.open .ds-accordion-content` 设为 `display: block`
- 箭头通过 `.open .ds-accordion-arrow { transform: rotate(180deg) }` 旋转
- 使用 inline `onclick` 切换 `.open` 类

### 8.7 标签页（Tabs）

**视觉样式：** 胶囊/药丸形状的标签组，不是传统的下划线标签。

```css
.ds-tabs {
  display: inline-flex;
  border-radius: var(--ds-radius-xl);      /* 12px 外壳圆角 */
  background: var(--ds-color-surface);      /* 浅灰背景 */
  padding: 3px;                             /* 内边距形成"凹槽" */
  border: 1px solid var(--ds-color-border-subtle);
}
.ds-tab--active {
  background: var(--ds-accent-soft);        /* 浅绿色高亮 */
  color: var(--ds-accent);                  /* 绿色文字 */
}
```

### 8.8 时间轴（Timeline）

**布局原理：**
```
│  ← 2px 宽的垂直线（::before伪元素，left: 20px）
●  ← 20px圆点（position: absolute, left: 11px）
    [内容卡片] ← padding-left: 56px (space-14) 避开线和点
│
●
    [内容卡片]
```

- 垂直线是 `.ds-timeline::before`，绝对定位，宽 2px，颜色为 `border-subtle`
- 圆点是 `.ds-timeline-dot`，20×20px，3px 实心绿色边框，白色填充
- 悬浮效果：圆点变为绿色实心 + 外发光扩大 + scale(1.1)

### 8.9 联系表单（Contact Form）

**布局：** 使用 `.ds-form-row` 创建两列网格（姓名 + 邮箱并排），在 `<640px` 屏幕下折叠为单列。

**输入框样式：** `.ds-form-input` 比基础 `.ds-input` 更大：
- padding: 12px 16px（更宽松）
- border-radius: 8px (radius-lg)（更圆润）
- font-size: 16px (body)（防止 iOS 自动缩放）

### 8.10 日期选择器（Date Picker）

纯展示性组件（无 JS 交互逻辑），结构：
- 输入框 + 日历图标（SVG 绝对定位在右侧）
- 日历面板：7×6 网格 + 星期头
- 选中日期：实心绿色圆角背景
- 今天日期：绿色文字 + 底部小圆点标记（`::after` 伪元素）
- 灰色日期：上/下月溢出日期，`cursor: not-allowed`

---


## 9. 暗色模式机制

### 9.1 触发方式

暗色模式通过在 `<html>` 元素上添加 `data-theme="dark"` 属性触发：

```html
<html lang="zh-CN" data-theme="dark">  <!-- 暗色模式 -->
<html lang="zh-CN">                     <!-- 浅色模式（默认） -->
```

### 9.2 CSS 覆盖策略

```css
[data-theme="dark"] {
  --ds-color-bg: oklch(15% 0.008 75);           /* 97% → 15% 反转 */
  --ds-color-surface: oklch(19% 0.008 75);      /* 99% → 19% */
  --ds-color-surface-raised: oklch(23% 0.01 75); /* 100% → 23% */
  --ds-color-fg: oklch(84% 0.008 72);           /* 20% → 84% 反转 */
  /* ... 所有颜色令牌重新定义 */
}
```

**关键设计决策：**
- 背景不用纯黑 `oklch(0%)` → 用暖灰 `oklch(15% 0.008 75)` 保持温暖感
- 文字不用纯白 `oklch(100%)` → 用 `oklch(84%)` 降低对比度刺眼感
- 橄榄绿从 olive-400 `oklch(52%)` 亮化到 `oklch(57%)` 确保暗底上可见
- 阴影 opacity 从 4-12% 提高到 25-50%（暗底上低 opacity 阴影不可见）

### 9.3 JavaScript 初始化逻辑

```javascript
// 优先级：localStorage > 系统偏好 > 默认浅色
(function() {
  var s = localStorage.getItem("ds-theme");
  if (s === "dark") {
    document.documentElement.setAttribute("data-theme", "dark");
    return;
  }
  if (!s && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    document.documentElement.setAttribute("data-theme", "dark");
  }
})();
```

### 9.4 切换函数

```javascript
function toggleDarkMode() {
  var h = document.documentElement;
  var d = h.getAttribute("data-theme") === "dark";
  h.setAttribute("data-theme", d ? "" : "dark");
  localStorage.setItem("ds-theme", d ? "light" : "dark");
}
```

### 9.5 过渡动画

```css
html { transition: background .4s, color .4s; }
body { transition: background .4s, color .4s; }
```

切换时整个页面背景和文字颜色有 400ms 的平滑过渡。

### 9.6 切换按钮 UI

固定在右下角的 44px 圆形按钮：
- `position: fixed; bottom: 24px; right: 24px;`
- 毛玻璃效果：`backdrop-filter: blur(8px)` + 半透明背景
- 包含两个 SVG 图标（月亮/太阳），通过 CSS 控制显示/隐藏：
  ```css
  [data-theme="dark"] #theme-toggle .moon-icon { display: none; }
  [data-theme="dark"] #theme-toggle .sun-icon { display: block; }
  #theme-toggle .sun-icon { display: none; }   /* 浅色时隐藏太阳 */
  #theme-toggle .moon-icon { display: block; }  /* 浅色时显示月亮 */
  ```

---


## 10. 响应式设计断点系统

### 10.1 断点定义

| Token | 值 | 对应设备 |
|-------|-----|----------|
| `--ds-bp-sm` | 640px | 大手机/小平板竖屏 |
| `--ds-bp-md` | 768px | 平板竖屏 |
| `--ds-bp-lg` | 1024px | 平板横屏/小笔记本 |
| `--ds-bp-xl` | 1280px | 笔记本 |
| `--ds-bp-2xl` | 1536px | 桌面显示器 |

### 10.2 媒体查询断点（实际使用）

```css
/* 小屏（手机）*/
@media (max-width: 639px) {
  .ds-cover h1 { font-size: 2.25rem; }      /* Hero 从 4.5rem 缩到 2.25rem */
  .ds-section { padding: var(--ds-space-12) 0; }  /* 80px → 48px */
  .ds-wrapper { padding: 0 var(--ds-space-4); }   /* 24px → 16px */
  .ds-grid-4 { grid-template-columns: 1fr; }      /* 多列 → 单列 */
}

/* Navbar 移动端/平板（< --ds-bp-lg 1024px）*/
@media (max-width: 1023px) {
  .ds-navbar-links {
    position: fixed;
    right: 0; top: 0; bottom: 0;
    width: min(340px, 86vw);
    transform: translateX(100%);   /* 默认滑出屏幕 */
    /* 打开时：transform: translateX(0) */
  }
  .ds-mnav-trigger { display: block; }  /* 显示汉堡菜单 */
}

/* 中屏（平板）*/
@media (min-width: 640px) and (max-width: 1023px) {
  .ds-grid-4 { grid-template-columns: repeat(2, 1fr); }  /* 4列→2列 */
}

/* 大屏调整 */
@media (min-width: 1024px) and (max-width: 1439px) {
  .ds-wrapper { padding: 0 var(--ds-space-8); }  /* 24px → 32px */
}

/* 浮动目录仅在大屏显示 */
@media (max-width: 1023px) {
  .ds-floating-toc { display: none; }
}
```

### 10.3 响应式变化的视觉影响总结

| 视口宽度 | 封面标题 | 网格列数 | 边距 | Section间距 | 浮动TOC | Navbar |
|----------|---------|---------|------|------------|---------|--------|
| <640px | 36px | 1列 | 16px | 48px | 隐藏 | 汉堡菜单 |
| 640-1023px | 72px | 2列 | 24px | 80px | 隐藏 | 汉堡菜单 |
| 1024-1439px | 72px | 4列 | 32px | 80px | 显示 | 水平链接 |
| ≥1440px | 72px | 4-5列 | 24px | 80px | 显示 | 水平链接 |

### 10.4 移动端 Navbar 抽屉动画

打开时的动画 timing：`transform .32s cubic-bezier(.16, 1, .3, 1)`

这是 `--ds-ease-out` 的值 — 开始时快速滑入，结尾减速。配合遮罩层 `opacity .3s` 的淡入，产生"从右侧滑入"的标准移动端导航体验。

---


## 11. JavaScript 逻辑详解

### 11.1 代码架构

`scripts.js` 由以下独立模块组成（全部为 IIFE 自执行函数）：

```
scripts.js
├── const ICONS = [...]              // 100个图标数据定义
├── const TOKENS = [...]             // 令牌键值对数组
├── IIFE: 图标网格渲染              // → #icon-grid
├── IIFE: 令牌表格渲染              // → #token-tbody
├── function toggleDarkMode()        // 暗色模式切换（全局函数）
├── IIFE: 暗色模式初始化            // 读取 localStorage/系统偏好
├── IIFE: Slider 同步               // range input ↔ value display
├── IIFE: Navbar 响应式切换          // 汉堡菜单开关
└── IIFE: 浮动目录生成与交互         // IntersectionObserver
```

### 11.2 图标渲染逻辑

```javascript
// 数据结构
const ICONS = [
  { id: "archive", svg: '<svg viewBox="0 0 24 24">...</svg>' },
  // ... 100个图标
];

// 渲染逻辑
var grid = document.getElementById("icon-grid");
ICONS.forEach(function(ic) {
  var box = document.createElement("div");
  box.className = "ds-icon-box";
  box.innerHTML = ic.svg + "<span>" + ic.id + "</span>";
  // 点击下载 SVG
  box.addEventListener("click", function() {
    var full = ic.svg.replace("<svg", '<svg xmlns="..." width="24" height="24"');
    var blob = new Blob([full], { type: "image/svg+xml" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url; a.download = ic.id + ".svg"; a.click();
    URL.revokeObjectURL(url);
  });
  grid.appendChild(box);
});
```

**关键点：**
- 图标 SVG 数据内嵌在 JS 中（不是外部文件请求）
- 点击图标触发 Blob 下载（无需服务器）
- 下载时补充 `xmlns` 和 `width/height` 属性确保 SVG 独立可用

### 11.3 令牌表格渲染

```javascript
const TOKENS = [
  ["--ds-color-bg", "oklch(97% 0.012 80)"],
  // ... 120+ 行
];

var tbody = document.getElementById("token-tbody");
TOKENS.forEach(function(t) {
  var tr = document.createElement("tr");
  tr.innerHTML = "<td>" + t[0] + "</td><td>" + t[1] + "</td>";
  tbody.appendChild(tr);
});
```

### 11.4 Slider 同步逻辑

```javascript
function syncSlider(slider) {
  var val = slider.value;                              // 当前值（0-100）
  var fill = slider.parentElement.querySelector(".ds-slider-fill");
  var valueSpan = document.getElementById(slider.dataset.valId);
  if (fill) fill.style.width = val + "%";              // 填充条宽度
  if (valueSpan) valueSpan.textContent = val + "%";    // 显示文字
}
```

**原理：** HTML range input 原生不支持自定义填充色，所以用一个 `div.ds-slider-fill` 叠加在轨道上方，宽度随 input 值动态设置。

### 11.5 Navbar 响应式逻辑

```javascript
// 打开/关闭抽屉
toggle.addEventListener("click", function() {
  var isOpen = menu.classList.contains("is-open");
  isOpen ? closeNav() : openNav();
});

// 点击遮罩层关闭
overlay.addEventListener("click", closeNav);

// ESC 键关闭
document.addEventListener("keydown", function(e) {
  if (e.key === "Escape") closeNav();
});

// 点击导航链接后关闭
links.forEach(function(link) {
  link.addEventListener("click", closeNav);
});

// 滚动阴影效果
window.addEventListener("scroll", function() {
  nav.classList.toggle("ds-navbar--scrolled", window.scrollY > 20);
}, { passive: true });
```

### 11.6 浮动目录（Floating TOC）

**生成阶段：**
1. 查找所有 `.ds-section[id]` 元素
2. 提取每个 section 的编号（`.ds-caption` 文字）和标题（`h2` 文字）
3. 动态创建 `<li><a>` 列表插入 `#floating-toc-list`

**高亮当前章节（IntersectionObserver）：**
```javascript
var obs = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      // 高亮对应的 TOC 链接
    }
  });
}, {
  threshold: 0.1,
  rootMargin: "-80px 0px -40% 0px"
  // -80px 顶部偏移（避开 navbar）
  // -40% 底部裁剪（section 进入视口 10% 即认为可见）
});
```

**显示/隐藏逻辑：** 当第一个 section 的底部还在视口内（页面在最顶部），TOC 隐藏；滚动过第一个 section 后显示。

---


## 12. 视觉效果层（Overlay / Glass / Blur）

### 12.1 遮罩层（Scrim/Overlay）

两种强度的遮罩：

| Token | 值 | 视觉效果 |
|-------|-----|----------|
| `--ds-color-overlay` | `oklch(0% 0 0 / 0.4)` | 40% 黑色遮罩，用于 Modal 背景 |
| `--ds-color-overlay-light` | `oklch(0% 0 0 / 0.12)` | 12% 黑色遮罩，轻微遮挡 |

### 12.2 毛玻璃效果（Glassmorphism）

```css
.ds-glass-card {
  background: var(--ds-glass-bg);           /* oklch(97% .012 80 / 55%) — 55%透明 */
  backdrop-filter: blur(var(--ds-blur-lg)); /* 24px 高斯模糊 */
  -webkit-backdrop-filter: blur(var(--ds-blur-lg));  /* Safari 兼容 */
  border: 1px solid var(--ds-glass-border); /* oklch(89% .012 80 / 25%) — 25%透明边框 */
  box-shadow: var(--ds-glass-shadow), var(--ds-shadow-md);  /* 双层阴影 */
}
```

**生效条件与视觉前提：**
1. 元素背景必须是半透明的（opacity < 100%）
2. 元素后方必须有内容（图片、渐变、文字）才能看到模糊效果
3. 本系统中，Glass 效果组件都放在 `.ds-glass-demo-bg` 容器内（带渐变背景）

### 12.3 模糊值等级

| Token | 值 | 用途 |
|-------|-----|------|
| `--ds-blur-sm` | 4px | 轻微模糊 |
| `--ds-blur-md` | 12px | 中等模糊（按钮、TOC） |
| `--ds-blur-lg` | 24px | 强模糊（Glass Card、Navbar） |
| `--ds-blur-xl` | 48px | 极强模糊（装饰用） |

### 12.4 装饰性元素

**角落 SVG 装饰（`.ds-edge-decor`）：**
- 固定在四角（`position: fixed`），120×120px
- 三层嵌套的 L 形路径，opacity 递减（100% / 50% / 25%）
- 通过 `transform: scaleX(-1)` / `scaleY(-1)` / `scale(-1)` 镜像到各角
- `pointer-events: none` 确保不干扰点击
- 暗色模式下 opacity 从 15% 降到 8%

**背景光晕（`.ds-bg-blob`）：**
- 两个大型圆形 div（400-500px），`position: fixed`
- `filter: blur(80px)` 产生柔和光晕
- `opacity: 0.06`（暗色模式 0.04）— 极微弱的背景色彩
- 一个在右上角（绿色），一个在左下角（浅绿色）

### 12.5 Frosted Navigation（毛玻璃导航栏）

```css
.ds-frosted-nav {
  display: inline-flex;
  padding: 12px 24px;
  border-radius: 16px;                          /* 胶囊形 */
  background: var(--ds-glass-bg);               /* 55% 透明 */
  backdrop-filter: blur(24px);
  border: 1px solid var(--ds-glass-border);     /* 25% 透明边框 */
}
```

### 12.6 Toast 通知

毛玻璃风格的通知条，三种语义变体：
- 默认（绿色图标）
- `--success`（绿色图标）
- `--error`（红色图标）
- `--warning`（黄色图标）

每个 Toast 包含：图标(18px) + 文字 + 关闭按钮(✕)

---


## 13. 修改代码时的陷阱与注意事项

### 13.1 "我改了颜色但看不到变化"

**可能原因：**
1. 暗色模式有独立覆盖 — 你改了 `:root` 但暗色模式下是 `[data-theme="dark"]` 的值
2. 组件使用的是语义变量而非原始变量 — 如修改 `--ds-color-olive-400` 但组件用的是 `--ds-accent`（虽然这里它们相等）
3. OKLch 中微小的彩度/色相变化在低饱和度下不可见

### 13.2 "我改了 padding 但元素没变大"

**可能原因：**
1. `box-sizing: border-box` — padding 包含在已设定的 width/height 内
2. `max-width` 限制 — 元素已达到最大宽度，padding 只压缩内容空间
3. Flexbox/Grid 子元素的 `min-width: 0` 或 `overflow` 可能吞掉空间

### 13.3 "我加了 z-index 但元素还是被遮盖"

**本系统的层叠顺序：**
```
z-index: 500  → Toast 通知
z-index: 400  → Modal 模态框
z-index: 300  → Overlay 遮罩
z-index: 200  → Sticky Navbar
z-index: 100  → Dropdown/浮动TOC
z-index: 1    → 普通元素
z-index: 0    → 装饰元素（blob、edge-decor）
```

**关键点：** `backdrop-filter` 会创建新的层叠上下文，子元素的 z-index 只在该上下文内有效。

### 13.4 "我改了 font-family 但字体没变"

**可能原因：**
1. 字体未安装 — 本系统不引入 Google Fonts，依赖系统预装字体
2. font-stack fallback — 如果首选字体不可用，浏览器按顺序尝试后续字体
3. CJK 字符与 Latin 可能使用不同的 fallback 字体
4. 某些组件有自己的 `font-family` 声明覆盖全局值

### 13.5 "暗色模式下颜色对比度不够"

**设计原则：**
- 暗色模式不是简单反转亮度值
- 文字在暗底上需要 **更低** 的亮度值差才能保持同样的对比度感知
- 橄榄绿在暗底上需要亮化 5-10%（olive-400 从 52% 提到 57%）

### 13.6 "backdrop-filter 在某些浏览器不生效"

- Firefox 较新版本已支持，但需确认
- Safari 需要 `-webkit-backdrop-filter` 前缀（本系统已添加）
- 如果不生效，元素会退化为纯半透明背景（无模糊），设计上可接受

### 13.7 "scroll-behavior: smooth 跳转位置偏移"

```css
html { scroll-padding-top: 72px; }
```

这确保锚点跳转时，目标位置距离视口顶部有 72px 间距（刚好是 Navbar 高度 64px + 8px 余量）。如果修改了 Navbar 高度，必须同步修改此值。

### 13.8 "修改了 transition 但动画不自然"

本系统使用的缓动函数：

| 函数 | 曲线 | 感觉 |
|------|------|------|
| `--ds-ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | 快速开始 → 慢慢停止（最常用） |
| `--ds-ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | 慢慢开始 → 快速结束（退出动画） |
| `--ds-ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` | 对称缓动 |
| `--ds-ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | 弹性感（过冲后回弹） |

**法则：** 进入动画用 ease-out，退出动画用 ease-in，循环动画用 ease-in-out。

---


## 14. 命名约定与扩展规则

### 14.1 CSS 变量命名

```
--ds-{category}-{name}[-{modifier}]

分类前缀：
  color    → 颜色
  font     → 字体族
  text     → 字号
  weight   → 字重
  leading  → 行高
  tracking → 字距
  space    → 间距
  radius   → 圆角
  shadow   → 阴影
  duration → 动画时长
  ease     → 缓动函数
  bp       → 断点
  z        → z-index
  blur     → 模糊值
  glass    → 玻璃效果
```

### 14.2 CSS 类名命名

```
.ds-{component}           → 组件基础类
.ds-{component}--{variant} → 变体修饰符
.ds-{component}-{element}  → 子元素

已有组件列表：
btn, card, input, select, checkbox, radio, toggle,
badge, chip, alert, modal, tooltip, accordion, tabs,
progress, avatar, breadcrumb, table, pagination,
nav, dropdown, icon-btn, skeleton, slider, date,
timeline, contact-form, toast, glass-card, glass-btn
```

### 14.3 添加新组件的步骤

1. **在 `styles.css` 中添加组件样式：**
   ```css
   /* ===== ComponentName ===== */
   .ds-component { /* 基础样式 */ }
   .ds-component--variant { /* 变体 */ }
   .ds-component-child { /* 子元素 */ }
   ```

2. **在 `index.html` 的 `#components` section 中添加预览：**
   ```html
   <div class="ds-component-group">
     <div class="ds-component-label">编号 · Component Name</div>
     <div class="ds-component-preview">
       <!-- 组件 HTML -->
     </div>
   </div>
   ```

3. **确保暗色模式兼容：**
   - 所有颜色使用 `var(--ds-color-*)` 令牌
   - 如需特殊暗色处理，在 `[data-theme="dark"]` 中添加覆盖

4. **确保响应式兼容：**
   - 在 `@media (max-width: 639px)` 中测试

### 14.4 添加新令牌的步骤

1. 在 `:root { }` 中定义新变量
2. 在 `[data-theme="dark"]` 中定义暗色值
3. 在 `scripts.js` 的 `TOKENS` 数组中添加条目（用于渲染令牌表）
4. 在 `tokens.json` 中添加结构化数据

### 14.5 图标扩展

在 `scripts.js` 的 `ICONS` 数组中添加新条目：
```javascript
{ id: "new-icon", svg: '<svg viewBox="0 0 24 24">...</svg>' }
```

**图标规范：**
- viewBox: `0 0 24 24`
- stroke-width: 1.5（由 CSS `.ds-icon-box svg { stroke-width: 1.5 }` 统一设定）
- fill: none
- 风格：Lucide / Feather 线性图标

---


## 15. 性能与可访问性

### 15.1 性能特征

| 指标 | 值 | 说明 |
|------|-----|------|
| HTML 大小 | ~35KB | 单文件，无外部 HTML 请求 |
| CSS 大小 | ~33KB | 单文件，无 @import |
| JS 大小 | ~16KB | 单文件，无外部库 |
| 总请求数 | 3 | HTML + CSS + JS |
| 外部字体 | 0 | 完全依赖系统字体 |
| 图片 | 0 | 所有图标为内联 SVG |

**优化措施：**
- 零外部依赖 = 无 CDN 单点故障
- 系统字体栈 = 零字体加载延迟
- 内联 SVG = 无额外图片请求
- `scroll` 事件使用 `{ passive: true }` = 不阻塞滚动

### 15.2 可访问性（Accessibility）

**已实现：**
- 语义化 HTML：`<nav>`, `<section>`, `<footer>`
- ARIA 标签：`aria-label="主导航"`, `aria-label="切换暗色/浅色模式"`
- `aria-expanded` 在 Navbar toggle 上动态更新
- 键盘可访问：ESC 关闭导航
- 色彩对比度：fg-strong(14%) on bg(97%) → 对比度 > 7:1
- `role="navigation"` 在导航元素上

**注意事项：**
- 部分组件使用 `onclick` 内联事件 — 不影响功能但不是最佳实践
- Tab 组件的键盘导航未完整实现（无 arrow key 支持）
- Accordion 使用 `onclick` 而非 `<button>` — 屏幕阅读器可能不识别为可交互

### 15.3 打印样式

```css
@media print {
  .ds-navbar, .ds-floating-toc, .ds-edge-decor,
  .ds-bg-blob, #theme-toggle { display: none !important; }
  .ds-section { break-inside: avoid; padding: var(--ds-space-12) 0; }
}
```

打印时隐藏所有固定定位的装饰/导航元素，section 不跨页分割。

### 15.4 自定义滚动条

```css
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-thumb {
  background: var(--ds-color-border);
  border-radius: 9999px;
  border: 2px solid transparent;
  background-clip: content-box;     /* 产生"内缩"效果 */
}
* { scrollbar-width: thin; scrollbar-color: var(--ds-color-border) transparent; }
```

滚动条在暗色模式下自动跟随令牌颜色变化。

---

## 附录 A：完整组件清单快速参考

| # | 组件 | 类名 | 变体 |
|---|------|------|------|
| 01 | Button | `.ds-btn` | `--primary`, `--secondary`, `--ghost`, `--sm`, `--lg` |
| 02 | Card | `.ds-card` | `--hoverable`, `--flat` |
| 03 | Text Input | `.ds-input` | `--error` |
| 04 | Select | `.ds-select` | — |
| 05 | Checkbox | `.ds-checkbox` | — |
| 06 | Radio | `.ds-radio` | — |
| 07 | Toggle | `.ds-toggle` | — |
| 08 | Badge | `.ds-badge` | `--default`, `--accent`, `--success`, `--warning`, `--error` |
| 09 | Chip | `.ds-chip` | `--active` |
| 10 | Alert | `.ds-alert` | `--info`, `--success`, `--warning`, `--error` |
| 11 | Modal | `.ds-modal` | — |
| 12 | Tooltip | `.ds-tooltip-demo` | — |
| 13 | Accordion | `.ds-accordion` | — |
| 14 | Tabs | `.ds-tabs` / `.ds-tab` | `--active` |
| 15 | Progress | `.ds-progress` | — |
| 16 | Avatar | `.ds-avatar` | `--sm`, `--lg` |
| 17 | Breadcrumb | `.ds-breadcrumb` | — |
| 18 | Pagination | `.ds-pagination` / `.ds-page-btn` | `--active` |
| 19 | Table | `.ds-table` | — |
| 20 | Navigation | `.ds-nav` / `.ds-nav-item` | `--active` |
| 21 | Dropdown | `.ds-dropdown` | — |
| 22 | Skeleton | `.ds-skeleton` | — |
| 23 | Icon Button | `.ds-icon-btn` | — |
| 24 | Slider | `.ds-slider` | — |
| 25 | Date Picker | `.ds-date-*` / `.ds-cal-*` | — |
| 26 | Timeline | `.ds-timeline` | — |
| 27 | Contact Form | `.ds-contact-form` / `.ds-form-*` | — |
| 28 | Toast | `.ds-toast` | `--success`, `--error`, `--warning` |
| 29 | Glass Card | `.ds-glass-card` | `--sm`, `--lg` |
| 30 | Glass Button | `.ds-glass-btn` | — |
| 31 | Frosted Nav | `.ds-frosted-nav` | — |
| 32 | Article TOC | `.ds-toc-article` | — |
| 33 | Divider | `.ds-divider` | — |
| 34 | Empty State | `.ds-empty-state` | — |
| 35 | Accordion (code) | `.ds-accordion--code` | — |
| 36 | Chart | `.ds-chart` / `.ds-chart-*` | `--bar`, `--line`, `--area`, `--pie`, `--donut`, `--horizontal`, `--stacked`, `--sparkline` |

---

## 附录 B：关键 CSS 选择器与其视觉作用

| 选择器 | 作用 | 视觉位置 |
|--------|------|----------|
| `.ds-navbar` | 顶部导航栏 | 固定在视口顶部，高64px |
| `.ds-floating-toc` | 右侧浮动目录 | fixed, 垂直居中, right:24px |
| `.ds-cover` | 封面英雄区 | padding-top:128px, 文字居中 |
| `.ds-wrapper` | 内容容器 | 最大宽1200px, 水平居中 |
| `.ds-section` | 章节容器 | 上下padding 80px, 底部1px分隔线 |
| `.ds-section-header` | 章节头部 | max-width:600px, 底部margin 48px |
| `#theme-toggle` | 主题切换按钮 | fixed, bottom:24px, right:24px |
| `.ds-edge-decor--tl` | 左上角装饰 | fixed, top:0, left:0 |
| `.ds-edge-decor--br` | 右下角装饰 | fixed, bottom:0, right:0 |
| `.ds-bg-blob--1` | 右上背景光晕 | fixed, top:-150px, right:-100px |
| `.ds-bg-blob--2` | 左下背景光晕 | fixed, bottom:-100px, left:-80px |
| `.ds-footer` | 页脚 | padding:48px, 居中文字, 顶部1px线 |

---

## 附录 C：tokens.json 数据结构

`tokens.json` 采用 **flat 结构**（扁平化），键名直接对应 CSS `--ds-*` 变量后缀，用 `--ds-` 前缀连接。
示例：`"color-bg"` → `--ds-color-bg`，`"color-olive-400"` → `--ds-color-olive-400`。
暗色模式 token 使用 `-dark` 后缀，映射到 `[data-theme="dark"]` 中的对应变量。

```json
{
  "name": "EDIC Design Tokens",
  "version": "1.9.1",
  "description": "Editorial × Olive Green design system tokens",
  "tokens": {
    "color-bg": "oklch(97% 0.012 80)",
    "color-surface": "oklch(99% 0.005 80)",
    "color-olive-400": "oklch(52% 0.08 115)",
    "color-success": "oklch(55% 0.1 145)",
    "color-error": "oklch(50% 0.14 30)",
    "color-warning": "oklch(65% 0.1 85)",
    "color-info": "oklch(55% 0.08 240)",
    "color-bg-dark": "oklch(15% 0.008 75)",
    "color-fg-dark": "oklch(84% 0.008 72)",
    "text-caption": "0.75rem",
    "text-body": "1rem",
    "text-hero": "4.5rem",
    "space-4": "1rem",
    "space-16": "4rem",
    "radius-md": "4px",
    "radius-xl": "12px",
    "shadow-sm": "0 1px 3px oklch(0% 0 0 / 6%)",
    "shadow-lg": "0 10px 15px oklch(0% 0 0 / 8%)",
    "duration-150": "150ms",
    "ease-out": "cubic-bezier(.16, 1, .3, 1)"
  }
}
```

> ⚠️ 此文件的 **ground truth 是 `styles.css`**（`styles.css` 是源，`tokens.json` 是从 `styles.css` 导出的结构化快照）。
> 修改 token 时，先改 `styles.css` `:root` 和 `[data-theme="dark"]`，再同步更新 `tokens.json`。

---

## 附录 D：常见修改场景快速指引

### D.1 更换强调色

1. 修改 `:root` 中 `--ds-color-olive-*` 全部 10 级色阶
2. 修改 `[data-theme="dark"]` 中对应的暗色值
3. `--ds-accent` 等语义映射无需改（它们引用 olive-400）

### D.2 更换字体

1. 修改 `--ds-font-display` / `--ds-font-body` 等变量的值
2. 如引入 Web Font，在 HTML `<head>` 中添加 `<link>` 或 `@font-face`

### D.3 调整全局间距感

- 增大所有间距：修改各 `--ds-space-*` 值（按比例放大）
- 或只修改 `html { font-size }` 基准值（所有 rem 值随之缩放）

### D.4 添加新页面

1. 创建新 HTML 文件
2. `<link rel="stylesheet" href="styles.css">` 引入样式
3. 使用 `.ds-wrapper` + `.ds-section` + 组件类组装页面
4. 如需交互，引入 `<script src="scripts.js">`

### D.5 修改 Navbar 链接

在 `index.html` 中找到 `.ds-navbar-links` 容器，修改其中的 `<a class="ds-navbar-link">` 元素。

---

*本文档基于项目源代码 v1.9.1 自动生成，如代码有更新请同步维护本指南。*
