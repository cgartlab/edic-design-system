# Release Please — 运维手册

> 本文档面向仓库管理员。包含 release-please 的初始配置、日常运维和故障排查。
> 普通贡献者无需阅读此文档——发布流程对你是透明的。

---

## 初始配置（一次性）

### Step 1：创建 Personal Access Token（PAT）

release-please 需要一个有写权限的 GitHub Token 来创建 PR 和 tag。

1. 打开 GitHub → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained personal access tokens**
2. 点击 **Generate new token**
3. 配置：
   - **Name**：`edic-release-please`
   - **Expiration**：90 days（建议）
   - **Repository access**：Only select repositories → `edic-design-system`
   - **Permissions**：
     - Contents: **Read and Write**
     - Pull requests: **Read and Write**
     - Metadata: **Read-only**（自动）
     - Actions: **Read and Write**
     - Workflows: **Read and Write**
4. 点击 **Generate token**
5. **立即复制 token**（关闭页面后无法再次查看）

### Step 2：添加 PAT 为 GitHub Secret

1. 打开仓库 → **Settings** → **Secrets and variables** → **Actions**
2. 点击 **New repository secret**
3. **Name**：`RELEASE_PLEASE_TOKEN`
4. **Secret**：粘贴上一步的 PAT 值
5. 点击 **Add secret**

> ⚠️ **重要**：PAT 会在到期后失效。设置日历提醒在 90 天内轮换。

### Step 3：配置 Branch Protection

1. 打开仓库 → **Settings** → **Branches** → **Branch protection rules**
2. 点击 **Add rule**
3. 配置：
   - **Branch name pattern**：`main`
   - ☑ **Require a pull request before merging**
   - ☑ **Require approvals**：1
   - ☑ **Require status checks to pass before merging**
     - 搜索并添加：`Validate`（来自 ci.yml）
   - ☑ **Allow specified actors to bypass PR requirements**
     - 添加：`github-actions[bot]`
   - ☑ **Require linear history**
   - ☑ **Do not allow force pushes**
   - ☑ **Do not allow branch deletions**
4. 点击 **Save**

> ℹ️ `github-actions[bot]` 的绕过仅限 **审批要求**，状态检查（Validate）不可绕过。

---

## 日常运维

### 正常发布流程（自动化）

1. 确认 `main` 有 `feat:` 或 `fix:` 类型的 commit
2. release-please 会自动打开一个 `chore(release): release vX.Y.Z` PR
3. 检查 PR 中的 CHANGELOG 是否正确
4. CI 的 `Validate` 检查必须通过
5. 合并 PR → 自动创建 tag → 自动构建 GitHub Release

### 手动触发（workflow_dispatch）

1. 打开 GitHub → **Actions** → **Release Please** → **Run workflow**
2. 填写参数：
    - **release-as**：强制版本号（如 `1.6.0`），留空则自动计算
3. 点击 **Run workflow**

### 紧急热修复（workflow_dispatch）

正常发布一律通过合并 Release PR 完成，由 release-please 自动创建 tag + GitHub Release。
紧急热修复仅在自动链路不可用时使用，通过 `release.yml` 的 `workflow_dispatch` 手动触发：

1. 创建 hotfix 分支、修复、提交、PR 合并
2. 打开 GitHub → **Actions** → **Release Pipeline** → **Run workflow**
3. 填写参数：
   - **version**（必填）：版本号（如 `1.6.0`）
   - **skip_validation**：紧急时勾选跳过验证
4. 验证 `main` 上 `VERSION` / HTML `?v=` 已同步（workflow_dispatch 路径自动执行 `stamp_version.py`）

> ⚠️ **不要手工 `git tag` + 手动预置 manifest**。手工 tag 会导致 release-please 误判，
> 产生"幽灵发布"（幽灵 Release PR / 重复版本 bump）。正常发布一律走 Release PR 合并。

---

## 故障排查

### release-please 没有创建 PR

**检查**：
1. `main` 分支是否有 `feat:`、`fix:`、`perf:` 等可发布类型的 commit？
2. PAT 是否有效？（Settings → Secrets and variables → 检查 `RELEASE_PLEASE_TOKEN`）
3. 查看 Actions → Release Please → 最新 run 的日志

**解决**：
```bash
# 手动触发 release-please
gh workflow run release-please.yml
```

### Release PR 合并后没有创建 tag

**检查**：Actions → Release Please 日志，确认：
1. `release_created` output 是否为 `true`
2. `tag_name` / `version` output 是否有输出值
3. `skip-github-release` 是否保持 `false`（release-please.yml 中应为注释而非显式 `true`）

**解决**：
```bash
# 手动重新触发 release-please.yml，让其重跑
gh workflow run release-please.yml
```

> ⚠️ **不要手工 `git tag`**。手工 tag 会导致 release-please 误判，产生幽灵发布。
> 如果必须介入，先用 `gh workflow run release-please.yml` 让 release-please-action 重跑一次。

### 版本不一致（VERSION vs CHANGELOG vs tag）

检查 `.release-please-manifest.json` 的版本是否与 `VERSION` 一致：

```bash
# 查看 manifest
cat .release-please-manifest.json

# 查看 VERSION
cat VERSION
```

如果不一致，手动修正：
```bash
# 修正 manifest
echo '{".": "1.6.0"}' > .release-please-manifest.json
git add .release-please-manifest.json
git commit -m "chore: sync manifest to v1.6.0"
git push
```

### PAT 过期

1. 重新生成 PAT（见 Step 1）
2. 更新 Secret：Settings → Secrets → `RELEASE_PLEASE_TOKEN` → **Update**

---

## PAT 轮换流程

PAT 建议每 90 天轮换一次：

1. 生成新 PAT（Step 1）
2. 更新 GitHub Secret（Step 2）
3. 验证：触发 `release-please.yml` 一次，确保新 token 有效
4. 撤销旧 PAT（GitHub → Developer settings → 找到旧 token → Revoke）

---

## 回滚

如果 release-please 创建了错误的版本：

```bash
# 1. 删除错误 tag
git tag -d v1.6.0
git push origin :refs/tags/v1.6.0

# 2. 删除 GitHub Release（如果已创建）
gh release delete v1.6.0 --yes

# 3. 修正 .release-please-manifest.json 到正确版本
echo '{".": "1.5.5"}' > .release-please-manifest.json
git add .release-please-manifest.json
git commit -m "chore: rollback manifest to v1.5.5"
git push

# 4. 重新触发 release-please.yml 以对齐 manifest
gh workflow run release-please.yml

# 5. 关闭已打开的 Release PR（如果有）
```

---

## 参考资料

- [release-please GitHub](https://github.com/googleapis/release-please)
- [release-please-action](https://github.com/googleapis/release-please-action)
- [Conventional Commits](https://www.conventionalcommits.org/)
