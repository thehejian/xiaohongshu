#!/usr/bin/env python3
"""Generate AI PPT Tools social card images — large text, clear & bold."""

import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

CARDS = [
    {
        "name": "cover",
        "w": 1024, "h": 1365,
        "bg_top": "#FAF7F2",
        "bg_bottom": "#F0EBE0",
        "accent": "#2563EB",
        "title": "AI做PPT工具",
        "subtitle": "四巨头横评",
        "tools": [
            {"name": "Gamma", "color": "#3B82F6", "tag": "全能型"},
            {"name": "Tome", "color": "#8B5CF6", "tag": "故事感"},
            {"name": "MindShow", "color": "#10B981", "tag": "大纲转"},
            {"name": "iSlide AI", "color": "#F59E0B", "tag": "插件派"},
        ],
        "desc": "一句话生成 / 设计感最强 / 大纲秒转 / 插件加速",
    },
    {
        "name": "card-gamma",
        "w": 1024, "h": 1365,
        "bg_top": "#FAF7F2",
        "bg_bottom": "#EFF6FF",
        "accent": "#3B82F6",
        "title": "Gamma",
        "subtitle": "全能型选手",
        "tagline": "一句话生成整套PPT",
        "sections": [
            {"label": "核心能力", "items": ["输入一句话，自动生成大纲+内容+排版", "网页版在线编辑，无需下载安装", "支持导出 PDF / PPTX / 分享链接"]},
            {"label": "适用场景", "items": ["从零开始做方案 / 汇报 / 路演", "课程课件 / 项目提案 / 商业计划"]},
            {"label": "价格", "items": ["免费版够用，高级模板需订阅"]},
        ],
        "rating": "★★★★☆",
        "rating_label": "新手首选",
    },
    {
        "name": "card-tome",
        "w": 1024, "h": 1365,
        "bg_top": "#FAF7F2",
        "bg_bottom": "#F5F3FF",
        "accent": "#8B5CF6",
        "title": "Tome",
        "subtitle": "故事感拉满",
        "tagline": "AI叙事型PPT，页面像杂志",
        "sections": [
            {"label": "核心能力", "items": ["AI叙事驱动，强调故事线设计", "页面排版高级，杂志级视觉效果", "支持嵌入 Figma / Loom / YouTube"]},
            {"label": "适用场景", "items": ["品牌介绍 / 作品集 / 创意提案", "pitch deck / 产品发布 / 艺术展示"]},
            {"label": "价格", "items": ["免费版有限制，高级功能需付费"]},
        ],
        "rating": "★★★★★",
        "rating_label": "设计感最强",
    },
    {
        "name": "card-mindshow",
        "w": 1024, "h": 1365,
        "bg_top": "#FAF7F2",
        "bg_bottom": "#ECFDF5",
        "accent": "#10B981",
        "title": "MindShow",
        "subtitle": "大纲转PPT神器",
        "tagline": "先写大纲，AI自动排版成PPT",
        "sections": [
            {"label": "核心能力", "items": ["大纲 → PPT，一键自动转换", "支持导入 Notion / XMind / Markdown", "模板丰富，排版自动优化"]},
            {"label": "适用场景", "items": ["快速把笔记/大纲变成正式PPT", "已有内容想快速出稿"]},
            {"label": "价格", "items": ["免费版可用，高级模板需付费", "国内访问友好，速度快"]},
        ],
        "rating": "★★★★☆",
        "rating_label": "出稿最快",
    },
    {
        "name": "card-islide",
        "w": 1024, "h": 1365,
        "bg_top": "#FAF7F2",
        "bg_bottom": "#FFFBEB",
        "accent": "#F59E0B",
        "title": "iSlide AI",
        "subtitle": "老牌插件的AI进化",
        "tagline": "PowerPoint插件，直接在PPT里用AI",
        "sections": [
            {"label": "核心能力", "items": ["PowerPoint插件，无需切换平台", "一键换模板、智能排版、图表生成", "图标库/素材库/图示库丰富"]},
            {"label": "适用场景", "items": ["已经会用PPT，想加速提效", "企业级PPT制作 / 标准化输出"]},
            {"label": "价格", "items": ["付费订阅制，功能全面"]},
        ],
        "rating": "★★★★☆",
        "rating_label": "老手提效",
    },
]


def svg_for_card(card):
    w, h = card["w"], card["h"]
    accent = card["accent"]
    bg_top = card["bg_top"]
    bg_bottom = card["bg_bottom"]

    parts = []

    parts.append(f'''<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{bg_top}"/>
    <stop offset="100%" stop-color="{bg_bottom}"/>
  </linearGradient>
  <linearGradient id="ab" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{accent}"/>
    <stop offset="100%" stop-color="{accent}" stop-opacity="0.6"/>
  </linearGradient>
  <filter id="sh" x="-10%" y="-10%" width="120%" height="120%">
    <feDropShadow dx="0" dy="6" stdDeviation="14" flood-color="#000" flood-opacity="0.1"/>
  </filter>
</defs>''')

    parts.append(f'<rect width="{w}" height="{h}" fill="url(#bg)"/>')
    parts.append(f'<circle cx="{w - 100}" cy="100" r="200" fill="{accent}" opacity="0.05"/>')
    parts.append(f'<circle cx="120" cy="{h - 120}" r="150" fill="{accent}" opacity="0.04"/>')
    parts.append(f'<rect width="{w}" height="8" fill="url(#ab)"/>')

    parts.append(f'''<text x="{w/2}" y="110" text-anchor="middle" font-size="64" fill="#0F172A" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="800">{card["title"]}</text>''')
    parts.append(f'''<text x="{w/2}" y="160" text-anchor="middle" font-size="32" fill="#64748B" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="500">{card["subtitle"]}</text>''')
    parts.append(f'''<rect x="{w/2 - 240}" y="190" width="480" height="56" rx="28" fill="{accent}" opacity="0.08"/>
<text x="{w/2}" y="228" text-anchor="middle" font-size="26" fill="{accent}" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="700">{card["tagline"]}</text>''')
    parts.append(f'<line x1="{w/2 - 140}" y1="260" x2="{w/2 + 140}" y2="260" stroke="{accent}" stroke-width="3" stroke-linecap="round" opacity="0.35"/>')

    section_start_y = 290
    section_h = 165
    section_gap = 24

    for si, section in enumerate(card["sections"]):
        sy = section_start_y + si * (section_h + section_gap)
        badge_w = 140
        parts.append(f'''<rect x="{w/2 - badge_w/2}" y="{sy}" width="{badge_w}" height="42" rx="21" fill="{accent}" opacity="0.12"/>
<text x="{w/2}" y="{sy + 29}" text-anchor="middle" font-size="22" fill="{accent}" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="700">{section["label"]}</text>''')

        item_start_y = sy + 60
        item_spacing = 42
        for ii, item in enumerate(section["items"]):
            iy = item_start_y + ii * item_spacing
            bullet_cx = w/2 - 230
            bullet_cy = iy + 12
            parts.append(f'''<circle cx="{bullet_cx}" cy="{bullet_cy}" r="7" fill="{accent}" opacity="0.75"/>
<text x="{w/2 - 205}" y="{iy + 20}" font-size="24" fill="#334155" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="500">{item}</text>''')

    rating_y = section_start_y + len(card["sections"]) * (section_h + section_gap) + 30
    parts.append(f'<line x1="{w/2 - 170}" y1="{rating_y}" x2="{w/2 + 170}" y2="{rating_y}" stroke="#E2E8F0" stroke-width="1.5"/>')
    parts.append(f'''<text x="{w/2}" y="{rating_y + 55}" text-anchor="middle" font-size="50" font-family="sans-serif">{card["rating"]}</text>''')

    label_y = rating_y + 100
    parts.append(f'''<rect x="{w/2 - 110}" y="{label_y}" width="220" height="42" rx="21" fill="{accent}" opacity="0.1"/>
<text x="{w/2}" y="{label_y + 29}" text-anchor="middle" font-size="22" fill="{accent}" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="600">{card["rating_label"]}</text>''')

    bottom_y = h - 55
    parts.append(f'''<rect x="{w/2 - 170}" y="{bottom_y - 24}" width="340" height="48" rx="24" fill="{accent}" opacity="0.08"/>
<text x="{w/2}" y="{bottom_y + 8}" text-anchor="middle" font-size="20" fill="#64748B" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="500">#AI工具 #PPT #效率提升</text>''')

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
  {' '.join(parts)}
</svg>'''
    return svg


def svg_for_cover(card):
    w, h = card["w"], card["h"]
    accent = card["accent"]
    bg_top = card["bg_top"]
    bg_bottom = card["bg_bottom"]
    tools = card["tools"]
    desc = card["desc"]

    parts = []

    parts.append(f'''<defs>
  <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{bg_top}"/>
    <stop offset="100%" stop-color="{bg_bottom}"/>
  </linearGradient>
  <linearGradient id="ab" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{accent}"/>
    <stop offset="100%" stop-color="{accent}" stop-opacity="0.5"/>
  </linearGradient>
  <filter id="sh" x="-10%" y="-10%" width="120%" height="120%">
    <feDropShadow dx="0" dy="8" stdDeviation="18" flood-color="#000" flood-opacity="0.12"/>
  </filter>
</defs>''')

    parts.append(f'<rect width="{w}" height="{h}" fill="url(#bg)"/>')
    parts.append(f'<circle cx="{w - 100}" cy="120" r="200" fill="{accent}" opacity="0.06"/>')
    parts.append(f'<circle cx="120" cy="{h - 120}" r="160" fill="{accent}" opacity="0.05"/>')
    parts.append(f'<circle cx="{w/2}" cy="{h/2}" r="300" fill="#FFFFFF" opacity="0.12"/>')
    parts.append(f'<rect width="{w}" height="8" fill="url(#ab)"/>')

    # === TITLE — EXTRA BIG ===
    parts.append(f'''<text x="{w/2}" y="145" text-anchor="middle" font-size="80" fill="#0F172A" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="800">{card["title"]}</text>''')

    # === SUBTITLE — BIG ===
    parts.append(f'''<text x="{w/2}" y="205" text-anchor="middle" font-size="36" fill="#64748B" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="500">{card["subtitle"]}</text>''')

    # Divider
    parts.append(f'<line x1="{w/2 - 160}" y1="245" x2="{w/2 + 160}" y2="245" stroke="{accent}" stroke-width="4" stroke-linecap="round" opacity="0.4"/>')

    # === 4 TOOL CARDS in 2x2 grid ===
    card_w = 360
    card_h = 210
    grid_start_x = (w - 2 * card_w - 60) / 2
    grid_start_y = 280

    for i, tool in enumerate(tools):
        row = i // 2
        col = i % 2
        cx = grid_start_x + col * (card_w + 60)
        cy = grid_start_y + row * (card_h + 45)

        parts.append(f'''<rect x="{cx}" y="{cy}" width="{card_w}" height="{card_h}" rx="24" fill="#FFFFFF" filter="url(#sh)"/>''')
        parts.append(f'''<rect x="{cx}" y="{cy}" width="{card_w}" height="8" rx="24" fill="{tool["color"]}"/>''')

        # Tool name — EXTRA BIG
        parts.append(f'''<text x="{cx + 35}" y="{cy + 75}" font-size="44" fill="{tool["color"]}" font-family="Arial, sans-serif" font-weight="800">{tool["name"]}</text>''')

        # Tag
        tag_w = 100
        tag_x = cx + (card_w - tag_w) / 2
        tag_y = cy + 115
        parts.append(f'''<rect x="{tag_x}" y="{tag_y}" width="{tag_w}" height="36" rx="18" fill="{tool["color"]}" opacity="0.12"/>
<text x="{cx + card_w/2}" y="{tag_y + 26}" text-anchor="middle" font-size="20" fill="{tool["color"]}" font-family="PingFang SC, sans-serif" font-weight="600">{tool["tag"]}</text>''')

        parts.append(f'''<text x="{cx + 25}" y="{cy + 175}" font-size="20" fill="#94A3B8" font-family="PingFang SC, sans-serif" font-weight="400">AI生成 / 智能排版</text>''')

    # Description line
    desc_y = grid_start_y + 2 * (card_h + 45) + 55
    parts.append(f'''<text x="{w/2}" y="{desc_y}" text-anchor="middle" font-size="24" fill="#64748B" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="500">{desc}</text>''')

    # Bottom tag
    bottom_y = h - 55
    parts.append(f'''<rect x="{w/2 - 170}" y="{bottom_y - 24}" width="340" height="48" rx="24" fill="{accent}" opacity="0.08"/>
<text x="{w/2}" y="{bottom_y + 8}" text-anchor="middle" font-size="20" fill="#64748B" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-weight="500">#AI工具 #PPT #效率提升</text>''')

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
  {' '.join(parts)}
</svg>'''
    return svg


def main():
    for card in CARDS:
        if card["name"] == "cover":
            svg = svg_for_cover(card)
        else:
            svg = svg_for_card(card)

        svg_path = os.path.join(OUT_DIR, f"{card['name']}.svg")
        with open(svg_path, "w") as f:
            f.write(svg)
        print(f"✅ {card['name']}.svg")

        png_path = os.path.join(OUT_DIR, f"{card['name']}.png")
        try:
            import subprocess
            subprocess.run(
                ["inkscape", svg_path, f"--export-filename={png_path}",
                 f"--export-width={card['w']}", f"--export-height={card['h']}"],
                check=True, capture_output=True, timeout=30
            )
            print(f"   → {card['name']}.png ({card['w']}×{card['h']})")
        except FileNotFoundError:
            print(f"   ⚠️  Inkscape not found")
        except Exception as e:
            print(f"   ⚠️  {e}")


if __name__ == "__main__":
    main()
