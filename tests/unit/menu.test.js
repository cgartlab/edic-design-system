/**
 * Menu (WAI-ARIA dropdown) tests
 */
import { describe, it, expect, beforeEach } from "vitest";
import { resetBody, runScripts, fireClick, fireKey } from "./helpers.js";

function setupMenu() {
  resetBody(`
    <div class="ds-menu-wrap">
      <button type="button" class="ds-btn ds-btn--secondary" data-menu-trigger data-menu-target="#menu-test" aria-haspopup="menu" aria-expanded="false">操作</button>
      <div class="ds-menu" id="menu-test" role="menu" data-menu hidden>
        <button class="ds-menu-item" type="button" role="menuitem">编辑</button>
        <button class="ds-menu-item" type="button" role="menuitem">复制</button>
        <div class="ds-menu-divider" role="separator"></div>
        <button class="ds-menu-item ds-menu-item--danger" type="button" role="menuitem">删除</button>
      </div>
    </div>
    <button id="outside" type="button">外部</button>
  `);
  runScripts();
}

describe("Menu", () => {
  beforeEach(setupMenu);

  it("opens on trigger click (hidden=false, aria-expanded=true)", () => {
    const trigger = document.querySelector("[data-menu-trigger]");
    const menu = document.querySelector("#menu-test");
    expect(menu.hidden).toBe(true);
    fireClick(trigger);
    expect(menu.hidden).toBe(false);
    expect(trigger.getAttribute("aria-expanded")).toBe("true");
  });

  it("moves focus to the first enabled item on open", () => {
    const trigger = document.querySelector("[data-menu-trigger]");
    fireClick(trigger);
    const items = document.querySelectorAll(".ds-menu-item");
    expect(document.activeElement).toBe(items[0]);
  });

  it("closes on outside click", () => {
    const trigger = document.querySelector("[data-menu-trigger]");
    fireClick(trigger);
    fireClick(document.querySelector("#outside"));
    expect(document.querySelector("#menu-test").hidden).toBe(true);
    expect(trigger.getAttribute("aria-expanded")).toBe("false");
  });

  it("navigates items with ArrowDown and wraps around", () => {
    const trigger = document.querySelector("[data-menu-trigger]");
    fireClick(trigger);
    const items = document.querySelectorAll(".ds-menu-item");
    fireKey(document.activeElement, "ArrowDown");
    expect(document.activeElement).toBe(items[1]);
    fireKey(document.activeElement, "ArrowDown");
    expect(document.activeElement).toBe(items[2]);
    fireKey(document.activeElement, "ArrowDown");
    expect(document.activeElement).toBe(items[0]);
  });

  it("navigates backward with ArrowUp", () => {
    const trigger = document.querySelector("[data-menu-trigger]");
    fireClick(trigger);
    const items = document.querySelectorAll(".ds-menu-item");
    fireKey(document.activeElement, "ArrowUp");
    expect(document.activeElement).toBe(items[items.length - 1]);
  });

  it("closes and restores focus to trigger on Escape", () => {
    const trigger = document.querySelector("[data-menu-trigger]");
    fireClick(trigger);
    expect(document.querySelector("#menu-test").hidden).toBe(false);
    fireKey(document.activeElement, "Escape");
    expect(document.querySelector("#menu-test").hidden).toBe(true);
    expect(document.activeElement).toBe(trigger);
  });
});
