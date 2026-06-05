#!/usr/bin/env python3
"""Dark-style cards v5 — 中国AI六小虎现状盘点 (1024x1024). Deep bg, bold light text."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

BG  = "#0B1027"
BG2 = "#131945"
WC  = "#1A2048"
WB  = "#222A55"
T   = "#FFFFFF"
TD  = "#CBD5E1"
TL  = "#94A3B8"
M   = "#64748B"

ZHIPU    = "#60A5FA"
ZHIPUS   = "#1E3A5F"
MINIMAX  = "#A78BFA"
MINIMAXS = "#2E1A5E"
KIMI     = "#FCD34D"
KIMIS    = "#5C4A1A"
BAICHUAN = "#34D399"
BAICHUANS= "#1A3D2A"
O1AI     = "#F472B6"
O1AIS    = "#4A1A33"
STEPFUN  = "#FB923C"
STEPFUNS = "#4A2A1A"
ROSE     = "#F87171"

FONT = 'font-family="ui-sans-serif,-apple-system,sans-serif"'

SHADOW = '''<filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#00000040"/></filter>'''

SHADOW2 = '''<filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
  <feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="#00000030"/></filter>'''

def svg_wrap(w, h, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
<defs><radialGradient id="bgG" cx="50%" cy="50%" r="75%"><stop offset="0%" stop-color="{BG2}"/><stop offset="100%" stop-color="{BG}"/></radialGradient></defs>
<rect width="{w}" height="{h}" fill="url(#bgG)"/>
{body}
</svg>'''

# ─── COVER — dark, bold, glowing ───
def cover():
    companies = [
        ("智谱 AI",     "政企之王",   ZHIPU,    ZHIPUS),
        ("MiniMax",     "全球化多模态", MINIMAX,  MINIMAXS),
        ("月之暗面",    "C端超级入口", KIMI,     KIMIS),
        ("百川智能",    "医疗AI深耕", BAICHUAN, BAICHUANS),
        ("零一万物",    "出海先锋",   O1AI,     O1AIS),
        ("阶跃星辰",    "端侧领跑者", STEPFUN,  STEPFUNS),
    ]
    chips = ""
    for i, (name, tag, color, light) in enumerate(companies):
        x = 72 + (i % 3) * 298
        y = 590 + (i // 3) * 80
        chips += f'''
<g transform="translate({x}, {y})">
  <rect x="0" y="0" width="278" height="64" rx="16" fill="{WC}" stroke="{color}" stroke-width="1.5" filter="url(#shadow2)"/>
  <rect x="0" y="0" width="8" height="64" rx="4" fill="{color}"/>
  <text x="22" y="28" {FONT} font-size="24" font-weight="800" fill="{T}">{name}</text>
  <text x="22" y="52" {FONT} font-size="15" font-weight="700" fill="{color}">{tag}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
<g transform="translate(512, 85)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="96" font-weight="900" fill="{T}">中国AI</text>
  <text x="0" y="115" text-anchor="middle" {FONT} font-size="88" font-weight="900" fill="{KIMI}">六小虎</text>
  <text x="0" y="180" text-anchor="middle" {FONT} font-size="34" font-weight="800" fill="{ZHIPU}">2026 最新格局全盘点</text>
</g>
<g transform="translate(512, 350)">
  <rect x="-280" y="-24" width="560" height="130" rx="20" fill="{ZHIPUS}" stroke="{ZHIPU}" stroke-width="1" filter="url(#shadow2)"/>
  <text x="0" y="18" text-anchor="middle" {FONT} font-size="28" font-weight="800" fill="{KIMI}">🔥 2026 格局巨变</text>
  <text x="0" y="60" text-anchor="middle" {FONT} font-size="18" fill="{TD}">智谱 / MiniMax 港股上市</text>
  <text x="0" y="88" text-anchor="middle" {FONT} font-size="18" fill="{TD}">Kimi 估值破200亿美元 · 阶跃星辰冲刺IPO</text>
  <text x="0" y="116" text-anchor="middle" {FONT} font-size="18" fill="{TD}">百川押注医疗 · 零一万物加速出海</text>
</g>
{chips}
<g transform="translate(512, 975)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="14" fill="{M}">数据来源：各公司公开信息 · 市值截至2026.5</text>
</g>
''')

# ─── COMPANY CARD — dark surface, brand accents, light text ───
def company_card(name, name_en, founder, founded, val, val_label, model, tagline, color, light, features_zh, stats, bg_img_letter):
    stat_rows = ""
    for i, (k, v) in enumerate(stats.items()):
        sy = 460 + i * 56
        stat_rows += f'''
<g transform="translate(80, {sy})">
  <text x="0" y="0" {FONT} font-size="17" font-weight="700" fill="{TL}">{k}</text>
  <text x="340" y="0" {FONT} font-size="24" font-weight="900" fill="{color}" text-anchor="end">{v}</text>
</g>'''
    feat_items = ""
    for i, f in enumerate(features_zh):
        fy = 700 + i * 40
        feat_items += f'<text x="80" y="{fy}" {FONT} font-size="19" fill="{TD}">✦  {f}</text>'
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
<rect x="62" y="40" width="900" height="944" rx="28" fill="{WC}" filter="url(#shadow)"/>
<rect x="62" y="40" width="900" height="175" rx="28" fill="{light}"/>
<rect x="62" y="190" width="900" height="25" fill="{light}"/>
<rect x="62" y="40" width="12" height="175" rx="6" fill="{color}"/>

<g transform="translate(100, 72)">
  <rect x="0" y="0" width="64" height="64" rx="16" fill="{WB}"/>
  <text x="32" y="44" text-anchor="middle" {FONT} font-size="34" font-weight="900" fill="{color}">{bg_img_letter}</text>
  <text x="84" y="34" {FONT} font-size="42" font-weight="900" fill="{T}">{name}</text>
  <text x="84" y="64" {FONT} font-size="19" font-weight="600" fill="{T}" opacity="0.8">{name_en}</text>
</g>
<g transform="translate(512, 76)">
  <rect x="-155" y="0" width="310" height="40" rx="20" fill="{WB}"/>
  <text x="0" y="27" text-anchor="middle" {FONT} font-size="19" font-weight="800" fill="{color}">{founder}</text>
</g>
<g transform="translate(512, 128)">
  <rect x="-140" y="0" width="280" height="30" rx="15" fill="{WB}"/>
  <text x="0" y="21" text-anchor="middle" {FONT} font-size="14" font-weight="700" fill="{TL}">{founded}</text>
</g>

<g transform="translate(80, 258)">
  <text x="0" y="0" {FONT} font-size="16" font-weight="700" fill="{TL}">估值</text>
  <text x="0" y="58" {FONT} font-size="72" font-weight="900" fill="{color}">{val}</text>
  <text x="0" y="88" {FONT} font-size="18" font-weight="600" fill="{TL}">{val_label}</text>
</g>

<g transform="translate(80, 388)">
  <text x="0" y="0" {FONT} font-size="20" font-weight="800" fill="{T}">📊 核心指标</text>
</g>
<line x1="80" y1="415" x2="944" y2="415" stroke="{WB}" stroke-width="1"/>

{stat_rows}

<line x1="80" y1="680" x2="944" y2="680" stroke="{WB}" stroke-width="1"/>

<g transform="translate(80, 686)">
  <text x="0" y="0" {FONT} font-size="20" font-weight="800" fill="{T}">✨ 核心看点</text>
</g>
{feat_items}

<g transform="translate(512, 882)">
  <rect x="-215" y="-22" width="430" height="56" rx="28" fill="{WB}" stroke="{color}" stroke-width="2" filter="url(#shadow2)"/>
  <text x="0" y="18" text-anchor="middle" {FONT} font-size="22" font-weight="800" fill="{color}">🏷️  {tagline}</text>
</g>

<g transform="translate(512, 970)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="14" fill="{M}">#{name} #AI六小虎 #大模型 #国产AI</text>
</g>
''')

def card_zhipu():
    return company_card("智谱 AI", "Zhipu AI", "张鹏（清华系）", "2019成立 · 2026.1港股上市",
        "~4400亿", "港元（约¥3800亿）", "GLM系列", "政企之王 · AI国家队", ZHIPU, ZHIPUS, [
        "全球大模型第一股，先发优势显著",
        "12000+企业客户，8000万+终端装机",
        "深嵌信创生态，B端私有化部署",
        "2025营收¥7.24亿，政企需求强劲",
    ], {
        "模型系列": "GLM-4 / GLM-Z1",
        "企业客户": "12,000+",
        "终端装机": "8,000万+",
        "2025年营收": "¥7.24亿",
    }, "智")

def card_minimax():
    return company_card("MiniMax", "稀宇科技", "闫俊杰（前商汤）", "2021成立 · 2026.1港股上市",
        "~2500亿", "港元（约¥2200亿）", "MiniMax M3", "全球化多模态 · AGI领跑者", MINIMAX, MINIMAXS, [
        "港股上市，全球AGI第一股",
        "Talkie全球AI伴侣头部应用",
        "海外收入占比超70%",
        "全模态：文本/语音/视频/音乐",
    ], {
        "全球用户": "2.36亿+",
        "企业客户": "214,000+",
        "2025前三季收入": "$5,343万",
        "毛利率": "23.3%",
    }, "M")

def card_kimi():
    return company_card("月之暗面", "Moonshot AI · Kimi", "杨植麟（清华叉院）", "2023成立",
        "~200亿", "美元（约¥1,400亿）", "Kimi K2.6", "C端超级入口 · Agent之王", KIMI, KIMIS, [
        "K2.6模型1T参数，持平GPT-5.4",
        "ARR超2亿美元，增速行业第一",
        "累计融资376亿+人民币",
        "中国移动参投，运营商渠道加持",
    ], {
        "旗舰模型": "Kimi K2.6 (1T MoE)",
        "ARR (2026.4)": "超2亿美元",
        "累计融资": "¥376亿+",
        "最新估值": "200亿美元",
    }, "K")

def card_baichuan():
    return company_card("百川智能", "Baichuan AI", "王小川（前搜狗CEO）", "2023成立",
        "~200亿", "人民币", "Baichuan系列", "医疗AI · 最难也最值钱", BAICHUAN, BAICHUANS, [
        "全面聚焦医疗垂直赛道",
        "B端企业市场，放弃烧钱C端",
        "王小川：30亿现金储备",
        "计划2027年启动IPO",
    ], {
        "最新估值": "~200亿人民币",
        "A轮融资": "50亿（2024）",
        "现金储备": "30亿",
        "上市计划": "2027年启动",
    }, "百")

def card_o1ai():
    return company_card("零一万物", "01.AI", "李开复", "2023成立",
        "~10亿", "美元", "Yi系列", "出海先锋 · 双线作战", O1AI, O1AIS, [
        "李开复创立，明星创业团队",
        "Yi系列大模型，技术实力强",
        "东南亚/中东市场起步最早",
        "万智企业平台落标客户",
    ], {
        "最新估值": "~10亿美元",
        "2024年营收": "超1亿元",
        "核心产品": "万智企业大模型",
        "标杆客户": "中国移动等",
    }, "零")

def card_stepfun():
    return company_card("阶跃星辰", "Stepfun", "姜大昕（微软亚研院）", "2023成立（上海）",
        "~200亿", "人民币（近25亿美元融资）", "Step系列", "端侧AI · 出货量王者", STEPFUN, STEPFUNS, [
        "多模态技术：文/图/视/语音",
        "4200万+终端装机量",
        "OPPO/荣耀/中兴等品牌合作",
        "上海国资+头部VC同时押注",
    ], {
        "最新估值": "~200亿人民币",
        "C轮融资": "近25亿美元",
        "终端装机": "4,200万+",
        "日均调用": "近2,000万人次",
    }, "阶")

def summary_card():
    companies = [
        ("智谱 AI",   "政企B端",    "4400亿港元",  "港股上市",   ZHIPU,    ZHIPUS),
        ("MiniMax",   "全球化C端",  "2500亿港元",  "港股上市",   MINIMAX,  MINIMAXS),
        ("月之暗面",  "C端入口",    "200亿美元",   "Pre-IPO",   KIMI,     KIMIS),
        ("百川智能",  "医疗垂类",   "200亿人民币", "计划2027",  BAICHUAN, BAICHUANS),
        ("零一万物",  "出海+B端",   "10亿美元",    "Pre-IPO",   O1AI,     O1AIS),
        ("阶跃星辰",  "端侧多模态", "200亿人民币", "冲刺IPO",   STEPFUN,  STEPFUNS),
    ]
    rows = ""
    for i, (name, route, val, status, color, light) in enumerate(companies):
        y = 370 + i * 74
        rows += f'''
<g transform="translate(80, {y})">
  <rect x="0" y="0" width="864" height="60" rx="14" fill="{WC}" stroke="{color}" stroke-width="1" filter="url(#shadow2)"/>
  <rect x="0" y="0" width="6" height="60" rx="3" fill="{color}"/>
  <text x="22" y="38" {FONT} font-size="22" font-weight="800" fill="{T}">{name}</text>
  <rect x="150" y="14" width="100" height="34" rx="17" fill="{light}"/>
  <text x="200" y="37" text-anchor="middle" {FONT} font-size="14" font-weight="700" fill="{color}">{route}</text>
  <text x="340" y="38" {FONT} font-size="22" font-weight="900" fill="{color}">{val}</text>
  <rect x="650" y="14" width="180" height="34" rx="17" fill="{light}"/>
  <text x="740" y="37" text-anchor="middle" {FONT} font-size="15" font-weight="700" fill="{T}">{status}</text>
</g>'''
    return svg_wrap(1024, 1024, f'''
{SHADOW}
{SHADOW2}
<rect x="62" y="40" width="900" height="944" rx="28" fill="{WC}" filter="url(#shadow)"/>
<g transform="translate(512, 85)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="52" font-weight="900" fill="{T}">📊 六小虎全景对比</text>
  <text x="0" y="50" text-anchor="middle" {FONT} font-size="22" font-weight="700" fill="{ZHIPU}">一图看懂六家公司格局 · 2026年5月</text>
</g>

<g transform="translate(80, 175)">
  <rect x="0" y="0" width="864" height="135" rx="20" fill="{ZHIPUS}" stroke="{ZHIPU}" stroke-width="1" filter="url(#shadow2)"/>
  <text x="30" y="36" {FONT} font-size="22" font-weight="800" fill="{KIMI}">🔥 关键趋势</text>
  <text x="30" y="74" {FONT} font-size="18" fill="{TD}">• 智谱 / MiniMax 已上市，估值分化明显</text>
  <text x="30" y="102" {FONT} font-size="18" fill="{TD}">• 月之暗面 / 阶跃星辰 / 零一万物 冲刺IPO中</text>
  <text x="30" y="130" {FONT} font-size="18" fill="{TD}">• 百川差异化走医疗赛道，长期价值待验证</text>
</g>

<g transform="translate(80, 340)">
  <rect x="0" y="0" width="864" height="36" rx="12" fill="{WB}"/>
  <text x="24" y="25" {FONT} font-size="16" font-weight="700" fill="{TL}">公司</text>
  <text x="158" y="25" {FONT} font-size="16" font-weight="700" fill="{TL}">路线</text>
  <text x="340" y="25" {FONT} font-size="16" font-weight="700" fill="{TL}">估值/市值</text>
  <text x="750" y="25" {FONT} font-size="16" font-weight="700" fill="{TL}">上市状态</text>
</g>

{rows}

<g transform="translate(512, 970)">
  <text x="0" y="0" text-anchor="middle" {FONT} font-size="14" fill="{M}">数据来源：公开财报/融资信息 · 市值截至2026.5.13</text>
</g>
''')

if __name__ == "__main__":
    print("Generating AI Six Tigers cards v5 (dark)...")
    cards = [
        ("cover",      cover()),
        ("zhipu",      card_zhipu()),
        ("minimax",    card_minimax()),
        ("kimi",       card_kimi()),
        ("baichuan",   card_baichuan()),
        ("01ai",       card_o1ai()),
        ("stepfun",    card_stepfun()),
        ("summary",    summary_card()),
    ]
    for name, svg in cards:
        svg_path = os.path.join(ROOT, f"{name}.svg")
        png_path = os.path.join(ROOT, f"{name}.png")
        with open(svg_path, "w") as f:
            f.write(svg)
        subprocess.run(["inkscape", svg_path, "-o", png_path, "-w", "1024", "-h", "1024"], check=True, capture_output=True)
        print(f"  -> {name}.png")
    print(f"Done! {len(cards)} cards saved.")
