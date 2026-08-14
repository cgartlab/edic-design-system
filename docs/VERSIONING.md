# 版本控制策略（Versioning Strategy）

> 本项目采用**语义化版本 2.0.0**（[SemVer](https://semver.org/lang/zh-CN/)）作为基础，
> 并针对**设计系统**特性做了适配。

## 版本号格式

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

| 段 | 含义 | 设计系统适配 |
|----|------|---------------|
| **MAJOR** | 破坏性变更 | 删除/重命名组件、令牌重构、视觉风格大改 |
| **MINOR** | 向后兼容的新功能 | 新增组件、新增令牌档位、新增示例页、动效系统升级 |
| **PATCH** | 向后兼容的修复 | 暗色模式对比度调整、bug 修复、文档修正 |
| **PRERELEASE** | 预发布标识 | `alpha.N` / `beta.N` / `rc.N` |
| **BUILD** | 构建元数据 | 内部 CI 编号（不发布到 tag） |

## 何时递增？

### MAJOR（破坏性变更）

✅ 触发条件（**任意一项**）：

- 删除或重命名**公共**组件（`ds-btn` → `ds-button`）
- 删除或重命名**公共**令牌（`--ds-color-olive-400` → `--ds-color-accent-400`）
- 改变基础设计语言（更换强调色系、改变排版基础）
- 暗色模式下基础对比度变化导致现有页面需重新调整
- HTTP 资源路径变化（如 CDN 域名切换）

❌ 不触发 MAJOR：

- 新增组件/令牌（向后兼容）
- 暗色模式微调（保持对比度 ≥ WCAG AA）
- 文档/示例更新
- 内部代码重构（不影响公共 API）

### MINOR（新功能）

✅ 触发条件：

- 新增一个或多个组件
- 新增一组令牌（如新增 `--ds-color-blue-*` 蓝色阶）
- 新增图标（不删除现有）
- 新增示例页
- 新增动效关键帧或工具类
- 引入新的开发工具（如 `tools/validate_*`）

### PATCH（修复）

✅ 触发条件：

- 修复组件 bug（如 Slider 在 0% 时的渲染问题）
- 暗色模式颜色微调
- 浏览器兼容性问题修复
- 文档错别字、链接失效
- 性能优化（不改变行为）

## 预发布版本

用于正式发布前的内部测试：

| 标识 | 含义 | 用途 |
|------|------|------|
| `1.2.0-alpha.1` | 内部 Alpha | 维护者自测，不邀请外部 |
| `1.2.0-beta.1` | 公开 Beta | 邀请社区试用，开放反馈 |
| `1.2.0-rc.1` | 发布候选 | 锁定功能，仅修 bug |

## 资源版本号同步

由于本项目无构建工具，浏览器/CDN 通过 `?v=` 查询字符串刷新资源缓存：

```html
<link rel="stylesheet" href="styles.css?v=1.10.1">
<script src="scripts.js?v=1.10.1"></script>
```

**规则**：

1. **MAJOR / MINOR bump** → 同步更新所有 HTML 的 `?v=`
2. **PATCH bump** → 必须同步更新所有 HTML 的 `?v=`
3. 自动化校验：`python3 tools/validate_versions.py` 会扫描所有 HTML，
   校验 `?v=` 是否与 `package.json` / `CHANGELOG.md` 中最新版本号一致

> 注意：当前项目没有 `package.json`，版本源在专门的 `VERSION` 单行文件（无构建步骤，GitHub Pages 直接部署静态文件）。

### stamp 工具（自动化同步）

为消除"改 VERSION → 改 6 个 HTML → 改 README → 改 AGENTS"的繁琐手动流程，
项目提供 `tools/stamp_version.py`：

| 场景 | 命令 |
|------|------|
| 修改 VERSION 后同步全部资源 | `python3 tools/stamp_version.py` |
| CI / pre-commit 检查是否已 stamp | `python3 tools/stamp_version.py --check` |
| 预览 diff | `python3 tools/stamp_version.py --diff` |
| 反向还原（开发期） | `python3 tools/stamp_version.py --restore` |

源码中所有需要跟随 VERSION 同步的位置都使用 `DS_VERSION` 占位符（由双花括号包裹），
stamp 工具会一次性替换为 VERSION 中的真实版本号（无构建步骤，GitHub Pages 仍可直接部署静态文件）。

> 占位符使用 `DS_` 前缀（Design System）以避免与文档中说明占位符语法的示例
> （如 `{{VERSION}}`、`{{TOKEN}}` 等通用写法）发生冲突。

**触发方式**：
- pre-commit hook：改 HTML/CSS/JS 时自动 stamp
- Release workflow：打 tag 前手动 `make stamp-version`

**典型发布流程**（release-please 自动 tag 模型）：

```
Feature PR merge → main
    ↓
release-please 分析 Conventional Commits → 创建/更新 Release PR
    ↓
人类审查 Release PR（直接编辑 CHANGELOG.md 对应版本节润色措辞）
    ↓
合并 Release PR
    ↓
release-please 自动：
  ① 更新 VERSION / .release-please-manifest.json / tokens.json / package.json
  ② 创建 git tag vX.Y.Z（GitHub 后台签名，无需本地 GPG）
  ③ 创建 GitHub Release（notes 取自 CHANGELOG.md）
    ↓
release.yml（release: published 事件）→ 构建 PDF/ZIP/CHECKSUMS → 上传资产
    ↓
post-merge-stamp 自动：
  ① stamp_version.py（同步 ?v= 缓存戳）
  ② generate_changelog_html.py（从 CHANGELOG.md 重建网站变更页）
```

## 分支与版本对应

| 分支 | 用途 | tag 前缀 |
|------|------|----------|
| `main` | 稳定发布 | `vX.Y.Z` |
| `dev-xxx` | 新功能开发 | 无（合并后通过 release 分支打 tag） |
| `fix-xxx` | 修复 | 无 |
| `release/x.y.z` | 发布准备（可选） | `vX.Y.Z` |

（分支规范见 `docs/BRANCH-WORKFLOW.md`，如需可自行创建。）

## 提交信息与版本联动

Conventional Commits 的类型映射到版本：

| 提交类型 | 影响版本 | 示例 |
|----------|----------|------|
| `feat` | MINOR | `feat(component): 新增 ds-tabs 键盘导航` |
| `fix` | PATCH | `fix(token): 暗色模式对比度调整` |
| `feat!` / `BREAKING CHANGE:` | MAJOR | `feat(component)!: 重命名 ds-button → ds-btn` |
| `docs` / `style` / `chore` | 不发版（除非累积） | — |

release-please / semantic-release 风格的自动化可在未来引入（见 [未来工作](#未来工作)）。

## 当前版本

- **最新稳定版**：`v1.10.1`（2026-08-14）
- **VERSION 文件**：项目根目录 `VERSION` 单行文件存放当前版本号

## 自动化发布（Release Please）

项目已集成 [release-please](https://github.com/googleapis/release-please) 自动化发布流程。

### 发布策略：release-please 自动 tag + GitHub Release

`release-please`（`skip-github-release: false`）自动完成 Release PR、CHANGELOG、
版本号同步、tag 创建与 GitHub Release。
Release PR 合并后，release-please 自动创建 tag 和 GitHub Release，`release: published`
事件触发 `release.yml` 构建资产并上传至已创建的 GitHub Release。

这样设计的好处：
- 避免"一合并就发布"绕过人类审查（Release PR 仍需人工 Review）
- release-please 在 PR 合并后自动创建 tag 和 GitHub Release，减少人工操作环节
- 人类在发布前仍可编辑 Release PR 的 CHANGELOG 措辞，发布后通过 `workflow_dispatch` 可做紧急热修复

### 触发方式

| 方式 | 说明 |
|------|------|
| **自动（创建 Release PR）** | push to `main` → release-please 分析 commits → 创建/更新 Release PR |
| **合并 Release PR** | 合并后 release-please 自动创建 tag + GitHub Release（notes 取自 CHANGELOG） |
| **workflow_dispatch** | 手动触发 release-please.yml，可强制版本号（release-as）；紧急热修复时手动触发 release.yml（见 [AGENTS.md](../../AGENTS.md)） |
| **紧急热修复** | 自动链路不可用时，通过 `workflow_dispatch` 手动触发 `release.yml`，指定 `version` 参数 |

### 完整发布流程

```
提交（Conventional Commits）
  → release-please 分析
  → 创建/更新 Release PR（CHANGELOG.md + .release-please-manifest.json + tokens.json + package.json）
  → 人类审查 Release PR（如需润色措辞，直接编辑 CHANGELOG.md 对应节）
  → 合并 Release PR
  → release-please 自动：
      ① 更新 .release-please-manifest.json / tokens.json / package.json（extra-files）
      ② 创建 git tag vX.Y.Z（GitHub 后台签名）
      ③ 创建 GitHub Release（notes 取自 CHANGELOG.md）
      ④ post-merge-stamp：从 release-please 的 `version` output 同步 `VERSION` 文件
  → release.yml（release: published 事件触发）：
      构建 PDF/ZIP/CHECKSUMS → 上传至已创建的 GitHub Release
  → post-merge-stamp 自动（检测 release_created output）：
      ① stamp_version.py（同步 ?v= 缓存戳）
      ② generate_changelog_html.py（从 CHANGELOG.md 重建网站变更页）
```

### Release PR 包含的内容

Release PR 包含：
- `CHANGELOG.md` 更新（基于 Conventional Commits 自动分类，中文章节）—— **变更日志唯一来源**
- `VERSION`、`tokens.json`、`package.json` 版本同步

> 网站变更页（changelog.html）与 GitHub Release notes **都从 `CHANGELOG.md` 生成**，无需单独维护人类摘要文件。`validate_release_notes.py` 会校验 `CHANGELOG.md` 含该版本节。

### 版本同步

Release PR 合并后，`post-merge-stamp` 自动（检测 `release_created` output）：
1. 运行 `stamp_version.py` 同步所有 HTML/MD 中的 `?v=` 缓存 busting 参数
2. 运行 `generate_changelog_html.py` 从 `CHANGELOG.md` 单源重建网站变更页

完整流程见 [docs/RELEASE-CHECKLIST.md](./RELEASE-CHECKLIST.md)。

## 未来工作

- [x] ~~引入 release-please 自动化~~（已实施）
- [ ] 引入 Changesets（多组件包场景）
- [ ] npm 发布为可选（如果未来需要 programmatic API）
- [ ] 语义化令牌演进（`@deprecated` 标记、迁移指南）

---

*本文档是 [docs/RELEASE-CHECKLIST.md](./RELEASE-CHECKLIST.md) 的前置阅读。*
