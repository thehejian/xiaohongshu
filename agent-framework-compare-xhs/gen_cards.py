#!/usr/bin/env python3
"""Generate XHS cards for AI Agent framework comparison — v3 with accurate brand logos + viral design."""

import os, subprocess

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
BG       = "#FAF7F2"
INK      = "#0F172A"
INK_DIM  = "#475569"
INK_MUTE = "#94A3B8"

# Brand colors — accurate to real brands
N8N      = "#EA580C"   # N8N orange
N8N_BG   = "#FFF7ED"
DIFY     = "#2563EB"   # Dify blue
DIFY_BG  = "#EFF6FF"
COZE     = "#F43F5E"   # Coze rose/red
COZE_BG  = "#FFF1F2"
TITLE    = "#7C3AED"   # purple for title

FONT = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"


def card_shadow():
    return '''<filter id="cardShadow" x="-15%" y="-15%" width="130%" height="130%">
    <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000" flood-opacity="0.12"/>
  </filter>'''


def n8n_logo(cx, cy, scale):
    """N8N logo: accurate chain link / infinity shape — two interlocking rounded rectangles"""
    s = scale
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <!-- N8N chain link: two interlocking ovals -->
    <ellipse cx="-14" cy="0" rx="16" ry="20" fill="none" stroke="{N8N}" stroke-width="5" stroke-linecap="round"/>
    <ellipse cx="14" cy="0" rx="16" ry="20" fill="none" stroke="{N8N}" stroke-width="5" stroke-linecap="round"/>
    <!-- Overlap fill -->
    <path d="M -6 -16 A 8 16 0 0 1 -6 16 L 6 16 A 8 16 0 0 1 6 -16 Z" fill="{N8N}" opacity="0.15"/>
  </g>'''


def dify_logo(cx, cy, scale):
    """Dify logo: accurate wave symbol — three connected arcs with dots"""
    s = scale
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <!-- Dify wave: three connected curves -->
    <path d="M -20 -3 C -20 -12, -5 -12, -5 -3 C -5 6, 5 6, 5 -3 C 5 -12, 20 -12, 20 -3"
          fill="none" stroke="{DIFY}" stroke-width="6" stroke-linecap="round"/>
    <!-- Three dots at key points -->
    <circle cx="-5" cy="-3" r="4" fill="{DIFY}"/>
    <circle cx="5" cy="-3" r="4" fill="{DIFY}"/>
    <circle cx="20" cy="-3" r="4" fill="{DIFY}"/>
  </g>'''


def coze_logo(cx, cy, scale):
    """Coze logo: accurate speech bubble with three dots"""
    s = scale
    return f'''<g transform="translate({cx},{cy}) scale({s})">
    <!-- Coze speech bubble -->
    <rect x="-22" y="-18" width="44" height="32" rx="8" fill="{COZE}"/>
    <!-- Tail pointing down-left -->
    <polygon points="-10,10 -22,22 -6,14" fill="{COZE}"/>
    <!-- Three white dots -->
    <circle cx="-8" cy="-4" r="3" fill="white"/>
    <circle cx="2" cy="-4" r="3" fill="white"/>
    <circle cx="12" cy="-4" r="3" fill="white"/>
  </g>'''


def logo_circle(cx, cy, r, bg_color, logo_func, s=2.5):
    """Colored circle badge with logo inside"""
    return f'''<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg_color}"/>
  {logo_func(cx, cy, s)}'''


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
    <feGaussianBlur stdDeviation="12" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="shadow" x="-10%" y="-10%" width="125%" height="125%">
    <feDropShadow dx="0" dy="8" stdDeviation="16" flood-color="#000" flood-opacity="0.1"/>
  </filter>
  {card_shadow()}
</defs>

<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<!-- Decorative background circles -->
<circle cx="100" cy="100" r="160" fill="{TITLE}" opacity="0.05"/>
<circle cx="{W-100}" cy="{H-100}" r="200" fill="{TITLE}" opacity="0.05"/>
<circle cx="{W-200}" cy="200" r="100" fill="{N8N}" opacity="0.03"/>
<circle cx="200" cy="{H-200}" r="120" fill="{DIFY}" opacity="0.03"/>

<!-- Eyebrow with number badge -->
<g transform="translate(80, 50)">
  <rect x="0" y="0" width="52" height="52" rx="14" fill="{TITLE}" opacity="0.12"/>
  <text x="26" y="34" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="900" fill="{TITLE}">4</text>
  <rect x="64" y="0" width="10" height="52" rx="5" fill="{TITLE}"/>
  <text x="86" y="20" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="4" fill="{TITLE}">AI AGENT FRAMEWORK</text>
  <text x="86" y="44" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">N8N · Dify · Coze 四选一</text>
</g>

<!-- Hero title — HUGE with glow -->
<g transform="translate(80, 140)">
  <text x="0" y="0" font-family="{FONT}" font-size="100" font-weight="900" fill="{INK}" letter-spacing="-5" filter="url(#glow)">AI Agent</text>
  <text x="0" y="110" font-family="{FONT}" font-size="100" font-weight="900" fill="url(#titleGrad)" letter-spacing="-5">框架对比</text>
</g>

<!-- Subtitle -->
<g transform="translate(80, 295)">
  <text x="0" y="0" font-family="{FONT}" font-size="28" font-weight="600" fill="{INK_DIM}">看完这张图，选对工具不踩坑 👇</text>
</g>

<!-- Three platform cards with BIG logos — horizontal row -->
<!-- N8N card -->
<g transform="translate(80, 370)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="380" rx="28" fill="white"/>
  <!-- Gradient top bar -->
  <rect x="0" y="0" width="270" height="12" rx="28" fill="url(#orangeGrad)"/>
  <rect x="0" y="12" width="270" height="12" rx="0" fill="url(#orangeGrad)"/>
  
  <!-- BIG logo badge -->
  {logo_circle(135, 105, 60, N8N_BG, n8n_logo)}
  
  <!-- Number badge -->
  <circle cx="220" cy="55" r="22" fill="{N8N}"/>
  <text x="220" y="63" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="900" fill="white">1</text>
  
  <!-- Platform name — BIG -->
  <text x="135" y="195" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="900" fill="{N8N}">N8N</text>
  <text x="135" y="225" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_MUTE}">工作流自动化</text>
  
  <line x1="35" y1="255" x2="235" y2="255" stroke="#E2E8F0" stroke-width="1"/>
  
  <!-- Features -->
  <g transform="translate(35, 275)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{N8N}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">开源可自托管</text>
  </g>
  <g transform="translate(35, 315)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{N8N}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">500+ 集成节点</text>
  </g>
  <g transform="translate(35, 355)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{N8N}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上手难度：中等</text>
  </g>
</g>

<!-- Dify card -->
<g transform="translate(377, 370)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="380" rx="28" fill="white"/>
  <rect x="0" y="0" width="270" height="12" rx="28" fill="url(#blueGrad)"/>
  <rect x="0" y="12" width="270" height="12" rx="0" fill="url(#blueGrad)"/>
  
  {logo_circle(135, 105, 60, DIFY_BG, dify_logo)}
  
  <circle cx="220" cy="55" r="22" fill="{DIFY}"/>
  <text x="220" y="63" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="900" fill="white">2</text>
  
  <text x="135" y="195" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="900" fill="{DIFY}">Dify</text>
  <text x="135" y="225" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_MUTE}">LLM 应用开发</text>
  
  <line x1="35" y1="255" x2="235" y2="255" stroke="#E2E8F0" stroke-width="1"/>
  
  <g transform="translate(35, 275)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{DIFY}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">开源可自部署</text>
  </g>
  <g transform="translate(35, 315)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{DIFY}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">RAG + Agent 工作流</text>
  </g>
  <g transform="translate(35, 355)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{DIFY}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上手难度：中等</text>
  </g>
</g>

<!-- Coze card -->
<g transform="translate(674, 370)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="380" rx="28" fill="white"/>
  <rect x="0" y="0" width="270" height="12" rx="28" fill="url(#roseGrad)"/>
  <rect x="0" y="12" width="270" height="12" rx="0" fill="url(#roseGrad)"/>
  
  {logo_circle(135, 105, 60, COZE_BG, coze_logo)}
  
  <circle cx="220" cy="55" r="22" fill="{COZE}"/>
  <text x="220" y="63" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="900" fill="white">3</text>
  
  <text x="135" y="195" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="900" fill="{COZE}">扣子</text>
  <text x="135" y="225" text-anchor="middle" font-family="{FONT}" font-size="18" fill="{INK_MUTE}">插件生态 Bot</text>
  
  <line x1="35" y1="255" x2="235" y2="255" stroke="#E2E8F0" stroke-width="1"/>
  
  <g transform="translate(35, 275)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{COZE}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">闭源 SaaS 平台</text>
  </g>
  <g transform="translate(35, 315)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{COZE}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上百插件 + 多模态</text>
  </g>
  <g transform="translate(35, 355)">
    <rect x="0" y="0" width="8" height="28" rx="4" fill="{COZE}"/>
    <text x="18" y="21" font-family="{FONT}" font-size="16" font-weight="700" fill="{INK}">上手难度：低</text>
  </g>
</g>

<!-- Bottom summary bar -->
<g transform="translate(80, 800)">
  <rect x="0" y="0" width="864" height="72" rx="18" fill="{INK}" opacity="0.04"/>
  <text x="30" y="30" font-family="{FONT}" font-size="16" font-weight="800" fill="{N8N}">🟠 N8N → 自动化流程</text>
  <text x="340" y="30" font-family="{FONT}" font-size="16" font-weight="800" fill="{DIFY}">🔵 Dify → LLM 应用 + 知识库</text>
  <text x="680" y="30" font-family="{FONT}" font-size="16" font-weight="800" fill="{COZE}">🔴 扣子 → Bot + 快速上线</text>
  <text x="30" y="56" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">三者组合用也不冲突：N8N 底层 + Dify LLM 层 + 扣子前端</text>
</g>

<!-- Footer -->
<g transform="translate(80, 925)">
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

<!-- BIG logo + title at top -->
<g transform="translate(80, 40)">
  {logo_circle(70, 65, 70, N8N_BG, n8n_logo)}
  <!-- Number badge -->
  <circle cx="145" cy="25" r="24" fill="{N8N}"/>
  <text x="145" y="34" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="900" fill="white">1</text>
  <text x="165" y="55" font-family="{FONT}" font-size="68" font-weight="900" fill="{N8N}" letter-spacing="-2">N8N</text>
  <text x="165" y="85" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">WORKFLOW AUTOMATION</text>
</g>

<line x1="80" y1="175" x2="944" y2="175" stroke="#E2E8F0" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 205)">
  <rect x="0" y="0" width="12" height="44" rx="6" fill="{N8N}"/>
  <text x="28" y="18" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">开源 · 自托管 · 500+ 集成</text>
</g>

<!-- Hero title — HUGE -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="88" font-weight="900" fill="{INK}" letter-spacing="-3">工作流自动化</text>
  <text x="0" y="95" font-family="{FONT}" font-size="72" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">王 者</text>
</g>

<line x1="80" y1="415" x2="944" y2="415" stroke="#E2E8F0" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 445)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{N8N}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{N8N}">开源可自托管</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">代码完全开源，可部署在自己的服务器上</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 数据完全可控  ✅ 无 API 调用费用  ✅ 社区持续更新</text>
</g>

<g transform="translate(524, 445)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{N8N}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{N8N}">节点式编排</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">拖拽节点串联 API、数据库、AI 模型</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 500+ 原生集成  ✅ 可视化工作流  ✅ 支持自定义节点</text>
</g>

<g transform="translate(80, 635)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{N8N}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{N8N}">典型使用场景</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">自动化脚本 · 数据同步 · 内部工具集成 · 定时任务 · 跨平台工作流</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：有开发能力、重视数据隐私的团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 825)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="90" rx="22" fill="#FEF2F2"/>
  <rect x="0" y="0" width="12" height="90" rx="6" fill="#EF4444"/>
  <text x="30" y="42" font-family="{FONT}" font-size="20" font-weight="800" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="70" font-family="{FONT}" font-size="17" fill="#991B1B">LLM 原生能力较弱，需要自己接 OpenAI / Claude 等 API</text>
</g>

<!-- Rating -->
<g transform="translate(80, 940)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="38" font-weight="900" fill="{N8N}">中等</text>
  <text x="0" y="52" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="52" font-family="{FONT}" font-size="38" font-weight="900" fill="{N8N}">★★★★☆</text>
</g>

<g transform="translate(80, 1045)">
  <rect x="0" y="0" width="864" height="54" rx="16" fill="{N8N}" opacity="0.08"/>
  <text x="24" y="34" font-family="{FONT}" font-size="17" font-weight="800" fill="{N8N}">🎯 有开发能力 · 重视数据隐私的团队</text>
</g>

<g transform="translate(80, 1115)">
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
  {logo_circle(70, 65, 70, DIFY_BG, dify_logo)}
  <circle cx="145" cy="25" r="24" fill="{DIFY}"/>
  <text x="145" y="34" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="900" fill="white">2</text>
  <text x="165" y="55" font-family="{FONT}" font-size="68" font-weight="900" fill="{DIFY}" letter-spacing="-2">Dify</text>
  <text x="165" y="85" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">LLM APPLICATION PLATFORM</text>
</g>

<line x1="80" y1="175" x2="944" y2="175" stroke="#E2E8F0" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 205)">
  <rect x="0" y="0" width="12" height="44" rx="6" fill="{DIFY}"/>
  <text x="28" y="18" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">开源 · RAG + Agent + 模型管理</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="88" font-weight="900" fill="{INK}" letter-spacing="-3">LLM 应用</text>
  <text x="0" y="95" font-family="{FONT}" font-size="72" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">开 发 平 台</text>
</g>

<line x1="80" y1="415" x2="944" y2="415" stroke="#E2E8F0" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 445)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{DIFY}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{DIFY}">RAG 知识库</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">上传文档自动切片 · 向量检索 · 精准回答</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ PDF/Word/Markdown  ✅ 知识库管理  ✅ 混合检索</text>
</g>

<g transform="translate(524, 445)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{DIFY}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{DIFY}">Agent 工作流</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">可视化编排 Agent 推理流程</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 多模型路由  ✅ Prompt 版本管理  ✅ 工具调用</text>
</g>

<g transform="translate(80, 635)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{DIFY}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{DIFY}">典型使用场景</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">企业知识库问答 · ChatBot · 内容生成 · 数据分析助手 · 智能客服</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：想快速搭建 LLM 应用、需要知识库的企业</text>
</g>

<!-- Advantage -->
<g transform="translate(80, 825)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="90" rx="22" fill="#EFF6FF"/>
  <rect x="0" y="0" width="12" height="90" rx="6" fill="{DIFY}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="20" font-weight="800" fill="{DIFY}">💡 优势</text>
  <text x="30" y="70" font-family="{FONT}" font-size="17" fill="#1E40AF">比 N8N 更懂 LLM，比 Coze 更灵活 · 开源可自部署 · 社区活跃</text>
</g>

<!-- Rating -->
<g transform="translate(80, 940)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="38" font-weight="900" fill="{DIFY}">中等</text>
  <text x="0" y="52" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="52" font-family="{FONT}" font-size="38" font-weight="900" fill="{DIFY}">★★★★★</text>
</g>

<g transform="translate(80, 1045)">
  <rect x="0" y="0" width="864" height="54" rx="16" fill="{DIFY}" opacity="0.08"/>
  <text x="24" y="34" font-family="{FONT}" font-size="17" font-weight="800" fill="{DIFY}">🎯 想快速搭建 LLM 应用 · 需要知识库的企业</text>
</g>

<g transform="translate(80, 1115)">
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
  {logo_circle(70, 65, 70, COZE_BG, coze_logo)}
  <circle cx="145" cy="25" r="24" fill="{COZE}"/>
  <text x="145" y="34" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="900" fill="white">3</text>
  <text x="165" y="55" font-family="{FONT}" font-size="68" font-weight="900" fill="{COZE}" letter-spacing="-2">扣子</text>
  <text x="165" y="85" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">BYTE DANCE AI BOT PLATFORM</text>
</g>

<line x1="80" y1="175" x2="944" y2="175" stroke="#E2E8F0" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 205)">
  <rect x="0" y="0" width="12" height="44" rx="6" fill="{COZE}"/>
  <text x="28" y="18" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">闭源 · 插件生态 · 多模态 · 一键发布</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="88" font-weight="900" fill="{INK}" letter-spacing="-3">字节出品</text>
  <text x="0" y="95" font-family="{FONT}" font-size="72" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">插 件 生 态</text>
</g>

<line x1="80" y1="415" x2="944" y2="415" stroke="#E2E8F0" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 445)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{COZE}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{COZE}">插件生态</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">上百个现成插件，搜索/数据库/绘图一键调用</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 无需开发  ✅ 拖拽配置  ✅ 社区贡献</text>
</g>

<g transform="translate(524, 445)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{COZE}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{COZE}">多模态能力</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">文本 + 图片 + 语音，全能型 Bot</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 图片识别  ✅ 文生图  ✅ 语音输入输出</text>
</g>

<g transform="translate(80, 635)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="160" rx="22" fill="white"/>
  <rect x="0" y="0" width="12" height="160" rx="6" fill="{COZE}"/>
  <text x="30" y="58" font-family="{FONT}" font-size="32" font-weight="800" fill="{COZE}">典型使用场景</text>
  <text x="30" y="92" font-family="{FONT}" font-size="20" fill="{INK_DIM}">客服 Bot · 内容助手 · 个人 AI 助理 · 社交媒体运营 · 智能问答</text>
  <text x="30" y="122" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：想快速上线 Bot、依赖插件生态的个人/小团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 825)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="90" rx="22" fill="#FEF2F2"/>
  <rect x="0" y="0" width="12" height="90" rx="6" fill="#EF4444"/>
  <text x="30" y="42" font-family="{FONT}" font-size="20" font-weight="800" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="70" font-family="{FONT}" font-size="17" fill="#991B1B">闭源 SaaS，数据在字节服务器上 · 无法自托管 · 有使用限制</text>
</g>

<!-- Rating -->
<g transform="translate(80, 940)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="38" font-weight="900" fill="{COZE}">低</text>
  <text x="0" y="52" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="52" font-family="{FONT}" font-size="38" font-weight="900" fill="{COZE}">★★★★☆</text>
</g>

<g transform="translate(80, 1045)">
  <rect x="0" y="0" width="864" height="54" rx="16" fill="{COZE}" opacity="0.08"/>
  <text x="24" y="34" font-family="{FONT}" font-size="17" font-weight="800" fill="{COZE}">🎯 想快速上线 Bot · 依赖插件生态的个人/小团队</text>
</g>

<g transform="translate(80, 1115)">
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
    print("Generating v3 XHS cards with accurate brand logos + viral design...")
    cards = [
        ("compare-square", make_square()),
        ("compare-card-n8n", make_card_n8n()),
        ("compare-card-dify", make_card_dify()),
        ("compare-card-coze", make_card_coze()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")
