#!/usr/bin/env python3

import subprocess
import os

W, H = 1024, 1024
BG = "#0B1027"
TEXT_WHITE = "#F1F5F9"
TEXT_MUTED = "#94A3B8"
TEXT_LIGHT = "#64748B"
AMBER = "#F59E0B"
GREEN = "#10B981"
PURPLE = "#8B5CF6"


def shadow_filter():
    return '''
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="16" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
    '''


def cover():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      <radialGradient id="radial" cx="50%" cy="40%" r="60%">
        <stop offset="0%" stop-color="#1E1B4B"/>
        <stop offset="100%" stop-color="{BG}"/>
      </radialGradient>
      <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="{AMBER}"/>
        <stop offset="50%" stop-color="{GREEN}"/>
        <stop offset="100%" stop-color="{PURPLE}"/>
      </linearGradient>
      {shadow_filter()}
    </defs>
    <rect width="{W}" height="{H}" fill="url(#radial)"/>

    <circle cx="100" cy="80" r="5" fill="{AMBER}" opacity="0.2"/>
    <circle cx="120" cy="75" r="3" fill="{GREEN}" opacity="0.2"/>
    <circle cx="140" cy="80" r="5" fill="{PURPLE}" opacity="0.2"/>

    <text x="60" y="180" font-size="72" font-weight="800" fill="url(#titleGrad)" font-family="Inter, Helvetica, sans-serif">AI RURAL</text>
    <text x="60" y="260" font-size="72" font-weight="800" fill="url(#titleGrad)" font-family="Inter, Helvetica, sans-serif">QUOTES</text>

    <line x1="60" y1="310" x2="350" y2="310" stroke="{AMBER}" stroke-width="3" stroke-linecap="round" opacity="0.4"/>

    <text x="60" y="370" font-size="28" font-weight="600" fill="{TEXT_WHITE}" font-family="Inter, Helvetica, sans-serif">WeChat Video Channel Goldmine</text>
    <text x="60" y="415" font-size="22" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Millions of Views · AI-Generated · Ad Revenue</text>

    <rect x="60" y="480" width="904" height="90" rx="14" fill="#FFFFFF" opacity="0.06" filter="url(#shadow)"/>
    <text x="80" y="520" font-size="26" font-weight="700" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">10K views = $4-12 USD</text>
    <text x="80" y="555" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">1M views = $400-1,100 · Post 3/day = $1,500+/mo</text>

    <rect x="60" y="610" width="280" height="48" rx="24" fill="{AMBER}" opacity="0.12"/>
    <text x="100" y="642" font-size="18" font-weight="600" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">Elder traffic</text>

    <rect x="360" y="610" width="260" height="48" rx="24" fill="{GREEN}" opacity="0.12"/>
    <text x="400" y="642" font-size="18" font-weight="600" fill="{GREEN}" font-family="Inter, Helvetica, sans-serif">AI batch</text>

    <rect x="640" y="610" width="220" height="48" rx="24" fill="{PURPLE}" opacity="0.12"/>
    <text x="670" y="642" font-size="18" font-weight="600" fill="{PURPLE}" font-family="Inter, Helvetica, sans-serif">Ads share</text>

    <text x="60" y="740" font-size="16" fill="{TEXT_LIGHT}" font-family="Inter, Helvetica, sans-serif">#WeChat #VideoChannel #AIsidehustle #ContentCreator</text>
  </svg>'''


def card_why():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      <radialGradient id="radial" cx="50%" cy="30%" r="55%">
        <stop offset="0%" stop-color="#1E1B4B"/>
        <stop offset="100%" stop-color="{BG}"/>
      </radialGradient>
      {shadow_filter()}
    </defs>
    <rect width="{W}" height="{H}" fill="url(#radial)"/>

    <rect width="{W}" height="120" fill="{AMBER}" opacity="0.06"/>
    <text x="60" y="50" font-size="16" font-weight="600" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">CARD 01</text>
    <text x="60" y="90" font-size="36" font-weight="800" fill="{TEXT_WHITE}" font-family="Inter, Helvetica, sans-serif">Why Rural Quotes</text>

    <rect x="60" y="155" width="904" height="200" rx="14" fill="#FFFFFF" opacity="0.05" filter="url(#shadow)"/>
    <text x="90" y="195" font-size="20" font-weight="700" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">Target audience: 40-65 (60%+ of users)</text>
    <text x="90" y="235" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Rural wisdom quotes = max engagement</text>
    <text x="90" y="270" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Completion rate: 3-5x vs entertainment</text>
    <text x="90" y="305" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Comments: "So true!" "Well said"</text>

    <rect x="60" y="390" width="904" height="200" rx="14" fill="#FFFFFF" opacity="0.05" filter="url(#shadow)"/>
    <text x="90" y="430" font-size="20" font-weight="700" fill="{GREEN}" font-family="Inter, Helvetica, sans-serif">Viral Quote Examples</text>
    <text x="90" y="470" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">"When poor, keep silent; when low, don't preach"</text>
    <text x="90" y="505" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">"Relatives shouldn't share money"</text>
    <text x="90" y="540" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">"Better offend a gentleman than a petty man"</text>

    <rect x="60" y="625" width="904" height="60" rx="12" fill="#FFFFFF" opacity="0.03"/>
    <text x="100" y="662" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Rural quotes = elder traffic goldmine</text>

    <text x="60" y="760" font-size="14" fill="{TEXT_LIGHT}" font-family="Inter, Helvetica, sans-serif">#WeChat #ContentStrategy #ViralContent</text>
  </svg>'''


def card_how():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      <radialGradient id="radial" cx="50%" cy="30%" r="55%">
        <stop offset="0%" stop-color="#1E1B4B"/>
        <stop offset="100%" stop-color="{BG}"/>
      </radialGradient>
      {shadow_filter()}
    </defs>
    <rect width="{W}" height="{H}" fill="url(#radial)"/>

    <rect width="{W}" height="120" fill="{GREEN}" opacity="0.06"/>
    <text x="60" y="50" font-size="16" font-weight="600" fill="{GREEN}" font-family="Inter, Helvetica, sans-serif">CARD 02</text>
    <text x="60" y="90" font-size="36" font-weight="800" fill="{TEXT_WHITE}" font-family="Inter, Helvetica, sans-serif">AI Pipeline: 5 min/video</text>

    <rect x="60" y="155" width="904" height="380" rx="14" fill="#FFFFFF" opacity="0.05" filter="url(#shadow)"/>
    <text x="90" y="195" font-size="20" font-weight="700" fill="{TEXT_WHITE}" font-family="Inter, Helvetica, sans-serif">Full Workflow</text>

    <text x="90" y="245" font-size="18" font-weight="600" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">01 Script — DeepSeek/Claude</text>
    <text x="90" y="272" font-size="16" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">50-80 char quote, elder speech style</text>

    <text x="90" y="322" font-size="18" font-weight="600" fill="{GREEN}" font-family="Inter, Helvetica, sans-serif">02 Voice — 11Labs/Volc Engine</text>
    <text x="90" y="349" font-size="16" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Elder male/female voice, natural tone</text>

    <text x="90" y="399" font-size="18" font-weight="600" fill="{PURPLE}" font-family="Inter, Helvetica, sans-serif">03 Footage — Free stock/AI gen</text>
    <text x="90" y="426" font-size="16" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Rural scenes: fields, old houses, tools</text>

    <text x="90" y="476" font-size="18" font-weight="600" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">04 Edit — CapCut 1-tap export</text>
    <text x="90" y="503" font-size="16" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">Script + voice + BGM + subs = done</text>

    <rect x="60" y="570" width="904" height="100" rx="12" fill="{GREEN}" opacity="0.06"/>
    <text x="100" y="610" font-size="18" font-weight="700" fill="{GREEN}" font-family="Inter, Helvetica, sans-serif">Pro Tips</text>
    <text x="100" y="643" font-size="16" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• Quotes need emotional tension + payoff</text>
    <text x="100" y="668" font-size="16" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• Big text cover + elder avatar image</text>

    <text x="60" y="770" font-size="14" fill="{TEXT_LIGHT}" font-family="Inter, Helvetica, sans-serif">#AIvideo #CapCut #AIVoiceover #WeChatCreator</text>
  </svg>'''


def card_money():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <defs>
      <radialGradient id="radial" cx="50%" cy="30%" r="55%">
        <stop offset="0%" stop-color="#1E1B4B"/>
        <stop offset="100%" stop-color="{BG}"/>
      </radialGradient>
      {shadow_filter()}
    </defs>
    <rect width="{W}" height="{H}" fill="url(#radial)"/>

    <rect width="{W}" height="120" fill="{PURPLE}" opacity="0.06"/>
    <text x="60" y="50" font-size="16" font-weight="600" fill="{PURPLE}" font-family="Inter, Helvetica, sans-serif">CARD 03</text>
    <text x="60" y="90" font-size="36" font-weight="800" fill="{TEXT_WHITE}" font-family="Inter, Helvetica, sans-serif">Revenue Breakdown</text>

    <rect x="60" y="155" width="430" height="120" rx="14" fill="{AMBER}" opacity="0.08"/>
    <text x="90" y="195" font-size="16" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">PER 10K VIEWS</text>
    <text x="90" y="250" font-size="34" font-weight="800" fill="{AMBER}" font-family="Inter, Helvetica, sans-serif">$4-12 USD</text>

    <rect x="530" y="155" width="434" height="120" rx="14" fill="{GREEN}" opacity="0.08"/>
    <text x="560" y="195" font-size="16" fill="{GREEN}" font-family="Inter, Helvetica, sans-serif">PER 1M VIEWS</text>
    <text x="560" y="250" font-size="34" font-weight="800" fill="{GREEN}" font-family="Inter, Helvetica, sans-serif">$400-1,100</text>

    <rect x="60" y="310" width="904" height="170" rx="14" fill="#FFFFFF" opacity="0.05" filter="url(#shadow)"/>
    <text x="90" y="355" font-size="20" font-weight="700" fill="{TEXT_WHITE}" font-family="Inter, Helvetica, sans-serif">Operating Model</text>
    <text x="90" y="395" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• Post 3 videos/day, 2-5M monthly views</text>
    <text x="90" y="428" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• Steady account: $400-1,100/mo</text>
    <text x="90" y="461" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• One viral hit (1M+) = instant $1,100+</text>

    <rect x="60" y="515" width="904" height="170" rx="12" fill="#FFFFFF" opacity="0.03"/>
    <text x="100" y="560" font-size="20" font-weight="700" fill="{PURPLE}" font-family="Inter, Helvetica, sans-serif">Why Enter Now</text>
    <text x="100" y="600" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• Platform traffic support for new creators</text>
    <text x="100" y="635" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• Rural quote niche is not saturated</text>
    <text x="100" y="670" font-size="18" fill="{TEXT_MUTED}" font-family="Inter, Helvetica, sans-serif">• AI batch = 1 person runs 10 accounts</text>

    <text x="60" y="770" font-size="14" fill="{TEXT_LIGHT}" font-family="Inter, Helvetica, sans-serif">#AIsidehustle #MakeMoneyOnline #WeChat</text>
  </svg>'''


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)

    svgs = [
        ("ai-rural-quotes-tw-cover.svg", cover()),
        ("ai-rural-quotes-tw-card-why.svg", card_why()),
        ("ai-rural-quotes-tw-card-how.svg", card_how()),
        ("ai-rural-quotes-tw-card-money.svg", card_money()),
    ]

    for name, svg in svgs:
        path = os.path.join(out_dir, name)
        with open(path, "w") as f:
            f.write(svg)
        print(f"✅ {path}")

    print("\n🎨 Rendering PNGs with Inkscape...")
    for name, _ in svgs:
        svg_path = os.path.join(out_dir, name)
        png_file = name.replace(".svg", ".png")
        png_path = os.path.join(out_dir, png_file)
        result = subprocess.run(
            ["inkscape", svg_path, "--export-type=png",
             f"--export-filename={png_path}", "-w", str(W), "-h", str(H)],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode == 0 and os.path.getsize(png_path) > 50000:
            print(f"✅ {png_file} ({os.path.getsize(png_path)//1024}KB)")
        else:
            print(f"❌ {png_file} — {result.stderr[:200] if result.stderr else 'blank/small file'}")

    print("\n✨ Done!")


if __name__ == "__main__":
    main()
