#!/usr/bin/env python3
"""Generate 4 cards for 刘琨与祖逖."""
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
    "Two young ancient Chinese warriors practicing swords in a courtyard at dawn, rooster silhouetted against the sunrise, steam rising from practice, determined expressions, traditional Chinese ink wash painting, Song dynasty aesthetic, warm golden tones",
    "Ancient Chinese general at the bow of a boat in the middle of a wide river, striking his oar against the water, making a solemn vow to heaven, soldiers behind him inspired, dramatic clouds, traditional Chinese ink wash painting, Song dynasty aesthetic",
    "Lone ancient Chinese general on a desolate northern battlefield, holding a broken sword, worn armor, writing a poem with a brush, melancholy atmosphere, ruins in background, traditional Chinese ink wash painting, Song dynasty aesthetic, muted tones",
    "Two Chinese heroes standing back to back on a mountain ridge, one looking south across the river, one looking north toward lost lands, connected by a shared dream, traditional Chinese ink wash painting, Song dynasty aesthetic, bittersweet and epic",
]

FILES = ["wjqw-cover", "wjqw-card-1", "wjqw-card-2", "wjqw-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#F59E0B" letter-spacing="6" {STROKE}>晋·北伐双雄</text>
<text x="512" y="340" text-anchor="middle" font-family="{FONT}" font-size="110" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>刘琨与祖逖</text>
<rect x="312" y="385" width="400" height="3" rx="1.5" fill="#F59E0B" opacity="0.7"/>
<text x="512" y="490" text-anchor="middle" font-family="{FONT}" font-size="46" font-weight="800" fill="#F59E0B" letter-spacing="4" {STROKE}>闻鸡起舞</text>
<text x="512" y="590" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>中流击楫 · 百炼钢化绕指柔 · 壮志未酬</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#祖逖 #刘琨 #闻鸡起舞 #中流击楫 #东晋 #北伐</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#3B82F6" letter-spacing="3" {STROKE}>祖逖 · 中流击楫</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>率众南渡</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>带着一百多户族人南迁</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#3B82F6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>中流立誓</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>船到江心击桨发誓：不复中原不过江</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>壮志未酬</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>朝廷猜忌不给支援，忧愤病死</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#3B82F6" {STROKE}>收复大片失地，却抵不过朝堂猜忌</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#祖逖 #中流击楫 #东晋 #北伐</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#F59E0B" letter-spacing="3" {STROKE}>刘琨 · 百炼钢绕指柔</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>孤军留守北方</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>西晋灭亡后仍死守北方阵地</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#F59E0B"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>战败写诗</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>"何意百炼钢，化为绕指柔"</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>被盟友勒死</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>投靠鲜卑段部，反被段部杀害</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>英雄末路，诗传千古</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#刘琨 #百炼钢 #绕指柔 #东晋 #诗人</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#F59E0B" letter-spacing="3" {STROKE}>闻鸡起舞 · 千古流芳</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#F59E0B"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>闻鸡起舞</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>鸡叫就起来练剑——中国最著名的励志故事</text>
</g>

<g transform="translate(40, 310)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#F59E0B"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>中流击楫</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>渡江立誓——收复失地的精神象征</text>
</g>

<g transform="translate(40, 470)">
  <rect x="0" y="0" width="944" height="120" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="120" rx="3" fill="#F59E0B"/>
  <text x="30" y="46" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>精神遗产</text>
  <text x="30" y="84" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>千年以来，激励每一个北伐者的热血</text>
</g>

<text x="512" y="760" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#F59E0B" {STROKE}>他们失败了，但他们没有输</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#闻鸡起舞 #祖逖 #刘琨 #北伐 #爱国 #英雄</text>
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
