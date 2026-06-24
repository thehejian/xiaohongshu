#!/usr/bin/env python3
"""Generate 4 cards for 刘牢之和北府军."""
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
    "Ferocious ancient Chinese army of northern refugee warriors marching through a mountain pass, battle-worn faces, determined and fierce, iron armor and weapons, traditional Chinese ink wash painting, Song dynasty aesthetic, steel blue and gray palette",
    "Ancient Chinese general leading a cavalry charge across a river, vanguard of a massive battle, fierce determination, arrows flying, dramatic battle scene, traditional Chinese ink wash painting, Song dynasty aesthetic",
    "Ancient Chinese general changing sides at a council of war, switching his allegiance, tense political scene with multiple powerful figures watching, traditional Chinese ink wash painting, Song dynasty aesthetic, shadowy and uncertain atmosphere",
    "Ancient Chinese general hanging himself in despair, abandoned army camp outside, his armor and sword discarded, tragic end of a once-great warrior, traditional Chinese ink wash painting, Song dynasty aesthetic, mournful tone",
]

FILES = ["liulaozhi-cover", "liulaozhi-card-1", "liulaozhi-card-2", "liulaozhi-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#64748B" letter-spacing="6" {STROKE}>东晋·北府军</text>
<text x="512" y="340" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>刘牢之</text>
<rect x="312" y="390" width="400" height="3" rx="1.5" fill="#64748B" opacity="0.7"/>
<text x="512" y="500" text-anchor="middle" font-family="{FONT}" font-size="46" font-weight="800" fill="#64748B" letter-spacing="4" {STROKE}>北府军的背叛者</text>
<text x="512" y="600" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>淝水先锋 · 三叛 · 引出自灭</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘牢之 #北府军 #北府兵 #淝水之战 #东晋</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#475569" letter-spacing="3" {STROKE}>北府军的诞生</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>谢玄招募流民</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>在京口招募北方流亡者组建新军</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>亡命之徒</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>家乡被占，无路可退，打仗最拼命</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#475569"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>南北朝最强军队</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>后来刘裕以同一支军队建立刘宋</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#475569" {STROKE}>没有北府军，就没有南朝</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北府军 #北府兵 #谢玄 #京口 #东晋</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>淝水先锋 · 三叛</text>

<g transform="translate(40, 145)">
  <rect x="0" y="0" width="944" height="95" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="95" rx="3" fill="#3B82F6"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#3B82F6" {STROKE}>淝水之战率五千精锐打前锋</text>
  <text x="30" y="68" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>一战成名，成为北府军核心人物</text>
</g>

<g transform="translate(40, 265)">
  <rect x="0" y="0" width="944" height="95" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="95" rx="3" fill="#EF4444"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#EF4444" {STROKE}>一叛：叛司马道子</text>
  <text x="30" y="68" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>先追随，后翻脸</text>
</g>

<g transform="translate(40, 385)">
  <rect x="0" y="0" width="944" height="95" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="95" rx="3" fill="#EF4444"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#EF4444" {STROKE}>二叛：降桓玄</text>
  <text x="30" y="68" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>奉命讨伐桓玄，中途投敌</text>
</g>

<g transform="translate(40, 505)">
  <rect x="0" y="0" width="944" height="95" rx="12" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="95" rx="3" fill="#EF4444"/>
  <text x="30" y="38" font-family="{FONT}" font-size="24" font-weight="700" fill="#EF4444" {STROKE}>三叛：背桓玄</text>
  <text x="30" y="68" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>后悔投降又想反，但已无人追随</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>反复叛变，最终自掘坟墓</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘牢之 #背叛 #北府军 #东晋</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#78716C" letter-spacing="3" {STROKE}>自杀 & 北府军的结局</text>

<g transform="translate(40, 145)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>众叛亲离</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>部下看不起他反复无常，纷纷离去</text>
</g>

<g transform="translate(40, 285)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>自缢身亡</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>上吊自杀，北府军陷入混乱</text>
</g>

<g transform="translate(40, 425)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#78716C"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>刘裕继承</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>北府军残部被刘裕收编，开创刘宋</text>
</g>

<text x="512" y="680" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#78716C" {STROKE}>不忠诚比没本事死得更快</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘牢之 #刘裕 #北府军 #刘宋 #南朝</text>
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
