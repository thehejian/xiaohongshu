#!/usr/bin/env python3
"""为worldcup-young-stars图片添加中文文字 - 调整版"""
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/image-cards/worldcup-young-stars"
OUTPUT_DIR = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/worldcup-young-stars-xhs"

def get_font(size):
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                continue
    return ImageFont.load_default()

def add_cover_text(img_path, output_path):
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    title_font = get_font(80)
    subtitle_font = get_font(52)
    
    title = "身价大洗牌！"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, 100), title, fill="#1E293B", font=title_font)
    
    subtitle = "谁是美加墨新任太子？"
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sw = bbox[2] - bbox[0]
    draw.text(((w - sw) // 2, 230), subtitle, fill="#E8655A", font=subtitle_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)

def add_player_card_text(img_path, output_path, name, info, stats):
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    name_font = get_font(72)
    info_font = get_font(44)
    stats_font = get_font(40)
    
    # 姓名
    bbox = draw.textbbox((0, 0), name, font=name_font)
    nw = bbox[2] - bbox[0]
    draw.text(((w - nw) // 2, 80), name, fill="#1E293B", font=name_font)
    
    # 信息
    bbox = draw.textbbox((0, 0), info, font=info_font)
    iw = bbox[2] - bbox[0]
    draw.text(((w - iw) // 2, 180), info, fill="#E8655A", font=info_font)
    
    # 数据
    bbox = draw.textbbox((0, 0), stats, font=stats_font)
    sw = bbox[2] - bbox[0]
    draw.text(((w - sw) // 2, h - 150), stats, fill="#1E293B", font=stats_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)

def add_ranking_text(img_path, output_path):
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    title_font = get_font(60)
    rank_font = get_font(44)
    
    title = "身价暴涨预测榜"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, 70), title, fill="#1E293B", font=title_font)
    
    ranks = [
        ("No.1  亚马尔", "2亿欧潜力"),
        ("No.2  罗克", "1.2亿欧起步"),
        ("No.3  穆西亚拉", "已破1亿"),
        ("No.4  萨利巴", "8000万→1亿"),
        ("No.5  阿斯拉尼", "6000万→8000万"),
    ]
    
    y_start = 190
    spacing = 130
    
    for i, (player, value) in enumerate(ranks):
        y = y_start + i * spacing
        
        # 玩家名（左侧）
        bbox = draw.textbbox((0, 0), player, font=rank_font)
        pw = bbox[2] - bbox[0]
        draw.text((100, y), player, fill="#1E293B", font=rank_font)
        
        # 身价（右侧）
        bbox = draw.textbbox((0, 0), value, font=rank_font)
        vw = bbox[2] - bbox[0]
        draw.text((w - 100 - vw, y), value, fill="#E8655A", font=rank_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)

def add_ending_text(img_path, output_path):
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    
    q_font = get_font(60)
    cta_font = get_font(48)
    
    q = "谁是你的世界杯黑马？"
    bbox = draw.textbbox((0, 0), q, font=q_font)
    qw = bbox[2] - bbox[0]
    draw.text(((w - qw) // 2, 250), q, fill="#1E293B", font=q_font)
    
    cta = "评论区押宝👇"
    bbox = draw.textbbox((0, 0), cta, font=cta_font)
    cw = bbox[2] - bbox[0]
    draw.text(((w - cw) // 2, 420), cta, fill="#E8655A", font=cta_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    add_cover_text(f"{BASE_DIR}/01-cover0_0.png", f"{OUTPUT_DIR}/01-cover.png")
    print("✓ 封面")
    
    add_player_card_text(f"{BASE_DIR}/02-yamal0_0.png", f"{OUTPUT_DIR}/02-yamal.png",
        "亚马尔", "西班牙 · 17岁 · 巴萨", "盘带·视野·传球 顶级")
    print("✓ 亚马尔卡")
    
    add_player_card_text(f"{BASE_DIR}/03-musiala0_0.png", f"{OUTPUT_DIR}/03-musiala.png",
        "穆西亚拉", "德国 · 21岁 · 拜仁", "左右脚都能踢 能突能传")
    print("✓ 穆西亚拉卡")
    
    add_player_card_text(f"{BASE_DIR}/04-roak-saliba0_0.png", f"{OUTPUT_DIR}/04-roak-saliba.png",
        "罗克 & 萨利巴", "巴西18岁锋线 / 法国22岁中卫", "速度爆发力 vs 防线定海神针")
    print("✓ 罗克&萨利巴卡")
    
    add_ranking_text(f"{BASE_DIR}/05-ranking0_0.png", f"{OUTPUT_DIR}/05-ranking.png")
    print("✓ 身价榜单")
    
    add_ending_text(f"{BASE_DIR}/06-ending0_0.png", f"{OUTPUT_DIR}/06-ending.png")
    print("✓ 结尾卡")
    
    print("\n全部完成！")
