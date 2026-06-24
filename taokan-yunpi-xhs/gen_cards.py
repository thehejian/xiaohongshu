#!/usr/bin/env python3
"""Generate 4 cards for 陶侃."""
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
    "Elderly ancient Chinese official in simple robes carrying a stack of bricks in a courtyard at sunrise, disciplined and determined expression, traditional Chinese ink wash painting, Song dynasty aesthetic, muted blue-gray tones, austere and dignified",
    "Ancient Chinese courtyard scene, an old general moving bricks from one side to another, morning light, simple and rustic surroundings, the act of self-discipline, traditional Chinese ink wash painting, Song dynasty aesthetic",
    "Ancient Chinese general commanding a grand army, imperial banners, battle formations, decisive battle scene, epic and heroic, traditional Chinese ink wash painting, Song dynasty aesthetic, blue and green landscape",
    "Three generations of Chinese scholars and officials, an old general passing wisdom to his grandson, a young poet (Tao Yuanming) in the background, family legacy, traditional Chinese ink wash painting, Song dynasty aesthetic, warm and nostalgic",
]

FILES = ["taokan-cover", "taokan-card-1", "taokan-card-2", "taokan-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.12"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#64748B" letter-spacing="6" {STROKE}>东晋·寒门名将</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="160" font-weight="900" fill="#FFFFFF" letter-spacing="12" {STROKE}>陶侃</text>
<rect x="362" y="405" width="300" height="3" rx="1.5" fill="#64748B" opacity="0.7"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="800" fill="#64748B" letter-spacing="6" {STROKE}>运甓翁</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>搬砖磨志 · 三定江南 · 惜寸阴</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶侃 #运甓 #东晋 #陶渊明 #寒门逆袭</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#64748B" letter-spacing="3" {STROKE}>运甓——搬砖磨炼意志</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#64748B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#64748B" {STROKE}>早起搬砖</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>每天把一百块砖搬到屋外，晚上搬回</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#64748B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#64748B" {STROKE}>怕安逸丧志</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>怕自己太安逸，用体力活提醒自己</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#64748B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#64748B" {STROKE}>惜寸阴</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"大禹惜寸阴，众人当惜分阴"</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#64748B" {STROKE}>中国历史上最自律的名将</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶侃 #运甓 #自律 #惜寸阴 #励志</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>三定江南</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>平王敦之乱</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>王敦第二次造反，陶侃率兵讨平</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>平苏峻之乱</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>苏峻攻破建康挟持皇帝，陶侃任总指挥</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>平郭默之乱</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>一战擒杀，干净利落</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>东晋真正的顶梁柱</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶侃 #王敦 #苏峻 #东晋 #名将</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#059669" letter-spacing="3" {STROKE}>寒门逆袭 & 遗产</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#059669"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>出身寒门</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>在门阀垄断的东晋硬靠本事爬上来</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#059669"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>官至八州都督</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>东汉以来寒门出身的最高职位</text>
</g>

<g transform="translate(40, 470)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#059669"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>孙子陶渊明</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>中国最伟大的田园诗人</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>搬砖搬出来的传奇人生</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陶侃 #寒门 #逆袭 #陶渊明 #东晋</text>
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
