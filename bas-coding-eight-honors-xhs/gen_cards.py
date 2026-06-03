#!/usr/bin/env python3
"""Generate XHS cards for AI编程八荣八耻 (formal & grand style)."""

import os
import subprocess

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
BG       = "#0B1120"
BG_CARD  = "#111827"
BG_DEEP  = "#070B15"
LINE     = "#1E293B"
INK      = "#F8FAFC"
INK_DIM  = "#94A3B8"
INK_MUTE = "#64748B"
INK_GOLD = "#F59E0B"
GOLD     = "#F59E0B"
GOLD_LT  = "#FBBF24"
GOLD_DK  = "#D97706"

ACCENTS = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899", "#06B6D4", "#EF4444", "#FBBF24"]
ACCENT_NAMES = ["蓝", "绿", "金", "紫", "粉", "青", "红", "金"]

FONT_SANS = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FONT_MONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"

HONORS = [
    ("认真查阅文档", "暗猜接口参数"),
    ("寻求确认再执行", "模糊执行不管后果"),
    ("找人类确认业务", "自己想象需求"),
    ("复用现有代码", "创造新接口/轮子"),
    ("主动测试验证", "跳过验证直接交差"),
    ("遵循代码规范", "破坏现有架构"),
    ("诚实说不知道", "假装理解硬撑"),
    ("谨慎重构", "盲目修改"),
]


def base_defs():
    return f'''<defs>
  <radialGradient id="bgGrad" cx="50%" cy="30%" r="80%">
    <stop offset="0%" stop-color="#1E293B"/>
    <stop offset="100%" stop-color="{BG_DEEP}"/>
  </radialGradient>
  <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{GOLD}"/>
    <stop offset="100%" stop-color="{GOLD_LT}"/>
  </linearGradient>
  <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#2563EB"/>
    <stop offset="100%" stop-color="#3B82F6"/>
  </linearGradient>
  <filter id="cardShadow" x="-10%" y="-10%" width="130%" height="130%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity=".4"/>
  </filter>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="6" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
    <path d="M 60 0 L 0 0 0 60" fill="none" stroke="{LINE}" stroke-width="0.5" opacity="0.3"/>
  </pattern>
</defs>'''


def honor_card(w, h, idx, honor, disgrace, color):
    accent = color
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{base_defs()}
<rect width="{w}" height="{h}" fill="url(#bgGrad)"/>
<rect width="{w}" height="{h}" fill="url(#grid)" opacity="0.15"/>

<!-- Corner decoration -->
<circle cx="0" cy="0" r="180" fill="{accent}" opacity="0.04"/>
<circle cx="{w}" cy="{h}" r="200" fill="{GOLD}" opacity="0.04"/>

<!-- Main card -->
<g transform="translate(32, 32)">
  <rect x="0" y="0" width="{w-64}" height="{h-64}" rx="20" fill="{BG_CARD}" filter="url(#cardShadow)"/>
  <rect x="0" y="0" width="{w-64}" height="{h-64}" rx="20" fill="none" stroke="{LINE}" stroke-width="1"/>

  <!-- Top accent bar -->
  <rect x="0" y="0" width="{w-64}" height="6" rx="3" fill="{accent}"/>

  <!-- Number badge -->
  <g transform="translate(48, 48)">
    <rect x="0" y="0" width="56" height="56" rx="14" fill="{accent}" opacity="0.12"/>
    <rect x="0" y="0" width="56" height="56" rx="14" fill="none" stroke="{accent}" stroke-width="1.5" opacity="0.4"/>
    <text x="28" y="36" text-anchor="middle" font-family="{FONT_SANS}" font-size="28" font-weight="800" fill="{accent}">{idx+1}</text>
  </g>

  <!-- 荣 label -->
  <g transform="translate(140, 48)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="4" fill="{accent}">第 {idx+1} 荣</text>
  </g>

  <!-- Honor section -->
  <g transform="translate(48, 148)">
    <rect x="0" y="0" width="48" height="48" rx="24" fill="#10B981" opacity="0.15"/>
    <text x="24" y="31" text-anchor="middle" font-family="{FONT_SANS}" font-size="24">✓</text>
    <text x="68" y="34" font-family="{FONT_SANS}" font-size="36" font-weight="800" fill="{INK}">{honor}</text>
  </g>

  <!-- Arrow divider -->
  <g transform="translate({(w-64)//2 - 40}, 240)">
    <line x1="0" y1="0" x2="80" y2="0" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>
  <text x="{(w-64)//2}" y="268" text-anchor="middle" font-family="{FONT_SANS}" font-size="18" fill="{INK_MUTE}">✕</text>
  <g transform="translate({(w-64)//2 - 40}, 284)">
    <line x1="0" y1="0" x2="80" y2="0" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>

  <!-- Disgrace section -->
  <g transform="translate(48, 308)">
    <rect x="0" y="0" width="48" height="48" rx="24" fill="#EF4444" opacity="0.15"/>
    <text x="24" y="31" text-anchor="middle" font-family="{FONT_SANS}" font-size="24">✕</text>
    <text x="68" y="34" font-family="{FONT_SANS}" font-size="36" font-weight="800" fill="{INK_DIM}" opacity="0.7">{disgrace}</text>
  </g>

  <!-- Rule tag -->
  <g transform="translate(48, {h-64-72})">
    <line x1="0" y1="0" x2="{w-64-96}" y2="0" stroke="{LINE}" stroke-width="1"/>
    <text x="0" y="28" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{INK_MUTE}">原则 · 以{ACCENT_NAMES[idx]}为准</text>
    <text x="{w-64-96}" y="28" text-anchor="end" font-family="{FONT_MONO}" font-size="12" letter-spacing="1" fill="{INK_MUTE}">{idx+1:02d} / 08</text>
  </g>
</g>
</svg>'''


def make_banner():
    W, H = 1792, 1024
    left = f'''
<!-- Eyebrow -->
<g transform="translate(96, 80)">
  <rect x="0" y="0" width="8" height="48" fill="{GOLD}"/>
  <text x="28" y="22" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="4" fill="{GOLD}">AI CODING ETHICS</text>
  <text x="28" y="46" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">VIBE CODING 时代 · 人机协作规范</text>
</g>

<!-- Hero title -->
<g transform="translate(96, 200)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="140" font-weight="900" fill="{INK}" letter-spacing="-4">AI 编程</text>
  <text x="0" y="140" font-family="{FONT_SANS}" font-size="140" font-weight="900" fill="url(#goldGrad)" letter-spacing="-4">八荣八耻</text>
</g>

<!-- Subtitle -->
<g transform="translate(96, 420)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="28" font-weight="500" fill="{INK_DIM}">治好人机协作的「默契」</text>
  <text x="0" y="42" font-family="{FONT_SANS}" font-size="22" font-weight="400" fill="{INK_MUTE}">八条黄金规矩，让 AI 学会"做人"</text>
</g>

<!-- Quote panel -->
<g transform="translate(96, 530)">
  <rect x="0" y="0" width="680" height="130" rx="16" fill="{BG_CARD}" filter="url(#cardShadow)"/>
  <rect x="0" y="0" width="680" height="130" rx="16" fill="none" stroke="{LINE}" stroke-width="1"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{GOLD}"/>
  <text x="32" y="42" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{GOLD}">— 写在前面</text>
  <text x="32" y="76" font-family="{FONT_SANS}" font-size="22" font-weight="500" fill="{INK}">"AI 不是不懂，是没规矩。</text>
  <text x="32" y="108" font-family="{FONT_SANS}" font-size="22" font-weight="500" fill="{INK}">八荣八耻，立好规矩，代码质量立竿见影。"</text>
</g>

<!-- Tags -->
<g transform="translate(96, 720)">
  <g transform="translate(0,0)">
    <rect x="0" y="0" width="110" height="38" rx="19" fill="{GOLD}" opacity="0.1"/>
    <rect x="0" y="0" width="110" height="38" rx="19" fill="none" stroke="{GOLD}" stroke-width="1" opacity="0.4"/>
    <text x="55" y="24" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{GOLD}">Claude Code</text>
  </g>
  <g transform="translate(126,0)">
    <rect x="0" y="0" width="90" height="38" rx="19" fill="#3B82F6" opacity="0.1"/>
    <rect x="0" y="0" width="90" height="38" rx="19" fill="none" stroke="#3B82F6" stroke-width="1" opacity="0.4"/>
    <text x="45" y="24" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="#3B82F6">Cursor</text>
  </g>
  <g transform="translate(232,0)">
    <rect x="0" y="0" width="130" height="38" rx="19" fill="#10B981" opacity="0.1"/>
    <rect x="0" y="0" width="130" height="38" rx="19" fill="none" stroke="#10B981" stroke-width="1" opacity="0.4"/>
    <text x="65" y="24" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="#10B981">System Prompt</text>
  </g>
  <g transform="translate(378,0)">
    <rect x="0" y="0" width="110" height="38" rx="19" fill="#EC4899" opacity="0.1"/>
    <rect x="0" y="0" width="110" height="38" rx="19" fill="none" stroke="#EC4899" stroke-width="1" opacity="0.4"/>
    <text x="55" y="24" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="#EC4899">CLAUDE.md</text>
  </g>
</g>
'''

    right = f'''
<!-- Right panel: 8 rules overview -->
<g transform="translate(960, 80)">
  <rect x="0" y="0" width="740" height="820" rx="20" fill="{BG_CARD}" filter="url(#cardShadow)"/>
  <rect x="0" y="0" width="740" height="820" rx="20" fill="none" stroke="{LINE}" stroke-width="1"/>

  <text x="40" y="50" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="3" fill="{GOLD}">八荣八耻 · 总览</text>
  <line x1="40" y1="68" x2="700" y2="68" stroke="{LINE}" stroke-width="1"/>

  <g transform="translate(40, 96)">
    {"".join(
      f'''<g transform="translate(0, {i * 80})">
        <rect x="0" y="0" width="660" height="64" rx="10" fill="{ACCENTS[i]}" opacity="0.04"/>
        <rect x="0" y="0" width="4" height="64" rx="2" fill="{ACCENTS[i]}"/>
        <text x="20" y="28" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{ACCENTS[i]}">{i+1:02d}</text>
        <text x="52" y="28" font-family="{FONT_SANS}" font-size="20" font-weight="700" fill="{INK}">✓ {honor}</text>
        <text x="52" y="52" font-family="{FONT_SANS}" font-size="14" fill="{INK_MUTE}">✕ {disgrace}</text>
      </g>'''
      for i, (honor, disgrace) in enumerate(HONORS)
    )}
  </g>
</g>
'''

    bottom = f'''
<g transform="translate(96, 960)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">▶ 查看完整卡片 · 每张详解一条荣耻规则</text>
  <text x="1600" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">beisi-tech.github.io</text>
</g>
'''

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{base_defs()}
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>
<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.1"/>

<!-- Decorative -->
<circle cx="120" cy="120" r="6" fill="{GOLD}" opacity="0.3"/>
<circle cx="160" cy="120" r="4" fill="#3B82F6" opacity="0.3"/>
<circle cx="1680" cy="120" r="5" fill="#10B981" opacity="0.3"/>

{left}
{right}
{bottom}
</svg>'''


def make_square():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{base_defs()}
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>
<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.1"/>

<!-- Decorative -->
<circle cx="80" cy="80" r="4" fill="{GOLD}" opacity="0.3"/>
<circle cx="120" cy="80" r="3" fill="#3B82F6" opacity="0.3"/>
<circle cx="160" cy="80" r="4" fill="#10B981" opacity="0.3"/>

<!-- Eyebrow -->
<g transform="translate(80, 100)">
  <rect x="0" y="0" width="6" height="40" fill="{GOLD}"/>
  <text x="22" y="20" font-family="{FONT_SANS}" font-size="16" font-weight="700" letter-spacing="3" fill="{GOLD}">AI CODING ETHICS</text>
  <text x="22" y="40" font-family="{FONT_MONO}" font-size="12" letter-spacing="2" fill="{INK_MUTE}">八条规矩 · 立竿见影</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 200)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="92" font-weight="900" fill="{INK}" letter-spacing="-2">AI 编程</text>
  <text x="0" y="110" font-family="{FONT_SANS}" font-size="92" font-weight="900" fill="url(#goldGrad)" letter-spacing="-2">八荣八耻</text>
</g>

<!-- Subtitle -->
<g transform="translate(80, 360)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="26" font-weight="500" fill="{INK_DIM}">治好人机协作的「默契」</text>
</g>

<!-- 8 rules preview in 2x4 grid -->
<g transform="translate(44, 430)">
  {"".join(
    f'''<g transform="translate({(i%2)*468}, {(i//2)*78})">
      <rect x="0" y="0" width="448" height="62" rx="10" fill="{ACCENTS[i]}" opacity="0.04"/>
      <rect x="0" y="0" width="4" height="62" rx="2" fill="{ACCENTS[i]}"/>
      <text x="20" y="26" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{ACCENTS[i]}">{i+1:02d}</text>
      <text x="48" y="26" font-family="{FONT_SANS}" font-size="18" font-weight="700" fill="{INK}">✓ {honor}</text>
      <text x="48" y="48" font-family="{FONT_SANS}" font-size="13" fill="{INK_MUTE}">✕ {disgrace}</text>
    </g>'''
    for i, (honor, disgrace) in enumerate(HONORS)
  )}
</g>

<!-- Bottom -->
<g transform="translate(80, 940)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">▶ 放入 System Prompt / CLAUDE.md</text>
  <text x="864" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">beisi-tech.github.io</text>
</g>
</svg>'''


def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}"],
        check=True, capture_output=True,
    )
    print(f"  -> {png_path}")


if __name__ == "__main__":
    print("Generating AI编程八荣八耻 cards (formal & grand)...")

    cards = [
        ("bas-coding-eight-honors-banner", make_banner()),
        ("bas-coding-eight-honors-square", make_square()),
    ]

    for i, (honor, disgrace) in enumerate(HONORS):
        svg = honor_card(800, 800, i, honor, disgrace, ACCENTS[i])
        cards.append((f"honor-card-{i+1:02d}", svg))

    for name, svg in cards:
        save_svg(name, svg)

    print(f"Done! {len(cards)} cards saved to {OUT}")