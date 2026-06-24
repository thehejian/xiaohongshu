#!/usr/bin/env python3
"""Generate 4 cards for Ran Min / Ran Wei using Agnes AI backgrounds."""
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
    "Dark epic portrait of a fierce Han Chinese general in blood-stained armor, holding a sword, standing on a battlefield littered with bodies, dramatic red sunset sky, smoke and fire, traditional Chinese ink wash meets dark epic, intense gaze, Song dynasty aesthetic, bloody atmosphere",
    "Ancient Chinese capital city massacre scene at night, torchlight, bodies in streets, soldiers with swords, dramatic and tragic atmosphere, traditional Chinese painting style, dark red tones, smoke and fire, epic historical horror scene",
    "Ancient Chinese battlefield, a Han Chinese general fighting alone surrounded by enemy soldiers, dramatic cloudy sky, broken weapons, desperate last stand, traditional ink wash painting meets cinematic epic, tragic heroism, mid-day battle scene with dust",
    "Ancient Chinese execution ground, a bound Han general kneeling before a Xianbei king on horseback, dramatic cloudy sky, traditional Chinese painting, tragic final moment, epic historical painting, Song dynasty aesthetic, solemn atmosphere",
]

FILES = ["ranmin-cover", "ranmin-card-1", "ranmin-card-2", "ranmin-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="40%" stop-color="#000" stop-opacity="0.2"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="700" fill="#FF4444" letter-spacing="8" {STROKE}>五胡十六国</text>
<text x="512" y="400" text-anchor="middle" font-family="{FONT}" font-size="170" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>冉闵</text>
<rect x="312" y="445" width="400" height="3" rx="1.5" fill="#FF4444" opacity="0.7"/>
<text x="512" y="550" text-anchor="middle" font-family="{FONT}" font-size="54" font-weight="800" fill="#FF4444" letter-spacing="4" {STROKE}>杀胡令下的人间炼狱</text>
<text x="512" y="630" text-anchor="middle" font-family="{FONT}" font-size="28" fill="#E2E8F0" {STROKE_S}>最争议的十六国人物</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>冉魏建立者</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>石虎养孙</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>350 - 352</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#冉闵 #杀胡令 #冉魏 #十六国 #争议</text>
''')

def make_card_1(bg_b64):
    items = [
        ("石虎养孙", "汉人，骁勇善战，被石虎收为养孙"),
        ("后赵内乱", "石虎死后，趁机夺取政权"),
        ("杀胡令下", "350年下令屠杀境内胡人"),
        ("一夜血洗", "邺城二十万胡人被杀，误杀无数"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#FF4444"/>
  <text x="30" y="48" font-family="{FONT}" font-size="30" font-weight="700" fill="#FF4444" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="24" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FF4444" letter-spacing="3" {STROKE}>杀胡令</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FF4444" letter-spacing="3" {STROKE}>冉魏兴亡</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#FF4444"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#FF4444" {STROKE}>350年 · 称帝建国</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>国号魏，史称冉魏</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>定都邺城</text>
</g>

<g transform="translate(40, 370)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#E2E8F0" {STROKE}>352年 · 兵败被俘</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>前燕慕容儁率军攻冉魏</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>冉闵突围时战马倒毙被俘</text>
</g>

<g transform="translate(40, 580)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#FF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="28" font-weight="700" fill="#FF4444" {STROKE}>最后的对话</text>
  <text x="30" y="90" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>慕容儁：\u201c奴仆下人，怎敢自称天子？\u201d</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>冉闵：\u201c夷狄禽兽尚且称帝，我中原英雄为何不能！\u201d</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#冉闵 #冉魏 #慕容儁 #十六国</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FF4444" letter-spacing="3" {STROKE}>后世争议</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FF4444" {STROKE}>民族英雄？</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>有人视其为捍卫汉人尊严的英雄</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>杀胡令被解读为民族复仇的正义之举</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>屠夫？</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>杀胡令导致数十万无辜者丧命</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>误杀的汉人也不计其数</text>
</g>

<g transform="translate(40, 530)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FF4444" {STROKE}>短命的冉魏</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>只存在了两年，十六国中最短命的政权</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>杀伐太重，终难长久</text>
</g>

<text x="512" y="820" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FF4444" {STROKE}>争议千年，未有定论</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#冉闵 #杀胡令 #冉魏 #历史争议 #十六国</text>
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
