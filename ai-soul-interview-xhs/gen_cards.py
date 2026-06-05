#!/usr/bin/env python3
"""Light (CN) + Dark (EN) cards — flex-centered, no shadows, no gray/dark text, super large font."""
import subprocess, os
ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Light palette ──
LBG  = "#FAF7F2"
LBG2 = "#F5F0E8"
LCD  = "#FFFFFF"
LTXT = "#1E293B"
BLU  = "#2563EB"
PUR  = "#7C3AED"
PNK  = "#EC4899"
GRN  = "#059669"
ORN  = "#D97706"
TEL  = "#0D9488"
IND  = "#4F46E5"

# ── Dark palette ──
DBG  = "#070717"
DBG2 = "#0B0B20"
DCD  = "#111130"
DTXT = "#E2E8F0"
DBLU = "#60A5FA"
DPUR = "#A78BFA"
DPNK = "#F472B6"
DGRN = "#34D399"
DORN = "#FBBF24"
DTEL = "#2DD4BF"
DIND = "#818CF8"

FZ = "PingFang SC, Heiti SC, STHeiti, Hiragino Sans GB, Microsoft YaHei, sans-serif"
FE = "Inter, SF Pro Display, Helvetica Neue, Arial, sans-serif"

# ── vertical centering helpers ──
# SVG y is baseline; visual center ≈ baseline - fs*0.35
def v1(ry, rh, fs):
    return ry + rh // 2 + int(fs * 0.35)

def v2(ry, rh, fs1, fs2, gap=10):
    tv = int(0.75 * fs1) + gap + int(0.75 * fs2)
    vt = ry + (rh - tv) // 2
    return vt + int(0.7 * fs1), vt + int(0.75 * fs1) + gap + int(0.7 * fs2)

def v3(ry, rh, fs1, fs2, gap=8):
    return v2(ry, rh, fs1, fs2, gap)

def lbg(w, h):
    return f'''<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{LBG}"/><stop offset="1" stop-color="{LBG2}"/></linearGradient></defs>
<rect width="{w}" height="{h}" fill="url(#g)"/>
<circle cx="80" cy="80" r="200" fill="{PUR}" opacity=".04"/>
<circle cx="{w-80}" cy="{h-60}" r="240" fill="{BLU}" opacity=".04"/>'''

def dbg(w, h):
    return f'''<defs><radialGradient id="g" cx="50%" cy="50%" r="70%"><stop offset="0" stop-color="{DBG2}"/><stop offset="1" stop-color="{DBG}"/></radialGradient></defs>
<rect width="{w}" height="{h}" fill="url(#g)"/>
<circle cx="80" cy="80" r="200" fill="{DPUR}" opacity=".06"/>
<circle cx="{w-80}" cy="{h-60}" r="240" fill="{DBLU}" opacity=".06"/>'''

def ir(x, y, w, h, c, o):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{c}" opacity="{o}"/>'

# ═══════════════ LIGHT (Chinese) ═══════════════

def L_cover():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{lbg(1024,1024)}
<text x="512" y="340" text-anchor="middle" font-family="{FZ}" font-size="120" font-weight="900" fill="{LTXT}" letter-spacing="-6">AI灵魂拷问</text>
<text x="512" y="480" text-anchor="middle" font-family="{FZ}" font-size="52" font-weight="800" fill="{PUR}" letter-spacing="2">30天扒光潜意识</text>
<line x1="280" y1="570" x2="744" y2="570" stroke="{BLU}" stroke-width="4" stroke-linecap="round" opacity=".35"/>
<text x="512" y="660" text-anchor="middle" font-family="{FZ}" font-size="28" font-weight="600" fill="{TEL}">比MBTI深100倍 · 比塔罗准100倍</text>
<text x="512" y="730" text-anchor="middle" font-family="{FZ}" font-size="24" font-weight="500" fill="{IND}">每天30分钟 · 连续30天</text>
</svg>'''

def L_1():
    d = [("1  拆防御", "温和问题让你放松警惕", BLU),
         ("2  追矛盾", "对比前后不一致的陈述", PUR),
         ("3  挖根源", "追到童年·家庭·创伤层", PNK),
         ("4  重建", "重构自我认知", GRN)]
    rw, rh, gp = 760, 152, 44
    ox, oy, ow, oh = 62, 60, 900, 904
    th = len(d) * rh + (len(d) - 1) * gp
    sy = oy + (oh - th) // 2
    sx = ox + (ow - rw) // 2
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{lbg(1024,1024)}
<rect x="{ox}" y="{oy}" width="{ow}" height="{oh}" rx="36" fill="{LCD}"/>'''
    y = sy
    for t, ds, c in d:
        y1, y2 = v2(y, rh, 40, 26)
        s += f'''
{ir(sx, y, rw, rh, c, .08)}
<text x="{cx(sx, rw)}" y="{y1}" text-anchor="middle" font-family="{FZ}" font-size="40" font-weight="800" fill="{c}">{t}</text>
<text x="{cx(sx, rw)}" y="{y2}" text-anchor="middle" font-family="{FZ}" font-size="26" font-weight="500" fill="{LTXT}">{ds}</text>'''
        y += rh + gp
    return s + "\n</svg>"

def cx(x, w):
    return x + w // 2

def L_2():
    d = [("MBTI", "15分钟", "表面标签", BLU),
         ("塔罗牌", "30分钟", "模棱两可", ORN),
         ("AI灵魂拷问", "30天", "潜意识层", PUR)]
    rw, rh, gp = 760, 160, 36
    ox, oy, ow, oh = 62, 60, 900, 904
    th = len(d) * rh + (len(d) - 1) * gp
    sy = oy + (oh - th) // 2
    sx = ox + (ow - rw) // 2
    c1x, c2x, c3x = sx + rw // 4, cx(sx, rw) - 20, cx(sx, rw) + 120
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{lbg(1024,1024)}
<rect x="{ox}" y="{oy}" width="{ow}" height="{oh}" rx="36" fill="{LCD}"/>'''
    y = sy
    for nm, tm, dp, c in d:
        hl = (nm == "AI灵魂拷问")
        fs = 44 if hl else 34
        fw = "900" if hl else "700"
        yb = v1(y, rh, fs)
        bd = f'stroke="{c}" stroke-width="2"' if hl else ''
        op = ".10" if hl else ".08"
        s += f'''
<rect x="{sx}" y="{y}" width="{rw}" height="{rh}" rx="16" fill="{c}" opacity="{op}" {bd}/>
<text x="{c1x}" y="{yb}" text-anchor="middle" font-family="{FZ}" font-size="{fs}" font-weight="{fw}" fill="{c}">{nm}</text>
<text x="{c2x}" y="{yb+4}" text-anchor="middle" font-family="{FZ}" font-size="26" font-weight="600" fill="{LTXT}">{tm}</text>
<text x="{c3x}" y="{yb+4}" text-anchor="middle" font-family="{FZ}" font-size="26" font-weight="600" fill="{LTXT}">{dp}</text>'''
        y += rh + gp
    return s + "\n</svg>"

def L_3():
    d = [("高频词云", "应该 · 别人 · 不敢 · 等以后", BLU),
         ("核心矛盾", "理想 vs 现实的差距在哪里", PUR),
         ("防御模式", "你用什么方式逃避自己", PNK),
         ("底层信念", "童年种下的那些真理", ORN),
         ("重建路径", "从认知到行动的具体步骤", GRN)]
    rw, rh, gp = 820, 128, 32
    ox, oy, ow, oh = 62, 60, 900, 904
    th = len(d) * rh + (len(d) - 1) * gp
    sy = oy + (oh - th) // 2
    sx = ox + (ow - rw) // 2
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{lbg(1024,1024)}
<rect x="{ox}" y="{oy}" width="{ow}" height="{oh}" rx="36" fill="{LCD}"/>'''
    y = sy
    for t, ds, c in d:
        y1, y2 = v2(y, rh, 34, 22)
        s += f'''
{ir(sx, y, rw, rh, c, .08)}
<text x="{cx(sx, rw)}" y="{y1}" text-anchor="middle" font-family="{FZ}" font-size="34" font-weight="800" fill="{c}">{t}</text>
<text x="{cx(sx, rw)}" y="{y2}" text-anchor="middle" font-family="{FZ}" font-size="22" font-weight="500" fill="{LTXT}">{ds}</text>'''
        y += rh + gp
    return s + "\n</svg>"

# ═══════════════ DARK (English) ═══════════════

def D_cover():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{dbg(1024,1024)}
<text x="512" y="300" text-anchor="middle" font-family="{FE}" font-size="76" font-weight="800" fill="{DTEL}" letter-spacing="3">AI SOUL</text>
<text x="512" y="400" text-anchor="middle" font-family="{FE}" font-size="76" font-weight="800" fill="{DPUR}" letter-spacing="3">INTERVIEW</text>
<line x1="260" y1="470" x2="764" y2="470" stroke="{DBLU}" stroke-width="4" stroke-linecap="round" opacity=".4"/>
<text x="512" y="550" text-anchor="middle" font-family="{FE}" font-size="32" font-weight="700" fill="{DORN}">30 Days to Bare Your Soul</text>
<text x="512" y="610" text-anchor="middle" font-family="{FE}" font-size="22" font-weight="500" fill="{DTXT}">Deeper than MBTI · More accurate than Tarot</text>
<text x="512" y="660" text-anchor="middle" font-family="{FE}" font-size="20" font-weight="400" fill="{DIND}">30 min a day · 30 consecutive days</text>
</svg>'''

def D_1():
    d = [("CRACK DEFENSES", "Gentle questions lower your guard", DBLU),
         ("FIND GAPS", "AI contrasts your contradictions", DPUR),
         ("TRACE ROOTS", "Back to childhood and trauma", DPNK),
         ("REBUILD", "Reshape self-awareness from scratch", DGRN)]
    rw, rh, gp = 800, 140, 40
    ox, oy, ow, oh = 52, 50, 920, 924
    th = len(d) * rh + (len(d) - 1) * gp
    sy = oy + (oh - th) // 2
    sx = ox + (ow - rw) // 2
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{dbg(1024,1024)}
<rect x="{ox}" y="{oy}" width="{ow}" height="{oh}" rx="36" fill="{DCD}"/>'''
    y = sy
    for t, ds, c in d:
        y1, y2 = v2(y, rh, 28, 18)
        s += f'''
{ir(sx, y, rw, rh, c, .12)}
<text x="{cx(sx, rw)}" y="{y1}" text-anchor="middle" font-family="{FE}" font-size="28" font-weight="800" fill="{c}">{t}</text>
<text x="{cx(sx, rw)}" y="{y2}" text-anchor="middle" font-family="{FE}" font-size="18" font-weight="500" fill="{DTXT}">{ds}</text>'''
        y += rh + gp
    return s + "\n</svg>"

def D_2():
    d = [("MBTI", "15 min", "Surface labels", DBLU),
         ("TAROT", "30 min", "Vague comfort", DORN),
         ("AI SOUL", "30 days", "Subconscious", DPUR)]
    rw, rh, gp = 800, 152, 34
    ox, oy, ow, oh = 52, 50, 920, 924
    th = len(d) * rh + (len(d) - 1) * gp
    sy = oy + (oh - th) // 2
    sx = ox + (ow - rw) // 2
    c1x, c2x, c3x = sx + rw // 4, cx(sx, rw), cx(sx, rw) + 140
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{dbg(1024,1024)}
<rect x="{ox}" y="{oy}" width="{ow}" height="{oh}" rx="36" fill="{DCD}"/>'''
    y = sy
    for nm, tm, dp, c in d:
        hl = (nm == "AI SOUL")
        fs = 40 if hl else 28
        fw = "900" if hl else "700"
        yb = v1(y, rh, fs)
        bd = f'stroke="{c}" stroke-width="2"' if hl else ''
        op = ".10" if hl else ".12"
        s += f'''
<rect x="{sx}" y="{y}" width="{rw}" height="{rh}" rx="16" fill="{c}" opacity="{op}" {bd}/>
<text x="{c1x}" y="{yb}" text-anchor="middle" font-family="{FE}" font-size="{fs}" font-weight="{fw}" fill="{c}">{nm}</text>
<text x="{c2x}" y="{yb}" text-anchor="middle" font-family="{FE}" font-size="22" font-weight="600" fill="{DTXT}">{tm}</text>
<text x="{c3x}" y="{yb}" text-anchor="middle" font-family="{FE}" font-size="22" font-weight="600" fill="{DTXT}">{dp}</text>'''
        y += rh + gp
    return s + "\n</svg>"

def D_3():
    d = [("WORD CLOUD", "Should · Others · Afraid · Someday", DBLU),
         ("CORE CONFLICT", "Ideal life vs what you actually do", DPUR),
         ("DEFENSE MODE", "How you run from yourself", DPNK),
         ("DEEP BELIEFS", "Childhood truths you still carry", DORN),
         ("REBUILD PATH", "From insight to daily action", DGRN)]
    rw, rh, gp = 830, 118, 30
    ox, oy, ow, oh = 52, 50, 920, 924
    th = len(d) * rh + (len(d) - 1) * gp
    sy = oy + (oh - th) // 2
    sx = ox + (ow - rw) // 2
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024">
{dbg(1024,1024)}
<rect x="{ox}" y="{oy}" width="{ow}" height="{oh}" rx="36" fill="{DCD}"/>'''
    y = sy
    for t, ds, c in d:
        y1, y2 = v2(y, rh, 24, 17)
        s += f'''
{ir(sx, y, rw, rh, c, .12)}
<text x="{cx(sx, rw)}" y="{y1}" text-anchor="middle" font-family="{FE}" font-size="24" font-weight="800" fill="{c}">{t}</text>
<text x="{cx(sx, rw)}" y="{y2}" text-anchor="middle" font-family="{FE}" font-size="17" font-weight="500" fill="{DTXT}">{ds}</text>'''
        y += rh + gp
    return s + "\n</svg>"

# ═══════════════ MAIN ═══════════════

if __name__ == "__main__":
    cards = [
        ("card-cover", L_cover(), 1024, 1024),
        ("card-1", L_1(), 1024, 1024),
        ("card-2", L_2(), 1024, 1024),
        ("card-3", L_3(), 1024, 1024),
        ("card-cover-dark", D_cover(), 1024, 1024),
        ("card-1-dark", D_1(), 1024, 1024),
        ("card-2-dark", D_2(), 1024, 1024),
        ("card-3-dark", D_3(), 1024, 1024),
    ]
    for nm, svg, w, h in cards:
        sp = os.path.join(ROOT, f"{nm}.svg")
        pp = os.path.join(ROOT, f"{nm}.png")
        with open(sp, "w") as f:
            f.write(svg)
        r = subprocess.run(["inkscape", sp, "-o", pp, "-w", str(w), "-h", str(h)], capture_output=True, text=True)
        if r.returncode:
            print(f"  {nm}: ERROR - {r.stderr.strip()}")
        else:
            print(f"  {nm}.png ({os.path.getsize(pp)//1024} KB)")
    print("Done!")