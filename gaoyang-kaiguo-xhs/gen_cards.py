#!/usr/bin/env python3
"""Generate 4 cards for 高洋."""
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
    "Dual portrait of a Chinese emperor split down the middle: left side heroic emperor in magnificent dragon robes with wise expression, right side same emperor disheveled and wild-eyed holding a wine jug, split personality, traditional Chinese ink wash painting, dramatic contrast, Song dynasty aesthetic",
    "Ancient Chinese court scene, an emperor sitting half-naked on the throne laughing maniacally, drinking wine, disheveled, courtiers looking terrified, chaotic palace hall, traditional Chinese ink wash painting, dark and unsettling, Song dynasty aesthetic",
    "Ancient Chinese street scene, a crazed emperor on horseback laughing while holding a bow, terrorizing the common people, citizens fleeing, chaos in the city, traditional Chinese ink wash painting, disturbing atmosphere, Song dynasty aesthetic",
    "Ancient Chinese palace at night, a dying emperor collapsed on the floor surrounded by wine jugs, a crown fallen beside him, tragic end of a once-great ruler, moonlight through windows, traditional Chinese ink wash painting, poetic tragedy, Song dynasty aesthetic",
]

FILES = ["gaoyang-cover", "gaoyang-card-1", "gaoyang-card-2", "gaoyang-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#EF4444" letter-spacing="6" {STROKE}>北齐·开国即疯魔</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>高洋</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#EF4444" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="800" fill="#EF4444" letter-spacing="4" {STROKE}>最荒唐的开国君主</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>前半生英主 · 后半生疯魔 · 饮鸩止渴</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>北齐文宣帝</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>高欢次子</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>529 - 559</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高洋 #北齐 #文宣帝 #荒唐皇帝 #南北朝</text>
''')

def make_card_1(bg_b64):
    items = [
        ("高欢次子", "哥哥高澄被杀后迅速夺权"),
        ("逼东魏禅让", "550年建立北齐，登基称帝"),
        ("北击柔然", "打得突厥称其为'英雄天子'"),
        ("治国有方", "早期精明能干，国力蒸蒸日上"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#3B82F6"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#3B82F6" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>前期：英明之主</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>后期：疯狂实录</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>赤身上朝</text>
  <text x="30" y="78" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>在朝堂上裸体跳舞弹琴</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>肢解宠妃</text>
  <text x="30" y="78" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>用腿骨做琵琶，抱着弹唱</text>
</g>

<g transform="translate(40, 460)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="42" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>射杀大臣</text>
  <text x="30" y="78" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>喝醉了就拿弓箭随便射人</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>比夏桀商纣还离谱</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高洋 #北齐 #暴君 #荒唐</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>结局与矛盾</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>死亡</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>34岁酗酒暴毙</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>遗言</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>对弟弟高演：你要当皇帝的话别学我</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>矛盾</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>既能为国开疆扩土，也能把自己喝死</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>开国英主与终极疯子合二为一</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#高洋 #北齐 #文宣帝 #南北朝 #历史</text>
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
