#!/usr/bin/env python3
"""Generate 4 cards for 杨坚."""
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
    "Ancient Chinese emperor in magnificent golden and yellow imperial robes, standing with supreme authority, founder of the Sui dynasty, unifier of China, traditional Chinese ink wash painting, Tang dynasty aesthetic, imperial yellow and gold palette, monumental",
    "Ancient Chinese military aristocrat from the Wuchuan garrison, descendant of a warrior family, part of the Guanlong aristocratic group, traditional Chinese ink wash painting, Tang dynasty aesthetic, deep blue and gold tones",
    "Ancient Chinese ceremony of dynastic founding, a new emperor receiving the mandate of heaven, establishing the Sui dynasty, traditional Chinese ink wash painting, Tang dynasty aesthetic, gold and vermilion palette, solemn",
    "Ancient Chinese grand unification scene, the Yangtze River crossing, Sui army conquering the Chen dynasty, end of centuries of division, traditional Chinese ink wash painting, Tang dynasty aesthetic, epic landscape with golden sky",
]

FILES = ["yangjian-cover", "yangjian-card-1", "yangjian-card-2", "yangjian-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#EAB308" letter-spacing="6" {STROKE}>隋·文帝</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="10" {STROKE}>杨坚</text>
<rect x="262" y="405" width="500" height="3" rx="1.5" fill="#EAB308" opacity="0.7"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="48" font-weight="800" fill="#EAB308" letter-spacing="6" {STROKE}>终结三百年分裂</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>武川后代 · 代周建隋 · 开皇之治 · 灭陈统一</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#杨坚 #隋文帝 #开皇之治 #统一 #南北朝 #隋朝</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EAB308" letter-spacing="3" {STROKE}>武川后代</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>父：杨忠</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>武川镇出身的"战神"，西魏十二大将军之一</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>岳父：独孤信</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>八柱国之一，七女嫁三朝皇帝</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>关陇集团嫡系传人</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>从武川到隋朝——这个圈子走出了一部南北朝史</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>武川集团的终极果实</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#杨坚 #杨忠 #独孤信 #武川集团 #关陇集团</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EAB308" letter-spacing="3" {STROKE}>代周建隋</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>外戚辅政</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>女儿是北周宣帝皇后，580年宣帝死，杨坚辅政</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>581年受禅</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>逼北周静帝禅让，建立隋朝</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>权力转移</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>关陇集团内部，从宇文氏到杨氏的和平交替</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>宇文泰始创的基业，被他的后代继承人接过了</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#杨坚 #隋朝 #北周 #禅让 #关陇集团</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EAB308" letter-spacing="3" {STROKE}>开皇之治 · 天下一统</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>589年灭陈统一</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>从311年永嘉之乱算起，近300年分裂终结束</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>制度奠基</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>均田制、三省六部、科举雏形——隋为唐用</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EAB308"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>晚年猜忌</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>杀功臣、废太子，最终被次子杨广谋害</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EAB308" {STROKE}>一个复杂的人，一个伟大的时代开启者</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#杨坚 #开皇之治 #隋朝 #统一 #隋文帝 #南北朝</text>
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
