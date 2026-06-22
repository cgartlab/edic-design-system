# 发布检查清单（Release Checklist）

> 在打 tag 之前必须完成的所有事项。本清单是 [VERSIONING.md](./VERSIONING.md) 的执行细节。

## 准备阶段（T-7 天）

- [ ] 确认所有 `dev-xxx` 分支已合并或关闭
- [ ] 确认所有阻塞性 issue 已解决
- [ ] 创建 `release/x.y.z` 分支（如需冻结代码）
- [ ] 通知贡献者：「即将发布，请检查是否有未提交的 PR」
- [ ] 检查外部依赖（GitHub Pages、CNAME 解析）是否健康

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

## 文档阶段（T-1 天）

- [ ] 更新 `CHANGELOG.md`：将 `[未发布]` 段改名为新版本号 + 日期
- [ ] 检查 `README.md` 截图与示例是否需要更新
- [ ] 检查 `AGENTS.md` 组件清单是否需要更新
- [ ] 检查 `DEVELOPMENT-GUIDE.md` 是否需要更新
- [ ] 检查 `docs.html` 预览是否完整
- [ ] 检查 `docs.html` 教程是否需要更新

## 代码阶段（发布当天）

- [ ] 写入新版本号到 `VERSION`（如 `1.4.0`）
- [ ] 运行 `make sync-versions` 一次性同步 VERSION / tokens.json / package.json 及 HTML/MD
- [ ] 同步更新 `scripts.js` 的 `TOKENS` 数组（如有新增令牌）
- [ ] 运行 `make validate` 全部通过
- [ ] 重新生成示例 PDF（如有视觉变更）：`python3 tools/generate_pdfs.py`
- [ ] 提交最终 commit：`chore(release): bump vX.Y.Z`

## 发布阶段

- [ ] 合并 `release/x.y.z` → `main`（如使用 release 分支）
- [ ] 打 tag：`git tag -a vX.Y.Z -m "Release vX.Y.Z"`
- [ ] 推送 tag：`git push origin vX.Y.Z`
- [ ] 在 GitHub 上创建 Release（基于 tag）
  - 标题：`vX.Y.Z`
  - 内容：从 `CHANGELOG.md` 复制
  - 附件：上传 `assets/downloads/*.pdf`（如有变更）
- [ ] 验证 GitHub Pages 自动部署成功（Settings → Pages → 部署历史）
- [ ] 访问 https://edic.cgartlab.com 确认正常
- [ ] 在社交渠道（可选）发布公告

## 发布后（T+1 天）

- [ ] 监控 issue 区是否有 release 相关问题
- [ ] 如有 hotfix：创建 `hotfix/x.y.z` 分支，修复合并后打 `vX.Y.Z+1` tag
- [ ] 在 `CHANGELOG.md` 顶部新增 `## [未发布]` 段，为下版本做准备
- [ ] 关闭 milestone（如使用 GitHub Milestones）
- [ ] 团队庆祝 🎉

## 紧急回滚

如果发布后发现严重问题：

```bash
# 1. 删除远程 tag
git push origin :refs/tags/vX.Y.Z

# 2. 恢复 main 到上一个稳定 tag
git checkout main
git reset --hard vX.Y.Z-1
git push --force-with-lease

# 3. 修复 → hotfix 分支 → 重新发布
git checkout -b hotfix/vX.Y.Z
# ... 修复 ...
git tag -a vX.Y.Z -m "Hotfix vX.Y.Z"
git push origin vX.Y.Z
```

> ⚠️ `--force-with-lease` 比 `--force` 安全，会检测上游是否被改过。

## 版本号速查

当前版本见 `CHANGELOG.md` 顶部。

| 类型 | 例 | 何时 |
|------|----|------|
| 下一个 MAJOR | `2.0.0` | 删除组件 / 令牌重构 / 设计语言变化 |
| 下一个 MINOR | `1.2.0` | 新增组件 / 新增令牌 / 新增示例 |
| 下一个 PATCH | `1.1.1` | 修复 / 暗色微调 / 文档修正 |
| 预发布 | `1.2.0-beta.1` | 公开测试 |

---

*执行模板：可复制此清单到对应 GitHub Issue，命名为 `Release vX.Y.Z`，逐项勾选。*
