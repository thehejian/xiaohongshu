#!/usr/bin/env python3
"""Generate 5 SVG cards for minimax M3 release (Xiaohongshu style).

Layout:
  - m3-banner.png   1792 x 1024  (horizontal cover, used for Weibo/header)
  - m3-square.png   1024 x 1024  (square cover, XHS thumbnail)
  - m3-card-1.png   1024 x 1024  (BrowseComp 83.5 > Opus 4.7)
  - m3-card-2.png   1024 x 1024  (12h ICLR paper reproduction)
  - m3-card-3.png   1024 x 1024  (CUDA 9.4x acceleration)
"""

import os
import subprocess

OUT = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/minimax-m3-xhs"
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
BG       = "#0A0A14"   # near-black
BG_PANEL = "#15151F"   # panel fill
BG_DEEP  = "#050509"
INK      = "#F5F5F7"   # primary text
INK_DIM  = "#A1A1AA"   # secondary text
INK_MUTE = "#71717A"   # tertiary
LINE     = "#27272A"   # hairline
ORANGE   = "#FF6B35"   # minimax primary
ORANGE_D = "#F97316"
PURPLE   = "#8B5CF6"
CYAN     = "#06B6D4"
GREEN    = "#10B981"
RED      = "#EF4444"
GOLD     = "#FBBF24"

FONT_SANS = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FONT_MONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"


# ---------- shared defs ----------
def defs(extra=""):
    return f'''<defs>
  <linearGradient id="orangeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{ORANGE}"/>
    <stop offset="100%" stop-color="{GOLD}"/>
  </linearGradient>
  <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{PURPLE}"/>
    <stop offset="100%" stop-color="{ORANGE}"/>
  </linearGradient>
  <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{CYAN}"/>
    <stop offset="100%" stop-color="{PURPLE}"/>
  </linearGradient>
  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{BG_PANEL}"/>
    <stop offset="100%" stop-color="{BG_DEEP}"/>
  </linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="4" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
    <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity=".5"/>
  </filter>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{LINE}" stroke-width="0.5" opacity="0.4"/>
  </pattern>
  {extra}
</defs>'''


def base_bg(w, h):
    return f'''<rect width="{w}" height="{h}" fill="{BG}"/>
<rect width="{w}" height="{h}" fill="url(#grid)" opacity="0.3"/>
<circle cx="0" cy="0" r="300" fill="{ORANGE}" opacity="0.08"/>
<circle cx="{w}" cy="{h}" r="400" fill="{PURPLE}" opacity="0.08"/>'''


def header(w, title, subtitle, x=64, y=64):
    return f'''<g transform="translate({x},{y})">
  <rect x="0" y="0" width="6" height="36" fill="{ORANGE}"/>
  <text x="20" y="20" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{ORANGE_D}">MINIMAX · M3 RELEASE</text>
  <text x="20" y="34" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">2026.06 · MODEL DROP</text>
</g>'''


def footer(w, y, h):
    return f'''<g transform="translate(64,{h-40})">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">SOURCE · minimaxi.com/models/text/m3</text>
  <text x="{w-128}" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">#M3 #BrowseComp #Agent</text>
</g>'''


def chip(x, y, label, color, dark_text=False):
    """Pill-shaped tag."""
    text_color = BG if dark_text else INK
    w = len(label) * 12 + 30
    return f'''<g transform="translate({x},{y})">
  <rect x="0" y="0" width="{w}" height="28" rx="14" fill="{color}" opacity="0.18"/>
  <rect x="0" y="0" width="{w}" height="28" rx="14" fill="none" stroke="{color}" stroke-width="1" opacity="0.6"/>
  <text x="{w/2}" y="18" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="600" fill="{color}">{label}</text>
</g>'''


# ================================================================
# CARD: banner  (1792 x 1024) — horizontal cover
# ================================================================
def make_banner():
    W, H = 1792, 1024

    # Left column: big title + comparison line
    left = f'''
<!-- Eyebrow -->
<g transform="translate(96, 80)">
  <rect x="0" y="0" width="8" height="48" fill="{ORANGE}"/>
  <text x="28" y="22" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="4" fill="{ORANGE}">minimax · M3</text>
  <text x="28" y="42" font-family="{FONT_MONO}" font-size="13" letter-spacing="2" fill="{INK_MUTE}">FRONTIER OPEN-WORLD MODEL · 2026.06</text>
</g>

<!-- Hero title -->
<g transform="translate(96, 320)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="160" font-weight="900" fill="{INK}" letter-spacing="-4">minimax</text>
  <text x="0" y="160" font-family="{FONT_SANS}" font-size="200" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-6">M3</text>
</g>

<!-- Subtitle -->
<g transform="translate(96, 700)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="32" font-weight="500" fill="{INK}">首个 frontier 国产开源旗舰</text>
  <text x="0" y="40" font-family="{FONT_SANS}" font-size="22" font-weight="400" fill="{INK_DIM}">百万上下文 · 原生多模态 · 前沿 Coding &amp; Agentic</text>
</g>

<!-- Chip row -->
<g transform="translate(96, 800)">
  {chip(0,    0, "1M 上下文", ORANGE)}
  {chip(200,  0, "BrowseComp 83.5", PURPLE)}
  {chip(450,  0, "原生多模态", CYAN)}
  {chip(640,  0, "即将开源", GREEN)}
</g>

<!-- Bottom stat -->
<g transform="translate(96, 920)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="14" letter-spacing="2" fill="{INK_MUTE}">▶ POSTTRAINBENCH · 12H ICLR PAPER · CUDA 9.4×</text>
</g>'''

    # Right column: focal number + comparison
    right = f'''
<!-- Right panel: BrowseComp focal -->
<g transform="translate(1120, 80)">
  <rect x="0" y="0" width="576" height="720" rx="20" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="576" height="720" rx="20" fill="none" stroke="{LINE}" stroke-width="1"/>

  <text x="40" y="60" font-family="{FONT_SANS}" font-size="16" font-weight="700" letter-spacing="3" fill="{ORANGE}">BROWSE COMP</text>
  <text x="40" y="84" font-family="{FONT_MONO}" font-size="12" letter-spacing="2" fill="{INK_MUTE}">AGENT BENCHMARK · 智能体能力</text>

  <line x1="40" y1="100" x2="536" y2="100" stroke="{LINE}" stroke-width="1"/>

  <!-- minimax M3 label -->
  <text x="40" y="140" font-family="{FONT_SANS}" font-size="20" font-weight="600" fill="{INK}">minimax M3</text>

  <!-- Big focal number -->
  <text x="40" y="320" font-family="{FONT_SANS}" font-size="200" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-6">83.5</text>

  <!-- VS line -->
  <line x1="40" y1="380" x2="536" y2="380" stroke="{LINE}" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- Comparison rows -->
  <g transform="translate(40, 410)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="18" font-weight="500" fill="{INK_DIM}">Opus 4.7</text>
    <rect x="160" y="6" width="200" height="20" rx="4" fill="{LINE}"/>
    <rect x="160" y="6" width="158" height="20" rx="4" fill="{PURPLE}"/>
    <text x="370" y="22" font-family="{FONT_MONO}" font-size="22" font-weight="700" fill="{PURPLE}">79.3</text>
  </g>

  <g transform="translate(40, 450)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="18" font-weight="500" fill="{INK_DIM}">GPT-5.5</text>
    <rect x="160" y="6" width="200" height="20" rx="4" fill="{LINE}"/>
    <rect x="160" y="6" width="142" height="20" rx="4" fill="{CYAN}"/>
    <text x="370" y="22" font-family="{FONT_MONO}" font-size="22" font-weight="700" fill="{CYAN}">71.5</text>
  </g>

  <g transform="translate(40, 490)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="18" font-weight="500" fill="{INK_DIM}">Claude 4 Sonnet</text>
    <rect x="160" y="6" width="200" height="20" rx="4" fill="{LINE}"/>
    <rect x="160" y="6" width="110" height="20" rx="4" fill="{GOLD}"/>
    <text x="370" y="22" font-family="{FONT_MONO}" font-size="22" font-weight="700" fill="{GOLD}">55.0</text>
  </g>

  <!-- Highlight bar -->
  <g transform="translate(40, 600)">
    <rect x="0" y="0" width="496" height="80" rx="8" fill="{ORANGE}" opacity="0.12"/>
    <text x="20" y="36" font-family="{FONT_SANS}" font-size="20" font-weight="700" fill="{ORANGE_D}">+4.2 领先 Opus 4.7</text>
    <text x="20" y="62" font-family="{FONT_SANS}" font-size="14" font-weight="400" fill="{ORANGE_D}">首个 BrowseComp 上 80 分的国产模型</text>
  </g>
</g>'''

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs()}
{base_bg(W, H)}
{left}
{right}
{footer(W, 0, H)}
</svg>'''


# ================================================================
# CARD: square  (1024 x 1024) — XHS cover
# ================================================================
def make_square():
    W, H = 1024, 1024

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs()}
{base_bg(W, H)}

<!-- Eyebrow -->
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="6" height="36" fill="{ORANGE}"/>
  <text x="22" y="18" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{ORANGE}">minimax · M3</text>
  <text x="22" y="34" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">FRONTIER · 2026.06</text>
</g>

<!-- Hero -->
<g transform="translate(64, 180)">
  <text x="0" y="80" font-family="{FONT_SANS}" font-size="92" font-weight="900" fill="{INK}" letter-spacing="-3">minimax</text>
  <text x="0" y="220" font-family="{FONT_SANS}" font-size="160" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-5">M3</text>
</g>

<!-- Focal number -->
<g transform="translate(64, 480)">
  <rect x="0" y="0" width="896" height="280" rx="16" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="896" height="280" rx="16" fill="none" stroke="{LINE}" stroke-width="1"/>

  <text x="40" y="50" font-family="{FONT_SANS}" font-size="14" font-weight="700" letter-spacing="3" fill="{ORANGE}">BROWSE COMP</text>
  <text x="40" y="78" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">AGENT BENCHMARK</text>

  <text x="40" y="200" font-family="{FONT_SANS}" font-size="120" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-3">83.5</text>
  <text x="280" y="200" font-family="{FONT_SANS}" font-size="40" font-weight="300" fill="{INK_DIM}">vs</text>
  <text x="370" y="200" font-family="{FONT_SANS}" font-size="80" font-weight="700" fill="{PURPLE}">79.3</text>
  <text x="600" y="160" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{INK_MUTE}">Opus 4.7</text>
  <text x="600" y="190" font-family="{FONT_SANS}" font-size="16" font-weight="700" fill="{ORANGE_D}">+4.2 领先</text>

  <text x="40" y="245" font-family="{FONT_SANS}" font-size="18" font-weight="500" fill="{INK_DIM}">首个 frontier 国产开源旗舰</text>
</g>

<!-- 3 chips -->
<g transform="translate(64, 800)">
  {chip(0,   0, "1M 上下文", ORANGE)}
  {chip(180, 0, "原生多模态", CYAN)}
  {chip(360, 0, "前沿 Coding", PURPLE)}
  {chip(540, 0, "即将开源", GREEN)}
</g>

<!-- Bottom -->
<g transform="translate(64, 940)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="12" letter-spacing="2" fill="{INK_MUTE}">▶ POSTTRAINBENCH · ICLR 12H · CUDA 9.4×</text>
  <text x="896" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="12" letter-spacing="2" fill="{INK_MUTE}">2026.06</text>
</g>
</svg>'''


# ================================================================
# CARD 1: BrowseComp 83.5 > Opus 4.7
# ================================================================
def make_card1():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs()}
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.3"/>

{header(W, "", "")}

<!-- Title -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="20" font-weight="700" letter-spacing="3" fill="{ORANGE}">CARD 01 · 智能体能力</text>
  <text x="0" y="60" font-family="{FONT_SANS}" font-size="56" font-weight="900" fill="{INK}" letter-spacing="-2">BrowseComp 评测</text>
  <text x="0" y="120" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">M3 跑赢 Opus 4.7,领先 4.2 分</text>
</g>

<!-- Big focal number + vs -->
<g transform="translate(64, 380)">
  <!-- M3 card -->
  <rect x="0" y="0" width="416" height="280" rx="16" fill="{ORANGE}" opacity="0.12" filter="url(#shadow)"/>
  <rect x="0" y="0" width="416" height="280" rx="16" fill="none" stroke="{ORANGE}" stroke-width="2"/>
  <text x="208" y="60" text-anchor="middle" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="2" fill="{ORANGE}">minimax M3</text>
  <text x="208" y="200" text-anchor="middle" font-family="{FONT_SANS}" font-size="160" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-4">83.5</text>
  <text x="208" y="240" text-anchor="middle" font-family="{FONT_SANS}" font-size="16" font-weight="600" fill="{ORANGE}">🥇 第 1</text>

  <!-- VS -->
  <g transform="translate(432, 140)">
    <text x="32" y="0" text-anchor="middle" font-family="{FONT_SANS}" font-size="36" font-weight="300" fill="{INK_MUTE}">VS</text>
    <line x1="0" y1="20" x2="64" y2="20" stroke="{LINE}" stroke-width="1"/>
  </g>

  <!-- Opus 4.7 card -->
  <rect x="544" y="0" width="416" height="280" rx="16" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="544" y="0" width="416" height="280" rx="16" fill="none" stroke="{LINE}" stroke-width="1"/>
  <text x="752" y="60" text-anchor="middle" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="2" fill="{PURPLE}">Opus 4.7</text>
  <text x="752" y="200" text-anchor="middle" font-family="{FONT_SANS}" font-size="160" font-weight="900" fill="{PURPLE}" letter-spacing="-4">79.3</text>
  <text x="752" y="240" text-anchor="middle" font-family="{FONT_SANS}" font-size="16" font-weight="600" fill="{INK_MUTE}">第 2</text>
</g>

<!-- Bar comparison -->
<g transform="translate(64, 700)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="600" letter-spacing="2" fill="{INK_MUTE}">全模型对比</text>

  <g transform="translate(0, 30)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{INK}">minimax M3</text>
    <rect x="180" y="6" width="600" height="22" rx="4" fill="{LINE}"/>
    <rect x="180" y="6" width="600" height="22" rx="4" fill="url(#orangeGrad)"/>
    <text x="800" y="22" font-family="{FONT_MONO}" font-size="18" font-weight="700" fill="{ORANGE}">83.5</text>
  </g>

  <g transform="translate(0, 64)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{INK_DIM}">Opus 4.7</text>
    <rect x="180" y="6" width="600" height="22" rx="4" fill="{LINE}"/>
    <rect x="180" y="6" width="569" height="22" rx="4" fill="{PURPLE}"/>
    <text x="800" y="22" font-family="{FONT_MONO}" font-size="18" font-weight="700" fill="{PURPLE}">79.3</text>
  </g>

  <g transform="translate(0, 98)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{INK_DIM}">GPT-5.5</text>
    <rect x="180" y="6" width="600" height="22" rx="4" fill="{LINE}"/>
    <rect x="180" y="6" width="513" height="22" rx="4" fill="{CYAN}"/>
    <text x="800" y="22" font-family="{FONT_MONO}" font-size="18" font-weight="700" fill="{CYAN}">71.5</text>
  </g>

  <g transform="translate(0, 132)">
    <text x="0" y="20" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{INK_DIM}">Claude 4 Sonnet</text>
    <rect x="180" y="6" width="600" height="22" rx="4" fill="{LINE}"/>
    <rect x="180" y="6" width="395" height="22" rx="4" fill="{GOLD}"/>
    <text x="800" y="22" font-family="{FONT_MONO}" font-size="18" font-weight="700" fill="{GOLD}">55.0</text>
  </g>
</g>

<!-- Footer note -->
<g transform="translate(64, 940)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{ORANGE}">▶ 首个 BrowseComp 上 80 分的国产模型</text>
</g>
</svg>'''


# ================================================================
# CARD 2: 12h ICLR paper reproduction
# ================================================================
def make_card2():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs()}
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.3"/>

{header(W, "", "")}

<!-- Title -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="20" font-weight="700" letter-spacing="3" fill="{ORANGE}">CARD 02 · 长程执行</text>
  <text x="0" y="60" font-family="{FONT_SANS}" font-size="44" font-weight="900" fill="{INK}" letter-spacing="-2">12 小时自主复现</text>
  <text x="0" y="110" font-family="{FONT_SANS}" font-size="44" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-2">ICLR 2025 杰出论文</text>
</g>

<!-- Stats row -->
<g transform="translate(64, 360)">
  <!-- 12H -->
  <rect x="0" y="0" width="280" height="200" rx="16" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="280" height="200" rx="16" fill="none" stroke="{ORANGE}" stroke-width="2"/>
  <text x="140" y="50" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="600" letter-spacing="2" fill="{ORANGE}">连续运行</text>
  <text x="140" y="140" text-anchor="middle" font-family="{FONT_SANS}" font-size="80" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-2">12h</text>
  <text x="140" y="175" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="500" fill="{INK_DIM}">零人工介入</text>

  <!-- 18 commits -->
  <rect x="308" y="0" width="280" height="200" rx="16" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="308" y="0" width="280" height="200" rx="16" fill="none" stroke="{PURPLE}" stroke-width="2"/>
  <text x="448" y="50" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="600" letter-spacing="2" fill="{PURPLE}">代码提交</text>
  <text x="448" y="140" text-anchor="middle" font-family="{FONT_SANS}" font-size="80" font-weight="900" fill="{PURPLE}" letter-spacing="-2">18</text>
  <text x="448" y="175" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="500" fill="{INK_DIM}">commits</text>

  <!-- 23 charts -->
  <rect x="616" y="0" width="280" height="200" rx="16" fill="{BG_PANEL}" filter="url(#shadow)"/>
  <rect x="616" y="0" width="280" height="200" rx="16" fill="none" stroke="{CYAN}" stroke-width="2"/>
  <text x="756" y="50" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="600" letter-spacing="2" fill="{CYAN}">实验图表</text>
  <text x="756" y="140" text-anchor="middle" font-family="{FONT_SANS}" font-size="80" font-weight="900" fill="{CYAN}" letter-spacing="-2">23</text>
  <text x="756" y="175" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="500" fill="{INK_DIM}">figures</text>
</g>

<!-- Timeline -->
<g transform="translate(64, 620)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="600" letter-spacing="2" fill="{INK_MUTE}">LONG HORIZON TIMELINE</text>

  <!-- timeline bar -->
  <line x1="0" y1="60" x2="896" y2="60" stroke="{LINE}" stroke-width="2"/>
  <rect x="0" y="50" width="896" height="20" rx="10" fill="url(#purpleGrad)"/>

  <!-- milestones -->
  <g transform="translate(0, 30)">
    <circle cx="0"   cy="30" r="10" fill="{ORANGE}"/>
    <text x="0" y="0"  text-anchor="middle" font-family="{FONT_MONO}" font-size="11" fill="{INK_MUTE}">0H</text>
    <text x="0" y="100" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="500" fill="{INK_DIM}">读论文</text>

    <circle cx="280" cy="30" r="10" fill="{PURPLE}"/>
    <text x="280" y="0" text-anchor="middle" font-family="{FONT_MONO}" font-size="11" fill="{INK_MUTE}">4H</text>
    <text x="280" y="100" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="500" fill="{INK_DIM}">代码骨架</text>

    <circle cx="560" cy="30" r="10" fill="{CYAN}"/>
    <text x="560" y="0" text-anchor="middle" font-family="{FONT_MONO}" font-size="11" fill="{INK_MUTE}">8H</text>
    <text x="560" y="100" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="500" fill="{INK_DIM}">实验运行</text>

    <circle cx="896" cy="30" r="10" fill="{GREEN}"/>
    <text x="896" y="0" text-anchor="middle" font-family="{FONT_MONO}" font-size="11" fill="{INK_MUTE}">12H</text>
    <text x="896" y="100" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="500" fill="{GREEN}">✅ 复现成功</text>
  </g>
</g>

<!-- Paper info -->
<g transform="translate(64, 850)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="18" font-weight="500" fill="{INK}">论文:Learning Dynamics of LLM Finetuning</text>
  <text x="0" y="32" font-family="{FONT_SANS}" font-size="16" font-weight="400" fill="{INK_DIM}">多模态读图 + 长上下文 + Agent 长线程执行 — 三能力首次合一</text>
</g>

<!-- Footer -->
<g transform="translate(64, 980)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">CARD 02/03 · 02/03</text>
</g>
</svg>'''


# ================================================================
# CARD 3: CUDA 9.4x acceleration
# ================================================================
def make_card3():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{defs()}
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.3"/>

{header(W, "", "")}

<!-- Title -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="20" font-weight="700" letter-spacing="3" fill="{ORANGE}">CARD 03 · 系统优化</text>
  <text x="0" y="60" font-family="{FONT_SANS}" font-size="56" font-weight="900" fill="url(#orangeGrad)" letter-spacing="-2">CUDA 9.4× 加速</text>
  <text x="0" y="120" font-family="{FONT_SANS}" font-size="28" font-weight="400" fill="{INK_DIM}">FP8 矩阵乘 kernel 自主优化</text>
</g>

<!-- Hero: utilization before/after -->
<g transform="translate(64, 360)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="14" font-weight="600" letter-spacing="2" fill="{INK_MUTE}">NVIDIA Hopper 架构 · 硬件峰值利用率</text>

  <!-- BEFORE -->
  <g transform="translate(0, 50)">
    <text x="0" y="0" font-family="{FONT_SANS}" font-size="18" font-weight="500" fill="{INK_MUTE}">起点 (Triton 骨架)</text>
    <rect x="0" y="20" width="896" height="50" rx="8" fill="{LINE}"/>
    <rect x="0" y="20" width="68" height="50" rx="8" fill="{RED}" opacity="0.6"/>
    <text x="78" y="55" font-family="{FONT_MONO}" font-size="24" font-weight="700" fill="{RED}">7.6%</text>
  </g>

  <!-- AFTER -->
  <g transform="translate(0, 160)">
    <text x="0" y="0" font-family="{FONT_SANS}" font-size="18" font-weight="500" fill="{ORANGE}">终点 (M3 优化后)</text>
    <rect x="0" y="20" width="896" height="50" rx="8" fill="{LINE}"/>
    <rect x="0" y="20" width="639" height="50" rx="8" fill="url(#orangeGrad)"/>
    <text x="650" y="55" font-family="{FONT_MONO}" font-size="24" font-weight="700" fill="{ORANGE}">71.3%</text>
  </g>

  <!-- 9.4x badge -->
  <g transform="translate(680, 280)">
    <rect x="0" y="0" width="216" height="80" rx="40" fill="{ORANGE}" filter="url(#glow)"/>
    <text x="108" y="38" text-anchor="middle" font-family="{FONT_SANS}" font-size="14" font-weight="600" letter-spacing="3" fill="{BG}">SPEED UP</text>
    <text x="108" y="68" text-anchor="middle" font-family="{FONT_SANS}" font-size="32" font-weight="900" fill="{BG}">9.4 ×</text>
  </g>
</g>

<!-- Stats row -->
<g transform="translate(64, 760)">
  <rect x="0" y="0" width="280" height="120" rx="12" fill="{BG_PANEL}"/>
  <rect x="0" y="0" width="280" height="120" rx="12" fill="none" stroke="{LINE}" stroke-width="1"/>
  <text x="140" y="36" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="600" letter-spacing="2" fill="{ORANGE}">BENCHMARK 提交</text>
  <text x="140" y="86" text-anchor="middle" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{ORANGE}">147</text>
  <text x="140" y="108" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" fill="{INK_MUTE}">次迭代</text>

  <rect x="308" y="0" width="280" height="120" rx="12" fill="{BG_PANEL}"/>
  <rect x="308" y="0" width="280" height="120" rx="12" fill="none" stroke="{LINE}" stroke-width="1"/>
  <text x="448" y="36" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="600" letter-spacing="2" fill="{PURPLE}">工具调用</text>
  <text x="448" y="86" text-anchor="middle" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{PURPLE}">1959</text>
  <text x="448" y="108" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" fill="{INK_MUTE}">次</text>

  <rect x="616" y="0" width="280" height="120" rx="12" fill="{BG_PANEL}"/>
  <rect x="616" y="0" width="280" height="120" rx="12" fill="none" stroke="{LINE}" stroke-width="1"/>
  <text x="756" y="36" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" font-weight="600" letter-spacing="2" fill="{CYAN}">运行时长</text>
  <text x="756" y="86" text-anchor="middle" font-family="{FONT_SANS}" font-size="48" font-weight="900" fill="{CYAN}">24h</text>
  <text x="756" y="108" text-anchor="middle" font-family="{FONT_SANS}" font-size="12" fill="{INK_MUTE}">连续</text>
</g>

<!-- Footer -->
<g transform="translate(64, 920)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="{ORANGE_D}">▶ 起点 1 个无法运行的 Triton 骨架,终点 9.4× 加速</text>
  <text x="0" y="28" font-family="{FONT_SANS}" font-size="14" font-weight="400" fill="{INK_DIM}">硬件加速比从 7.6% 推进至 71.3% —— 全程零人工介入</text>
</g>

<g transform="translate(64, 1000)">
  <text x="0" y="0" font-family="{FONT_MONO}" font-size="11" letter-spacing="2" fill="{INK_MUTE}">CARD 03/03 · END</text>
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
    # Use Inkscape for SVG -> PNG (better font handling, renders CJK correctly)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}"],
        check=True, capture_output=True,
    )
    print(f"  -> {png_path}")


if __name__ == "__main__":
    print("Generating minimax M3 XHS cards...")
    cards = [
        ("m3-banner",  make_banner()),
        ("m3-square",  make_square()),
        ("m3-card-1",  make_card1()),
        ("m3-card-2",  make_card2()),
        ("m3-card-3",  make_card3()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")
