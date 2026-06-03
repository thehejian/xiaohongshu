#!/usr/bin/env python3
"""Light-style cards for 大模型API价格战 (1024x1024)."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

C  = "#FAF7F2"
C2 = "#F3F0E8"
W  = "#FFFFFF"
T  = "#1E293B"
TD = "#64748B"
TL = "#94A3B8"

DEEPSEEK  = "#4F6EF7"
DEEPSEEKS = "#DEE3FF"
QWEN      = "#FF6A00"
QWENS     = "#FFF0E0"
GPT4O     = "#10A37F"
GPT4OS    = "#E0F5EF"
CLAUDE    = "#CC4C00"
CLAUDES   = "#FFE4CC"
GEMINI    = "#4285F4"
GEMINIS   = "#E0EEFF"
GOLD      = "#D4A017"
ROSE      = "#F43F5E"

FONT = 'font-family="ui-sans-serif,-apple-system,sans-serif"'

SHADOW = '''<filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#00000010"/></filter>'''

SHADOW2 = '''<filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#00000008"/></filter>'''

GLOW = '''<filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
  <feGaussianBlur stdDeviation="12" result="blur"/>
  <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'''

def bg(w, h):
    c1 = f'<circle cx="{w*0.08}" cy="{h*0.08}" r="{min(w,h)*0.06}" fill="#E0F2FE" opacity="0.4"/>'
    c2 = f'<circle cx="{w*0.92}" cy="{h*0.12}" r="{min(w,h)*0.05}" fill="#EDE9FE" opacity="0.4"/>'
    c3 = f'<circle cx="{w*0.08}" cy="{h*0.88}" r="{min(w,h)*0.07}" fill="#FFEDD5" opacity="0.3"/>'
    c4 = f'<circle cx="{w*0.92}" cy="{h*0.78}" r="{min(w,h)*0.08}" fill="#D1FAE5" opacity="0.3"/>'
    return c1 + c2 + c3 + c4

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><linearGradient id="bgG" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="{C}"/><stop offset="100%" stop-color="{C2}"/></linearGradient></defs>
<rect width="{w}" height="{h}" fill="url(#bgG)"/>
{bg(w, h)}
{body}
</svg>'''

def logo_svg(name):
    logos = {
        "deepseek": f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{DEEPSEEK}"/><text x="26" y="35" text-anchor="middle" {FONT} font-size="15" font-weight="900" fill="#FFF">DS</text>',
        "qwen":     f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{QWEN}"/><text x="26" y="35" text-anchor="middle" {FONT} font-size="14" font-weight="900" fill="#FFF">通义</text>',
        "gpt4o":    f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{GPT4O}"/><text x="26" y="35" text-anchor="middle" {FONT} font-size="14" font-weight="900" fill="#FFF">GPT</text>',
        "claude":   f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{CLAUDE}"/><text x="26" y="35" text-anchor="middle" {FONT} font-size="14" font-weight="900" fill="#FFF">Cl</text>',
        "gemini":   f'<rect x="0" y="0" width="52" height="52" rx="12" fill="{GEMINI}"/><text x="26" y="35" text-anchor="middle" {FONT} font-size="14" font-weight="900" fill="#FFF">Ge</text>',
    }
    return logos.get(name, "")

def cover():
    items = [
        ("DeepSeek-V4", "¥0.5 / ¥2", "价格屠夫", DEEPSEEK, DEEPSEEKS, "deepseek"),
        ("Qwen-Max",    "¥2 / ¥6",   "企业首选", QWEN,     QWENS,     "qwen"),
        ("GPT-4o",      "¥18 / ¥72", "多模态王者", GPT4O,   GPT4OS,    "gpt4o"),
        ("Claude 3.5",  "¥22 / ¥108","长文天花板",CLAUDE,   CLAUDES,   "claude"),
        ("Gemini 2.0",  "¥9 / ¥36",  "谷歌生态", GEMINI,   GEMINIS,   "gemini"),
    ]
    rows = ""
    for i, (name, price, tag, color, light, lk) in enumerate(items):
        y = 480 + i * 86
        rows += f'''
<g transform="translate(80, {y})">
  <rect x="0" y="0" width="864" height="72" rx="16" fill="{W}" filter="url(#shadow2)"/>
  <g transform="translate(16, 10)">{logo_svg(lk)}</g>
  <text x="82" y="44" {FONT} font-size="22" font-weight="800" fill="{T}">{name}</text>
  <text x="420" y="44" {FONT} font-size="24" font-weight="900" fill="{color}">{price}</text>
  <rect x="620" y="16" width="120" height="40" rx="20" fill="{light}" stroke="{color}" stroke-width="1.5"/>
  <text x="680" y="43" text-anchor="middle" {FONT} font-size="16" font-weight="700" fill="{color}">{tag}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
{GLOW}
<rect x="62" y="50" width="900" height="924" rx="28" fill="{W}" filter="url(#shadow)"/>
<g transform="translate(512, 100)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="88" font-weight="900" fill="{T}">大模型</text>
  <text x="0" y="100" text-anchor="middle" {FONT} font-size="80" font-weight="900" fill="{ROSE}">API 价格战</text>
</g>
<g transform="translate(512, 240)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="26" font-weight="600" fill="{TD}">DeepSeek VS Qwen VS GPT-4o VS Claude VS Gemini</text>
  <text x="0" y="36" text-anchor="middle" {FONT} font-size="22" fill="{TL}">每百万Token价格 · 人民币计价</text>
</g>
<line x1="100" y1="310" x2="924" y2="310" stroke="#E2E8F0" stroke-width="1"/>
<g transform="translate(512, 350)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="18" font-weight="700" fill="{TL}">模型</text>
  <text x="340" y="0" text-anchor="middle" {FONT} font-size="18" font-weight="700" fill="{TL}">输入 / 输出 (¥)</text>
  <text x="680" y="0" text-anchor="middle" {FONT} font-size="18" font-weight="700" fill="{TL}">定位</text>
</g>
{rows}
<g transform="translate(512, 955)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="14" fill="{TL}">价格数据来源：各厂商官网 · 统一按每百万Token计算</text>
</g>
''')

TABLE_LOGO_KEY = {
    "DeepSeek-V4": "deepseek",
    "Qwen-Max": "qwen",
    "GPT-4o": "gpt4o",
    "Claude 3.5": "claude",
    "Gemini 2.0": "gemini",
}

def table_card():
    headers = ["模型", "输入(¥)", "输出(¥)", "上下文", "多模态", "核心优势"]
    models = [
        ("DeepSeek-V4", "0.5", "2", "128K", "✅", "价格屠夫", DEEPSEEK, DEEPSEEKS),
        ("Qwen-Max",    "2",   "6", "128K", "✅", "阿里生态", QWEN,     QWENS),
        ("GPT-4o",      "18",  "72","128K", "✅", "综合最强", GPT4O,    GPT4OS),
        ("Claude 3.5",  "22",  "108","200K","✅", "长文最优", CLAUDE,   CLAUDES),
        ("Gemini 2.0",  "9",   "36","2M",   "✅", "超长上下文",GEMINI,   GEMINIS),
    ]
    header_html = ""
    for j, h in enumerate(headers):
        xs = [60, 260, 380, 500, 620, 740]
        a = "start" if j == 0 else "middle"
        header_html += f'<text x="{xs[j]}" y="38" text-anchor="{a}" {FONT} font-size="16" font-weight="700" fill="{TL}">{h}</text>'
    
    rows = ""
    for i, (name, inp, out, ctx, multi, tag, color, light) in enumerate(models):
        y = 240 + i * 80
        bg_c = light if i % 2 == 0 else W
        lk = TABLE_LOGO_KEY.get(name, "")
        rows += f'''
<g transform="translate(60, {y})">
  <rect x="0" y="0" width="904" height="64" rx="12" fill="{bg_c}"/>
  {f'<g transform="translate(10, 6)">{logo_svg(lk)}</g>' if lk else ''}
  <text x="{70 if lk else 20}" y="40" {FONT} font-size="20" font-weight="800" fill="{T}">{name}</text>
  <text x="260" y="40" text-anchor="middle" {FONT} font-size="22" font-weight="900" fill="{color}">{inp}</text>
  <text x="380" y="40" text-anchor="middle" {FONT} font-size="22" font-weight="900" fill="{color}">{out}</text>
  <text x="500" y="40" text-anchor="middle" {FONT} font-size="18" fill="{TD}">{ctx}</text>
  <text x="620" y="40" text-anchor="middle" {FONT} font-size="18" fill="{color}">{multi}</text>
  <rect x="720" y="12" width="150" height="40" rx="20" fill="{light}" stroke="{color}" stroke-width="1.5"/>
  <text x="795" y="39" text-anchor="middle" {FONT} font-size="15" font-weight="700" fill="{color}">{tag}</text>
</g>'''
    
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
<rect x="62" y="50" width="900" height="924" rx="28" fill="{W}" filter="url(#shadow)"/>
<g transform="translate(512, 100)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="48" font-weight="900" fill="{T}">📊 价格参数全对比</text>
  <text x="0" y="36" text-anchor="middle" {FONT} font-size="18" fill="{TD}">每百万Token · 人民币计价</text>
</g>
<g transform="translate(60, 170)">
  <rect x="0" y="0" width="904" height="44" rx="12" fill="#F1F5F9"/>
  {header_html}
</g>
{rows}
<line x1="60" y1="660" x2="964" y2="660" stroke="#E2E8F0" stroke-width="1"/>
<g transform="translate(512, 710)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="24" font-weight="900" fill="{ROSE}">💡 省钱公式</text>
</g>
<g transform="translate(512, 760)">
  <rect x="-200" y="-20" width="400" height="80" rx="16" fill="{DEEPSEEKS}" stroke="{DEEPSEEK}" stroke-width="1.5"/>
  <text x="0" y="10" text-anchor="middle" {FONT} font-size="20" font-weight="800" fill="{DEEPSEEK}">DeepSeek 省 90%</text>
  <text x="0" y="40" text-anchor="middle" {FONT} font-size="15" fill="{TD}">价格仅为 GPT-4o 的 1/36</text>
</g>
<g transform="translate(512, 870)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="18" font-weight="700" fill="{TD}">推荐场景速查</text>
</g>
<g transform="translate(80, 910)">
  <rect x="0" y="0" width="200" height="46" rx="12" fill="{DEEPSEEKS}"/><text x="100" y="29" text-anchor="middle" {FONT} font-size="15" font-weight="700" fill="{DEEPSEEK}">日常 → DeepSeek</text>
  <rect x="210" y="0" width="200" height="46" rx="12" fill="{GPT4OS}"/><text x="310" y="29" text-anchor="middle" {FONT} font-size="15" font-weight="700" fill="{GPT4O}">写代码 → GPT-4o</text>
  <rect x="420" y="0" width="200" height="46" rx="12" fill="{CLAUDES}"/><text x="520" y="29" text-anchor="middle" {FONT} font-size="15" font-weight="700" fill="{CLAUDE}">长文 → Claude</text>
  <rect x="630" y="0" width="200" height="46" rx="12" fill="{QWENS}"/><text x="730" y="29" text-anchor="middle" {FONT} font-size="15" font-weight="700" fill="{QWEN}">企业 → Qwen</text>
</g>
<g transform="translate(512, 976)">
  <rect x="-200" y="-22" width="400" height="44" rx="12" fill="{GEMINIS}" stroke="{GEMINI}" stroke-width="1"/>
  <text x="0" y="10" text-anchor="middle" {FONT} font-size="15" font-weight="700" fill="{GEMINI}">超长文档 → Gemini (2M上下文)</text>
</g>
''')

def model_card(name_zh, name_en, price_in, price_out, ctx, highlight, tagline, features, weakness, color, light, logo_key, rank):
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
<rect x="62" y="50" width="900" height="924" rx="28" fill="{W}" filter="url(#shadow)"/>
<rect x="62" y="50" width="900" height="180" rx="28" fill="{color}"/>
<rect x="62" y="200" width="900" height="30" rx="0" fill="{color}"/>
<g transform="translate(100, 90)">
  <g transform="translate(0, 0)">{logo_svg(logo_key)}</g>
  <text x="72" y="36" {FONT} font-size="32" font-weight="900" fill="#FFF">{name_zh}</text>
  <text x="72" y="62" {FONT} font-size="18" fill="#FFF" opacity="0.85">{name_en}</text>
</g>
<g transform="translate(512, 90)">
  <rect x="-80" y="0" width="160" height="36" rx="18" fill="#FFF" opacity="0.25"/>
  <text x="0" y="26" text-anchor="middle" {FONT} font-size="18" font-weight="800" fill="#FFF">#{rank}</text>
</g>
<g transform="translate(100, 280)">
  <text x="0" y="0" {FONT} font-size="18" font-weight="700" fill="{TL}">输入价格</text>
  <text x="0" y="42" {FONT} font-size="48" font-weight="900" fill="{color}">¥{price_in}</text>
  <text x="0" y="70" {FONT} font-size="16" fill="{TD}">每百万Token</text>
  
  <text x="300" y="0" {FONT} font-size="18" font-weight="700" fill="{TL}">输出价格</text>
  <text x="300" y="42" {FONT} font-size="48" font-weight="900" fill="{color}">¥{price_out}</text>
  <text x="300" y="70" {FONT} font-size="16" fill="{TD}">每百万Token</text>
  
  <text x="600" y="0" {FONT} font-size="18" font-weight="700" fill="{TL}">上下文长度</text>
  <text x="600" y="42" {FONT} font-size="48" font-weight="900" fill="{color}">{ctx}</text>
  <text x="600" y="70" {FONT} font-size="16" fill="{TD}">Token</text>
</g>
<line x1="100" y1="400" x2="924" y2="400" stroke="#E2E8F0" stroke-width="1"/>
<g transform="translate(100, 440)">
  <rect x="0" y="0" width="824" height="60" rx="14" fill="{light}"/>
  <text x="30" y="38" {FONT} font-size="22" font-weight="800" fill="{color}">🏆 {highlight}</text>
</g>
<g transform="translate(100, 520)">
  <text x="0" y="0" {FONT} font-size="20" font-weight="800" fill="{T}">核心优势</text>
  {''.join(f'<text x="0" y="{32 + i*36}" {FONT} font-size="17" fill="{TD}">✅ {f}</text>' for i, f in enumerate(features))}
</g>
<g transform="translate(100, 730)">
  <rect x="0" y="0" width="824" height="90" rx="14" fill="#FEF2F2"/>
  <rect x="0" y="0" width="12" height="90" rx="6" fill="#EF4444"/>
  <text x="30" y="36" {FONT} font-size="18" font-weight="800" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="66" {FONT} font-size="17" fill="#991B1B">{weakness}</text>
</g>
<g transform="translate(100, 860)">
  <text x="0" y="0" {FONT} font-size="18" font-weight="700" fill="{TD}">{tagline}</text>
</g>
<g transform="translate(100, 920)">
  <text x="0" y="0" {FONT} font-size="15" fill="{TL}">#{name_zh} #{name_en.split()[-1] if ' ' in name_en else name_en} #大模型API #价格战</text>
</g>
''')

def card_deepseek():
    return model_card("DeepSeek-V4", "DeepSeek-V4", "0.5", "2", "128K",
        "价格屠夫 · 国产之光", "🧑‍💻 程序员首选 · 省钱天花板",
        ["中文表现极强，超越GPT-4", "开源可自部署，数据安全", "推理速度快，延迟低", "社区活跃，生态快速增长"],
        "英文能力相对弱一些，部分复杂推理不如GPT-4o",
        DEEPSEEK, DEEPSEEKS, "deepseek", "价格之王")

def card_qwen():
    return model_card("Qwen-Max", "通义千问 Max", "2", "6", "128K",
        "阿里云生态 · 企业首选", "🏢 企业部署的第一选择",
        ["阿里云全家桶无缝集成", "中文理解能力一流", "企业级稳定性保障", "有免费额度可用"],
        "多模态能力较弱，创意写作不如Claude",
        QWEN, QWENS, "qwen", "企业之选")

def card_gpt4o():
    return model_card("GPT-4o", "OpenAI GPT-4o", "18", "72", "128K",
        "综合最强 · 多模态王者", "💻 写代码/推理用这个",
        ["编程能力业界最强", "多模态全能（图/音/视）", "生态系统最完善", "插件和工具链丰富"],
        "价格最贵，国内访问需代理，存在数据隐私问题",
        GPT4O, GPT4OS, "gpt4o", "综合王者")

def card_claude():
    return model_card("Claude 3.5 Sonnet", "Anthropic Claude", "22", "108", "200K",
        "长文天花板 · 写作最优", "✍️ 写作分析的天花板",
        ["200K超长上下文", "写作/分析质量最高", "安全性最好，幻觉最低", "思维链推理透明"],
        "价格最高，API调取较慢，中文支持一般",
        CLAUDE, CLAUDES, "claude", "写作天花板")

def card_gemini():
    return model_card("Gemini 2.0 Pro", "Google Gemini 2.0", "9", "36", "2M",
        "超长上下文 · 谷歌生态", "📄 超长文档扫描神器",
        ["2M超长上下文（可处理整本书）", "谷歌生态深度整合", "性价比高（价格适中）", "多模态能力强"],
        "中文支持不如国产模型，服务稳定性一般",
        GEMINI, GEMINIS, "gemini", "长文之王")

def summary_card():
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
<rect x="62" y="50" width="900" height="924" rx="28" fill="{W}" filter="url(#shadow)"/>
<g transform="translate(512, 100)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="48" font-weight="900" fill="{T}">🎯 终极选择指南</text>
</g>
<g transform="translate(100, 180)">
  <text x="0" y="0" {FONT} font-size="20" font-weight="800" fill="{T}">按需求选模型</text>
</g>
<g transform="translate(100, 230)">
  <rect x="0" y="0" width="824" height="54" rx="14" fill="{DEEPSEEKS}"/>
  <text x="20" y="34" {FONT} font-size="18" font-weight="800" fill="{DEEPSEEK}">💰 预算有限 → DeepSeek-V4</text>
  <text x="500" y="34" {FONT} font-size="15" fill="{TD}">每日百万Token仅 ¥2</text>
</g>
<g transform="translate(100, 296)">
  <rect x="0" y="0" width="824" height="54" rx="14" fill="{GPT4OS}"/>
  <text x="20" y="34" {FONT} font-size="18" font-weight="800" fill="{GPT4O}">💻 写代码 → GPT-4o</text>
  <text x="500" y="34" {FONT} font-size="15" fill="{TD}">编程能力无可替代</text>
</g>
<g transform="translate(100, 362)">
  <rect x="0" y="0" width="824" height="54" rx="14" fill="{CLAUDES}"/>
  <text x="20" y="34" {FONT} font-size="18" font-weight="800" fill="{CLAUDE}">✍️ 写作/分析 → Claude</text>
  <text x="500" y="34" {FONT} font-size="15" fill="{TD}">200K上下文+顶级输出质量</text>
</g>
<g transform="translate(100, 428)">
  <rect x="0" y="0" width="824" height="54" rx="14" fill="{QWENS}"/>
  <text x="20" y="34" {FONT} font-size="18" font-weight="800" fill="{QWEN}">🏢 企业部署 → Qwen-Max</text>
  <text x="500" y="34" {FONT} font-size="15" fill="{TD}">阿里云生态全家桶</text>
</g>
<g transform="translate(100, 494)">
  <rect x="0" y="0" width="824" height="54" rx="14" fill="{GEMINIS}"/>
  <text x="20" y="34" {FONT} font-size="18" font-weight="800" fill="{GEMINI}">📄 超长文档 → Gemini</text>
  <text x="500" y="34" {FONT} font-size="15" fill="{TD}">2M上下文碾压全场</text>
</g>
<line x1="100" y1="580" x2="924" y2="580" stroke="#E2E8F0" stroke-width="1"/>
<g transform="translate(512, 620)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="20" font-weight="800" fill="{ROSE}">💰 每月费用估算（日均10万Token）</text>
</g>
<g transform="translate(100, 670)">
  <rect x="0" y="0" width="400" height="44" rx="12" fill="{DEEPSEEKS}"/><text x="200" y="29" text-anchor="middle" {FONT} font-size="16" font-weight="800" fill="{DEEPSEEK}">DeepSeek:  ¥6/月</text>
  <rect x="424" y="0" width="400" height="44" rx="12" fill="{QWENS}"/><text x="624" y="29" text-anchor="middle" {FONT} font-size="16" font-weight="800" fill="{QWEN}">Qwen:  ¥24/月</text>
</g>
<g transform="translate(100, 724)">
  <rect x="0" y="0" width="400" height="44" rx="12" fill="{GPT4OS}"/><text x="200" y="29" text-anchor="middle" {FONT} font-size="16" font-weight="800" fill="{GPT4O}">GPT-4o:  ¥270/月</text>
  <rect x="424" y="0" width="400" height="44" rx="12" fill="{CLAUDES}"/><text x="624" y="29" text-anchor="middle" {FONT} font-size="16" font-weight="800" fill="{CLAUDE}">Claude:  ¥390/月</text>
</g>
<g transform="translate(512, 785)">
  <rect x="-200" y="0" width="400" height="44" rx="12" fill="{GEMINIS}" stroke="{GEMINI}" stroke-width="1.5"/>
  <text x="0" y="29" text-anchor="middle" {FONT} font-size="18" font-weight="800" fill="{GEMINI}">Gemini:  ¥135/月</text>
</g>
<g transform="translate(512, 870)">
  <rect x="-200" y="0" width="400" height="44" rx="12" fill="#F1F5F9"/>
  <text x="0" y="29" text-anchor="middle" {FONT} font-size="16" font-weight="800" fill="{ROSE}">🔥 DeepSeek 仅为 GPT-4o 的 1/36</text>
</g>
<g transform="translate(512, 955)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="14" fill="{TL}">#大模型 #API价格 #DeepSeek #Qwen #GPT4o #Claude #Gemini #省钱攻略</text>
</g>
''')

if __name__ == "__main__":
    print("Generating price war cards...")
    cards = [
        ("price-war-cover", cover()),
        ("price-war-table", table_card()),
        ("price-war-deepseek", card_deepseek()),
        ("price-war-qwen", card_qwen()),
        ("price-war-gpt4o", card_gpt4o()),
        ("price-war-claude", card_claude()),
        ("price-war-gemini", card_gemini()),
        ("price-war-summary", summary_card()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", "1024", "-h", "1024"], check=True, capture_output=True)
        print(f"  -> {name}.png")
    print(f"Done! {len(cards)} cards saved.")