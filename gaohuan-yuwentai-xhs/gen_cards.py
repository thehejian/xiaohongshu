#!/usr/bin/env python3
"""Generate 4 cards for 高欢与宇文泰."""
import subprocess, os, requests, time, base64
ROOT = os.path.dirname(os.path.abspath(__file__))

API_KEY = "sk-YjJnlziWMJgYHmiJiX8peB5PtNx1hInu7SQnivjeavaN4Ect"
API_URL = "https://apihub.agnes-ai.com/v1/images/generations"

STROKE = 'paint-order="stroke fill" stroke="#000" stroke-width="5" stroke-linejoin="round"'
STROKE_S = 'paint-order="stroke fill" stroke="#000" stroke-width="3" stroke-linejoin="round"'
FONT = 'Noto Sans SC,PingFang SC,Microsoft YaHei,sans-serif'

def agnes_image(prompt, size="1024x1024", retries=3):
    for attempt in range(retries):
        try:
            r = requests.post(API_URL, headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }, json={"model": "agnes-image-2.1-flash", "prompt": prompt, "size": size, "n": 1}, timeout=120)
            r.raise_for_status()
            url = r.json()["data"][0]["url"]
            img = requests.get(url, timeout=60)
            return img.content
        except Exception as e:
            print(f"  Agnes attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(5)
    raise RuntimeError(f"Failed after {retries} attempts")

PROMPTS = [
    "Epic dual portrait scene, two rival Chinese warlords facing each other across a misty ancient battlefield at sunset, one in dark armor on horseback commanding eastern plains, one in white armor commanding western mountains, dramatic sky, traditional Chinese ink wash painting meets cinematic epic, Song dynasty aesthetic, divided land",
    "Massive ancient Chinese battle scene at dawn, one army ambushing another in a riverside marsh, thousands of soldiers clashing, arrows flying, dust clouds, one army many times larger than the other being routed, chaotic battle, traditional Chinese ink wash painting, epic scale, Song dynasty aesthetic",
    "Dual scene split composition: left side a prosperous eastern capital with bustling markets and luxurious palaces, right side a spartan western capital with disciplined soldiers drilling and scholars drafting laws, contrast of wealth vs discipline, traditional Chinese painting, Song dynasty aesthetic",
    "Dual scene: two dying warlords on their deathbeds, each surrounded by their sons who will become founding emperors, east side a flourishing kingdom, west side a disciplined kingdom, two thrones awaiting their successors, traditional Chinese ink wash painting, poetic historical farewell, Song dynasty aesthetic",
]

FILES = ["gaohuan-cover", "gaohuan-card-1", "gaohuan-card-2", "gaohuan-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.1"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.6"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>南北朝·双雄对决</text>
<text x="512" y="330" text-anchor="middle" font-family="{FONT}" font-size="110" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>既生瑜何生亮</text>
<rect x="312" y="365" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="460" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>高欢 vs 宇文泰</text>
<text x="512" y="540" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>东魏霸主 · 西魏柱石 · 二十年的龙虎斗</text>
<g transform="translate(200, 640)">
  <rect x="0" y="0" width="280" height="60" rx="10" fill="#1E3A5F" opacity="0.85"/>
  <text x="140" y="38" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#60A5FA" {STROKE}>高欢</text>
  <rect x="320" y="0" width="280" height="60" rx="10" fill="#5F1E1E" opacity="0.85"/>
  <text x="460" y="38" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F87171" {STROKE}>宇文泰</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高欢 #宇文泰 #东魏 #西魏 #沙苑之战 #南北朝</text>
''')

def make_card_1(bg_b64):
    items = [
        ("高欢", "六镇豪强，宽厚善用人，坐镇邺城"),
        ("宇文泰", "武川军团领袖，精于制度，控制长安"),
        ("同在尔朱荣麾下", "两人都出身卑微，都是尔朱荣部将"),
        ("瓜分帝国", "尔朱荣死后，东西分治，谁都不服谁"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        colors = ["#60A5FA", "#F87171", "#FFD700", "#FFD700"]
        c = colors[i]
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="{c}"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="{c}" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>两位枭雄</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>沙苑之战 537年</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#60A5FA"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#60A5FA" {STROKE}>高欢</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>率20万大军西征，志在必得</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#F87171"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#F87171" {STROKE}>宇文泰</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>不足1万人，退守渭水沙苑</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>设伏两侧，待敌半入而击</text>
</g>

<g transform="translate(40, 520)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>结局</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>东魏军大败，损失8万余人</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>高欢乘马逃脱，双方恢复对峙</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高欢 #宇文泰 #沙苑之战 #渭水</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>遗产与命运</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#60A5FA"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#60A5FA" {STROKE}>高欢 → 北齐</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>子高洋废东魏立北齐，享国28年</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#F87171"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#F87171" {STROKE}>宇文泰 → 北周</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>子宇文觉废西魏立北周，享国24年</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>最终赢家</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>北周灭北齐，统一北方</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>宇文泰的府兵制被隋唐继承</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高欢 #宇文泰 #北齐 #北周 #府兵制 #历史</text>
''')

if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    makers = [make_cover, make_card_1, make_card_2, make_card_3]
    for i, prompt in enumerate(PROMPTS):
        name = FILES[i]
        print(f"  Generating Agnes image for {name}...")
        img_data = agnes_image(prompt)
        bg_b64 = base64.b64encode(img_data).decode()
        svg = makers[i](bg_b64)
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg)
        subprocess.run(
            ["inkscape", svg_path, "-o", png_path, "-w", "1024", "-h", "1024"],
            check=True, capture_output=True
        )
        sz = os.path.getsize(png_path) // 1024
        print(f"  {name}.png ({sz} KB)")
    print("Done! 4 cards generated.")
