#!/usr/bin/env python3
"""Generate XHS-style cards for AI side hustle topic.
Light style: cream bg #FAF7F2, white cards, brand accent colors.
"""

import subprocess
import os
import sys

W, H = 1024, 1024
BG = "#FAF7F2"
WHITE = "#FFFFFF"
TEXT_DARK = "#1A1A2E"
TEXT_MID = "#4A4A68"
TEXT_LIGHT = "#8888A0"
SHADOW = "0 8px 32px rgba(30, 30, 60, 0.06)"

COLORS = {
    "write": "#6366F1",
    "draw":  "#EC4899",
    "ppt":   "#F59E0B",
}


def shadow_filter():
    return """
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E1E3C" flood-opacity="0.06"/>
    </filter>
    """


def card(x, y, w, h, color, title, desc, price, icon_text):
    """Draw a single card with left color bar.
    Layout (h=260):
      y+30   icon circle (r=24, cy=y+58) + emoji
      y+58   title (fs=26, x starts at 100, clear of icon)
      y+100  description (fs=18)
      y+h-85 price tag (left) + bottom tag (right)
    """
    icon_cy = y + 58
    icon_r = 22
    icon_emoji_y = y + 66
    title_y = y + 62
    desc_y = y + 100
    tag_y = y + h - 85
    tag_text_y = y + h - 61

    return f'''
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="{x}" y="{y}" width="8" height="{h}" rx="4" fill="{color}"/>
    <circle cx="{x + 56}" cy="{icon_cy}" r="{icon_r}" fill="{color}" opacity="0.12"/>
    <text x="{x + 56}" y="{icon_emoji_y}" font-size="22" text-anchor="middle" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{icon_text}</text>
    <text x="{x + 96}" y="{title_y}" font-size="26" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{title}</text>
    <text x="{x + 30}" y="{desc_y}" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{desc}</text>
    <rect x="{x + 30}" y="{tag_y}" width="140" height="38" rx="19" fill="{color}" opacity="0.1"/>
    <text x="{x + 42}" y="{tag_text_y}" font-size="16" font-weight="600" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{price}</text>
    <rect x="{x + w - 130}" y="{tag_y}" width="100" height="38" rx="19" fill="{TEXT_DARK}" opacity="0.06"/>
    <text x="{x + w - 80}" y="{tag_text_y}" font-size="15" text-anchor="middle" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">适合新手</text>
    '''


def cover():
    """Cover card: title + 3 path cards."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="{BG}"/>
        <stop offset="100%" stop-color="#F3F0E8"/>
      </linearGradient>
      <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#6366F1"/>
        <stop offset="50%" stop-color="#EC4899"/>
        <stop offset="100%" stop-color="#F59E0B"/>
      </linearGradient>
      {shadow_filter()}
    </defs>
    <rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

    <!-- Decorative dots -->
    <circle cx="100" cy="90" r="6" fill="#6366F1" opacity="0.15"/>
    <circle cx="130" cy="90" r="6" fill="#EC4899" opacity="0.15"/>
    <circle cx="160" cy="90" r="6" fill="#F59E0B" opacity="0.15"/>

    <!-- Main title -->
    <text x="60" y="180" font-size="72" font-weight="800" fill="url(#titleGrad)" font-family="PingFang SC, Microsoft YaHei, sans-serif">AI搞钱</text>
    <text x="60" y="270" font-size="38" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">3条普通人能接的路</text>

    <!-- Divider -->
    <line x1="60" y1="310" x2="400" y2="310" stroke="#6366F1" stroke-width="4" stroke-linecap="round" opacity="0.3"/>

    <!-- 3 Path cards -->
    {card(60, 380, 280, 260, COLORS["write"], "AI写稿接单", "小红书/公众号代写", "50-300元/篇", "✍️")}
    {card(380, 380, 280, 260, COLORS["draw"], "AI做头像", "头像/壁纸/表情包", "10-198元/张", "🎨")}
    {card(700, 380, 280, 260, COLORS["ppt"], "AI做PPT", "汇报/课件/路演", "100-500元/套", "📊")}

    <!-- Bottom note -->
    <rect x="60" y="680" width="904" height="80" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="715" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">门槛低 · 靠量积累 · 月入2k-5k不难</text>
    <text x="100" y="748" font-size="18" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">从最顺手的开始，别贪多</text>

    <!-- Footer -->
    <text x="60" y="820" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #搞钱 #自由职业 #AI写稿 #AI绘画 #AI PPT</text>
  </svg>'''


def path_card(path_name, title, desc, price, icon, tips):
    """Single path detail card."""
    color = COLORS[path_name]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      {shadow_filter()}
    </defs>

    <!-- Top bar -->
    <rect width="{W}" height="140" fill="{color}" opacity="0.08"/>
    <text x="60" y="60" font-size="20" font-weight="600" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">PATH 0{["write","draw","ppt"].index(path_name)+1}</text>
    <text x="60" y="105" font-size="44" font-weight="800" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{title}</text>

    <!-- Icon (left column) -->
    <circle cx="120" cy="360" r="65" fill="{color}" opacity="0.12"/>
    <text x="120" y="380" font-size="52" text-anchor="middle" font-family="Apple Color Emoji, sans-serif">{icon}</text>

    <!-- Description (right column) -->
    <text x="230" y="220" font-size="24" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{desc}</text>
    <text x="230" y="258" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">接单平台：闲鱼 / 小红书 / 朋友圈</text>

    <!-- Price box -->
    <rect x="60" y="400" width="300" height="120" rx="16" fill="{color}" opacity="0.1"/>
    <text x="80" y="438" font-size="16" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">定价参考</text>
    <text x="80" y="490" font-size="32" font-weight="700" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{price}</text>

    <!-- Tips section -->
    <rect x="60" y="540" width="904" height="255" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="585" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">💡 关键技巧</text>
    {"".join(f'<text x="100" y="{635+i*45}" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• {tip}</text>' for i, tip in enumerate(tips))}

    <!-- Bottom note -->
    <rect x="60" y="820" width="904" height="60" rx="14" fill="{TEXT_DARK}" opacity="0.04"/>
    <text x="100" y="858" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">适合：审美在线 · prompt熟练 · 出图快</text>

    <!-- Footer -->
    <text x="60" y="900" font-size="14" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #搞钱 #自由职业</text>
  </svg>'''


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)

    # Cover
    svg = cover()
    svg_path = os.path.join(out_dir, "ai-side-hustle-square.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    print(f"✅ {svg_path}")

    # Path cards
    cards = [
        ("write", "AI写稿接单", "小红书/公众号/知乎代写", "50-300元/篇", "✍️", [
            "用Claude写初稿，人工润色",
            "客户要的是结果，不是过程",
            "效率翻倍，一天能接3-5单",
            "前期靠量，后期靠复购",
        ]),
        ("draw", "AI做头像定制", "头像/壁纸/表情包全套", "10-198元/张", "🎨", [
            "Midjourney v6出图，风格统一",
            "prompt模板化，5分钟4张备选",
            "表情包要表情丰富、动作夸张",
            '小红书搜"AI头像定制"需求大',
        ]),
        ("ppt", "AI做PPT", "企业汇报/课件/路演", "100-500元/套", "📊", [
            "Gamma / 讯飞智文 10分钟出稿",
            "积累行业模板：科技/教育/金融",
            "改稿控制在2轮内，效率关键",
            "数据可视化能力是加分项",
        ]),
    ]

    for name, title, desc, price, icon, tips in cards:
        svg = path_card(name, title, desc, price, icon, tips)
        svg_path = os.path.join(out_dir, f"ai-side-hustle-card-{name}.svg")
        with open(svg_path, "w") as f:
            f.write(svg)
        print(f"✅ {svg_path}")

    # Render SVG → PNG
    print("\n🎨 Rendering PNGs with Inkscape...")
    for svg_file in ["ai-side-hustle-square.svg",
                      "ai-side-hustle-card-write.svg",
                      "ai-side-hustle-card-draw.svg",
                      "ai-side-hustle-card-ppt.svg"]:
        svg_path = os.path.join(out_dir, svg_file)
        png_file = svg_file.replace(".svg", ".png")
        png_path = os.path.join(out_dir, png_file)
        result = subprocess.run(
            ["inkscape", svg_path, "--export-type=png",
             f"--export-filename={png_path}", "-w", str(W), "-h", str(H)],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0 and os.path.getsize(png_path) > 50000:
            print(f"✅ {png_file} ({os.path.getsize(png_path)//1024}KB)")
        else:
            print(f"❌ {png_file} — {result.stderr[:200] if result.stderr else 'blank/small file'}")

    print("\n✨ Done!")


if __name__ == "__main__":
    main()
