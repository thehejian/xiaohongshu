#!/usr/bin/env python3
"""Generate 4 cards for 北齐律."""
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
    "Ancient Chinese scroll of law and justice, stacks of bamboo slips and scrolls with Chinese legal text, a gavel carved from jade, solemn and scholarly atmosphere, dark background with warm candlelight, traditional Chinese painting style, Song dynasty aesthetic, highly detailed",
    "Ancient Chinese legal symbols, the words 十恶不赦 written in bold red ink on a scroll, surrounded by bamboo slips, seals, and judgment tokens, solemn and authoritative mood, traditional Chinese ink wash with red accents, Song dynasty aesthetic",
    "Ancient Chinese library with 12 scrolls arranged in a semicircle, each scroll labeled with Chinese characters representing legal chapters, a wooden desk with traditional writing brushes, scholarly atmosphere, muted colors with gold accents, traditional Chinese painting style",
    "Timeline visualization in ancient Chinese style, from Northern Qi scroll to Tang code to Qing dynasty law, a long scroll spanning across three eras, ancestral connection of law through Chinese history, traditional ink wash, warm aged-paper tones, Song dynasty aesthetic",
]

FILES = ["beiqi-lv-cover", "beiqi-lv-card-1", "beiqi-lv-card-2", "beiqi-lv-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="40%" stop-color="#000" stop-opacity="0.2"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>南北朝·北齐</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="140" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>北齐律</text>
<rect x="312" y="405" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="490" text-anchor="middle" font-family="{FONT}" font-size="42" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>十恶不赦的出处</text>
<text x="512" y="580" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>禽兽王朝 · 千年法典</text>
<text x="512" y="640" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#94A3B8" {STROKE_S}>影响中国1300年的法律基石</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北齐律 #十恶不赦 #法制史 #南北朝</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>十恶不赦的由来</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>重罪十条</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>北齐律首创，列出十条最不能饶恕的大罪</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>隋唐演变</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>隋开皇律改称"十恶"，唐律沿用</text>
</g>

<g transform="translate(40, 450)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>沿用至清末</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>十恶不赦一词，用了整整1300年</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>每天说的成语，来自一部千年法典</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北齐律 #十恶不赦 #成语故事</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>12篇体系结构</text>

<g transform="translate(40, 145)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <text x="40" y="46" font-family="{FONT}" font-size="22" font-weight="700" fill="#FFD700" {STROKE}>名例律 · 禁卫律 · 职制律</text>
  <text x="40" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>总则 · 宫廷警卫 · 官吏职责</text>
</g>

<g transform="translate(40, 265)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <text x="40" y="46" font-family="{FONT}" font-size="22" font-weight="700" fill="#FFD700" {STROKE}>户婚律 · 厩库律 · 擅兴律</text>
  <text x="40" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>户籍婚姻 · 仓库畜牧 · 军事征调</text>
</g>

<g transform="translate(40, 385)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <text x="40" y="46" font-family="{FONT}" font-size="22" font-weight="700" fill="#FFD700" {STROKE}>贼盗律 · 斗讼律 · 诈伪律</text>
  <text x="40" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>贼盗 · 斗殴诉讼 · 欺诈伪造</text>
</g>

<g transform="translate(40, 505)">
  <rect x="0" y="0" width="944" height="100" rx="12" fill="#0F172A" opacity="0.82"/>
  <text x="40" y="46" font-family="{FONT}" font-size="22" font-weight="700" fill="#FFD700" {STROKE}>杂律 · 捕亡律 · 断狱律</text>
  <text x="40" y="76" font-family="{FONT}" font-size="18" fill="#CBD5E1" {STROKE_S}>杂项 · 追捕逃犯 · 审判程序</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#3B82F6" {STROKE_S}>隋唐律直接复制这个框架</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北齐律 #唐律疏议 #中国法制史</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>影响千年的遗产</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>隋 · 开皇律</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>直接以北齐律为蓝本编纂</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>唐 · 唐律疏议</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>中华法系巅峰，框架继承北齐</text>
</g>

<g transform="translate(40, 450)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>宋元明清</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>全都在北齐律框架上修修补补</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>一部禽兽王朝的遗产</text>
<text x="512" y="780" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>比它所有皇帝加起来都伟大</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#北齐律 #中华法系 #法律史</text>
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
