#!/usr/bin/env python3
"""
C罗世界杯小红书图片 - 文字叠加脚本
使用Pillow将中文文字叠加到AI生成的无文字图片上
"""

import os
from PIL import Image, ImageDraw, ImageFont

# 配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "image-cards")

# 中文字体路径（macOS）
CHINESE_FONT_PATHS = [
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
]

# 英文字体路径（macOS）
ENGLISH_FONT_PATH = "/System/Library/Fonts/SFNSMono.ttf"

def get_chinese_font(size):
    """获取中文字体"""
    for font_path in CHINESE_FONT_PATHS:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                continue
    # fallback
    return ImageFont.load_default()

def get_english_font(size):
    """获取英文字体"""
    if os.path.exists(ENGLISH_FONT_PATH):
        try:
            return ImageFont.truetype(ENGLISH_FONT_PATH, size)
        except Exception:
            pass
    return ImageFont.load_default()

def add_cover_overlay(img_path, output_path):
    """
    封面图：大字标题 + 副标题
    """
    img = Image.open(img_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    w, h = img.size
    
    # 从底部向上的半透明渐变遮罩
    for y in range(h):
        alpha = int(180 * (1 - y / h))
        draw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))
    
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)
    
    # 标题文字
    title = "C罗还没退役！"
    subtitle = "30岁老将的压力来了"
    
    title_font = get_chinese_font(72)
    subtitle_font = get_chinese_font(42)
    
    # 计算文字位置（居中偏下）
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    title_h = title_bbox[3] - title_bbox[1]
    
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_w = subtitle_bbox[2] - subtitle_bbox[0]
    
    title_x = (w - title_w) // 2
    title_y = h - 320
    
    subtitle_x = (w - subtitle_w) // 2
    subtitle_y = title_y + title_h + 20
    
    # 绘制白色文字带阴影
    shadow_offset = 3
    draw.text((title_x + shadow_offset, title_y + shadow_offset), title, 
              fill=(0, 0, 0, 180), font=title_font)
    draw.text((title_x, title_y), title, fill=(255, 255, 255, 255), font=title_font)
    
    draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle,
              fill=(0, 0, 0, 150), font=subtitle_font)
    draw.text((subtitle_x, subtitle_y), subtitle, fill=(255, 200, 50, 255), font=subtitle_font)
    
    # 底部标签
    tag = "2026世界杯 · 葡萄牙即将开打"
    tag_font = get_chinese_font(28)
    tag_bbox = draw.textbbox((0, 0), tag, font=tag_font)
    tag_w = tag_bbox[2] - tag_bbox[0]
    tag_x = (w - tag_w) // 2
    tag_y = h - 80
    
    draw.text((tag_x, tag_y), tag, fill=(255, 255, 255, 200), font=tag_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)
    print(f"✓ 封面图已保存: {output_path}")


def add_messi_mbappe_overlay(img_path, output_path):
    """
    图2：梅西vs姆巴佩对比图
    """
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    
    # 顶部标题
    title = "前辈们已经交卷"
    title_font = get_chinese_font(48)
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    title_x = (w - title_w) // 2
    
    draw.text((title_x + 2, 30 + 2), title, fill=(0, 0, 0, 180), font=title_font)
    draw.text((title_x, 30), title, fill=(255, 255, 255, 255), font=title_font)
    
    # 左侧 - 梅西
    left_label = "梅西"
    left_sub = "帽子戏法"
    left_font = get_chinese_font(52)
    left_sub_font = get_chinese_font(36)
    
    left_bbox = draw.textbbox((0, 0), left_label, font=left_font)
    left_w = left_bbox[2] - left_bbox[0]
    left_x = w // 4 - left_w // 2
    left_y = h // 2 - 40
    
    draw.text((left_x + 2, left_y + 2), left_label, fill=(0, 0, 0, 180), font=left_font)
    draw.text((left_x, left_y), left_label, fill=(100, 180, 255, 255), font=left_font)
    
    left_sub_bbox = draw.textbbox((0, 0), left_sub, font=left_sub_font)
    left_sub_w = left_sub_bbox[2] - left_sub_bbox[0]
    left_sub_x = w // 4 - left_sub_w // 2
    draw.text((left_sub_x, left_y + 70), left_sub, fill=(255, 255, 255, 230), font=left_sub_font)
    
    # 右侧 - 姆巴佩
    right_label = "姆巴佩"
    right_sub = "梅开二度"
    right_font = get_chinese_font(52)
    right_sub_font = get_chinese_font(36)
    
    right_bbox = draw.textbbox((0, 0), right_label, font=right_font)
    right_w = right_bbox[2] - right_bbox[0]
    right_x = 3 * w // 4 - right_w // 2
    right_y = h // 2 - 40
    
    draw.text((right_x + 2, right_y + 2), right_label, fill=(0, 0, 0, 180), font=right_font)
    draw.text((right_x, right_y), right_label, fill=(80, 120, 255, 255), font=right_font)
    
    right_sub_bbox = draw.textbbox((0, 0), right_sub, font=right_sub_font)
    right_sub_w = right_sub_bbox[2] - right_sub_bbox[0]
    right_sub_x = 3 * w // 4 - right_sub_w // 2
    draw.text((right_sub_x, right_y + 70), right_sub, fill=(255, 255, 255, 230), font=right_sub_font)
    
    # 底部文字
    bottom = "6月17日 · 小组赛完美答卷"
    bottom_font = get_chinese_font(28)
    bottom_bbox = draw.textbbox((0, 0), bottom, font=bottom_font)
    bottom_w = bottom_bbox[2] - bottom_bbox[0]
    bottom_x = (w - bottom_w) // 2
    bottom_y = h - 80
    
    draw.text((bottom_x, bottom_y), bottom, fill=(255, 255, 255, 200), font=bottom_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)
    print(f"✓ 对比图已保存: {output_path}")


def add_cr7_portrait_overlay(img_path, output_path):
    """
    图3：C罗特写 + 精神力量
    """
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    
    # 左上角标题
    title = "压力，全给了C罗"
    font = get_chinese_font(56)
    bbox = draw.textbbox((0, 0), title, font=font)
    tw = bbox[2] - bbox[0]
    tx = 40
    ty = 40
    
    draw.text((tx + 2, ty + 2), title, fill=(0, 0, 0, 180), font=font)
    draw.text((tx, ty), title, fill=(255, 80, 50, 255), font=font)
    
    # 底部文字
    bottom_lines = [
        "30岁 · 最后一届世界杯",
        "他不需要证明，但他偏要证明"
    ]
    bottom_font = get_chinese_font(32)
    
    y_pos = h - 180
    for line in bottom_lines:
        bbox = draw.textbbox((0, 0), line, font=bottom_font)
        lw = bbox[2] - bbox[0]
        x_pos = (w - lw) // 2
        draw.text((x_pos + 2, y_pos + 2), line, fill=(0, 0, 0, 160), font=bottom_font)
        draw.text((x_pos, y_pos), line, fill=(255, 255, 255, 240), font=bottom_font)
        y_pos += 45
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)
    print(f"✓ C罗特写图已保存: {output_path}")


def add_determination_overlay(img_path, output_path):
    """
    图4：偏执精神 - 金句型
    """
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    
    # 半透明遮罩
    for y in range(h):
        alpha = int(120 * (1 - y / h))
        draw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))
    
    # 居中金句
    quote = "C罗不是靠速度吃饭的人"
    sub_quote = "他是靠\u201c\u6211\u8981\u8d62\u201d\u7684\u504f\u6267"
    
    quote_font = get_chinese_font(52)
    sub_font = get_chinese_font(38)
    
    quote_bbox = draw.textbbox((0, 0), quote, font=quote_font)
    qw = quote_bbox[2] - quote_bbox[0]
    qh = quote_bbox[3] - quote_bbox[1]
    
    qx = (w - qw) // 2
    qy = h // 2 - 60
    
    draw.text((qx + 3, qy + 3), quote, fill=(0, 0, 0, 200), font=quote_font)
    draw.text((qx, qy), quote, fill=(255, 255, 255, 255), font=quote_font)
    
    sub_bbox = draw.textbbox((0, 0), sub_quote, font=sub_font)
    sw = sub_bbox[2] - sub_bbox[0]
    sx = (w - sw) // 2
    sy = qy + qh + 40
    
    draw.text((sx + 2, sy + 2), sub_quote, fill=(0, 0, 0, 160), font=sub_font)
    draw.text((sx, sy), sub_quote, fill=(255, 200, 50, 255), font=sub_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)
    print(f"✓ 偏执精神图已保存: {output_path}")


def add_final_overlay(img_path, output_path):
    """
    图5：结尾图 - CTA
    """
    img = Image.open(img_path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    
    w, h = img.size
    
    # 顶部标题
    title = "明天凌晨，葡萄牙开打"
    font = get_chinese_font(52)
    bbox = draw.textbbox((0, 0), title, font=font)
    tw = bbox[2] - bbox[0]
    tx = (w - tw) // 2
    ty = h // 2 - 100
    
    draw.text((tx + 3, ty + 3), title, fill=(0, 0, 0, 200), font=font)
    draw.text((tx, ty), title, fill=(255, 255, 255, 255), font=font)
    
    # 底部小字
    bottom = "如果C罗也在小组赛爆发呢？"
    bottom_font = get_chinese_font(36)
    bbox = draw.textbbox((0, 0), bottom, font=bottom_font)
    bw = bbox[2] - bbox[0]
    bx = (w - bw) // 2
    by = h // 2 + 40
    
    draw.text((bx + 2, by + 2), bottom, fill=(0, 0, 0, 160), font=bottom_font)
    draw.text((bx, by), bottom, fill=(255, 200, 50, 255), font=bottom_font)
    
    # 底部CTA
    cta = "评论区押宝👇 他能像梅西一样爆发吗？"
    cta_font = get_chinese_font(26)
    bbox = draw.textbbox((0, 0), cta, font=cta_font)
    cw = bbox[2] - bbox[0]
    cx = (w - cw) // 2
    cy = h - 100
    
    draw.text((cx, cy), cta, fill=(255, 255, 255, 180), font=cta_font)
    
    img.convert("RGB").save(output_path, "JPEG", quality=95)
    print(f"✓ 结尾图已保存: {output_path}")


if __name__ == "__main__":
    print("开始为C罗世界杯图片叠加文字...\n")
    
    # 处理所有图片
    add_cover_overlay(
        os.path.join(IMAGE_DIR, "01-cover0_0.png"),
        os.path.join(IMAGE_DIR, "01-cover.jpg")
    )
    
    add_messi_mbappe_overlay(
        os.path.join(IMAGE_DIR, "02-messi-mbappe0_0.png"),
        os.path.join(IMAGE_DIR, "02-messi-mbappe.jpg")
    )
    
    add_cr7_portrait_overlay(
        os.path.join(IMAGE_DIR, "03-cr7-portrait0_0.png"),
        os.path.join(IMAGE_DIR, "03-cr7-portrait.jpg")
    )
    
    add_determination_overlay(
        os.path.join(IMAGE_DIR, "04-determination0_0.png"),
        os.path.join(IMAGE_DIR, "04-determination.jpg")
    )
    
    add_final_overlay(
        os.path.join(IMAGE_DIR, "05-final-match0_0.png"),
        os.path.join(IMAGE_DIR, "05-final-match.jpg")
    )
    
    print("\n✓ 所有图片文字叠加完成！")
