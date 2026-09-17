/**
 * Safe localStorage tests
 */
import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { resetBody, runScripts } from "./helpers.js";

function setupStorage() {
  resetBody(`
    <button id="theme-toggle-btn" class="ds-theme-toggle-btn" type="button"
            aria-label="跟随系统 · 点击切换">
      <span class="theme-icon"></span>
    </button>
    <button class="ds-lang-switch-btn" type="button" aria-label="语言：中文">
      <span class="lang-label">中文</span>
    </button>
  `);
  localStorage.clear();
  document.documentElement.removeAttribute("data-theme");
  document.documentElement.removeAttribute("data-theme-mode");
  document.documentElement.lang = "zh-CN";
  runScripts();
}

describe("Safe localStorage", () => {
  beforeEach(setupStorage);
  afterEach(() => {
    vi.restoreAllMocks();
    localStorage.clear();
  });

  it("applies theme and language when localStorage is blocked", () => {
    vi.spyOn(console, "warn").mockImplementation(() => {});
    localStorage.setItem = () => { throw new Error("blocked"); };
    localStorage.getItem = () => { throw new Error("blocked"); };

    expect(() => window.setTheme("dark")).not.toThrow();
    expect(() => window.setLang("en")).not.toThrow();
    expect(document.documentElement.getAttribute("data-theme")).toBe("dark");
    expect(document.documentElement.getAttribute("data-theme-mode")).toBe("dark");
    expect(document.documentElement.lang).toBe("en");
  });
});
