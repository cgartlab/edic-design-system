# 发布检查清单（Release Checklist）

> 在打 tag 之前必须完成的所有事项。本清单是 [VERSIONING.md](./VERSIONING.md) 的执行细节。

---

## 发布策略概览

```
普通 PR merge → main
    ↓
release-please 分析 Conventional Commits
    ↓
创建/更新 Release PR（自动 CHANGELOG + 版本 bump）
    ↓
人类审查 Release PR 内容 → 合并
    ↓
post-merge-stamp 自动：
  ① stamp_version.py（同步 ?v= 缓存戳）
  ② generate_changelog_html.py（重建网站变更页）
    ↓
人类决定发布时机，手动执行：
  git tag vX.Y.Z && git push origin vX.Y.Z
    ↓
release.yml 自动触发 → 构建资产 → 创建 GitHub Release
```

**关键原则：** `release-please` 只做 Release PR 和 CHANGELOG，**不自动打 tag**。
只有人类明确 `git tag vX.Y.Z && git push origin vX.Y.Z` 才会触发正式发布构建。

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
> 合并后 `post-merge-stamp` 自动同步。人工任务只是确认和打 tag。

- [ ] 确认 Release PR 已合并
- [ ] 确认 `post-merge-stamp` job 成功（Actions → 最新 Release Please 运行）
- [ ] 验证 main 上的 VERSION 已更新为新版本号
- [ ] 验证 changelog.html 已包含新版本的内容（本地 `make changelog-check`）
- [ ] 运行 `make validate` 全部通过
- [ ] 确认 `CHANGELOG.md` 含该版本节（`validate_release_notes.py` 会校验）

---

## 发布阶段（手动打 tag）

```bash
# 1. 确保本地 main 是最新
git checkout main && git pull

# 2. 验证
make validate

# 3. 打版本 tag（格式必须是 vX.Y.Z）
git tag vX.Y.Z
git push origin vX.Y.Z

# → release.yml 自动触发：
#   - 构建 PDF、Skill ZIP、完整发行 ZIP
#   - 生成 CHECKSUMS.txt
#   - 创建 GitHub Release 并上传所有资产
```

- [ ] tag 已推送：`git push origin vX.Y.Z`
- [ ] GitHub Actions → Release Pipeline 运行成功
- [ ] GitHub Release 页面存在，资产文件齐全（PDF + ZIP + CHECKSUMS.txt）
- [ ] 所有资产 URL 不包含 `untagged-`（防止 v1.8.1 事故重现）
- [ ] 验证 GitHub Pages 自动部署成功（Settings → Pages → 部署历史）
- [ ] 访问 https://edic.cgartlab.com 确认正常

---

## 发布后（T+1 天）

- [ ] 监控 issue 区是否有 release 相关问题
- [ ] 如有 hotfix：创建 `hotfix/x.y.z` 分支，修复合并后打 `vX.Y.Z+1` tag
- [ ] 关闭 milestone（如使用 GitHub Milestones）
- [ ] 团队庆祝 🎉

---

## 紧急回滚

如果发布后发现严重问题：

```bash
# 1. 删除远程 tag
git push origin :refs/tags/vX.Y.Z

# 2. 如已创建 GitHub Release，在 GitHub UI 中将其删除或标记为 pre-release

# 3. 恢复 main 到上一个稳定 tag
git checkout main
git reset --hard vX.Y.Z-1
git push --force-with-lease

# 4. 修复 → hotfix 分支 → 重新发布
git checkout -b hotfix/vX.Y.Z
# ... 修复 ...
git tag -a vX.Y.Z -m "Hotfix vX.Y.Z"
git push origin vX.Y.Z
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
