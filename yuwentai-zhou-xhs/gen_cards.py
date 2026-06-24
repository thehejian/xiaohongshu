#!/usr/bin/env python3
"""Generate 4 cards for 宇文泰."""
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
    "Ancient Chinese military commander in dark armor standing on a mountain pass overlooking the Guanzhong plains, holding a command token, stern and determined expression, dramatic clouds, traditional Chinese ink wash painting, Song dynasty aesthetic, epic and majestic, deep blue and gold palette",
    "Ancient Chinese battle scene in a vast reed marsh, ambush unfolding, soldiers charging from reeds, arrows flying, two armies clashing at sunset, chaotic yet strategic, traditional Chinese ink wash painting, Song dynasty aesthetic, dramatic orange and blue sky",
    "Ancient Chinese imperial council chamber, eight military commanders kneeling before a leader, banners and weapons displayed, ceremony of establishing a new military order, solemn atmosphere, traditional Chinese ink wash painting, Song dynasty aesthetic, rich colors",
    "Ancient Chinese timeline vision, a single general's figure at the root, branching into three imperial lineages: Northern Zhou, Sui, and Tang, interconnected by threads of fate, scroll-like composition, traditional Chinese ink wash painting, Song dynasty aesthetic",
]

FILES = ["yuwentai-cover", "yuwentai-card-1", "yuwentai-card-2", "yuwentai-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="35%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#3B82F6" letter-spacing="6" {STROKE}>南北朝·西魏·北周</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>宇文泰</text>
<rect x="312" y="405" width="400" height="3" rx="1.5" fill="#3B82F6" opacity="0.7"/>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#3B82F6" letter-spacing="4" {STROKE}>关陇集团之父</text>
<text x="512" y="600" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>武川出身 · 沙苑破敌 · 隋唐奠基</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇文泰 #关陇集团 #八柱国 #西魏 #北周</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#F59E0B" letter-spacing="3" {STROKE}>沙苑之战 · 两万破二十万</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>高欢来犯</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>东魏二十万大军压境，西魏危在旦夕</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>芦苇伏兵</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>宇文泰把仅有两万人埋伏在芦苇丛中</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>一战定乾坤</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>高欢大败，西魏由此站稳脚跟</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>中国军事史上经典以少胜多</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#沙苑之战 #宇文泰 #高欢 #以少胜多</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>制度遗产</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="125" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="125" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>八柱国</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>八大军事贵族统领体系，武川系为核心</text>
  <text x="30" y="108" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>被隋唐继承，影响中国数百年</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="125" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="125" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>府兵制</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>兵农合一，平时种地战时打仗</text>
  <text x="30" y="108" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>自给自足的军事体系，沿用至唐中期</text>
</g>

<g transform="translate(40, 470)">
  <rect x="0" y="0" width="944" height="125" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="125" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>关陇集团</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>以武川军人为核心的贵族军事集团</text>
  <text x="30" y="108" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>宇文泰是这一政治集团的总设计师</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#八柱国 #府兵制 #关陇集团 #宇文泰</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>隋唐帝国的精神祖先</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>北周</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>儿子宇文觉逼西魏禅让，建北周</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>隋</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>杨坚继承关陇集团的政治遗产建隋</text>
</g>

<g transform="translate(40, 450)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>唐</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>李渊同为关陇集团出身，承袭府兵制</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>三代而兴，三百年而不衰</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇文泰 #隋唐 #关陇集团 #八柱国</text>
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
