#!/usr/bin/env python3
"""Generate 5 LIGHT (cream/white) viral-style cards for Agnes AI free XHS post.
Big titles, clean layout, brand accent colors."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent

CREAM = "#FAF7F2"
CREAM2 = "#F5F0E8"
WHITE = "#FFFFFF"
TEXT = "#1E293B"
TEXT_DIM = "#64748B"
TEXT_LIGHT = "#94A3B8"
BLUE = "#2563EB"
BLUE_LIGHT = "#DBEAFE"
BLUE_DARK = "#1D4ED8"
PURPLE = "#7C3AED"
PURPLE_LIGHT = "#EDE9FE"
PINK = "#EC4899"
PINK_LIGHT = "#FCE7F3"
GREEN = "#059669"
GREEN_LIGHT = "#D1FAE5"
ORANGE = "#D97706"
ORANGE_LIGHT = "#FEF3C7"
TEAL = "#0D9488"
TEAL_LIGHT = "#CCFBF1"
RED = "#DC2626"
RED_LIGHT = "#FEE2E2"
INDIGO = "#4F46E5"
INDIGO_LIGHT = "#E0E7FF"

CARDS = []


def card_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </radialGradient>
    <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="50%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="#1E293B" flood-opacity="0.10"/>
    </filter>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>

  <circle cx="120" cy="120" r="140" fill="{BLUE_LIGHT}" opacity="0.4"/>
  <circle cx="880" cy="180" r="100" fill="{PURPLE_LIGHT}" opacity="0.4"/>
  <circle cx="160" cy="880" r="110" fill="{PINK_LIGHT}" opacity="0.3"/>
  <circle cx="900" cy="850" r="90" fill="{INDIGO_LIGHT}" opacity="0.3"/>

  <rect x="62" y="40" width="900" height="110" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{BLUE}">🔥 AI 绘画免费时代来了</text>
  <text x="512" y="230" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="100" font-weight="900" fill="url(#titleG)">Agnes AI</text>
  <text x="512" y="310" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">免费了！</text>

  <rect x="112" y="360" width="800" height="70" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="405" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{TEXT}">最强生图 API 全面免费开放</text>

  <g transform="translate(112, 470)">
    <rect x="0" y="0" width="800" height="490" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT_DIM}">🎉 不用绑卡 不限额 即开即用</text>
    <line x1="50" y1="80" x2="750" y2="80" stroke="#E2E8F0" stroke-width="1"/>

    <g transform="translate(40, 105)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{BLUE_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{BLUE}">100% 免费</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{BLUE_DARK}">无需绑定信用卡</text>
    </g>
    <g transform="translate(420, 105)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{PURPLE_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{PURPLE}">1-2 秒出图</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{PURPLE}">比 DALL-E 快 10 倍</text>
    </g>

    <g transform="translate(40, 235)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{GREEN_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{GREEN}">OpenAI 兼容</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{GREEN}">一行代码迁移</text>
    </g>
    <g transform="translate(420, 235)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{PINK_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{PINK}">中文友好</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{PINK}">中文理解远超同行</text>
    </g>

    <text x="400" y="390" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT_DIM}">AI 绘画从此不用再烧钱</text>

    <rect x="200" y="420" width="400" height="50" rx="25" fill="{INDIGO_LIGHT}"/>
    <text x="400" y="452" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{INDIGO}">agnes-ai.com</text>
  </g>

  <text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{BLUE}">#AgnesAI #AI绘画 #免费API #生图工具 #AIGC</text>
</svg>'''
    (ROOT / "agnes-cover.svg").write_text(svg)
    CARDS.append("agnes-cover.svg")


def card_1_news():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="80" cy="80" r="70" fill="{RED_LIGHT}" opacity="0.4"/>
  <circle cx="720" cy="720" r="60" fill="{INDIGO_LIGHT}" opacity="0.3"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{RED_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">🔥 刚刚官宣免费</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="140" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="360" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{BLUE}">Agnes AI 全面免费开放</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT}">模型：agnes-image-2.1-flash</text>
    <text x="40" y="118" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">所有用户直接白嫖，无需任何条件</text>
  </g>

  <g transform="translate(40, 355)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{GREEN_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{GREEN}">&#x2705; 不绑卡</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">注册即用</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">零门槛上手</text>
  </g>

  <g transform="translate(420, 355)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{BLUE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{BLUE}">&#x26A1; 不限量</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">无请求数限制</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">随意调用</text>
  </g>

  <g transform="translate(40, 550)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PURPLE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PURPLE}">&#x1F504; OpenAI 兼容</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">改一行 base_url</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">无需改代码</text>
  </g>

  <g transform="translate(420, 550)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PINK_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PINK}">&#x1F3AF; 高清输出</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">1024x1024 原图</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">无水印无压缩</text>
  </g>

  <g transform="translate(40, 740)">
    <rect x="0" y="0" width="720" height="40" rx="20" fill="{ORANGE_LIGHT}"/>
    <text x="360" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="{ORANGE}">趁还没限流，赶紧注册</text>
  </g>
</svg>'''
    (ROOT / "agnes-card-1-news.svg").write_text(svg)
    CARDS.append("agnes-card-1-news.svg")


def card_2_features():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="700" cy="80" r="60" fill="{GREEN_LIGHT}" opacity="0.5"/>
  <circle cx="80" cy="720" r="50" fill="{BLUE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{BLUE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">&#x2728; 免费能干吗？</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{BLUE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">1</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">文章配图  秒出高质量插图</text>
  </g>

  <g transform="translate(40, 280)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{PURPLE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">2</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">社交卡片  小红书/公众号封面</text>
  </g>

  <g transform="translate(40, 385)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{PINK}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">3</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">产品原型  概念图快速可视化</text>
  </g>

  <g transform="translate(40, 490)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{GREEN}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">4</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">电商主图  商品图批量生成</text>
  </g>

  <g transform="translate(40, 595)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{ORANGE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">5</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">视频封面  高点击率封面图</text>
  </g>

  <g transform="translate(40, 700)">
    <rect x="0" y="0" width="720" height="70" rx="35" fill="{INDIGO_LIGHT}" stroke="{INDIGO}" stroke-width="2"/>
    <text x="360" y="44" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{INDIGO}">中文理解能力远超主流引擎</text>
  </g>
</svg>'''
    (ROOT / "agnes-card-2-features.svg").write_text(svg)
    CARDS.append("agnes-card-2-features.svg")


def card_3_howto():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="80" cy="80" r="70" fill="{GREEN_LIGHT}" opacity="0.4"/>
  <circle cx="720" cy="720" r="60" fill="{PURPLE_LIGHT}" opacity="0.3"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{GREEN_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">&#x1F4CB; 一分钟上手</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="720" height="55" rx="14" fill="{BLUE_LIGHT}"/>
    <text x="360" y="36" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{BLUE}">1. 注册获取 API Key</text>
  </g>

  <g transform="translate(40, 250)">
    <rect x="0" y="0" width="720" height="200" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="40" font-family="monospace" font-size="16" font-weight="700" fill="{TEXT}"># curl 直接调用</text>
    <text x="40" y="70" font-family="monospace" font-size="14" fill="{TEXT_DIM}">curl https://apihub.agnes-ai.com/v1/images/generations \</text>
    <text x="40" y="95" font-family="monospace" font-size="14" fill="{TEXT_DIM}">  -H "Authorization: Bearer $AGNES_KEY" \</text>
    <text x="40" y="120" font-family="monospace" font-size="14" fill="{TEXT_DIM}">  -d '{{"model":"agnes-image-2.1-flash",</text>
    <text x="40" y="145" font-family="monospace" font-size="14" fill="{TEXT_DIM}">        "prompt":"a cat wearing sunglasses",</text>
    <text x="40" y="170" font-family="monospace" font-size="14" fill="{TEXT_DIM}">        "n":1,"size":"1024x1024"}}'</text>
  </g>

  <g transform="translate(40, 480)">
    <rect x="0" y="0" width="720" height="140" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="35" font-family="monospace" font-size="16" font-weight="700" fill="{TEXT}"># Python (OpenAI SDK)</text>
    <text x="40" y="65" font-family="monospace" font-size="14" fill="{TEXT_DIM}">from openai import OpenAI</text>
    <text x="40" y="90" font-family="monospace" font-size="14" fill="{TEXT_DIM}">client = OpenAI(</text>
    <text x="40" y="115" font-family="monospace" font-size="14" fill="{TEXT_DIM}">    base_url="https://apihub.agnes-ai.com/v1",</text>
    <text x="40" y="140" font-family="monospace" font-size="14" fill="{TEXT_DIM}">    api_key="sk-...")</text>
  </g>

  <g transform="translate(40, 650)">
    <rect x="0" y="0" width="340" height="100" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{GREEN_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{GREEN}">&#x1F3C3; 速度快</text>
    <text x="170" y="75" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">1-2 秒出图</text>
  </g>

  <g transform="translate(420, 650)">
    <rect x="0" y="0" width="340" height="100" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{PURPLE_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{PURPLE}">&#x1F3B5; 质量高</text>
    <text x="170" y="75" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">吊打 DALL-E 3</text>
  </g>

  <g transform="translate(40, 770)">
    <rect x="0" y="0" width="720" height="20" rx="10" fill="{ORANGE_LIGHT}"/>
    <text x="360" y="15" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="13" font-weight="700" fill="{ORANGE}">完全免费 · 无需信用卡 · 注册即用</text>
  </g>
</svg>'''
    (ROOT / "agnes-card-3-howto.svg").write_text(svg)
    CARDS.append("agnes-card-3-howto.svg")


def card_4_compare():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="700" cy="80" r="60" fill="{ORANGE_LIGHT}" opacity="0.5"/>
  <circle cx="80" cy="720" r="50" fill="{BLUE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{ORANGE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">&#x2694;&#xFE0F; 竞品对比</text>

  <g transform="translate(40, 170)">
    <rect x="0" y="0" width="720" height="40" rx="10" fill="{RED_LIGHT}"/>
    <text x="100" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="700" fill="{TEXT}">产品</text>
    <text x="300" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="700" fill="{TEXT}">价格</text>
    <text x="460" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="700" fill="{TEXT}">API</text>
    <text x="620" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="700" fill="{TEXT}">速度</text>
  </g>

  <g transform="translate(40, 225)">
    <rect x="0" y="0" width="720" height="60" rx="10" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="{TEXT}">DALL-E 3</text>
    <text x="300" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{RED}">付费</text>
    <text x="460" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{GREEN}">✅</text>
    <text x="620" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{RED}">慢</text>
  </g>

  <g transform="translate(40, 300)">
    <rect x="0" y="0" width="720" height="60" rx="10" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="{TEXT}">Midjourney</text>
    <text x="300" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{RED}">付费</text>
    <text x="460" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{RED}">❌</text>
    <text x="620" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{ORANGE}">中等</text>
  </g>

  <g transform="translate(40, 375)">
    <rect x="0" y="0" width="720" height="60" rx="10" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="100" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="{TEXT}">Stable Diffusion</text>
    <text x="300" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{ORANGE}">自部署</text>
    <text x="460" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{GREEN}">✅</text>
    <text x="620" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{RED}">吃显卡</text>
  </g>

  <g transform="translate(40, 450)">
    <rect x="0" y="0" width="720" height="60" rx="10" fill="{BLUE_LIGHT}" stroke="{BLUE}" stroke-width="2"/>
    <text x="100" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{BLUE}">Agnes AI</text>
    <text x="300" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{GREEN}">免费</text>
    <text x="460" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{GREEN}">✅</text>
    <text x="620" y="37" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{GREEN}">1-2s</text>
  </g>

  <g transform="translate(40, 545)">
    <rect x="0" y="0" width="340" height="110" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{GREEN_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{GREEN}">&#x1F3C6; 碾压优势</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">免费 + 有 API + 秒出图</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">真正的降维打击</text>
  </g>

  <g transform="translate(420, 545)">
    <rect x="0" y="0" width="340" height="110" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{PINK_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{PINK}">&#x1F4AC; 中文友好</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">中文 prompt 理解力</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">远超国外竞品</text>
  </g>

  <g transform="translate(40, 690)">
    <rect x="0" y="0" width="720" height="80" rx="40" fill="{INDIGO_LIGHT}" stroke="{INDIGO}" stroke-width="2"/>
    <text x="360" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{INDIGO}">趁还没人知道，赶紧上车 🐑</text>
  </g>
</svg>'''
    (ROOT / "agnes-card-4-compare.svg").write_text(svg)
    CARDS.append("agnes-card-4-compare.svg")


def main():
    card_cover()
    card_1_news()
    card_2_features()
    card_3_howto()
    card_4_compare()

    print(f"Generated {len(CARDS)} SVGs")
    for name in CARDS:
        png = name.replace(".svg", ".png")
        size = 1024 if "cover" in name else 800
        subprocess.run([
            "inkscape", str(ROOT / name),
            "-o", str(ROOT / png),
            "-w", str(size), "-h", str(size)
        ], check=True)
        print(f"  ✓ {png}")


if __name__ == "__main__":
    main()
