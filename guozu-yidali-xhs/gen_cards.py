import subprocess, os, textwrap

OUT = "output"
os.makedirs(OUT, exist_ok=True)

CREAM = "#FAF7F2"
DEEP = "#1E293B"
RED = "#DC2626"
GREEN = "#059669"
GOLD = "#B8860B"
GRAY = "#94A3B8"

def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}",
         "-w", "1024", "-h", "1024"],
        check=True, capture_output=True,
    )

def word_wrap(text, max_chars=16):
    lines = []
    for line in text.split("\n"):
        if not line.strip():
            lines.append("")
            continue
        while len(line) > max_chars:
            idx = max_chars
            lines.append(line[:idx])
            line = line[idx:]
        lines.append(line)
    return lines

def cover_card():
    lines = [
        ("国足：", "bold", 48, DEEP),
        ("扩军也没用", "bold", 48, RED),
        ("", "", 30, DEEP),
        ("2026世界杯 48队名额", "normal", 22, GRAY),
        ("亚洲8.5席 历史最多", "normal", 22, GRAY),
        ("国足——还是没进", "bold", 28, RED),
    ]
    y = 200
    texts = ""
    for text, style, size, color in lines:
        fw = "font-weight: bold" if style == "bold" else ""
        texts += f'<text x="512" y="{y}" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="{size}" fill="{color}" {fw}>{text}</text>\n'
        y += size + 10

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <rect x="80" y="120" width="864" height="400" rx="20" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="8,4"/>
  {texts}
  <text x="512" y="680" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}">评论区告诉我想看国足什么梗</text>
  <line x1="200" y1="720" x2="824" y2="720" stroke="#E2E8F0" stroke-width="1"/>
  <text x="512" y="760" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="16" fill="{GRAY}">足球段子手 | 持续更新</text>
</svg>'''

def card_asia():
    texts = ""
    items = [
        ("日本 ✅", GREEN, "赢了西班牙德国"),
        ("韩国 ✅", GREEN, "干翻葡萄牙"),
        ("伊朗 ✅", GREEN, "跟葡萄牙五五开"),
        ("沙特 ✅", GREEN, "爆冷阿根廷"),
        ("澳大利亚 ✅", GREEN, "稳定出线"),
        ("卡塔尔 ✅", GREEN, "主场表现还行"),
        ("伊拉克 ✅", GREEN, "也进了"),
        ("印尼 ✅", GREEN, "？？？他们也进了"),
        ("国足 ❌", RED, "亚洲8.5个名额都没捞到"),
    ]
    y = 200
    for name, color, note in items:
        texts += f'<text x="150" y="{y}" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{color}">{name}</text>\n'
        texts += f'<text x="370" y="{y}" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">—— {note}</text>\n'
        y += 48
    prompt = "国足：我早说了亚洲区很强，8.5个名额都不够分"
    texts += f'<text x="512" y="{y + 30}" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}" font-style="italic">"{prompt}"</text>\n'

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <text x="512" y="100" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="30" fill="{DEEP}" font-weight="bold">亚洲区 2026 出线名单</text>
  <line x1="150" y1="120" x2="874" y2="120" stroke="#E2E8F0" stroke-width="1"/>
  {texts}
</svg>'''

def card_italy():
    texts = ""
    dialogue = [
        ("意大利", "我进了，你呢？"),
        ("国足", "我……亚洲区太卷了。"),
        ("意大利", "欧洲也卷，但我不卷了。"),
        ("国足", "你上次不是也没进？"),
        ("意大利", "上次是让你们的。"),
        ("国足", "那你这次怎么不让了？"),
        ("意大利", "再不让你们也进不去啊。"),
        ("国足", "……"),
    ]
    y = 180
    for speaker, line in dialogue:
        color = GREEN if speaker == "意大利" else RED
        lbl = f"{speaker}：" if speaker else ""
        texts += f'<text x="160" y="{y}" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{color}" font-weight="bold">{lbl}</text>\n'
        texts += f'<text x="160" y="{y + 28}" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{DEEP}">{line}</text>\n'
        y += 70

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{CREAM}"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <text x="512" y="90" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="30" fill="{DEEP}" font-weight="bold">意大利 vs 国足 对话实录</text>
  <line x1="160" y1="110" x2="864" y2="110" stroke="#E2E8F0" stroke-width="1"/>
  {texts}
  <text x="512" y="820" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="22" fill="{RED}" font-weight="bold">48个名额都救不了国足</text>
  <text x="512" y="860" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="18" fill="{GRAY}">这回真没借口了</text>
</svg>'''

def card_end():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <rect width="1024" height="1024" fill="{CREAM}"/>
  <text x="512" y="380" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="50" fill="{DEEP}" font-weight="bold">关注我</text>
  <text x="512" y="450" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="24" fill="{GRAY}">看国足还能找到什么借口</text>
  <text x="512" y="550" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="{GRAY}">点赞 ❤️ 收藏 ⭐ 转发 🔄</text>
  <rect x="362" y="600" width="300" height="50" rx="25" fill="{RED}"/>
  <text x="512" y="633" text-anchor="middle" font-family="PingFang SC, Heiti SC, sans-serif" font-size="20" fill="#FFF" font-weight="bold">下期预告：国足十大经典借口</text>
</svg>'''

if __name__ == "__main__":
    print("Generating cards...")
    for i, (name, fn) in enumerate([
        ("01-cover", cover_card),
        ("02-asia", card_asia),
        ("03-italy", card_italy),
        ("04-end", card_end),
    ]):
        svg = fn()
        save_svg(name, svg)
        print(f"  {name}.svg + {name}.png")
    print("Done! 4 cards generated in output/")