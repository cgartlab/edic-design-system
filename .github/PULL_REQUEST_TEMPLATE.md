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
- [ ] `README.md` / `AGENTS.md` / `DEVELOPMENT-GUIDE.md`
- [ ] `CHANGELOG.md`
- [ ] `docs/changelog_human/`（新增版本的更新摘要 Markdown）
- [ ] `docs/*`（流程文档）
- [ ] `prompts/*` / `skills/*`
- [ ] `tools/*` / `tests/*`
- [ ] `.github/*`
- [ ] `assets/*`
- [ ] 全部 HTML 中的 `?v=` 版本号已 bump

## 版本影响 (Version Impact)

**重要：Commit 前缀决定版本号增幅。**

| 前缀 | 版本增幅 | 适用场景 |
|------|----------|----------|
| `fix:` | PATCH (1.7.0→1.7.1) | Bug 修复、样式微调、文档修正 |
| `feat:` | MINOR (1.7.0→1.8.0) | 新功能、新组件、新令牌 |
| `feat!:` / `fix!:` | MAJOR (→2.0.0) | 破坏性变更（需在下方说明）|

**Breaking Change：** 如果是破坏性变更，请在 PR Description 正文末尾添加：
```
BREAKING CHANGE: <简要说明破坏了什么>
```

---

## 版本更新摘要（仅发布 PR 填写）

**此次发布是否需要更新网站更新日志？**

- [ ] 需要（请继续填写）
- [ ] 不需要（bug 修复、文档修正等不影响用户的功能性变更）

**如果是需要更新，请创建/更新 `docs/changelog_human/vX.Y.Z.md`**：

此文件将自动生成网站更新日志中的对应版本摘要。

---

## 验证

请确认已运行以下检查：

- [ ] `make validate`（全部校验通过）
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
