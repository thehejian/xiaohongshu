#!/usr/bin/env python3
"""Hermes 🤝 飞书 — XHS 爆款卡片 v3（高饱和渐变 + 全幅背景 + 大标题冲击）"""
import subprocess
from pathlib import Path

CARDS = [
    {
        "title": "Hermes",
        "title2": "🤝 飞书",
        "subtitle": "",
        "grad": ("#7C3AED", "#4F46E5"),
        "accent": "#F472B6",
        "icon": "⚡",
        "file": "hermes-feishu-cover",
        "bottom": "AI管家 + 飞书后台 = 双剑合璧",
        "show_icon": True,
    },
    {
        "num": "01",
        "title": "先搞清楚它不干什么",
        "desc": "不是聊天机器人 · 不是代码助手\n是一个跑在你服务器上的自主 Agent",
        "subtitle": "跟它说完需求它就自己去干了",
        "grad": ("#2563EB", "#3B82F6"),
        "accent": "#60A5FA",
        "icon": "🤖",
        "file": "hermes-feishu-card-1",
        "bottom": "像请了个远程实习生",
    },
    {
        "num": "02",
        "title": "飞书日程\n一句话安排",
        "desc": "「明天 2 点跟市场部开会」\n自动查日历 · 找空闲 · 发邀请",
        "subtitle": "不用打开飞书网页",
        "grad": ("#DB2777", "#EC4899"),
        "accent": "#F9A8D4",
        "icon": "📅",
        "file": "hermes-feishu-card-2",
        "bottom": "再也不会忘开会了",
    },
    {
        "num": "03",
        "title": "飞书消息\n它帮你 7×24 盯",
        "desc": "群聊监控 · 自动回复\n关键词触发 · 通知转 Telegram",
        "subtitle": "半夜发消息也有人处理",
        "grad": ("#0D9488", "#14B8A6"),
        "accent": "#99F6E4",
        "icon": "💬",
        "file": "hermes-feishu-card-3",
        "bottom": "消息再多也不怕",
    },
    {
        "num": "04",
        "title": "Bitable\n自动录数据",
        "desc": "信息自动写入多维表格\n定时同步 · 批量改 500 行",
        "subtitle": "告别手动复制粘贴",
        "grad": ("#EA580C", "#F97316"),
        "accent": "#FDBA74",
        "icon": "📊",
        "file": "hermes-feishu-card-4",
        "bottom": "表格自动化真香",
    },
    {
        "num": "05",
        "title": "文档草稿\n自动生成",
        "desc": "给主题就帮你写\n排版 · 插图 · 目录全自动",
        "subtitle": "周报 · 方案 · 纪要全包",
        "grad": ("#7C3AED", "#8B5CF6"),
        "accent": "#C4B5FD",
        "icon": "📝",
        "file": "hermes-feishu-card-5",
        "bottom": "写文档的时间省了",
    },
    {
        "num": "06",
        "title": "审批流程\n不用盯",
        "desc": "报销自动审批 · 请假智能判\n异常单据自动标记",
        "subtitle": "规则灵活 · 不漏单不卡单",
        "grad": ("#0891B2", "#06B6D4"),
        "accent": "#67E8F9",
        "icon": "✅",
        "file": "hermes-feishu-card-6",
        "bottom": "审批流终于不烦人了",
    },
    {
        "num": "07",
        "title": "双内核\n飞书+Telegram",
        "desc": "OpenClaw 管飞书\nHermes 管 Telegram",
        "subtitle": "同一台机器 · 共享技能库",
        "grad": ("#1E293B", "#334155"),
        "accent": "#818CF8",
        "icon": "🔗",
        "file": "hermes-feishu-card-7",
        "bottom": "圈里叫它「养虾又养马」",
    },
]

W, H = 1024, 1024


def gen_svg(c, out):
    g0, g1 = c["grad"]
    icon = c.get("icon", "⚡")
    bottom = c.get("bottom", "")
    is_cover = "num" not in c
    num = c.get("num", "")

    if is_cover:
        t1_fs = 100
        t1_y = 320
        t2_fs = 56
        t2_y = t1_y + 80
        t1 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="{}" font-weight="900" fill="url(#titleGrad)">{}</text>'.format(t1_y, t1_fs, c["title"])
        t2 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="{}" font-weight="800" fill="#FFFFFF">{}</text>'.format(t2_y, t2_fs, c["title2"])
        icon_elem = '<text x="512" y="160" text-anchor="middle" font-size="72">⚡</text>'
    else:
        num_fs = 140
        num_y = 240
        t_fs = 52
        t_y = 360
        t1 = '<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="{}" font-weight="900" fill="url(#titleGrad)">{}</text>'.format(num_y, num_fs, num)
        t2_lines = c["title"].split("\n")
        t2_parts = []
        for i, line in enumerate(t2_lines):
            t2_parts.append('<text x="512" y="{}" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="{}" font-weight="800" fill="#FFFFFF">{}</text>'.format(t_y + i * 60, t_fs, line))
        t2 = "\n".join(t2_parts)
        icon_elem = '<text x="512" y="140" text-anchor="middle" font-size="56">{}</text>'.format(icon)

    desc_lines = c.get("desc", "").split("\n")
    desc_parts = []
    desc_y_start = 620
    for i, line in enumerate(desc_lines):
        desc_parts.append('<text x="512" y="{}" text-anchor="middle" font-family="system-ui,sans-serif" font-size="26" font-weight="500" fill="#E2E8F0">{}</text>'.format(desc_y_start + i * 38, line))
    desc_xml = "\n".join(desc_parts)

    sub = c.get("subtitle", "")
    sub_elem = '<text x="512" y="760" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" fill="#94A3B8">{}</text>'.format(sub) if sub else ""

    bottom_elem = '<text x="512" y="940" text-anchor="middle" font-family="system-ui,sans-serif" font-size="24" font-weight="600" fill="#FFFFFF" opacity="0.9">{}</text>'.format(bottom) if bottom else ""

    badges = ""
    if is_cover:
        badges = '''
  <rect x="160" y="500" width="200" height="44" rx="22" fill="#FFFFFF" opacity="0.15"/>
  <text x="260" y="528" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" font-weight="600" fill="#FFFFFF">自主 Agent</text>
  <rect x="380" y="500" width="180" height="44" rx="22" fill="#FFFFFF" opacity="0.15"/>
  <text x="470" y="528" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" font-weight="600" fill="#FFFFFF">175K ⭐</text>
  <rect x="580" y="500" width="200" height="44" rx="22" fill="#FFFFFF" opacity="0.15"/>
  <text x="680" y="528" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" font-weight="600" fill="#FFFFFF">飞书集成</text>
  <rect x="262" y="560" width="500" height="44" rx="22" fill="#FFFFFF" opacity="0.15"/>
  <text x="512" y="588" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" font-weight="600" fill="#FFFFFF">7 个场景 · 个个实用</text>'''

    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{G0}"/>
      <stop offset="100%" stop-color="{G1}"/>
    </linearGradient>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="40%" stop-color="#FDE68A"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="1024" height="1024" fill="url(#bg)"/>

  <!-- 装饰元素 -->
  <circle cx="80" cy="80" r="180" fill="#FFFFFF" opacity="0.04"/>
  <circle cx="944" cy="944" r="220" fill="#FFFFFF" opacity="0.04"/>
  <circle cx="512" cy="100" r="80" fill="{AC}" opacity="0.12"/>
  <circle cx="900" cy="300" r="40" fill="#FFFFFF" opacity="0.06"/>
  <circle cx="120" cy="700" r="50" fill="#FFFFFF" opacity="0.06"/>

  <!-- 装饰星点 -->
  <text x="150" y="200" font-size="20" fill="#FFFFFF" opacity="0.3">✦</text>
  <text x="850" y="180" font-size="14" fill="#FFFFFF" opacity="0.25">✦</text>
  <text x="200" y="800" font-size="16" fill="#FFFFFF" opacity="0.2">✦</text>
  <text x="800" y="750" font-size="22" fill="#FFFFFF" opacity="0.25">✦</text>

  {ICON}

  <!-- 标题区 -->
  {T1}
  {T2}

  <!-- 标签 -->
  {BADGES}

  <!-- 底部色块卡片 -->
  <rect x="80" y="580" width="864" height="320" rx="24" fill="#000000" opacity="0.15"/>

  <!-- 描述文字 -->
  {DESC}

  <!-- 副标题 -->
  {SUB}

  <!-- 分隔装饰线 -->
  <rect x="380" y="800" width="264" height="3" rx="1.5" fill="{AC}" opacity="0.5"/>

  <!-- 底部 -->
  {BTM}
</svg>'''.format(
        G0=g0, G1=g1, AC=c["accent"],
        ICON=icon_elem,
        T1=t1, T2=t2,
        BADGES=badges,
        DESC=desc_xml,
        SUB=sub_elem,
        BTM=bottom_elem,
    )

    out.write_text(svg, encoding="utf-8")


def to_png(svg_path, png_path):
    r = subprocess.run(
        ["inkscape", str(svg_path), "--export-type=png", "--export-dpi=100", "--export-filename={}".format(png_path)],
        capture_output=True, text=True,
    )
    return r.returncode == 0


def main():
    d = Path(__file__).parent
    print("🎨 生成 Hermes 🤝 飞书 爆款卡片 v3（高饱和冲击风格）...")
    for i, c in enumerate(CARDS):
        svg_path = d / "{}.svg".format(c["file"])
        png_path = d / "{}.png".format(c["file"])
        print("  {}/{} {}".format(i + 1, len(CARDS), c.get("title2", c["title"])))
        gen_svg(c, svg_path)
        if to_png(svg_path, png_path):
            print("    ✅ {}".format(png_path.name))
        else:
            print("    ❌ inkscape error")
        svg_path.unlink(missing_ok=True)
    print("\n✨ 完成！")


if __name__ == "__main__":
    main()