#!/usr/bin/env python3
"""Generate 5 LIGHT (cream/white) viral-style cards for MCP XHS post.
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
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>

  <circle cx="120" cy="120" r="140" fill="{BLUE_LIGHT}" opacity="0.4"/>
  <circle cx="880" cy="180" r="100" fill="{PURPLE_LIGHT}" opacity="0.4"/>
  <circle cx="160" cy="880" r="110" fill="{PINK_LIGHT}" opacity="0.3"/>
  <circle cx="900" cy="850" r="90" fill="{INDIGO_LIGHT}" opacity="0.3"/>

  <rect x="62" y="60" width="900" height="160" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="120" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="700" fill="{BLUE}">🔌 AI 圈的 USB-C 标准</text>
  <text x="512" y="190" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="76" font-weight="900" fill="url(#titleG)" filter="url(#glow)">MCP 是什么？</text>

  <rect x="112" y="260" width="800" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="313" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="800" fill="{TEXT}">Model Context Protocol 完全解读</text>

  <g transform="translate(112, 380)">
    <rect x="0" y="0" width="800" height="560" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT_DIM}">📋 为什么 MCP 刷屏了？</text>
    <line x1="50" y1="80" x2="750" y2="80" stroke="#E2E8F0" stroke-width="1"/>

    <g transform="translate(40, 105)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{BLUE_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{BLUE}">Anthropic 发布</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{BLUE_DARK}">2024.11 正式开源</text>
    </g>
    <g transform="translate(420, 105)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{PURPLE_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{PURPLE}">业界统一</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{PURPLE}">OpenAI &amp; Google 均已支持</text>
    </g>

    <g transform="translate(40, 235)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{GREEN_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{GREEN}">10,000+ 服务器</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{GREEN}">MCP 生态爆发式增长</text>
    </g>
    <g transform="translate(420, 235)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{PINK_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{PINK}">捐赠 Linux 基金会</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{PINK}">成为中立行业标准</text>
    </g>

    <text x="400" y="420" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" line-height="1.6" fill="{TEXT_DIM}">AI Agent 时代的"基础设施协议"</text>
    <text x="400" y="455" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{BLUE}">不了解 MCP = 错过 AI 下一波浪潮 🌊</text>

    <rect x="200" y="490" width="400" height="50" rx="25" fill="{INDIGO_LIGHT}"/>
    <text x="400" y="522" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{INDIGO}">modelcontextprotocol.io</text>
  </g>

  <text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{BLUE}">#MCP #ModelContextProtocol #AI协议 #AIAgent</text>
</svg>'''
    (ROOT / "mcp-cover.svg").write_text(svg)
    CARDS.append("mcp-cover.svg")


def card_1_problem():
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
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">❌ 没有 MCP 的世界</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="110" rx="7" fill="{RED}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">🔧 每个工具都要写自定义集成</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">数据库、API、文件系统…每种对接方式不同</text>
  </g>

  <g transform="translate(40, 320)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="110" rx="7" fill="{RED}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">🧩 N × M 维护噩梦</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">N 个模型 × M 个工具 = N×M 个集成</text>
  </g>

  <g transform="translate(40, 460)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="110" rx="7" fill="{RED}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">🚫 AI 被隔离在数据孤岛</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">再强的大模型也拿不到实时业务数据</text>
  </g>

  <g transform="translate(40, 620)">
    <rect x="0" y="0" width="720" height="60" rx="30" fill="{RED_LIGHT}" stroke="{RED}" stroke-width="2"/>
    <text x="360" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED}">每个 AI 项目都在"重复造轮子"</text>
  </g>

  <g transform="translate(40, 720)">
    <rect x="0" y="0" width="720" height="50" rx="25" fill="{BLUE_LIGHT}"/>
    <text x="360" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{BLUE}">MCP 就是来终结这种混乱的 ✅</text>
  </g>
</svg>'''
    (ROOT / "mcp-card-1-problem.svg").write_text(svg)
    CARDS.append("mcp-card-1-problem.svg")


def card_2_what():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <linearGradient id="bigG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#7C3AED"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <circle cx="700" cy="80" r="60" fill="{BLUE_LIGHT}" opacity="0.4"/>
  <circle cx="80" cy="720" r="50" fill="{PURPLE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{BLUE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">✅ MCP = AI 的 USB-C</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="170" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="360" y="50" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="url(#bigG)" filter="url(#glow)">Model Context Protocol</text>
    <text x="40" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT}">由 Anthropic 于 2024.11 发布的开源标准</text>
    <text x="40" y="130" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT}">JSON-RPC 2.0 协议，统一 AI ↔ 工具 连接</text>
    <text x="40" y="163" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">一个协议 = 无限兼容，告别碎片化集成</text>
  </g>

  <g transform="translate(40, 390)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{BLUE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{BLUE}">&#x1F50C; 统一标准</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">一个协议对接所有工具</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">M + N 代替 M×N</text>
  </g>

  <g transform="translate(420, 390)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PURPLE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PURPLE}">🔧 三原语</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Tools · Resources · Prompts</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">覆盖所有交互场景</text>
  </g>

  <g transform="translate(40, 590)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{GREEN_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{GREEN}">&#x1F512; 安全可控</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">每个工具声明权限和参数</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">模型按规则调用</text>
  </g>

  <g transform="translate(420, 590)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PINK_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PINK}">&#x1F310; 厂商中立</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">捐赠给 Linux 基金会</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">开放、免费、无锁</text>
  </g>
</svg>'''
    (ROOT / "mcp-card-2-what.svg").write_text(svg)
    CARDS.append("mcp-card-2-what.svg")


def card_3_how():
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

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{GREEN_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">⚙️ MCP 怎么工作</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{BLUE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">1</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">MCP Host（AI 应用）发起连接</text>
  </g>

  <g transform="translate(40, 285)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{PURPLE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">2</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">MCP Client 发现可用工具</text>
  </g>

  <g transform="translate(40, 390)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{PINK}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">3</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">MCP Server 暴露工具 &amp; 资源</text>
  </g>

  <g transform="translate(40, 495)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{GREEN}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">4</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">LLM 自动选择调用合适工具</text>
  </g>

  <g transform="translate(40, 600)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{ORANGE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">5</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">数据通过 JSON-RPC 双向传输</text>
  </g>

  <g transform="translate(40, 720)">
    <rect x="0" y="0" width="720" height="50" rx="25" fill="{BLUE_LIGHT}"/>
    <text x="360" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{BLUE}">传输层：stdio / SSE / HTTP 灵活切换</text>
  </g>
</svg>'''
    (ROOT / "mcp-card-3-how.svg").write_text(svg)
    CARDS.append("mcp-card-3-how.svg")


def card_4_adoption():
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

  <circle cx="80" cy="80" r="70" fill="{ORANGE_LIGHT}" opacity="0.5"/>
  <circle cx="720" cy="720" r="60" fill="{PURPLE_LIGHT}" opacity="0.3"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{ORANGE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">🚀 MCP 生态爆发</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{TEXT}">164M+ 月下载量</text>
    <text x="680" y="55" text-anchor="end" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" fill="{BLUE}">📈 爆炸增长</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Python SDK 月下载量 (2026.04)</text>
  </g>

  <g transform="translate(40, 295)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{TEXT}">10,000+ 服务器</text>
    <text x="680" y="55" text-anchor="end" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" fill="{GREEN}">🌐 全球覆盖</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">覆盖数据库、SaaS、开发工具等</text>
  </g>

  <g transform="translate(40, 410)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{TEXT}">全厂商支持</text>
    <text x="680" y="55" text-anchor="end" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" fill="{PURPLE}">🤝 统一标准</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Anthropic · OpenAI · Google · Microsoft · AWS</text>
  </g>

  <g transform="translate(40, 525)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{TEXT}">SDK 覆盖 4 大语言</text>
    <text x="680" y="55" text-anchor="end" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" fill="{ORANGE}">💻 全栈可用</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Python · TypeScript · Java · C#</text>
  </g>

  <g transform="translate(40, 650)">
    <rect x="0" y="0" width="720" height="100" rx="50" fill="{INDIGO_LIGHT}" stroke="{INDIGO}" stroke-width="2"/>
    <text x="360" y="58" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{INDIGO}">已经被捐赠给 Linux 基金会，永不锁死</text>
  </g>
</svg>'''
    (ROOT / "mcp-card-4-adoption.svg").write_text(svg)
    CARDS.append("mcp-card-4-adoption.svg")


def main():
    card_cover()
    card_1_problem()
    card_2_what()
    card_3_how()
    card_4_adoption()

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
