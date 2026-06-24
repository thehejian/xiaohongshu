#!/usr/bin/env python3
"""Algeria card set: football + travel light-mode SVG cards"""
import subprocess, os

OUT = "output"
os.makedirs(OUT, exist_ok=True)

CREAM = "#FAF7F2"
CREAM2 = "#F5F0E8"
WHITE = "#FFFFFF"
TEXT = "#1E293B"
TEXT_DIM = "#64748B"
TEXT_LIGHT = "#94A3B8"
GREEN = "#006633"
GREEN_LIGHT = "#E8F5E9"
RED = "#DC2626"
RED_LIGHT = "#FEE2E2"
GOLD = "#D4A843"
GOLD_LIGHT = "#FEF9E7"

def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}",
         "-w", "1024", "-h", "1024"],
        check=True, capture_output=True,
    )

def shadow():
    return ('<filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">'
            '<feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>'
            '</filter>')

def bg_circles():
    return f'''<circle cx="80" cy="80" r="140" fill="{GREEN_LIGHT}" opacity="0.15"/>
<circle cx="924" cy="924" r="180" fill="{GOLD_LIGHT}" opacity="0.12"/>
<circle cx="80" cy="924" r="80" fill="{RED_LIGHT}" opacity="0.1"/>
<circle cx="924" cy="80" r="60" fill="{GREEN_LIGHT}" opacity="0.08"/>'''

def page_footer(y=960, hashtag=""):
    return f'''<line x1="80" y1="{y}" x2="944" y2="{y}" stroke="#E2E8F0" stroke-width="1"/>
<text x="512" y="{y+30}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_LIGHT}">{hashtag}</text>'''

def card_cover():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#006633"/>
    <stop offset="50%" stop-color="#00884A"/>
    <stop offset="100%" stop-color="#006633"/>
  </linearGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
{bg_circles()}
<rect x="62" y="40" width="900" height="80" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="90" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="28" font-weight="700" fill="{GREEN}">\U0001F3C6 阿尔及利亚 · 北非雄狮</text>

<rect x="112" y="170" width="800" height="120" rx="20" fill="{GREEN_LIGHT}" stroke="{GREEN}" stroke-width="1.5"/>
<text x="512" y="215" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="52" font-weight="900" fill="url(#titleG)">\U0001F9E1 足球 · 沙漠 · 地中海</text>
<text x="512" y="270" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">一个被严重低估的北非宝藏国家</text>

<rect x="212" y="330" width="600" height="50" rx="25" fill="{GREEN}"/>
<text x="512" y="363" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="#FFF">下翻  →  足球篇</text>

<rect x="62" y="420" width="900" height="400" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
<g transform="translate(82, 440)">
  <text x="0" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">本期内容速览</text>

  <rect x="0" y="60" width="400" height="50" rx="12" fill="{GREEN_LIGHT}"/>
  <text x="200" y="92" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="700" fill="{GREEN}">\U0001F3C0 足球</text>

  <rect x="420" y="60" width="440" height="50" rx="12" fill="{GOLD_LIGHT}"/>
  <text x="640" y="92" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" font-weight="700" fill="{GOLD}">\U0001F30D 旅行</text>

  <text x="0" y="150" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">· 2014世界杯差点掀翻德国</text>
  <text x="0" y="185" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">· 2019非洲杯冠军 · 马赫雷斯</text>
  <text x="0" y="220" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">· 齐达内的根在阿尔及利亚</text>
  <text x="0" y="260" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">· 白城阿尔及尔 · 卡斯巴老城</text>
  <text x="0" y="295" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">· 撒哈拉 · 塔西利恩阿耶</text>
  <text x="0" y="330" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">· 古罗马遗址 · 古斯古斯</text>
</g>
{page_footer(960, "#阿尔及利亚 #北非旅行 #足球 #撒哈拉 #小众旅行地")}
</svg>'''

def card_football():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="90" fill="{GREEN_LIGHT}" opacity="0.2"/>
<circle cx="924" cy="924" r="100" fill="{GOLD_LIGHT}" opacity="0.15"/>

<rect x="62" y="30" width="900" height="80" rx="35" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="30" font-weight="800" fill="{TEXT}">\U0001F3C0 阿尔及利亚 · 足球故事</text>

<g transform="translate(62, 140)">
  <rect x="0" y="0" width="900" height="120" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="{GREEN}"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{GREEN}">2014 世界杯 · 差点掀翻德国</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">1/8决赛，阿尔及利亚 1-2 德国（加时赛）</text>
  <text x="30" y="105" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">穆博利全场11次扑救 · 非洲球队最强表现</text>
</g>

<g transform="translate(62, 290)">
  <rect x="0" y="0" width="900" height="120" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="{GOLD}"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{GOLD}">2019 非洲杯 · 时隔29年夺冠</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">马赫雷斯决赛任意球绝杀塞内加尔</text>
  <text x="30" y="105" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">7战全胜 · 0失球 · 最完美冠军之路</text>
</g>

<g transform="translate(62, 440)">
  <rect x="0" y="0" width="900" height="120" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="{GREEN}"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{GREEN}">马赫雷斯 · 阿尔及利亚队长</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">曼城英超四连冠核心 · PFA最佳球员</text>
  <text x="30" y="105" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">"最骄傲的身份永远是阿尔及利亚队长"</text>
</g>

<g transform="translate(62, 590)">
  <rect x="0" y="0" width="900" height="100" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="{GOLD}"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{GOLD}">齐达内 · 根在阿尔及利亚</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">齐祖父亲是阿尔及利亚卡比利亚人 · 血脉永不断</text>
</g>

<rect x="62" y="730" width="900" height="70" rx="20" fill="{GREEN_LIGHT}" stroke="{GREEN}" stroke-width="1.5"/>
<text x="512" y="765" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{GREEN}">北非雄狮 · 世界足坛不敢小看的名字</text>

<rect x="312" y="840" width="400" height="50" rx="25" fill="{GREEN}"/>
<text x="512" y="873" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="#FFF">下翻  →  旅行篇</text>
{page_footer(960, "#阿尔及利亚足球 #马赫雷斯 #齐达内 #世界杯 #非洲杯")}
</svg>'''

def card_travel():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="80" fill="{GOLD_LIGHT}" opacity="0.2"/>
<circle cx="924" cy="924" r="120" fill="{GREEN_LIGHT}" opacity="0.15"/>

<rect x="62" y="30" width="900" height="80" rx="35" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="30" font-weight="800" fill="{TEXT}">\U0001F30D 阿尔及利亚 · 旅行宝藏</text>

<g transform="translate(62, 140)">
  <rect x="0" y="0" width="900" height="130" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">\U0001F3F0 阿尔及尔 · 白色之城</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">白房子依山而建，面朝地中海</text>
  <text x="30" y="105" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">像圣托里尼，但没游客 · 物价只有摩洛哥一半</text>
</g>

<g transform="translate(62, 300)">
  <rect x="0" y="0" width="900" height="130" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">\U0001F3DB 卡斯巴老城 · 世界遗产</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">奥斯曼时期窄巷迷宫 · 每一步都是历史</text>
  <text x="30" y="105" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">当地人会拉你喝薄荷茶 · 不喝完三杯走不掉</text>
</g>

<g transform="translate(62, 460)">
  <rect x="0" y="0" width="900" height="130" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">\U0001F3DE 古罗马遗址</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">提姆加德 · 杰米拉 · 北非保存最完整</text>
  <text x="30" y="105" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">站在两千年前的街道上 · 能听到历史的声音</text>
</g>

<g transform="translate(62, 620)">
  <rect x="0" y="0" width="900" height="100" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="40" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">\U0001F372 阿尔及利亚美食</text>
  <text x="30" y="75" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">古斯古斯国菜 · Mechoui烤全羊 · 法棍比巴黎正宗</text>
</g>

<rect x="62" y="760" width="900" height="70" rx="20" fill="{GOLD_LIGHT}" stroke="{GOLD}" stroke-width="1.5"/>
<text x="512" y="795" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{GOLD}">签证在放开口子 · 趁人少赶紧去</text>

<rect x="312" y="870" width="400" height="50" rx="25" fill="{GREEN}"/>
<text x="512" y="903" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="#FFF">下翻  →  撒哈拉</text>
{page_footer(960, "#阿尔及利亚旅行 #北非 #地中海 #卡斯巴 #古罗马遗址")}
</svg>'''

def card_sahara():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="70%">
    <stop offset="0%" stop-color="{CREAM}"/>
    <stop offset="100%" stop-color="{CREAM2}"/>
  </radialGradient>
  {shadow()}
</defs>
<rect width="1024" height="1024" fill="url(#bg)"/>
<circle cx="80" cy="80" r="100" fill="{GOLD_LIGHT}" opacity="0.15"/>
<circle cx="924" cy="924" r="130" fill="{GREEN_LIGHT}" opacity="0.12"/>

<rect x="62" y="30" width="900" height="80" rx="35" fill="{WHITE}" filter="url(#shadow)"/>
<text x="512" y="80" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="30" font-weight="800" fill="{TEXT}">\U0001F3D4 撒哈拉 · 阿尔及利亚的沙漠</text>

<rect x="62" y="140" width="900" height="350" rx="24" fill="{WHITE}" filter="url(#shadow)"/>

<g transform="translate(82, 160)">
  <rect x="0" y="0" width="860" height="55" rx="12" fill="{GOLD_LIGHT}"/>
  <text x="430" y="35" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{GOLD}">塔西利恩阿耶 · 世界遗产</text>
</g>

<g transform="translate(82, 235)">
  <text x="0" y="30" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">\U0001F3D4 全球最美沙漠段 · 没有之一</text>
  <text x="0" y="65" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">\U0001F3F3 史前岩画 · 一万年前的人类印记</text>
  <text x="0" y="100" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">\U0001F3EC 沙漠玫瑰石 · 大自然的鬼斧神工</text>
  <text x="0" y="135" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">\U0001F30C 星空密集到让人失语</text>
  <text x="0" y="170" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">\U0001F3A5 海市蜃楼 · 沙漠里的幻觉</text>
  <text x="0" y="205" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">\U0001F3D4 绵延沙丘 · 黄昏光影绝美</text>
</g>

<g transform="translate(62, 540)">
  <rect x="0" y="0" width="900" height="90" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">\U0001F4CD 地理位置</text>
  <text x="30" y="72" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">阿尔及利亚 · 非洲面积最大国家 · 撒哈拉占总面积80%</text>
</g>

<g transform="translate(62, 660)">
  <rect x="0" y="0" width="900" height="90" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="30" y="35" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">\U0001F465 当地人这样说</text>
  <text x="30" y="72" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="18" fill="{TEXT_DIM}">"阿尔及利亚的撒哈拉，才是真正的撒哈拉"</text>
</g>

<rect x="62" y="790" width="900" height="70" rx="20" fill="{GOLD_LIGHT}" stroke="{GOLD}" stroke-width="1.5"/>
<text x="512" y="825" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" font-weight="800" fill="{GOLD}">此生必去 · 阿尔及利亚</text>

<rect x="312" y="890" width="400" height="50" rx="25" fill="{GREEN}"/>
<text x="512" y="923" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="20" font-weight="700" fill="#FFF">点赞收藏 · 下次出发</text>

<text x="512" y="970" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, PingFang SC, sans-serif" font-size="22" fill="{TEXT_DIM}">❤️ 点赞  ⭐ 收藏  🔄 转发</text>
{page_footer(990, "#撒哈拉沙漠 #阿尔及利亚 #北非旅行 #塔西利恩阿耶 #小众旅行地")}
</svg>'''

if __name__ == "__main__":
    print("Generating Algeria cards...")
    for name, fn in [
        ("01-cover", card_cover),
        ("02-football", card_football),
        ("03-travel", card_travel),
        ("04-sahara", card_sahara),
    ]:
        svg = fn()
        save_svg(name, svg)
        print(f"  \u2713 {name}")
    print("Done! 4 cards in output/")
