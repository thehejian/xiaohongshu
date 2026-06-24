#!/usr/bin/env python3
"""Generate 4 cards for 武川军事集团."""
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
    "Ancient Chinese border garrison town at dawn, warriors training in a dusty courtyard, military banners with Chinese characters, snow-capped mountains in the distance, vast Mongolian plateau landscape, traditional Chinese ink wash painting, epic and grand atmosphere, Song dynasty aesthetic",
    "Eight ancient Chinese generals on horseback forming a semicircle, each wearing distinct armor, imperial palace behind them, grand ceremony, dark blue and gold palette, traditional Chinese ink wash painting, majestic and solemn",
    "Ancient Chinese scene of a powerful father sending his three daughters to marry three different emperors, a grand wedding procession for each, three imperial palaces visible in the distance, traditional Chinese ink wash painting with rich colors, poetic and dramatic",
    "Ancient Chinese timeline scroll showing three dynasties flowing from a single source, Northern Zhou, Sui, and Tang imperial symbols connected by threads of fate, a small border town at the root, traditional Chinese painting, warm aged tones, Song dynasty aesthetic",
]

FILES = ["wuchuan-cover", "wuchuan-card-1", "wuchuan-card-2", "wuchuan-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="35%" stop-color="#000" stop-opacity="0.2"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>北魏·六镇·武川</text>
<text x="512" y="350" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>武川</text>
<rect x="312" y="395" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="50" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>三朝皇帝的摇篮</text>
<text x="512" y="600" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>一个边镇 · 八柱国 · 北周隋唐三百年</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#武川 #关陇集团 #八柱国 #隋唐 #南北朝</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>八柱国 · 武川占五席</text>

<g transform="translate(40, 145)">
  <rect x="0" y="0" width="444" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#FFD700"/>
  <text x="24" y="46" font-family="{FONT}" font-size="24" font-weight="700" fill="#FFD700" {STROKE}>宇文泰</text>
  <text x="24" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>北周太祖 · 武川人</text>
</g>
<g transform="translate(540, 145)">
  <rect x="0" y="0" width="444" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#3B82F6"/>
  <text x="24" y="46" font-family="{FONT}" font-size="24" font-weight="700" fill="#3B82F6" {STROKE}>李虎</text>
  <text x="24" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>唐太祖 · 武川人</text>
</g>

<g transform="translate(40, 270)">
  <rect x="0" y="0" width="444" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#3B82F6"/>
  <text x="24" y="46" font-family="{FONT}" font-size="24" font-weight="700" fill="#3B82F6" {STROKE}>独孤信</text>
  <text x="24" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>三朝国丈 · 武川人</text>
</g>
<g transform="translate(540, 270)">
  <rect x="0" y="0" width="444" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="100" rx="3" fill="#3B82F6"/>
  <text x="24" y="46" font-family="{FONT}" font-size="24" font-weight="700" fill="#3B82F6" {STROKE}>赵贵 / 侯莫陈崇</text>
  <text x="24" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>皆武川人</text>
</g>

<text x="512" y="460" text-anchor="middle" font-family="{FONT}" font-size="22" fill="#94A3B8" {STROKE_S}>八柱国中武川籍贯的占五人</text>
<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>八柱国中五人来自武川</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#八柱国 #武川 #宇文泰 #独孤信 #李虎</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#A855F7" letter-spacing="3" {STROKE}>独孤信：三朝国丈</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#A855F7"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>长女 → 北周明帝</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>嫁宇文毓，成北周皇后</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#A855F7"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>四女 → 唐高祖之母</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>嫁李昞，生李渊（唐高祖）</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#A855F7"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>七女 → 隋文帝皇后</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>独孤伽罗嫁杨坚，生杨广</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>三朝皇后皆出一门</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#独孤信 #三朝国丈 #北周 #隋 #唐</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>关陇集团 · 四百年统治</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>宇文泰 · 西魏/北周</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>武川军人集团的核心缔造者</text>
</g>

<g transform="translate(40, 290)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>杨坚 · 隋</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>独孤信女婿，继承武川政治遗产</text>
</g>

<g transform="translate(40, 430)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>李渊 · 唐</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>独孤信外孙，武川血脉的最后高峰</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>535 - 907 · 一个边镇的世纪</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#关陇集团 #武川 #隋唐 #中国历史</text>
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
