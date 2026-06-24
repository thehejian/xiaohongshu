#!/usr/bin/env python3
"""Generate 4 cards for 孝文帝改革."""
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
    "A young Xianbei emperor in magnificent Han Chinese imperial dragon robes sitting on throne in Luoyang palace, Northern Wei dynasty, cultural transformation scene, majestic golden light streaming through windows, traditional Chinese painting meets epic historical scale, Song dynasty aesthetic, young emperor with visionary expression",
    "Epic ancient Chinese scene, an emperor leading his entire court and army on a journey south, grand procession crossing Yellow River, thousands of soldiers and carts, Luoyang city walls in distance, relocation of a civilization, traditional Chinese ink wash scroll painting, cinematic grand scale",
    "Ancient Chinese imperial court, an emperor issuing decrees of reform, ministers in Han Chinese robes, some kneeling in submission some looking reluctant, scrolls of new laws, cultural transformation scene, traditional Chinese painting, tense political atmosphere, Song dynasty aesthetic",
    "Dual scene composition: left side a magnificent Luoyang palace with thriving culture and grand ceremonies, right side bleak northern garrisons with disgruntled soldiers in abandoned fortresses, split screen fate of an empire, traditional Chinese ink wash painting, dramatic contrast, Song dynasty aesthetic",
]

FILES = ["xiaowen-cover", "xiaowen-card-1", "xiaowen-card-2", "xiaowen-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.1"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.6"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>北魏·太和改制</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>孝文帝改革</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>一场改变中国历史的汉化运动</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>迁都洛阳 · 改汉姓 · 穿汉服 · 说汉语</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>北魏孝文帝</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>拓跋宏→元宏</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>467 - 499</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#孝文帝 #太和改制 #北魏 #汉化 #迁都洛阳</text>
''')

def make_card_1(bg_b64):
    items = [
        ("迁都洛阳", "494年以'南征'为名迁都，摆脱旧贵族"),
        ("改汉姓", "拓跋改元，独孤改刘，百余姓氏汉化"),
        ("穿汉服", "禁止鲜卑服装，改穿汉人衣冠"),
        ("说汉语", "30岁以下官员必须说汉语，违者免职"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#FFD700"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#FFD700" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>四大汉化政策</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>迁都洛阳</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>背景</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>旧都平城（大同）偏居塞北</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>鲜卑旧势力强大，改革阻力大</text>
</g>

<g transform="translate(40, 350)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>妙计</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>宣称南征萧齐，率大军南下</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>到洛阳后宣布——不走了，定都于此</text>
</g>

<g transform="translate(40, 540)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>影响</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>远离旧贵族势力掌控</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>扎根中原，加速汉化进程</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#孝文帝 #迁都洛阳 #平城 #北魏</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>争议与遗产</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>正面</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>北魏转型为中原王朝，融入华夏文明</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>推动民族融合，影响深远</text>
</g>

<g transform="translate(40, 330)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>负面</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>太子元恂因反对被赐死</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>六镇被遗忘，最终引发叛混乱</text>
</g>

<g transform="translate(40, 510)">
  <rect x="0" y="0" width="944" height="140" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="140" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>总结</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>一场改革强盛了三十年</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>也埋下了灭亡的种子</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#孝文帝 #六镇 #北魏 #南北朝 #历史</text>
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
