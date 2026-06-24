#!/usr/bin/env python3
"""Generate 4 cards for 六镇之乱."""
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
    "Ancient Chinese northern frontier fortress under siege, massive battle scene at night with fire and torches, soldiers in Chinese armor storming gates, dramatic flames and smoke, dangerous atmosphere, traditional Chinese ink wash painting meets cinematic epic, Song dynasty aesthetic, chaos and rebellion",
    "Ancient Chinese northern frontier, desolate military garrison on cold barren steppe, lonely fortress walls against grey sky, abandoned watchtowers, neglected soldiers in worn armor, melancholy atmosphere, traditional Chinese painting, cold color palette, Song dynasty aesthetic",
    "Epic ancient Chinese battle scene, rebel soldiers on horseback charging across the northern plains, torches and banners flying, massive uprising, chaotic cavalry charge at dawn, dust and fury, traditional Chinese ink wash meets cinematic scale, Song dynasty aesthetic",
    "Ancient Chinese empire splitting apart, symbolic scene of a map of Northern Wei cracking into two pieces, two emerging power centers symbolized by army camps on east and west, twilight over divided land, traditional Chinese painting, dramatic historical metaphor, Song dynasty aesthetic",
]

FILES = ["liuzhen-cover", "liuzhen-card-1", "liuzhen-card-2", "liuzhen-card-3"]

def svg_card(bg_b64, text_layer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1024" height="1024" viewBox="0 0 1024 1024">
<defs>
  <linearGradient id="ovG" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000" stop-opacity="0"/>
    <stop offset="30%" stop-color="#000" stop-opacity="0.15"/>
    <stop offset="100%" stop-color="#000" stop-opacity="0.7"/>
  </linearGradient>
</defs>
<image href="data:image/png;base64,{bg_b64}" x="0" y="0" width="1024" height="1024" preserveAspectRatio="xMidYMid slice"/>
<rect x="0" y="0" width="1024" height="1024" fill="url(#ovG)"/>
{text_layer}
</svg>'''

def make_cover(bg_b64):
    return svg_card(bg_b64, f'''
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="36" font-weight="700" fill="#EF4444" letter-spacing="6" {STROKE}>北魏·亡国之乱</text>
<text x="512" y="370" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>六镇之乱</text>
<rect x="312" y="415" width="400" height="3" rx="1.5" fill="#EF4444" opacity="0.7"/>
<text x="512" y="520" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="800" fill="#EF4444" letter-spacing="4" {STROKE}>孝文帝改革埋下的定时炸弹</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>523年 · 塞北烽火 · 帝国崩塌的起点</text>
<g transform="translate(262, 710)">
  <text x="0" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>六个军事重镇</text>
  <text x="250" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="middle" {STROKE_S}>破六韩拔陵起义</text>
  <text x="500" y="34" font-family="{FONT}" font-size="22" fill="#CBD5E1" text-anchor="end" {STROKE_S}>北魏分裂东魏西魏</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#六镇之乱 #北魏 #孝文帝 #尔朱荣 #高欢 #宇文泰</text>
''')

def make_card_1(bg_b64):
    items = [
        ("六镇", "沃野、怀朔、武川、抚冥、柔玄、怀荒"),
        ("昔日荣耀", "精英将士，地位尊崇，可嫁皇室"),
        ("迁都之后", "被朝廷遗忘，镇户沦为贱民"),
        ("身份崩塌", "从帝国精锐变成被贵族鄙视的武夫"),
    ]
    items_svg = ""
    for i, (title, desc) in enumerate(items):
        y = 175 + i * 145
        items_svg += f'''
<g transform="translate(40, {y})">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#EF4444"/>
  <text x="30" y="48" font-family="{FONT}" font-size="28" font-weight="700" fill="#EF4444" {STROKE}>{title}</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>{desc}</text>
</g>'''
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>六镇的由盛转衰</text>
{items_svg}
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>起事与蔓延</text>

<g transform="translate(40, 160)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>523年 · 导火索</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>怀荒镇饥荒，请开仓被拒</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>愤怒士兵杀死镇将，揭竿而起</text>
</g>

<g transform="translate(40, 350)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>燎原之势</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>破六韩拔陵率沃野镇起义</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>六镇全部响应，席卷整个北方</text>
</g>

<g transform="translate(40, 540)">
  <rect x="0" y="0" width="944" height="150" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="150" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>镇压</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>北魏向世仇柔然求援</text>
  <text x="30" y="120" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>起义被残忍镇压，但帝国已元气大伤</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#六镇之乱 #破六韩拔陵 #怀荒镇 #柔然</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>帝国的送葬曲</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>尔朱荣崛起</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>镇压义军中壮大，掌控朝政</text>
</g>

<g transform="translate(40, 320)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#CBD5E1" opacity="0.5"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#E2E8F0" {STROKE}>高欢与宇文泰</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>出身六镇的枭雄，割据东西</text>
</g>

<g transform="translate(40, 490)">
  <rect x="0" y="0" width="944" height="130" rx="16" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>北魏分裂</text>
  <text x="30" y="88" font-family="{FONT}" font-size="22" fill="#FFFFFF" {STROKE_S}>534年，分裂为东魏与西魏</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="700" fill="#EF4444" {STROKE}>一场边塞叛乱，埋葬了百年帝国</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#六镇之乱 #尔朱荣 #高欢 #宇文泰 #东魏 #西魏</text>
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
