/**
 * File Upload (drag-drop + file list) tests
 */
import { describe, it, expect, beforeEach } from "vitest";
import { resetBody, runScripts, fire, fireClick } from "./helpers.js";

function setupUpload() {
  resetBody(`
    <div class="ds-file-upload">
      <div class="ds-file-upload-drop" tabindex="0" role="button">
        <p>点击选择或拖拽文件</p>
        <input class="ds-file-upload-input" type="file" multiple hidden />
      </div>
      <p class="ds-file-upload-status ds-sr-only" aria-live="polite"></p>
      <ul class="ds-file-upload-list"></ul>
    </div>
  `);
  runScripts();
}

function fakeFile(name, size) {
  return { name: name, size: size };
}

describe("File Upload", () => {
  beforeEach(setupUpload);

  it("adds files to the list on input change", () => {
    const input = document.querySelector(".ds-file-upload-input");
    Object.defineProperty(input, "files", { value: [fakeFile("a.txt", 100)], configurable: true });
    fire(input, "change");
    const items = document.querySelectorAll(".ds-file-upload-item");
    expect(items.length).toBe(1);
    expect(items[0].querySelector(".ds-file-upload-name").textContent).toBe("a.txt");
  });

  it("adds files on drop", () => {
    const drop = document.querySelector(".ds-file-upload-drop");
    const dt = { files: [fakeFile("b.png", 2048)] };
    const evt = new Event("drop", { bubbles: true, cancelable: true });
    evt.dataTransfer = dt;
    drop.dispatchEvent(evt);
    const items = document.querySelectorAll(".ds-file-upload-item");
    expect(items.length).toBe(1);
    expect(items[0].querySelector(".ds-file-upload-name").textContent).toBe("b.png");
  });

  it("toggles dragover class", () => {
    const drop = document.querySelector(".ds-file-upload-drop");
    fire(drop, "dragover");
    expect(drop.classList.contains("is-dragover")).toBe(true);
    fire(drop, "dragleave");
    expect(drop.classList.contains("is-dragover")).toBe(false);
  });

  it("removes a file via remove button", () => {
    const input = document.querySelector(".ds-file-upload-input");
    Object.defineProperty(input, "files", { value: [fakeFile("c.md", 10)], configurable: true });
    fire(input, "change");
    expect(document.querySelectorAll(".ds-file-upload-item").length).toBe(1);
    fireClick(document.querySelector(".ds-file-upload-remove"));
    expect(document.querySelectorAll(".ds-file-upload-item").length).toBe(0);
  });

  it("announces added count via aria-live status", () => {
    const input = document.querySelector(".ds-file-upload-input");
    Object.defineProperty(input, "files", { value: [fakeFile("a.txt", 100), fakeFile("b.txt", 200)], configurable: true });
    fire(input, "change");
    expect(document.querySelector(".ds-file-upload-status").textContent).toContain("2");
  });
});
