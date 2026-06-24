#!/usr/bin/env python3
"""Generate 4 cards for 兰陵王入阵曲."""
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
    "Ancient Chinese warrior prince in magnificent armor with a fierce golden mask and purple cape on horseback, charging into battle, the most beautiful general in history, heroic and tragic, traditional Chinese ink wash painting meets cinematic epic, dramatic clouds, Song dynasty aesthetic",
    "Epic ancient Chinese battle scene, a single masked warrior on horseback leading a small cavalry charge against a massive army, city walls in background, breaking through enemy lines, dust and chaos, traditional Chinese ink wash painting, cinematic scale, Song dynasty aesthetic",
    "Ancient Chinese city gate, a masked warrior removing his helmet to reveal a strikingly handsome face, soldiers on the wall cheering in joy and relief, moment of recognition, emotional reunion, traditional Chinese painting, warm golden light, Song dynasty aesthetic",
    "Ancient Chinese palace at night, a beautiful prince in royal robes kneeling before a cup of poisoned wine, moonlight streaming through latticed windows, tragic farewell, traditional Chinese ink wash painting, poetic sorrow, Song dynasty aesthetic",
]

FILES = ["lanling-cover", "lanling-card-1", "lanling-card-2", "lanling-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.1"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#A855F7" letter-spacing="6" {STROKE}>北齐·悲歌</text>
<text x="512" y="350" text-anchor="middle" font-family="{FONT}" font-size="130" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>兰陵王入阵曲</text>
<rect x="312" y="395" width="400" height="3" rx="1.5" fill="#A855F7" opacity="0.7"/>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="800" fill="#A855F7" letter-spacing="4" {STROKE}>面具下的悲歌</text>
<text x="512" y="590" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>五百铁骑破十万 · 一曲战舞传千年</text>
<g transform="translate(262, 690)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>高长恭</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>北齐宗室名将</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>541 - 573</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#兰陵王 #入阵曲 #北齐 #高长恭 #邙山之战</text>
''')

def make_card_1(bg_b64):
    items = [
        ("最美王子", "高欢之孙，因容貌绝世，上阵必戴面具"),
        ("邙山之战", "564年率500骑冲破北周十万大军"),
        ("城下摘盔", "守军不敢认，摘下面具后全城沸腾"),
        ("入阵曲诞生", "将士编创战歌纪念，传唱百年"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#A855F7"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#A855F7" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#A855F7" letter-spacing="3" {STROKE}>传奇事迹</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#A855F7" letter-spacing="3" {STROKE}>入阵曲的流传</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>起源</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>将士为纪念兰陵王所创，戴面具边唱边舞</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>传入日本</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>唐代传入日本雅乐，保存至今</text>
</g>

<g transform="translate(40, 520)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>逆输入</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>中国本土失传千年，近代才从日本找回</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#兰陵王 #入阵曲 #雅乐 #日本 #唐代</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#A855F7" letter-spacing="3" {STROKE}>悲剧结局</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>功高震主</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>"入阵太深"——皇帝高纬起了杀心</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>赐死</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>573年，高纬赐毒酒</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>"我忠以事上，何辜于天？"</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>身后</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>兰陵王死后四年，北齐灭亡</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>一曲入阵曲，传唱千年不衰</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#兰陵王 #高纬 #北齐 #悲剧英雄 #历史</text>
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
