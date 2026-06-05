#!/usr/bin/env python3
"""Generate 4 SVG cards — rich content, centered layout, strict design rules."""

import os

OUT = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/ai-tool-stack-2026-xhs"
os.makedirs(OUT, exist_ok=True)

W, H = 800, 800
FONT = "system-ui,-apple-system,sans-serif"

def render():
    # Card 0: Dark, English — Writing & Search
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#0B1027"/>
<text x="{W//2}" y="120" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="40" font-weight="800" font-family="{FONT}">Writing &amp; Search</text>
<text x="{W//2}" y="170" text-anchor="middle" dominant-baseline="central" fill="#94A3B8" font-size="18" font-weight="500" font-family="{FONT}">写作 · 对话</text>
<rect x="100" y="220" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="260" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">Claude Sonnet 4.6</text>
<text x="140" y="295" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">Long-form Writing · Deep Analysis</text>
<rect x="100" y="340" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="380" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">ChatGPT</text>
<text x="140" y="415" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">Daily Q&amp;A · Full Plugin Ecosystem</text>
<text x="{W//2}" y="500" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="40" font-weight="800" font-family="{FONT}">AI Search</text>
<rect x="100" y="550" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="590" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">Perplexity</text>
<text x="140" y="625" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">Answers with Sources · Research</text>
<rect x="100" y="670" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="710" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">Copilot</text>
<text x="140" y="745" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">Office Ecosystem · Microsoft</text>
</svg>'''
    with open(f'{OUT}/card-0.svg', 'w') as f:
        f.write(svg)

    # Card 1: Dark, English — Image & Video
    # 浅字：#F1F5F9, 描述：#94A3B8, 背景：#0B1027
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#0B1027"/>
<text x="{W//2}" y="120" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="40" font-weight="800" font-family="{FONT}">Image &amp; Video</text>
<text x="{W//2}" y="170" text-anchor="middle" dominant-baseline="central" fill="#94A3B8" font-size="18" font-weight="500" font-family="{FONT}">图像 · 视频</text>
<rect x="100" y="220" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="260" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">Midjourney</text>
<text x="140" y="295" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">审美天花板 · 艺术感</text>
<rect x="100" y="340" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="380" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">Firefly</text>
<text x="140" y="415" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">商业合规 · PS 集成</text>
<rect x="100" y="460" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="500" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">Veo 3</text>
<text x="140" y="535" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">Google · 最强视频生成</text>
<rect x="100" y="580" width="600" height="100" rx="16" fill="#1E293B"/>
<text x="140" y="620" fill="#F1F5F9" font-size="28" font-weight="700" font-family="{FONT}">可灵 AI</text>
<text x="140" y="655" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">快手 · 中文最强 · 便宜</text>
<text x="{W//2}" y="730" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="40" font-weight="800" font-family="{FONT}">PPT · 演示</text>
<rect x="100" y="760" width="600" height="30" rx="15" fill="#1E293B"/>
<text x="140" y="775" fill="#F1F5F9" font-size="14" font-weight="600" font-family="{FONT}">Gamma · 描述即生成 · 颜值高</text>
</svg>'''
    with open(f'{OUT}/card-1.svg', 'w') as f:
        f.write(svg)

    # Card 2: Dark, English — Audio & Music + Coding
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#0B1027"/>
<text x="{W//2}" y="120" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="40" font-weight="800" font-family="{FONT}">Audio · Music · Coding</text>
<text x="{W//2}" y="170" text-anchor="middle" dominant-baseline="central" fill="#94A3B8" font-size="18" font-weight="500" font-family="{FONT}">音频 · 音乐 · 编程</text>
<rect x="100" y="220" width="600" height="80" rx="16" fill="#1E293B"/>
<text x="140" y="250" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">Suno AI</text>
<text x="140" y="280" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Everyone Can Write Songs</text>
<rect x="100" y="310" width="600" height="80" rx="16" fill="#1E293B"/>
<text x="140" y="340" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">ElevenLabs</text>
<text x="140" y="370" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Voice Synthesis · Top Quality</text>
<rect x="100" y="400" width="600" height="80" rx="16" fill="#1E293B"/>
<text x="140" y="430" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">Notta</text>
<text x="140" y="460" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Meeting Transcription · Real-time</text>
<rect x="100" y="490" width="600" height="80" rx="16" fill="#1E293B"/>
<text x="140" y="520" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">Claude Code</text>
<text x="140" y="550" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Most Stable · Complex Projects</text>
<rect x="100" y="580" width="600" height="80" rx="16" fill="#1E293B"/>
<text x="140" y="610" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">Codex</text>
<text x="140" y="640" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">OpenAI · Browser Control</text>
<rect x="100" y="670" width="600" height="80" rx="16" fill="#1E293B"/>
<text x="140" y="700" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">Cursor</text>
<text x="140" y="730" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">VS Code Fork · Best Integration</text>
<rect x="100" y="760" width="600" height="30" rx="15" fill="#1E293B"/>
<text x="140" y="775" fill="#F1F5F9" font-size="14" font-weight="600" font-family="{FONT}">Windsurf · AI Coding · Cline Team</text>
</svg>'''
    with open(f'{OUT}/card-2.svg', 'w') as f:
        f.write(svg)

    # Card 3: Dark, English — Full Stack Overview + Principles
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">
<rect width="{W}" height="{H}" fill="#0B1027"/>
<text x="{W//2}" y="90" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="44" font-weight="800" font-family="{FONT}">2026 AI Tool Stack</text>
<text x="{W//2}" y="130" text-anchor="middle" dominant-baseline="central" fill="#94A3B8" font-size="16" font-weight="500" font-family="{FONT}">7 大分类 · 全景图</text>
<rect x="80" y="180" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="180" y="215" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">写作</text>
<text x="180" y="245" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Claude · ChatGPT</text>
<rect x="300" y="180" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="400" y="215" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">搜索</text>
<text x="400" y="245" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Perplexity · Copilot</text>
<rect x="520" y="180" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="620" y="215" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">生图</text>
<text x="620" y="245" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Midjourney · Firefly</text>
<rect x="80" y="300" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="180" y="335" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">视频</text>
<text x="180" y="365" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Veo 3 · 可灵 AI</text>
<rect x="300" y="300" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="400" y="335" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">PPT</text>
<text x="400" y="365" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Gamma · Tome</text>
<rect x="520" y="300" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="620" y="335" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">音乐</text>
<text x="620" y="365" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Suno · ElevenLabs</text>
<rect x="80" y="420" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="180" y="455" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">转录</text>
<text x="180" y="485" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Notta</text>
<rect x="300" y="420" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="400" y="455" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">编程</text>
<text x="400" y="485" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Claude Code · Codex</text>
<rect x="520" y="420" width="200" height="100" rx="16" fill="#1E293B"/>
<text x="620" y="455" text-anchor="middle" fill="#F1F5F9" font-size="24" font-weight="700" font-family="{FONT}">IDE</text>
<text x="620" y="485" text-anchor="middle" fill="#94A3B8" font-size="14" font-weight="500" font-family="{FONT}">Cursor · Windsurf</text>
<text x="{W//2}" y="570" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">查资料 → Perplexity</text>
<text x="{W//2}" y="610" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">写长文 → Claude</text>
<text x="{W//2}" y="650" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">做图片 → Midjourney</text>
<text x="{W//2}" y="690" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="26" font-weight="700" font-family="{FONT}">做视频 → Veo 3</text>
<rect x="200" y="730" width="400" height="40" rx="20" fill="#1E293B"/>
<text x="{W//2}" y="755" text-anchor="middle" dominant-baseline="central" fill="#F1F5F9" font-size="16" font-weight="600" font-family="{FONT}">工具选对 · 效率翻倍</text>
</svg>'''
    with open(f'{OUT}/card-3.svg', 'w') as f:
        f.write(svg)

    print("Generated 4 SVG cards")

if __name__ == '__main__':
    render()