#!/usr/bin/env python3
"""Generate summary card with all 8 荣耻 rules in 以...为耻/荣 format."""

import os
import subprocess

OUT = os.path.dirname(os.path.abspath(__file__))
FONT_SANS = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FONT_MONO = "SF Mono, JetBrains Mono, IBM Plex Mono, Menlo, Consolas, monospace"

RULES = [
    "以暗猜接口为耻，以认真查阅为荣",
    "以模糊执行为耻，以寻求确认为荣",
    "以盲想业务为耻，以人类确认为荣",
    "以创造接口为耻，以复用现有为荣",
    "以跳过验证为耻，以主动测试为荣",
    "以破坏架构为耻，以遵循规范为荣",
    "以假装理解为耻，以诚实无知为荣",
    "以盲目修改为耻，以谨慎重构为荣",
]

ACCENTS = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899", "#06B6D4", "#EF4444", "#FBBF24"]

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="30%" r="80%">
    <stop offset="0%" stop-color="#1E293B"/>
    <stop offset="100%" stop-color="#070B15"/>
  </radialGradient>
  <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="#F59E0B"/>
    <stop offset="100%" stop-color="#FBBF24"/>
  </linearGradient>
  <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
    <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity=".5"/>
  </filter>
  <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
    <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#1E293B" stroke-width="0.5" opacity="0.3"/>
  </pattern>
</defs>

<rect width="1024" height="1024" fill="url(#bg)"/>
<rect width="1024" height="1024" fill="url(#grid)" opacity="0.12"/>

<!-- Corner glows -->
<circle cx="0" cy="0" r="200" fill="#F59E0B" opacity="0.04"/>
<circle cx="1024" cy="1024" r="250" fill="#3B82F6" opacity="0.04"/>

<!-- Title bar -->
<g transform="translate(64, 80)">
  <rect x="0" y="0" width="8" height="48" fill="#F59E0B"/>
  <text x="28" y="22" font-family="{FONT_SANS}" font-size="18" font-weight="700" letter-spacing="4" fill="#F59E0B">AI 编程八荣八耻</text>
  <text x="28" y="46" font-family="{FONT_MONO}" font-size="12" letter-spacing="2" fill="#64748B">SUMMARY · 八条戒律</text>
</g>

<!-- Subtitle -->
<g transform="translate(64, 180)">
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="36" font-weight="500" fill="#94A3B8">以荣为纲，以耻为戒</text>
  <text x="0" y="48" font-family="{FONT_SANS}" font-size="20" font-weight="400" fill="#64748B">八条黄金规矩，让 AI 学会"做人"</text>
</g>

<!-- Rules list -->
<g transform="translate(64, 280)">
  {''.join(
    f'''<g transform="translate(0, {i * 76})">
    <rect x="0" y="0" width="896" height="64" rx="10" fill="#111827" filter="url(#shadow)"/>
    <rect x="0" y="0" width="896" height="64" rx="10" fill="none" stroke="{ACCENTS[i]}" stroke-width="1" opacity="0.35"/>
    <rect x="0" y="0" width="4" height="64" rx="2" fill="{ACCENTS[i]}"/>
    <text x="24" y="38" font-family="{FONT_SANS}" font-size="14" font-weight="700" fill="{ACCENTS[i]}">{i+1:02d}</text>
    <text x="64" y="38" font-family="{FONT_SANS}" font-size="22" font-weight="600" fill="#F8FAFC">{rule}</text>
  </g>'''
    for i, rule in enumerate(RULES)
  )}
</g>

<!-- Footer -->
<g transform="translate(64, 940)">
  <line x1="0" y1="-12" x2="896" y2="-12" stroke="#1E293B" stroke-width="1"/>
  <text x="0" y="0" font-family="{FONT_SANS}" font-size="16" font-weight="500" fill="#F59E0B">▶ 放入 System Prompt / CLAUDE.md</text>
  <text x="896" y="0" text-anchor="end" font-family="{FONT_MONO}" font-size="12" letter-spacing="1" fill="#64748B">beisi-tech.github.io</text>
</g>
</svg>'''

out_path = os.path.join(OUT, "honor-card-summary.svg")
png_path = os.path.join(OUT, "honor-card-summary.png")

with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg)

subprocess.run(
    ["inkscape", out_path, "--export-type=png", f"--export-filename={png_path}"],
    check=True, capture_output=True,
)

print(f"Generated: {png_path}")
