#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Clean ALL prompt files by removing all known additions, then re-adding clean ones once."""
import re, os

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

WAR = {64, 67, 70, 74, 77, 81, 86, 98}

EN_STYLE = {
    "war": "Han iron lamellar armor (札甲) on soldiers, ring-pommel dao (环首刀), Han crossbow (弩), tense battlefield atmosphere with charging cavalry, dust and urgency",
    "court": "Han dynasty shenyi robe with crossed-collar right closure (交领右衽), traditional topknot with guan headpiece (冠), palace with rammed-earth walls and tiled roof, low tables and floor mats",
    "daily": "Han commoners in hemp short jacket (短褐) with cloth headwrap, period pottery and wooden utensils",
    "culture": "Han dynasty shenyi robe with crossed-collar right closure (交领右衽), traditional topknot with guan headpiece (冠), period writing implements with bamboo slips and brush",
    "other": "Han dynasty period setting with appropriate clothing and architecture",
}

CN_STYLE = {
    "war": "汉军铁甲札甲，环首刀，汉弩，紧张战场气氛，骑兵冲锋动感，尘土飞扬",
    "court": "汉式交领右衽深衣，丝帛衣料，男子束发戴冠，女子高髻，汉代宫室夯土墙瓦顶，席地而坐低案陈设",
    "daily": "汉代百姓短褐麻衣，布巾裹头，陶器木器日用",
    "culture": "汉式交领右衽深衣，束发戴冠，竹简毛笔书写用具",
    "other": "汉代背景，符合时代的人物服饰与器物",
}

# ALL known additions (both old and new formats) - complete list of strings to remove
ALL_EN_OLD = [
    "tense battlefield atmosphere, charging cavalry without stirrups, Han soldiers in lamellar iron armor (札甲), tense atmosphere, dynamic charging motion, war horses galloping, dust clouds, urgency",
    "Han-dynasty shenyi robe with crossed-collar right closure (交领右衽), silk fabric, traditional Han topknot with guan headpiece (汉式发髻冠), Han palace with rammed-earth walls, tiled roof, dougong brackets, low lacquer table (案), floor mats (席), Han palace hall with floor mats, low tables, silk curtains",
    "Han palace with rammed-earth walls, tiled roof, dougong brackets, low lacquer table (案), floor mats (席)",
    "Han-dynasty shenyi robe with crossed-collar right closure (交领右衽), silk fabric, traditional Han topknot with guan headpiece (汉式发髻冠)",
    "Han palace with rammed-earth walls, tiled roof, dougong brackets",
    "Han-dynasty shenyi robe with crossed-collar right closure",
    "traditional Han topknot with guan headpiece",
    "low lacquer table (案), floor mats (席)",
    "Han palace hall with floor mats, low tables, silk curtains",
    "Han palace with rammed-earth walls, tiled roof, dougong brackets, low lacquer table (案), floor mats (席), Han palace hall with floor mats, low tables, silk curtains",
    "Han dynasty shenyi robe with crossed-collar right closure (交领右衽), traditional topknot with guan headpiece (冠), palace with rammed-earth walls and tiled roof, low tables and floor mats",
    "Han iron lamellar armor (札甲) on soldiers, ring-pommel dao (环首刀), Han crossbow (弩), tense battlefield atmosphere with charging cavalry, dust and urgency",
    "Han commoners in hemp short jacket (短褐) with cloth headwrap, period pottery and wooden utensils",
    "Han dynasty period setting with appropriate clothing and architecture",
    "Han dynasty shenyi robe with crossed-collar right closure (交领右衽), traditional topknot with guan headpiece (冠), period writing implements with bamboo slips and brush",
]

ALL_CN_OLD = [
    "紧张战场气氛，骑兵冲锋（无马镫），汉军铁甲札甲，紧张感，骑兵冲锋动感，战马嘶鸣，尘土飞扬",
    "紧张感，骑兵冲锋动感，战马嘶鸣，尘土飞扬",
    "汉代宫室，夯土墙，瓦顶，斗拱席地而坐，低案陈设汉代殿堂，席地而坐，低案，丝帷",
    "汉代宫室，夯土墙，瓦顶，斗拱席地而坐，低案陈设",
    "汉代宫室，夯土墙，瓦顶，斗拱",
    "汉式交领右衽深衣，丝帛面料，汉式发髻戴冠，男子束发，紧张感，骑兵冲锋动感，战马嘶鸣，尘土飞扬",
    "汉式交领右衽深衣，丝帛面料，汉式发髻戴冠，男子束发",
    "汉式交领右衽深衣，束发戴冠，竹简毛笔书写用具",
    "汉式交领右衽深衣，丝帛衣料，男子束发戴冠，女子高髻，汉代宫室夯土墙瓦顶，席地而坐低案陈设",
    "汉代百姓短褐麻衣，布巾裹头，陶器木器日用",
    "汉代背景，符合时代的人物服饰与器物",
    "汉军铁甲札甲，环首刀，汉弩，紧张战场气氛，骑兵冲锋动感，尘土飞扬",
]

def get_type(num):
    if num in WAR:
        return "war"
    court_set = {43,44,47,48,50,51,54,56,59,60,61,62,63,66,68,69,75,76,78,79,80,82,83,85,87,88,89,90,91,92,93,99,100}
    if num in court_set:
        return "court"
    culture_set = {46,58,65,72,73,94}
    if num in culture_set:
        return "culture"
    daily_set = {45,49,52,84,95}
    if num in daily_set:
        return "daily"
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

fixed = 0
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
        
        original = content
        
        if fname == "01-cover.md":
            # Remove all known old additions
            for s in ALL_EN_OLD:
                content = content.replace(s, "").strip()
            # Clean up multiple spaces and punctuation
            content = content.replace("  ", " ").replace("  ", " ")
            content = content.replace("..", ".").replace("..", ".")
            # Re-add clean addition once after "misty atmosphere."
            if "misty atmosphere." in content:
                content = content.replace("misty atmosphere.", f"misty atmosphere. {en_add}.", 1)
        else:
            # Remove all known old additions
            for s in ALL_CN_OLD:
                content = content.replace(s, "").strip()
            # Clean up
            content = content.replace("。。", "。").replace("。。", "。")
            content = content.replace("，。", "。")
            # Re-add clean addition once after "雾气氛围"
            if "雾气氛围。" in content:
                content = content.replace("雾气氛围。", f"雾气氛围。{cn_add}。", 1)
        
        if content != original:
            with open(fpath, 'w') as f:
                f.write(content)
            fixed += 1

print(f"Fixed {fixed} prompt files")