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
<link rel="stylesheet" href="styles.css?v=1.8.1">
<script src="scripts.js?v=1.8.1"></script>
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

**典型发布流程**：

```bash
# 1. 改 VERSION（单行文本）
echo "1.5.5" > VERSION

# 2. 自动同步所有文件
make stamp-version

# 3. 验证
make validate-versions

# 4. 提交
git add -A && git commit -m "chore(release): bump to v1.8.1"

# 5. 打 tag
git tag v1.8.1 && git push origin v1.8.1
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

- **最新稳定版**：`v1.8.1`（2026-06-08）
- **VERSION 文件**：项目根目录 `VERSION` 单行文件存放当前版本号

## 自动化发布（Release Please）

项目已集成 [release-please](https://github.com/googleapis/release-please) 自动化发布流程。

### 发布策略：手工 tag 触发正式发布

`release-please` **只负责** Release PR 和 CHANGELOG，**不会**自动打 tag，**不会**自动触发 release 流水线。
只有人类明确执行 `git tag vX.Y.Z && git push origin vX.Y.Z` 之后，`release.yml` 才会触发。

这样设计的原因：
- 避免"一合并就发布"的自动链路绕过人类审查
- 人类可以在 Release PR 合并后、发布前做最终验收
- 版本发布时机完全由人类决定（比如避开周五下午）

### 触发方式

| 方式 | 说明 |
|------|------|
| **自动（创建 Release PR）** | push to `main` → release-please 分析 commits → 创建/更新 Release PR |
| **合并 Release PR** | 合并后 post-merge-stamp 自动同步 ?v= 和 changelog.html |
| **手动发布（打 tag）** | `git tag vX.Y.Z && git push origin vX.Y.Z` → 触发 release.yml |
| **强制版本** | `workflow_dispatch` + `release-as` 输入 → 强制指定版本号 |
| **预发布** | `workflow_dispatch` + `prerelease=true` → 标记为预发布 |

### 完整发布流程

```
提交（Conventional Commits）
  → release-please 分析
  → 创建/更新 Release PR（CHANGELOG + 版本 bump）
  → 人类在 Release PR 中添加 docs/changelog_human/vX.Y.Z.md
  → 合并 Release PR
  → post-merge-stamp 自动：
      ① stamp_version.py（同步 ?v= 缓存戳）
      ② generate_changelog_html.py（重建网站变更页）
  ↓
  人类决定发布时机：
  git tag vX.Y.Z && git push origin vX.Y.Z
  → release.yml 触发
  → 构建 PDF/ZIP 资产 + GitHub Release
```

### Release PR 包含的内容

Release PR 包含：
- `CHANGELOG.md` 更新（基于 Conventional Commits 自动分类，中文章节）
- `VERSION`、`tokens.json`、`package.json` 版本同步

> 人类需要在合并前额外添加：`docs/changelog_human/vX.Y.Z.md`（人类友好的版本说明，CI 会检查）

### 版本同步

Release PR 合并后，`post-merge-stamp` 会自动：
1. 运行 `stamp_version.py` 同步所有 HTML/MD 中的 `?v=` 缓存 busting 参数
2. 运行 `generate_changelog_html.py` 从 `docs/changelog_human/` 重建网站变更页

完整流程见 [docs/RELEASE-CHECKLIST.md](./RELEASE-CHECKLIST.md)。

## 未来工作

- [x] ~~引入 release-please 自动化~~（已实施）
- [ ] 引入 Changesets（多组件包场景）
- [ ] npm 发布为可选（如果未来需要 programmatic API）
- [ ] 语义化令牌演进（`@deprecated` 标记、迁移指南）

---

*本文档是 [docs/RELEASE-CHECKLIST.md](./RELEASE-CHECKLIST.md) 的前置阅读。*
