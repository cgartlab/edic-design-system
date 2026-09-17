#!/usr/bin/env node
/**
 * scripts/run-audit.js — EDIC Design System 2.0 audit gate.
 *
 * Aggregates the existing validators, version checks, icon sprite checks,
 * size checks, and Vitest coverage without adding runtime dependencies.
 */

const { spawnSync } = require("node:child_process");

function canRunPython(command, args) {
  try {
    const result = spawnSync(command, [...args, "--version"], {
      encoding: "utf8",
      stdio: ["ignore", "pipe", "pipe"],
      timeout: 3000,
    });
    if (result.error) return false;
    const output = `${result.stdout || ""}${result.stderr || ""}`;
    return result.status === 0 && /Python \d/.test(output);
  } catch {
    return false;
  }
}

function detectPython() {
  const explicit = process.env.PY || process.env.PYTHON;
  if (explicit && canRunPython(explicit, [])) return [explicit];

  const candidates = [];
  if (process.platform === "win32") {
    candidates.push(["py", "-V:Astral/CPython3.12.13"]);
    candidates.push(["py"]);
  }
  candidates.push(["python3"]);
  candidates.push(["python"]);

  for (const commandArgs of candidates) {
    if (canRunPython(commandArgs[0], commandArgs.slice(1))) return commandArgs;
  }
  return process.platform === "win32" ? ["python"] : ["python3"];
}

const PYTHON_COMMAND = detectPython();
const CHILD_ENV = { ...process.env, PYTHONIOENCODING: process.env.PYTHONIOENCODING || "utf-8" };

// release-please 分支/合并提交存在「tokens/package 已 bump 而 VERSION 未同步」的
// 预期过渡态（AGENTS.md §3.1），由 post-merge-stamp 收敛。此时跳过版本相关检查。
const SKIP_VERSION_CHECKS = ["1", "true", "yes"].includes(
  String(process.env.AUDIT_SKIP_VERSION_CHECKS || "").toLowerCase()
);

const CHECKS = [
  ["Version stamp", "python", "stamp_version.py", ["--check"]],
  ["Version sync", "python", "sync_versions.py", ["--check"]],
  ["Validators", "node-script", "scripts/run-validators.js", []],
  ["Icon sprite", "python", "generate_icons.py", ["--check"]],
  ["Visual baseline", "python", "validate_visual_baseline.py", []],
  ["Size budget", "python", "validate_size.py", []],
  ["Changelog", "python", "generate_changelog_html.py", ["--check"]],
  ["Unit tests", "node-script", "node_modules/vitest/vitest.mjs", ["run"]],
];

function effectiveChecks() {
  if (!SKIP_VERSION_CHECKS) return CHECKS;
  // 除 stamp/sync 外，Icon sprite（generate_icons.py --check）也会因 release-please
  // 预 bump 的 icons.json 在过渡态与 VERSION 失配，一并跳过。
  const filtered = CHECKS.filter(
    ([label]) => label !== "Version stamp" && label !== "Version sync" && label !== "Icon sprite"
  );
  console.log("注：AUDIT_SKIP_VERSION_CHECKS 已启用 — 跳过版本 stamp/sync 与 Icon sprite（release-please 过渡态，post-merge-stamp 收敛）。");
  return filtered;
}

function runCheck(label, mode, command, args) {
  console.log(`\n── ${label} ──`);
  let child;
  if (mode === "python") {
    child = spawnSync(PYTHON_COMMAND[0], [...PYTHON_COMMAND.slice(1), `tools/${command}`, ...args], { env: CHILD_ENV, stdio: "inherit" });
  } else if (mode === "node-script") {
    child = spawnSync(process.execPath, [command, ...args], { env: CHILD_ENV, stdio: "inherit", cwd: process.cwd() });
  } else {
    child = spawnSync(command, args, { env: CHILD_ENV, stdio: "inherit", shell: process.platform === "win32" });
  }

  if (child.error) {
    console.error(`[ERROR] ${label}: ${child.error.message}`);
    return 1;
  }

  const code = child.status ?? 0;
  if (code !== 0) {
    console.error(`[ERROR] ${label}: exit code ${code}`);
  }
  if (code === 0) return 0;
  if (code === 2 && label !== "Unit tests") return 2;
  return code;
}

function main() {
  let failed = false;
  let warned = false;

  for (const [label, mode, command, args] of effectiveChecks()) {
    const code = runCheck(label, mode, command, args);
    if (code === 1 || code > 2) failed = true;
    else if (code === 2) warned = true;
  }

  console.log("\n────────────────────");
  if (failed) {
    console.log("✗ Audit failed");
    process.exit(1);
  }
  if (warned) {
    console.log("⚠ Audit passed with warnings");
    process.exit(2);
  }
  console.log("✓ Audit passed");
}

main();
