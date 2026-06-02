#!/usr/bin/env python3
"""Generate 6 LIGHT (cream/white) cards for Codex++ XHS post (800x800)."""
import base64
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
LOGO_B64 = (ROOT / "codex-logo.b64").read_text().strip()

# LIGHT palette: cream base, white cards, brand blue/purple accents
CREAM = "#FAF7F2"
CREAM2 = "#F3F0E8"
WHITE = "#FFFFFF"
TEXT = "#1E293B"
TEXT_DIM = "#64748B"
TEXT_LIGHT = "#94A3B8"
BORDER = "#E2E8F0"
BLUE = "#3B82F6"
BLUE_LIGHT = "#DBEAFE"
PURPLE = "#8B5CF6"
PURPLE_LIGHT = "#EDE9FE"
PINK = "#EC4899"
GREEN = "#10B981"
ORANGE = "#F59E0B"
TEAL = "#06B6D4"
RED = "#EF4444"

CARDS = []


def card_1_cover():
    """Cover with logo + title + tagline"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <linearGradient id="title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3B82F6"/>
      <stop offset="50%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="12" flood-color="#1E293B" flood-opacity="0.08"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <!-- Decorative circles -->
  <circle cx="80" cy="100" r="60" fill="#DBEAFE" opacity="0.5"/>
  <circle cx="700" cy="150" r="40" fill="#EDE9FE" opacity="0.5"/>
  <circle cx="100" cy="650" r="50" fill="#FCE7F3" opacity="0.4"/>
  <circle cx="680" cy="600" r="70" fill="#DBEAFE" opacity="0.3"/>

  <!-- Logo -->
  <image href="data:image/png;base64,{LOGO_B64}" x="290" y="140" width="220" height="220"/>

  <!-- Title -->
  <text x="400" y="450" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="88" font-weight="900" fill="url(#title)">Codex++</text>

  <!-- Tagline card -->
  <rect x="150" y="500" width="500" height="60" rx="30" fill="{WHITE}" filter="url(#shadow)"/>
  <text x="400" y="538" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="24" font-weight="600" fill="{TEXT}">Codex App 外部增强启动器</text>

  <!-- Description -->
  <text x="400" y="610" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" fill="{TEXT_DIM}">不动原文件 · CDP 注入 · 全平台开源免费</text>

  <!-- Tags -->
  <g transform="translate(190, 660)">
    <rect x="0" y="0" width="90" height="38" rx="19" fill="{BLUE_LIGHT}"/>
    <text x="45" y="26" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="600" fill="{BLUE}">Rust</text>
    <rect x="110" y="0" width="90" height="38" rx="19" fill="{PURPLE_LIGHT}"/>
    <text x="155" y="26" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="600" fill="{PURPLE}">Tauri</text>
    <rect x="220" y="0" width="120" height="38" rx="19" fill="#FCE7F3"/>
    <text x="280" y="26" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" font-weight="600" fill="{PINK}">Open Source</text>
  </g>

  <text x="400" y="760" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_LIGHT}">github.com/BigPizzaV3/CodexPlusPlus</text>
</svg>'''
    (ROOT / "codex-card-1-cover.svg").write_text(svg)
    CARDS.append("codex-card-1-cover.svg")


def card_2_pain():
    """Pain points comparison: native vs Codex++"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="8" flood-color="#1E293B" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <text x="400" y="60" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="800" fill="{TEXT}">Codex App 的两个老大难</text>

  <!-- Left: Native Codex -->
  <g transform="translate(40, 120)">
    <rect x="0" y="0" width="340" height="600" rx="20" fill="{WHITE}" filter="url(#shadow)" stroke="#FCA5A5" stroke-width="2"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{RED}">❌ 原生 Codex</text>

    <!-- Pain 1 -->
    <rect x="20" y="80" width="300" height="220" rx="14" fill="#FEF2F2"/>
    <text x="40" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{RED}">🤯 插件入口锁死</text>
    <text x="40" y="160" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">API Key 登录后插件页灰掉</text>
    <text x="40" y="190" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">点啥都提示</text>
    <text x="40" y="220" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">"需要登录 ChatGPT"</text>
    <text x="40" y="260" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{RED}" font-weight="600">× 强行切回云端</text>

    <!-- Pain 2 -->
    <rect x="20" y="320" width="300" height="220" rx="14" fill="#FEF2F2"/>
    <text x="40" y="360" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{RED}">🗑️ 会话只能归档</text>
    <text x="40" y="400" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">界面只有 Archive</text>
    <text x="40" y="430" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">没有真·Delete 按钮</text>
    <text x="40" y="470" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{RED}" font-weight="600">× state_5.sqlite 越塞越大</text>
  </g>

  <!-- Arrow -->
  <g transform="translate(405, 420)">
    <path d="M -5 -10 L 8 0 L -5 10" stroke="{BLUE}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Right: Codex++ -->
  <g transform="translate(420, 120)">
    <rect x="0" y="0" width="340" height="600" rx="20" fill="{WHITE}" filter="url(#shadow)" stroke="#6EE7B7" stroke-width="2"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{GREEN}">✅ Codex++</text>

    <!-- Solution 1 -->
    <rect x="20" y="80" width="300" height="220" rx="14" fill="#F0FDF4"/>
    <text x="40" y="120" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{GREEN}">🔓 插件强制解锁</text>
    <text x="40" y="160" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">CDP 注入 renderer 脚本</text>
    <text x="40" y="190" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">所有插件入口可用</text>
    <text x="40" y="230" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{GREEN}" font-weight="600">✓ 不切回云端</text>

    <!-- Solution 2 -->
    <rect x="20" y="320" width="300" height="220" rx="14" fill="#F0FDF4"/>
    <text x="40" y="360" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{GREEN}">🗑️ 真·删除按钮</text>
    <text x="40" y="400" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">列表悬停出 Delete</text>
    <text x="40" y="430" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT}">真删本地数据库</text>
    <text x="40" y="470" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{GREEN}" font-weight="600">✓ 释放磁盘</text>
  </g>

  <text x="400" y="755" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_LIGHT}">外部 launcher 启动 · 不动 Codex 原文件 · 升级也不影响</text>
</svg>'''
    (ROOT / "codex-card-2-pain.svg").write_text(svg)
    CARDS.append("codex-card-2-pain.svg")


def card_3_features():
    """Features grid: 8 capabilities"""
    features = [
        ("01", "插件入口解锁", "API Key 也能用", BLUE, BLUE_LIGHT),
        ("02", "真·删除会话", "列表悬停即删", RED, "#FEF2F2"),
        ("03", "Markdown 导出", "一键导出 .md", GREEN, "#F0FDF4"),
        ("04", "项目移动", "UI 调归属", PURPLE, PURPLE_LIGHT),
        ("05", "Timeline 视图", "按时间浏览", ORANGE, "#FFFBEB"),
        ("06", "用户脚本注入", "自定义 JS", TEAL, "#ECFEFF"),
        ("07", "Upstream worktree", "智能创建分支", PINK, "#FCE7F3"),
        ("08", "Zed Remote 打开", "远程上下文识别", "#6366F1", "#EEF2FF"),
    ]
    items = ""
    for i, (num, name, desc, color, bg) in enumerate(features):
        col = i % 2
        row = i // 2
        x = 40 + col * 370
        y = 140 + row * 130
        items += f'''
    <g transform="translate({x}, {y})">
      <rect x="0" y="0" width="350" height="110" rx="16" fill="{WHITE}" stroke="{color}" stroke-width="1.5"/>
      <circle cx="38" cy="55" r="24" fill="{bg}" stroke="{color}" stroke-width="1"/>
      <text x="38" y="63" text-anchor="middle" font-family="ui-monospace, monospace" font-size="22" font-weight="800" fill="{color}">{num}</text>
      <text x="78" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">{name}</text>
      <text x="78" y="82" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">{desc}</text>
    </g>'''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="800" fill="{TEXT}">8 大核心能力</text>
  <text x="400" y="90" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">所有增强走 CDP 注入 · 不改原文件</text>
  {items}
  <text x="400" y="770" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="15" fill="{TEXT_LIGHT}">Rust 后端 · Tauri 管理面板 · 深色/浅色切换</text>
</svg>'''
    (ROOT / "codex-card-3-features.svg").write_text(svg)
    CARDS.append("codex-card-3-features.svg")


def card_4_relay():
    """Relay injection: steps + config.toml"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="8" flood-color="#1E293B" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="800" fill="{TEXT}">🔌 中转注入模式</text>
  <text x="400" y="90" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">官方登录 + 第三方 API · 一键热切换</text>

  <!-- Steps -->
  <g transform="translate(40, 140)">
    <rect x="0" y="0" width="720" height="60" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="30" r="20" fill="{BLUE}"/>
    <text x="40" y="36" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#FFF">1</text>
    <text x="80" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="600" fill="{TEXT}">登录 ChatGPT 官方</text>
    <text x="320" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">在 Codex 里完成 OAuth 登录</text>
  </g>

  <g transform="translate(40, 220)">
    <rect x="0" y="0" width="720" height="60" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="30" r="20" fill="{PURPLE}"/>
    <text x="40" y="36" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#FFF">2</text>
    <text x="80" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="600" fill="{TEXT}">添加中转配置</text>
    <text x="320" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Base URL + Key，可多套</text>
  </g>

  <g transform="translate(40, 300)">
    <rect x="0" y="0" width="720" height="60" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="30" r="20" fill="{PINK}"/>
    <text x="40" y="36" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#FFF">3</text>
    <text x="80" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="600" fill="{TEXT}">应用中转注入</text>
    <text x="320" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">Codex++ 自动写好 provider</text>
  </g>

  <g transform="translate(40, 380)">
    <rect x="0" y="0" width="720" height="60" rx="14" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="40" cy="30" r="20" fill="{GREEN}"/>
    <text x="40" y="36" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" font-weight="700" fill="#FFF">4</text>
    <text x="80" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" font-weight="600" fill="{TEXT}">启动 Codex++</text>
    <text x="320" y="36" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">想回官方？点「清除 API 模式」</text>
  </g>

  <!-- Config card -->
  <g transform="translate(40, 480)">
    <rect x="0" y="0" width="720" height="260" rx="16" fill="#1E293B" filter="url(#shadow)"/>
    <text x="24" y="36" font-family="ui-monospace, monospace" font-size="16" font-weight="700" fill="{BLUE_LIGHT}">~/.codex/config.toml</text>
    <line x1="24" y1="52" x2="696" y2="52" stroke="#334155" stroke-width="1"/>
    <text x="24" y="90" font-family="ui-monospace, monospace" font-size="15" fill="#E2E8F0">model_provider = "CodexPlusPlus"</text>
    <text x="24" y="130" font-family="ui-monospace, monospace" font-size="15" fill="{PURPLE_LIGHT}">[model_providers.CodexPlusPlus]</text>
    <text x="48" y="165" font-family="ui-monospace, monospace" font-size="15" fill="#CBD5E1">wire_api = "responses"</text>
    <text x="48" y="195" font-family="ui-monospace, monospace" font-size="15" fill="#CBD5E1">base_url = "https://example.com/v1"</text>
    <text x="48" y="225" font-family="ui-monospace, monospace" font-size="15" fill="#CBD5E1">experimental_bearer_token = "sk-..."</text>
  </g>
</svg>'''
    (ROOT / "codex-card-4-relay.svg").write_text(svg)
    CARDS.append("codex-card-4-relay.svg")


def card_5_platforms():
    """Platform support cards"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="8" flood-color="#1E293B" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="800" fill="{TEXT}">🖥️ 三平台覆盖</text>
  <text x="400" y="90" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">从 GitHub Releases 直接下载</text>

  <g transform="translate(40, 150)">
    <rect x="0" y="0" width="720" height="150" rx="18" fill="{WHITE}" filter="url(#shadow)" stroke="{BLUE}" stroke-width="1.5"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="700" fill="{TEXT}">🪟 Windows x64</text>
    <text x="30" y="90" font-family="ui-monospace, monospace" font-size="16" fill="{BLUE}">CodexPlusPlus-*-windows-x64-setup.exe</text>
    <text x="30" y="125" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">NSIS 安装包 · 桌面 + 开始菜单快捷方式</text>
  </g>

  <g transform="translate(40, 330)">
    <rect x="0" y="0" width="720" height="150" rx="18" fill="{WHITE}" filter="url(#shadow)" stroke="{PURPLE}" stroke-width="1.5"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="700" fill="{TEXT}">🍎 macOS Intel x64</text>
    <text x="30" y="90" font-family="ui-monospace, monospace" font-size="16" fill="{PURPLE}">CodexPlusPlus-*-macos-x64.dmg</text>
    <text x="30" y="125" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">安装 /Applications/Codex++.app + 管理工具.app</text>
  </g>

  <g transform="translate(40, 510)">
    <rect x="0" y="0" width="720" height="150" rx="18" fill="{WHITE}" filter="url(#shadow)" stroke="{PINK}" stroke-width="1.5"/>
    <text x="30" y="50" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="28" font-weight="700" fill="{TEXT}">🍎 macOS Apple Silicon</text>
    <text x="30" y="90" font-family="ui-monospace, monospace" font-size="16" fill="{PINK}">CodexPlusPlus-*-macos-arm64.dmg</text>
    <text x="30" y="125" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">M1/M2/M3/M4 专用 · 静默入口隐藏 Dock</text>
  </g>

  <text x="400" y="730" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_DIM}">⚠️ macOS 首次打开报"已损坏"？执行 xattr -rd com.apple.quarantine</text>
</svg>'''
    (ROOT / "codex-card-5-platforms.svg").write_text(svg)
    CARDS.append("codex-card-5-platforms.svg")


def card_6_start():
    """Quick start + GitHub"""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" width="800" height="800">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FAF7F2"/>
      <stop offset="100%" stop-color="#F5F0E8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="8" flood-color="#1E293B" flood-opacity="0.06"/>
    </filter>
  </defs>
  <rect width="800" height="800" fill="url(#bg)"/>

  <text x="400" y="55" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="36" font-weight="800" fill="{TEXT}">🚀 三步上手</text>
  <text x="400" y="90" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="18" fill="{TEXT_DIM}">从 0 到 Codex++ 不到 5 分钟</text>

  <!-- Step 1 -->
  <g transform="translate(50, 150)">
    <rect x="0" y="0" width="700" height="80" rx="18" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="55" cy="40" r="26" fill="{BLUE}"/>
    <text x="55" y="47" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#FFF">1</text>
    <text x="105" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">下载安装包</text>
    <text x="350" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">去 GitHub Releases 选平台</text>
  </g>

  <!-- Step 2 -->
  <g transform="translate(50, 260)">
    <rect x="0" y="0" width="700" height="80" rx="18" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="55" cy="40" r="26" fill="{PURPLE}"/>
    <text x="55" y="47" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#FFF">2</text>
    <text x="105" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">打开管理工具</text>
    <text x="350" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">Tauri 面板 · 配置中转/增强</text>
  </g>

  <!-- Step 3 -->
  <g transform="translate(50, 370)">
    <rect x="0" y="0" width="700" height="80" rx="18" fill="{WHITE}" filter="url(#shadow)"/>
    <circle cx="55" cy="40" r="26" fill="{GREEN}"/>
    <text x="55" y="47" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="800" fill="#FFF">3</text>
    <text x="105" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="20" font-weight="700" fill="{TEXT}">启动 Codex++</text>
    <text x="350" y="48" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">静默启动 · CDP 自动注入</text>
  </g>

  <!-- GitHub card -->
  <g transform="translate(50, 510)">
    <rect x="0" y="0" width="700" height="200" rx="20" fill="{WHITE}" filter="url(#shadow)" stroke="{BLUE}" stroke-width="1.5"/>
    <text x="350" y="45" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="22" font-weight="700" fill="{TEXT}">📦 GitHub 仓库</text>
    <rect x="100" y="70" width="500" height="48" rx="24" fill="{BLUE_LIGHT}"/>
    <text x="350" y="101" text-anchor="middle" font-family="ui-monospace, monospace" font-size="18" font-weight="600" fill="{BLUE}">github.com/BigPizzaV3/CodexPlusPlus</text>

    <text x="350" y="160" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="17" fill="{TEXT_DIM}">QQ 群 1103050832 · Telegram @CodexPlusPlus</text>
  </g>

  <text x="400" y="760" text-anchor="middle" font-family="ui-sans-serif, -apple-system, sans-serif" font-size="16" fill="{TEXT_LIGHT}">完全开源免费 · 打赏 & PR 都欢迎 ✨</text>
</svg>'''
    (ROOT / "codex-card-6-start.svg").write_text(svg)
    CARDS.append("codex-card-6-start.svg")


def main():
    card_1_cover()
    card_2_pain()
    card_3_features()
    card_4_relay()
    card_5_platforms()
    card_6_start()

    print(f"Generated {len(CARDS)} SVGs")
    for name in CARDS:
        png = name.replace(".svg", ".png")
        subprocess.run([
            "inkscape", str(ROOT / name),
            "-o", str(ROOT / png),
            "-w", "800", "-h", "800"
        ], check=True)
        print(f"  ✓ {png}")


if __name__ == "__main__":
    main()
