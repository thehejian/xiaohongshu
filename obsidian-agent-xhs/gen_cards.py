#!/usr/bin/env python3
"""Generate 8 cards: 4 Chinese light + 4 English dark for Obsidian+AI Agent post."""
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

DARK_BG = "#0B1027"
DARK_CARD = "#141B33"
DARK_TEXT = "#E2E8F0"
DARK_DIM = "#8892B0"
DARK_ACCENT = "#60A5FA"

CARDS = []


def zh_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </radialGradient>
    <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="40%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="#1E293B" flood-opacity="0.10"/>
    </filter>
    <filter id="glowBlue" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <rect x="62" y="40" width="900" height="110" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{BLUE}">🧠 第二大脑 × AI 管家的真相</text>
  <text x="512" y="220" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="96" font-weight="900" fill="url(#titleG)">Obsidian + AI</text>
  <text x="512" y="320" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="64" font-weight="900" fill="url(#titleG)">真有搞头</text>
  <rect x="162" y="370" width="700" height="70" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="416" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{TEXT}">一篇说清背后的逻辑与生态</text>
  <g transform="translate(112, 480)">
    <rect x="0" y="0" width="800" height="460" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT_DIM}">📊 四大信号告诉你答案</text>
    <line x1="50" y1="80" x2="750" y2="80" stroke="#E2E8F0" stroke-width="1"/>
    <g transform="translate(40, 105)">
      <rect x="0" y="0" width="340" height="80" rx="16" fill="{BLUE_LIGHT}"/>
      <text x="170" y="32" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{BLUE}">CLI 打通</text>
      <text x="170" y="62" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{BLUE_DARK}">搜索快 grep 54 倍</text>
    </g>
    <g transform="translate(420, 105)">
      <rect x="0" y="0" width="340" height="80" rx="16" fill="{PURPLE_LIGHT}"/>
      <text x="170" y="32" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{PURPLE}">MCP 桥梁</text>
      <text x="170" y="62" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{PURPLE}">AI 原生读写 vault</text>
    </g>
    <g transform="translate(40, 215)">
      <rect x="0" y="0" width="340" height="80" rx="16" fill="{GREEN_LIGHT}"/>
      <text x="170" y="32" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{GREEN}">Agents Read</text>
      <text x="170" y="62" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{GREEN}">AI 读、人类写</text>
    </g>
    <g transform="translate(420, 215)">
      <rect x="0" y="0" width="340" height="80" rx="16" fill="{PINK_LIGHT}"/>
      <text x="170" y="32" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{PINK}">生态爆发</text>
      <text x="170" y="62" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{PINK}">6+ 插件的集群效应</text>
    </g>
    <rect x="100" y="330" width="600" height="50" rx="25" fill="{INDIGO_LIGHT}"/>
    <text x="400" y="362" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{INDIGO}">AI 不该在笔记里聊天，该安静递材料</text>
    <text x="400" y="420" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{BLUE}">Obsidian 不是被 AI 替代，是被激活 🔋</text>
  </g>
  <text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{BLUE}">#Obsidian #AI #第二大脑 #知识管理</text>
</svg>'''
    (ROOT / "oa-cover-zh.svg").write_text(svg)
    CARDS.append(("oa-cover-zh.svg", 1024))


def zh_card_1_pain():
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
  <circle cx="720" cy="720" r="60" fill="{BLUE_LIGHT}" opacity="0.3"/>
  <rect x="40" y="40" width="720" height="100" rx="50" fill="{RED_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">你的笔记还是死笔记</text>
  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="110" rx="7" fill="{RED}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">📝 写了 5000 条笔记却没人读</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">知识库变成了"数字坟墓"，只进不出</text>
  </g>
  <g transform="translate(40, 320)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="110" rx="7" fill="{RED}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">🔌 AI 碰不到你的本地笔记</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">每次都要手动复制粘贴到对话窗口</text>
  </g>
  <g transform="translate(40, 460)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="110" rx="7" fill="{RED}"/>
    <text x="40" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">🧩 插件插件一堆，各玩各的</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">Copilot · SmartConnections · 但没有统一入口</text>
  </g>
  <g transform="translate(40, 620)">
    <rect x="0" y="0" width="720" height="60" rx="30" fill="{RED_LIGHT}" stroke="{RED}" stroke-width="2"/>
    <text x="360" y="38" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{RED}">你的"第二大脑"缺了颗 AI 心脏</text>
  </g>
  <g transform="translate(40, 720)">
    <rect x="0" y="0" width="720" height="50" rx="25" fill="{BLUE_LIGHT}"/>
    <text x="360" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{BLUE}">好消息：2026 年一切都变了 ✅</text>
  </g>
</svg>'''
    (ROOT / "oa-card-1-zh.svg").write_text(svg)
    CARDS.append(("oa-card-1-zh.svg", 800))


def zh_card_2_solution():
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
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="700" cy="80" r="60" fill="{GREEN_LIGHT}" opacity="0.4"/>
  <circle cx="80" cy="720" r="50" fill="{PURPLE_LIGHT}" opacity="0.4"/>
  <rect x="40" y="40" width="720" height="100" rx="50" fill="{GREEN_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">AI 管家接管第二大脑</text>
  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="170" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="360" y="50" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="url(#bigG)">Agents Read, Humans Write</text>
    <text x="40" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT}">AI 读取你的 vault 做语义搜索、联想</text>
    <text x="40" y="130" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT}">但从不替你写——思考权永远在你手上</text>
    <text x="40" y="163" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">这才是 AI × 知识管理正确的分工</text>
  </g>
  <g transform="translate(40, 390)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{BLUE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{BLUE}">CLI 打通</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Obsidian 1.12 CLI 发布</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">搜索比 grep 快 54 倍</text>
    <text x="20" y="140" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Agent 原生读写 vault</text>
  </g>
  <g transform="translate(420, 390)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PURPLE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PURPLE}">MCP 桥梁</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">obsidian-claude-code-mcp</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">WebSocket 桥接</text>
    <text x="20" y="140" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">无需 symlink 或 cd</text>
  </g>
  <g transform="translate(40, 590)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{GREEN_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{GREEN}">QMD 同步</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Claude 会话自动导出</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">关闭即写回 vault</text>
    <text x="20" y="140" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">token 减少 60%+</text>
  </g>
  <g transform="translate(420, 590)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PINK_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PINK}">生态集群</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Copilot · SmartConnections</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Claudian · Agent Client</text>
    <text x="20" y="140" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">全场景覆盖</text>
  </g>
</svg>'''
    (ROOT / "oa-card-2-zh.svg").write_text(svg)
    CARDS.append(("oa-card-2-zh.svg", 800))


def zh_card_3_data():
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
  <circle cx="80" cy="80" r="70" fill="{BLUE_LIGHT}" opacity="0.5"/>
  <circle cx="720" cy="720" r="60" fill="{ORANGE_LIGHT}" opacity="0.3"/>
  <rect x="40" y="40" width="720" height="100" rx="50" fill="{BLUE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">三组数据告诉你答案</text>
  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="32" font-weight="800" fill="{BLUE}">54x</text>
    <text x="160" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">CLI 搜索速度 vs grep</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">4663 文件、16GB vault 实测：0.26s vs 15.6s</text>
    <text x="40" y="105" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}" font-style="italic">来源: @drrobcincotta</text>
  </g>
  <g transform="translate(40, 320)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="32" font-weight="800" fill="{PURPLE}">60%+</text>
    <text x="190" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">Token 用量降低</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">QMD 方案实测：上下文效率大幅提升</text>
    <text x="40" y="105" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}" font-style="italic">来源: Kevin Lee / Shopify CEO 团队</text>
  </g>
  <g transform="translate(40, 460)">
    <rect x="0" y="0" width="720" height="110" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="32" font-weight="800" fill="{GREEN}">6+</text>
    <text x="150" y="55" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">AI 插件集群</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Copilot · Smart Connections · Claudian · Agent Client · Claude Sidebar · Nexus</text>
  </g>
  <g transform="translate(40, 620)">
    <rect x="0" y="0" width="720" height="100" rx="50" fill="{INDIGO_LIGHT}" stroke="{INDIGO}" stroke-width="2"/>
    <text x="360" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{INDIGO}">基础设施就位，生态已经爆发</text>
    <text x="360" y="80" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">现在上车，时机刚好 🚀</text>
  </g>
</svg>'''
    (ROOT / "oa-card-3-zh.svg").write_text(svg)
    CARDS.append(("oa-card-3-zh.svg", 800))


def en_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="#0B1027"/>
    </radialGradient>
    <linearGradient id="titleG" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#60A5FA"/>
      <stop offset="50%" stop-color="#A78BFA"/>
      <stop offset="100%" stop-color="#F472B6"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="#000" flood-opacity="0.30"/>
    </filter>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <circle cx="120" cy="120" r="140" fill="#1E3A5F" opacity="0.3"/>
  <circle cx="880" cy="180" r="100" fill="#3B1F6E" opacity="0.3"/>
  <circle cx="160" cy="880" r="110" fill="#5F1E4A" opacity="0.2"/>
  <circle cx="900" cy="850" r="90" fill="#1E3A5F" opacity="0.2"/>
  <rect x="62" y="40" width="900" height="110" rx="40" fill="#1A2340" filter="url(#shadow)"/>
  <text x="512" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="#60A5FA">🧠 Your Second Brain Just Got a Brain</text>
  <text x="512" y="230" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="80" font-weight="900" fill="url(#titleG)">Obsidian + AI</text>
  <text x="512" y="330" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="52" font-weight="900" fill="url(#titleG)">Overhyped or Underrated?</text>
  <rect x="162" y="380" width="700" height="70" rx="20" fill="#1A2340" filter="url(#shadow)"/>
  <text x="512" y="426" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="800" fill="{DARK_TEXT}">The real story behind the hype</text>
  <g transform="translate(112, 490)">
    <rect x="0" y="0" width="800" height="440" rx="30" fill="#1A2340" filter="url(#shadow)"/>
    <text x="400" y="50" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_DIM}">Why now? 4 signals converging</text>
    <line x1="50" y1="75" x2="750" y2="75" stroke="#2A3A5F" stroke-width="1"/>
    <g transform="translate(40, 100)">
      <rect x="0" y="0" width="340" height="70" rx="16" fill="#1E3A5F"/>
      <text x="170" y="30" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#60A5FA">CLI Released</text>
      <text x="170" y="57" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="#8892B0">54x faster than grep</text>
    </g>
    <g transform="translate(420, 100)">
      <rect x="0" y="0" width="340" height="70" rx="16" fill="#3B1F6E"/>
      <text x="170" y="30" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#A78BFA">MCP Bridges</text>
      <text x="170" y="57" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="#8892B0">Native vault access</text>
    </g>
    <g transform="translate(40, 200)">
      <rect x="0" y="0" width="340" height="70" rx="16" fill="#1E4A3A"/>
      <text x="170" y="30" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#34D399">Agents Read</text>
      <text x="170" y="57" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="#8892B0">Humans write, AI reads</text>
    </g>
    <g transform="translate(420, 200)">
      <rect x="0" y="0" width="340" height="70" rx="16" fill="#5F1E4A"/>
      <text x="170" y="30" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#F472B6">Ecosystem Boom</text>
      <text x="170" y="57" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="#8892B0">6+ plugins, growing fast</text>
    </g>
    <rect x="100" y="310" width="600" height="50" rx="25" fill="#60A5FA" opacity="0.15"/>
    <text x="400" y="342" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="#60A5FA">AI shouldn't chat in your notes — it should serve them</text>
    <text x="400" y="400" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="700" fill="#A78BFA">Obsidian isn't replaced — it's unlocked 🔓</text>
  </g>
  <text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="#60A5FA">#Obsidian #AIAgent #SecondBrain #PKM</text>
</svg>'''
    (ROOT / "oa-cover-en.svg").write_text(svg)
    CARDS.append(("oa-cover-en.svg", 1024))


def en_card_1_philosophy():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="#0B1027"/>
    </radialGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.30"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="700" cy="80" r="60" fill="#3B1F6E" opacity="0.4"/>
  <circle cx="80" cy="720" r="50" fill="#1E3A5F" opacity="0.4"/>
  <rect x="40" y="40" width="720" height="100" rx="50" fill="#1E3A5F" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="44" font-weight="900" fill="{DARK_TEXT}">Agents Read, Humans Write</text>
  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="130" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <text x="360" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="800" fill="#60A5FA">The Golden Rule</text>
    <text x="40" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{DARK_TEXT}">AI reads your vault for context</text>
    <text x="40" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{DARK_TEXT}">But never writes into it</text>
    <text x="40" y="125" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="14" fill="{DARK_DIM}">— Greg Isenberg / InternetVin</text>
  </g>
  <g transform="translate(40, 340)">
    <rect x="0" y="0" width="340" height="180" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <text x="20" y="35" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#34D399">/my-world</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">AI reads your vault</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">to understand who you are</text>
  </g>
  <g transform="translate(420, 340)">
    <rect x="0" y="0" width="340" height="180" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <text x="20" y="35" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#F472B6">/today</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">AI pulls context from</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">today's notes and tasks</text>
  </g>
  <g transform="translate(40, 550)">
    <rect x="0" y="0" width="340" height="180" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <text x="20" y="35" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#A78BFA">/close</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">Auto-saves session context</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">back to your vault</text>
  </g>
  <g transform="translate(420, 550)">
    <rect x="0" y="0" width="340" height="180" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <text x="20" y="35" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#F59E0B">/trace</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">Trace back your</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">chain of thought</text>
  </g>
</svg>'''
    (ROOT / "oa-card-1-en.svg").write_text(svg)
    CARDS.append(("oa-card-1-en.svg", 800))


def en_card_2_architecture():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="#0B1027"/>
    </radialGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.30"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="70" fill="#1E3A5F" opacity="0.4"/>
  <circle cx="720" cy="720" r="60" fill="#3B1F6E" opacity="0.4"/>
  <rect x="40" y="40" width="720" height="100" rx="50" fill="#3B1F6E" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="44" font-weight="900" fill="{DARK_TEXT}">How It Works</text>
  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <circle cx="40" cy="45" r="22" fill="#60A5FA"/>
    <text x="40" y="51" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">1</text>
    <text x="80" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_TEXT}">Obsidian CLI — 54x faster than grep</text>
    <text x="80" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{DARK_DIM}">Native vault search from any Agent</text>
  </g>
  <g transform="translate(40, 290)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <circle cx="40" cy="45" r="22" fill="#A78BFA"/>
    <text x="40" y="51" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">2</text>
    <text x="80" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_TEXT}">MCP Server connects the dots</text>
    <text x="80" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{DARK_DIM}">WebSocket bridge, no symlink needed</text>
  </g>
  <g transform="translate(40, 405)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <circle cx="40" cy="45" r="22" fill="#34D399"/>
    <text x="40" y="51" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">3</text>
    <text x="80" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_TEXT}">QMD syncs sessions to vault</text>
    <text x="80" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{DARK_DIM}">Claude output -> markdown, 60% token saved</text>
  </g>
  <g transform="translate(40, 520)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <circle cx="40" cy="45" r="22" fill="#F472B6"/>
    <text x="40" y="51" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">4</text>
    <text x="80" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{DARK_TEXT}">Agent uses vault as memory</text>
    <text x="80" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{DARK_DIM}">Semantic search + link suggestions + recall</text>
  </g>
  <g transform="translate(40, 650)">
    <rect x="0" y="0" width="720" height="100" rx="50" fill="#60A5FA" opacity="0.1" stroke="#60A5FA" stroke-width="2"/>
    <text x="360" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#60A5FA">CLI + MCP + QMD = The Trinity</text>
    <text x="360" y="78" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">Three tools, one seamless workflow</text>
  </g>
</svg>'''
    (ROOT / "oa-card-2-en.svg").write_text(svg)
    CARDS.append(("oa-card-2-en.svg", 800))


def en_card_3_verdict():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="75%">
      <stop offset="0%" stop-color="#141B33"/>
      <stop offset="100%" stop-color="#0B1027"/>
    </radialGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.30"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="70" fill="#1E3A5F" opacity="0.5"/>
  <circle cx="720" cy="720" r="60" fill="#3B1F6E" opacity="0.4"/>
  <rect x="40" y="40" width="720" height="100" rx="50" fill="#1E3A5F" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{DARK_TEXT}">The Verdict</text>
  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="#34D399"/>
    <text x="40" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_TEXT}">The chat-in-sidepanel was wrong</text>
    <text x="40" y="72" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">Community rejected AI-as-chatbot in the vault</text>
  </g>
  <g transform="translate(40, 310)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="#60A5FA"/>
    <text x="40" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_TEXT}">The winner: invisible background agent</text>
    <text x="40" y="72" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">Semantic search, link suggestions, session recall</text>
  </g>
  <g transform="translate(40, 440)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="#A78BFA"/>
    <text x="40" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_TEXT}">Infrastructure is ready</text>
    <text x="40" y="72" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">CLI + MCP + QMD = production-ready pipeline</text>
  </g>
  <g transform="translate(40, 570)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#1A2340" filter="url(#shadow)"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="#F472B6"/>
    <text x="40" y="40" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{DARK_TEXT}">Obsidian isn't replaced — it's unlocked</text>
    <text x="40" y="72" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{DARK_DIM}">The killer app hasn't shipped yet. It will.</text>
  </g>
  <g transform="translate(40, 720)">
    <rect x="0" y="0" width="720" height="50" rx="25" fill="#60A5FA" opacity="0.15"/>
    <text x="360" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="#60A5FA">Yes, 有搞头 — and you're early enough to ride it</text>
  </g>
</svg>'''
    (ROOT / "oa-card-3-en.svg").write_text(svg)
    CARDS.append(("oa-card-3-en.svg", 800))


def main():
    zh_cover()
    zh_card_1_pain()
    zh_card_2_solution()
    zh_card_3_data()
    en_cover()
    en_card_1_philosophy()
    en_card_2_architecture()
    en_card_3_verdict()

    print(f"Generated {len(CARDS)} SVGs")
    for name, size in CARDS:
        png = name.replace(".svg", ".png")
        subprocess.run([
            "inkscape", str(ROOT / name),
            "-o", str(ROOT / png),
            "-w", str(size), "-h", str(size)
        ], check=True)
        print(f"  OK {png}")


if __name__ == "__main__":
    main()
