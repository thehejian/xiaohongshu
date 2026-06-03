#!/usr/bin/env python3
"""Generate SVG cards for Coding Plan (Xiaohongshu style, white theme).

Layout:
  - coding-plan-banner.png   1792 x 1024  (horizontal cover)
  - coding-plan-square.png   1024 x 1024  (XHS thumbnail)
"""

import os
import subprocess

OUT = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/coding-plan-xhs"
os.makedirs(OUT, exist_ok=True)

# ---------- white palette ----------
BG       = "#FFFFFF"
BG_SOFT  = "#FAFAFA"
BG_PANEL = "#F5F7FA"
BG_CARD  = "#FFFFFF"
INK      = "#0F172A"
INK_DIM  = "#475569"
INK_MUTE = "#94A3B8"
LINE     = "#E2E8F0"
LINE_SFT = "#F1F5F9"

TEAL     = "#0EA5E9"
TEAL_D   = "#0284C7"
TEAL_LT  = "#E0F2FE"
BLUE     = "#3B82F6"
BLUE_LT  = "#DBEAFE"
CYAN     = "#06B6D4"
PURPLE   = "#8B5CF6"
PURPLE_LT= "#EDE9FE"
ORANGE   = "#F97316"
ORANGE_LT= "#FFEDD5"
GREEN    = "#10B981"
GREEN_LT = "#D1FAE5"
AMBER    = "#F59E0B"
ROSE     = "#F43F5E"
ROSE_LT  = "#FFE4E6"

FONT_SANS = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, Inter, sans-serif"
FONT_MONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"


def defs(extra=""):
    return f'''<defs>
  <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{TEAL}"/>
    <stop offset="100%" stop-color="{CYAN}"/>
  </linearGradient>
  <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{BLUE}"/>
    <stop offset="100%" stop-color="{TEAL}"/>
  </linearGradient>
  <linearGradient id="warmGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{ORANGE}"/>
    <stop offset="100%" stop-color="{AMBER}"/>
  </linearGradient>
  <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{ROSE}"/>
    <stop offset="100%" stop-color="{PURPLE}"/>
  </linearGradient>
  <filter id="softShadow" x="-10%" y="-10%" width="130%" height="130%">
    <feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="#0F172A" flood-opacity=".06"/>
  </filter>
  <filter id="liftShadow" x="-10%" y="-10%" width="130%" height="130%">
    <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#0F172A" flood-opacity=".08"/>
  </filter>
  <pattern id="dotGrid" width="32" height="32" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r="1" fill="{LINE}" opacity="0.6"/>
  </pattern>
  {extra}
</defs>'''


def soft_bg(w, h):
    return f'''<rect width="{w}" height="{h}" fill="{BG}"/>
<rect width="{w}" height="{h}" fill="url(#dotGrid)" opacity="0.4"/>'''


def chip(x, y, label, accent, bg=None):
    w = len(label) * 14 + 32
    bgc = bg or f"{accent}1A"
    return f'''<g transform="translate({x},{y})">
  <rect x="0" y="0" width="{w}" height="32" rx="16" fill="{bgc}" stroke="{accent}" stroke-opacity="0.4" stroke-width="1"/>
  <text x="{w/2}" y="21" text-anchor="middle" font-family="{FONT_SANS}" font-size="13" font-weight="600" fill="{accent}">{label}</text>
</g>'''


# ================================================================
# BANNER (1792 x 1024)
# ================================================================
def make_banner():
    W, H = 1792, 1024

    # Platforms for right-side ranking cards
    platforms = [
        ("1", "智谱AI", "GLM-5.1 · T0代码", TEAL, TEAL_LT),
        ("2", "MiniMax", "M2.7 · 最低价", BLUE, BLUE_LT),
        ("3", "讯飞星火", "GLM-5.1 · 不限购", GREEN, GREEN_LT),
        ("4", "Kimi", "K2.6 · 多模态", PURPLE, PURPLE_LT),
    ]

    right = ""
    for i, (rank, name, desc, color, lt) in enumerate(platforms):
        y = 200 + i * 180
        right += f'''<g transform="translate(940,{y})">
  <rect x="0" y="0" width="680" height="140" rx="16" fill="{BG_CARD}" filter="url(#softShadow)"/>
  <rect x="0" y="0" width="680" height="140" rx="16" fill="none" stroke="{color}" stroke-opacity="0.3"/>
  <rect x="0" y="0" width="80" height="140" rx="16" fill="{color}" fill-opacity="0.1"/>
  <text x="40" y="88" text-anchor="middle" font-family="{FONT_SANS}" font-size="40" font-weight="900" fill="{color}">{rank}</text>
  <text x="110" y="60" font-family="{FONT_SANS}" font-size="30" font-weight="800" fill="{INK}">{name}</text>
  <text x="110" y="100" font-family="{FONT_SANS}" font-size="20" font-weight="400" fill="{INK_DIM}">{desc}</text>
  <circle cx="640" cy="70" r="8" fill="{color}"/>
</g>'''

    left = f'''
<!-- Eyebrow -->
<g transform="translate(80, 80)">
  <rect x="0" y="0" width="8" height="48" fill="url(#roseGrad)"/>
  <text x="28" y="22" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="4" fill="{ROSE}">2026 · CODING PLAN</text>
  <text x="28" y="44" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">25 PLATFORMS · COMPARISON</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 240)">
  <text x="0" y="0"   font-family="{FONT_SANS}" font-size="72" font-weight="900" fill="{INK}" letter-spacing="-2">AI Coding Plan</text>
  <text x="0" y="90" font-family="{FONT_SANS}" font-size="120" font-weight="900" fill="url(#tealGrad)" letter-spacing="-4">最强攻略</text>
</g>

<!-- Subtitle -->
<g transform="translate(80, 500)">
  <text x="0" y="0"  font-family="{FONT_SANS}" font-size="28" font-weight="500" fill="{INK}">25大平台横向对比 · 附选购指南</text>
  <text x="0" y="42" font-family="{FONT_SANS}" font-size="20" font-weight="400" fill="{INK_DIM}">智谱 · MiniMax · 讯飞 · Kimi · 字节 · 阿里 · 小米 · 腾讯 ...</text>
</g>

<!-- Warning chip -->
<g transform="translate(80, 640)">
  <rect x="0" y="0" width="680" height="60" rx="12" fill="{ROSE_LT}"/>
  <text x="24" y="36" font-family="{FONT_SANS}" font-size="22" font-weight="700" fill="{ROSE}">⚠️ 大厂纷纷转 Token Plan, Coding Plan 且买且珍惜</text>
</g>

<!-- Tag chips -->
<g transform="translate(80, 760)">
  {chip(0,   0, "限购预警", ROSE)}
  {chip(140, 0, "性价比之王", GREEN)}
  {chip(290, 0, "代码专用", TEAL)}
  {chip(440, 0, "免费羊毛", BLUE)}
  {chip(590, 0, "多模态Agent", PURPLE)}
</g>'''

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs()}
{soft_bg(W, H)}
{left}
{right}
<g transform="translate(80,{H-50})">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">SOURCE · codingplan.fyi (2026.5.19)</text>
  <text x="{W-160}" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">#CodingPlan #AI编程</text>
</g>
</svg>'''


# ================================================================
# SQUARE (1024 x 1024) — XHS cover
# ================================================================
def make_square():
    W, H = 1024, 1024

    # Price cards
    plans = [
        ("智谱AI", "¥46.55/月", "GLM-5.1 · T0", TEAL, TEAL_LT),
        ("MiniMax", "¥26.1/月", "M2.7 · 最低价", GREEN, GREEN_LT),
        ("讯飞星火", "¥39/月", "GLM-5.1 · 不限购", BLUE, BLUE_LT),
        ("Kimi", "¥49/月", "K2.6 · 多模态", PURPLE, PURPLE_LT),
    ]

    cards_svg = ""
    for i, (name, price, desc, color, lt) in enumerate(plans):
        col = i % 2
        row = i // 2
        x = 56 + col * 460
        y = 360 + row * 170
        cards_svg += f'''<g transform="translate({x},{y})">
  <rect x="0" y="0" width="430" height="140" rx="16" fill="{BG_CARD}" filter="url(#softShadow)"/>
  <rect x="0" y="0" width="430" height="140" rx="16" fill="none" stroke="{color}" stroke-opacity="0.3"/>
  <rect x="0" y="0" width="10" height="140" rx="5" fill="{color}"/>
  <text x="30" y="40" font-family="{FONT_SANS}" font-size="22" font-weight="800" fill="{INK}">{name}</text>
  <text x="30" y="80" font-family="{FONT_SANS}" font-size="32" font-weight="900" fill="{color}">{price}</text>
  <text x="30" y="115" font-family="{FONT_SANS}" font-size="15" font-weight="400" fill="{INK_DIM}">{desc}</text>
</g>'''

    # Bottom warning bar
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs()}
{soft_bg(W, H)}

<!-- Eyebrow -->
<g transform="translate(56, 56)">
  <rect x="0" y="0" width="6" height="36" fill="url(#roseGrad)"/>
  <text x="22" y="16" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{ROSE}">2026 · CODING PLAN</text>
  <text x="22" y="34" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">25 PLATFORMS</text>
</g>

<!-- Hero title -->
<g transform="translate(56, 160)">
  <text x="0" y="0"   font-family="{FONT_SANS}" font-size="64" font-weight="900" fill="{INK}" letter-spacing="-2">AI Coding Plan</text>
  <text x="0" y="72" font-family="{FONT_SANS}" font-size="80" font-weight="900" fill="url(#tealGrad)" letter-spacing="-3">最强攻略</text>
</g>

<!-- Price cards -->
{cards_svg}

<!-- Bottom warning -->
<g transform="translate(56, 750)">
  <rect x="0" y="0" width="912" height="52" rx="12" fill="{ROSE_LT}"/>
  <text x="456" y="32" text-anchor="middle" font-family="{FONT_SANS}" font-size="18" font-weight="700" fill="{ROSE}">⚠️ 大厂转 Token Plan · Coding Plan 且买且珍惜</text>
</g>

<!-- Chips -->
<g transform="translate(56, 840)">
  {chip(0,   0, "限购预警", ROSE)}
  {chip(140, 0, "性价比之王", GREEN)}
  {chip(290, 0, "代码T0", TEAL)}
  {chip(430, 0, "免费羊毛", BLUE)}
  {chip(570, 0, "选购指南", PURPLE)}
</g>

<!-- Footer -->
<g transform="translate(56, 930)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">codingplan.fyi (2026.5.19)</text>
  <text x="912" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">#CodingPlan #AI编程</text>
</g>
</svg>'''


# ================================================================
# MAIN
# ================================================================
def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}"],
        check=True, capture_output=True,
    )
    size_kb = os.path.getsize(png_path) / 1024
    print(f"  -> {png_path} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    print("Generating Coding Plan XHS cards (white style)...")
    cards = [
        ("coding-plan-banner", make_banner()),
        ("coding-plan-square", make_square()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"\nDone! {len(cards)} cards (svg+png) saved to {OUT}")