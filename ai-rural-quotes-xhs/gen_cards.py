#!/usr/bin/env python3

import subprocess
import os

W, H = 1024, 1024
BG = "#FAF7F2"
WHITE = "#FFFFFF"
TEXT_DARK = "#1E293B"
TEXT_MID = "#475569"
TEXT_LIGHT = "#94A3B8"

AMBER = "#B45309"
EMERALD = "#059669"
STONE = "#78350F"


def shadow_filter():
    return '''
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E1E3C" flood-opacity="0.06"/>
    </filter>
    '''


def cover():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="{BG}"/>
        <stop offset="100%" stop-color="#F3F0E8"/>
      </linearGradient>
      <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="{AMBER}"/>
        <stop offset="100%" stop-color="{EMERALD}"/>
      </linearGradient>
      {shadow_filter()}
    </defs>
    <rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

    <circle cx="120" cy="100" r="8" fill="{AMBER}" opacity="0.12"/>
    <circle cx="150" cy="95" r="5" fill="{EMERALD}" opacity="0.12"/>
    <circle cx="180" cy="100" r="8" fill="{AMBER}" opacity="0.12"/>

    <text x="60" y="200" font-size="80" font-weight="800" fill="url(#titleGrad)" font-family="PingFang SC, Microsoft YaHei, sans-serif">AI农村语录</text>
    <text x="60" y="290" font-size="40" font-weight="600" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">视频号冷门红利</text>

    <line x1="60" y1="340" x2="350" y2="340" stroke="{AMBER}" stroke-width="4" stroke-linecap="round" opacity="0.3"/>

    <text x="60" y="400" font-size="22" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">百万播放 · 广告分成 · AI批量生产</text>

    <rect x="60" y="460" width="904" height="100" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="90" y="500" font-size="28" font-weight="700" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">1万播放 ≈ 30-80元</text>
    <text x="90" y="540" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">百万播放 = 3000-8000元 · 日更3条月入过万</text>

    <rect x="60" y="600" width="904" height="80" rx="14" fill="{STONE}" opacity="0.06"/>
    <text x="100" y="640" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">5分钟一条 · 一人管10号 · 视频号流量扶持</text>
    <text x="100" y="668" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">现在入场还不晚</text>

    <rect x="60" y="720" width="280" height="48" rx="24" fill="{AMBER}" opacity="0.1"/>
    <text x="100" y="752" font-size="18" font-weight="600" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">中老年流量密码</text>

    <rect x="360" y="720" width="220" height="48" rx="24" fill="{EMERALD}" opacity="0.1"/>
    <text x="400" y="752" font-size="18" font-weight="600" fill="{EMERALD}" font-family="PingFang SC, Microsoft YaHei, sans-serif">AI批量生成</text>

    <rect x="600" y="720" width="200" height="48" rx="24" fill="{STONE}" opacity="0.1"/>
    <text x="630" y="752" font-size="18" font-weight="600" fill="{STONE}" font-family="PingFang SC, Microsoft YaHei, sans-serif">广告分成</text>

    <text x="60" y="860" font-size="16" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #视频号 #农村语录 #AI搞钱 #冷门红利</text>
  </svg>'''


def card_why():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      {shadow_filter()}
    </defs>

    <rect width="{W}" height="140" fill="{AMBER}" opacity="0.08"/>
    <text x="60" y="60" font-size="20" font-weight="600" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">CARD 01</text>
    <text x="60" y="105" font-size="44" font-weight="800" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">为什么是农村语录</text>

    <text x="60" y="180" font-size="22" font-weight="600" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">视频号主力用户：中老年人（40-65岁）占60%+</text>

    <rect x="60" y="220" width="904" height="220" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="90" y="265" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">语录示例（爆款公式）</text>
    <text x="90" y="310" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">"人穷别说话，位卑别劝人"</text>
    <text x="90" y="345" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">"亲戚不共财，共财两不来"</text>
    <text x="90" y="380" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">"宁得罪君子，不得罪小人"</text>

    <rect x="60" y="470" width="904" height="180" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="90" y="520" font-size="22" font-weight="700" fill="{EMERALD}" font-family="PingFang SC, Microsoft YaHei, sans-serif">为什么效果好</text>
    <text x="90" y="560" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">真实感强 · 共情度高 · 中老年人爱转发</text>
    <text x="90" y="595" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">完播率是娱乐内容的3-5倍</text>
    <text x="90" y="630" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">评论区全是"说得好""太对了"</text>

    <rect x="60" y="680" width="904" height="60" rx="14" fill="{TEXT_DARK}" opacity="0.04"/>
    <text x="100" y="720" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">一句话总结：农村语录 = 中老年流量密码</text>

    <text x="60" y="820" font-size="14" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#视频号 #农村语录 #中老年流量</text>
  </svg>'''


def card_how():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      {shadow_filter()}
    </defs>

    <rect width="{W}" height="140" fill="{EMERALD}" opacity="0.08"/>
    <text x="60" y="60" font-size="20" font-weight="600" fill="{EMERALD}" font-family="PingFang SC, Microsoft YaHei, sans-serif">CARD 02</text>
    <text x="60" y="105" font-size="44" font-weight="800" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">AI怎么做 5分钟/条</text>

    <rect x="60" y="170" width="904" height="380" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="90" y="215" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">全流程</text>

    <!-- Step 1 -->
    <text x="90" y="270" font-size="20" font-weight="600" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">01 文案 - DeepSeek/Claude</text>
    <text x="90" y="300" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">50-80字农村语录，模仿老人说话风格</text>

    <!-- Step 2 -->
    <text x="90" y="355" font-size="20" font-weight="600" fill="{EMERALD}" font-family="PingFang SC, Microsoft YaHei, sans-serif">02 配音 - 11Labs/火山引擎</text>
    <text x="90" y="385" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">中老年男声/女声，接地气（不用标准播音腔）</text>

    <!-- Step 3 -->
    <text x="90" y="440" font-size="20" font-weight="600" fill="{STONE}" font-family="PingFang SC, Microsoft YaHei, sans-serif">03 素材 - 免费素材/AI生图</text>
    <text x="90" y="470" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">农村实拍：田野/老屋/农具，风格统一</text>

    <!-- Step 4 -->
    <text x="90" y="525" font-size="20" font-weight="600" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">04 剪辑 - 剪映一键成片</text>
    <text x="90" y="555" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">文案+配音+背景乐+字幕，5分钟一条</text>

    <rect x="60" y="580" width="904" height="120" rx="14" fill="{EMERALD}" opacity="0.06"/>
    <text x="100" y="625" font-size="20" font-weight="700" fill="{EMERALD}" font-family="PingFang SC, Microsoft YaHei, sans-serif">关键技巧</text>
    <text x="100" y="660" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• 语录要有"反差感"：先情绪张力，再用道理收尾</text>
    <text x="100" y="690" font-size="18" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• 封面大字标题 + 老人头像（免费素材库有）</text>

    <text x="60" y="800" font-size="14" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI视频 #剪映 #AI配音 #视频号创作</text>
  </svg>'''


def card_money():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      {shadow_filter()}
    </defs>

    <rect width="{W}" height="140" fill="{STONE}" opacity="0.08"/>
    <text x="60" y="60" font-size="20" font-weight="600" fill="{STONE}" font-family="PingFang SC, Microsoft YaHei, sans-serif">CARD 03</text>
    <text x="60" y="105" font-size="44" font-weight="800" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">收益有多大</text>

    <rect x="60" y="180" width="430" height="140" rx="16" fill="{AMBER}" opacity="0.08"/>
    <text x="90" y="225" font-size="18" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">1万播放</text>
    <text x="90" y="285" font-size="36" font-weight="800" fill="{AMBER}" font-family="PingFang SC, Microsoft YaHei, sans-serif">30-80元</text>

    <rect x="530" y="180" width="434" height="140" rx="16" fill="{EMERALD}" opacity="0.08"/>
    <text x="560" y="225" font-size="18" fill="{EMERALD}" font-family="PingFang SC, Microsoft YaHei, sans-serif">百万播放</text>
    <text x="560" y="285" font-size="36" font-weight="800" fill="{EMERALD}" font-family="PingFang SC, Microsoft YaHei, sans-serif">3000-8000元</text>

    <rect x="60" y="360" width="904" height="180" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="90" y="410" font-size="22" font-weight="700" fill="{TEXT_DARK}" font-family="PingFang SC, Microsoft YaHei, sans-serif">运营模型</text>
    <text x="90" y="455" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• 日更3条，月播放稳定200-500万</text>
    <text x="90" y="490" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• 月收入3000+（稳定号）</text>
    <text x="90" y="525" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• 爆一条百万级视频 = 直接破万</text>

    <rect x="60" y="580" width="904" height="180" rx="14" fill="{STONE}" opacity="0.06"/>
    <text x="100" y="625" font-size="22" font-weight="700" fill="{STONE}" font-family="PingFang SC, Microsoft YaHei, sans-serif">为什么现在入场</text>
    <text x="100" y="665" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• 视频号流量扶持新人，冷启动快</text>
    <text x="100" y="700" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• 农村语录赛道还没卷起来</text>
    <text x="100" y="735" font-size="20" fill="{TEXT_MID}" font-family="PingFang SC, Microsoft YaHei, sans-serif">• AI批量生产，一个人管10个号</text>

    <text x="60" y="840" font-size="14" fill="{TEXT_LIGHT}" font-family="PingFang SC, Microsoft YaHei, sans-serif">#AI副业 #搞钱 #视频号分成 #冷门红利</text>
  </svg>'''


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)

    svgs = [
        ("ai-rural-quotes-cover.svg", cover()),
        ("ai-rural-quotes-card-why.svg", card_why()),
        ("ai-rural-quotes-card-how.svg", card_how()),
        ("ai-rural-quotes-card-money.svg", card_money()),
    ]

    for name, svg in svgs:
        path = os.path.join(out_dir, name)
        with open(path, "w") as f:
            f.write(svg)
        print(f"✅ {path}")

    print("\n🎨 Rendering PNGs with Inkscape...")
    for name, _ in svgs:
        svg_path = os.path.join(out_dir, name)
        png_file = name.replace(".svg", ".png")
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
