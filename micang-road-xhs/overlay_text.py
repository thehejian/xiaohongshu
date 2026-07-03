from PIL import Image, ImageDraw, ImageFont
import os
BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/micang-road-xhs"
FONT = "/System/Library/Fonts/STHeiti Medium.ttc"
cards = {
    "01-cover": {"title": "米仓道", "subtitle": "粮仓的秘密通道"},
    "02-card1": {"title": "路线", "subtitle": "汉中南郑 → 巴中，300公里"},
    "03-card2": {"title": "米仓粮道", "subtitle": "运送粮食的命脉"},
    "04-card3": {"title": "三国用兵", "subtitle": "蜀魏奇兵袭险"},
    "05-card4": {"title": "金丝猴家园", "subtitle": "米仓山自然保护区"},
    "06-card5": {"title": "巴人文化", "subtitle": "鸟纹龙纹青铜器"},
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
