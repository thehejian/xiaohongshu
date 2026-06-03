#!/usr/bin/env python3
"""Hermes Feishu cards v3 with dual logos"""
import subprocess, json, base64
from pathlib import Path

D = Path(__file__).parent
HERMES = json.loads((D / "hermes_logo.json").read_text())
FEISHU = json.loads((D / "feishu_logo.json").read_text())

CARDS = [
    {"sg":"cover","g":("#7C3AED","#3370FF"),"a":"#F472B6","f":"hermes-feishu-cover"},
    {"sg":"num","n":"01","t":"先搞清楚它不干什么","d":"不是聊天机器人 · 不是代码助手","s":"跟它说完需求它就自己去干了","g":("#2563EB","#3B82F6"),"a":"#60A5FA","i":"🤖","f":"hermes-feishu-card-1","b":"像请了个远程实习生"},
    {"sg":"num","n":"02","t":"飞书日程","d":"「明天 2 点跟市场部开会」","s":"自动查日历 · 找空闲 · 发邀请","g":("#DB2777","#EC4899"),"a":"#F9A8D4","i":"📅","f":"hermes-feishu-card-2","b":"再也不会忘开会了"},
    {"sg":"num","n":"03","t":"飞书消息","d":"群聊监控 · 自动回复","s":"7×24 在线，半夜也有人处理","g":("#0D9488","#14B8A6"),"a":"#99F6E4","i":"💬","f":"hermes-feishu-card-3","b":"消息再多也不怕"},
    {"sg":"num","n":"04","t":"Bitable 自动录","d":"信息自动写入多维表格","s":"一条指令批量改 500 行","g":("#EA580C","#F97316"),"a":"#FDBA74","i":"📊","f":"hermes-feishu-card-4","b":"告别手动复制粘贴"},
    {"sg":"num","n":"05","t":"文档自动生成","d":"给主题就帮你写","s":"排版 · 插图 · 目录全自动","g":("#7C3AED","#8B5CF6"),"a":"#C4B5FD","i":"📝","f":"hermes-feishu-card-5","b":"写文档的时间省了"},
    {"sg":"num","n":"06","t":"审批不用盯","d":"报销自动审批 · 请假智能判","s":"规则灵活 · 不漏单不卡单","g":("#0891B2","#06B6D4"),"a":"#67E8F9","i":"✅","f":"hermes-feishu-card-6","b":"审批流终于不烦人了"},
    {"sg":"num","n":"07","t":"双核并行","d":"OpenClaw 管飞书 + Hermes 管 Telegram","s":"同一台机器 · 共享技能库","g":("#1E293B","#334155"),"a":"#818CF8","i":"🔗","f":"hermes-feishu-card-7","b":"圈里叫它「养虾又养马」"},
]

def gen_svg(c, out):
    g0,g1 = c["g"]
    a = c["a"]
    star = "✦"

    if c["sg"] == "cover":
        svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{G0}"/><stop offset="50%" stop-color="#4F46E5"/><stop offset="100%" stop-color="{G1}"/>
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="#000" flood-opacity="0.2"/>
    </filter>
  </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <circle cx="512" cy="512" r="420" fill="#FFFFFF" opacity="0.03"/>
  <circle cx="150" cy="150" r="200" fill="#FFFFFF" opacity="0.04"/>
  <circle cx="874" cy="874" r="200" fill="#FFFFFF" opacity="0.04"/>
  <text x="200" y="120" font-size="20" fill="#FFFFFF" opacity="0.25">{STAR}</text>
  <text x="820" y="200" font-size="16" fill="#FFFFFF" opacity="0.2">{STAR}</text>
  <text x="180" y="800" font-size="18" fill="#FFFFFF" opacity="0.2">{STAR}</text>
  <text x="850" y="700" font-size="14" fill="#FFFFFF" opacity="0.2">{STAR}</text>
  <circle cx="310" cy="280" r="80" fill="#FFFFFF" filter="url(#shadow)"/>
  <image x="246" y="216" width="128" height="128" href="data:image/png;base64,{HL}"/>
  <text x="310" y="400" text-anchor="middle" font-family="system-ui,sans-serif" font-size="36" font-weight="900" fill="#FFFFFF">Hermes</text>
  <text x="512" y="315" text-anchor="middle" font-size="64">🤝</text>
  <circle cx="714" cy="280" r="80" fill="#FFFFFF" filter="url(#shadow)"/>
  <image x="650" y="216" width="128" height="128" href="data:image/png;base64,{FL}"/>
  <text x="714" y="400" text-anchor="middle" font-family="system-ui,sans-serif" font-size="36" font-weight="900" fill="#FFFFFF">飞书</text>
  <text x="512" y="500" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="48" font-weight="800" fill="#FFFFFF">AI管家 + 飞书后台 = 双剑合璧</text>
  <text x="512" y="620" text-anchor="middle" font-family="system-ui,sans-serif" font-size="24" fill="#E2E8F0">7 个场景 · 个个实用 · 看看怎么做到的</text>
  <rect x="340" y="700" width="344" height="56" rx="28" fill="#FFFFFF" opacity="0.15"/>
  <text x="512" y="735" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="600" fill="#FFFFFF">⚡ 一行命令安装</text>
  <rect x="120" y="780" width="784" height="64" rx="12" fill="#000000" opacity="0.2"/>
  <text x="144" y="820" font-family="ui-monospace,monospace" font-size="22" font-weight="500" fill="#FDE68A">curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash</text>
  <text x="512" y="940" text-anchor="middle" font-family="system-ui,sans-serif" font-size="18" fill="#FFFFFF" opacity="0.6">175K+ Stars · MIT · Nous Research</text>
</svg>""".format(G0=g0,G1=g1,HL=HERMES,FL=FEISHU,STAR=star)
    else:
        num=c["n"]; title=c["t"]; desc=c["d"]; sub=c["s"]; icon=c.get("i","*"); bottom=c.get("b","")
        svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{G0}"/><stop offset="100%" stop-color="{G1}"/>
    </linearGradient>
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF"/><stop offset="40%" stop-color="#FDE68A"/><stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    </defs>
  <rect width="1024" height="1024" fill="url(#bg)"/>
  <circle cx="80" cy="80" r="180" fill="#FFFFFF" opacity="0.04"/>
  <circle cx="944" cy="944" r="220" fill="#FFFFFF" opacity="0.04"/>
  <circle cx="512" cy="100" r="80" fill="{AC}" opacity="0.12"/>
  <circle cx="900" cy="300" r="40" fill="#FFFFFF" opacity="0.06"/>
  <circle cx="120" cy="700" r="50" fill="#FFFFFF" opacity="0.06"/>
  <text x="150" y="200" font-size="20" fill="#FFFFFF" opacity="0.3">{STAR}</text>
  <text x="850" y="180" font-size="14" fill="#FFFFFF" opacity="0.25">{STAR}</text>
  <text x="200" y="800" font-size="16" fill="#FFFFFF" opacity="0.2">{STAR}</text>
  <text x="800" y="750" font-size="22" fill="#FFFFFF" opacity="0.25">{STAR}</text>
  <text x="512" y="140" text-anchor="middle" font-size="56">{ICON}</text>
  <text x="512" y="240" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="140" font-weight="900" fill="url(#titleGrad)">{NUM}</text>
  <text x="512" y="360" text-anchor="middle" font-family="system-ui,-apple-system,sans-serif" font-size="48" font-weight="800" fill="#FFFFFF">{TITLE}</text>
  <rect x="80" y="520" width="864" height="340" rx="24" fill="#000000" opacity="0.15"/>
  <text x="512" y="590" text-anchor="middle" font-family="system-ui,sans-serif" font-size="28" font-weight="500" fill="#E2E8F0">{DESC}</text>
  <text x="512" y="660" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" fill="#94A3B8">{SUB}</text>
  <rect x="380" y="700" width="264" height="3" rx="1.5" fill="{AC}" opacity="0.5"/>
  <text x="512" y="780" text-anchor="middle" font-family="system-ui,sans-serif" font-size="24" font-weight="600" fill="#FFFFFF" opacity="0.9">{BTM}</text>
</svg>""".format(G0=g0,G1=g1,AC=a,STAR=star,ICON=icon,NUM=num,TITLE=title,DESC=desc,SUB=sub,BTM=bottom)

    out.write_text(svg, encoding="utf-8")

def to_png(svg_path, png_path):
    r=subprocess.run(["inkscape",str(svg_path),"--export-type=png","--export-dpi=100","--export-filename={}".format(png_path)],capture_output=True,text=True)
    return r.returncode==0

def main():
    print("Gen Hermes Feishu cards v3 (Dual Logo)...")
    for i,c in enumerate(CARDS):
        svp=D/"{}.svg".format(c["f"]); pnp=D/"{}.png".format(c["f"])
        print("  {}/{} {}".format(i+1,len(CARDS),c["f"]))
        gen_svg(c,svp)
        if to_png(svp,pnp): print("    OK")
        else: print("    FAIL")
        svp.unlink(missing_ok=True)
    print("Done!")

if __name__=="__main__": main()