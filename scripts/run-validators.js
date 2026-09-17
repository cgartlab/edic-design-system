#!/usr/bin/env node
/**
 * scripts/run-validators.js — 跨平台验证运行器（Node 包装器）
 *
 * 原因：并非所有开发者都装了 Python。用 Node 包装各 Python 验证脚本，
 * 提供统一入口 `npm run validate`。
 *
 * 要求：CI 环境和 Linux/macOS 需 Python 3.11+。Windows 用户可用 WSL。
 */

const { spawnSync } = require("node:child_process");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..");

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
    candidates.push(["py", ["-V:Astral/CPython3.12.13"]]);
    candidates.push(["py", ["--version"]]);
  }
  candidates.push(["python3", []]);
  candidates.push(["python", []]);

  for (const commandArgs of candidates) {
    if (canRunPython(commandArgs[0], commandArgs.slice(1))) return commandArgs;
  }
  return process.platform === "win32" ? ["python"] : ["python3"];
}

const PYTHON_COMMAND = detectPython();
const CHILD_ENV = { ...process.env, PYTHONIOENCODING: process.env.PYTHONIOENCODING || "utf-8" };

const VALIDATORS = [
  "validate_tokens.py",
  "validate_naming.py",
  "validate_html.py",
  "validate_a11y.py",
  "validate_versions.py",
  "validate_links.py",
  "validate_cssref.py",
  "validate_darkmode.py",
  "validate_verext.py",
  "validate_hardcode.py",
  "validate_manifest.py",
  "validate_manifest_css.py",
  "validate_components.py",
  "validate_icons.py",
  "validate_visual_baseline.py",
];

const STAMPERS = [
  // validate_versions.py 已经会检测 {{DS_VERSION}} 占位符残留；
  // 单独 stamp --check 用于在 CI 入口最前面快速失败。
  { script: "stamp_version.py", args: ["--check"] },
];

// release-please 分支/合并提交存在「tokens/package 已 bump 而 VERSION 未同步」的
// 预期过渡态（AGENTS.md §3.1），由 post-merge-stamp 收敛。此时跳过版本相关校验。
const SKIP_VERSION_CHECKS = ["1", "true", "yes"].includes(
  String(process.env.AUDIT_SKIP_VERSION_CHECKS || "").toLowerCase()
);

function effectiveValidators() {
  return SKIP_VERSION_CHECKS
    ? VALIDATORS.filter((s) => s !== "validate_versions.py" && s !== "validate_verext.py")
    : VALIDATORS;
}

function effectiveStampers() {
  return SKIP_VERSION_CHECKS ? [] : STAMPERS;
}

function runOne(script, args = []) {
  const toolPath = path.join(ROOT, "tools", script);
  const label = args.length ? `${script} ${args.join(" ")}` : script;
  console.log(`\n-- ${label} --`);
  const result = spawnSync(PYTHON_COMMAND[0], [...PYTHON_COMMAND.slice(1), toolPath, ...args], {
    encoding: "utf8",
    env: CHILD_ENV,
    stdio: ["ignore", "pipe", "pipe"],
    cwd: ROOT,
  });

  if (result.stdout) process.stdout.write(result.stdout);
  if (result.stderr) process.stderr.write(result.stderr);

  if (result.error) {
    console.error(`[ERROR] ${label}: ${result.error.message}`);
    return "fail";
  }
  if (result.status !== 0 && !result.stdout && !result.stderr) {
    console.error(`[ERROR] ${label}: exit code ${result.status}`);
  }
  return result.status === 0 ? "ok" : result.status === 2 ? "warn" : "fail";
}

function main() {
  console.log("EDIC Design System — 验证运行器");
  console.log("Python:", PYTHON_COMMAND.join(" "), "\n");

  let hasFail = false;
  let hasWarn = false;
  if (SKIP_VERSION_CHECKS) {
    console.log("注：AUDIT_SKIP_VERSION_CHECKS 已启用 — 跳过版本校验器 validate-versions/validate-verext 与 stamp 检查（release-please 过渡态）。");
  }
  for (const { script, args } of effectiveStampers()) {
    const r = runOne(script, args);
    if (r === "fail") hasFail = true;
    if (r === "warn") hasWarn = true;
  }
  for (const script of effectiveValidators()) {
    const r = runOne(script);
    if (r === "fail") hasFail = true;
    if (r === "warn") hasWarn = true;
  }

  console.log("\n----------------------");
  if (hasFail) {
    console.log("x 部分验证失败");
    process.exit(1);
  } else if (hasWarn) {
    console.log("! 全部通过（有警告）");
    process.exit(2);
  } else {
    console.log("v 全部通过");
    process.exit(0);
  }
}

main();
