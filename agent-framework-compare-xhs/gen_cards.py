#!/usr/bin/env python3
"""Generate XHS cards for AI Agent framework comparison — redesigned for maximum visual impact with brand logos."""

import os, subprocess

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
BG       = "#FAF7F2"
INK      = "#0F172A"
INK_DIM  = "#475569"
INK_MUTE = "#94A3B8"
LINE     = "#E2E8F0"

# Brand colors — bold, saturated
N8N      = "#F97316"
DIFY     = "#2563EB"
COZE     = "#F43F5E"
TITLE    = "#7C3AED"

FONT = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"


def card_shadow():
    return '''<filter id="cardShadow" x="-10%" y="-10%" width="125%" height="125%">
    <feDropShadow dx="0" dy="12" stdDeviation="20" flood-color="#000" flood-opacity="0.1"/>
  </filter>'''


def n8n_logo(cx, cy, size):
    """N8N: chain link logo — two interlocking ovals"""
    s = size
    return f'''<g transform="translate({cx},{cy})">
    <ellipse cx="-s*0.35" cy="0" rx="s*0.38" ry="s*0.5" fill="none" stroke="{N8N}" stroke-width="s*0.12" opacity="0.95"/>
    <ellipse cx="s*0.35" cy="0" rx="s*0.38" ry="s*0.5" fill="none" stroke="{N8N}" stroke-width="s*0.12" opacity="0.95"/>
    <ellipse cx="0" cy="0" rx="s*0.15" ry="s*0.3" fill="{N8N}" opacity="0.2"/>
  </g>'''


def dify_logo(cx, cy, size):
    """Dify: wave / infinity symbol"""
    s = size
    return f'''<g transform="translate({cx},{cy})">
    <path d="M -s*0.45 -s*0.05 C -s*0.45 -s*0.35, -s*0.15 -s*0.35, -s*0.15 -s*0.05 C -s*0.15 s*0.25, s*0.15 s*0.25, s*0.15 -s*0.05 C s*0.15 -s*0.35, s*0.45 -s*0.35, s*0.45 -s*0.05"
          fill="none" stroke="{DIFY}" stroke-width="s*0.14" stroke-linecap="round"/>
    <circle cx="-s*0.15" cy="-s*0.05" r="s*0.06" fill="{DIFY}"/>
    <circle cx="s*0.15" cy="-s*0.05" r="s*0.06" fill="{DIFY}"/>
    <circle cx="s*0.45" cy="-s*0.05" r="s*0.06" fill="{DIFY}"/>
  </g>'''


def coze_logo(cx, cy, size):
    """Coze: speech bubble with three dots"""
    s = size
    return f'''<g transform="translate({cx},{cy})">
    <rect x="-s*0.4" y="-s*0.35" width="s*0.8" height="s*0.6" rx="s*0.1" fill="{COZE}"/>
    <polygon points="-s*0.15,s*0.25 -s*0.4,s*0.55 -s*0.05,s*0.3" fill="{COZE}"/>
    <circle cx="-s*0.15" cy="0" r="s*0.05" fill="white"/>
    <circle cx="0" cy="0" r="s*0.05" fill="white"/>
    <circle cx="s*0.15" cy="0" r="s*0.05" fill="white"/>
  </g>'''


def logo_badge(cx, cy, r, bg_color, logo_svg, fill_color):
    return f'''<circle cx="{cx}" cy="{cy}" r="{r}" fill="{bg_color}"/>
  {logo_svg(cx, cy, r * 2.2)}'''


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
    <feGaussianBlur stdDeviation="10" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  {card_shadow()}
</defs>

<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<circle cx="120" cy="120" r="140" fill="{TITLE}" opacity="0.04"/>
<circle cx="{W-120}" cy="{H-120}" r="180" fill="{TITLE}" opacity="0.04"/>

<!-- Eyebrow -->
<g transform="translate(80, 60)">
  <rect x="0" y="0" width="10" height="44" rx="5" fill="{TITLE}"/>
  <text x="28" y="18" font-family="{FONT}" font-size="16" font-weight="800" letter-spacing="4" fill="{TITLE}">AI AGENT FRAMEWORK</text>
  <text x="28" y="44" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">N8N · Dify · 扣子 三选一</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 150)">
  <text x="0" y="0" font-family="{FONT}" font-size="92" font-weight="900" fill="{INK}" letter-spacing="-4" filter="url(#glow)">AI Agent</text>
  <text x="0" y="100" font-family="{FONT}" font-size="92" font-weight="900" fill="url(#titleGrad)" letter-spacing="-4">框架对比</text>
</g>

<!-- Subtitle -->
<g transform="translate(80, 300)">
  <text x="0" y="0" font-family="{FONT}" font-size="26" font-weight="600" fill="{INK_DIM}">看完这张图，选对工具不踩坑 👇</text>
</g>

<!-- Three platform cards with BIG logos — horizontal row -->
<!-- N8N card -->
<g transform="translate(80, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="360" rx="24" fill="white"/>
  <rect x="0" y="0" width="270" height="10" rx="24" fill="url(#orangeGrad)"/>
  <rect x="0" y="10" width="270" height="10" rx="0" fill="url(#orangeGrad)"/>
  
  {logo_badge(135, 110, 55, "#FFF7ED", n8n_logo, N8N)}
  
  <text x="135" y="200" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="900" fill="{N8N}">N8N</text>
  <text x="135" y="228" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">工作流自动化</text>
  
  <line x1="35" y1="255" x2="235" y2="255" stroke="{LINE}" stroke-width="1"/>
  
  <g transform="translate(35, 275)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{N8N}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">开源可自托管</text>
  </g>
  <g transform="translate(35, 310)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{N8N}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">500+ 集成节点</text>
  </g>
  <g transform="translate(35, 345)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{N8N}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">上手难度：中等</text>
  </g>
</g>

<!-- Dify card -->
<g transform="translate(377, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="360" rx="24" fill="white"/>
  <rect x="0" y="0" width="270" height="10" rx="24" fill="url(#blueGrad)"/>
  <rect x="0" y="10" width="270" height="10" rx="0" fill="url(#blueGrad)"/>
  
  {logo_badge(135, 110, 55, "#EFF6FF", dify_logo, DIFY)}
  
  <text x="135" y="200" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="900" fill="{DIFY}">Dify</text>
  <text x="135" y="228" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">LLM 应用开发</text>
  
  <line x1="35" y1="255" x2="235" y2="255" stroke="{LINE}" stroke-width="1"/>
  
  <g transform="translate(35, 275)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{DIFY}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">开源可自部署</text>
  </g>
  <g transform="translate(35, 310)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{DIFY}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">RAG + Agent 工作流</text>
  </g>
  <g transform="translate(35, 345)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{DIFY}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">上手难度：中等</text>
  </g>
</g>

<!-- Coze card -->
<g transform="translate(674, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="360" rx="24" fill="white"/>
  <rect x="0" y="0" width="270" height="10" rx="24" fill="url(#roseGrad)"/>
  <rect x="0" y="10" width="270" height="10" rx="0" fill="url(#roseGrad)"/>
  
  {logo_badge(135, 110, 55, "#FFF1F2", coze_logo, COZE)}
  
  <text x="135" y="200" text-anchor="middle" font-family="{FONT}" font-size="44" font-weight="900" fill="{COZE}">扣子</text>
  <text x="135" y="228" text-anchor="middle" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">插件生态 Bot</text>
  
  <line x1="35" y1="255" x2="235" y2="255" stroke="{LINE}" stroke-width="1"/>
  
  <g transform="translate(35, 275)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{COZE}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">闭源 SaaS 平台</text>
  </g>
  <g transform="translate(35, 310)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{COZE}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">上百插件 + 多模态</text>
  </g>
  <g transform="translate(35, 345)">
    <rect x="0" y="0" width="8" height="26" rx="4" fill="{COZE}"/>
    <text x="18" y="19" font-family="{FONT}" font-size="15" font-weight="700" fill="{INK}">上手难度：低</text>
  </g>
</g>

<!-- Bottom summary bar -->
<g transform="translate(80, 790)">
  <rect x="0" y="0" width="864" height="68" rx="16" fill="{INK}" opacity="0.04"/>
  <text x="30" y="28" font-family="{FONT}" font-size="15" font-weight="800" fill="{N8N}">🟠 N8N → 自动化流程</text>
  <text x="340" y="28" font-family="{FONT}" font-size="15" font-weight="800" fill="{DIFY}">🔵 Dify → LLM 应用 + 知识库</text>
  <text x="680" y="28" font-family="{FONT}" font-size="15" font-weight="800" fill="{COZE}">🔴 扣子 → Bot + 快速上线</text>
  <text x="30" y="52" font-family="{FONT}" font-size="13" fill="{INK_MUTE}">三者组合用也不冲突：N8N 底层 + Dify LLM 层 + 扣子前端</text>
</g>

<!-- Footer -->
<g transform="translate(80, 910)">
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

<rect x="0" y="0" width="{W}" height="12" fill="url(#accentGrad)"/>

<!-- BIG logo + title at top -->
<g transform="translate(80, 50)">
  {logo_badge(70, 60, 65, "#FFF7ED", n8n_logo, N8N)}
  <text x="160" y="55" font-family="{FONT}" font-size="64" font-weight="900" fill="{N8N}" letter-spacing="-2">N8N</text>
  <text x="160" y="90" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">WORKFLOW AUTOMATION</text>
</g>

<line x1="80" y1="170" x2="944" y2="170" stroke="{LINE}" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 200)">
  <rect x="0" y="0" width="10" height="40" rx="5" fill="{N8N}"/>
  <text x="26" y="18" font-family="{FONT}" font-size="15" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">开源 · 自托管 · 500+ 集成</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="80" font-weight="900" fill="{INK}" letter-spacing="-3">工作流自动化</text>
  <text x="0" y="90" font-family="{FONT}" font-size="64" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">王 者</text>
</g>

<line x1="80" y1="400" x2="944" y2="400" stroke="{LINE}" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 430)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{N8N}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{N8N}">开源可自托管</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">代码完全开源，可部署在自己的服务器上</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 数据完全可控  ✅ 无 API 调用费用  ✅ 社区持续更新</text>
</g>

<g transform="translate(524, 430)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{N8N}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{N8N}">节点式编排</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">拖拽节点串联 API、数据库、AI 模型</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 500+ 原生集成  ✅ 可视化工作流  ✅ 支持自定义节点</text>
</g>

<g transform="translate(80, 610)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{N8N}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{N8N}">典型使用场景</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">自动化脚本 · 数据同步 · 内部工具集成 · 定时任务 · 跨平台工作流</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：有开发能力、重视数据隐私的团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 790)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="85" rx="20" fill="#FEF2F2"/>
  <rect x="0" y="0" width="10" height="85" rx="5" fill="#EF4444"/>
  <text x="30" y="40" font-family="{FONT}" font-size="20" font-weight="800" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="66" font-family="{FONT}" font-size="17" fill="#991B1B">LLM 原生能力较弱，需要自己接 OpenAI / Claude 等 API</text>
</g>

<!-- Rating -->
<g transform="translate(80, 900)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="36" font-weight="900" fill="{N8N}">中等</text>
  <text x="0" y="48" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="48" font-family="{FONT}" font-size="36" font-weight="900" fill="{N8N}">★★★★☆</text>
</g>

<g transform="translate(80, 1000)">
  <rect x="0" y="0" width="864" height="50" rx="14" fill="{N8N}" opacity="0.08"/>
  <text x="22" y="32" font-family="{FONT}" font-size="17" font-weight="800" fill="{N8N}">🎯 有开发能力 · 重视数据隐私的团队</text>
</g>

<g transform="translate(80, 1070)">
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

<rect x="0" y="0" width="{W}" height="12" fill="url(#accentGrad)"/>

<!-- BIG logo + title -->
<g transform="translate(80, 50)">
  {logo_badge(70, 60, 65, "#EFF6FF", dify_logo, DIFY)}
  <text x="160" y="55" font-family="{FONT}" font-size="64" font-weight="900" fill="{DIFY}" letter-spacing="-2">Dify</text>
  <text x="160" y="90" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">LLM APPLICATION PLATFORM</text>
</g>

<line x1="80" y1="170" x2="944" y2="170" stroke="{LINE}" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 200)">
  <rect x="0" y="0" width="10" height="40" rx="5" fill="{DIFY}"/>
  <text x="26" y="18" font-family="{FONT}" font-size="15" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">开源 · RAG + Agent + 模型管理</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="80" font-weight="900" fill="{INK}" letter-spacing="-3">LLM 应用</text>
  <text x="0" y="90" font-family="{FONT}" font-size="64" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">开 发 平 台</text>
</g>

<line x1="80" y1="400" x2="944" y2="400" stroke="{LINE}" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 430)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{DIFY}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{DIFY}">RAG 知识库</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">上传文档自动切片 · 向量检索 · 精准回答</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ PDF/Word/Markdown  ✅ 知识库管理  ✅ 混合检索</text>
</g>

<g transform="translate(524, 430)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{DIFY}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{DIFY}">Agent 工作流</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">可视化编排 Agent 推理流程</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 多模型路由  ✅ Prompt 版本管理  ✅ 工具调用</text>
</g>

<g transform="translate(80, 610)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{DIFY}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{DIFY}">典型使用场景</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">企业知识库问答 · ChatBot · 内容生成 · 数据分析助手 · 智能客服</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：想快速搭建 LLM 应用、需要知识库的企业</text>
</g>

<!-- Advantage -->
<g transform="translate(80, 790)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="85" rx="20" fill="#EFF6FF"/>
  <rect x="0" y="0" width="10" height="85" rx="5" fill="{DIFY}"/>
  <text x="30" y="40" font-family="{FONT}" font-size="20" font-weight="800" fill="{DIFY}">💡 优势</text>
  <text x="30" y="66" font-family="{FONT}" font-size="17" fill="#1E40AF">比 N8N 更懂 LLM，比 Coze 更灵活 · 开源可自部署 · 社区活跃</text>
</g>

<!-- Rating -->
<g transform="translate(80, 900)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="36" font-weight="900" fill="{DIFY}">中等</text>
  <text x="0" y="48" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="48" font-family="{FONT}" font-size="36" font-weight="900" fill="{DIFY}">★★★★★</text>
</g>

<g transform="translate(80, 1000)">
  <rect x="0" y="0" width="864" height="50" rx="14" fill="{DIFY}" opacity="0.08"/>
  <text x="22" y="32" font-family="{FONT}" font-size="17" font-weight="800" fill="{DIFY}">🎯 想快速搭建 LLM 应用 · 需要知识库的企业</text>
</g>

<g transform="translate(80, 1070)">
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

<rect x="0" y="0" width="{W}" height="12" fill="url(#accentGrad)"/>

<!-- BIG logo + title -->
<g transform="translate(80, 50)">
  {logo_badge(70, 60, 65, "#FFF1F2", coze_logo, COZE)}
  <text x="160" y="55" font-family="{FONT}" font-size="64" font-weight="900" fill="{COZE}" letter-spacing="-2">扣子</text>
  <text x="160" y="90" font-family="{FONT}" font-size="20" fill="{INK_MUTE}">BYTE DANCE AI BOT PLATFORM</text>
</g>

<line x1="80" y1="170" x2="944" y2="170" stroke="{LINE}" stroke-width="1"/>

<!-- Eyebrow -->
<g transform="translate(80, 200)">
  <rect x="0" y="0" width="10" height="40" rx="5" fill="{COZE}"/>
  <text x="26" y="18" font-family="{FONT}" font-size="15" font-weight="800" letter-spacing="3" fill="{INK_MUTE}">闭源 · 插件生态 · 多模态 · 一键发布</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 280)">
  <text x="0" y="0" font-family="{FONT}" font-size="80" font-weight="900" fill="{INK}" letter-spacing="-3">字节出品</text>
  <text x="0" y="90" font-family="{FONT}" font-size="64" font-weight="900" fill="url(#accentGrad)" letter-spacing="-1">插 件 生 态</text>
</g>

<line x1="80" y1="400" x2="944" y2="400" stroke="{LINE}" stroke-width="1"/>

<!-- Feature blocks -->
<g transform="translate(80, 430)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{COZE}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{COZE}">插件生态</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">上百个现成插件，搜索/数据库/绘图一键调用</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 无需开发  ✅ 拖拽配置  ✅ 社区贡献</text>
</g>

<g transform="translate(524, 430)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{COZE}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{COZE}">多模态能力</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">文本 + 图片 + 语音，全能型 Bot</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">✅ 图片识别  ✅ 文生图  ✅ 语音输入输出</text>
</g>

<g transform="translate(80, 610)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="150" rx="20" fill="white"/>
  <rect x="0" y="0" width="10" height="150" rx="5" fill="{COZE}"/>
  <text x="30" y="55" font-family="{FONT}" font-size="30" font-weight="800" fill="{COZE}">典型使用场景</text>
  <text x="30" y="88" font-family="{FONT}" font-size="20" fill="{INK_DIM}">客服 Bot · 内容助手 · 个人 AI 助理 · 社交媒体运营 · 智能问答</text>
  <text x="30" y="116" font-family="{FONT}" font-size="17" fill="{INK_MUTE}">适合：想快速上线 Bot、依赖插件生态的个人/小团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 790)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="85" rx="20" fill="#FEF2F2"/>
  <rect x="0" y="0" width="10" height="85" rx="5" fill="#EF4444"/>
  <text x="30" y="40" font-family="{FONT}" font-size="20" font-weight="800" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="66" font-family="{FONT}" font-size="17" fill="#991B1B">闭源 SaaS，数据在字节服务器上 · 无法自托管 · 有使用限制</text>
</g>

<!-- Rating -->
<g transform="translate(80, 900)">
  <text x="0" y="0" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="36" font-weight="900" fill="{COZE}">低</text>
  <text x="0" y="48" font-family="{FONT}" font-size="20" font-weight="800" fill="{INK}">推荐指数</text>
  <text x="200" y="48" font-family="{FONT}" font-size="36" font-weight="900" fill="{COZE}">★★★★☆</text>
</g>

<g transform="translate(80, 1000)">
  <rect x="0" y="0" width="864" height="50" rx="14" fill="{COZE}" opacity="0.08"/>
  <text x="22" y="32" font-family="{FONT}" font-size="17" font-weight="800" fill="{COZE}">🎯 想快速上线 Bot · 依赖插件生态的个人/小团队</text>
</g>

<g transform="translate(80, 1070)">
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
    print("Generating redesigned XHS cards with brand logos...")
    cards = [
        ("compare-square", make_square()),
        ("compare-card-n8n", make_card_n8n()),
        ("compare-card-dify", make_card_dify()),
        ("compare-card-coze", make_card_coze()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")
