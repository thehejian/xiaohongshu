#!/usr/bin/env python3
"""Generate 5 LIGHT (cream/white) viral-style cards for Zhejiang 取消中考 XHS post."""
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
      <stop offset="50%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="16" flood-color="#1E293B" flood-opacity="0.10"/>
    </filter>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>

  <circle cx="120" cy="120" r="140" fill="{BLUE_LIGHT}" opacity="0.4"/>
  <circle cx="880" cy="180" r="100" fill="{GREEN_LIGHT}" opacity="0.4"/>
  <circle cx="160" cy="880" r="110" fill="{ORANGE_LIGHT}" opacity="0.3"/>
  <circle cx="900" cy="850" r="90" fill="{PURPLE_LIGHT}" opacity="0.3"/>

  <rect x="62" y="40" width="900" height="110" rx="40" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="95" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="26" font-weight="700" fill="{BLUE}">&#x1F4F0; 冲上热搜的教育改革</text>
  <text x="512" y="220" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="96" font-weight="900" fill="url(#titleG)">取消中考选拔</text>
  <text x="512" y="300" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">全员直升高中</text>

  <rect x="112" y="350" width="800" height="70" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="512" y="395" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{TEXT}">浙江舟山嵊泗县·人口仅6.5万</text>

  <g transform="translate(112, 460)">
    <rect x="0" y="0" width="800" height="500" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT_DIM}">&#x1F4AC; 一石激起千层浪</text>
    <line x1="50" y1="80" x2="750" y2="80" stroke="#E2E8F0" stroke-width="1"/>

    <g transform="translate(40, 105)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{BLUE_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{BLUE}">取消分数线</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{BLUE_DARK}">普高100%直升</text>
    </g>
    <g transform="translate(420, 105)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{GREEN_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{GREEN}">300人/年</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{GREEN}">全县初中毕业生</text>
    </g>

    <g transform="translate(40, 235)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{ORANGE_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{ORANGE}">2025年启动</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{ORANGE}">改革已实施一年</text>
    </g>
    <g transform="translate(420, 235)">
      <rect x="0" y="0" width="340" height="100" rx="16" fill="{PURPLE_LIGHT}"/>
      <text x="170" y="40" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{PURPLE}">因地制宜</text>
      <text x="170" y="72" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{PURPLE}">破解人口小县难题</text>
    </g>

    <text x="400" y="390" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT_DIM}">教育的本质不是筛选，是培养</text>

    <rect x="200" y="425" width="400" height="50" rx="25" fill="{BLUE_LIGHT}"/>
    <text x="400" y="457" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{BLUE}">你觉得这模式能推广吗？</text>
  </g>

  <text x="512" y="990" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{BLUE}">#浙江 #取消中考 #全员直升 #教育改革 #嵊泗</text>
</svg>'''
    (ROOT / "zhongkao-cover.svg").write_text(svg)
    CARDS.append("zhongkao-cover.svg")


def card_1_what():
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

  <circle cx="80" cy="80" r="70" fill="{BLUE_LIGHT}" opacity="0.4"/>
  <circle cx="720" cy="720" r="60" fill="{ORANGE_LIGHT}" opacity="0.3"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{BLUE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">&#x1F4F0; 发生了什么？</text>

  <g transform="translate(40, 180)">
    <rect x="0" y="0" width="720" height="140" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="360" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="800" fill="{BLUE}">浙江嵊泗&#xB7;取消中考选拔</text>
    <text x="40" y="85" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT}">2025年起，取消普高录取分数线</text>
    <text x="40" y="118" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">所有初中毕业生100%升入普通高中</text>
  </g>

  <g transform="translate(40, 355)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{GREEN_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{GREEN}">&#x2705; 不是取消考试</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">学生仍需参加全省中考</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">取消的是"选拔功能"</text>
  </g>

  <g transform="translate(420, 355)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{ORANGE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{ORANGE}">&#x1F3ED; 全员直升</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">通过学业水平考试即可</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">100%升入普高</text>
  </g>

  <g transform="translate(40, 550)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PURPLE_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PURPLE}">&#x1F4C5; 高一后分方向</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">高一结束后自主选择</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">文科/理科发展方向</text>
  </g>

  <g transform="translate(420, 550)">
    <rect x="0" y="0" width="340" height="160" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="50" rx="20" fill="{PINK_LIGHT}"/>
    <text x="170" y="33" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{PINK}">&#x1F4AC; 冲上热搜</text>
    <text x="20" y="80" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">2026.6.14登上热搜第一</text>
    <text x="20" y="110" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">全网讨论中</text>
  </g>

  <g transform="translate(40, 745)">
    <rect x="0" y="0" width="720" height="35" rx="17" fill="{RED_LIGHT}"/>
    <text x="360" y="24" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="700" fill="{RED}">&#x1F525; 一考定终身的模式正在被打破</text>
  </g>
</svg>'''
    (ROOT / "zhongkao-card-1-what.svg").write_text(svg)
    CARDS.append("zhongkao-card-1-what.svg")


def card_2_why():
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
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">&#x1F914; 为什么这么做？</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="50" r="24" fill="{BLUE}"/>
    <text x="40" y="58" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#FFF">1</text>
    <text x="80" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">人口仅6.5万</text>
    <text x="80" y="78" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">海岛县，位置偏远，人口持续外流</text>
  </g>

  <g transform="translate(40, 305)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="50" r="24" fill="{PURPLE}"/>
    <text x="40" y="58" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#FFF">2</text>
    <text x="80" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">每年仅300毕业生</text>
    <text x="80" y="78" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">生源连年下降，学校难以为继</text>
  </g>

  <g transform="translate(40, 435)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="50" r="24" fill="{ORANGE}"/>
    <text x="40" y="58" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#FFF">3</text>
    <text x="80" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">稳住生源是关键</text>
    <text x="80" y="78" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">取消选拔=告诉家长孩子有学上</text>
  </g>

  <g transform="translate(40, 565)">
    <rect x="0" y="0" width="720" height="100" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="50" r="24" fill="{GREEN}"/>
    <text x="40" y="58" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#FFF">4</text>
    <text x="80" y="45" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">不是一时兴起</text>
    <text x="80" y="78" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">官方：破解人口小县教育难题</text>
  </g>

  <g transform="translate(40, 700)">
    <rect x="0" y="0" width="720" height="70" rx="35" fill="{ORANGE_LIGHT}" stroke="{ORANGE}" stroke-width="2"/>
    <text x="360" y="44" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{ORANGE}">被"逼"出来的改革，也是务实的改革</text>
  </g>
</svg>'''
    (ROOT / "zhongkao-card-2-why.svg").write_text(svg)
    CARDS.append("zhongkao-card-2-why.svg")


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

  <circle cx="80" cy="80" r="70" fill="{GREEN_LIGHT}" opacity="0.4"/>
  <circle cx="720" cy="720" r="60" fill="{PURPLE_LIGHT}" opacity="0.3"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{ORANGE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">&#x1F3EB; 具体怎么操作？</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{BLUE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">1</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">参加全省统一中考</text>
  </g>

  <g transform="translate(40, 280)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{PURPLE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">2</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">取消普高录取分数线</text>
  </g>

  <g transform="translate(40, 385)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{GREEN}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">3</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">通过学业水平考试即升学</text>
  </g>

  <g transform="translate(40, 490)">
    <rect x="0" y="0" width="720" height="80" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="40" r="22" fill="{ORANGE}"/>
    <text x="40" y="48" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="#FFF">4</text>
    <text x="80" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="700" fill="{TEXT}">高一结束自主选方向</text>
  </g>

  <g transform="translate(40, 610)">
    <rect x="0" y="0" width="340" height="140" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{BLUE_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{BLUE}">&#x2714;&#xFE0F; 不变的是</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">&#x2022; 中考仍然正常进行</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">&#x2022; 教学大纲不变</text>
    <text x="20" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">&#x2022; 高考升学路径不变</text>
  </g>

  <g transform="translate(420, 610)">
    <rect x="0" y="0" width="340" height="140" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{GREEN_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{GREEN}">&#x1F195; 变的是</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">&#x2022; 取消分数线门槛</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">&#x2022; 不再一考定去向</text>
    <text x="20" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">&#x2022; 赋予学生更多选择权</text>
  </g>

  <g transform="translate(40, 775)">
    <rect x="0" y="0" width="720" height="20" rx="10" fill="{PURPLE_LIGHT}"/>
    <text x="360" y="15" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="13" font-weight="700" fill="{PURPLE}">一场考试不再决定一个孩子的命运</text>
  </g>
</svg>'''
    (ROOT / "zhongkao-card-3-how.svg").write_text(svg)
    CARDS.append("zhongkao-card-3-how.svg")


def card_4_debate():
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
  <circle cx="80" cy="720" r="50" fill="{RED_LIGHT}" opacity="0.4"/>

  <rect x="40" y="40" width="720" height="100" rx="50" fill="{PURPLE_LIGHT}" filter="url(#shadow)"/>
  <text x="400" y="108" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="48" font-weight="900" fill="{TEXT}">&#x1F91E; 争议与思考</text>

  <g transform="translate(40, 175)">
    <rect x="0" y="0" width="340" height="170" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="20" fill="{GREEN_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{GREEN}">&#x1F44D; 支持方</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">减轻初中升学焦虑</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">给每个孩子成长机会</text>
    <text x="20" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">小县城就该因地制宜</text>
    <text x="20" y="145" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">教育是为培养不是筛选</text>
  </g>

  <g transform="translate(420, 175)">
    <rect x="0" y="0" width="340" height="170" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="20" fill="{RED_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{RED}">&#x1F44E; 反对方</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">没有选拔质量如何保</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">高中内部分层是问题</text>
    <text x="20" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">其他地区能复制吗</text>
    <text x="20" y="145" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">公平和质量如何兼得</text>
  </g>

  <g transform="translate(40, 380)">
    <rect x="0" y="0" width="720" height="90" rx="20" fill="{WHITE}" filter="url(#shadow)"/>
    <text x="40" y="35" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="800" fill="{TEXT}">&#x1F4A1; 深度思考</text>
    <text x="40" y="72" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">在大城市，中考是资源分配机制。在6.5万人的海岛县，</text>
    <text x="40" y="97" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">强行搞选拔才是真正的资源浪费。</text>
  </g>

  <g transform="translate(40, 505)">
    <rect x="0" y="0" width="340" height="110" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{BLUE_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{BLUE}">&#x1F30D; 能推广吗</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">取决于人口和教育资源</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">大城市未必适用</text>
  </g>

  <g transform="translate(420, 505)">
    <rect x="0" y="0" width="340" height="110" rx="16" fill="{WHITE}" filter="url(#shadow)"/>
    <rect x="0" y="0" width="340" height="40" rx="16" fill="{PURPLE_LIGHT}"/>
    <text x="170" y="27" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="800" fill="{PURPLE}">&#x1F3AF; 核心结论</text>
    <text x="20" y="70" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">能因地制宜就是进步</text>
    <text x="20" y="95" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">没有标准答案</text>
  </g>

  <g transform="translate(40, 650)">
    <rect x="0" y="0" width="720" height="100" rx="50" fill="{GREEN_LIGHT}" stroke="{GREEN}" stroke-width="2"/>
    <text x="360" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{GREEN}">教育的本质不是筛选</text>
    <text x="360" y="80" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="{GREEN}">是培养</text>
  </g>

  <g transform="translate(40, 770)">
    <rect x="0" y="0" width="720" height="20" rx="10" fill="{BLUE_LIGHT}"/>
    <text x="360" y="15" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="13" font-weight="700" fill="{BLUE}">你觉得这样的改革好吗？评论区聊聊</text>
  </g>
</svg>'''
    (ROOT / "zhongkao-card-4-debate.svg").write_text(svg)
    CARDS.append("zhongkao-card-4-debate.svg")


def main():
    card_cover()
    card_1_what()
    card_2_why()
    card_3_how()
    card_4_debate()

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