#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

BASE = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/xiaomi-nas-xhs"

def font(s):
    paths = ["/System/Library/Fonts/PingFang.ttc", "/System/Library/Fonts/STHeiti Medium.ttc"]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, s)
    return ImageFont.load_default()

def center(draw, text, y, f, c="#FFFFFF", max_w=800):
    img_w = 1024
    lines = []
    for char in text:
        if not lines: lines.append("")
        test = lines[-1] + char
        if draw.textbbox((0, 0), test, font=f)[2] > max_w and lines[-1]:
            lines.append(char)
        else:
            lines[-1] = test
    for line in lines:
        bw = draw.textbbox((0, 0), line, font=f)
        draw.text(((img_w - (bw[2] - bw[0])) // 2, y), line, fill=c, font=f)
        y += f.size + 6
    return y

def overlay_all():
    # 01-cover
    img = Image.open(f"{BASE}/01-cover-ai.png").convert("RGBA")
    d = ImageDraw.Draw(img)
    f72, f40, f28, f22, f20 = font(72), font(40), font(28), font(22), font(20)
    center(d, "Xiaomi 智能存储", 280, f72, "#FFFFFF")
    center(d, "小米首款NAS", 370, f40, "#F59E0B")
    center(d, "2026.06.24 正式发布 开启预约", 500, f28, "#94A3B8")
    center(d, "家庭私有云 · 开箱即用", 550, f22, "#64748B")
    center(d, "4TB 套装 2299元起", 640, f28, "#F59E0B")
    img.convert("RGB").save(f"{BASE}/01-cover-ai.png", "JPEG", quality=95)
    print("✓ 01-cover")

    # 02-features
    img = Image.open(f"{BASE}/02-features-ai.png").convert("RGBA")
    d = ImageDraw.Draw(img)
    center(d, "开箱即用的家庭存储中心", 200, f40, "#FFFFFF")
    for i, (t, s) in enumerate([
        ("预装硬盘套装", "开箱通电即用，无需选硬盘型号"),
        ("米家App一键操控", "手机完成管理，不需电脑配置"),
        ("去极客化设计", "为家庭用户打造，不折腾Docker"),
    ]):
        y = 380 + i * 130
        d.text((140, y), t, fill="#F59E0B", font=f28)
        d.text((140, y + 45), s, fill="#94A3B8", font=f22)
    img.convert("RGB").save(f"{BASE}/02-features-ai.png", "JPEG", quality=95)
    print("✓ 02-features")

    # 03-features list
    img = Image.open(f"{BASE}/03-features-ai.png").convert("RGBA")
    d = ImageDraw.Draw(img)
    center(d, "四大核心功能", 180, f40, "#FFFFFF")
    items = [
        ("01", "手机相册自动备份", "原图无损，AI智能分类生成家庭相册", "#F59E0B"),
        ("02", "米家生态深度联动", "摄像头录像自动保存，免云存储会员", "#60A5FA"),
        ("03", "家庭影音娱乐中心", "4K原画电视直接放，无广告不限速", "#34D399"),
        ("04", "隐私与安全保障", "数据存家里硬盘，物理隔绝公有云", "#A78BFA"),
    ]
    for i, (num, title, desc, color) in enumerate(items):
        y = 300 + i * 110
        d.text((120, y), num, fill=color, font=font(20))
        d.text((180, y), title, fill="#FFFFFF", font=f28)
        d.text((180, y + 50), desc, fill="#94A3B8", font=f20)
    img.convert("RGB").save(f"{BASE}/03-features-ai.png", "JPEG", quality=95)
    print("✓ 03-features")

    # 04-pricing
    img = Image.open(f"{BASE}/04-pricing-ai.png").convert("RGBA")
    d = ImageDraw.Draw(img)
    center(d, "版本与价格", 180, f40, "#FFFFFF")
    tiers = [
        ("4TB 入门版", "手机备份 · 监控存储 · 家庭影音", "2299", "原价3499", "#F59E0B"),
        ("8TB 进阶版", "摄影爱好者 · 视频创作者 · 多成员", "2899", "原价4499", "#60A5FA"),
        ("16TB 专业版", "数据安全高要求 · 工作文件备份", "4699", "原价6999", "#34D399"),
    ]
    for i, (name, desc, price, orig, color) in enumerate(tiers):
        y = 310 + i * 130
        d.text((120, y), name, fill=color, font=f28)
        d.text((120, y + 45), desc, fill="#94A3B8", font=f20)
        d.text((860, y + 5), price, fill=color, font=font(36), anchor="rt")
        d.text((710, y + 48), f"众筹价", fill="#64748B", font=font(18))
        d.text((860, y + 48), orig, fill="#64748B", font=font(18), anchor="rt")
    img.convert("RGB").save(f"{BASE}/04-pricing-ai.png", "JPEG", quality=95)
    print("✓ 04-pricing")

    # 05-advice
    img = Image.open(f"{BASE}/05-advice-ai.png").convert("RGBA")
    d = ImageDraw.Draw(img)
    center(d, "购买建议", 180, f40, "#FFFFFF")
    tips = [
        ("推荐：小米全家桶用户", "手机+摄像头+电视联动体验极佳", "#F59E0B"),
        ("推荐：普通家庭用户", "手机空间不够 · 云盘太贵 · 监控没地存", "#60A5FA"),
        ("慎重：数码极客 / Docker玩家", "系统封闭，建议选绿联、群晖", "#64748B"),
    ]
    for i, (title, desc, color) in enumerate(tips):
        y = 310 + i * 140
        d.text((120, y), title, fill=color, font=f28)
        d.text((120, y + 50), desc, fill="#94A3B8", font=f22)
    img.convert("RGB").save(f"{BASE}/05-advice-ai.png", "JPEG", quality=95)
    print("✓ 05-advice")

    # 06-ending
    img = Image.open(f"{BASE}/06-ending-ai.png").convert("RGBA")
    d = ImageDraw.Draw(img)
    center(d, "Xiaomi 智能存储", 280, f40, "#F59E0B")
    center(d, "家庭私有云新选择", 340, f28, "#FFFFFF")
    for i, t in enumerate([
        "4TB 2299元起，预装硬盘开箱即用",
        "米家App操控，全家老少都能用",
        "已开启预约，各大电商平台可下单",
    ]):
        y = 450 + i * 60
        d.text((160, y), "—", fill="#F59E0B", font=f22)
        d.text((200, y), t, fill="#CBD5E1", font=f22)
    center(d, "你会入手吗？评论区聊聊", 680, f22, "#F59E0B")
    img.convert("RGB").save(f"{BASE}/06-ending-ai.png", "JPEG", quality=95)
    print("✓ 06-ending")

overlay_all()
print("\n全部完成")