# Automated Release Workflows Research

**Project:** EDIC Design System
**Date:** 2026-06-22
**Purpose:** Evaluate automated version release tools for GitHub-based design system with zero runtime dependencies

> **状态：** ✅ 已实施（Phase 1–3 已完成，Phase 4 待 GitHub UI 配置）
> 实施细节见：[`.github/RELEASE-PLEASE-SETUP.md`](../.github/RELEASE-PLEASE-SETUP.md)

---

## Executive Summary

| Tool | Best For | EDIC Fit | Complexity | npm Dependency |
|------|----------|----------|------------|----------------|
| **release-please** | Google-style repos, multi-language, GitHub Releases | ⭐⭐⭐⭐⭐ | Low | No |
| **semantic-release** | Full automation, npm-centric but extensible | ⭐⭐⭐⭐ | Medium | Optional |
| **Changesets** | Monorepos, multi-package coordination | ⭐⭐⭐ | Medium-High | Yes |
| **Custom GitHub Actions** | Full control, any workflow | ⭐⭐⭐⭐ | Variable | No |

**Recommendation:** For EDIC Design System's specific needs (zero npm publish, three version sources, Conventional Commits), **release-please** with manifest mode or a **custom GitHub Actions workflow** are the best fits.

---

## 1. release-please (Google)

### How It Works

**release-please** (by Google) automates releases based on Conventional Commits by:

1. **Parsing git history** for Conventional Commit messages
2. **Creating Release PRs** with changelog updates and version bumps
3. **Generating GitHub Releases** when PRs are merged
4. **Supporting multiple release types** via `release-type` configuration

**Core workflow:**
```
Commit → release-please scans history → Creates Release PR → 
Merge PR → Version bumped, tag created → GitHub Release published
```

### Version Bump Logic

| Commit Type | SemVer Bump |
|-------------|-------------|
| `fix:` | Patch (1.0.0 → 1.0.1) |
| `feat:` | Minor (1.0.0 → 1.1.0) |
| `feat!:`, `fix!:`, `BREAKING CHANGE:` | Major (1.0.0 → 2.0.0) |

### Configuration Options

**Basic setup (simple strategy):**
```yaml
# .github/workflows/release-please.yml
on:
  push:
    branches:
      - main

permissions:
  contents: write
  pull-requests: write

jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          token: ${{ secrets.MY_RELEASE_PLEASE_TOKEN }}
          release-type: simple  # For non-npm projects
```

**Advanced manifest mode (recommended for EDIC):**
```yaml
jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          config-file: release-please-config.json
          manifest-file: .release-please-manifest.json
```

**release-please-config.json:**
```json
{
  "packages": {
    ".": {
      "release-type": "simple",
      "changelog-type": "default",
      "prerelease": false,
      "prerelease-type": "alpha"
    }
  }
}
```

### Prerelease Support

release-please supports prereleases via:

```yaml
- uses: googleapis/release-please-action@v4
  with:
    prerelease: true
    prerelease-type: beta  # alpha, beta, rc, etc.
```

**Versioning strategies available:**
- `default` - Standard SemVer (breaking→major, feat→minor, fix→patch)
- `always-bump-patch` - Always patch bump
- `always-bump-minor` - Always minor bump
- `always-bump-major` - Always major bump
- `prerelease` - Bumps prerelease number (1.2.0-beta01 → 1.2.0-beta02)

### Pros for EDIC

✅ **Zero npm dependency** - `release-type: simple` works for static HTML/CSS/JS  
✅ **GitHub-native** - Creates PRs, tags, and releases automatically  
✅ **Conventional Commits** - Already used in EDIC codebase  
✅ **Pre-release support** - Alpha/beta/rc via configuration  
✅ **Manual triggers** - Can be triggered via workflow_dispatch  
✅ **Multi-language** - Designed for non-node projects (Go, Rust, Python, etc.)  
✅ **PR-based workflow** - Human review before release (safety)  
✅ **Well-maintained** - Google-backed, 7K+ stars, active development  

### Cons for EDIC

❌ **Three version sources** - Requires custom script to sync VERSION, tokens.json, package.json  
❌ **CHANGELOG.md** - Generates CHANGELOG.md but may not match Keep a Changelog format exactly  
❌ **Release PR overhead** - Creates intermediate PR that must be merged  
❌ **No built-in multi-file bump** - Doesn't natively update multiple version files simultaneously  

### Non-npm Project Examples

**Static website / no package manager:**
```yaml
- uses: googleapis/release-please-action@v4
  with:
    release-type: simple
```

**Rust/Cargo projects:**
```yaml
- uses: googleapis/release-please-action@v4
  with:
    release-type: rust
```

**Go modules:**
```yaml
- uses: googleapis/release-please-action@v4
  with:
    release-type: go
```

**Python projects:**
```yaml
- uses: googleapis/release-please-action@v4
  with:
    release-type: python
```

### Real-World Usage

- **googleapis** - All Google Cloud APIs
- **terraform-provider** - HashiCorp Terraform providers
- **cncf** - Cloud Native Computing Foundation projects
- **static-site-generator** - See: https://github.com/sebastienrousseau/static-site-generator

---

## 2. semantic-release

### How It Works

**semantic-release** is a fully automated release tool that:

1. **Analyzes commits** since last release using plugins
2. **Determines next version** based on Conventional Commits
3. **Generates changelog** using configurable generators
4. **Publishes to channels** (npm, GitHub Releases, GitLab, etc.)
5. **Creates git tags** automatically

**Core workflow:**
```
Push to main → CI runs semantic-release → 
Analyze commits → Determine version → Generate changelog → 
Create tag → Publish → Notify
```

### Plugin Architecture

```json
{
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    ["@semantic-release/changelog", { "changelogFile": "CHANGELOG.md" }],
    ["@semantic-release/git", {
      "assets": ["CHANGELOG.md", "package.json"],
      "message": "chore(release): ${nextRelease.version} [skip ci]"
    }],
    "@semantic-release/github"
  ]
}
```

### Non-npm Configuration

**For non-npm projects (GitHub Releases only):**
```json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    ["@semantic-release/changelog", { "changelogFile": "CHANGELOG.md" }],
    ["@semantic-release/git", {
      "assets": ["CHANGELOG.md"],
      "message": "chore(release): ${nextRelease.version} [skip ci]"
    }],
    ["@semantic-release/github", {
      "assets": ["dist/**", "*.zip"]
    }]
  ]
}
```

**GitHub Actions workflow:**
```yaml
# .github/workflows/release.yml
on:
  push:
    branches: [main]

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Required for full git history

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm install

      - name: Run semantic-release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: npx semantic-release
```

### Prerelease Support

```json
{
  "branches": [
    "main",
    { "name": "beta", "prerelease": "beta" },
    { "name": "alpha", "prerelease": "alpha" }
  ]
}
```

### Pros for EDIC

✅ **Fully automated** - No manual intervention needed  
✅ **Plugin ecosystem** - 100+ plugins for any integration  
✅ **Multi-channel** - Can publish to npm, GitHub, GitLab simultaneously  
✅ **Conventional Commits** - Native support  
✅ **Pre-release branches** - Dedicated alpha/beta branches  
✅ **Issue/PR closing** - Auto-closes issues referenced in commits  
✅ **Community support** - Large ecosystem, many configurations  

### Cons for EDIC

❌ **Node.js required** - Even for non-node projects  
❌ **npm token confusion** - Documentation assumes npm, requires non-npm config  
❌ **Three version sources** - Requires custom plugin or script to sync multiple files  
❌ **Opinionated flow** - Every push to main triggers release (no PR review)  
❌ **Complex configuration** - Many plugins to configure correctly  
❌ **Breaking changes auto-bump** - Can't easily control major bumps without review  

### Non-npm Project Examples

**Discussion: C# project without npm:**
https://github.com/semantic-release/semantic-release/discussions/1967

**Shareable config for GitHub-only:**
https://github.com/JanSzewczyk/semantic-release-config

```javascript
// shareable config
export default {
  branches: ["master"],
  extends: "@szum-tech/semantic-release-config/without-npm"
};
```

### Alternative: sr (Rust-based semantic-release)

A newer, language-agnostic alternative:
- Single static binary
- Zero runtime dependencies
- Works with any language (Go, Rust, Python, Java)
- Built-in Conventional Commits parsing
- GitHub Releases support

```bash
# Install
curl -fsSL https://sr.sh | sh

# Release
sr release
```

---

## 3. Changesets

### How It Works

**Changesets** is a monorepo-focused tool that:

1. **Developers add changesets** via `npx changeset` (intent to release)
2. **Changeset files** describe which packages changed and bump type
3. **CI collects changesets** and creates release PR
4. **Merge PR** → versions bumped, changelogs updated
5. **Publish** → releases to npm/GitHub

**Core workflow:**
```
Developer: npx changeset → Creates .changeset/*.md → 
PR includes changeset → Merge → 
CI: npx changeset version → Bumps versions → 
npx changeset publish → Releases
```

### Configuration

```json
// .changeset/config.json
{
  "$schema": "https://unpkg.com/@changesets/config@2.3.0/schema.json",
  "changelog": "@changesets/cli/changelog",
  "commit": false,
  "fixed": [],
  "linked": [],
  "access": "restricted",
  "baseBranch": "main",
  "updateInternalDependencies": "patch",
  "ignore": []
}
```

### GitHub Actions Workflow

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    branches:
      - main

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm install

      - name: Build
        run: npm run build

      - name: Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx changeset publish
```

### Prerelease Support

```bash
# Start prerelease
npx changeset pre enter beta

# Exit prerelease
npx changeset pre exit
```

### Pros for EDIC

✅ **Monorepo-ready** - If EDIC expands to multiple packages  
✅ **Human-in-the-loop** - Changesets added during PR creation  
✅ **Transparent** - Release intent visible before merge  
✅ **Internal dependency handling** - Coordinates version bumps across packages  
✅ **Pre-release workflow** - Built-in prerelease mode  

### Cons for EDIC

❌ **npm-focused** - Designed for npm packages, requires npm install  
❌ **Heavy for single package** - Overkill for single static site  
❌ **Node.js required** - Even for non-node projects  
❌ **Manual changeset creation** - Developers must remember to add changesets  
❌ **No built-in GitHub Releases** - Requires additional configuration  
❌ **Multiple version files** - Not designed for non-package.json version sources  

### When to Use Changesets

**Best for:**
- Monorepos with multiple npm packages
- Teams wanting transparent release process
- Projects where packages depend on each other

**Not ideal for:**
- Single-package projects
- Non-npm projects
- Projects wanting fully automated releases

---

## 4. Custom GitHub Actions Workflow

### Pattern 1: Tag-Triggered Release

```yaml
# .github/workflows/release.yml
name: Create Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Generate Changelog
        id: changelog
        uses: TriPSs/conventional-changelog-action@v5
        with:
          github-token: ${{ secrets.github_token }}
          output-file: 'CHANGELOG.md'
          preset: 'angular'
          tag-prefix: 'v'

      - name: Create GitHub Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: ${{ github.ref }}
          body_path: 'CHANGELOG.md'
```

### Pattern 2: Auto-Versioning with Conventional Commits

```yaml
# .github/workflows/release.yml
name: Auto Version & Release

on:
  push:
    branches:
      - main
  workflow_dispatch:
    inputs:
      version:
        description: 'Manual version bump (e.g., 1.2.0)'
        required: false

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm install

      - name: Generate Changelog & Bump Version
        id: changelog
        uses: TriPSs/conventional-changelog-action@v5
        with:
          github-token: ${{ secrets.github_token }}
          git-message: 'chore(release): {version}'
          preset: 'angular'
          tag-prefix: 'v'
          output-file: 'CHANGELOG.md'
          version-file: './package.json'
          version-path: 'version'
          skip-on-empty: 'false'
          skip-commit: 'false'

      - name: Sync Versions
        run: |
          # Sync VERSION file
          NEW_VERSION=${{ steps.changelog.outputs.version }}
          echo "$NEW_VERSION" > VERSION
          
          # Sync tokens.json
          node -e "
            const fs = require('fs');
            const tokens = JSON.parse(fs.readFileSync('tokens.json', 'utf8'));
            tokens.version = '$NEW_VERSION';
            fs.writeFileSync('tokens.json', JSON.stringify(tokens, null, 2));
          "
          
          # Sync package.json (already done by changelog-action)
          echo "Versions synced to $NEW_VERSION"

      - name: Create GitHub Release
        if: steps.changelog.outputs.skipped == 'false'
        uses: ncipollo/release-action@v1
        with:
          tag: "v${{ steps.changelog.outputs.version }}"
          name: "v${{ steps.changelog.outputs.version }}"
          body: ${{ steps.changelog.outputs.clean_changelog }}
          generateReleaseNotes: true
          draft: false
          prerelease: false
```

### Pattern 3: Manual Trigger with Version Input

```yaml
# .github/workflows/release.yml
name: Manual Release

on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to release (e.g., 1.2.0)'
        required: true
        type: string
      prerelease:
        description: 'Mark as prerelease'
        required: false
        type: boolean
        default: false
      draft:
        description: 'Create as draft'
        required: false
        type: boolean
        default: false

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Git
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

      - name: Update Version Files
        run: |
          VERSION="${{ inputs.version }}"
          
          # Update VERSION file
          echo "$VERSION" > VERSION
          
          # Update tokens.json
          node -e "
            const fs = require('fs');
            const tokens = JSON.parse(fs.readFileSync('tokens.json', 'utf8'));
            tokens.version = '$VERSION';
            fs.writeFileSync('tokens.json', JSON.stringify(tokens, null, 2));
          "
          
          # Update package.json
          node -e "
            const fs = require('fs');
            const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
            pkg.version = '$VERSION';
            fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
          "
          
          git add VERSION tokens.json package.json
          git commit -m "chore(release): bump to v$VERSION"
          git push

      - name: Create Tag
        run: |
          git tag "v${{ inputs.version }}"
          git push origin "v${{ inputs.version }}"

      - name: Generate Changelog
        id: changelog
        uses: TriPSs/conventional-changelog-action@v5
        with:
          github-token: ${{ secrets.github_token }}
          output-file: 'CHANGELOG.md'
          preset: 'angular'
          tag-prefix: 'v'
          release-count: '10'

      - name: Create GitHub Release
        uses: ncipollo/release-action@v1
        with:
          tag: "v${{ inputs.version }}"
          name: "v${{ inputs.version }}"
          body: ${{ steps.changelog.outputs.clean_changelog }}
          draft: ${{ inputs.draft }}
          prerelease: ${{ inputs.prerelease }}
          generateReleaseNotes: false
```

### Pattern 4: Idempotent Release (Safe Retry)

```yaml
- name: Create/Update GitHub Release
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    TAG: "v${{ steps.version.outputs.current }}"
  run: |
    BODY=$(cat /tmp/release-body.md)
    
    # Idempotent: create if doesn't exist, else update in place
    if gh release view "$TAG" >/dev/null 2>&1; then
      echo "Release $TAG already exists — updating in place"
      gh release edit "$TAG" \
        --title "$TAG" \
        --notes "$BODY"
      gh release upload "$TAG" artifacts/* --clobber
    else
      gh release create "$TAG" \
        --title "$TAG" \
        --notes "$BODY" \
        --generate-notes \
        artifacts/*
    fi
```

### Available Actions

| Action | Purpose |
|--------|---------|
| `TriPSs/conventional-changelog-action` | Changelog generation + version bump |
| `ncipollo/release-action` | Create GitHub Releases |
| `actions/create-release` | Official GitHub release creation |
| `softprops/action-gh-release` | Release with asset upload |
| `ietf-tools/semver-action` | Calculate next SemVer version |
| `prantlf/bump-version-action` | Bump version + changelog |

### Pros for EDIC

✅ **Full control** - Customize every step of the workflow  
✅ **Three version sources** - Can sync VERSION, tokens.json, package.json  
✅ **Keep a Changelog** - Can format changelog exactly as needed  
✅ **Manual triggers** - Emergency releases via workflow_dispatch  
✅ **No npm dependency** - Pure GitHub Actions  
✅ **Idempotent** - Safe to retry on failure  
✅ **No PR overhead** - Direct tag and release creation  

### Cons for Custom Workflow

❌ **Maintenance burden** - Must maintain workflow yourself  
❌ **Error handling** - Must handle edge cases manually  
❌ **No built-in SemVer analysis** - Requires external action or script  
❌ **Breaking change detection** - Must implement manually  

---

## 5. Comparison Matrix

| Feature | release-please | semantic-release | Changesets | Custom GA |
|---------|---------------|------------------|------------|-----------|
| **npm Required** | ❌ No | ✅ Yes | ✅ Yes | ❌ No |
| **Conventional Commits** | ✅ Native | ✅ Native | ⚠️ Manual | ⚠️ Via action |
| **GitHub Releases** | ✅ Native | ✅ Plugin | ⚠️ Plugin | ✅ Native |
| **Pre-release Support** | ✅ Config | ✅ Branches | ✅ CLI | ✅ Input |
| **Manual Trigger** | ✅ workflow_dispatch | ❌ No | ⚠️ CLI | ✅ workflow_dispatch |
| **Multi-file Version** | ⚠️ Script | ⚠️ Plugin | ❌ No | ✅ Custom |
| **PR Review** | ✅ Release PR | ❌ Auto | ✅ Changeset PR | ❌ Direct |
| **Monorepo Support** | ✅ Manifest | ⚠️ Lerna | ✅ Native | ❌ Custom |
| **Keep a Changelog** | ⚠️ Format diff | ⚠️ Format diff | ⚠️ Format diff | ✅ Custom |
| **Zero Dependencies** | ✅ | ❌ Node.js | ❌ Node.js | ✅ |
| **Community Size** | 7K+ stars | 8K+ stars | 12K+ stars | N/A |

---

## 6. EDIC-Specific Recommendations

### Recommended: release-please with Manifest Mode

**Why:**
- Zero npm dependency required
- GitHub-native workflow
- PR-based (human review before release)
- Well-documented for non-node projects
- Active maintenance by Google

**Implementation:**

1. **Create release-please-config.json:**
```json
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "packages": {
    ".": {
      "release-type": "simple",
      "changelog-type": "default",
      "bump-minor-pre-major": true,
      "bump-patch-for-minor-pre-major": true
    }
  }
}
```

2. **Create workflow:**
```yaml
# .github/workflows/release-please.yml
name: release-please

on:
  push:
    branches:
      - main
  workflow_dispatch:
    inputs:
      release-as:
        description: 'Force version (e.g., 1.2.3)'
        required: false

permissions:
  contents: write
  pull-requests: write

jobs:
  release-please:
    runs-on: ubuntu-latest
    outputs:
      release_created: ${{ steps.release.outputs.release_created }}
      tag_name: ${{ steps.release.outputs.tag_name }}
    steps:
      - uses: googleapis/release-please-action@v4
        id: release
        with:
          token: ${{ secrets.RELEASE_PLEASE_TOKEN || secrets.GITHUB_TOKEN }}
          config-file: release-please-config.json
          manifest-file: .release-please-manifest.json

  sync-versions:
    needs: release-please
    if: ${{ needs.release-please.outputs.release_created == 'true' }}
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.RELEASE_PLEASE_TOKEN || secrets.GITHUB_TOKEN }}
          fetch-depth: 0

      - name: Setup Git
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

      - name: Sync Version Files
        run: |
          # Extract version from tag (remove 'v' prefix)
          VERSION="${{ needs.release-please.outputs.tag_name }}"
          VERSION="${VERSION#v}"
          
          # Sync VERSION file
          echo "$VERSION" > VERSION
          
          # Sync tokens.json
          node -e "
            const fs = require('fs');
            const tokens = JSON.parse(fs.readFileSync('tokens.json', 'utf8'));
            tokens.version = '$VERSION';
            fs.writeFileSync('tokens.json', JSON.stringify(tokens, null, 2));
          "
          
          # Sync package.json
          node -e "
            const fs = require('fs');
            const pkg = JSON.parse(fs.readFileSync('package.json', 'utf8'));
            pkg.version = '$VERSION';
            fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
          "
          
          # Run stamp_version.py to sync HTML/MD
          python3 tools/stamp_version.py
          
          git add VERSION tokens.json package.json docs/
          git commit -m "chore(release): sync versions to $VERSION [skip ci]"
          git push

  validate:
    needs: sync-versions
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm install

      - name: Run validators
        run: npm run validate
```

3. **Create PAT secret:**
```bash
# Create a Personal Access Token with repo scope
# Add as secret: RELEASE_PLEASE_TOKEN
```

### Alternative: Custom GitHub Actions Workflow

**If you prefer direct control without PRs:**

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    branches:
      - main
  workflow_dispatch:
    inputs:
      version:
        description: 'Manual version (e.g., 1.2.0)'
        required: false
      prerelease:
        description: 'Prerelease'
        type: boolean
        default: false
      draft:
        description: 'Draft'
        type: boolean
        default: false

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm install

      - name: Generate Changelog
        id: changelog
        uses: TriPSs/conventional-changelog-action@v5
        with:
          github-token: ${{ secrets.github_token }}
          git-message: 'chore(release): {version}'
          preset: 'angular'
          tag-prefix: 'v'
          output-file: 'CHANGELOG.md'
          version-file: './package.json'
          version-path: 'version'
          skip-on-empty: 'false'
          skip-commit: 'false'
          release-count: '10'

      - name: Sync All Version Files
        if: steps.changelog.outputs.skipped == 'false'
        run: |
          NEW_VERSION="${{ steps.changelog.outputs.version }}"
          
          # Sync VERSION
          echo "$NEW_VERSION" > VERSION
          
          # Sync tokens.json
          node -e "
            const fs = require('fs');
            const tokens = JSON.parse(fs.readFileSync('tokens.json', 'utf8'));
            tokens.version = '$NEW_VERSION';
            fs.writeFileSync('tokens.json', JSON.stringify(tokens, null, 2));
          "
          
          # Run stamp_version.py
          python3 tools/stamp_version.py
          
          git add VERSION tokens.json CHANGELOG.md docs/
          git commit -m "chore(release): v$NEW_VERSION"
          git push

      - name: Create Tag
        if: steps.changelog.outputs.skipped == 'false'
        run: |
          git tag "v${{ steps.changelog.outputs.version }}"
          git push origin "v${{ steps.changelog.outputs.version }}"

      - name: Create GitHub Release
        if: steps.changelog.outputs.skipped == 'false'
        uses: ncipollo/release-action@v1
        with:
          tag: "v${{ steps.changelog.outputs.version }}"
          name: "v${{ steps.changelog.outputs.version }}"
          body: ${{ steps.changelog.outputs.clean_changelog }}
          draft: ${{ inputs.draft || false }}
          prerelease: ${{ inputs.prerelease || false }}
          generateReleaseNotes: false
```

---

## 7. Pre-release Strategy

### release-please Pre-release

```yaml
# Branch-based prerelease
branches:
  - main        # Stable releases
  - beta        # Beta releases
  - alpha       # Alpha releases

# Or via config
{
  "packages": {
    ".": {
      "prerelease": true,
      "prerelease-type": "beta"
    }
  }
}
```

### Custom Workflow Pre-release

```yaml
# Manual trigger with prerelease flag
workflow_dispatch:
  inputs:
    prerelease:
      type: boolean
      default: false
```

---

## 8. Emergency Release Support

### release-please

```bash
# CLI for emergency release
npx release-please release-as --version=1.2.3
```

### Custom Workflow

```yaml
# Manual dispatch with version input
workflow_dispatch:
  inputs:
    version:
      required: true
```

---

## 9. Implementation Checklist

### For release-please:

- [ ] Create `release-please-config.json`
- [ ] Create `.github/workflows/release-please.yml`
- [ ] Create PAT with `repo` scope → add as `RELEASE_PLEASE_TOKEN`
- [ ] Test with `workflow_dispatch`
- [ ] Verify three version files sync correctly
- [ ] Update existing `release.yml` to use new workflow
- [ ] Document in CONTRIBUTING.md

### For Custom Workflow:

- [ ] Create `.github/workflows/release.yml`
- [ ] Test conventional commit parsing
- [ ] Verify three version files sync
- [ ] Test manual trigger
- [ ] Test prerelease flag
- [ ] Test draft release
- [ ] Add idempotent release logic
- [ ] Document in CONTRIBUTING.md

---

## 10. References

### Official Documentation

- **release-please:** https://github.com/googleapis/release-please
- **release-please-action:** https://github.com/googleapis/release-please-action
- **semantic-release:** https://github.com/semantic-release/semantic-release
- **Changesets:** https://github.com/changesets/changesets
- **Conventional Commits:** https://www.conventionalcommits.org/
- **Keep a Changelog:** https://keepachangelog.com/

### Real-World Examples

- **googleapis/release-please:** https://github.com/googleapis/release-please
- **static-site-generator (release-please):** https://github.com/sebastienrousseau/static-site-generator
- **gh-secrets (release-please + multi-asset):** https://github.com/nickderobertis/github-secrets
- **semantic-release without npm:** https://github.com/semantic-release/semantic-release/discussions/1967

### GitHub Actions

- **conventional-changelog-action:** https://github.com/TriPSs/conventional-changelog-action
- **ncipollo/release-action:** https://github.com/ncipollo/release-action
- **softprops/action-gh-release:** https://github.com/softprops/action-gh-release
- **ietf-tools/semver-action:** https://github.com/ietf-tools/semver-action

---

## 11. Conclusion

For the **EDIC Design System**, I recommend:

**Primary Choice: release-please with manifest mode**
- Best fit for zero npm dependency
- PR-based workflow provides human review
- Well-maintained by Google
- Supports pre-releases
- Can be extended with version sync script

**Alternative: Custom GitHub Actions workflow**
- Full control over every step
- No intermediate PRs
- Direct integration with existing stamp_version.py
- Better for emergency releases

**Not Recommended:**
- **semantic-release** - Requires Node.js, npm-focused, opinionated auto-release
- **Changesets** - Overkill for single package, npm-focused, manual changeset creation

The choice between release-please and custom workflow depends on whether you prefer:
- **Release PR review** → release-please
- **Direct automation** → Custom workflow

Both can be configured to sync all three version sources (VERSION, tokens.json, package.json) and maintain Keep a Changelog format.