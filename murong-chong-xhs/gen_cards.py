#!/usr/bin/env python3
"""Generate 8 beautiful cards for Murong Chong & Fu Jian using Agnes AI backgrounds."""
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
    "Epic ancient Chinese scene at dawn: a magnificent ancient city wall with an emperor in dragon robe standing on top, below a handsome young general in white armor on horseback with army, dramatic golden mist, traditional Chinese painting meets cinematic epic, red banners, emotional confrontation, Song dynasty aesthetic, masterpiece quality",
    "Ancient Chinese palace in ruins after battle, a young prince in royal robes being led away by soldiers, dramatic cloudy sky, fallen flags, traditional ink wash painting style, tragic atmosphere, Song dynasty historical scroll aesthetic, muted colors with touches of gold",
    "Inside an ancient Chinese imperial palace, a powerful emperor on throne looking at a beautiful young boy in fine robes, ambiguous tension, ornate palace interior with red pillars and golden decorations, traditional Chinese painting style, dramatic lighting through palace windows, Song dynasty court scene",
    "A handsome young general in white armor on a white horse, leading thousands of soldiers across a river at sunrise, phoenix-shaped war banner flying, dramatic golden light, misty mountains in background, traditional Chinese epic painting style, revolutionary spirit, cinematic composition",
    "Ancient Chinese city wall battle scene, thousands of soldiers assaulting a great capital city, ladders climbing walls, arrows flying, smoke and fire, dramatic orange sky, epic cinematic Chinese historical painting, Song dynasty siege scene, massive scale",
    "Dramatic close-up of two ancient Chinese figures at a city gate: an emperor on wall looking down with complex emotions, a young general on horseback looking up defiantly, a golden brocade robe hanging between them, sunset lighting, emotional tension, traditional Chinese ink wash cinematic style",
    "Ancient Chinese capital city burning at night, flames lighting up the sky, soldiers running through streets, collapsing palace buildings, dramatic orange and red fire light, dark smoke clouds, traditional Chinese painting meets epic disaster scene, tragic beauty",
    "A magnificent golden phoenix rising from flames over an ancient Chinese battlefield at dawn, traditional ink wash painting with gold leaf accents, misty mountains, fallen banners, a lone moon in pale sky, poetic and bittersweet atmosphere, masterpiece Chinese painting, metaphorical",
]

FILES = [
    "murong-cover", "murong-card-1", "murong-card-2", "murong-card-3",
    "murong-card-4", "murong-card-5", "murong-card-6", "murong-card-7",
]

CAPTIONS = [
    ("慕容冲与苻坚", "锦袍之辱 · 凤凰复仇"),
    ("前燕亡国", "12岁的慕容冲被俘入长安"),
    ("笼中凤凰", "一雌复一雄，双飞入紫宫"),
    ("河东起兵", "淝水战后，凤凰展翅"),
    ("围攻长安", "长安城下，两军对峙"),
    ("城楼对话", "岂念一袍小惠！"),
    ("长安陷落", "大火焚烧，帝国崩塌"),
    ("凤凰涅槃", "27岁，流星般的一生"),
]

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
<text x="512" y="200" text-anchor="middle" font-family="{FONT}" font-size="42" font-weight="700" fill="#FFD700" letter-spacing="8" {STROKE}>五胡十六国</text>
<text x="512" y="380" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="#FFFFFF" letter-spacing="4" {STROKE}>慕容冲</text>
<text x="512" y="450" text-anchor="middle" font-family="{FONT}" font-size="40" font-weight="400" fill="#F1F5F9" letter-spacing="2" {STROKE_S}>与</text>
<text x="512" y="540" text-anchor="middle" font-family="{FONT}" font-size="100" font-weight="900" fill="#FFD700" letter-spacing="6" {STROKE}>苻坚</text>
<rect x="312" y="575" width="400" height="3" rx="1.5" fill="#FFD700" opacity="0.7"/>
<text x="512" y="660" text-anchor="middle" font-family="{FONT}" font-size="50" font-weight="800" fill="#FFFFFF" letter-spacing="5" {STROKE}>锦袍之辱</text>
<g transform="translate(262, 740)">
  <text x="0" y="34" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>慕容冲小字凤皇</text>
  <text x="512" y="34" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#E2E8F0" {STROKE_S}>苻坚：阿房，真吾之凤凰也</text>
</g>
<text x="512" y="850" text-anchor="middle" font-family="{FONT}" font-size="22" fill="#CBD5E1" {STROKE_S}>一雌复一雄，双飞入紫宫 · 长安歌谣</text>
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#慕容冲 #苻坚 #十六国 #前秦 #历史</text>
''')

def make_card(i, bg_b64):
    title, sub = CAPTIONS[i]
    lines = {
        1: ["前秦铁骑踏破邺城", "慕容氏王族尽为阶下囚", "12岁的慕容冲被送入长安", "等待他的是不可言说的命运"],
        2: ["苻坚将慕容冲收入后宫", "长安童谣唱遍街头巷尾", "\u201c一雌复一雄，双飞入紫宫\u201d", "凤凰被困在金丝笼中"],
        3: ["淝水战后前秦大乱", "慕容冲在河东集结旧部", "凤凰终于展翅", "目标直指长安"],
        4: ["385年，慕容冲兵临长安", "苻坚登城远望", "城下英姿勃发的少年", "已不再是当年笼中鸟"],
        5: ["苻坚派人送去锦袍", "\u201c卿为朕之故旧，岂无旧情？\u201d", "慕容冲傲然答道：", "\u201c孤今心在天下，岂念一袍小惠！\u201d"],
        6: ["长安大火三日不绝", "苻坚弃城出逃", "慕容冲踏入空荡荡的宫殿", "复仇的快感转瞬即逝"],
        7: ["386年，慕容冲被部下所杀", "年仅27岁", "凤凰坠落，短暂而耀眼", "他的一生是一场复仇的火焰"],
    }

    items = ""
    for j, line in enumerate(lines.get(i, [""])):
        y = 530 + j * 60
        opacity = "1" if j < 2 else "0.8"
        fs = "34" if j < 2 else "26"
        items += f'''
<text x="512" y="{y}" text-anchor="middle" font-family="{FONT}" font-size="{fs}" fill="#FFFFFF" opacity="{opacity}" {STROKE}>{line.replace('"', '&quot;')}</text>'''

    return svg_card(bg_b64, f'''
<rect x="0" y="0" width="1024" height="200" fill="#0F172A" opacity="0.88"/>
<text x="512" y="62" text-anchor="middle" font-family="{FONT}" font-size="20" fill="#FFD700" opacity="0.9" letter-spacing="4" {STROKE_S}>第 {i} 幕</text>
<text x="512" y="128" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="800" fill="#FFD700" letter-spacing="3" {STROKE}>{title}</text>
<text x="512" y="170" text-anchor="middle" font-family="{FONT}" font-size="24" fill="#CBD5E1" {STROKE_S}>{sub}</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="{FONT}" font-size="18" fill="#94A3B8" {STROKE_S}>#慕容冲 #苻坚 #十六国 #前秦 #历史</text>
''')

if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    for i, prompt in enumerate(PROMPTS):
        name = FILES[i]
        print(f"  Generating Agnes image for {name}...")
        img_data = agnes_image(prompt)
        bg_b64 = base64.b64encode(img_data).decode()
        svg = make_cover(bg_b64) if i == 0 else make_card(i, bg_b64)
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
    print("Done! 8 beautiful cards generated.")
