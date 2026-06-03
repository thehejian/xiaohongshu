#!/usr/bin/env python3
"""Generate XHS cards for AI Agent framework comparison (N8N, Dify, Coze)."""

import os, subprocess

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---------- palette ----------
BG       = "#FAF7F2"
BG_CARD  = "#FFFFFF"
INK      = "#1E293B"
INK_DIM  = "#475569"
INK_MUTE = "#94A3B8"
LINE     = "#E2E8F0"

# Brand colors
N8N      = "#EA580C"   # orange-red
DIFY     = "#2563EB"   # blue
COZE     = "#F97316"   # orange
COMPARE  = "#8B5CF6"   # purple

FONT = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"


def card_shadow():
    return '''<filter id="cardShadow" x="-5%" y="-5%" width="115%" height="115%">
    <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#000" flood-opacity="0.06"/>
  </filter>'''


def feature_item(x, y, label, desc, color):
    return f'''<g transform="translate({x}, {y})">
    <rect x="0" y="0" width="6" height="28" rx="3" fill="{color}"/>
    <text x="18" y="12" font-family="{FONT}" font-size="14" font-weight="700" fill="{color}">{label}</text>
    <text x="18" y="28" font-family="{FONT}" font-size="15" fill="{INK_DIM}">{desc}</text>
  </g>'''


def target_box(x, y, w, text, color):
    return f'''<g transform="translate({x}, {y})">
    <rect x="0" y="0" width="{w}" height="42" rx="10" fill="{color}" opacity="0.08"/>
    <text x="16" y="27" font-family="{FONT}" font-size="15" font-weight="600" fill="{color}">🎯 {text}</text>
  </g>'''


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
    <stop offset="0%" stop-color="{COMPARE}"/>
    <stop offset="100%" stop-color="#A78BFA"/>
  </linearGradient>
  {card_shadow()}
</defs>

<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<!-- Eyebrow -->
<g transform="translate(80, 80)">
  <rect x="0" y="0" width="6" height="36" rx="3" fill="{COMPARE}"/>
  <text x="20" y="14" font-family="{FONT}" font-size="14" font-weight="700" letter-spacing="3" fill="{INK_MUTE}">AI AGENT FRAMEWORK</text>
  <text x="20" y="34" font-family="{FONT}" font-size="12" fill="{INK_MUTE}">N8N · Dify · Coze 三选一</text>
</g>

<!-- Hero title -->
<g transform="translate(80, 160)">
  <text x="0" y="0" font-family="{FONT}" font-size="72" font-weight="900" fill="{INK}" letter-spacing="-2">AI Agent</text>
  <text x="0" y="82" font-family="{FONT}" font-size="72" font-weight="900" fill="url(#titleGrad)" letter-spacing="-2">框架四巨头对比</text>
</g>

<!-- Subtitle -->
<g transform="translate(80, 300)">
  <text x="0" y="0" font-family="{FONT}" font-size="22" font-weight="500" fill="{INK_DIM}">看完这张图，选对工具不踩坑</text>
</g>

<!-- Three platform cards in a row -->
<!-- N8N card -->
<g transform="translate(80, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="300" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="270" height="6" rx="3" fill="{N8N}"/>
  <text x="135" y="52" text-anchor="middle" font-family="{FONT}" font-size="32" font-weight="800" fill="{N8N}">N8N</text>
  <text x="135" y="80" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">工作流自动化</text>
  <line x1="30" y1="100" x2="240" y2="100" stroke="{LINE}" stroke-width="1"/>
  {feature_item(30, 120, "开源", "可自托管，数据可控", N8N)}
  {feature_item(30, 165, "节点", "500+ 集成，拖拽编排", N8N)}
  {feature_item(30, 210, "优势", "自动化流程，开发者友好", N8N)}
  {target_box(30, 255, 210, "有开发能力 · 重视隐私", N8N)}
</g>

<!-- Dify card -->
<g transform="translate(377, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="300" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="270" height="6" rx="3" fill="{DIFY}"/>
  <text x="135" y="52" text-anchor="middle" font-family="{FONT}" font-size="32" font-weight="800" fill="{DIFY}">Dify</text>
  <text x="135" y="80" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">LLM 应用开发</text>
  <line x1="30" y1="100" x2="240" y2="100" stroke="{LINE}" stroke-width="1"/>
  {feature_item(30, 120, "开源", "可自部署，社区活跃", DIFY)}
  {feature_item(30, 165, "RAG", "知识库 + Agent 工作流", DIFY)}
  {feature_item(30, 210, "优势", "Prompt 调优 · 模型管理", DIFY)}
  {target_box(30, 255, 210, "搭 LLM 应用 · 需知识库", DIFY)}
</g>

<!-- Coze card -->
<g transform="translate(674, 380)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="270" height="300" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="270" height="6" rx="3" fill="{COZE}"/>
  <text x="135" y="52" text-anchor="middle" font-family="{FONT}" font-size="32" font-weight="800" fill="{COZE}">扣子</text>
  <text x="135" y="80" text-anchor="middle" font-family="{FONT}" font-size="14" fill="{INK_MUTE}">插件生态 Bot</text>
  <line x1="30" y1="100" x2="240" y2="100" stroke="{LINE}" stroke-width="1"/>
  {feature_item(30, 120, "闭源", "SaaS 平台，上手最快", COZE)}
  {feature_item(30, 165, "插件", "上百现成插件，多模态", COZE)}
  {feature_item(30, 210, "优势", "一键发布 · 抖音/飞书/微信", COZE)}
  {target_box(30, 255, 210, "快速上线 · 依赖插件", COZE)}
</g>

<!-- Bottom summary bar -->
<g transform="translate(80, 740)">
  <rect x="0" y="0" width="864" height="60" rx="12" fill="{INK}" opacity="0.04"/>
  <text x="30" y="26" font-family="{FONT}" font-size="14" font-weight="700" fill="{INK_MUTE}">N8N → 自动化流程</text>
  <text x="320" y="26" font-family="{FONT}" font-size="14" font-weight="700" fill="{INK_MUTE}">Dify → LLM 应用 + 知识库</text>
  <text x="640" y="26" font-family="{FONT}" font-size="14" font-weight="700" fill="{INK_MUTE}">扣子 → Bot + 快速上线</text>
  <text x="30" y="50" font-family="{FONT}" font-size="13" fill="{INK_MUTE}">三者组合用也不冲突：N8N 底层 + Dify LLM 层 + 扣子前端</text>
</g>

<!-- Footer -->
<g transform="translate(80, 860)">
  <text x="0" y="0" font-family="{FONT}" font-size="16" fill="{INK}" font-weight="600">#AI Agent · #N8N · #Dify · #扣子 · #Coze · #LLM · #AI工具 · #自动化</text>
</g>
</svg>'''


def make_card_n8n():
    W, H = 1024, 1024
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{BG}"/>
    <stop offset="100%" stop-color="#FDF2F0"/>
  </linearGradient>
  {card_shadow()}
</defs>
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<!-- Top accent -->
<rect x="0" y="0" width="{W}" height="8" fill="{N8N}"/>

<!-- Header -->
<g transform="translate(80, 70)">
  <rect x="0" y="0" width="6" height="36" rx="3" fill="{N8N}"/>
  <text x="20" y="14" font-family="{FONT}" font-size="14" font-weight="700" letter-spacing="3" fill="{INK_MUTE}">WORKFLOW AUTOMATION</text>
  <text x="20" y="34" font-family="{FONT}" font-size="12" fill="{INK_MUTE}">开源 · 自托管 · 500+ 集成</text>
</g>

<!-- Title -->
<g transform="translate(80, 150)">
  <text x="0" y="0" font-family="{FONT}" font-size="80" font-weight="900" fill="{N8N}" letter-spacing="-2">N8N</text>
  <text x="0" y="80" font-family="{FONT}" font-size="36" font-weight="600" fill="{INK}">工作流自动化王者</text>
</g>

<!-- Divider -->
<line x1="80" y1="260" x2="944" y2="260" stroke="{LINE}" stroke-width="1"/>

<!-- Feature blocks -->
<!-- Block 1: 开源 -->
<g transform="translate(80, 300)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{N8N}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{N8N}">开源可自托管</text>
  <text x="30" y="72" font-family="{FONT}" font-size="18" fill="{INK_DIM}">代码开源，可部署在自己的服务器上</text>
  <text x="30" y="96" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">数据完全可控 · 无 API 调用费用</text>
</g>

<!-- Block 2: 节点 -->
<g transform="translate(524, 300)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{N8N}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{N8N}">节点式编排</text>
  <text x="30" y="72" font-family="{FONT}" font-size="18" fill="{INK_DIM}">拖拽节点串联 API、数据库、AI 模型</text>
  <text x="30" y="96" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">500+ 原生集成 · 可视化工作流</text>
</g>

<!-- Block 3: 场景 -->
<g transform="translate(80, 470)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{N8N}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{N8N}">典型使用场景</text>
  <text x="30" y="76" font-family="{FONT}" font-size="18" fill="{INK_DIM}">自动化脚本 · 数据同步 · 内部工具集成 · 定时任务</text>
  <text x="30" y="100" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">适合：有开发能力、重视数据隐私的团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 640)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="80" rx="16" fill="#FEF2F2"/>
  <rect x="0" y="0" width="6" height="80" rx="3" fill="#EF4444"/>
  <text x="30" y="34" font-family="{FONT}" font-size="18" font-weight="700" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="58" font-family="{FONT}" font-size="16" fill="#991B1B">LLM 原生能力较弱，需要自己接 OpenAI / Claude 等 API</text>
</g>

<!-- Rating -->
<g transform="translate(80, 770)">
  <text x="0" y="0" font-family="{FONT}" font-size="18" font-weight="700" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="28" font-weight="800" fill="{N8N}">中等</text>
  <text x="0" y="40" font-family="{FONT}" font-size="18" font-weight="700" fill="{INK}">推荐指数</text>
  <text x="200" y="40" font-family="{FONT}" font-size="28" font-weight="800" fill="{N8N}">★★★★☆</text>
</g>

<!-- Target -->
{target_box(80, 870, 864, "有开发能力 · 重视数据隐私的团队", N8N)}

<!-- Footer -->
<g transform="translate(80, 960)">
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
  {card_shadow()}
</defs>
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<rect x="0" y="0" width="{W}" height="8" fill="{DIFY}"/>

<!-- Header -->
<g transform="translate(80, 70)">
  <rect x="0" y="0" width="6" height="36" rx="3" fill="{DIFY}"/>
  <text x="20" y="14" font-family="{FONT}" font-size="14" font-weight="700" letter-spacing="3" fill="{INK_MUTE}">LLM APPLICATION PLATFORM</text>
  <text x="20" y="34" font-family="{FONT}" font-size="12" fill="{INK_MUTE}">开源 · RAG + Agent + 模型管理</text>
</g>

<!-- Title -->
<g transform="translate(80, 150)">
  <text x="0" y="0" font-family="{FONT}" font-size="80" font-weight="900" fill="{DIFY}" letter-spacing="-2">Dify</text>
  <text x="0" y="80" font-family="{FONT}" font-size="36" font-weight="600" fill="{INK}">LLM 应用开发平台</text>
</g>

<line x1="80" y1="260" x2="944" y2="260" stroke="{LINE}" stroke-width="1"/>

<!-- Block 1: RAG -->
<g transform="translate(80, 300)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{DIFY}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{DIFY}">RAG 知识库</text>
  <text x="30" y="72" font-family="{FONT}" font-size="18" fill="{INK_DIM}">上传文档自动切片 · 向量检索 · 精准回答</text>
  <text x="30" y="96" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">支持 PDF/Word/Markdown · 知识库管理</text>
</g>

<!-- Block 2: Agent -->
<g transform="translate(524, 300)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{DIFY}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{DIFY}">Agent 工作流</text>
  <text x="30" y="72" font-family="{FONT}" font-size="18" fill="{INK_DIM}">可视化编排 Agent 推理流程</text>
  <text x="30" y="96" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">多模型路由 · Prompt 版本管理</text>
</g>

<!-- Block 3: 场景 -->
<g transform="translate(80, 470)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{DIFY}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{DIFY}">典型使用场景</text>
  <text x="30" y="76" font-family="{FONT}" font-size="18" fill="{INK_DIM}">企业知识库问答 · ChatBot · 内容生成 · 数据分析助手</text>
  <text x="30" y="100" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">适合：想快速搭建 LLM 应用、需要知识库的企业</text>
</g>

<!-- Advantage -->
<g transform="translate(80, 640)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="80" rx="16" fill="#EFF6FF"/>
  <rect x="0" y="0" width="6" height="80" rx="3" fill="{DIFY}"/>
  <text x="30" y="34" font-family="{FONT}" font-size="18" font-weight="700" fill="{DIFY}">💡 优势</text>
  <text x="30" y="58" font-family="{FONT}" font-size="16" fill="#1E40AF">比 N8N 更懂 LLM，比 Coze 更灵活 · 开源可自部署</text>
</g>

<!-- Rating -->
<g transform="translate(80, 770)">
  <text x="0" y="0" font-family="{FONT}" font-size="18" font-weight="700" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="28" font-weight="800" fill="{DIFY}">中等</text>
  <text x="0" y="40" font-family="{FONT}" font-size="18" font-weight="700" fill="{INK}">推荐指数</text>
  <text x="200" y="40" font-family="{FONT}" font-size="28" font-weight="800" fill="{DIFY}">★★★★★</text>
</g>

{target_box(80, 870, 864, "想快速搭建 LLM 应用 · 需要知识库的企业", DIFY)}

<g transform="translate(80, 960)">
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
    <stop offset="100%" stop-color="#FFF7ED"/>
  </linearGradient>
  {card_shadow()}
</defs>
<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>

<rect x="0" y="0" width="{W}" height="8" fill="{COZE}"/>

<!-- Header -->
<g transform="translate(80, 70)">
  <rect x="0" y="0" width="6" height="36" rx="3" fill="{COZE}"/>
  <text x="20" y="14" font-family="{FONT}" font-size="14" font-weight="700" letter-spacing="3" fill="{INK_MUTE}">BYTE DANCE AI BOT PLATFORM</text>
  <text x="20" y="34" font-family="{FONT}" font-size="12" fill="{INK_MUTE}">闭源 · 插件生态 · 多模态 · 一键发布</text>
</g>

<!-- Title -->
<g transform="translate(80, 150)">
  <text x="0" y="0" font-family="{FONT}" font-size="80" font-weight="900" fill="{COZE}" letter-spacing="-2">扣子</text>
  <text x="0" y="80" font-family="{FONT}" font-size="36" font-weight="600" fill="{INK}">字节出品 · 插件生态 Bot 平台</text>
</g>

<line x1="80" y1="260" x2="944" y2="260" stroke="{LINE}" stroke-width="1"/>

<!-- Block 1: 插件 -->
<g transform="translate(80, 300)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{COZE}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{COZE}">插件生态</text>
  <text x="30" y="72" font-family="{FONT}" font-size="18" fill="{INK_DIM}">上百个现成插件，搜索/数据库/绘图一键调用</text>
  <text x="30" y="96" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">无需开发 · 拖拽配置 · 社区贡献</text>
</g>

<!-- Block 2: 多模态 -->
<g transform="translate(524, 300)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="420" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{COZE}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{COZE}">多模态能力</text>
  <text x="30" y="72" font-family="{FONT}" font-size="18" fill="{INK_DIM}">文本 + 图片 + 语音，全能型 Bot</text>
  <text x="30" y="96" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">图片识别 · 文生图 · 语音输入输出</text>
</g>

<!-- Block 3: 场景 -->
<g transform="translate(80, 470)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="130" rx="16" fill="{BG_CARD}"/>
  <rect x="0" y="0" width="6" height="130" rx="3" fill="{COZE}"/>
  <text x="30" y="42" font-family="{FONT}" font-size="22" font-weight="800" fill="{COZE}">典型使用场景</text>
  <text x="30" y="76" font-family="{FONT}" font-size="18" fill="{INK_DIM}">客服 Bot · 内容助手 · 个人 AI 助理 · 社交媒体运营</text>
  <text x="30" y="100" font-family="{FONT}" font-size="16" fill="{INK_MUTE}">适合：想快速上线 Bot、依赖插件生态的个人/小团队</text>
</g>

<!-- Limitation -->
<g transform="translate(80, 640)" filter="url(#cardShadow)">
  <rect x="0" y="0" width="864" height="80" rx="16" fill="#FEF2F2"/>
  <rect x="0" y="0" width="6" height="80" rx="3" fill="#EF4444"/>
  <text x="30" y="34" font-family="{FONT}" font-size="18" font-weight="700" fill="#DC2626">⚠️ 注意</text>
  <text x="30" y="58" font-family="{FONT}" font-size="16" fill="#991B1B">闭源 SaaS，数据在字节服务器上 · 无法自托管</text>
</g>

<!-- Rating -->
<g transform="translate(80, 770)">
  <text x="0" y="0" font-family="{FONT}" font-size="18" font-weight="700" fill="{INK}">上手难度</text>
  <text x="200" y="0" font-family="{FONT}" font-size="28" font-weight="800" fill="{COZE}">低</text>
  <text x="0" y="40" font-family="{FONT}" font-size="18" font-weight="700" fill="{INK}">推荐指数</text>
  <text x="200" y="40" font-family="{FONT}" font-size="28" font-weight="800" fill="{COZE}">★★★★☆</text>
</g>

{target_box(80, 870, 864, "想快速上线 Bot · 依赖插件生态的个人/小团队", COZE)}

<g transform="translate(80, 960)">
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
    print("Generating AI Agent framework comparison cards...")
    cards = [
        ("compare-square", make_square()),
        ("compare-card-n8n", make_card_n8n()),
        ("compare-card-dify", make_card_dify()),
        ("compare-card-coze", make_card_coze()),
    ]
    for name, svg in cards:
        save_svg(name, svg)
    print(f"Done! {len(cards)} cards saved to {OUT}")
