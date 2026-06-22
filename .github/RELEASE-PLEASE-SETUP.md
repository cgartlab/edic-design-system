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
   - **prerelease**：勾选则标记为预发布
3. 点击 **Run workflow**

### 紧急热修复（手动 tag）

当 GitHub Actions 不可用时：

```bash
# 1. 同步版本
make sync-versions

# 2. 验证
make validate

# 3. 提交
git add -A && git commit -m "chore(release): bump v1.6.0"

# 4. 打 tag 并推送
git tag -a v1.6.0 -m "Release v1.6.0"
git push && git push origin v1.6.0

# 5. 手动同步 .release-please-manifest.json（避免下次 release-please 重复发布）
```

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

**检查**：Actions → Release Please 日志，看是否输出了 `tag_name: vX.Y.Z`

**解决**：
```bash
# 手动创建 tag
git tag -a v1.6.0 -m "Release v1.6.0"
git push origin v1.6.0
```

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

# 4. 关闭已打开的 Release PR（如果有）
```

---

## 参考资料

- [release-please GitHub](https://github.com/googleapis/release-please)
- [release-please-action](https://github.com/googleapis/release-please-action)
- [Conventional Commits](https://www.conventionalcommits.org/)
