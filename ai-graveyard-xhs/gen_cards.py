#!/usr/bin/env python3
"""Generate cards for AI Graveyard XHS post — light theme with bold dark/brand accents."""
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
RED = "#DC2626"
RED_LIGHT = "#FEE2E2"
RED_DARK = "#B91C1C"
DARK = "#0F172A"
GRAY_BORDER = "#E2E8F0"

CARDS = []


def card_cover():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    <radialGradient id="bg" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F0EAE0"/>
    </radialGradient>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#DC2626"/>
      <stop offset="50%" stop-color="#7C3AED"/>
      <stop offset="100%" stop-color="#1E293B"/>
    </linearGradient>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>

  <circle cx="120" cy="120" r="140" fill="{RED_LIGHT}" opacity="0.4"/>
  <circle cx="900" cy="180" r="100" fill="{PURPLE_LIGHT}" opacity="0.3"/>
  <circle cx="180" cy="900" r="110" fill="{PINK_LIGHT}" opacity="0.3"/>
  <circle cx="900" cy="880" r="90" fill="{BLUE_LIGHT}" opacity="0.3"/>

  <rect x="312" y="40" width="400" height="52" rx="26" fill="{RED_LIGHT}"/>
  <text x="512" y="75" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="24" font-weight="700" fill="{RED}">💀 2025-2026 关停大盘点</text>

  <text x="512" y="210" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="108" font-weight="900" fill="url(#titleGrad)">AI 产品死亡名单</text>

  <rect x="262" y="260" width="500" height="4" rx="2" fill="{RED}" opacity="0.3"/>

  <text x="512" y="340" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="36" font-weight="800" fill="{TEXT}">烧了几百亿，说没就没了</text>

  <line x1="200" y1="430" x2="824" y2="430" stroke="{GRAY_BORDER}" stroke-width="1"/>

  <text x="512" y="480" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="26" font-weight="700" fill="{TEXT_DIM}">📊 一组触目惊心的数据</text>

  <rect x="80" y="530" width="200" height="88" rx="16" fill="{RED_LIGHT}"/>
  <text x="180" y="585" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="40" font-weight="900" fill="{RED}">3800+</text>
  <text x="320" y="585" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="26" fill="{TEXT}">AI 初创在 2025 年关停</text>

  <rect x="80" y="648" width="200" height="88" rx="16" fill="{PURPLE_LIGHT}"/>
  <text x="180" y="703" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="40" font-weight="900" fill="{PURPLE}">40%</text>
  <text x="320" y="703" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="26" fill="{TEXT}">24 个月内创业失败率</text>

  <rect x="80" y="766" width="200" height="88" rx="16" fill="{PINK_LIGHT}"/>
  <text x="180" y="821" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="40" font-weight="900" fill="{PINK}">1592</text>
  <text x="320" y="821" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="26" fill="{TEXT}">个 AI 工具有墓碑</text>

  <rect x="80" y="884" width="200" height="88" rx="16" fill="{BLUE_LIGHT}"/>
  <text x="180" y="939" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="40" font-weight="900" fill="{BLUE}">25+</text>
  <text x="320" y="939" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="26" fill="{TEXT}">国产 AI 应用 2025 年停运</text>
</svg>'''
    (ROOT / "ai-graveyard-cover.svg").write_text(svg)
    CARDS.append("ai-graveyard-cover.svg")


def card_1_global():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>

  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="60" fill="{RED_LIGHT}" opacity="0.5"/>
  <circle cx="720" cy="720" r="70" fill="{PURPLE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{RED_LIGHT}"/>
  <text x="400" y="110" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">🌍 全球重磅</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#F5F0E8"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="{RED}"/>
    <text x="40" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="24" font-weight="800" fill="{TEXT}">OpenAI Sora</text>
    <text x="300" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{RED}">2026.3 关停</text>
    <text x="40" y="78" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{TEXT_DIM}">日运营成本 $1500万 / 月收入仅 $54万 / 10亿迪士尼合作泡汤</text>
  </g>

  <g transform="translate(40, 300)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#F5F0E8"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="{RED}"/>
    <text x="40" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="24" font-weight="800" fill="{TEXT}">Humane AI Pin</text>
    <text x="300" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{RED}">2025.2 关停</text>
    <text x="40" y="78" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{TEXT_DIM}">融资 $2.3亿 / 卖身 HP 仅 $1.16亿 / $699 变废铁</text>
  </g>

  <g transform="translate(40, 425)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#F5F0E8"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="{RED}"/>
    <text x="40" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="24" font-weight="800" fill="{TEXT}">Builder.ai</text>
    <text x="300" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{RED}">2025 倒闭</text>
    <text x="40" y="78" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{TEXT_DIM}">融资 $4.45亿 / "AI编程"实为印度外包 / 收入虚报 75%</text>
  </g>

  <g transform="translate(40, 550)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#F5F0E8"/>
    <rect x="0" y="0" width="14" height="100" rx="7" fill="{RED}"/>
    <text x="40" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="24" font-weight="800" fill="{TEXT}">Stability AI</text>
    <text x="300" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{RED}">2025 严重萎缩</text>
    <text x="40" y="78" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{TEXT_DIM}">CEO 辞职 / 裁员 10% / 版权诉讼 / 核心团队流失</text>
  </g>

  <g transform="translate(40, 680)">
    <rect x="0" y="0" width="720" height="80" rx="40" fill="{RED_LIGHT}"/>
    <text x="360" y="48" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{RED}">还有 Rabbit R1 · Inflection AI · Tome AI</text>
  </g>
</svg>'''
    (ROOT / "ai-graveyard-card-1-global.svg").write_text(svg)
    CARDS.append("ai-graveyard-card-1-global.svg")


def card_2_cn():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>

  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="700" cy="80" r="60" fill="{PURPLE_LIGHT}" opacity="0.5"/>
  <circle cx="80" cy="720" r="70" fill="{RED_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{PURPLE_LIGHT}"/>
  <text x="400" y="110" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">🇨🇳 国产阵亡名单</text>

  <g transform="translate(40, 170)">
    <rect x="0" y="0" width="345" height="130" rx="16" fill="#F5F0E8"/>
    <rect x="0" y="0" width="345" height="6" rx="3" fill="{RED}"/>
    <text x="20" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">冒泡鸭</text>
    <text x="200" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="14" fill="{RED}">阶跃星辰</text>
    <text x="20" y="72" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">600万下载 · AI陪伴标杆</text>
    <text x="20" y="100" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">2025.11 关停</text>
  </g>

  <g transform="translate(415, 170)">
    <rect x="0" y="0" width="345" height="130" rx="16" fill="#F5F0E8"/>
    <rect x="0" y="0" width="345" height="6" rx="3" fill="{PURPLE}"/>
    <text x="20" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">鹿班</text>
    <text x="200" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="14" fill="{PURPLE}">阿里</text>
    <text x="20" y="72" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">电商AI设计平台</text>
    <text x="20" y="100" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">2025.6 停服</text>
  </g>

  <g transform="translate(40, 325)">
    <rect x="0" y="0" width="345" height="130" rx="16" fill="#F5F0E8"/>
    <rect x="0" y="0" width="345" height="6" rx="3" fill="{PINK}"/>
    <text x="20" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">腾讯智影</text>
    <text x="200" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="14" fill="{PINK}">腾讯</text>
    <text x="20" y="72" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">AI视频 + 数字人</text>
    <text x="20" y="100" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">2025.6 清空用户数据</text>
  </g>

  <g transform="translate(415, 325)">
    <rect x="0" y="0" width="345" height="130" rx="16" fill="#F5F0E8"/>
    <rect x="0" y="0" width="345" height="6" rx="3" fill="{BLUE}"/>
    <text x="20" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">小悟空</text>
    <text x="200" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="14" fill="{BLUE}">字节</text>
    <text x="20" y="72" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">200+AI工具 · 200万下载</text>
    <text x="20" y="100" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">2025 整合下架</text>
  </g>

  <g transform="translate(40, 480)">
    <rect x="0" y="0" width="345" height="130" rx="16" fill="#F5F0E8"/>
    <rect x="0" y="0" width="345" height="6" rx="3" fill="{GREEN}"/>
    <text x="20" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">奇域AI</text>
    <text x="200" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="14" fill="{GREEN}">小红书</text>
    <text x="20" y="72" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">国风AI绘图</text>
    <text x="20" y="100" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">2025.6 版权诉讼下关停</text>
  </g>

  <g transform="translate(415, 480)">
    <rect x="0" y="0" width="345" height="130" rx="16" fill="#F5F0E8"/>
    <rect x="0" y="0" width="345" height="6" rx="3" fill="{ORANGE}"/>
    <text x="20" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">Wow AI</text>
    <text x="200" y="42" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="14" fill="{ORANGE}">美团</text>
    <text x="20" y="72" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">AI聊天App</text>
    <text x="20" y="100" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="15" fill="{TEXT_DIM}">2025.12 关服</text>
  </g>

  <g transform="translate(40, 640)">
    <rect x="0" y="0" width="720" height="120" rx="20" fill="#F5F0E8"/>
    <text x="360" y="42" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="18" font-weight="700" fill="{TEXT_DIM}">还有这些也凉了</text>
    <line x1="60" y1="62" x2="660" y2="62" stroke="{GRAY_BORDER}" stroke-width="1"/>
    <text x="360" y="92" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{TEXT_DIM}">XEVA · 异世界回响 · 腾讯翻译君 · 讯飞写作 · Lumi噜米 · 百度脑图</text>
  </g>
</svg>'''
    (ROOT / "ai-graveyard-card-2-cn.svg").write_text(svg)
    CARDS.append("ai-graveyard-card-2-cn.svg")


def card_3_death_reasons():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>

  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="60" fill="{BLUE_LIGHT}" opacity="0.5"/>
  <circle cx="720" cy="720" r="60" fill="{RED_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{RED_LIGHT}"/>
  <text x="400" y="110" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="48" font-weight="900" fill="{RED}">💀 三大死因</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="720" height="155" rx="20" fill="#F5F0E8"/>
    <rect x="0" y="0" width="14" height="155" rx="7" fill="{RED}"/>
    <text x="40" y="48" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="28" font-weight="800" fill="{RED}">死因 1：薄包装，没护城河</text>
    <text x="40" y="88" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">套壳 GPT API + 漂亮 UI = 你的全部竞争力</text>
    <text x="40" y="118" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">大模型一迭代，你的存在理由就少一分</text>
    <text x="40" y="148" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">写作、图像、聊天 — 这三个赛道死得最多</text>
  </g>

  <g transform="translate(40, 360)">
    <rect x="0" y="0" width="720" height="155" rx="20" fill="#F5F0E8"/>
    <rect x="0" y="0" width="14" height="155" rx="7" fill="{PURPLE}"/>
    <text x="40" y="48" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="28" font-weight="800" fill="{PURPLE}">死因 2：商业化失败</text>
    <text x="40" y="88" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">免费获客 → 烧钱运营 → 无法变现</text>
    <text x="40" y="118" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">陪伴类 AI 尤其惨：流量高、留存低、转化更低</text>
    <text x="40" y="148" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">2025 年至少 8 个 AI 陪伴产品集中阵亡</text>
  </g>

  <g transform="translate(40, 545)">
    <rect x="0" y="0" width="720" height="155" rx="20" fill="#F5F0E8"/>
    <rect x="0" y="0" width="14" height="155" rx="7" fill="{PINK}"/>
    <text x="40" y="48" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="28" font-weight="800" fill="{PINK}">死因 3：大厂收缩时被放弃</text>
    <text x="40" y="88" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">字节关停十余款应用，百度清理工具产品</text>
    <text x="40" y="118" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">OpenAI 砍掉 Sora，阿里关停鹿班</text>
    <text x="40" y="148" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="17" fill="{TEXT_DIM}">做减法正在取代做加法成为主旋律</text>
  </g>

  <g transform="translate(40, 730)">
    <rect x="0" y="0" width="720" height="40" rx="20" fill="{RED_LIGHT}"/>
    <text x="360" y="27" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" font-weight="700" fill="{RED}">没有护城河的产品，终将成为 AI 时代的墓碑</text>
  </g>
</svg>'''
    (ROOT / "ai-graveyard-card-3-death-reasons.svg").write_text(svg)
    CARDS.append("ai-graveyard-card-3-death-reasons.svg")


def card_4_survivors():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>

  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="60" fill="{GREEN_LIGHT}" opacity="0.5"/>
  <circle cx="720" cy="720" r="60" fill="{BLUE_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{GREEN_LIGHT}"/>
  <text x="400" y="110" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">🏆 谁活下来了？</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="345" height="70" rx="16" fill="#F5F0E8"/>
    <text x="20" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">Cursor</text>
    <text x="100" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{GREEN}">AI编程 · 幸存</text>
  </g>
  <g transform="translate(415, 175)">
    <rect x="0" y="0" width="345" height="70" rx="16" fill="#F5F0E8"/>
    <text x="20" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">GitHub Copilot</text>
    <text x="180" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{BLUE}">AI编程 · 幸存</text>
  </g>

  <g transform="translate(40, 270)">
    <rect x="0" y="0" width="345" height="70" rx="16" fill="#F5F0E8"/>
    <text x="20" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">ChatGPT</text>
    <text x="120" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{GREEN}">超级平台 · 幸存</text>
  </g>
  <g transform="translate(415, 270)">
    <rect x="0" y="0" width="345" height="70" rx="16" fill="#F5F0E8"/>
    <text x="20" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">Claude</text>
    <text x="100" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{PURPLE}">深度推理 · 幸存</text>
  </g>

  <g transform="translate(40, 365)">
    <rect x="0" y="0" width="345" height="70" rx="16" fill="#F5F0E8"/>
    <text x="20" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">Midjourney</text>
    <text x="150" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{GREEN}">图像 · 幸存</text>
  </g>
  <g transform="translate(415, 365)">
    <rect x="0" y="0" width="345" height="70" rx="16" fill="#F5F0E8"/>
    <text x="20" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">Perplexity</text>
    <text x="140" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{BLUE}">AI搜索 · 幸存</text>
  </g>

  <g transform="translate(40, 460)">
    <rect x="0" y="0" width="720" height="70" rx="16" fill="#F5F0E8"/>
    <text x="20" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{TEXT}">豆包 · DeepSeek · Notion AI · Grammarly</text>
    <text x="580" y="45" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{GREEN}">··· 幸存</text>
  </g>

  <g transform="translate(40, 565)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="#F5F0E8"/>
    <text x="360" y="42" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">它们做对了什么？</text>
    <line x1="60" y1="62" x2="660" y2="62" stroke="{GRAY_BORDER}" stroke-width="1"/>
    <text x="360" y="88" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="16" fill="{TEXT_DIM}">不是薄包装 · 嵌入用户工作流 · 有数据飞轮</text>
  </g>

  <g transform="translate(40, 695)">
    <rect x="0" y="0" width="720" height="70" rx="35" fill="{RED_LIGHT}"/>
    <text x="360" y="43" text-anchor="middle" font-family="PingFang SC, Microsoft YaHei, sans-serif" font-size="22" font-weight="800" fill="{RED}">💡 结论：做产品，别做 API 皮肤</text>
  </g>
</svg>'''
    (ROOT / "ai-graveyard-card-4-survivors.svg").write_text(svg)
    CARDS.append("ai-graveyard-card-4-survivors.svg")


def main():
    card_cover()
    card_1_global()
    card_2_cn()
    card_3_death_reasons()
    card_4_survivors()

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
