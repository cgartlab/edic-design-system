# 贡献指南（Contributing Guide）

> 感谢你有兴趣贡献 EDIC 设计系统！本文档说明提交流程、规范与质量要求。

## 行为准则

本项目遵循 [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)。参与即表示你同意遵守其条款。

## 我能贡献什么？

| 类型 | 适合谁 | 入口 |
|------|--------|------|
| 🐞 报告 Bug | 使用者 | [Bug Report](../../issues/new?template=bug_report.md) |
| 💡 功能建议 | 设计师 / 开发者 | [Feature Request](../../issues/new?template=feature_request.md) |
| 🧩 新组件 | 前端开发者 | [Component Request](../../issues/new?template=component_request.md)（先评审再实现） |
| 🎨 新令牌 | 设计师 | [Token Request](../../issues/new?template=token_request.md) |
| 🖼️ 新图标 | 设计师 | PR（直接提交，遵循 [图标规范](./docs/COMPONENT-DEVELOPMENT.md#图标规范)） |
| 📝 文档改进 | 任何人 | PR（错别字、示例、说明） |
| ♿ 可访问性 | 任何人 | PR（键盘、对比度、ARIA） |

> **重要**：新增组件 / 令牌 / 破坏性变更请**先提 Issue 讨论**，再开 PR。直接开 PR 容易被拒。

## 开发流程

### 1. 准备工作

```bash
# 克隆
git clone https://github.com/cgartlab/cgartlab-design-system.git
cd cgartlab-design-system

# 本地预览（任选其一）
python3 -m http.server 8000
# 或
npx serve .
```

> 项目采用**零构建**架构，无需 `npm install` / `pnpm install`。所有文件即用即看。

### 2. 创建分支

遵循根工作区 [`BRANCH-WORKFLOW.md`](../BRANCH-WORKFLOW.md) 的命名规范：

```bash
# 开发
git checkout -b dev-组件名-简短描述
# 例：git checkout -b dev-tabs-keyboard-nav

# 修复
git checkout -b fix-简短描述
# 例：git checkout -b fix-dark-mode-contrast

# 新内容（写作类）
git checkout -b write-主题-简短描述
```

提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/)：

```text
feat(component): 新增 ds-tabs 键盘导航支持
fix(token): 暗色模式对比度调整
docs(handbook): 补全 Slider 组件示例
style(swatch): 调整间距
refactor(scripts): 拆分图标渲染 IIFE
test(validate): 增加 token 名称正则校验
chore(release): bump v1.6.0
```

### 3. 本地验证

在提 PR 前必须运行：

```bash
# 全部校验（推荐）
make validate
# 等价于：
python3 tools/validate_tokens.py
python3 tools/validate_naming.py
python3 tools/validate_html.py
python3 tools/validate_a11y.py
python3 tools/validate_versions.py
python3 tools/validate_links.py
```

或单独运行某一项：

```bash
make validate-tokens   # 仅令牌
make validate-html     # 仅 HTML
make serve             # 本地预览
```

### 4. 提 PR

- 填写 [PR 模板](../../pulls) 中所有勾选项
- 关联相关 Issue（`Closes #123`）
- 截图 / 录屏展示改动效果（尤其视觉相关）
- 确保 CI 全绿

## 质量标准

### 设计令牌

- ✅ 必须用 OKLch 表达颜色（与现有体系一致）
- ✅ 必须有完整暗色模式对应值
- ✅ 必须有 WCAG AA 文字对比度（4.5:1 普通 / 3:1 大字）
- ✅ 命名遵循 `--ds-{category}-{name}[-{modifier}]`
- ❌ 禁止硬编码 `#fff`、`#000`、`16px` 等魔法值

详见 [`docs/COMPONENT-DEVELOPMENT.md`](./docs/COMPONENT-DEVELOPMENT.md#令牌规范) 与 [SKILL.md](./skills/edic-design-system/SKILL.md)。

### 组件

- ✅ 基础 + 修饰符：`ds-btn` / `ds-btn--primary`
- ✅ 状态完整：default / hover / active / focus / disabled
- ✅ 暗色模式正常（用令牌，不写死颜色）
- ✅ 键盘可达：Tab、Enter、Esc、方向键（按需）
- ✅ 屏幕阅读器：语义化标签、`aria-*` 合理
- ❌ 禁止内联 `style=`（除动态计算值如错峰延迟 `--d`）
- ❌ 禁止 `onclick` 内联事件（用 `addEventListener`）

详见 [`docs/COMPONENT-DEVELOPMENT.md`](./docs/COMPONENT-DEVELOPMENT.md)。

### 图标

- viewBox 必须为 `0 0 24 24`
- stroke-width: 1.5（CSS 统一控制）
- fill: none
- 风格统一：Lucide / Feather 线性
- 命名：`kebab-case.svg`（如 `arrow-right.svg`）

### 文档

- 改动 `styles.css` / `scripts.js` 后，**必须**在所有 HTML 中同步 bump `?v=` 版本号
- 改动令牌需同步更新 `tokens.json` 与 `scripts.js` 的 `TOKENS` 数组
- 新增组件需在 `docs.html` 的 `#visual-components` 区域添加预览
- 重大变更需更新 `CHANGELOG.md` 并 bump 版本号

### 发布流程

发布已自动化。贡献者无需手动发布：

- **提交符合 Conventional Commits** 的 PR（`feat:`、`fix:`、`docs:` 等）
- 合并到 `main` 后，`release-please` 自动创建 Release PR
- Release PR 合并后自动打 tag → GitHub Release 包含 PDF/ZIP 附件

详见 [`docs/VERSIONING.md`](./docs/VERSIONING.md) 和 [`docs/RELEASE-CHECKLIST.md`](./docs/RELEASE-CHECKLIST.md)。

## 目录结构（参考）

```
edic-design-system/
├── index.html / docs.html / prompts.html / downloads.html / terms.html
├── blog.html / company.html / resume.html / report.html   # 真实示例
├── styles.css         # 令牌 + 暗色 + 组件 + 动效
├── scripts.js         # 交互
├── tokens.json        # 结构化令牌（程序化导入）
├── assets/            # brand / downloads
├── prompts/           # AI 提示词（system / quick）
├── skills/            # Agent SKILL 包
├── tools/             # 验证脚本（validate_*.py / generate_pdfs.py）
├── tests/             # 验证夹具与测试
├── docs/              # 流程文档（VERSIONING / COMPONENT-DEVELOPMENT / TESTING / RELEASE-CHECKLIST）
├── .github/           # Issue / PR 模板 / Workflows
├── scripts/           # 本地开发脚本（dev.sh / dev.ps1）
└── 配置文件：.editorconfig / .gitattributes / Makefile / AGENTS.md / README.md / LICENSE
```

## 评审流程

1. **自动化**：CI 跑全部验证脚本，任一失败 → 阻塞合并
2. **设计评审**：视觉相关改动需至少 1 位维护者 LGTM
3. **代码评审**：至少 1 位维护者 LGTM
4. **兼容性检查**：移动端（≤640px）、平板（768-1023px）、桌面（≥1024px）
5. **可访问性**：键盘可达 + 屏幕阅读器可读

## 许可证

贡献即表示你同意你的贡献以 [CC BY 4.0](./LICENSE) 许可证发布。衍生作品可选择不同许可证（不强制保持 CC BY 4.0）。

---

有问题？在 [Discussion](../../discussions) 开帖或在相关 Issue 下留言。
