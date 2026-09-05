#!/usr/bin/env node
/**
 * scripts/run-validators.js — 跨平台验证运行器（Node 包装器）
 *
 * 原因：并非所有开发者都装了 Python。用 Node 包装各 Python 验证脚本，
 * 提供统一入口 `npm run validate`。
 *
 * 要求：CI 环境和 Linux/macOS 需 Python 3.11+。Windows 用户可用 WSL。
 *
 * 超时保护：
 *   默认每个验证器 120s 超时（PYTHON_TIMEOUT_MS 可覆盖，非法值报 CLI 用法错误）。
 *   目的：某个 Python 验证器死循环、等 stdin 或崩溃挂起时，不再永久卡住
 *   run-validators.js 或 pre-commit hook（见 issue #229）。
 */

const { spawnSync } = require("node:child_process");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..");
const PYTHON = process.env.PYTHON || (process.platform === "win32" ? "python" : "python3");
const DEFAULT_TIMEOUT_MS = 120_000; // 120s per validator

function parseTimeoutMs() {
  if (!process.env.PYTHON_TIMEOUT_MS) return DEFAULT_TIMEOUT_MS;
  const n = Number(process.env.PYTHON_TIMEOUT_MS);
  if (!Number.isFinite(n) || !Number.isInteger(n) || n < 0) {
    console.error(
      `[run-validators] 非法 PYTHON_TIMEOUT_MS="${process.env.PYTHON_TIMEOUT_MS}"` +
        `（需为非负整数毫秒；0 禁用超时）`,
    );
    process.exit(64); // EX_USAGE
  }
  return n;
}

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
];

const STAMPERS = [
  // validate_versions.py 已经会检测 {{DS_VERSION}} 占位符残留；
  // 单独 stamp --check 用于在 CI 入口最前面快速失败。
  { script: "stamp_version.py", args: ["--check"] },
];

function runOne(script, args = [], timeoutMs) {
  const toolPath = path.join(ROOT, "tools", script);
  const label = args.length ? `${script} ${args.join(" ")}` : script;
  const hasTimeout = timeoutMs > 0;
  const timeoutTag = hasTimeout ? ` (timeout ${timeoutMs}ms)` : " (no timeout)";
  console.log(`\n── ${label}${timeoutTag} ──`);

  // spawnSync `timeout` 选项：到期后 Node 内核用 SIGTERM 杀掉子进程。
  // 16MB maxBuffer 避免 Python 侧异常大输出撑爆 Node 内存。
  // 传入的 timeoutMs 允许为 0（禁用超时），故用 hasTimeout 显式判定。
  const options = {
    stdio: "inherit",
    cwd: ROOT,
    maxBuffer: 16 * 1024 * 1024,
  };
  if (hasTimeout) options.timeout = timeoutMs;

  const result = spawnSync(PYTHON, [toolPath, ...args], options);

  // 超时：明确报超时，返回 "fail"，让 CI/pre-commit 立刻中断（否则卡住到 GitHub job timeout）。
  // Node 版本差异：老版本暴露 result.timedOut=true；v22 起可能只暴露 error.code='ETIMEDOUT' + signal='SIGTERM'。
  // 三种判定方式都检查，保证跨 Node 版本一致。
  const isTimeout =
    result.timedOut === true ||
    result.error?.code === "ETIMEDOUT" ||
    result.signal === "SIGTERM";
  if (isTimeout) {
    console.error(
      `\n[timeout] ${label} 超过 ${timeoutMs}ms，已强制终止 (SIGTERM)。\n` +
        "         排查：该验证器可能死循环、等 stdin 或异常挂起；\n" +
        "         可设 PYTHON_TIMEOUT_MS=<ms> 覆盖（非负整数；0 禁用）。",
    );
    return "fail";
  }

  // Python 缺失或其他 spawn 错误（ENOENT 等）：明确报错，返回 "fail"。
  if (result.error) {
    console.error(`[error] ${label} 无法启动: ${result.error.message}`);
    return "fail";
  }

  return result.status === 0 ? "ok" : result.status === 2 ? "warn" : "fail";
}

function main() {
  console.log("EDIC Design System — 验证运行器");
  console.log("Python:", PYTHON);
  const timeoutMs = parseTimeoutMs();
  console.log(
    `Timeout per validator: ${timeoutMs > 0 ? `${timeoutMs}ms` : "disabled (PYTHON_TIMEOUT_MS=0)"}`,
    "\n",
  );

  let hasFail = false;
  let hasWarn = false;
  for (const { script, args } of STAMPERS) {
    const r = runOne(script, args, timeoutMs);
    if (r === "fail") hasFail = true;
    if (r === "warn") hasWarn = true;
  }
  for (const script of VALIDATORS) {
    const r = runOne(script, [], timeoutMs);
    if (r === "fail") hasFail = true;
    if (r === "warn") hasWarn = true;
  }

  console.log("\n────────────────────");
  if (hasFail) {
    console.log("✗ 部分验证失败");
    process.exit(1);
  } else if (hasWarn) {
    console.log("⚠ 全部通过（有警告）");
    process.exit(2);
  } else {
    console.log("✓ 全部通过");
    process.exit(0);
  }
}

main();
