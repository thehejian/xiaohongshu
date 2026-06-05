#!/usr/bin/env python3
"""Generate 6 LIGHT (cream/white) viral-style cards for DeepSeek API tutorial XHS post."""
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
RED = "#DC2626"
RED_LIGHT = "#FEE2E2"

CARDS = []


def card_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </radialGradient>
    <linearGradient id="title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="40%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="#1E293B" flood-opacity="0.10"/>
    </filter>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>

  <circle cx="150" cy="150" r="120" fill="{BLUE_LIGHT}" opacity="0.4"/>
  <circle cx="850" cy="200" r="90" fill="{PURPLE_LIGHT}" opacity="0.4"/>
  <circle cx="200" cy="850" r="100" fill="{PINK_LIGHT}" opacity="0.3"/>
  <circle cx="880" cy="800" r="80" fill="{BLUE_LIGHT}" opacity="0.3"/>

  <rect x="62" y="60" width="900" height="180" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="120" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="700" fill="{BLUE}">🔥 保姆级教程</text>
  <text x="512" y="200" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="80" font-weight="900" fill="url(#title)">DeepSeek API</text>

  <rect x="162" y="280" width="700" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="333" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="38" font-weight="800" fill="{TEXT}">申请 → 调用 → 避坑</text>

  <g transform="translate(162, 420)">
    <rect x="0" y="0" width="700" height="520" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="350" y="58" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT_DIM}">📋 本教程覆盖</text>
    <line x1="60" y1="80" x2="640" y2="80" stroke="#E2E8F0" stroke-width="1"/>

    <g transform="translate(40, 110)">
      <circle cx="20" cy="20" r="18" fill="{BLUE}"/>
      <text x="20" y="26" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFF">1</text>
      <text x="55" y="27" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="600" fill="{TEXT}">官网注册 &amp; 登录</text>
    </g>
    <g transform="translate(40, 180)">
      <circle cx="20" cy="20" r="18" fill="{PURPLE}"/>
      <text x="20" y="26" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFF">2</text>
      <text x="55" y="27" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="600" fill="{TEXT}">API Key 创建 &amp; 保存</text>
    </g>
    <g transform="translate(40, 250)">
      <circle cx="20" cy="20" r="18" fill="{PINK}"/>
      <text x="20" y="26" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFF">3</text>
      <text x="55" y="27" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="600" fill="{TEXT}">cURL / Python 调用</text>
    </g>
    <g transform="translate(40, 320)">
      <circle cx="20" cy="20" r="18" fill="{GREEN}"/>
      <text x="20" y="26" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="#FFF">4</text>
      <text x="55" y="27" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="600" fill="{TEXT}">价格参考 &amp; 避坑</text>
    </g>

    <text x="350" y="420" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">🚀 零基础 5 分钟搞定</text>
  </g>

  <text x="512" y="980" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{BLUE}">platform.deepseek.com</text>
</svg>'''
    (ROOT / "deepseek-square-cover.svg").write_text(svg)
    CARDS.append("deepseek-square-cover.svg")


def card_1_signup():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="80" cy="80" r="60" fill="{BLUE_LIGHT}" opacity="0.5"/>
  <circle cx="700" cy="120" r="50" fill="{PURPLE_LIGHT}" opacity="0.4"/>
  <circle cx="120" cy="700" r="70" fill="{PINK_LIGHT}" opacity="0.3"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{BLUE_LIGHT}" filter="url(#shadow)"/>
    <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">Step 1 注册 &amp; 登录</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="160" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="16" height="160" rx="8" fill="{BLUE}"/>
    <text x="40" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{TEXT}">🌐 打开官网</text>
    <rect x="40" y="70" width="640" height="60" rx="12" fill="{BLUE_LIGHT}"/>
    <text x="360" y="108" text-anchor="middle" font-family="ui-monospace, monospace" font-size="26" font-weight="700" fill="{BLUE_DARK}">platform.deepseek.com</text>
    <text x="40" y="135" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{RED}" font-weight="600">⚠️ 是 platform 不是 chat！</text>
  </g>

  <g transform="translate(40, 380)">
    <rect x="0" y="0" width="720" height="160" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="16" height="160" rx="8" fill="{PURPLE}"/>
    <text x="40" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{TEXT}">✉️ 注册 / 登录</text>
    <text x="40" y="90" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT}">点击右上角 Sign Up → 邮箱注册</text>
    <text x="40" y="125" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT}">支持邮箱验证码，无需翻墙</text>
  </g>

  <g transform="translate(40, 580)">
    <rect x="0" y="0" width="720" height="160" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="16" height="160" rx="8" fill="{GREEN}"/>
    <text x="40" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{TEXT}">🎁 免费额度</text>
    <text x="40" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{GREEN}">新用户赠送 500 万 tokens</text>
    <text x="40" y="130" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">有效期 30 天 · 够玩很久了</text>
  </g>
</svg>'''
    (ROOT / "deepseek-card-1-signup.svg").write_text(svg)
    CARDS.append("deepseek-card-1-signup.svg")


def card_2_apikey():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="700" cy="80" r="60" fill="{PURPLE_LIGHT}" opacity="0.5"/>
  <circle cx="80" cy="720" r="50" fill="{BLUE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{PURPLE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">Step 2 创建 API Key</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="140" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="16" height="140" rx="8" fill="{PURPLE}"/>
    <text x="40" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{TEXT}">🗝️ 找到 API Keys</text>
    <text x="40" y="90" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT}">左侧导航栏 → API Keys</text>
    <text x="40" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">点击「+ Create API key」按钮</text>
  </g>

  <g transform="translate(40, 360)">
    <rect x="0" y="0" width="720" height="140" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="16" height="140" rx="8" fill="{PINK}"/>
    <text x="40" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{TEXT}">📝 填写信息</text>
    <text x="40" y="90" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT}">给密钥取个名字（随意）</text>
    <text x="40" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">例如：my-dev-key</text>
  </g>

  <g transform="translate(40, 540)">
    <rect x="0" y="0" width="720" height="200" rx="24" fill="{RED_LIGHT}" filter="url(#shadow)" stroke="{RED}" stroke-width="2"/>
    <text x="360" y="50" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{RED}">⚠️ 关键！只显示一次</text>
    <text x="360" y="100" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT}">创建成功后密钥一次性显示</text>
    <text x="360" y="140" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT}">关掉就再也看不到了！</text>
    <text x="360" y="180" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED}">👉 立刻复制保存！</text>
  </g>
</svg>'''
    (ROOT / "deepseek-card-2-apikey.svg").write_text(svg)
    CARDS.append("deepseek-card-2-apikey.svg")


def card_3_code():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="80" cy="80" r="60" fill="{GREEN_LIGHT}" opacity="0.5"/>
  <circle cx="720" cy="700" r="50" fill="{BLUE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{GREEN_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">Step 3 开始调用</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="50" rx="12" fill="{GREEN_LIGHT}"/>
    <text x="30" y="33" font-family="ui-monospace, monospace" font-size="18" font-weight="700" fill="{GREEN}">$ cURL 版本</text>
  </g>

  <g transform="translate(40, 240)">
    <rect x="0" y="0" width="720" height="200" rx="16" fill="#1E293B" filter="url(#shadow)"/>
    <text x="24" y="32" font-family="ui-monospace, monospace" font-size="14" fill="#E2E8F0">curl https://api.deepseek.com/v1/chat/completions \</text>
    <text x="24" y="60" font-family="ui-monospace, monospace" font-size="14" fill="#94A3B8">  -H "Content-Type: application/json" \</text>
    <text x="24" y="88" font-family="ui-monospace, monospace" font-size="14" fill="#94A3B8">  -H "Authorization: Bearer sk-..." \</text>
    <text x="24" y="116" font-family="ui-monospace, monospace" font-size="14" fill="#E2E8F0">  -d '{{"model": "deepseek-chat",</text>
    <text x="36" y="144" font-family="ui-monospace, monospace" font-size="14" fill="#E2E8F0">"messages": [{{"role": "user", "content": "你好"}}]}}'</text>
  </g>

  <g transform="translate(40, 460)">
    <rect x="0" y="0" width="720" height="50" rx="12" fill="{BLUE_LIGHT}"/>
    <text x="30" y="33" font-family="ui-monospace, monospace" font-size="18" font-weight="700" fill="{BLUE}">$ Python 版本</text>
  </g>

  <g transform="translate(40, 520)">
    <rect x="0" y="0" width="720" height="230" rx="16" fill="#1E293B" filter="url(#shadow)"/>
    <text x="24" y="36" font-family="ui-monospace, monospace" font-size="15" fill="#6EE7B7">from openai import OpenAI</text>
    <text x="24" y="72" font-family="ui-monospace, monospace" font-size="15" fill="#E2E8F0">client = OpenAI(</text>
    <text x="40" y="104" font-family="ui-monospace, monospace" font-size="15" fill="#FCD34D">api_key="sk-...",</text>
    <text x="40" y="136" font-family="ui-monospace, monospace" font-size="15" fill="#FCD34D">base_url="https://api.deepseek.com/v1"</text>
    <text x="24" y="168" font-family="ui-monospace, monospace" font-size="15" fill="#E2E8F0">)</text>
    <text x="24" y="200" font-family="ui-monospace, monospace" font-size="15" fill="#6EE7B7"># 兼容 OpenAI SDK！</text>
  </g>
</svg>'''
    (ROOT / "deepseek-card-3-code.svg").write_text(svg)
    CARDS.append("deepseek-card-3-code.svg")


def card_4_pricing():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="700" cy="100" r="60" fill="{ORANGE_LIGHT}" opacity="0.5"/>
  <circle cx="80" cy="720" r="70" fill="{PINK_LIGHT}" opacity="0.3"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{ORANGE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">💰 价格参考</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="200" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="360" y="50" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{TEXT}">DeepSeek-V3</text>
    <text x="360" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">输入：¥1 / 百万 tokens</text>
    <text x="360" y="130" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">输出：¥2 / 百万 tokens</text>
    <text x="360" y="175" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{GREEN}">性价比之王</text>
  </g>

  <g transform="translate(40, 420)">
    <rect x="0" y="0" width="720" height="200" rx="24" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="360" y="50" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{TEXT}">DeepSeek-R1</text>
    <text x="360" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">输入：¥4 / 百万 tokens</text>
    <text x="360" y="130" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">输出：¥16 / 百万 tokens</text>
    <text x="360" y="175" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{PURPLE}">推理能力强悍</text>
  </g>

  <g transform="translate(40, 660)">
    <rect x="0" y="0" width="720" height="100" rx="50" fill="{GREEN_LIGHT}" stroke="{GREEN}" stroke-width="2"/>
    <text x="360" y="58" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="800" fill="{GREEN}">比 GPT-4o 便宜 10-20 倍</text>
  </g>
</svg>'''
    (ROOT / "deepseek-card-4-pricing.svg").write_text(svg)
    CARDS.append("deepseek-card-4-pricing.svg")


def card_5_tips():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="100" cy="100" r="70" fill="{RED_LIGHT}" opacity="0.4"/>
  <circle cx="720" cy="720" r="60" fill="{BLUE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{RED_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">📌 避坑提醒</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="120" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="120" rx="7" fill="{RED}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">❌ 密钥别传 GitHub</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">加 .gitignore 或环境变量</text>
  </g>

  <g transform="translate(40, 330)">
    <rect x="0" y="0" width="720" height="120" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="120" rx="7" fill="{BLUE}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">✅ 余额用完需充值</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">去 Billing 页面充值续费</text>
  </g>

  <g transform="translate(40, 480)">
    <rect x="0" y="0" width="720" height="120" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="120" rx="7" fill="{GREEN}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">✅ 兼容 OpenAI SDK</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">改 base_url 即可无缝迁移</text>
  </g>

  <g transform="translate(40, 630)">
    <rect x="0" y="0" width="720" height="120" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="120" rx="7" fill="{PURPLE}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">✅ 支持多种语言</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">cURL / Python / JavaScript 都能调</text>
  </g>
</svg>'''
    (ROOT / "deepseek-card-5-tips.svg").write_text(svg)
    CARDS.append("deepseek-card-5-tips.svg")


def main():
    card_cover()
    card_1_signup()
    card_2_apikey()
    card_3_code()
    card_4_pricing()
    card_5_tips()

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
