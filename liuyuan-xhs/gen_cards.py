#!/usr/bin/env python3
"""Generate 4 cards for Liu Yuan / Han Zhao using Agnes AI backgrounds."""
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
    "Epic cinematic portrait of a powerful Xiongnu war king in magnificent armor on a black horse at sunset, wearing a Chinese-style dragon crown, vast Mongolian steppe in background, dramatic golden light, traditional Chinese ink wash meets epic fantasy, majestic composition, Song dynasty aesthetic, highly detailed",
    "Ancient nomadic Xiongnu camp on the Mongolian steppe at dawn, felt tents and horse herds, a young prince reading Chinese scrolls, blend of northern grassland culture and Chinese civilization, epic historical scene, misty horizon, traditional Chinese painting style",
    "Massive nomadic army marching across a vast plain, thousands of Xiongnu warriors with banners, a king in chariot leading the host, dramatic cloudy sky, dust and smoke, epic ancient Chinese battlefield, traditional ink wash painting meets cinematic scope, Song dynasty aesthetic",
    "Ancient Chinese imperial palace scene, a Xiongnu king on dragon throne wearing both steppe and Chinese regalia, court officials paying homage, magnificent hall, dramatic light through pillars, blend of two cultures, traditional Chinese painting, epic historical moment",
]

FILES = ["liuyuan-cover", "liuyuan-card-1", "liuyuan-card-2", "liuyuan-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="40%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.65"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="700" fill="#FFD700" letter-spacing="8" {STROKE}>五胡十六国</text>
<text x="512" y="400" text-anchor="middle" font-family="{FONT}" font-size="170" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>刘渊</text>
<rect x="312" y="445" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="545" text-anchor="middle" font-family="{FONT}" font-size="58" font-weight="800" fill="#FFD700" letter-spacing="5" {STROKE}>匈奴汉王</text>
<text x="512" y="630" text-anchor="middle" font-family="{FONT}" font-size="30" fill="#FFFFFF" {STROKE_S}>第一个称帝的匈奴人</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>汉赵建立者</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>庙号高祖</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>304 - 310</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘渊 #匈奴 #汉赵 #十六国 #五胡十六国</text>
''')

def make_card_1(bg_b64):
    items = [
        ("匈奴王子", "左贤王刘豹之子，自幼在洛阳为质"),
        ("汉化教育", "读《春秋》《孙子兵法》，文武双全"),
        ("八王之乱", "晋室内乱，匈奴各部推举刘渊为大单于"),
        ("志在天下", "\u201c大丈夫当为汉高、魏武，呼韩邪何足效也！\u201d"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#FFD700"/>
  <text x="30" y="48" font-family="{FONT}" font-size="30" font-weight="700" fill="#FFD700" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="24" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>从匈奴王子到汉王</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>建国称帝</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="200" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="200" rx="3" fill="#FFD700"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#FFD700" {STROKE}>304年 · 左国城称汉王</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>自称汉朝公主后代，继承汉统</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>建国号\u201c汉\u201d，改元元熙</text>
  <text x="30" y="172" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>匈奴人第一次以皇帝自称</text>
</g>

<g transform="translate(40, 400)">
  <rect x="0" y="0" width="944" height="200" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="200" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#E2E8F0" {STROKE}>政治策略</text>
  <text x="30" y="98" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>用汉文化包装胡人政权</text>
  <text x="30" y="135" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>设百官，立宗庙，行汉制</text>
  <text x="30" y="172" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>开启胡人政权的汉化模式</text>
</g>

<g transform="translate(40, 640)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="28" font-weight="700" fill="#FFD700" {STROKE}>继承人</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>子刘聪继位，311年破洛阳，316年灭西晋</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘渊 #汉赵 #十六国</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>历史意义</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="160" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="160" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>第一个称帝的匈奴人</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>打破\u201c胡人不可为帝王\u201d的政治禁忌</text>
  <text x="30" y="125" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>为石勒、苻坚、慕容垂等人开辟道路</text>
</g>

<g transform="translate(40, 350)">
  <rect x="0" y="0" width="944" height="160" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="160" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>汉化模式的先驱</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>用汉文化包装胡人政权，争取汉人士族支持</text>
  <text x="30" y="125" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>这一模式被五胡十六国所有胡人政权沿用</text>
</g>

<g transform="translate(40, 550)">
  <rect x="0" y="0" width="944" height="160" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="160" rx="3" fill="#FFD700"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>开启五胡十六国序幕</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>汉赵之后，成汉、后赵、前燕、前秦相继建立</text>
  <text x="30" y="125" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>中国进入长达135年的分裂时代</text>
</g>

<text x="512" y="820" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>不必做草原上的狼，也可以当中原的王</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘渊 #匈奴 #五胡十六国 #历史</text>
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
