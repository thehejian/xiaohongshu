import subprocess, os

ROOT = os.path.dirname(os.path.abspath(__file__))

BG = "#FAF7F2"
CARD_BG = "#F3EFE8"
TEXT = "#1E293B"
SUB = "#64748B"
RED = "#DC2626"
RED_BG = "#FEF2F2"
RED_BORDER = "#FECACA"
ORANGE = "#EA580C"
ORANGE_BG = "#FFF7ED"
ORANGE_BORDER = "#FED7AA"
PURPLE = "#7C3AED"
PURPLE_BG = "#F5F3FF"
PURPLE_BORDER = "#DDD6FE"
GREEN = "#059669"
GREEN_BG = "#ECFDF5"
GREEN_BORDER = "#A7F3D0"

FONT = "PingFang SC,Heiti SC,STHeiti,Hiragino Sans GB,Microsoft YaHei,sans-serif"
FONT_EN = "Inter,Helvetica,Arial,sans-serif"

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs>
<linearGradient id="bgG" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="{BG}"/>
<stop offset="100%" stop-color="#F0EBE3"/>
</linearGradient>
</defs>
<rect width="{w}" height="{h}" fill="url(#bgG)"/>
{body}
</svg>'''

def cover():
    return svg_wrap(1024, 1024, f'''
<rect x="0" y="0" width="1024" height="1024" fill="none"/>
<g transform="translate(512, 512)">
<rect x="-340" y="-200" width="680" height="400" rx="24" fill="{CARD_BG}" stroke="#E2D9CC" stroke-width="1"/>
<text x="0" y="-60" text-anchor="middle" font-family="{FONT}" font-size="64" font-weight="900" fill="{TEXT}" letter-spacing="-2">Anthropic</text>
<text x="0" y="20" text-anchor="middle" font-family="{FONT}" font-size="64" font-weight="900" fill="{TEXT}" letter-spacing="-2">封禁大反转</text>
<rect x="-120" y="55" width="240" height="40" rx="20" fill="{RED}" opacity="0.1" stroke="{RED}" stroke-width="1"/>
<text x="0" y="81" text-anchor="middle" font-family="{FONT}" font-size="18" font-weight="700" fill="{RED}">24小时滑跪道歉</text>
<text x="0" y="140" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="500" fill="{SUB}">从封禁者→被封禁者</text>
<text x="0" y="175" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="500" fill="{SUB}">AI圈一周剧情大反转</text>
</g>
<text x="512" y="940" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">#Anthropic #Fable5 #AI封禁</text>
''')

def card_1():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="70" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="900" fill="{TEXT}">6月9日 偷偷降智</text>
<text x="512" y="105" text-anchor="middle" font-family="{FONT}" font-size="20" fill="{SUB}">Fable 5发布，319页说明书藏玄机</text>

<g transform="translate(62, 140)">
<rect x="0" y="0" width="900" height="180" rx="16" fill="{RED_BG}" stroke="{RED_BORDER}" stroke-width="1"/>
<circle cx="50" cy="50" r="24" fill="{RED}" opacity="0.15"/>
<text x="50" y="57" text-anchor="middle" font-family="{FONT_EN}" font-size="20" font-weight="800" fill="{RED}">!</text>
<text x="90" y="48" font-family="{FONT}" font-size="28" font-weight="800" fill="{RED}">静默降级机制</text>
<text x="90" y="85" font-family="{FONT}" font-size="20" font-weight="500" fill="{TEXT}">检测到蒸馏行为 → 自动回退到Opus 4.8</text>
<text x="90" y="115" font-family="{FONT}" font-size="18" fill="{SUB}">用户完全不知情，以为还在用最强模型</text>
<text x="90" y="155" font-family="{FONT}" font-size="18" fill="{RED}" opacity="0.7">核心争议：不是不让限制，是凭什么偷偷来？</text>
</g>

<g transform="translate(62, 350)">
<rect x="0" y="0" width="900" height="180" rx="16" fill="{CARD_BG}" stroke="#E2D9CC" stroke-width="1"/>
<circle cx="50" cy="50" r="24" fill="{ORANGE}" opacity="0.15"/>
<text x="50" y="57" text-anchor="middle" font-family="{FONT_EN}" font-size="20" font-weight="800" fill="{ORANGE}">3</text>
<text x="90" y="48" font-family="{FONT}" font-size="28" font-weight="800" fill="{TEXT}">319页系统说明书</text>
<text x="90" y="85" font-family="{FONT}" font-size="20" font-weight="500" fill="{TEXT}">藏在不起眼的角落，像一颗定时炸弹</text>
<text x="90" y="115" font-family="{FONT}" font-size="18" fill="{SUB}">网友逐行阅读，终于发现了这条骚操作</text>
<text x="90" y="155" font-family="{FONT}" font-size="18" fill="{SUB}">社区连夜AB测试验证，24小时内引爆全球</text>
</g>

<g transform="translate(62, 560)">
<rect x="0" y="0" width="900" height="120" rx="16" fill="{PURPLE_BG}" stroke="{PURPLE_BORDER}" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{PURPLE}">🔥 话题登上全球X/Twitter趋势</text>
<text x="40" y="85" font-family="{FONT}" font-size="18" fill="{SUB}">开发者集体抗议：Anthropic涉嫌不道德行为</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">来源: Reddit, Twitter, 36氪</text>
''')

def card_2():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="70" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="900" fill="{TEXT}">6月11日 24小时道歉</text>
<text x="512" y="105" text-anchor="middle" font-family="{FONT}" font-size="20" fill="{SUB}">Anthropic连夜滑跪反转</text>

<g transform="translate(62, 140)">
<rect x="0" y="0" width="900" height="180" rx="16" fill="{GREEN_BG}" stroke="{GREEN_BORDER}" stroke-width="1"/>
<circle cx="50" cy="50" r="24" fill="{GREEN}" opacity="0.15"/>
<text x="50" y="57" text-anchor="middle" font-family="{FONT_EN}" font-size="20" font-weight="800" fill="{GREEN}">✓</text>
<text x="90" y="48" font-family="{FONT}" font-size="28" font-weight="800" fill="{GREEN}">撤销隐蔽降智政策</text>
<text x="90" y="85" font-family="{FONT}" font-size="20" font-weight="500" fill="{TEXT}">以后被标记的请求会明确通知用户</text>
<text x="90" y="115" font-family="{FONT}" font-size="18" fill="{SUB}">"你的请求已回退到Opus 4.8"</text>
<text x="90" y="155" font-family="{FONT}" font-size="18" fill="{GREEN}" opacity="0.7">API端返回明确的拒绝原因</text>
</g>

<g transform="translate(62, 350)">
<rect x="0" y="0" width="900" height="180" rx="16" fill="{CARD_BG}" stroke="#E2D9CC" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="24" font-weight="700" fill="{TEXT}">官方道歉原文：</text>
<text x="40" y="85" font-family="{FONT}" font-size="20" font-weight="500" fill="{SUB}">"We made the wrong tradeoff, and we</text>
<text x="40" y="115" font-family="{FONT}" font-size="20" font-weight="500" fill="{SUB}">apologize for not getting the balance</text>
<text x="40" y="145" font-family="{FONT}" font-size="20" font-weight="500" fill="{SUB}">right."</text>
</g>

<g transform="translate(62, 560)">
<rect x="0" y="0" width="900" height="120" rx="16" fill="{ORANGE_BG}" stroke="{ORANGE_BORDER}" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">😏 中文媒体神评论</text>
<text x="40" y="85" font-family="{FONT}" font-size="20" font-weight="600" fill="{TEXT}">"对不起，我不偷偷阴你了。但我要正大光明地阴你。"</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">来源: Anthropic官方公告, 36氪</text>
''')

def card_3():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="70" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="900" fill="{TEXT}">6月12日 美国政府反杀</text>
<text x="512" y="105" text-anchor="middle" font-family="{FONT}" font-size="20" fill="{SUB}">Anthropic前脚封别人，后脚被封</text>

<g transform="translate(62, 140)">
<rect x="0" y="0" width="900" height="180" rx="16" fill="{RED_BG}" stroke="{RED_BORDER}" stroke-width="1"/>
<circle cx="50" cy="50" r="24" fill="{RED}" opacity="0.15"/>
<text x="50" y="57" text-anchor="middle" font-family="{FONT_EN}" font-size="20" font-weight="800" fill="{RED}">!</text>
<text x="90" y="48" font-family="{FONT}" font-size="28" font-weight="800" fill="{RED}">美国商务部下令禁了Fable 5</text>
<text x="90" y="85" font-family="{FONT}" font-size="20" font-weight="500" fill="{TEXT}">理由：国家安全——禁止任何外国人访问</text>
<text x="90" y="115" font-family="{FONT}" font-size="18" fill="{SUB}">不仅限海外用户，连Anthropic自己的</text>
<text x="90" y="145" font-family="{FONT}" font-size="18" fill="{SUB}">非美国籍员工也被全球禁用</text>
</g>

<g transform="translate(62, 350)">
<rect x="0" y="0" width="900" height="180" rx="16" fill="{CARD_BG}" stroke="#E2D9CC" stroke-width="1"/>
<circle cx="50" cy="50" r="24" fill="{PURPLE}" opacity="0.15"/>
<text x="50" y="57" text-anchor="middle" font-family="{FONT_EN}" font-size="20" font-weight="800" fill="{PURPLE}">?</text>
<text x="90" y="48" font-family="{FONT}" font-size="28" font-weight="800" fill="{TEXT}">导火索：越狱漏洞</text>
<text x="90" y="85" font-family="{FONT}" font-size="20" font-weight="500" fill="{TEXT}">Fable 5存在jailbreak漏洞，可绕过安全</text>
<text x="90" y="115" font-family="{FONT}" font-size="18" fill="{SUB}">护栏，访问Mythos 5的完整网络战能力</text>
<text x="90" y="155" font-family="{FONT}" font-size="18" fill="{SUB}">CEO Dario Amodei拒绝修复，认为漏洞</text>
<text x="90" y="185" font-family="{FONT}" font-size="18" fill="{SUB}">"狭窄且非通用"，GPT-5.5上也能复现</text>
</g>

<g transform="translate(62, 560)">
<rect x="0" y="0" width="900" height="120" rx="16" fill="{ORANGE_BG}" stroke="{ORANGE_BORDER}" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{ORANGE}">🔪 亚马逊背刺</text>
<text x="40" y="85" font-family="{FONT}" font-size="20" font-weight="600" fill="{TEXT}">大股东Andy Jassy向白宫发出安全预警</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">来源: Bloomberg, Fortune, CryptoBriefing</text>
''')

def card_4():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="70" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="900" fill="{TEXT}">一周时间 完整闭环</text>
<text x="512" y="105" text-anchor="middle" font-family="{FONT}" font-size="20" fill="{SUB}">Anthropic从封禁者到被封禁者</text>

<g transform="translate(62, 140)">
<rect x="0" y="0" width="900" height="110" rx="16" fill="{RED_BG}" stroke="{RED_BORDER}" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="28" font-weight="800" fill="{RED}">封别人 → 自己被封</text>
<text x="40" y="85" font-family="{FONT}" font-size="18" fill="{SUB}">2025年9月封杀中国实体 → 2026年6月被美国禁</text>
</g>

<g transform="translate(62, 280)">
<rect x="0" y="0" width="900" height="110" rx="16" fill="{ORANGE_BG}" stroke="{ORANGE_BORDER}" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="28" font-weight="800" fill="{ORANGE}">偷偷降智 → 公开道歉</text>
<text x="40" y="85" font-family="{FONT}" font-size="18" fill="{SUB}">24小时滑跪认错，改为可见降级通知</text>
</g>

<g transform="translate(62, 420)">
<rect x="0" y="0" width="900" height="110" rx="16" fill="{PURPLE_BG}" stroke="{PURPLE_BORDER}" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="28" font-weight="800" fill="{PURPLE}">安全卫士 → 安全隐患</text>
<text x="40" y="85" font-family="{FONT}" font-size="18" fill="{SUB}">拒绝修漏洞被举报，从监管者变被监管者</text>
</g>

<g transform="translate(62, 560)">
<rect x="0" y="0" width="900" height="120" rx="16" fill="{GREEN_BG}" stroke="{GREEN_BORDER}" stroke-width="1"/>
<text x="40" y="45" font-family="{FONT}" font-size="22" font-weight="700" fill="{GREEN}">💡 启示</text>
<text x="40" y="80" font-family="{FONT}" font-size="20" font-weight="600" fill="{TEXT}">AI圈没有永远的王者</text>
<text x="40" y="110" font-family="{FONT}" font-size="18" fill="{SUB}">今天你封别人，明天就轮到你</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{SUB}" opacity="0.5">AI圈哪有永远的赢家</text>
''')

if __name__ == "__main__":
    cards = [
        ("cover", cover(), 1024, 1024),
        ("card-1", card_1(), 1024, 1024),
        ("card-2", card_2(), 1024, 1024),
        ("card-3", card_3(), 1024, 1024),
        ("card-4", card_4(), 1024, 1024),
    ]
    for name, svg, w, h in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(w), "-h", str(h)], check=True, capture_output=True)
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done! 5 cards regenerated.")
