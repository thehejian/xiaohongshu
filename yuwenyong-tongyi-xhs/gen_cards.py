#!/usr/bin/env python3
"""Generate 4 cards for 宇文邕."""
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
    "Ancient Chinese emperor in magnificent dragon robes standing on a mountain peak, one hand reaching toward a unified land below, dramatic clouds and golden sunset, epic and bittersweet, traditional Chinese ink wash painting, Song dynasty aesthetic, imperial gold and blue",
    "Ancient Chinese palace scene, a young prince pretending to be simple-minded, laughing foolishly while a sinister regent watches, hidden intelligence in his eyes, tense atmosphere, traditional Chinese ink wash painting, Song dynasty aesthetic",
    "Ancient Chinese battlefield, imperial army advancing under golden banners, northern capital city falling, conquest and victory, traditional Chinese ink wash painting, Song dynasty aesthetic, dynamic composition",
    "Ancient Chinese emperor on horseback suddenly collapsing from illness during a northern campaign, his army stopping in concern, tragic moment, cloudy sky, traditional Chinese ink wash painting, Song dynasty aesthetic, melancholic atmosphere",
]

FILES = ["yuwenyong-cover", "yuwenyong-card-1", "yuwenyong-card-2", "yuwenyong-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#FFD700" letter-spacing="6" {STROKE}>南北朝·北周武帝</text>
<text x="512" y="360" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="8" {STROKE}>宇文邕</text>
<rect x="312" y="405" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="510" text-anchor="middle" font-family="{FONT}" font-size="46" font-weight="800" fill="#FFD700" letter-spacing="4" {STROKE}>大一统一步之遥</text>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>装傻12年 · 灭北齐 · 灭佛强国 · 36岁骤逝</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇文邕 #北周武帝 #灭北齐 #大一统 #南北朝</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>装傻12年，一击必杀</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>宇文护立他为帝</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>以为他也是个听话的傀儡</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>装傻充愣</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>宇文护说什么都拍手说好，绝不反抗</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>一笏板毙命</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>572年探母，趁其不备当场击杀</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>装最傻的傻，杀最狠的人</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇文邕 #宇文护 #隐忍 #北周</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>灭北齐 · 灭佛 · 强国</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>灭北齐（577年）</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>御驾亲征，数月吞掉北齐全境</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>灭佛</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>还俗僧尼、充公庙产、增加兵源税源</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#FFD700"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>国力暴涨</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>北周一跃成为当时最强政权</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#FFD700" {STROKE}>统一北方的唯一雄主</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇文邕 #灭北齐 #灭佛 #北周 #南北朝</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>历史的遗憾</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>北伐突厥</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>578年御驾亲征，大军行至半途</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>突发疾病</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>突然病倒，年仅36岁驾崩</text>
</g>

<g transform="translate(40, 470)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#EF4444"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>杨坚捡漏</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>3年后杨坚篡周，9年后隋灭南陈</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>如果多活十年，就没有隋朝</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#宇文邕 #大一统 #英年早逝 #历史</text>
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
