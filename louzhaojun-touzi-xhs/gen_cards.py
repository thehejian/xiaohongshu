#!/usr/bin/env python3
"""Generate 4 cards for 娄昭君."""
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
    "Ancient Chinese noblewoman in magnificent Tang-style robes, Lou Zhaojun, elegant and intelligent, standing in a wealthy mansion courtyard, jade ornaments, traditional Chinese ink wash painting, warm golden light, confident wise expression, Song dynasty aesthetic",
    "Ancient Chinese frontier town scene, a wealthy noblewoman in fine robes watching a poor but handsome soldier on city wall, love at first sight, two different worlds meeting, traditional Chinese ink wash painting, romantic atmosphere, Song dynasty aesthetic",
    "Ancient Chinese grand banquet hall, an empress dowager on a throne surrounded by four sons in imperial dragon robes, four emperors born from one mother, magnificent court scene, traditional Chinese painting, golden light, powerful matriarch, Song dynasty aesthetic",
    "Ancient Chinese palace, an aging empress dowager on her deathbed surrounded by her imperial sons, peaceful and satisfied smile, having seen her family rise to the pinnacle of power, traditional Chinese ink wash painting, touching farewell, warm candlelight, Song dynasty aesthetic",
]

FILES = ["louzhaojun-cover", "louzhaojun-card-1", "louzhaojun-card-2", "louzhaojun-card-3"]

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
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>南北朝·传奇女性</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>娄昭君</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>历史上最牛的天使投资人</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>投资高欢 · 回报四帝 · 一母生四皇</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>鲜卑贵族</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>高欢之妻</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>501 - 562</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#娄昭君 #高欢 #北齐 #天使投资 #南北朝 #女性</text>
''')

def make_card_1(bg_b64):
    items = [
        ("鲜卑贵族", "娄氏豪门之女，家财万贯"),
        ("一见高欢", "看到守城穷兵高欢：'此真吾夫也'"),
        ("主动求婚", "派侍女传话，不计门第嫁给他"),
        ("倾家资助", "嫁妆全用来买马买武器结交豪杰"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#FFD700"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#FFD700" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>天使投资</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>回报率：四个皇帝</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>高澄</text>
  <text x="30" y="78" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>东魏丞相，追尊文襄皇帝</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>高洋</text>
  <text x="30" y="78" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>北齐开国皇帝</text>
</g>

<g transform="translate(40, 460)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>高演·高湛</text>
  <text x="30" y="78" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>孝昭帝 · 武成帝</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>一母生四帝，历史绝无仅有</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#娄昭君 #北齐 #高欢 #高洋 #母子</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>政治手腕</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>高欢死后</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>出面稳定局势，扶持高澄顺利接班</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>高澄被杀后</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>迅速扶持高洋上位，避免政权动荡</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>北齐建立</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>对高洋说：你父亲一辈子没当成的皇帝</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>你做到了</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#娄昭君 #东魏 #北齐 #太后 #女性政治家</text>
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
