#!/usr/bin/env python3
"""为worldcup-young-stars图片添加中文文字"""
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/image-cards/worldcup-young-stars"
OUTPUT_DIR = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/worldcup-young-stars-xhs"

# 尝试加载中文字体
def get_font(size):
    """获取中文字体，fallback到系统字体"""
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                continue
    return ImageFont.load_default()

def add_cover_text(img_path, output_path):
    """封面：添加标题"""
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    title_font = get_font(72)
    subtitle_font = get_font(48)
    
    # 标题
    title = "身价大洗牌！"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, 80), title, fill="#1E293B", font=title_font)
    
    # 副标题
    subtitle = "谁是美加墨新任太子？"
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    sw = bbox[2] - bbox[0]
    draw.text(((w - sw) // 2, 200), subtitle, fill="#E8655A", font=subtitle_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)

def add_player_card_text(img_path, output_path, name, info, stats):
    """球员卡：添加姓名、信息、数据"""
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    name_font = get_font(64)
    info_font = get_font(40)
    stats_font = get_font(36)
    
    # 姓名（顶部）
    bbox = draw.textbbox((0, 0), name, font=name_font)
    nw = bbox[2] - bbox[0]
    draw.text(((w - nw) // 2, 60), name, fill="#1E293B", font=name_font)
    
    # 信息（年龄/国籍/球队）
    bbox = draw.textbbox((0, 0), info, font=info_font)
    iw = bbox[2] - bbox[0]
    draw.text(((w - iw) // 2, 160), info, fill="#E8655A", font=info_font)
    
    # 数据（底部）
    bbox = draw.textbbox((0, 0), stats, font=stats_font)
    sw = bbox[2] - bbox[0]
    draw.text(((w - sw) // 2, h - 160), stats, fill="#1E293B", font=stats_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)

def add_ranking_text(img_path, output_path):
    """身价榜单：添加排名和身价"""
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    title_font = get_font(56)
    rank_font = get_font(40)
    
    # 标题
    title = "身价暴涨预测榜"
    bbox = draw.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) // 2, 60), title, fill="#1E293B", font=title_font)
    
    # 排名数据
    ranks = [
        ("No.1  亚马尔", "2亿欧潜力"),
        ("No.2  罗克", "1.2亿欧起步"),
        ("No.3  穆西亚拉", "已破1亿"),
        ("No.4  萨利巴", "8000万→1亿"),
        ("No.5  阿斯拉尼", "6000万→8000万"),
    ]
    
    y_start = 180
    spacing = 140
    
    for i, (player, value) in enumerate(ranks):
        y = y_start + i * spacing
        
        # 玩家名
        bbox = draw.textbbox((0, 0), player, font=rank_font)
        pw = bbox[2] - bbox[0]
        draw.text(((w - pw) // 2, y), player, fill="#1E293B", font=rank_font)
        
        # 身价（右侧对齐）
        bbox = draw.textbbox((0, 0), value, font=rank_font)
        vw = bbox[2] - bbox[0]
        draw.text((w - vw - 60, y), value, fill="#E8655A", font=rank_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)

def add_ending_text(img_path, output_path):
    """结尾卡：添加互动引导"""
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    q_font = get_font(56)
    cta_font = get_font(44)
    
    # 问题
    q = "谁是你的世界杯黑马？"
    bbox = draw.textbbox((0, 0), q, font=q_font)
    qw = bbox[2] - bbox[0]
    draw.text(((w - qw) // 2, 200), q, fill="#1E293B", font=q_font)
    
    # CTA
    cta = "评论区押宝👇"
    bbox = draw.textbbox((0, 0), cta, font=cta_font)
    cw = bbox[2] - bbox[0]
    draw.text(((w - cw) // 2, 400), cta, fill="#E8655A", font=cta_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 1. 封面
    add_cover_text(
        f"{BASE_DIR}/01-cover0_0.png",
        f"{OUTPUT_DIR}/01-cover.png"
    )
    print("✓ 封面完成")
    
    # 2. 亚马尔
    add_player_card_text(
        f"{BASE_DIR}/02-yamal0_0.png",
        f"{OUTPUT_DIR}/02-yamal.png",
        "亚马尔",
        "西班牙 · 17岁 · 巴萨",
        "盘带·视野·传球 顶级"
    )
    print("✓ 亚马尔卡完成")
    
    # 3. 穆西亚拉
    add_player_card_text(
        f"{BASE_DIR}/03-musiala0_0.png",
        f"{OUTPUT_DIR}/03-musiala.png",
        "穆西亚拉",
        "德国 · 21岁 · 拜仁",
        "左右脚都能踢 能突能传"
    )
    print("✓ 穆西亚拉卡完成")
    
    # 4. 罗克&萨利巴
    add_player_card_text(
        f"{BASE_DIR}/04-roak-saliba0_0.png",
        f"{OUTPUT_DIR}/04-roak-saliba.png",
        "罗克 & 萨利巴",
        "巴西18岁锋线 / 法国22岁中卫",
        "速度爆发力 vs 防线定海神针"
    )
    print("✓ 罗克&萨利巴卡完成")
    
    # 5. 身价榜单
    add_ranking_text(
        f"{BASE_DIR}/05-ranking0_0.png",
        f"{OUTPUT_DIR}/05-ranking.png"
    )
    print("✓ 身价榜单完成")
    
    # 6. 结尾
    add_ending_text(
        f"{BASE_DIR}/06-ending0_0.png",
        f"{OUTPUT_DIR}/06-ending.png"
    )
    print("✓ 结尾卡完成")
    
    print(f"\n全部完成！输出目录: {OUTPUT_DIR}")
