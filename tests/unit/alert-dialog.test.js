/**
 * Alert Dialog (confirmation, focus trap) tests
 */
import { describe, it, expect, beforeEach } from "vitest";
import { resetBody, runScripts, fireClick, fireKey } from "./helpers.js";

function setupDialog() {
  resetBody(`
    <button type="button" class="ds-btn" data-dialog-trigger data-dialog-target="#dlg">打开</button>
    <div class="ds-alert-dialog-backdrop" hidden>
      <div class="ds-alert-dialog" id="dlg" role="alertdialog" aria-modal="true" aria-labelledby="dlg-title">
        <h2 class="ds-alert-dialog-title" id="dlg-title">确认</h2>
        <p class="ds-alert-dialog-desc">描述</p>
        <div class="ds-alert-dialog-actions">
          <button class="ds-btn" type="button" data-dialog-close>取消</button>
          <button class="ds-btn" type="button" data-dialog-close>确定</button>
        </div>
      </div>
    </div>
  `);
  runScripts();
}

describe("Alert Dialog", () => {
  beforeEach(setupDialog);

  it("opens on trigger click", () => {
    const backdrop = document.querySelector(".ds-alert-dialog-backdrop");
    expect(backdrop.hidden).toBe(true);
    fireClick(document.querySelector("[data-dialog-trigger]"));
    expect(backdrop.hidden).toBe(false);
  });

  it("moves focus into the dialog on open", () => {
    fireClick(document.querySelector("[data-dialog-trigger]"));
    expect(document.querySelector("#dlg").contains(document.activeElement)).toBe(true);
  });

  it("closes on close button", () => {
    fireClick(document.querySelector("[data-dialog-trigger]"));
    fireClick(document.querySelector("[data-dialog-close]"));
    expect(document.querySelector(".ds-alert-dialog-backdrop").hidden).toBe(true);
  });

  it("closes on backdrop click", () => {
    fireClick(document.querySelector("[data-dialog-trigger]"));
    fireClick(document.querySelector(".ds-alert-dialog-backdrop"));
    expect(document.querySelector(".ds-alert-dialog-backdrop").hidden).toBe(true);
  });

  it("closes on Escape and restores focus to trigger", () => {
    const trigger = document.querySelector("[data-dialog-trigger]");
    fireClick(trigger);
    fireKey(document.activeElement, "Escape");
    expect(document.querySelector(".ds-alert-dialog-backdrop").hidden).toBe(true);
    expect(document.activeElement).toBe(trigger);
  });

  it("wraps Tab focus from last to first (focus trap)", () => {
    fireClick(document.querySelector("[data-dialog-trigger]"));
    const btns = document.querySelectorAll(".ds-alert-dialog [data-dialog-close]");
    btns[btns.length - 1].focus();
    fireKey(btns[btns.length - 1], "Tab");
    expect(document.activeElement).toBe(btns[0]);
  });

  it("wraps Shift+Tab from first to last (focus trap)", () => {
    fireClick(document.querySelector("[data-dialog-trigger]"));
    const btns = document.querySelectorAll(".ds-alert-dialog [data-dialog-close]");
    btns[0].focus();
    fireKey(btns[0], "Tab", { shiftKey: true });
    expect(document.activeElement).toBe(btns[btns.length - 1]);
  });
});
