#!/usr/bin/env python3
"""Generate 4 cards for 陈后主."""
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
    "Ancient Chinese last emperor of the Southern Dynasties, decadent and poetic, sitting in a luxurious palace with beautiful concubines, flowers in the courtyard, traditional Chinese ink wash painting, Song dynasty aesthetic, rose and gold palette, melancholic beauty",
    "Ancient Chinese imperial concubine with extraordinarily long hair, Zhang Lihua, beautiful and elegant in a Chen dynasty palace, traditional Chinese ink wash painting, Song dynasty aesthetic, pink and jade tones, ethereal beauty",
    "Ancient Chinese scene of an emperor hiding in a well with two concubines, Sui soldiers discovering them, dramatic and darkly comic, traditional Chinese ink wash painting, Song dynasty aesthetic, gray and dark tones",
    "Ancient Chinese scene of the fall of a dynasty, Sui soldiers entering Jiankang palace, end of an era, traditional Chinese ink wash painting, Song dynasty aesthetic, gray and desolate tones, epic",
]

FILES = ["chen-cover", "chen-card-1", "chen-card-2", "chen-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#F43F5E" letter-spacing="6" {STROKE}>南朝·末帝</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>陈叔宝</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#F43F5E" opacity="0.7"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#F43F5E" letter-spacing="6" {STROKE}>隔江犹唱后庭花</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>玉树后庭花 · 胭脂井 · 南朝终章</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈后主 #陈叔宝 #南朝 #后庭花 #胭脂井 #杜牧</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#F43F5E" letter-spacing="3" {STROKE}>玉树后庭花</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F43F5E"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F43F5E" {STROKE}>不理朝政</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>整天跟文人妃子饮酒作乐</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F43F5E"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F43F5E" {STROKE}>张丽华</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>头发七尺长，光可鉴人，宠冠后宫</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F43F5E"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F43F5E" {STROKE}>亡国之音</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"妖姬脸似花含露，玉树流光照后庭"</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F43F5E" {STROKE}>美人是祸水，歌是亡国之音</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈后主 #张丽华 #玉树后庭花 #南朝 #陈朝</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#78716C" letter-spacing="3" {STROKE}>井中天子</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>589年隋灭陈</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>杨广率军攻入建康</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>跳井躲藏</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>拉着张丽华和孔贵嫔躲进枯井</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>胭脂井</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>三人被拉上来，胭脂蹭到井口，后世得名</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>亡国之君最荒诞的一幕</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈后主 #胭脂井 #隋灭陈 #杨广 #魏晋南北朝</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#78716C" letter-spacing="3" {STROKE}>南朝终章</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>300年分裂结束</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>隋灭陈，南北朝终结，天下统一</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>商女不知亡国恨</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>杜牧过秦淮，闻歌女唱后庭花而作</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>最文学化的亡国</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>以一首艳曲终结一个时代</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F43F5E" {STROKE}>宋齐梁陈——南朝四代，到此终</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#陈后主 #杜牧 #南朝 #南北朝 #隋 #中国历史</text>
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
