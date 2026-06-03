#!/usr/bin/env python3
"""Generate XHS cards v4 — real SimpleIcons brand logos + viral design."""

import os, subprocess

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

BG       = "#FAF7F2"
INK      = "#0F172A"
INK_DIM  = "#475569"
INK_MUTE = "#94A3B8"

N8N      = "#EA580C"
N8N_BG   = "#FFF7ED"
DIFY     = "#2563EB"
DIFY_BG  = "#EFF6FF"
COZE     = "#F43F5E"
COZE_BG  = "#FFF1F2"
TITLE    = "#7C3AED"

FONT = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"


def card_shadow():
    return '''<filter id="cardShadow" x="-15%" y="-15%" width="130%" height="130%">
    <feDropShadow dx="0" dy="20" stdDeviation="28" flood-color="#000" flood-opacity="0.1"/>
  </filter>'''


def n8n_logo_svg(cx, cy, s):
    """N8N: official SimpleIcons path"""
    return f'''<g transform="translate({cx},{cy}) scale({s})"><path d="M21.4737 5.6842c-1.1772 0-2.1663.8051-2.4468 1.8947h-2.8955c-1.235 0-2.289.893-2.492 2.111l-.1038.623a1.263 1.263 0 0 1-1.246 1.0555H11.289c-.2805-1.0896-1.2696-1.8947-2.4468-1.8947s-2.1663.8051-2.4467 1.8947H4.973c-.2805-1.0896-1.2696-1.8947-2.4468-1.8947C1.1311 9.4737 0 10.6047 0 12s1.131 2.5263 2.5263 2.5263c1.1772 0 2.1663-.8051 2.4468-1.8947h1.4223c.2804 1.0896 1.2696 1.8947 2.4467 1.8947 1.1772 0 2.1663-.8051 2.4468-1.8947h1.0008a1.263 1.263 0 0 1 1.2459 1.0555l.1038.623c.203 1.218 1.257 2.111 2.492 2.111h.3692c.2804 1.0895 1.2696 1.8947 2.4468 1.8947 1.3952 0 2.5263-1.131 2.5263-2.5263s-1.131-2.5263-2.5263-2.5263c-1.1772 0-2.1664.805-2.4468 1.8947h-.3692a1.263 1.263 0 0 1-1.246-1.0555l-.1037-.623A2.52 2.52 0 0 0 13.9607 12a2.52 2.52 0 0 0 .821-1.4794l.1038-.623a1.263 1.263 0 0 1 1.2459-1.0555h2.8955c.2805 1.0896 1.2696 1.8947 2.4468 1.8947 1.3952 0 2.5263-1.131 2.5263-2.5263s-1.131-2.5263-2.5263-2.5263m0 1.2632a1.263 1.263 0 0 1 1.2631 1.2631 1.263 1.263 0 0 1-1.2631 1.2632 1.263 1.263 0 0 1-1.2632-1.2632 1.263 1.263 0 0 1 1.2632-1.2631M2.5263 10.7368A1.263 1.263 0 0 1 3.7895 12a1.263 1.263 0 0 1-1.2632 1.2632A1.263 1.263 0 0 1 1.2632 12a1.263 1.263 0 0 1 1.2631-1.2632m6.3158 0A1.263 1.263 0 0 1 10.1053 12a1.263 1.263 0 0 1-1.2632 1.2632A1.263 1.263 0 0 1 7.579 12a1.263 1.263 0 0 1 1.2632-1.2632m10.1053 3.7895a1.263 1.263 0 0 1 1.2631 1.2632 1.263 1.263 0 0 1-1.2631 1.2631 1.263 1.263 0 0 1-1.2632-1.2631 1.263 1.263 0 0 1 1.2632-1.2632" fill="{N8N}"/>'''


def dify_logo_svg(cx, cy, s):
    """Dify: official SimpleIcons path"""
    return f'''<g transform="translate({cx},{cy}) scale({s})"><path d="m22.417 9.334-1.333 4.333-1.334-4.333h-1.583L20.1 14.94c.2.583-.14 1.06-.756 1.06h-.678v1.334h.996c.869 0 1.65-.55 1.945-1.367L24 9.334ZM2.833 6.667H0v8.666h2.833c3.5 0 4.5-2 4.5-4.333s-1-4.334-4.5-4.334zM2.866 14H1.6V8h1.266c2.013 0 2.867.988 2.867 3s-.854 3-2.867 3m11-5.267v.6h-1.532v1.334h1.533V14h-2.534V9.334H8v1.334h1.867V14h-2.2v1.334h10V14h-2.332v-3.333h2.333V9.334h-2.333V8h2.333V6.667h-1.733a2.07 2.07 0 0 0-2.067 2.067Zm-3.266-.2c.681 0 .933-.417.933-.933 0-.515-.252-.933-.933-.933-.68 0-.934.418-.934.933s.253.934.934.934" fill="{DIFY}"/>'''


def coze_logo_svg(cx, cy, s):
    """Coze: official SimpleIcons path"""
    return f'''<g transform="translate({cx},{cy}) scale({s})"><path d="M9.366 12.096a.61.61 0 0 0-.608.608v1.218a.609.609 0 1 0 1.217 0v-1.218a.61.61 0 0 0-.609-.608m.8 3.453a.605.605 0 1 1 0-.86.605.605 0 0 1 .859 0 1.52 1.52 0 0 0 2.149 0 .605.605 0 0 1 .859 0 .605.605 0 0 1 0 .86 2.73 2.73 0 0 1-3.867 0m4.062-2.24a.61.61 0 1 1 .609.609.606.606 0 0 1-.61-.609zM3.023 0A3.024 3.024 0 0 0 0 3.023v17.954A3.024 3.024 0 0 0 3.023 24h17.954A3.024 3.024 0 0 0 24 20.977V3.023A3.024 3.024 0 0 0 20.977 0ZM12.1 3.78h.004a6.287 6.287 0 0 1 6.283 6.286v2.635h1.508c1.73 0 2.12 2.426.476 2.97l-1.984.663v1.137a1.513 1.513 0 0 1-2.19 1.353l-1.101-.549c-.052-.024-.115 0-.131.055-.892 2.785-4.835 2.785-5.727 0a.095.095 0 0 0-.13-.055l-1.102.55a1.513 1.513 0 0 1-2.19-1.354v-1.139l-1.984-.66c-1.647-.541-1.254-2.97.477-2.97h1.507v-2.636A6.285 6.285 0 0 1 12.1 3.78" fill="{COZE}"/>'''


def logo_badge(cx, cy, r, bg_color, logo_svg_func, s=1.6):
    return f'''<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg_color}"/>
  {logo_svg_func(cx, cy, s)}'''


def make_square():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{BG}"/>
    <stop offset="100%" stop-color="#F3F0E8"/>
  </linearGradient>
  <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="{TITLE}"/>
    <stop offset="100%" stop-color="#A78BFA"/>
  </linearGradient>
  <linearGradient id="orangeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#FB923C"/>
    <stop offset="100%" stop-color="{N8N}"/>
  </linearGradient>
  <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#60A5FA"/>
    <stop offset="100%" stop-color="{DIFY}"/>
  </linearGradient>
  <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#FB7185"/>
    <stop offset="100%" stop-color="{COZE}"/>
  </linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="14" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  {card_shadow()}
</defs>

<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<circle cx="100" cy="100" r="180" fill="{TITLE}" opacity="0.06"/>
<circle cx="{W-100}" cy="{H-100}" r="220" fill="{TITLE}" opacity="0.06"/>

<!-- Eyebrow -->
<g transform="translate(80, 50)">
  <rect x="0" y="0" width="56" height="56" rx="16" fill="{TITLE}" opacity="0.12"/>
  <text x="28" y="36" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="900" fill="{TITLE}">4</text>
  <rect x="70" y="0" width="12" height="56" rx="6" fill="{TITLE}"/>
  <text x="92" y="22" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="4" fill="{TITLE}">AI AGENT FRAMEWORK</text>
  <text x="92" y="46" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">N8N · Dify · Coze 四选一</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 140)">
  <text x="0" y="0" font-family="{FONT}" font-size="104" font-weight="900" fill="{INK}" letter-spacing="-5" filter="url(#glow)">AI Agent</text>
  <text x="0" y="115" font-family="{FONT}" font-size="104" font-weight="900" fill="url(#titleGrad)" letter-spacing="-5">框架对比</text>
</g>

<!-- Subtitle -->
<g transform="translate(80, 300)">
  <text x="0" y="0" font-family="{FONT}" font-size="28" font-weight="600" fill="{INK_DIM}">看完这张图，选对工具不踩坑 👇</text>
</g>

<!-- Three platform cards -->
<!-- N8N card -->
<g transform="translate(80, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="380" rx="28" fill="white"/>
  <rect x="0" y="0" width="270" height="14" rx="28" fill="url(#orangeGrad)"/>
  <rect x="0" y="14" width="270" height="14" rx="0" fill="url(#orangeGrad)"/>
  
  {logo_badge(135, 100, 62, N8N_BG, n8n_logo_svg, 1.8)}
  
  <circle cx="222" cy="52" r="24" fill="{N8N}"/>
  <text x="222" y="61" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="900" fill="white">1</text>
  
  <text x="135" y="192" text-anchor="middle" font-family="{FONT}" font-size="54" font-weight="900" fill="{N8N}">N8N</text>
  <text x="135" y="222" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_MUTE}">工作流自动化</text>
  
  <line x1="35" y1="252" x2="235" y2="252" stroke="#E2E8F0" stroke-width="1"/>
  
  <g transform="translate(35, 272)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{N8N}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">开源可自托管</text>
  </g>
  <g transform="translate(35, 314)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{N8N}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">500+ 集成节点</text>
  </g>
  <g transform="translate(35, 356)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{N8N}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上手难度：中等</text>
  </g>
</g>

<!-- Dify card -->
<g transform="translate(377, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="380" rx="28" fill="white"/>
  <rect x="0" y="0" width="270" height="14" rx="28" fill="url(#blueGrad)"/>
  <rect x="0" y="14" width="270" height="14" rx="0" fill="url(#blueGrad)"/>
  
  {logo_badge(135, 100, 62, DIFY_BG, dify_logo_svg, 1.8)}
  
  <circle cx="222" cy="52" r="24" fill="{DIFY}"/>
  <text x="222" y="61" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="900" fill="white">2</text>
  
  <text x="135" y="192" text-anchor="middle" font-family="{FONT}" font-size="54" font-weight="900" fill="{DIFY}">Dify</text>
  <text x="135" y="222" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_MUTE}">LLM 应用开发</text>
  
  <line x1="35" y1="252" x2="235" y2="252" stroke="#E2E8F0" stroke-width="1"/>
  
  <g transform="translate(35, 272)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{DIFY}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">开源可自部署</text>
  </g>
  <g transform="translate(35, 314)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{DIFY}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">RAG + Agent 工作流</text>
  </g>
  <g transform="translate(35, 356)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{DIFY}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上手难度：中等</text>
  </g>
</g>

<!-- Coze card -->
<g transform="translate(674, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="380" rx="28" fill="white"/>
  <rect x="0" y="0" width="270" height="14" rx="28" fill="url(#roseGrad)"/>
  <rect x="0" y="14" width="270" height="14" rx="0" fill="url(#roseGrad)"/>
  
  {logo_badge(135, 100, 62, COZE_BG, coze_logo_svg, 1.8)}
  
  <circle cx="222" cy="52" r="24" fill="{COZE}"/>
  <text x="222" y="61" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="900" fill="white">3</text>
  
  <text x="135" y="192" text-anchor="middle" font-family="{FONT}" font-size="54" font-weight="900" fill="{COZE}">扣子</text>
  <text x="135" y="222" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_MUTE}">插件生态 Bot</text>
  
  <line x1="35" y1="252" x2="235" y2="252" stroke="#E2E8F0" stroke-width="1"/>
  
  <g transform="translate(35, 272)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{COZE}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">闭源 SaaS 平台</text>
  </g>
  <g transform="translate(35, 314)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{COZE}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上百插件 + 多模态</text>
  </g>
  <g transform="translate(35, 356)">
    <rect x="0" y="0" width="8" height="30" rx="4" fill="{COZE}"/>
    <text x="18" y="22" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上手难度：低</text>
  </g>
</g>

<!-- Bottom summary bar -->
<g transform="translate(80, 810)">
  <rect x="0" y="0" width="864" height="72" rx="18" fill="{INK}" opacity="0.04"/>
  <text x="30" y="30" font-family="{FONT}" font-size="16" font-weight="800" fill="{N8N}">🟠 N8N → 自动化流程</text>
  <text x="340" y="30" font-family="{FONT}" font-size="16" font-weight="800" fill="{DIFY}">🔵 Dify → LLM 应用 + 知识库</text>
  <text x="680" y="30" font-family="{FONT}" font-size="16" font-weight="800" fill="{COZE}">🔴 扣子 → Bot + 快速上线</text>
  <text x="30" y="56" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">三者组合用也不冲突：N8N 底层 + Dify LLM 层 + 扣子前端</text>
</g>

<!-- Footer -->
<g transform="translate(80, 935)">
  <text x="0" y="0" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">#AI Agent · #N8N · #Dify · #扣子 · #Coze · #LLM · #AI工具 · #自动化</text>
</g>
</svg>'''


def make_card_n8n():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{BG}"/>
    <stop offset="100%" stop-color="#FFF7ED"/>
  </linearGradient>
  <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#FB923C"/>
    <stop offset="100%" stop-color="{N8N}"/>
  </linearGradient>
  {card_shadow()}
</defs>
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<rect x="0" y="0" width="{W}" height="14" fill="url(#accentGrad)"/>

<!-- BIG logo + title -->
<g transform="translate(80, 40)">
  {logo_badge(70, 65, 72, N8N_BG, n8n_logo_svg, 1.6)}
  <circle cx="155" cy="22" r="26" fill="{N8N}"/>
  <text x="155" y="31" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="900" fill="white">1</text>
  <text x="175" y="55" font-family="{FONT}" font-size="72" font-weight="900" fill="{N8N}" letter-spacing="-2">N8N</text>
  <text x="175" y="85" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">WORKFLOW AUTOMATION</text>
</g>

<line x1="80" y1="175" x2="944" y2="175" stroke="#E2E8F0" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 205)">
  <rect x="0" y="0" width="12" height="44" rx="6" fill="{N8N}"/>
  <text x="28" y="18" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">开源 · 自托管 · 500+ 集成</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="92" font-weight="900" fill="{INK}" letter-spacing="-3">工作流自动化</text>
  <text x="0" y="100" font-family="{FONT}" font-size="76" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">王 者</text>
</g>

<line x1="80" y1="425" x2="944" y2="425" stroke="#E2E8F0" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 455)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{N8N}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{N8N}">开源可自托管</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">代码完全开源，可部署在自己的服务器上</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 数据完全可控  ✅ 无 API 调用费用  ✅ 社区持续更新</text>
</g>

<g transform="translate(524, 455)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{N8N}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{N8N}">节点式编排</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">拖拽节点串联 API、数据库、AI 模型</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 500+ 原生集成  ✅ 可视化工作流  ✅ 支持自定义节点</text>
</g>

<g transform="translate(80, 645)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{N8N}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{N8N}">典型使用场景</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">自动化脚本 · 数据同步 · 内部工具集成 · 定时任务 · 跨平台工作流</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：有开发能力、重视数据隐私的团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 835)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="90" rx="22" fill="#FEF2F2"/>
  <rect x="0" y="0" width="12" height="90" rx="6" fill="#EF4444"/>
  <text x="30" y="42" font-family="{FONT}" font-size="20" font-weight="800" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="70" font-family="{FONT}" font-size="17" fill="#991B1B">LLM 原生能力较弱，需要自己接 OpenAI / Claude 等 API</text>
</g>

<!-- Rating -->
<g transform="translate(80, 950)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="40" font-weight="900" fill="{N8N}">中等</text>
  <text x="0" y="52" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="52" font-family="{FONT}" font-size="40" font-weight="900" fill="{N8N}">★★★★☆</text>
</g>

<g transform="translate(80, 1055)">
  <rect x="0" y="0" width="864" height="54" rx="16" fill="{N8N}" opacity="0.08"/>
  <text x="24" y="34" font-family="{FONT}" font-size="17" font-weight="800" fill="{N8N}">🎯 有开发能力 · 重视数据隐私的团队</text>
</g>

<g transform="translate(80, 1125)">
  <text x="0" y="0" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">#N8N #工作流自动化 #开源 #AI工具</text>
</g>
</svg>'''


def make_card_dify():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{BG}"/>
    <stop offset="100%" stop-color="#EFF6FF"/>
  </linearGradient>
  <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#60A5FA"/>
    <stop offset="100%" stop-color="{DIFY}"/>
  </linearGradient>
  {card_shadow()}
</defs>
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<rect x="0" y="0" width="{W}" height="14" fill="url(#accentGrad)"/>

<!-- BIG logo + title -->
<g transform="translate(80, 40)">
  {logo_badge(70, 65, 72, DIFY_BG, dify_logo_svg, 1.6)}
  <circle cx="155" cy="22" r="26" fill="{DIFY}"/>
  <text x="155" y="31" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="900" fill="white">2</text>
  <text x="175" y="55" font-family="{FONT}" font-size="72" font-weight="900" fill="{DIFY}" letter-spacing="-2">Dify</text>
  <text x="175" y="85" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">LLM APPLICATION PLATFORM</text>
</g>

<line x1="80" y1="175" x2="944" y2="175" stroke="#E2E8F0" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 205)">
  <rect x="0" y="0" width="12" height="44" rx="6" fill="{DIFY}"/>
  <text x="28" y="18" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">开源 · RAG + Agent + 模型管理</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="92" font-weight="900" fill="{INK}" letter-spacing="-3">LLM 应用</text>
  <text x="0" y="100" font-family="{FONT}" font-size="76" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">开 发 平 台</text>
</g>

<line x1="80" y1="425" x2="944" y2="425" stroke="#E2E8F0" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 455)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{DIFY}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{DIFY}">RAG 知识库</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">上传文档自动切片 · 向量检索 · 精准回答</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ PDF/Word/Markdown  ✅ 知识库管理  ✅ 混合检索</text>
</g>

<g transform="translate(524, 455)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{DIFY}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{DIFY}">Agent 工作流</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">可视化编排 Agent 推理流程</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 多模型路由  ✅ Prompt 版本管理  ✅ 工具调用</text>
</g>

<g transform="translate(80, 645)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{DIFY}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{DIFY}">典型使用场景</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">企业知识库问答 · ChatBot · 内容生成 · 数据分析助手 · 智能客服</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：想快速搭建 LLM 应用、需要知识库的企业</text>
</g>

<!-- Advantage -->
<g transform="translate(80, 835)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="90" rx="22" fill="#EFF6FF"/>
  <rect x="0" y="0" width="12" height="90" rx="6" fill="{DIFY}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="20" font-weight="800" fill="{DIFY}">💡 优势</text>
  <text x="30" y="70" font-family="{FONT}" font-size="17" fill="#1E40AF">比 N8N 更懂 LLM，比 Coze 更灵活 · 开源可自部署 · 社区活跃</text>
</g>

<!-- Rating -->
<g transform="translate(80, 950)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="40" font-weight="900" fill="{DIFY}">中等</text>
  <text x="0" y="52" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="52" font-family="{FONT}" font-size="40" font-weight="900" fill="{DIFY}">★★★★★</text>
</g>

<g transform="translate(80, 1055)">
  <rect x="0" y="0" width="864" height="54" rx="16" fill="{DIFY}" opacity="0.08"/>
  <text x="24" y="34" font-family="{FONT}" font-size="17" font-weight="800" fill="{DIFY}">🎯 想快速搭建 LLM 应用 · 需要知识库的企业</text>
</g>

<g transform="translate(80, 1125)">
  <text x="0" y="0" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">#Dify #LLM应用 #RAG #开源 #AI工具</text>
</g>
</svg>'''


def make_card_coze():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{BG}"/>
    <stop offset="100%" stop-color="#FFF1F2"/>
  </linearGradient>
  <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#FB7185"/>
    <stop offset="100%" stop-color="{COZE}"/>
  </linearGradient>
  {card_shadow()}
</defs>
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<rect x="0" y="0" width="{W}" height="14" fill="url(#accentGrad)"/>

<!-- BIG logo + title -->
<g transform="translate(80, 40)">
  {logo_badge(70, 65, 72, COZE_BG, coze_logo_svg, 1.6)}
  <circle cx="155" cy="22" r="26" fill="{COZE}"/>
  <text x="155" y="31" text-anchor="middle" font-family="{FONT}" font-size="24" font-weight="900" fill="white">3</text>
  <text x="175" y="55" font-family="{FONT}" font-size="72" font-weight="900" fill="{COZE}" letter-spacing="-2">扣子</text>
  <text x="175" y="85" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">BYTE DANCE AI BOT PLATFORM</text>
</g>

<line x1="80" y1="175" x2="944" y2="175" stroke="#E2E8F0" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 205)">
  <rect x="0" y="0" width="12" height="44" rx="6" fill="{COZE}"/>
  <text x="28" y="18" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">闭源 · 插件生态 · 多模态 · 一键发布</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="92" font-weight="900" fill="{INK}" letter-spacing="-3">字节出品</text>
  <text x="0" y="100" font-family="{FONT}" font-size="76" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">插 件 生 态</text>
</g>

<line x1="80" y1="425" x2="944" y2="425" stroke="#E2E8F0" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 455)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{COZE}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{COZE}">插件生态</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">上百个现成插件，搜索/数据库/绘图一键调用</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 无需开发  ✅ 拖拽配置  ✅ 社区贡献</text>
</g>

<g transform="translate(524, 455)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{COZE}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{COZE}">多模态能力</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">文本 + 图片 + 语音，全能型 Bot</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 图片识别  ✅ 文生图  ✅ 语音输入输出</text>
</g>

<g transform="translate(80, 645)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{COZE}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{COZE}">典型使用场景</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">客服 Bot · 内容助手 · 个人 AI 助理 · 社交媒体运营 · 智能问答</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：想快速上线 Bot、依赖插件生态的个人/小团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 835)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="90" rx="22" fill="#FEF2F2"/>
  <rect x="0" y="0" width="12" height="90" rx="6" fill="#EF4444"/>
  <text x="30" y="42" font-family="{FONT}" font-size="20" font-weight="800" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="70" font-family="{FONT}" font-size="17" fill="#991B1B">闭源 SaaS，数据在字节服务器上 · 无法自托管 · 有使用限制</text>
</g>

<!-- Rating -->
<g transform="translate(80, 950)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="40" font-weight="900" fill="{COZE}">低</text>
  <text x="0" y="52" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="52" font-family="{FONT}" font-size="40" font-weight="900" fill="{COZE}">★★★★☆</text>
</g>

<g transform="translate(80, 1055)">
  <rect x="0" y="0" width="864" height="54" rx="16" fill="{COZE}" opacity="0.08"/>
  <text x="24" y="34" font-family="{FONT}" font-size="17" font-weight="800" fill="{COZE}">🎯 想快速上线 Bot · 依赖插件生态的个人/小团队</text>
</g>

<g transform="translate(80, 1125)">
  <text x="0" y="0" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">#扣子 #Coze #字节跳动 #Bot #AI工具</text>
</g>
</svg>'''


def save_svg(name, svg):
    svg_path = os.path.join(OUT, f"{name}.svg")
    png_path = os.path.join(OUT, f"{name}.png")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    subprocess.run(
        ["inkscape", svg_path, "--export-type=png", f"--export-filename={png_path}", "-w", "1024", "-h", "1024"],
        check=True, capture_output=True,
    )
    print(f"  -> {png_path}")


if __name__ == "__main__":
    print("Generating v4 XHS cards with SimpleIcons brand logos...")
    cards = [
        ("compare-square", make_square()),
        ("compare-card-n8n", make_card_n8n()),
        ("compare-card-dify", make_card_dify()),
        ("compare-card-coze", make_card_coze()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")
