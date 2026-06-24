#!/usr/bin/env python3
"""Generate 4 cards for 侯景."""
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
    "A lone fierce general standing before a burning ancient Chinese palace, flames reflected in dark armor, holding a general's seal, dramatic crimson and black color scheme, traditional Chinese ink wash painting, Song dynasty aesthetic, dark and epic atmosphere",
    "Ancient Chinese scene of a treacherous general kneeling in submission before one emperor then stabbing the next, four different banners behind him showing his betrayals, chaotic battlefield, dark stormy sky, traditional Chinese ink wash painting",
    "Ancient Chinese city under siege, massive army attacking the walls of Jiankang, flames and smoke rising, desperation and chaos, traditional Chinese ink wash painting, dark red and black palette, Song dynasty aesthetic",
    "Ancient Chinese warship on river, a lone general's corpse being carried away by soldiers, a fallen crown and a banner reading 宇宙大将军 in the mud, poetic downfall, twilight sky, traditional Chinese ink wash painting, tragic atmosphere",
]

FILES = ["houjing-cover", "houjing-card-1", "houjing-card-2", "houjing-card-3"]

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
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#EF4444" letter-spacing="6" {STROKE}>南北朝·侯景之乱</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>侯景</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#EF4444" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="800" fill="#EF4444" letter-spacing="6" {STROKE}>宇宙大将军</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>五姓家奴 · 江南浩劫 · 自封全宇宙总管</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#侯景 #宇宙大将军 #侯景之乱 #南北朝 #梁朝</text>
''')

def make_card_1(bg_b64):
    items = [
        ("尔朱荣 → 高欢", "从北魏到东魏，反复横跳"),
        ("叛东魏投梁", "高欢一死立刻翻脸"),
        ("梁武帝收留", "给他大将军之位，但他嫌官小"),
        ("反噬梁朝", "仅带八百人起兵，一路打到建康"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 165 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#EF4444"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#EF4444" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>五姓家奴的背叛之路</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#DC2626" letter-spacing="3" {STROKE}>侯景之乱</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>围困建康</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>五千人打败梁朝几十万大军</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>饿死梁武帝</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>86岁的南朝明君被活活饿死</text>
</g>

<g transform="translate(40, 460)">
  <rect x="0" y="0" width="944" height="110" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#DC2626"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>江南浩劫</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>数百年繁华，一朝化为灰烬</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#DC2626" {STROKE}>他把一个百年王朝拖入深渊</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#侯景之乱 #梁朝 #建康 #南北朝</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>宇宙大将军 & 结局</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>自封宇宙大将军</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>中国史上最狂妄的称号，没有之一</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>部下背叛</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>当了一年皇帝就被部下出卖</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#CBD5E1" {STROKE}>惨死</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>逃跑途中被随从杀死，剁成肉酱</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>从宇宙大将军到一堆肉酱</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇宙大将军 #侯景 #乱世枭雄 #历史</text>
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
