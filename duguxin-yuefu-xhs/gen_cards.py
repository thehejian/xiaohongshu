#!/usr/bin/env python3
"""Generate 4 cards for 独孤信."""
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
    "Ancient Chinese handsome general in magnificent armor, elegant and handsome features, standing in a blooming garden with a slight smile, traditional Chinese ink wash painting, Song dynasty aesthetic, purple and gold palette, refined and noble atmosphere",
    "Ancient Chinese city street, a handsome general riding through town with his cap slightly tilted, young men all imitating his tilted cap style, lively market scene, traditional Chinese ink wash painting, Song dynasty aesthetic, warm and humorous",
    "Ancient Chinese wedding ceremony scene, a father sending three daughters to three different imperial palaces, three brides in phoenix crowns and red wedding gowns, grand processions, traditional Chinese ink wash painting, Song dynasty aesthetic, rich red and gold colors, poetic",
    "Ancient Chinese family tree painting, a single father figure at the root branching into three imperial lineages: Northern Zhou, Sui, and Tang, flowing scroll composition, traditional Chinese ink wash painting, Song dynasty aesthetic, warm aged tones",
]

FILES = ["duguxin-cover", "duguxin-card-1", "duguxin-card-2", "duguxin-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#A855F7" letter-spacing="6" {STROKE}>南北朝·八柱国</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="160" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>独孤信</text>
<rect x="312" y="405" width="400" height="3" rx="1.5" fill="#A855F7" opacity="0.7"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#A855F7" letter-spacing="4" {STROKE}>最牛老丈人</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>侧帽风流 · 三朝国丈 · 三个皇后</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#独孤信 #八柱国 #最强岳父 #北周 #隋 #唐</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#A855F7" letter-spacing="3" {STROKE}>侧帽风流</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>美男子</text>
  <text x="30" y="86" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>史称"美容仪，善骑射"——又帅又能打</text>
</g>

<g transform="translate(40, 330)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>侧帽典故</text>
  <text x="30" y="86" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>打猎回来帽子歪了，全城年轻人跟风模仿</text>
</g>

<g transform="translate(40, 500)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>八柱国</text>
  <text x="30" y="86" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>西魏最高军事统帅，武川系核心人物</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#侧帽风流 #独孤信 #八柱国 #美男子</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>三个女儿 · 三个皇后</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>长女 → 北周明帝</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>嫁宇文毓，北周皇后</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>四女 → 唐高祖之母</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>嫁李昞，生李渊（唐高祖）</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>七女 → 隋文帝皇后</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>独孤伽罗嫁杨坚，生杨广</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>北周 · 隋 · 唐 — 三朝皇后出独孤</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#独孤信 #三朝国丈 #北周 #隋 #唐 #皇后</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#A855F7" letter-spacing="3" {STROKE}>悲剧与遗产</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>被迫自杀</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>权臣宇文护逼他自尽，年仅55岁</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>死后荣耀</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>女儿们相继成为三朝皇后</text>
</g>

<g transform="translate(40, 470)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#A855F7"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>血脉统治</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>北周—隋—唐三百年，都是他的后代</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>帅了一辈子，打了一辈子</text>
<text x="512" y="820" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#A855F7" {STROKE}>最后靠女儿赢了整个天下</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#独孤信 #最强岳父 #南北朝 #历史人物</text>
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
