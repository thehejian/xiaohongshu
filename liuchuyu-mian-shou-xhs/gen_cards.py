#!/usr/bin/env python3
"""Generate 4 cards for 刘楚玉."""
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
    "Ancient Chinese princess in magnificent rose and gold silk robes, bold and confident expression, standing proudly in a palace garden, the famous Princess Shanyin, traditional Chinese ink wash painting, Song dynasty aesthetic, rose and gold palette, majestic feminine power",
    "Ancient Chinese palace scene, a princess boldly confronting her brother the emperor, demanding equal treatment, dramatic and charged atmosphere, traditional Chinese ink wash painting, Song dynasty aesthetic, warm gold and crimson tones",
    "Ancient Chinese palace garden with a princess surrounded by handsome attendants, luxurious and unconventional scene, traditional Chinese ink wash painting, Song dynasty aesthetic, pink and jade tones, decadent beauty",
    "Ancient Chinese palace in somber mood, a young princess in simple robes facing her fate, tragic and dignified, traditional Chinese ink wash painting, Song dynasty aesthetic, muted gray and pale rose tones",
]

FILES = ["liuchuyu-cover", "liuchuyu-card-1", "liuchuyu-card-2", "liuchuyu-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#E11D48" letter-spacing="6" {STROKE}>南朝·山阴公主</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="120" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>刘楚玉</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#E11D48" opacity="0.7"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#E11D48" letter-spacing="6" {STROKE}>谁说女子不如男</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>质问朝堂 · 三十面首 · 千年争议</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘楚玉 #山阴公主 #面首 #谁说女子不如男 #南朝</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#E11D48" letter-spacing="3" {STROKE}>石破天惊的问</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#E11D48"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>公主 vs 皇帝</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>对弟弟刘子业说：凭什么你后宫上万，我只有一个老公？</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#E11D48"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>事不均平</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"事不均平，一何至此"——1500年前的女权呐喊</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#E11D48"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>帝王哑口无言</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>刘子业无法反驳——逻辑上她说的完全正确</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>一千五百年前，一个公主质问公平</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘楚玉 #山阴公主 #公平 #性别 #刘宋</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#E11D48" letter-spacing="3" {STROKE}>三十面首</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#E11D48"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>面首的由来</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"面"是美貌，"首"是头发——面首即美男子</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#E11D48"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>皇帝特批</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>刘子业真给她配了30个，历史上独一份</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#E11D48"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>文化符号</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"面首"一词从此进入中文词汇</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>用一句质问，创造了一个千年词汇</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘楚玉 #面首 #山阴公主 #中国历史 #中文词汇</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#78716C" letter-spacing="3" {STROKE}>结局·争议</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>刘彧赐死</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>刘子业死后，被叔叔刘彧赐死</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>不到二十岁</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>短暂而激烈的一生，像一朵盛极而亡的花</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>千年争议</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>是女权先驱，还是放纵公主？众说纷纭</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#E11D48" {STROKE}>她用一生，问了一个永不过时的问题</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘楚玉 #山阴公主 #女权 #南朝 #中国历史 #奇女子</text>
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
