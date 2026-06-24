#!/usr/bin/env python3
"""Generate 4 cards for 王与马共天下."""
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
    "Ancient Chinese emperor and his chief minister sitting side by side in the imperial hall, two thrones of equal height, elegant and refined atmosphere, southern Chinese palace with lush gardens visible, traditional Chinese ink wash painting, Song dynasty aesthetic, jade green and gold palette",
    "Ancient Chinese scene of noble scholars arriving in the southern capital, a grand procession of northern elite crossing the Yangtze River, establishing a new court, misty landscape with willows, traditional Chinese ink wash painting, Song dynasty aesthetic, serene blue-green tones",
    "Ancient Chinese palace scene, emperor confronting a rebellious general, tension between civil and military branches of the same powerful family, dramatic confrontation, traditional Chinese ink wash painting, Song dynasty aesthetic, warm and intense colors",
    "Ancient Chinese aristocratic garden scene, a gathering of noble families in elegant robes deliberating over state affairs, scholars and officials discussing beneath bamboo groves, refined and sophisticated, traditional Chinese ink wash painting, Song dynasty aesthetic",
]

FILES = ["wangyuema-cover", "wangyuema-card-1", "wangyuema-card-2", "wangyuema-card-3"]

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
<text x="512" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="700" fill="#059669" letter-spacing="6" {STROKE}>东晋·门阀政治</text>
<text x="512" y="340" text-anchor="middle" font-family="{FONT}" font-size="120" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>王与马</text>
<text x="512" y="460" text-anchor="middle" font-family="{FONT}" font-size="120" font-weight="900" fill="#FFFFFF" letter-spacing="6" {STROKE}>共天下</text>
<rect x="362" y="500" width="300" height="3" rx="1.5" fill="#059669" opacity="0.7"/>
<text x="512" y="610" text-anchor="middle" font-family="{FONT}" font-size="26" fill="#E2E8F0" {STROKE_S}>琅琊王氏与司马皇族共享江山</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#王与马共天下 #王导 #东晋 #门阀 #琅琊王氏</text>
''')

def make_card_1(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#059669" letter-spacing="3" {STROKE}>王导立国</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#059669"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>司马睿南渡</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>西晋灭亡，北方司马皇族逃到建康</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#059669"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>江南不理他</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>江南士族：一个北方王爷凭什么当皇帝？</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#059669"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>王导出手</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>率北方名流当众跪拜，江南士族只得臣服</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#059669" {STROKE}>没有王导，就没有东晋</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#王导 #东晋 #司马睿 #衣冠南渡</text>
''')

def make_card_2(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#EF4444" letter-spacing="3" {STROKE}>王氏的内讧</text>

<g transform="translate(40, 155)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>王敦掌兵</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>王导堂兄王敦手握大军，看不惯皇帝</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>起兵造反</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>带兵攻打建康，要推翻司马睿</text>
</g>

<g transform="translate(40, 445)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#EF4444"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>王导的骚操作</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>一边抵抗，一边暗中给堂兄递情报</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#EF4444" {STROKE}>一个家族，分坐朝廷两边</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#王敦 #王导 #东晋 #门阀 #琅琊王氏</text>
''')

def make_card_3(bg_b64):
    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="110" fill="#0F172A" opacity="0.88"/>
<text x="512" y="72" text-anchor="middle" font-family="{FONT}" font-size="38" font-weight="800" fill="#8B5CF6" letter-spacing="3" {STROKE}>士族政治的顶峰</text>

<g transform="translate(40, 150)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#8B5CF6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#8B5CF6" {STROKE}>皇帝=CEO，士族=董事会</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>皇权被门阀架空，历史上罕见</text>
</g>

<g transform="translate(40, 300)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#8B5CF6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#8B5CF6" {STROKE}>持续百年</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>从东晋建立到刘裕篡位，整整100年</text>
</g>

<g transform="translate(40, 450)">
  <rect x="0" y="0" width="944" height="110" rx="14" fill="#0F172A" opacity="0.82"/>
  <rect x="0" y="0" width="6" height="110" rx="3" fill="#8B5CF6"/>
  <text x="30" y="44" font-family="{FONT}" font-size="26" font-weight="700" fill="#8B5CF6" {STROKE}>终结</text>
  <text x="30" y="80" font-family="{FONT}" font-size="22" fill="#E2E8F0" {STROKE_S}>刘裕建宋，皇权重新压倒门阀</text>
</g>

<text x="512" y="720" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="700" fill="#8B5CF6" {STROKE}>中国版的"虚君共治"</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#门阀政治 #东晋 #士族 #刘宋 #南北朝</text>
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
