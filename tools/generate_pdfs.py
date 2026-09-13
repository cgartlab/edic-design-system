#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate real, downloadable sample PDFs for the EDIC Design System.

No third-party dependencies: this writes valid PDF 1.7 by hand (Helvetica /
Helvetica-Bold / Courier built-in fonts + filled rectangles for swatches).
Text is ASCII (token names + OKLch values), which suits a reference card.

Capability: This script generates token/color REFERENCE CARDS only (ASCII text +
swatches). It does NOT perform full HTML → PDF rendering. For full-page PDF
generation from HTML templates, consider upgrading to WeasyPrint as an optional
dependency (pip install weasyprint), then call:
    from weasyprint import HTML, CSS
    HTML('handbook.html').write_pdf('handbook.pdf', stylesheets=['styles.css'])

版本号：页脚中显示的 "vX.Y.Z" 从仓库根目录的 VERSION 文件读取
（由 stamp_version.py 与 HTML/MD 文件保持一致）。

Outputs (relative to repo root):
    assets/downloads/edic-ds-reference.pdf   (multi-page reference)
    assets/downloads/edic-ds-color-card.pdf  (one-page color card)

Run:  python tools/generate_pdfs.py
"""

import math
import os

A4_W, A4_H = 595.28, 841.89  # points

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION_FILE = os.path.join(ROOT, "VERSION")


def read_version() -> str:
    """从仓库根目录的 VERSION 文件读取当前版本号。失败则报错。"""
    try:
        with open(VERSION_FILE, "r", encoding="utf-8") as f:
            text = f.read().strip().splitlines()[0].strip()
            if not text:
                raise ValueError("VERSION 文件为空")
            return text
    except OSError as e:
        raise RuntimeError(f"无法读取 VERSION 文件: {e}") from e
    except ValueError as e:
        raise RuntimeError(f"VERSION 文件格式错误: {e}") from e


VERSION = read_version()

# ---- OKLch palette (values from tokens.json) ----
# Each entry is an "oklch(L C h)" string where L is lightness [0..1],
# C is chroma, h is hue in degrees.
OKLCH = {
    "bg":             "oklch(0.97 0.012 80)",
    "surface":        "oklch(0.99 0.005 80)",
    "surface-raised": "oklch(1.00 0.000 0)",
    "border":         "oklch(0.89 0.012 80)",
    "border-strong":  "oklch(0.82 0.015 75)",
    "muted":          "oklch(0.48 0.015 60)",
    "fg-subtle":      "oklch(0.35 0.018 60)",
    "fg":             "oklch(0.20 0.020 60)",
    "fg-strong":      "oklch(0.14 0.025 60)",
    "olive-50":       "oklch(0.90 0.025 115)",
    "olive-100":      "oklch(0.82 0.035 115)",
    "olive-200":      "oklch(0.72 0.050 115)",
    "olive-300":      "oklch(0.62 0.065 115)",
    "olive-400":      "oklch(0.52 0.080 115)",
    "olive-500":      "oklch(0.45 0.085 115)",
    "olive-600":      "oklch(0.38 0.080 115)",
    "olive-700":      "oklch(0.30 0.070 115)",
    "olive-800":      "oklch(0.22 0.055 115)",
    "olive-900":      "oklch(0.15 0.040 115)",
    "success":        "oklch(0.55 0.100 145)",
    "warning":        "oklch(0.65 0.100 85)",
    "error":          "oklch(0.50 0.140 30)",
    "info":           "oklch(0.55 0.080 240)",
}


def _parse_oklch(s: str):
    """Parse 'oklch(L C h)' string into (L, C, h_deg) tuple of floats."""
    s = s.strip()
    # strip oklch(...)
    inner = s[s.index("(") + 1:s.index(")")]
    parts = inner.split()
    return float(parts[0]), float(parts[1]), float(parts[2])


def oklch_to_srgb(L: float, C: float, h: float):
    """Convert OKLch to gamma-corrected sRGB, each channel in [0..1].

    Implements the OKLch → OKLab → Linear sRGB → Gamma sRGB pipeline
    using the matrices published by Björn Ottosson.
    """
    # 1. OKLch → OKLab
    h_rad = math.radians(h)
    a = C * math.cos(h_rad)
    b = C * math.sin(h_rad)

    # 2. OKLab → LMS' (cube-root space)
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b

    # 3. Cube → Linear LMS
    l = l_ * l_ * l_
    m = m_ * m_ * m_
    s = s_ * s_ * s_

    # 4. LMS → Linear sRGB (inverse of M1)
    r_lin = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g_lin = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b_lin = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s

    # 5. Gamma encoding (sRGB piecewise)
    def gamma_encode(v: float) -> float:
        v = max(0.0, min(1.0, v))  # clamp out-of-gamut values
        if v <= 0.0031308:
            return 12.92 * v
        return 1.055 * (v ** (1.0 / 2.4)) - 0.055

    return (gamma_encode(r_lin), gamma_encode(g_lin), gamma_encode(b_lin))


# Compute RGB lookup from the canonical OKLCH values.
# 'white' is a special case (pure white has no OKLch representation beyond
# oklch(100% 0 0) which already resolves to (1,1,1)).
RGB = {}
for _key, _oklch_str in OKLCH.items():
    RGB[_key] = oklch_to_srgb(*_parse_oklch(_oklch_str))
RGB["white"] = (1.0, 1.0, 1.0)


def esc(s):
    return s.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")


class Page:
    def __init__(self, w=A4_W, h=A4_H):
        self.w, self.h = w, h
        self.ops = []

    def rect(self, x, y, w, h, color, fill=True, line_w=1.0):
        r, g, b = color
        if fill:
            self.ops.append(f"{r:.4f} {g:.4f} {b:.4f} rg")
            self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re f")
        else:
            self.ops.append(f"{r:.4f} {g:.4f} {b:.4f} RG")
            self.ops.append(f"{line_w:.2f} w")
            self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re S")

    def line(self, x1, y1, x2, y2, color, line_w=1.0):
        r, g, b = color
        self.ops.append(f"{r:.4f} {g:.4f} {b:.4f} RG")
        self.ops.append(f"{line_w:.2f} w")
        self.ops.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def text(self, x, y_top, s, font="F1", size=10, color=RGB["fg"]):
        # y_top measured from the top of the page
        r, g, b = color
        y = self.h - y_top
        self.ops.append("BT")
        self.ops.append(f"/{font} {size:.2f} Tf")
        self.ops.append(f"{r:.4f} {g:.4f} {b:.4f} rg")
        self.ops.append(f"1 0 0 1 {x:.2f} {y:.2f} Tm")
        self.ops.append(f"({esc(s)}) Tj")
        self.ops.append("ET")

    def swatch_row(self, x, y_top, name, value, color, w=150, h=22, ring=False):
        y = self.h - y_top - h
        r, g, b = color
        self.ops.append(f"{r:.4f} {g:.4f} {b:.4f} rg")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re f")
        br, bg, bb = RGB["border-strong"]
        self.ops.append(f"{br:.4f} {bg:.4f} {bb:.4f} RG")
        self.ops.append("0.6 w")
        self.ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re S")
        if ring:
            ar, ag, ab = RGB["olive-500"]
            self.ops.append(f"{ar:.4f} {ag:.4f} {ab:.4f} RG")
            self.ops.append("1.4 w")
            self.ops.append(f"{x-2:.2f} {y-2:.2f} {w+4:.2f} {h+4:.2f} re S")
        self.text(x + w + 12, y_top + 9, name, "F2", 9.5, RGB["fg-strong"])
        self.text(x + w + 12, y_top + 19, value, "F3", 8, RGB["muted"])

    def stream(self):
        return ("\n".join(self.ops)).encode("latin-1")


class PDFDoc:
    def __init__(self):
        self.pages = []

    def add_page(self, p):
        self.pages.append(p)

    def build(self):
        P = len(self.pages)
        # numbering: 1 catalog, 2 pages, 3 F1, 4 F2, 5 F3,
        # then per page: content(6+2i), page(7+2i)
        page_nums = [7 + 2 * i for i in range(P)]
        objects = []  # (num, body bytes)

        objects.append((1, b"<< /Type /Catalog /Pages 2 0 R >>"))
        kids = " ".join(f"{n} 0 R" for n in page_nums)
        objects.append((2, f"<< /Type /Pages /Count {P} /Kids [{kids}] >>".encode()))
        objects.append((3, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"))
        objects.append((4, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>"))
        objects.append((5, b"<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>"))
        for i, pg in enumerate(self.pages):
            cnum = 6 + 2 * i
            pnum = 7 + 2 * i
            data = pg.stream()
            content = (f"<< /Length {len(data)} >>\nstream\n".encode()
                       + data + b"\nendstream")
            objects.append((cnum, content))
            page_body = (
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {pg.w:.2f} {pg.h:.2f}] "
                f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R >> >> "
                f"/Contents {cnum} 0 R >>"
            ).encode()
            objects.append((pnum, page_body))

        objects.sort(key=lambda o: o[0])
        out = b"%PDF-1.7\n%\xe2\xe3\xcf\xd3\n"
        offsets = {}
        for num, body in objects:
            offsets[num] = len(out)
            out += f"{num} 0 obj\n".encode() + body + b"\nendobj\n"
        xref_pos = len(out)
        total = len(objects) + 1
        out += f"xref\n0 {total}\n".encode()
        out += b"0000000000 65535 f \n"
        for num in range(1, total):
            out += f"{offsets[num]:010d} 00000 n \n".encode()
        out += (f"trailer\n<< /Size {total} /Root 1 0 R >>\n"
                f"startxref\n{xref_pos}\n%%EOF").encode()
        return out


def header(p, title, subtitle):
    p.rect(0, p.h - 96, p.w, 96, RGB["olive-400"])
    p.text(56, 46, title, "F2", 22, RGB["white"])
    p.text(56, 70, subtitle, "F3", 9.5, RGB["olive-50"])
    # leaf glyph hint
    p.text(p.w - 90, 58, "EDIC", "F2", 11, RGB["white"])


def footer(p, page_label):
    p.line(56, 40, p.w - 56, 40, RGB["border"], 0.6)
    p.text(56, 36, f"EDIC Design System  -  Editorial x Olive Green  -  v{VERSION}", "F3", 7.5, RGB["muted"])
    p.text(p.w - 110, 36, page_label, "F3", 7.5, RGB["muted"])


def build_reference():
    doc = PDFDoc()

    # ---- Page 1: cover ----
    p = Page()
    p.rect(0, 0, p.w, p.h, RGB["bg"])
    p.rect(0, p.h - 280, p.w, 280, RGB["olive-400"])
    p.rect(56, p.h - 150, 64, 64, RGB["white"])
    p.text(70, 120, "CG", "F2", 30, RGB["olive-500"])
    p.text(56, 200, "EDIC", "F2", 40, RGB["white"])
    p.text(56, 244, "Design System", "F2", 40, RGB["olive-50"])
    p.text(56, 300, "Editorial x Olive Green  -  Quick Reference", "F3", 12, RGB["fg-strong"])
    p.text(56, 330, "OKLch tokens / dark-mode ready / framework-agnostic", "F1", 11, RGB["muted"])

    p.text(56, 430, "WHAT'S INSIDE", "F2", 10, RGB["olive-500"])
    items = [
        "01  Color tokens - neutral, olive ramp, semantic",
        "02  Typography - families and type scale",
        "03  Spacing, radius and shadow scales",
        "04  Component class catalog",
    ]
    yy = 456
    for it in items:
        p.text(56, yy, it, "F1", 11, RGB["fg"])
        yy += 26

    p.text(56, 690, "200+ design tokens   -   39 components   -   209 icons", "F2", 11, RGB["olive-600"])
    p.text(56, 712, "edic.cgartlab.com", "F3", 10, RGB["muted"])
    footer(p, "Page 1 / 4")
    doc.add_page(p)

    # ---- Page 2: colors ----
    p = Page()
    p.rect(0, 0, p.w, p.h, RGB["bg"])
    header(p, "01  Color Tokens", "All colors defined in OKLch for perceptual uniformity")
    y = 130
    p.text(56, y, "NEUTRAL", "F2", 10, RGB["olive-500"]); y += 16
    neutrals = [
        ("--ds-color-bg", OKLCH["bg"], RGB["bg"]),
        ("--ds-color-surface-raised", OKLCH["surface-raised"], RGB["surface-raised"]),
        ("--ds-color-border", OKLCH["border"], RGB["border"]),
        ("--ds-color-muted", OKLCH["muted"], RGB["muted"]),
        ("--ds-color-fg", OKLCH["fg"], RGB["fg"]),
        ("--ds-color-fg-strong", OKLCH["fg-strong"], RGB["fg-strong"]),
    ]
    for name, val, col in neutrals:
        p.swatch_row(56, y, name, val, col)
        y += 30
    y += 8
    p.text(56, y, "OLIVE GREEN  (accent = olive-400)", "F2", 10, RGB["olive-500"]); y += 16
    olive = [
        ("--ds-color-olive-100", OKLCH["olive-100"], RGB["olive-100"], False),
        ("--ds-color-olive-300", OKLCH["olive-300"], RGB["olive-300"], False),
        ("--ds-color-olive-400  *", OKLCH["olive-400"], RGB["olive-400"], True),
        ("--ds-color-olive-600", OKLCH["olive-600"], RGB["olive-600"], False),
        ("--ds-color-olive-800", OKLCH["olive-800"], RGB["olive-800"], False),
    ]
    for name, val, col, ring in olive:
        p.swatch_row(56, y, name, val, col, ring=ring)
        y += 30
    # second column: semantic
    y2 = 146
    p.text(320, y2, "SEMANTIC", "F2", 10, RGB["olive-500"]); y2 += 16
    sem = [
        ("--ds-color-success", OKLCH["success"], RGB["success"]),
        ("--ds-color-warning", OKLCH["warning"], RGB["warning"]),
        ("--ds-color-error", OKLCH["error"], RGB["error"]),
        ("--ds-color-info", OKLCH["info"], RGB["info"]),
    ]
    for name, val, col in sem:
        p.swatch_row(320, y2, name, val, col, w=120)
        y2 += 30
    footer(p, "Page 2 / 4")
    doc.add_page(p)

    # ---- Page 3: typography ----
    p = Page()
    p.rect(0, 0, p.w, p.h, RGB["bg"])
    header(p, "02  Typography", "Serif display + sans body + mono code")
    y = 134
    p.text(56, y, "FONT FAMILIES", "F2", 10, RGB["olive-500"]); y += 22
    fams = [
        ("Display", "Iowan Old Style / Charter / Georgia / serif"),
        ("Body & UI", "Noto Sans SC / -apple-system / system-ui / sans-serif"),
        ("Mono", "JetBrains Mono / IBM Plex Mono / monospace"),
    ]
    for role, stack in fams:
        p.text(56, y, role, "F2", 10.5, RGB["fg-strong"])
        p.text(150, y, stack, "F3", 9, RGB["muted"])
        y += 22
    y += 14
    p.text(56, y, "TYPE SCALE (rem)", "F2", 10, RGB["olive-500"]); y += 24
    scale = [
        ("hero", "4.5", 26), ("display", "3.75", 23), ("h1", "3", 20),
        ("h2", "2.25", 17), ("h3", "1.875", 15), ("h4", "1.5", 13),
        ("lead", "1.25", 12), ("body", "1", 11), ("body-sm", "0.875", 10),
        ("caption", "0.75", 9),
    ]
    for name, rem, sz in scale:
        p.text(56, y, "Editorial Olive", "F2", sz, RGB["fg"])
        p.text(360, y, f"--ds-text-{name}", "F3", 9, RGB["muted"])
        p.text(500, y, f"{rem} rem", "F3", 9, RGB["olive-600"])
        y += sz + 9
    footer(p, "Page 3 / 4")
    doc.add_page(p)

    # ---- Page 4: spacing + components ----
    p = Page()
    p.rect(0, 0, p.w, p.h, RGB["bg"])
    header(p, "03 / 04  Spacing & Components", "4px base scale + class catalog")
    y = 134
    p.text(56, y, "SPACING SCALE (4px base)", "F2", 10, RGB["olive-500"]); y += 20
    for tok, px in [("space-1", 4), ("space-2", 8), ("space-3", 12), ("space-4", 16),
                    ("space-6", 24), ("space-8", 32), ("space-12", 48), ("space-16", 64)]:
        p.rect(150, p.h - (y + 9), px, 10, RGB["olive-300"])
        p.text(56, y + 8, f"--ds-{tok}", "F3", 8.5, RGB["muted"])
        p.text(150 + px + 8, y + 8, f"{px}px", "F3", 8.5, RGB["fg"])
        y += 18
    y += 10
    p.text(56, y, "RADIUS", "F2", 10, RGB["olive-500"]); y += 16
    p.text(56, y, "sm 2  -  md 4  -  lg 8  -  xl 12  -  2xl 16  -  full", "F3", 9, RGB["fg"]); y += 20
    p.text(56, y, "SHADOW", "F2", 10, RGB["olive-500"]); y += 16
    p.text(56, y, "xs  -  sm  -  md  -  lg  -  xl  -  2xl", "F3", 9, RGB["fg"]); y += 28

    p.text(56, y, "COMPONENT CLASS CATALOG", "F2", 10, RGB["olive-500"]); y += 20
    cats = [
        ("Buttons", "ds-btn  --primary / --secondary / --ghost  --sm / --lg"),
        ("Cards", "ds-card  --hoverable / --flat   ds-glass-card"),
        ("Forms", "ds-input  ds-label  ds-select  ds-toggle  ds-form-*"),
        ("Feedback", "ds-badge--*  ds-alert--*  ds-toast"),
        ("Navigation", "ds-navbar  ds-tabs/ds-tab  ds-breadcrumb  ds-pagination"),
        ("Data", "ds-table  ds-progress  ds-avatar  ds-chip"),
        ("Type", "ds-display  ds-h1..h4  ds-caption  ds-eyebrow  ds-lead"),
        ("Motion", "ds-reveal (--left/--right/--scale)  ds-anim-float"),
    ]
    for role, cls in cats:
        p.text(56, y, role, "F2", 9.5, RGB["fg-strong"])
        p.text(150, y, cls, "F3", 8.5, RGB["muted"])
        y += 18
    footer(p, "Page 4 / 4")
    doc.add_page(p)

    return doc.build()


def build_color_card():
    doc = PDFDoc()
    p = Page()
    p.rect(0, 0, p.w, p.h, RGB["bg"])
    header(p, "Color Card", "OKLch palette - EDIC Design System")
    # big olive ramp
    y = 130
    p.text(56, y, "OLIVE RAMP  50 -> 900", "F2", 10, RGB["olive-500"]); y += 16
    ramp = ["olive-50", "olive-100", "olive-200", "olive-300", "olive-400",
            "olive-500", "olive-600", "olive-700", "olive-800", "olive-900"]
    bw = (p.w - 112) / len(ramp)
    for i, key in enumerate(ramp):
        p.rect(56 + i * bw, p.h - (y + 70), bw - 2, 70, RGB[key])
    y += 78
    p.text(56, y, "50", "F3", 8, RGB["muted"])
    p.text(p.w - 70, y, "900", "F3", 8, RGB["muted"])
    y += 24

    p.text(56, y, "ACCENT", "F2", 10, RGB["olive-500"]); y += 16
    p.swatch_row(56, y, "--ds-accent = --ds-color-olive-400", OKLCH["olive-400"], RGB["olive-400"], w=180, ring=True)
    y += 44

    p.text(56, y, "NEUTRALS", "F2", 10, RGB["olive-500"]); y += 16
    for name, key in [
        ("--ds-color-bg", "bg"),
        ("--ds-color-fg", "fg"),
        ("--ds-color-fg-strong", "fg-strong"),
        ("--ds-color-muted", "muted"),
    ]:
        p.swatch_row(56, y, name, OKLCH[key], RGB[key], w=150)
        y += 30
    y += 8
    p.text(56, y, "SEMANTIC", "F2", 10, RGB["olive-500"]); y += 16
    for name, key in [
        ("--ds-color-success", "success"),
        ("--ds-color-warning", "warning"),
        ("--ds-color-error", "error"),
        ("--ds-color-info", "info"),
    ]:
        p.swatch_row(56, y, name, OKLCH[key], RGB[key], w=150)
        y += 30
    footer(p, "Color Card")
    doc.add_page(p)
    return doc.build()


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(root, "assets", "downloads")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "edic-ds-reference.pdf"), "wb") as f:
        f.write(build_reference())
    with open(os.path.join(out_dir, "edic-ds-color-card.pdf"), "wb") as f:
        f.write(build_color_card())
    print("Generated PDFs in", out_dir)


if __name__ == "__main__":
    main()
