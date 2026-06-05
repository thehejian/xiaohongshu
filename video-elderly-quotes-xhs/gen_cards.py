#!/usr/bin/env python3
"""Generate XHS-style cards for AI elderly quotes trend topic.
Light style: cream bg #FAF7F2, white cards, brand accent colors.
"""

import subprocess
import os

W, H = 1024, 1024
BG = "#FAF7F2"
WHITE = "#FFFFFF"
TEXT_DARK = "#1E293B"
TEXT_MID = "#475569"
TEXT_LIGHT = "#94A3B8"

COLORS = {
    "purple": "#7C3AED",
    "rose":  "#E11D48",
    "amber": "#D97706",
    "teal":  "#0D9488",
}


def shadow_filter():
    return """
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E1E3C" flood-opacity="0.06"/>
    </filter>
    """


def cover():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="{BG}"/>
        <stop offset="100%" stop-color="#F3F0E8"/>
      </linearGradient>
      <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="{COLORS['purple']}"/>
        <stop offset="50%" stop-color="{COLORS['rose']}"/>
        <stop offset="100%" stop-color="{COLORS['amber']}"/>
      </linearGradient>
      {shadow_filter()}
    </defs>
    <rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

    <!-- Decorative circles -->
    <circle cx="90" cy="90" r="50" fill="{COLORS['purple']}" opacity="0.06"/>
    <circle cx="150" cy="80" r="20" fill="{COLORS['rose']}" opacity="0.08"/>
    <circle cx="190" cy="110" r="12" fill="{COLORS['amber']}" opacity="0.1"/>

    <!-- Main title -->
    <text x="60" y="200" font-size="72" font-weight="800" fill="url(#titleGrad)" font-family="PingFang SC, Microsoft YaHei, sans-serif">AI老人语录</text>
    <text x="60" y="290" font-size="38" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">视频号月入过万红利</text>

    <!-- Subtitle -->
    <line x1="60" y1="330" x2="500" y2="330" stroke="{COLORS['purple']}" stroke-width="4" stroke-linecap="round" opacity="0.25"/>
    <text x="60" y="380" font-size="24" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">GPT 模写莫言体 + AI 头像 + 慢 BGM</text>
    <text x="60" y="420" font-size="22" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">中老年人爱转，一条视频几十万播放</text>

    <!-- 4 step cards row -->
    <!-- Step 1: GPT -->
    <rect x="60" y="480" width="210" height="200" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="165" cy="520" r="28" fill="{COLORS['purple']}" opacity="0.12"/>
    <text x="165" y="530" font-size="28" text-anchor="middle" fill="{COLORS['purple']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">GPT</text>
    <text x="80" y="580" font-size="18" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">模写莫言体</text>
    <text x="80" y="610" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">投喂名作风范</text>
    <text x="80" y="635" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">输出人生金句</text>

    <!-- Step 2: AI Avatar -->
    <rect x="290" y="480" width="210" height="200" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="395" cy="520" r="28" fill="{COLORS['rose']}" opacity="0.12"/>
    <text x="395" y="530" font-size="28" text-anchor="middle" fill="{COLORS['rose']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">MJ</text>
    <text x="310" y="580" font-size="18" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">AI老人头像</text>
    <text x="310" y="610" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">逼真慈眉善目</text>
    <text x="310" y="635" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">以为是真人在线</text>

    <!-- Step 3: BGM -->
    <rect x="520" y="480" width="210" height="200" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="625" cy="520" r="28" fill="{COLORS['amber']}" opacity="0.12"/>
    <text x="625" y="530" font-size="28" text-anchor="middle" fill="{COLORS['amber']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">BGM</text>
    <text x="540" y="580" font-size="18" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">慢节奏配乐</text>
    <text x="540" y="610" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">抒情钢琴古筝</text>
    <text x="540" y="635" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">贴合中老年审美</text>

    <!-- Step 4: Distribute -->
    <rect x="750" y="480" width="210" height="200" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="855" cy="520" r="28" fill="{COLORS['teal']}" opacity="0.12"/>
    <text x="855" y="530" font-size="28" text-anchor="middle" fill="{COLORS['teal']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">发</text>
    <text x="770" y="580" font-size="18" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">视频号分发</text>
    <text x="770" y="610" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">精准触达</text>
    <text x="770" y="635" font-size="15" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">45-65岁人群</text>

    <!-- Bottom CTA -->
    <rect x="60" y="720" width="904" height="80" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="755" font-size="22" font-weight="700" fill="{COLORS['purple']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">GPT + MJ + 剪映，新手1小时上手</text>
    <text x="100" y="788" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">关键是内容被长辈惦记着转发</text>

    <!-- Footer -->
    <text x="60" y="880" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #微信视频号 #AI语录 #中老年流量 #搞钱</text>
  </svg>'''


def workflow_card():
    """Detail card: the 4-step workflow."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      {shadow_filter()}
    </defs>

    <!-- Top bar -->
    <rect width="{W}" height="140" fill="{COLORS['purple']}" opacity="0.08"/>
    <text x="60" y="60" font-size="20" font-weight="600" fill="{COLORS['purple']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">STEP BY STEP</text>
    <text x="60" y="105" font-size="44" font-weight="800" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">完整套路拆解</text>

    <!-- Step 1 -->
    <rect x="60" y="170" width="904" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="60" y="170" width="8" height="120" rx="4" fill="{COLORS['purple']}"/>
    <text x="100" y="210" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">01 GPT模写莫言体</text>
    <text x="100" y="245" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">投喂5-10篇莫言/余华语录，GPT模仿风范输出15-30字哲理金句</text>
    <text x="100" y="275" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">关键：短小精悍，适合视频展示</text>

    <!-- Step 2 -->
    <rect x="60" y="310" width="904" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="60" y="310" width="8" height="120" rx="4" fill="{COLORS['rose']}"/>
    <text x="100" y="350" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">02 AI生成老人头像</text>
    <text x="100" y="385" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">Midjourney生成慈眉善目老人形象，真实到中老年用户以为是真人</text>
    <text x="100" y="415" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">关键：不同视频换不同头像，避免被识别</text>

    <!-- Step 3 -->
    <rect x="60" y="450" width="904" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="60" y="450" width="8" height="120" rx="4" fill="{COLORS['amber']}"/>
    <text x="100" y="490" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">03 配慢节奏BGM</text>
    <text x="100" y="525" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">抒情钢琴曲或古筝二胡，节奏舒缓，音量偏低不盖过语音</text>
    <text x="100" y="555" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">关键：中老年偏好舒缓怀旧风格</text>

    <!-- Step 4 -->
    <rect x="60" y="590" width="904" height="120" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="60" y="590" width="8" height="120" rx="4" fill="{COLORS['teal']}"/>
    <text x="100" y="630" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">04 视频号精准分发</text>
    <text x="100" y="665" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">算法触达45-65岁人群，社交裂变转发率极高</text>
    <text x="100" y="695" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">关键：一条爆了持续推流3-7天</text>

    <!-- Bottom insight -->
    <rect x="60" y="740" width="904" height="80" rx="16" fill="{COLORS['purple']}" opacity="0.08"/>
    <text x="100" y="775" font-size="20" font-weight="600" fill="{COLORS['purple']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">情感共鸣 + 权威背书 = 高转发</text>
    <text x="100" y="805" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">长辈以为是"莫言本人语录"，天然可信</text>

    <!-- Footer -->
    <text x="60" y="880" font-size="14" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #微信视频号 #AI语录 #中老年流量 #搞钱</text>
  </svg>'''


def money_card():
    """Detail card: monetization methods."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      {shadow_filter()}
    </defs>

    <!-- Top bar -->
    <rect width="{W}" height="140" fill="{COLORS['amber']}" opacity="0.08"/>
    <text x="60" y="60" font-size="20" font-weight="600" fill="{COLORS['amber']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">MONEY</text>
    <text x="60" y="105" font-size="44" font-weight="800" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">4种变现方式</text>

    <!-- Method 1 -->
    <rect x="60" y="180" width="904" height="90" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="110" cy="225" r="24" fill="{COLORS['purple']}" opacity="0.12"/>
    <text x="110" y="232" font-size="20" text-anchor="middle" fill="{COLORS['purple']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">1</text>
    <text x="150" y="218" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">视频号带货</text>
    <text x="150" y="252" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">挂图书 / 保健品 / 养生品链接，佣金5-20%</text>

    <!-- Method 2 -->
    <rect x="60" y="290" width="904" height="90" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="110" cy="335" r="24" fill="{COLORS['rose']}" opacity="0.12"/>
    <text x="110" y="342" font-size="20" text-anchor="middle" fill="{COLORS['rose']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">2</text>
    <text x="150" y="328" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">引流私域</text>
    <text x="150" y="362" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">引导加微信，卖课程 / 社群会员，99-499元/人</text>

    <!-- Method 3 -->
    <rect x="60" y="400" width="904" height="90" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="110" cy="445" r="24" fill="{COLORS['amber']}" opacity="0.12"/>
    <text x="110" y="452" font-size="20" text-anchor="middle" fill="{COLORS['amber']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">3</text>
    <text x="150" y="438" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">流量主收益</text>
    <text x="150" y="472" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">视频号广告分成，万次播放30-80元</text>

    <!-- Method 4 -->
    <rect x="60" y="510" width="904" height="90" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="110" cy="555" r="24" fill="{COLORS['teal']}" opacity="0.12"/>
    <text x="110" y="562" font-size="20" text-anchor="middle" fill="{COLORS['teal']}" font-family="PingFang SC, Microsoft YaHei, sans-serif">4</text>
    <text x="150" y="548" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">做号转手</text>
    <text x="150" y="582" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">做出粉丝量后卖号，1-5万元/号</text>

    <!-- Tips section -->
    <rect x="60" y="630" width="904" height="180" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="670" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">实操建议</text>
    <text x="100" y="710" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">每天发3-5条，测试哪类语录数据好</text>
    <text x="100" y="740" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">同一段话换不同头像/BGM发布</text>
    <text x="100" y="770" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">不要直接写莫言说，用一位老人说避免侵权</text>
    <text x="100" y="800" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">评论区用小号互动大师说得对</text>

    <!-- Footer -->
    <text x="60" y="880" font-size="14" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #微信视频号 #AI语录 #中老年流量 #搞钱</text>
  </svg>'''


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))

    # Cover
    svg = cover()
    svg_path = os.path.join(out_dir, "ai-elderly-cover.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    print(f"Done {svg_path}")

    # Workflow card
    svg = workflow_card()
    svg_path = os.path.join(out_dir, "ai-elderly-workflow.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    print(f"Done {svg_path}")

    # Money card
    svg = money_card()
    svg_path = os.path.join(out_dir, "ai-elderly-money.svg")
    with open(svg_path, "w") as f:
        f.write(svg)
    print(f"Done {svg_path}")

    # Render SVG -> PNG
    print("\nRendering PNGs with Inkscape...")
    for svg_file in ["ai-elderly-cover.svg",
                      "ai-elderly-workflow.svg",
                      "ai-elderly-money.svg"]:
        svg_path = os.path.join(out_dir, svg_file)
        png_file = svg_file.replace(".svg", ".png")
        png_path = os.path.join(out_dir, png_file)
        result = subprocess.run(
            ["inkscape", svg_path, "--export-type=png",
             f"--export-filename={png_path}", "-w", str(W), "-h", str(H)],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0 and os.path.getsize(png_path) > 50000:
            print(f"OK {png_file} ({os.path.getsize(png_path)//1024}KB)")
        else:
            print(f"FAIL {png_file} - {result.stderr[:200] if result.stderr else 'blank/small file'}")

    print("\nDone!")


if __name__ == "__main__":
    main()