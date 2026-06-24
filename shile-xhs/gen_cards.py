#!/usr/bin/env python3
"""Generate 4 cards for Shi Le / Later Zhao using Agnes AI backgrounds."""
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
    "Epic cinematic portrait of a fierce nomadic Jie warrior king in magnificent armor, standing on a battlefield with burning city in background, dramatic sunset sky, traditional Chinese ink wash painting meets epic fantasy, powerful imposing figure, Song dynasty aesthetic, golden red tones, masterpiece quality",
    "Ancient Chinese slave market scene, a young nomadic man in chains being sold, dusty marketplace, dramatic cloudy sky, figures in ancient Chinese clothing, cinematic composition, traditional Chinese painting style, tragic atmosphere, muted earth tones",
    "Massive ancient Chinese cavalry battle scene, a Jie king leading thousands of warriors in a charge, war banners with Zhao characters, dramatic storm clouds and dust, epic cinematic Chinese historical painting, Song dynasty battlefield aesthetic, dynamic composition",
    "Ancient Chinese imperial palace, a former slave now emperor on dragon throne in magnificent hall, scholars and generals paying homage, ornate palace interior, dramatic light, traditional Chinese painting, triumphant atmosphere, rich red and gold tones",
]

FILES = ["shile-cover", "shile-card-1", "shile-card-2", "shile-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="40%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="700" fill="#FFD700" letter-spacing="8" {STROKE}>五胡十六国</text>
<text x="512" y="400" text-anchor="middle" font-family="{FONT}" font-size="170" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>石勒</text>
<rect x="312" y="445" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="545" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>从奴隶到皇帝</text>
<text x="512" y="630" text-anchor="middle" font-family="{FONT}" font-size="28" fill="#FFFFFF" {STROKE_S}>中国历史上出身最低微的帝王</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>羯族人</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>后赵建立者</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>319 - 333</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#石勒 #后赵 #十六国 #五胡十六国</text>
''')

def make_card_1(bg_b64):
    items = [
        ("被卖为奴", "年轻时被晋军抓获，在山东被贩卖"),
        ("逃出生天", "召集流亡者，拉起自己的队伍"),
        ("乱世崛起", "八王之乱中投靠刘渊，屡立战功"),
        ("用人之道", "不看出身只问能力，寒门张宾为谋主"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#FFD700"/>
  <text x="30" y="48" font-family="{FONT}" font-size="30" font-weight="700" fill="#FFD700" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="24" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>逆袭之路</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>称帝建国</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#FFD700"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#FFD700" {STROKE}>319年 · 称赵王</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>建立后赵，定都襄国（今邢台）</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>以\u201c赵\u201d为国号，继承前赵正统</text>
</g>

<g transform="translate(40, 370)">
  <rect x="0" y="0" width="944" height="170" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="170" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#E2E8F0" {STROKE}>329年 · 灭前赵</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>击败刘曜，统一北方</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>从奴隶到北方之主，仅用十年</text>
</g>

<g transform="translate(40, 580)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="28" font-weight="700" fill="#FFD700" {STROKE}>治国之道</text>
  <text x="30" y="90" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>推行均田制 · 整顿吏治 · 减轻赋税</text>
  <text x="30" y="122" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>胡汉分治，各安其业</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#石勒 #后赵 #十六国</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>历史印记</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>文盲皇帝爱读书</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>不识字，但命人读《汉书》</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>论政得失，常有独到见解</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>功过参半</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>严刑峻法杀人无数，但轻徭薄赋</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>晚年立嗣不当，石虎篡位毁其基业</text>
</g>

<g transform="translate(40, 530)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>历史评价</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>从奴隶到皇帝，中国历史上独一人</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>乱世之中，英雄不问出处</text>
</g>

<text x="512" y="820" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>英雄不问出处</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#石勒 #后赵 #从奴隶到皇帝</text>
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
