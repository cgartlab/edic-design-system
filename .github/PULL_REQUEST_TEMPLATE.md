# EDIC Design System — Pull Request

感谢你的贡献！请认真填写以下各项，有助于快速评审。

---

## 关联 Issue

- Closes #___（必填，如适用）
- Related to #___（可选）

## 类型

- [ ] 🐞 Bug 修复（`fix:`）
- [ ] ✨ 新功能（`feat:`）
- [ ] 🧩 新组件
- [ ] 🎨 新令牌
- [ ] 🖼️ 新图标
- [ ] 📝 文档改进（`docs:`）
- [ ] 💄 样式调整（`style:`）
- [ ] ♻️ 重构（`refactor:`）
- [ ] ⚡ 性能优化（`perf:`）
- [ ] ✅ 测试（`test:`）
- [ ] 🔧 构建 / 工具（`chore:`）

## 版本影响

> PR 标题前缀决定下次 release-please 自动计算的版本号。

| 前缀 | 版本影响 | 用途 |
|------|---------|------|
| `feat:` | MINOR 升级 | 新组件 / 新令牌 / 新功能 |
| `fix:` | PATCH 升级 | Bug 修复 / 暗色微调 / 文档修正 |
| `feat!:` / `fix!:` | MAJOR 升级 | 破坏性变更（慎用） |
| `chore:` / `docs:` / `style:` | **不触发版本升级** | 工具维护 / 纯文档 / 格式 |
| `refactor:` / `perf:` | 不触发版本升级（除非加 `!`） | 重构 / 性能 |

> ⚠️ **使用 `chore:`** 标注不希望触发版本号变更的 PR（CI 维护、依赖更新、文档修正等）。

当前 PR 适用前缀：______

## 破坏性变更

- [ ] 无
- [ ] 有（请在下方详细说明 + 关联 MAJOR 版本号变更）

**变更说明**：

## 改动清单

请勾选涉及的文件：

- [ ] `styles.css`
- [ ] `scripts.js`
- [ ] `tokens.json`
- [ ] `index.html` / `docs.html` / `prompts.html` / `downloads.html` / `terms.html`
- [ ] `blog.html` / `company.html` / `resume.html` / `report.html`
- [ ] `changelog.html`（⚠️ 不要手动编辑：由 `make changelog` 自动生成）
- [ ] `docs/changelog_human/vX.Y.Z.md`（新增版本说明，Release PR 必填）
- [ ] `README.md` / `AGENTS.md` / `DEVELOPMENT-GUIDE.md`
- [ ] `CHANGELOG.md`（由 release-please 自动管理，勿手动编辑）
- [ ] `docs/*`（流程文档）
- [ ] `prompts/*` / `skills/*`
- [ ] `tools/*` / `tests/*`
- [ ] `.github/*`
- [ ] `assets/*`
- [ ] 全部 HTML 中的 `?v=` 版本号已 bump（`make stamp-version`）

## 验证

请确认已运行以下检查：

- [ ] `make validate`（全部校验通过）
- [ ] `make changelog-check`（如添加了 `docs/changelog_human/` 内容）
- [ ] 浏览器实测（Chrome / Firefox / Safari）
- [ ] 浅色 + 暗色模式验证
- [ ] 移动端验证（375px / 768px）
- [ ] 键盘可达性（Tab / Enter / Esc）
- [ ] 屏幕阅读器（如有可访问性影响）

## 截图 / 录屏

**改动前**（如适用）：

**改动后**：

## 附加说明

（设计决策、取舍、未完成项等）
