#!/usr/bin/env python3
"""Generate 4 cards for 北魏子立母死."""
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
    "Ancient Chinese palace interior, dramatic dark scene, an emperor on throne issuing a decree, a weeping concubine being led away by guards, candlelit hall with deep shadows, traditional Chinese ink wash painting meets cinematic epic, tragic atmosphere, Song dynasty aesthetic",
    "Ancient Chinese palace, a young crown prince kneeling alone in a vast empty hall, a single scroll on the floor bearing an imperial decree, dramatic moonlight through latticed windows, deep shadows, traditional Chinese painting style, emotional tragedy, Song dynasty aesthetic",
    "Ancient northern Chinese palace at night, a young prince fleeing through a dark garden, torches in distance, soldiers searching, desperate escape, cinematic moonlight, traditional Chinese ink wash meets epic drama, Song dynasty aesthetic",
    "Ancient Chinese palace, seven ghostly figures of empresses in white robes floating in a dark hall, representing generations of mothers executed under this cruel policy, sad elegant spirits, traditional Chinese ink wash ghost painting, poetic tragedy, ethereal atmosphere",
]

FILES = ["weizilimusi-cover", "weizilimusi-card-1", "weizilimusi-card-2", "weizilimusi-card-3"]

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
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#EF4444" letter-spacing="6" {STROKE}>北魏·恐怖制度</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="160" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>子立母死</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#EF4444" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#EF4444" letter-spacing="4" {STROKE}>最残忍的立储制度</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>立太子日 · 赐死太子生母</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>北魏道武帝拓跋珪首创</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>延续七代皇帝</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>386 - 515</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北魏 #子立母死 #拓跋珪 #历史冷知识</text>
''')

def make_card_1(bg_b64):
    items = [
        ("子将立，母先死", "册立太子之日，太子生母即被处死"),
        ("目的", "防止母后干政，杜绝外戚乱政"),
        ("历史教训", "拓跋珪目睹西汉吕后专政，心生恐惧"),
        ("极端方案", "以最残酷的方式解决外戚问题"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#EF4444"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#EF4444" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="24" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>制度内容</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>拓跋嗣的悲剧</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>立太子日</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>拓跋珪立长子拓跋嗣为太子</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>同日下令处死其母刘贵人</text>
</g>

<g transform="translate(40, 350)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>太子逃亡</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>拓跋嗣悲痛欲绝，日夜痛哭</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>父王震怒，太子被迫逃出京城</text>
</g>

<g transform="translate(40, 540)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>讽刺结局</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>太子不在身边，无人护卫</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>拓跋珪被次子拓跋绍刺杀而死</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#拓跋珪 #拓跋嗣 #子立母死</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>制度的终结</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>七代传承</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>从道武帝到宣武帝，延续近130年</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>宣武帝废除</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>515年宣武帝元恪下诏废除这一制度</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>唯一例外</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>冯太后是养母非生母，得以幸存</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="700" fill="#EF4444" {STROKE}>中国历史上最奇特的立储制度</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北魏 #子立母死 #历史 #中国历史</text>
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
