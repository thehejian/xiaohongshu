#!/usr/bin/env python3
import os, shutil, subprocess, sys

W, H = 1792, 1024
bg_dark = "#0B1027"
dark_accent = "#1E293B"
text_light = "#FFFFFF"
brand_accent = "#F59E0B"
muted_light = "#94A3B8"

def bg():
    return f'''<defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" style="stop-color:#111827"/>
      <stop offset="100%" style="stop-color:{bg_dark}"/>
    </radialGradient>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>'''

def page_num(n, total):
    return f'<text x="{W-60}" y="{H-50}" font-family="Inter, sans-serif" font-size="22" fill="{muted_light}" text-anchor="end">{n}/{total}</text>'

CARDS = []

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  <rect x="0" y="0" width="{W}" height="6" fill="{brand_accent}"/>
  <text x="{W//2}" y="380" font-family="Inter, sans-serif" font-size="80" font-weight="bold" fill="{text_light}" text-anchor="middle">Learn Slow Enough</text>
  <text x="{W//2}" y="490" font-family="Inter, sans-serif" font-size="80" font-weight="bold" fill="{brand_accent}" text-anchor="middle">No Need to Learn</text>
  <text x="{W//2}" y="580" font-family="Inter, sans-serif" font-size="80" font-weight="bold" fill="{brand_accent}" text-anchor="middle">At All</text>
  <line x1="620" y1="630" x2="{W-620}" y2="630" stroke="#334155" stroke-width="3" stroke-linecap="round"/>
  <text x="{W//2}" y="730" font-family="Inter, sans-serif" font-size="34" fill="{muted_light}" text-anchor="middle">Anti-Anxiety Guide for the AI Era</text>
  <text x="{W//2}" y="790" font-family="Inter, sans-serif" font-size="26" fill="#475569" text-anchor="middle">Slow is smooth. Smooth is fast.</text>
  {page_num(1, 4)}
</svg>''')

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  <rect x="0" y="0" width="{W}" height="6" fill="{brand_accent}"/>
  <text x="100" y="140" font-family="Inter, sans-serif" font-size="28" fill="{muted_light}">01</text>
  <text x="100" y="200" font-family="Inter, sans-serif" font-size="56" font-weight="bold" fill="{text_light}">The Truth About</text>
  <text x="100" y="270" font-family="Inter, sans-serif" font-size="56" font-weight="bold" fill="{brand_accent}">AI Anxiety</text>
  <line x1="100" y1="320" x2="420" y2="320" stroke="{brand_accent}" stroke-width="4" stroke-linecap="round"/>
  <text x="100" y="430" font-family="Inter, sans-serif" font-size="36" fill="{text_light}">Reading 100 AI articles a day</text>
  <text x="100" y="490" font-family="Inter, sans-serif" font-size="36" fill="{text_light}">Bookmarking 50 tools</text>
  <text x="100" y="550" font-family="Inter, sans-serif" font-size="36" fill="{text_light}">Buying 3 courses</text>
  <text x="100" y="640" font-family="Inter, sans-serif" font-size="36" font-weight="bold" fill="{brand_accent}">And feeling even more anxious</text>
  <line x1="100" y1="710" x2="{W-100}" y2="710" stroke="#1E293B" stroke-width="2"/>
  <text x="100" y="790" font-family="Inter, sans-serif" font-size="28" fill="{muted_light}">90% of AI news means nothing 3 months later</text>
  <text x="100" y="850" font-family="Inter, sans-serif" font-size="28" fill="{muted_light}">Your anxiety drains more energy than AI ever will</text>
  {page_num(2, 4)}
</svg>''')

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  <rect x="0" y="0" width="{W}" height="6" fill="{brand_accent}"/>
  <text x="100" y="140" font-family="Inter, sans-serif" font-size="28" fill="{muted_light}">02</text>
  <text x="100" y="200" font-family="Inter, sans-serif" font-size="56" font-weight="bold" fill="{text_light}">Three Powers of</text>
  <text x="100" y="270" font-family="Inter, sans-serif" font-size="56" font-weight="bold" fill="{brand_accent}">Going Slow</text>
  <line x1="100" y1="320" x2="420" y2="320" stroke="{brand_accent}" stroke-width="4" stroke-linecap="round"/>
  <rect x="100" y="370" width="{W-200}" height="110" rx="16" fill="#1E293B"/>
  <circle cx="140" cy="425" r="10" fill="{brand_accent}"/>
  <text x="175" y="405" font-family="Inter, sans-serif" font-size="34" font-weight="bold" fill="{text_light}">Noise Filter</text>
  <text x="175" y="445" font-family="Inter, sans-serif" font-size="26" fill="{muted_light}">Automatically skip 90% of useless information</text>
  <rect x="100" y="500" width="{W-200}" height="110" rx="16" fill="#1E293B"/>
  <circle cx="140" cy="555" r="10" fill="{brand_accent}"/>
  <text x="175" y="535" font-family="Inter, sans-serif" font-size="34" font-weight="bold" fill="{text_light}">Depth Advantage</text>
  <text x="175" y="575" font-family="Inter, sans-serif" font-size="26" fill="{muted_light}">10 masterpieces with 1 tool > 10 dabbles with 20 tools</text>
  <rect x="100" y="630" width="{W-200}" height="110" rx="16" fill="#1E293B"/>
  <circle cx="140" cy="685" r="10" fill="{brand_accent}"/>
  <text x="175" y="665" font-family="Inter, sans-serif" font-size="34" font-weight="bold" fill="{text_light}">Timeless Skills</text>
  <text x="175" y="705" font-family="Inter, sans-serif" font-size="26" fill="{muted_light}">Prompt engineering · Data thinking · Problem decomposition</text>
  <text x="100" y="880" font-family="Inter, sans-serif" font-size="28" fill="{brand_accent}">Fast people chase trends. Slow people see what matters.</text>
  {page_num(3, 4)}
</svg>''')

CARDS.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  {bg()}
  <rect x="0" y="0" width="{W}" height="6" fill="{brand_accent}"/>
  <rect x="100" y="280" width="{W-200}" height="460" rx="24" fill="#1E293B"/>
  <text x="{W//2}" y="420" font-family="Inter, sans-serif" font-size="52" font-weight="bold" fill="{text_light}" text-anchor="middle">AI won't replace</text>
  <text x="{W//2}" y="495" font-family="Inter, sans-serif" font-size="52" font-weight="bold" fill="{brand_accent}" text-anchor="middle">"slow learners"</text>
  <text x="{W//2}" y="580" font-family="Inter, sans-serif" font-size="34" fill="{muted_light}" text-anchor="middle">It will replace those who</text>
  <text x="{W//2}" y="640" font-family="Inter, sans-serif" font-size="34" fill="{text_light}" text-anchor="middle">"only bookmark, never do"</text>
  <line x1="620" y1="690" x2="{W-620}" y2="690" stroke="{brand_accent}" stroke-width="3" stroke-linecap="round"/>
  <text x="{W//2}" y="820" font-family="Inter, sans-serif" font-size="28" fill="{muted_light}" text-anchor="middle">Like &amp; Share — now go take action</text>
  {page_num(4, 4)}
</svg>''')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for i, svg in enumerate(CARDS, 1):
    svg_path = f"card-dark-{i}.svg"
    png_path = f"card-dark-{i}.png"
    with open(svg_path, "w") as f:
        f.write(svg)
    print(f"Generated {svg_path}")

    if sys.platform == "darwin":
        inkscape = shutil.which("inkscape") or "inkscape"
        subprocess.run([inkscape, svg_path, "--export-filename", png_path, f"--export-width={W}", f"--export-height={H}"], check=True)
        print(f"Converted to {png_path}")
    else:
        subprocess.run(["inkscape", svg_path, "--export-filename", png_path], check=True)
        print(f"Converted to {png_path}")

print("Done!")