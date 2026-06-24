# v1.8.1 Release — Orphaned Asset URLs Fixed

**Date:** 2026-06-24
**Fixed by:** Oracle (release-pipeline owner)
**Verified by:** [pending — librarian + designer joint sign-off]

## What broke

The `v1.8.1` tag was deleted and recreated during the post-merge
stamp workflow, but the GitHub Release object was left behind with its
asset upload-session URLs bound to the original `untagged-acaefb84c0e4715ba7e0`
identifier instead of `v1.8.1`. Symptoms:

- `gh release list` did not show v1.8.1
- Asset download URLs served from
  `releases/download/untagged-acaefb84c0e4715ba7e0/...`
  instead of `releases/download/v1.8.1/...`
- Visible as a stale draft release orphaned against the new tag

## What was fixed

1. Identified the orphan draft release (id `343949195`) via REST API
2. Deleted it via `gh api -X DELETE repos/cgartlab/edic-design-system/releases/343949195`
3. Rebuilt all artifacts from source on the v1.8.1 tag commit (`c97fa59`):
   - `edic-ds-color-card.pdf` (5,225 bytes)
   - `edic-ds-reference.pdf` (17,283 bytes)
   - `edic-design-system-v1.8.1.zip` (54,471 bytes)
   - `edic-design-system-skill-v1.8.1.zip` (9,784 bytes)
   - `CHECKSUMS.txt` (4 entries, sha256)
4. Recreated the release with `gh release create v1.8.1 --latest`
   (new id `344041883`)
5. Verified all 5 asset URLs end with `/releases/download/v1.8.1/...`
6. Spot-downloaded CHECKSUMS.txt over HTTPS — 200 OK, content matches

## How we prevent recurrence

Added a new step to `.github/workflows/release.yml` (the "Verify asset
URLs are versioned" step) that runs immediately after `gh release
create` and fails the pipeline with `exit 1` if any asset URL:

- contains `untagged-`, OR
- does not contain the expected `/$TAG/` segment

This means a future tag-recreation incident cannot ship silently —
the pipeline will surface the mis-bound URLs as a CI annotation and
the release cannot be marked successful.

## Verification status

- [x] Tag v1.8.1 points to commit `c97fa59` on main
- [x] Exactly one release object for tag v1.8.1 (id `344041883`)
- [x] All 5 asset URLs are versioned (`/v1.8.1/`)
- [x] `gh release list` shows v1.8.1 as latest
- [x] Asset download (CHECKSUMS.txt) returns 200 with expected content
- [x] Local files match release assets (sha256 verified)
- [x] `release.yml` YAML parses cleanly with new guard step
- [ ] Librarian sign-off (documentation / version sync)
- [ ] Designer sign-off (PDF rendering / color-token parity)