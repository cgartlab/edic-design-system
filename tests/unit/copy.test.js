/**
 * Copy-to-clipboard tests — success, error (Fix B3), selector, TEXTAREA
 */
import { describe, it, expect, beforeEach, vi, afterEach } from "vitest";
import { resetBody, runScripts, fireClick } from "./helpers.js";

function setupCopy(html) {
  resetBody(html);
  runScripts();
}

describe("Copy – success path", () => {
  beforeEach(() => {
    _clipboardWriteText.mockClear();
    _clipboardWriteText.mockResolvedValue(undefined);
    setupCopy(`
      <button data-copy-text="hello world" type="button">
        <span class="ds-copy-label">复制</span>
      </button>
    `);
  });

  it("writes the correct text to clipboard", async () => {
    fireClick(document.querySelector("[data-copy-text]"));
    await new Promise(r => setTimeout(r, 0));
    expect(_clipboardWriteText).toHaveBeenCalledWith("hello world");
  });

  it("adds is-copied class after success", async () => {
    const btn = document.querySelector("[data-copy-text]");
    fireClick(btn);
    await new Promise(r => setTimeout(r, 0));
    expect(btn.classList.contains("is-copied")).toBe(true);
  });

  it("label changes to 已复制 after success", async () => {
    const btn = document.querySelector("[data-copy-text]");
    fireClick(btn);
    await new Promise(r => setTimeout(r, 0));
    expect(btn.querySelector(".ds-copy-label").textContent).toBe("已复制");
  });

  it("label restores to original after timeout", async () => {
    vi.useFakeTimers();
    _clipboardWriteText.mockResolvedValue(undefined);
    setupCopy(`
      <button data-copy-text="hello world" type="button">
        <span class="ds-copy-label">复制</span>
      </button>
    `);
    fireClick(document.querySelector("[data-copy-text]"));
    await Promise.resolve();
    vi.advanceTimersByTime(2000);
    expect(document.querySelector(".ds-copy-label").textContent).toBe("复制");
    vi.useRealTimers();
  });
});

describe("Copy – data-copy selector", () => {
  beforeEach(() => { _clipboardWriteText.mockClear(); });

  it("reads text from target element", async () => {
    _clipboardWriteText.mockResolvedValue(undefined);
    setupCopy(`
      <pre id="code-block">const x = 1;</pre>
      <button data-copy="#code-block" type="button">
        <span class="ds-copy-label">复制</span>
      </button>
    `);
    fireClick(document.querySelector("[data-copy]"));
    await new Promise(r => setTimeout(r, 0));
    expect(_clipboardWriteText).toHaveBeenCalledWith("const x = 1;");
  });

  it("does nothing when selector matches nothing", async () => {
    _clipboardWriteText.mockResolvedValue(undefined);
    setupCopy(`
      <button data-copy="#nonexistent" type="button">
        <span class="ds-copy-label">复制</span>
      </button>
    `);
    fireClick(document.querySelector("[data-copy]"));
    await new Promise(r => setTimeout(r, 0));
    expect(_clipboardWriteText).not.toHaveBeenCalled();
  });
});

describe("Copy – error path (Fix B3)", () => {
  beforeEach(() => {
    _clipboardWriteText.mockClear();
    _clipboardWriteText.mockRejectedValue(new Error("denied"));
    setupCopy(`
      <button data-copy-text="test" type="button">
        <span class="ds-copy-label">复制</span>
      </button>
    `);
  });

  afterEach(() => { vi.useRealTimers(); });

  it("adds is-error class on clipboard failure", async () => {
    const btn = document.querySelector("[data-copy-text]");
    fireClick(btn);
    await Promise.resolve(); await Promise.resolve();
    expect(btn.classList.contains("is-error")).toBe(true);
  });

  it("label changes to 复制失败 on error", async () => {
    fireClick(document.querySelector("[data-copy-text]"));
    await Promise.resolve(); await Promise.resolve();
    expect(document.querySelector(".ds-copy-label").textContent).toBe("复制失败");
  });

  it("[B3] label restores to original after error timeout — no ReferenceError", async () => {
    /**
     * Previously .catch() referenced `label` and `original` that were only
     * declared inside .then() — a ReferenceError that silently swallowed the
     * restore timeout, leaving the button stuck on "复制失败" forever.
     * Fix: hoist both vars before the then/catch split.
     */
    vi.useFakeTimers();
    fireClick(document.querySelector("[data-copy-text]"));
    await Promise.resolve(); await Promise.resolve();
    expect(document.querySelector(".ds-copy-label").textContent).toBe("复制失败");
    expect(() => vi.advanceTimersByTime(3000)).not.toThrow();
    expect(document.querySelector(".ds-copy-label").textContent).toBe("复制");
  });

  it("[B3] is-error class is removed after error timeout", async () => {
    vi.useFakeTimers();
    const btn = document.querySelector("[data-copy-text]");
    fireClick(btn);
    await Promise.resolve(); await Promise.resolve();
    vi.advanceTimersByTime(3000);
    expect(btn.classList.contains("is-error")).toBe(false);
  });
});

describe("Copy – TEXTAREA source", () => {
  it("reads .value from TEXTAREA", async () => {
    _clipboardWriteText.mockClear();
    _clipboardWriteText.mockResolvedValue(undefined);
    setupCopy(`
      <textarea id="ta">textarea value</textarea>
      <button data-copy="#ta" type="button">
        <span class="ds-copy-label">复制</span>
      </button>
    `);
    fireClick(document.querySelector("[data-copy]"));
    await new Promise(r => setTimeout(r, 0));
    expect(_clipboardWriteText).toHaveBeenCalledWith("textarea value");
  });
});

describe("Copy – execCommand fallback (no Clipboard API)", () => {
  beforeEach(() => {
    _clipboardWriteText.mockClear();
    setupCopy(`
      <button data-copy-text="fallback text" type="button">
        <span class="ds-copy-label">复制</span>
      </button>
    `);
  });

  afterEach(() => {
    if (window._origClipboard !== undefined) {
      navigator.clipboard = window._origClipboard;
      window._origClipboard = undefined;
    }
  });

  it("copies via execCommand when navigator.clipboard is unavailable (http:// preview)", async () => {
    window._origClipboard = navigator.clipboard;
    navigator.clipboard = undefined;
    const origExec = document.execCommand;
    document.execCommand = vi.fn(() => true);
    try {
      const btn = document.querySelector("[data-copy-text]");
      fireClick(btn);
      await new Promise(r => setTimeout(r, 0));
      expect(document.execCommand).toHaveBeenCalledWith("copy");
      expect(btn.classList.contains("is-copied")).toBe(true);
      expect(document.querySelector(".ds-copy-label").textContent).toBe("已复制");
      expect(_clipboardWriteText).not.toHaveBeenCalled();
    } finally {
      document.execCommand = origExec;
    }
  });

  it("marks failure when execCommand returns false", async () => {
    window._origClipboard = navigator.clipboard;
    navigator.clipboard = undefined;
    const origExec = document.execCommand;
    document.execCommand = vi.fn(() => false);
    try {
      fireClick(document.querySelector("[data-copy-text]"));
      await Promise.resolve(); await Promise.resolve();
      expect(document.querySelector(".ds-copy-label").textContent).toBe("复制失败");
    } finally {
      document.execCommand = origExec;
    }
  });
});
