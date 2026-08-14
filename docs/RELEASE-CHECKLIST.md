# 发布检查清单（Release Checklist）

> 在打 tag 之前必须完成的所有事项。本清单是 [VERSIONING.md](./VERSIONING.md) 的执行细节。

---

## 发布策略概览

```
普通 PR merge → main
    ↓
release-please（skip-github-release: false）分析 Conventional Commits
    ↓
创建/更新 Release PR（自动 CHANGELOG + 版本 bump）
    ↓
人类审查 Release PR 内容 → 合并
    ↓
release-please 自动：
  ① 创建 git tag vX.Y.Z（GitHub 后台签名）
  ② 创建 GitHub Release（notes 取自 CHANGELOG）
    ↓
release.yml（release: published 事件）触发 → 构建 PDF/ZIP/CHECKSUMS → 上传资产
    ↓
post-merge-stamp（检测 release_created output）自动：
  ① stamp_version.py（同步 ?v= 缓存戳）
  ② generate_changelog_html.py（重建网站变更页）
```

**关键原则：** `release-please` 负责 Release PR、CHANGELOG、tag 创建与 GitHub Release 全链路自动化。
无需人类手动执行 `git tag`。`release.yml` 由 `release: published` 事件触发。
`post-merge-stamp` 由 `release_created` output 触发。紧急热修复通过 `workflow_dispatch` 手动触发 `release.yml`。

---

## 准备阶段（T-7 天）

- [ ] 确认所有 `dev-xxx` 分支已合并或关闭
- [ ] 确认所有阻塞性 issue 已解决
- [ ] 创建 `release/x.y.z` 分支（如需冻结代码）
- [ ] 通知贡献者：「即将发布，请检查是否有未提交的 PR」
- [ ] 检查外部依赖（GitHub Pages、CNAME 解析）是否健康

---

## 测试阶段（T-3 天）

- [ ] 本地运行 `make validate` 全部通过
- [ ] 浏览器实测：
  - [ ] Chrome / Edge（最新）
  - [ ] Firefox（最新）
  - [ ] Safari（macOS / iOS）
  - [ ] 移动端 Chrome（Android）
- [ ] 多视口验证：375 / 768 / 1024 / 1440 / 1920
- [ ] 浅色 + 暗色模式都验证
- [ ] 键盘可达性测试（Tab / Enter / Esc / 方向键）
- [ ] 屏幕阅读器测试（NVDA / VoiceOver）
- [ ] 离线模式（断网测试静态资源是否齐全）

---

## 文档阶段（T-1 天）

- [ ] 检查 `CHANGELOG.md` 是否包含完整的版本条目（由 release-please 自动填入，是变更日志唯一来源）
  - 如需润色措辞，直接编辑 `CHANGELOG.md` 对应版本节即可（changelog.html 会从中重建）
- [ ] 运行 `make changelog` 预览 changelog.html 将如何更新
- [ ] 检查 `README.md` 截图与示例是否需要更新
- [ ] 检查 `AGENTS.md` 组件清单是否需要更新
- [ ] 检查 `docs.html` 预览是否完整

---

## 代码阶段（发布当天：Release PR 已合并时）

> release-please 会自动创建 Release PR 更新 VERSION / CHANGELOG.md。
> 合并后 release-please 自动创建 tag 和 GitHub Release，触发 release.yml 构建资产。
> post-merge-stamp 在 release_created output 触发后自动同步 ?v= 缓存戳。

- [ ] 确认 Release PR 已合并
- [ ] 确认 release-please 已自动创建 tag `vX.Y.Z`（GitHub 页面 → Tags）
- [ ] 确认 GitHub Release 已创建（notes 取自 CHANGELOG.md）
- [ ] 确认 `release.yml`（Release Pipeline）构建成功，资产已上传
- [ ] 确认 `post-merge-stamp` job 成功（Actions → 最新 Release Please 运行）
- [ ] 验证 main 上的 VERSION 已更新为新版本号
- [ ] 验证 changelog.html 已包含新版本的内容（本地 `make changelog-check`）
- [ ] 运行 `make validate` 全部通过
- [ ] 确认 `CHANGELOG.md` 含该版本节（`validate_release_notes.py` 会校验）

---

## 发布阶段（验证 release-please 自动 tag + GitHub Release）

Release PR 合并后，release-please 自动创建 tag 和 GitHub Release。
人工任务只是验证和确认：

```bash
# 1. 确认 release-please 已自动创建 tag
#    GitHub → Tags → 查找 vX.Y.Z（或 gh api 检查）
gh api repos/cgartlab/edic-design-system/git/ref/tags/vX.Y.Z --jq '.ref'

# 2. 确认 GitHub Release 已创建（notes 取自 CHANGELOG.md）
gh release view vX.Y.Z

# 3. 确认 release.yml 构建资产成功（Actions → Release Pipeline）
gh run list --workflow release.yml
```

- [ ] post-merge-stamp job 成功（VERSION 已更新、changelog.html 已重建）
- [ ] tag 已自动创建：`refs/tags/vX.Y.Z`（GitHub Tags 页面或 gh api 确认）
- [ ] GitHub Release 页面存在，标题无 "Draft" 标记
- [ ] GitHub Actions → Release Pipeline 运行成功（release: published 事件触发）
- [ ] 所有资产 URL 不包含 `untagged-`（防止 v1.8.1 事故重现）
- [ ] 资产文件齐全：PDF + ZIP + CHECKSUMS.txt
- [ ] 验证 GitHub Pages 自动部署成功（Settings → Pages → 部署历史）
- [ ] 访问 https://edic.cgartlab.com 确认正常

---

## 发布后（T+1 天）

- [ ] 监控 issue 区是否有 release 相关问题
- [ ] 如有 hotfix：创建 `hotfix/x.y.z` 分支，修复合并后通过 `workflow_dispatch` 触发 `release.yml` 发布
- [ ] 关闭 milestone（如使用 GitHub Milestones）
- [ ] 团队庆祝 🎉

---

## 紧急回滚

如果发布后发现严重问题：

```bash
# 1. 在 GitHub UI 中删除或标记该 Release 为 pre-release
#    （tag 和 Release 均由 GitHub 自动管理，无需本地 git 操作）

# 2. 恢复 main 到上一个稳定 tag
git checkout main
git reset --hard vX.Y.Z-1
git push --force-with-lease

# 3. 修复 → hotfix 分支 → 提交 → PR → merge
git checkout -b hotfix/vX.Y.Z
# ... 修复 ...

# 4. 手动触发 release.yml 发布（workflow_dispatch）
gh workflow run release.yml -f version=X.Y.Z+1
```

> ⚠️ `--force-with-lease` 比 `--force` 安全，会检测上游是否被改过。

---

## 版本号速查

当前版本见 `VERSION` 文件。

| 类型 | 例 | 何时 |
|------|----|------|
| 下一个 MAJOR | `2.0.0` | 删除组件 / 令牌重构 / 设计语言变化 |
| 下一个 MINOR | `1.2.0` | 新增组件 / 新增令牌 / 新增示例 |
| 下一个 PATCH | `1.1.1` | 修复 / 暗色微调 / 文档修正 |
| 预发布 | `1.2.0-beta.1` | 公开测试 |

---

*执行模板：可复制此清单到对应 GitHub Issue，命名为 `Release vX.Y.Z`，逐项勾选。*
