/**
 * Miscellaneous tests — Year stamp · Icon grid · Token table · Scroll reveal
 */
import { describe, it, expect } from "vitest";
import { resetBody, runScripts } from "./helpers.js";

describe("Year stamp", () => {
  it("fills .ds-year with current year", () => {
    resetBody(`<span class="ds-year"></span>`);
    runScripts();
    expect(document.querySelector(".ds-year").textContent).toBe(
      String(new Date().getFullYear())
    );
  });

  it("fills multiple .ds-year elements", () => {
    resetBody(`<span class="ds-year"></span><span class="ds-year"></span>`);
    runScripts();
    document.querySelectorAll(".ds-year").forEach((el) => {
      expect(el.textContent).toBe(String(new Date().getFullYear()));
    });
  });
});

describe("Icon grid", () => {
  it("renders icons into #icon-grid", () => {
    resetBody(`<div id="icon-grid"></div>`);
    runScripts();
    expect(document.getElementById("icon-grid").children.length).toBeGreaterThan(0);
  });

  it("each icon box has a label span", () => {
    resetBody(`<div id="icon-grid"></div>`);
    runScripts();
    document.querySelectorAll(".ds-icon-box").forEach((box) => {
      expect(box.querySelector("span")).toBeTruthy();
    });
  });

  it("each icon box has title attribute", () => {
    resetBody(`<div id="icon-grid"></div>`);
    runScripts();
    document.querySelectorAll(".ds-icon-box").forEach((box) => {
      expect(box.getAttribute("title")).toBeTruthy();
    });
  });

  it("does nothing when #icon-grid is absent", () => {
    resetBody(`<div></div>`);
    expect(() => runScripts()).not.toThrow();
  });
});

describe("Token table", () => {
  it("renders rows into #token-tbody", () => {
    resetBody(`<table><tbody id="token-tbody"></tbody></table>`);
    runScripts();
    expect(document.querySelectorAll("#token-tbody tr").length).toBeGreaterThan(0);
  });

  it("each row has three cells: name, light value, dark value", () => {
    resetBody(`<table><tbody id="token-tbody"></tbody></table>`);
    runScripts();
    document.querySelectorAll("#token-tbody tr").forEach((row) => {
      expect(row.cells.length).toBe(3);
    });
  });

  it("dark cell shows a value or the inherit placeholder", () => {
    resetBody(`<table><tbody id="token-tbody"></tbody></table>`);
    runScripts();
    const rows = Array.from(document.querySelectorAll("#token-tbody tr"));
    expect(rows.length).toBeGreaterThan(0);
    rows.forEach((row) => {
      const dark = row.cells[2].textContent.trim();
      // 要么是实际暗色值，要么是继承占位符 "—"
      expect(dark === "—" || dark.length > 0).toBe(true);
    });
    // 至少应存在一个真实暗色覆盖值
    const themed = rows.filter((r) => r.cells[2].textContent.trim() !== "—");
    expect(themed.length).toBeGreaterThan(0);
  });

  it("first cell starts with --ds-", () => {
    resetBody(`<table><tbody id="token-tbody"></tbody></table>`);
    runScripts();
    const first = document.querySelector("#token-tbody tr td:first-child");
    expect(first.textContent.startsWith("--ds-")).toBe(true);
  });

  it("does nothing when #token-tbody absent", () => {
    resetBody(`<div></div>`);
    expect(() => runScripts()).not.toThrow();
  });
});

describe("Scroll reveal", () => {
  it("immediately makes elements visible when prefers-reduced-motion", () => {
    window.matchMedia.mockImplementation((q) => ({
      matches: q.includes("reduce"),
      media: q,
      addEventListener: vi.fn(), removeEventListener: vi.fn(),
      addListener: vi.fn(), removeListener: vi.fn(),
    }));

    resetBody(`<div class="ds-reveal">content</div>`);
    runScripts();
    expect(document.querySelector(".ds-reveal").classList.contains("is-visible")).toBe(true);

    window.matchMedia.mockImplementation((q) => ({
      matches: false, media: q,
      addEventListener: vi.fn(), removeEventListener: vi.fn(),
      addListener: vi.fn(), removeListener: vi.fn(),
    }));
  });

  it("does nothing when no .ds-reveal elements present", () => {
    resetBody(`<div>no reveal</div>`);
    expect(() => runScripts()).not.toThrow();
  });
});
