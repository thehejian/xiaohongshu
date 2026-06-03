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

# Brand colors for each path
COLORS = {
    "write":  "#6366F1",  # indigo - AI写稿
    "draw":   "#EC4899",  # pink   - AI头像
    "ppt":    "#F59E0B",  # amber  - AI PPT
}

def shadow_filter():
    return """
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E1E3C" flood-opacity="0.06"/>
    </filter>
    """

def card(x, y, w, h, color, title, desc, price, icon_text):
    """Draw a single card with left color bar."""
    return f'''
    <!-- Card background -->
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <!-- Left color bar -->
    <rect x="{x}" y="{y}" width="8" height="{h}" rx="4" fill="{color}"/>
    <!-- Icon circle -->
    <circle cx="{x + 70}" cy="{y + 70}" r="36" fill="{color}" opacity="0.12"/>
    <text x="{x + 70}" y="{y + 82}" font-size="32" text-anchor="middle" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{icon_text}</text>
    <!-- Title -->
    <text x="{x + 120}" y="{y + 72}" font-size="36" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{title}</text>
    <!-- Description -->
    <text x="{x + 40}" y="{y + 130}" font-size="22" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{desc}</text>
    <!-- Price tag -->
    <rect x="{x + 40}" y="{y + h - 80}" width="180" height="44" rx="22" fill="{color}" opacity="0.1"/>
    <text x="{x + 52}" y="{y + h - 52}" font-size="22" font-weight="600" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{price}</text>
    <!-- Bottom tag -->
    <rect x="{x + w - 170}" y="{y + h - 80}" width="130" height="44" rx="22" fill="{TEXT_DARK}" opacity="0.06"/>
    <text x="{x + w - 105}" y="{y + h - 52}" font-size="18" text-anchor="middle" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">适合新手</text>
    '''

def cover():
    """Cover card: title + 3 path highlights."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <!-- Subtle gradient overlay -->
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

    <!-- Top decorative dots -->
    <circle cx="100" cy="100" r="6" fill="#6366F1" opacity="0.15"/>
    <circle cx="130" cy="100" r="6" fill="#EC4899" opacity="0.15"/>
    <circle cx="160" cy="100" r="6" fill="#F59E0B" opacity="0.15"/>

    <!-- Title -->
    <text x="60" y="220" font-size="72" font-weight="800" fill="url(#titleGrad)" font-family="PingFang SC, Microsoft YaHei, sans-serif">AI搞钱</text>
    <text x="60" y="310" font-size="42" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">3条普通人能接的路</text>

    <!-- Divider line -->
    <line x1="60" y1="360" x2="400" y2="360" stroke="#6366F1" stroke-width="4" stroke-linecap="round" opacity="0.3"/>

    <!-- 3 Path cards -->
    {card(60, 400, 280, 260, COLORS["write"], "AI写稿接单", "小红书/公众号代写", "50-300元/篇", "✍️")}
    {card(380, 400, 280, 260, COLORS["draw"], "AI做头像", "头像/壁纸/表情包", "10-198元/张", "🎨")}
    {card(700, 400, 280, 260, COLORS["ppt"], "AI做PPT", "汇报/课件/路演", "100-500元/套", "📊")}

    <!-- Bottom note -->
    <rect x="60" y="700" width="904" height="80" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="735" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">门槛低 · 靠量积累 · 月入2k-5k不难</text>
    <text x="100" y="765" font-size="18" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">从最顺手的开始，别贪多</text>

    <!-- Footer tags -->
    <text x="60" y="840" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #搞钱 #自由职业 #AI写稿 #AI绘画 #AI PPT</text>
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
    <text x="60" y="70" font-size="22" font-weight="600" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">PATH 0{["write","draw","ppt"].index(path_name)+1}</text>
    <text x="60" y="110" font-size="48" font-weight="800" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{title}</text>

    <!-- Main icon -->
    <circle cx="120" cy="260" r="70" fill="{color}" opacity="0.12"/>
    <text x="120" y="280" font-size="56" text-anchor="middle" font-family="Apple Color Emoji, sans-serif">{icon}</text>

    <!-- Description -->
    <text x="230" y="240" font-size="26" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{desc}</text>
    <text x="230" y="280" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">接单平台：闲鱼 / 小红书 / 朋友圈</text>

    <!-- Price box -->
    <rect x="60" y="330" width="300" height="90" rx="16" fill="{color}" opacity="0.1"/>
    <text x="80" y="365" font-size="18" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">定价参考</text>
    <text x="80" y="405" font-size="36" font-weight="700" fill="{color}" font-family="PingFang SC, Microsoft YaHei, sans-serif">{price}</text>

    <!-- Tips section -->
    <rect x="60" y="460" width="904" height="280" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="510" font-size="24" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">💡 关键技巧</text>

    <!-- Tips lines -->
    {"".join(f'<text x="100" y="{600+i*55}" font-size="22" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• {tip}</text>' for i, tip in enumerate(tips))}

    <!-- Bottom note -->
    <rect x="60" y="780" width="904" height="70" rx="14" fill="{TEXT_DARK}" opacity="0.04"/>
    <text x="100" y="822" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">适合：审美在线 · prompt熟练 · 出图快</text>

    <!-- Footer -->
    <text x="60" y="900" font-size="15" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #搞钱 #自由职业</text>
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

    # Render SVG → PNG with Inkscape
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

    print("\n✨ Done! All cards generated.")


if __name__ == "__main__":
    main()
