#!/usr/bin/env node
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

const requestedScript = process.argv[2];
const extraArgs = process.argv.slice(3);
if (!requestedScript || requestedScript === "--help") {
  console.error("Usage: node scripts/run-validator.js <validate_*.py | scripts/*.py>");
  process.exit(2);
}
const scriptName = requestedScript.endsWith(".py")
  ? requestedScript
  : `validate_${requestedScript}.py`;
const scriptPath = path.isAbsolute(scriptName)
  ? scriptName
  : path.join(ROOT, scriptName.startsWith("scripts/") ? scriptName : path.join("tools", scriptName));
const pythonCommand = detectPython();
const result = spawnSync(
  pythonCommand[0],
  [...pythonCommand.slice(1), scriptPath, ...extraArgs],
  {
    cwd: ROOT,
    env: { ...process.env, PYTHONIOENCODING: process.env.PYTHONIOENCODING || "utf-8" },
    stdio: "inherit",
  },
);

if (result.error) {
  console.error(`[ERROR] ${scriptName}: ${result.error.message}`);
  process.exit(1);
}
process.exit(result.status === 0 ? 0 : result.status);
