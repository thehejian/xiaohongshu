#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update all image prompts (topics 43-100) with period-accurate Han dynasty details.
Adds: hairstyles, clothing, architecture, utensils, war tension.
Strategy: insert period details into the style description, preserving all original text."""
import re, os

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

WAR = {64, 67, 70, 74, 77, 81, 86, 98}

# English style additions by topic type
EN_STYLE = {
    "war": "Han iron lamellar armor (札甲) on soldiers, ring-pommel dao (环首刀), Han crossbow (弩), tense battlefield atmosphere with charging cavalry, dust and urgency",
    "court": "Han dynasty shenyi robe with crossed-collar right closure (交领右衽), traditional topknot with guan headpiece (冠), palace with rammed-earth walls and tiled roof, low tables and floor mats",
    "daily": "Han commoners in hemp short jacket (短褐) with cloth headwrap, period pottery and wooden utensils",
    "culture": "Han dynasty shenyi robe with crossed-collar right closure (交领右衽), traditional topknot with guan headpiece (冠), period writing implements with bamboo slips and brush",
    "other": "Han dynasty period setting with appropriate clothing and architecture",
}

# Chinese style additions by topic type
CN_STYLE = {
    "war": "汉军铁甲札甲，环首刀，汉弩，紧张战场气氛，骑兵冲锋动感，尘土飞扬",
    "court": "汉式交领右衽深衣，丝帛衣料，男子束发戴冠，女子高髻，汉代宫室夯土墙瓦顶，席地而坐低案陈设",
    "daily": "汉代百姓短褐麻衣，布巾裹头，陶器木器日用",
    "culture": "汉式交领右衽深衣，束发戴冠，竹简毛笔书写用具",
    "other": "汉代背景，符合时代的人物服饰与器物",
}

def get_type(num):
    if num in WAR:
        return "war"
    elif num in {43, 44, 47, 48, 50, 51, 54, 56, 59, 60, 61, 62, 63, 66, 68, 69,
                 75, 76, 78, 79, 80, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 99, 100}:
        return "court"
    elif num in {46, 58, 65, 72, 73, 94}:
        return "culture"
    elif num in {45, 49, 52, 84, 95}:
        return "daily"
    else:
        return "other"

# Read folder mapping
with open(f"{BASE}/正文提示词.md") as f:
    doc = f.read()
blocks = re.split(r'\n(?=## 主题 \d+[：:])', doc)
folder_map = {}
for num in range(43, 101):
    for b in blocks:
        if f"## 主题 {num}" in b:
            fm = re.search(r'\*\*文件夹\*\*:\s*\x60(.+?)\x60', b)
            if fm:
                folder_map[num] = fm.group(1)

updated = 0
for num in range(43, 101):
    folder = folder_map.get(num)
    if not folder:
        continue
    prompt_dir = f"{BASE}/image-cards/{folder}/prompts"
    if not os.path.isdir(prompt_dir):
        continue
    
    t = get_type(num)
    en_add = EN_STYLE[t]
    cn_add = CN_STYLE[t]
    
    for fname in sorted(os.listdir(prompt_dir)):
        fpath = f"{prompt_dir}/{fname}"
        if not os.path.isfile(fpath):
            continue
        with open(fpath) as f:
            content = f.read()
        
        if fname == "01-cover.md":
            # English cover prompt - insert after the misty atmosphere description
            # Pattern: "...misty atmosphere. Scene description. Chinese title..."
            old = "misty atmosphere."
            if old in content:
                new = f"misty atmosphere. {en_add}."
                content = content.replace(old, new, 1)
                with open(fpath, 'w') as f:
                    f.write(content)
                updated += 1
        else:
            # Chinese prompt - insert after the style prefix
            # Pattern: "水墨风...雾气氛围。Scene description。题字「...」"
            old = "雾气氛围。"
            if old in content:
                new = f"雾气氛围。{cn_add}。"
                content = content.replace(old, new, 1)
                with open(fpath, 'w') as f:
                    f.write(content)
                updated += 1

print(f"Updated {updated} prompt files across topics 43-100")