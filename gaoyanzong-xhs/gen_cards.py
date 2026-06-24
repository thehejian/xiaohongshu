#!/usr/bin/env python3
"""Generate 4 cards for 高延宗."""
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
    "Ancient Chinese prince in magnificent battle armor standing on a city wall at sunset, holding a spear, determined heroic expression, city under siege in background, smoke and flames, a last stand, traditional Chinese ink wash painting meets cinematic epic, tragic hero, Song dynasty aesthetic",
    "Ancient Chinese city gate battle scene, a prince leading desperate urban street fighting, breaking through enemy lines, almost reaching the enemy commander, intense close combat, traditional Chinese ink wash painting, chaotic battle atmosphere, Song dynasty aesthetic",
    "Ancient Chinese palace tent, a victorious emperor and a captured prince sitting together drinking wine, mutual respect between enemies, one in dragon robes one in prisoner robes, traditional Chinese ink wash painting, complex emotional atmosphere, warm torchlight, Song dynasty aesthetic",
    "Ancient Chinese palace courtyard, a prince kneeling before a cup of poison, his armor beside him, twilight, a fallen kingdom's last light, tragic dignity, traditional Chinese ink wash painting, poetic farewell, Song dynasty aesthetic",
]

FILES = ["gaoyanzong-cover", "gaoyanzong-card-1", "gaoyanzong-card-2", "gaoyanzong-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#F59E0B" letter-spacing="6" {STROKE}>北齐·最后的英雄</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>高延宗</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#F59E0B" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="800" fill="#F59E0B" letter-spacing="4" {STROKE}>亡国前的最后一道光</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>晋阳巷战 · 几乎活捉宇文邕 · 英雄相惜</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>安德王</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>高澄之子 · 高欢之孙</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>576年称帝</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高延宗 #安德王 #北齐 #宇文邕 #晋阳之战</text>
''')

def make_card_1(bg_b64):
    items = [
        ("城楼拉屎", "北齐书记载：在楼上大便，让人张嘴在城下接"),
        ("马鞭取乐", "喜欢用鞭子抽人取乐，头破血流才停"),
        ("矛盾的人", "变态少年→战场上的好统帅，一体两面"),
        ("晋阳危局", "576年宇文邕伐齐，仓促即位守城"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        colors = ["#EF4444", "#EF4444", "#F59E0B", "#F59E0B"]
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="{colors[i]}"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="{colors[i]}" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#F59E0B" letter-spacing="3" {STROKE}>奇葩与英雄</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#F59E0B" letter-spacing="3" {STROKE}>高光时刻</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#F59E0B"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>巷战突围</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>城破后率军巷战，身先士卒杀向敌阵</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>几乎活捉宇文邕</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>一路杀到宇文邕面前，对方险被俘</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>这是宇文邕一生最接近死亡的时刻</text>
</g>

<g transform="translate(40, 520)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>城陷</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>叛徒开城投降，高延宗力竭被俘</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高延宗 #晋阳 #宇文邕 #巷战</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#F59E0B" letter-spacing="3" {STROKE}>英雄相惜</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#F59E0B"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>宇文邕的敬意</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"真想和你这样的英雄交个朋友"</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>善待</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>被俘后受礼遇，一起饮酒</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>赐死</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>北齐降将谋拥立，宇文邕被迫赐死</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>"今日之死，是我的命"</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>禽兽窝里的一道真光</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高延宗 #安德王 #北齐 #北周 #历史</text>
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
