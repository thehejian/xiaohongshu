#!/usr/bin/env python3
"""Generate 4 cards for 崔浩之死."""
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
    "Ancient Chinese court scene, a Han Chinese scholar-official in flowing robes standing before a Xianbei emperor on dragon throne, scroll in hand, tense dramatic confrontation, traditional Chinese ink wash painting, palace hall with columns, Song dynasty aesthetic",
    "Ancient Chinese city scene, large stone steles erected along a main road with Chinese characters carved on them, Xianbei noblemen on horseback reading them with angry expressions, public display of historical records, traditional Chinese painting, tense atmosphere, Song dynasty aesthetic",
    "Ancient Chinese execution ground at dawn, a bound scholar kneeling before the executioner's block, scattered scrolls on the ground, imperial guards surrounding the scene, tragic dignified atmosphere, traditional Chinese ink wash painting, Song dynasty aesthetic",
    "Ancient Chinese ancestral hall in ruins, ghostly figures of a massacred clan floating in mist, broken tablets and scattered scrolls, the weight of written history, ethereal tragedy, traditional Chinese ink wash ghost painting, Song dynasty aesthetic",
]

FILES = ["cuihao-cover", "cuihao-card-1", "cuihao-card-2", "cuihao-card-3"]

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
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#CBD5E1" letter-spacing="6" {STROKE}>北魏·文字狱</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>崔浩之死</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#CBD5E1" opacity="0.5"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="800" fill="#CBD5E1" letter-spacing="4" {STROKE}>一部国史引发的灭门惨案</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>秉笔直书 · 腰斩 · 灭族 · 国史之狱</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>北魏第一谋士</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>太武帝年间</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>450年</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#崔浩 #北魏 #国史之狱 #太武帝 #秉笔直书</text>
''')

def make_card_1(bg_b64):
    items = [
        ("三代帝师", "历仕道武、明元、太武三朝，被誉为北魏诸葛亮"),
        ("统一北方", "辅佐太武帝灭北凉、破柔然、统一华北"),
        ("修国史", "奉旨编纂北魏历史，坚持秉笔直书"),
        ("真相的代价", "将拓跋家族的丑事刻在石碑上公之于众"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#CBD5E1"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#CBD5E1" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#CBD5E1" letter-spacing="3" {STROKE}>崔浩其人</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#CBD5E1" letter-spacing="3" {STROKE}>国史之狱</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>写了什么？</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>拓跋部落早期抢掠、相残、乱伦丑闻</text>
</g>

<g transform="translate(40, 340)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>怎么发表的？</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>刻在石碑上立在都城大路边</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>鲜卑贵族路过大怒：祖辈的丑事全曝光了</text>
</g>

<g transform="translate(40, 520)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>皇帝的愤怒</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>太武帝震怒：那些事是真的，但你不能说</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#崔浩 #国史之狱 #鲜卑 #太武帝</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#CBD5E1" letter-spacing="3" {STROKE}>代价与影响</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>崔浩之死</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>腰斩于市，全族屠灭</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>株连灭族</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>范阳卢氏、太原郭氏、河东柳氏</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>河北汉人门阀被一网打尽</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>历史意义</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>汉人势力遭重创，鲜卑贵族巩固权力</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>用生命诠释了"秉笔直书"</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#崔浩 #清河崔氏 #北魏 #史官 #历史</text>
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
