#!/usr/bin/env python3
"""Generate Ollama on Mac tutorial cards (1024x1024 + 1792x1024 banner)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C = "#FAF7F2"
C2 = "#F3F0E8"
W = "#FFFFFF"
T = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"
TEAL = "#0EA5E9"
TEALL = "#E0F2FE"
BLUE = "#3B82F6"
BLUEL = "#DBEAFE"
PURPLE = "#8B5CF6"
PURPLEL = "#EDE9FE"
ORANGE = "#F97316"
ORANGEL = "#FFEDD5"
GREEN = "#10B981"
GREENL = "#D1FAE5"
RED = "#EF4444"
REDL = "#FEE2E2"

def bg(w, h):
    return f'<rect width="{w}" height="{h}" fill="url(#bgG)"/><circle cx="{w*0.08}" cy="{h*0.08}" r="60" fill="{TEALL}" opacity="0.4"/><circle cx="{w*0.92}" cy="{h*0.12}" r="50" fill="{PURPLEL}" opacity="0.4"/><circle cx="{w*0.08}" cy="{h*0.88}" r="70" fill="{BLUEL}" opacity="0.3"/><circle cx="{w*0.92}" cy="{h*0.78}" r="80" fill="{ORANGEL}" opacity="0.3"/>'

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
{bg(w, h)}
{body}
</svg>'''

def card_square():
    b = f'''
<text x="512" y="120" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="40" font-weight="900" fill="{T}" letter-spacing="-1">Ollama</text>
<text x="512" y="270" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="130" font-weight="900" fill="{TEAL}" letter-spacing="-5">Mac 本地</text>
<text x="512" y="420" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="130" font-weight="900" fill="{TEAL}" letter-spacing="-5">跑大模型</text>

<g transform="translate(162, 520)">
  <rect x="0" y="0" width="700" height="70" rx="35" fill="{GREENL}" stroke="{GREEN}" stroke-width="3"/>
  <text x="350" y="45" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="32" font-weight="800" fill="{GREEN}">免费 · 离线 · 隐私安全</text>
</g>

<text x="512" y="670" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="700" fill="{T}">brew install ollama</text>
<text x="512" y="710" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" fill="{TD}">一行命令搞定 · 小白也能上手</text>

<g transform="translate(70, 780)">
  <rect x="0" y="0" width="210" height="52" rx="26" fill="{TEALL}"/><text x="105" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TEAL}">M1-M4 全系支持</text>
  <rect x="235" y="0" width="210" height="52" rx="26" fill="{BLUEL}"/><text x="340" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{BLUE}">Metal GPU 加速</text>
  <rect x="470" y="0" width="190" height="52" rx="26" fill="{PURPLEL}"/><text x="565" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{PURPLE}">REST API</text>
  <rect x="685" y="0" width="150" height="52" rx="26" fill="{ORANGEL}"/><text x="760" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{ORANGE}">100+ 模型</text>
  <rect x="860" y="0" width="100" height="52" rx="26" fill="{REDL}"/><text x="910" y="34" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{RED}">开源</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="16" fill="{TL}">ollama.com · 95K+ GitHub Stars</text>'''
    return svg_wrap(1024, 1024, b)

def card_1():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">什么是 Ollama？</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">本地大模型的「Docker」</text>

<g transform="translate(62, 180)">
  <rect x="0" y="0" width="900" height="340" rx="18" fill="{W}" stroke="{TEAL}" stroke-width="2"/>
  <text x="40" y="50" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{TEAL}">核心特点</text>

  <g transform="translate(30, 90)">
    <circle cx="16" cy="16" r="12" fill="{GREEN}"/><text x="45" y="22" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">一行命令安装部署</text>
  </g>
  <g transform="translate(30, 140)">
    <circle cx="16" cy="16" r="12" fill="{GREEN}"/><text x="45" y="22" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">Apple Metal GPU 原生加速</text>
  </g>
  <g transform="translate(30, 190)">
    <circle cx="16" cy="16" r="12" fill="{GREEN}"/><text x="45" y="22" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">100+ 开源模型随便选</text>
  </g>
  <g transform="translate(30, 240)">
    <circle cx="16" cy="16" r="12" fill="{GREEN}"/><text x="45" y="22" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">内置 REST API，随时调用</text>
  </g>
  <g transform="translate(30, 290)">
    <circle cx="16" cy="16" r="12" fill="{GREEN}"/><text x="45" y="22" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="600" fill="{T}">完全离线，数据不出本机</text>
  </g>
</g>

<g transform="translate(62, 560)">
  <rect x="0" y="0" width="900" height="200" rx="16" fill="{BLUEL}"/>
  <text x="40" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{BLUE}">适合场景</text>
  <text x="40" y="80" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{T}">· 编程助手 (CodeGemma / DeepSeek-Coder)</text>
  <text x="40" y="115" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{T}">· 文档总结 (Qwen 2.5 / Llama 3)</text>
  <text x="40" y="150" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{T}">· 本地 RAG 知识库 (ollama + Chroma)</text>
  <text x="40" y="185" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{T}">· 私有数据处理 · 敏感信息零泄露</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="14" fill="{TL}">ollama.com · GitHub 95K+ Stars · MIT 开源</text>
''')

def card_2():
    steps = [
        ("1", "安装 Ollama", "brew install ollama", TEAL, TEALL),
        ("2", "启动服务", "ollama serve", BLUE, BLUEL),
        ("3", "下载模型", "ollama pull qwen2.5:7b", PURPLE, PURPLEL),
        ("4", "运行对话", "ollama run qwen2.5:7b", GREEN, GREENL),
    ]
    items = ""
    for i, (num, title, cmd, color, light) in enumerate(steps):
        y = 170 + i * 145
        items += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="120" rx="16" fill="{W}" stroke="{color}" stroke-width="1.5"/>
  <circle cx="45" cy="60" r="26" fill="{light}" stroke="{color}" stroke-width="2"/>
  <text x="45" y="67" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" font-weight="800" fill="{color}">{num}</text>
  <text x="90" y="48" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="24" font-weight="700" fill="{T}">{title}</text>
  <text x="90" y="88" font-family="ui-monospace,monospace" font-size="20" fill="{TD}">{cmd}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">4 步搞定</text>
<text x="512" y="120" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">打开终端，复制粘贴即可</text>
{items}
<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="16" fill="{TL}">⚠️ 首次下载模型需要网络，约 4-8 GB</text>
''')

def card_3():
    models = [
        ("Mac 配置", "推荐模型", "速度参考", TEAL),
        ("M1/M2 8GB", "Qwen 2.5:1.5b / Phi-4-mini", "15-30 tok/s", TEALL),
        ("M1/M2 16GB", "Qwen 2.5:7b / Llama 3.2:8b", "25-40 tok/s", BLUEL),
        ("M1 Pro/Max 16GB", "DeepSeek-R1:14b / Qwen 2.5:14b", "15-25 tok/s", PURPLEL),
        ("M2 Ultra / M3 Max", "Qwen 2.5:32b / Llama 3.3:70b", "8-20 tok/s", ORANGEL),
    ]
    rows = ""
    for i, (col1, col2, col3, color) in enumerate(models):
        y = 150 + i * 110
        if i == 0:
            rows += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="50" rx="10" fill="{TEAL}"/>
  <text x="40" y="33" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="#fff">{col1}</text>
  <text x="310" y="33" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="#fff">{col2}</text>
  <text x="760" y="33" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="#fff">{col3}</text>
</g>'''
        else:
            rows += f'''
<g transform="translate(62, {y})">
  <rect x="0" y="0" width="900" height="60" rx="10" fill="{color}"/>
  <text x="40" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{T}">{col1}</text>
  <text x="310" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" fill="{T}">{col2}</text>
  <text x="760" y="36" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{TEAL}">{col3}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
<text x="512" y="80" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">模型推荐 · 按配置选</text>
<text x="512" y="120" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">你的 MacBook 能跑多大模型？</text>
{rows}
<g transform="translate(62, 770)">
  <rect x="0" y="0" width="900" height="80" rx="14" fill="{ORANGEL}"/>
  <text x="30" y="35" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="700" fill="{ORANGE}">💡 选购建议</text>
  <text x="30" y="65" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">16GB 内存是分水岭：以上跑 7B 以下跑 1.5B · Qwen 2.5 系列性价比最高</text>
</g>
<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="14" fill="{TL}">速度仅供参考，实际取决于内存带宽和模型量化级别</text>
''')

def card_4():
    return svg_wrap(1024, 1024, f'''
<text x="512" y="90" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="38" font-weight="800" fill="{T}">进阶玩法</text>
<text x="512" y="130" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" fill="{TD}">开发者的完整工具箱</text>

<g transform="translate(62, 180)">
  <rect x="0" y="0" width="430" height="200" rx="16" fill="{W}" stroke="{TEAL}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{TEAL}">REST API</text>
  <text x="30" y="75" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">curl http://localhost:11434</text>
  <text x="30" y="75" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">curl http://localhost:11434</text>
  <text x="30" y="105" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">  /api/generate \</text>
  <text x="30" y="135" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">  -d '{{"model":"qwen2.5:7b",</text>
  <text x="30" y="165" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">  "prompt":"Hello"}}'</text>
</g>
<g transform="translate(532, 180)">
  <rect x="0" y="0" width="430" height="200" rx="16" fill="{W}" stroke="{PURPLE}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{PURPLE}">Python SDK</text>
  <text x="30" y="75" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">import ollama</text>
  <text x="30" y="105" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">response = ollama.chat(</text>
  <text x="30" y="135" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">  model='qwen2.5:7b',</text>
  <text x="30" y="165" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">  messages=[{{'role':'user',</text>
  <text x="30" y="195" font-family="ui-monospace,monospace" font-size="16" fill="{TD}">  'content':'你好'}}])</text>
</g>

<g transform="translate(62, 420)">
  <rect x="0" y="0" width="900" height="120" rx="16" fill="{W}" stroke="{GREEN}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{GREEN}">Web UI：Open WebUI</text>
  <text x="30" y="75" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{TD}">docker run -d -p 3000:8080 ghcr.io/open-webui/open-webui:main</text>
  <text x="30" y="105" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">然后浏览器打开 http://localhost:3000 — 媲美 ChatGPT 的界面</text>
</g>

<g transform="translate(62, 580)">
  <rect x="0" y="0" width="900" height="120" rx="16" fill="{W}" stroke="{ORANGE}" stroke-width="1.5"/>
  <text x="30" y="40" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="22" font-weight="700" fill="{ORANGE}">IDE 集成</text>
  <text x="30" y="75" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="19" fill="{TD}">Continue.dev + Ollama = VS Code/Cursor 内本地 AI 编程助手</text>
  <text x="30" y="105" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">配置一行 baseUrl: http://localhost:11434 即可</text>
</g>

<g transform="translate(62, 740)">
  <rect x="0" y="0" width="900" height="70" rx="14" fill="{TEALL}"/>
  <text x="40" y="32" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="20" font-weight="600" fill="{TEAL}">⚡ 性能调优</text>
  <text x="40" y="60" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="17" fill="{TD}">export OLLAMA_NUM_PARALLEL=4  ·  OLLAMA_MAX_LOADED_MODELS=2  ·  关闭后台应用释放内存</text>
</g>

<text x="512" y="960" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="14" fill="{TL}">ollama.com · python SDK: pip install ollama</text>
''')

def card_banner():
    return svg_wrap(1792, 1024, f'''
<text x="896" y="220" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="140" font-weight="900" fill="{T}" letter-spacing="-6">Ollama</text>
<text x="896" y="400" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="160" font-weight="900" fill="{TEAL}" letter-spacing="-6">Mac 本地跑大模型</text>

<g transform="translate(446, 480)">
  <rect x="0" y="0" width="900" height="70" rx="35" fill="{GREENL}" stroke="{GREEN}" stroke-width="2"/>
  <text x="450" y="44" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="28" font-weight="800" fill="{GREEN}">brew install ollama ← 就这么简单</text>
</g>

<text x="896" y="640" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="26" fill="{TD}">Apple Metal GPU 加速 · 100+ 模型 · REST API · Open WebUI</text>

<g transform="translate(200, 730)">
  <rect x="0" y="0" width="230" height="48" rx="24" fill="{TEALL}"/><text x="115" y="31" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{TEAL}">M1-M4 全系支持</text>
  <rect x="270" y="0" width="230" height="48" rx="24" fill="{BLUEL}"/><text x="385" y="31" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{BLUE}">离线隐私</text>
  <rect x="540" y="0" width="230" height="48" rx="24" fill="{PURPLEL}"/><text x="655" y="31" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{PURPLE}">零成本</text>
  <rect x="810" y="0" width="230" height="48" rx="24" fill="{ORANGEL}"/><text x="925" y="31" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{ORANGE}">开发者友好</text>
  <rect x="1080" y="0" width="230" height="48" rx="24" fill="{GREENL}"/><text x="1195" y="31" text-anchor="middle" font-family="ui-sans-serif,-apple-system,sans-serif" font-size="18" font-weight="600" fill="{GREEN}">95K+ Stars</text>
</g>

<text x="896" y="960" text-anchor="middle" font-family="ui-monospace,monospace" font-size="18" fill="{TL}">ollama.com · GitHub · MIT 开源</text>
''')

if __name__ == "__main__":
    cards = [
        ("ollama-square", card_square()),
        ("ollama-card-1", card_1()),
        ("ollama-card-2", card_2()),
        ("ollama-card-3", card_3()),
        ("ollama-card-4", card_4()),
        ("ollama-banner", card_banner()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", str(1792 if "banner" in name else 1024), "-h", "1024"], check=True, capture_output=True)
        print(f"  ✓ {name}.png ({os.path.getsize(png_path)//1024} KB)")
    print("Done! 6 cards regenerated.")
