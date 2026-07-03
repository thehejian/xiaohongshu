from PIL import Image, ImageDraw, ImageFont
import os
BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/baoxie-road-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"
cards = {
    "01-cover": {"title": "褒斜道", "subtitle": "使用率最高的官方驿道"},
    "02-card1": {"title": "路线", "subtitle": "眉县斜谷 → 汉中褒谷，400公里"},
    "03-card2": {"title": "石门石刻", "subtitle": "东汉开凿的中国最早隧道"},
    "04-card3": {"title": "诸葛亮五丈原", "subtitle": "北伐的主战场"},
    "05-card4": {"title": "曹操鸡肋", "subtitle": "感慨于此"},
    "06-card5": {"title": "商业大动脉", "subtitle": "运盐运茶运丝绸"},
}
for name, info in cards.items():
    path = os.path.join(BASE, f"{name}.png")
    if not os.path.exists(path): continue
    img = Image.open(path).convert("RGBA")
    ol = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(ol)
    w, h = img.size
    draw.rectangle([0, 0, w, int(h*0.25)], fill=(0, 0, 0, 100))
    tf = ImageFont.truetype(FONT, int(w*0.108))
    bbox = draw.textbbox((0, 0), info["title"], font=tf)
    tx = (w - (bbox[2]-bbox[0])) // 2
    draw.text((tx, int(h*0.04)), info["title"], fill=(255, 255, 255), font=tf)
    sf = ImageFont.truetype(FONT, int(w*0.06))
    bbox = draw.textbbox((0, 0), info["subtitle"], font=sf)
    sx = (w - (bbox[2]-bbox[0])) // 2
    draw.text((sx, int(h*0.04)+int(w*0.108)+int(h*0.025)), info["subtitle"], fill=(200, 200, 200), font=sf)
    r = Image.alpha_composite(img, ol).convert("RGB")
    r.save(path, "PNG")
    print(f"{name} OK")
