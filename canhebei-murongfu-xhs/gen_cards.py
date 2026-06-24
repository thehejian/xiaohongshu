#!/usr/bin/env python3
"""Generate 4 cards for 参合陂·慕容复."""
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
    "Ancient Chinese style martial arts novel scene, a proud prince in elegant robes at a lakeside manor named 'Canhe Manor', misty lake and pavilions, wuxia atmosphere, traditional Chinese ink wash painting, Song dynasty aesthetic, blue and gray tones, dramatic and poetic",
    "Ancient Chinese battle scene on a frozen river, cavalry charging across ice, surprise attack at dawn, chaotic battle, traditional Chinese ink wash painting, Song dynasty aesthetic, cold blue and white tones, epic destruction",
    "Ancient Chinese general consumed by sorrow, elderly and defeated, grieving over a lost battle that destroyed his kingdom's future, traditional Chinese ink wash painting, Song dynasty aesthetic, muted gray and dark tones, tragic",
    "A symbolic artistic scene showing two eras colliding: an ancient battlefield fading into a wuxia manor, time overlapping, historical tragedy echoing through fiction, traditional Chinese ink wash painting, surreal style, blue and gold tones, atmospheric",
]

FILES = ["canhe-cover", "canhe-card-1", "canhe-card-2", "canhe-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="700" fill="#475569" letter-spacing="6" {STROKE}>历史×武侠</text>
<text x="512" y="340" text-anchor="middle" font-family="{FONT}" font-size="80" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>慕容复的野望</text>
<rect x="262" y="380" width="500" height="3" rx="1.5" fill="#475569" opacity="0.6"/>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#475569" letter-spacing="6" {STROKE}>参合陂·参合庄·参合指</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>天龙八部 · 后燕亡国 · 历史的讽刺</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#天龙八部 #慕容复 #参合陂 #金庸 #慕容垂 #参合庄 #参合指</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#475569" letter-spacing="3" {STROKE}>金庸笔下的参合</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>参合庄</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>慕容复的家——燕子坞参合庄</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>参合指</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>慕容博的绝学之一——参合指</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>绝非巧合</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>金庸用"参合"二字，暗藏了一段灭国史</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>参合庄的"庄"，是参合陂的"陂"改的</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#天龙八部 #慕容复 #参合庄 #参合指 #金庸文化</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#475569" letter-spacing="3" {STROKE}>参合陂之战（395年）</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>慕容宝伐北魏</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>后燕太子率精锐征讨拓跋珪</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>拓跋珪回马枪</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>假装西逃，结冰后黄河奇袭</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>数万燕军被活埋</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>后燕精锐一夜覆灭——国家从此走向死亡</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>慕容家复兴大燕的梦，在参合陂断了根</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#慕容垂 #拓跋珪 #参合陂 #后燕 #北魏 #十六国</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="800" fill="#475569" letter-spacing="3" {STROKE}>命运的讽刺</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>慕容垂含恨而死</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>听到参合陂惨败，又悲又气，不久去世</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>后燕二十年后灭亡</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>参合陂一战直接决定了慕容氏的下场</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>金庸的深意</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>慕容复住参合庄——住在自己祖坟上做梦</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="700" fill="#475569" {STROKE}>换了字，逃不了命——参合庄的噩梦，慕容复也在做</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#天龙八部 #慕容复 #金庸 #参合陂 #参合庄 #命运的讽刺</text>
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
