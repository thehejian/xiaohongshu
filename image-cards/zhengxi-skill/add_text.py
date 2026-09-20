#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/image-cards/zhengxi-skill"

def get_font(size):
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
    ]
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                continue
    return ImageFont.load_default()

def draw_centered(draw, text, y, font, color="#1E293B", max_width=None):
    img_w = 1024
    if max_width:
        lines = []
        for char in text:
            if not lines:
                lines.append("")
            test = lines[-1] + char
            bbox = draw.textbbox((0, 0), test, font=font)
            if bbox[2] - bbox[0] > max_width:
                lines.append(char)
            else:
                lines[-1] = test
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            draw.text(((img_w - (bbox[2] - bbox[0])) // 2, y), line, fill=color, font=font)
            y += font.size + 8
        return y
    else:
        bbox = draw.textbbox((0, 0), text, font=font)
        draw.text(((img_w - (bbox[2] - bbox[0])) // 2, y), text, fill=color, font=font)
        return y + font.size + 8

def add_cover_text(path, out_path):
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    title_font = get_font(72)
    sub_font = get_font(40)
    tag_font = get_font(32)
    draw_centered(draw, "让AI学会", 140, title_font, "#1E293B")
    draw_centered(draw, "景气度投资", 220, title_font, "#E8655A")
    y = draw_centered(draw, "把基金经理方法论做成Agent Skill", 340, sub_font, "#1E293B", 800)
    draw_centered(draw, "github.com/JadenLuo18/zhengxi-skill", y + 20, tag_font, "#94A3B8")
    draw_centered(draw, "开源 · 免费", y + 70, tag_font, "#94A3B8")
    img.convert("RGB").save(out_path, "JPEG", quality=95)

def add_painpoint_text(path, out_path):
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    title_font = get_font(56)
    body_font = get_font(36)
    draw_centered(draw, "刷到热点，从哪下手？", 120, title_font, "#1E293B")
    y = 240
    points = [
        "看到AI算力、半导体涨价，能感受到热度",
        "但很难判断哪层产业链在涨价",
        "哪个环节扩产最难？",
        "哪些公司ROE还有弹性？",
    ]
    for p in points:
        for i, line in enumerate([p]):
            bbox = draw.textbbox((0, 0), f"· {line}", font=body_font)
            draw.text((140, y), f"· {line}", fill="#475569", font=body_font)
            y += body_font.size + 20
    draw_centered(draw, "郑希框架帮AI完成第一轮深度研究", y + 30, get_font(38), "#E8655A", 800)
    img.convert("RGB").save(out_path, "JPEG", quality=95)

def add_process_text(path, out_path):
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    title_font = get_font(56)
    step_font = get_font(34)
    detail_font = get_font(28)
    draw_centered(draw, "四步研究流程", 100, title_font, "#1E293B")
    steps = [
        ("01 全球图谱定方向", "识别系统变化 → 产业链分层 → 找通胀层"),
        ("02 选ROE低的公司", "行业压制型 A类 + 前瞻研发型 B类"),
        ("03 六维跟踪验证", "竞争对手·上游·下游·价格·新进入者·预期"),
        ("04 逐步拟合", "未启动 → 试水 → 拟合 → 成型 → 顶部"),
    ]
    y = 210
    for step, detail in steps:
        bbox = draw.textbbox((0, 0), step, font=step_font)
        draw.text((130, y), step, fill="#E8655A", font=step_font)
        y += 44
        bbox = draw.textbbox((0, 0), detail, font=detail_font)
        draw.text((130, y), detail, fill="#1E293B", font=detail_font)
        y += 90
    img.convert("RGB").save(out_path, "JPEG", quality=95)

def add_roe_text(path, out_path):
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    title_font = get_font(56)
    label_font = get_font(40)
    body_font = get_font(30)
    draw_centered(draw, "核心选股：ROE弹性", 100, title_font, "#1E293B")
    y = 210
    draw_centered(draw, "A类  行业压制型", y, label_font, "#E8655A")
    y += 60
    lines_a = ["ROE低因为行业差", "景气来临时修复弹性极大", "如MLCC涨价时的风华高科"]
    for l in lines_a:
        draw_centered(draw, l, y, body_font, "#1E293B", 700)
        y += 44
    y += 40
    draw_centered(draw, "B类  前瞻研发型", y, label_font, "#0EA5E9")
    y += 60
    lines_b = ["研发投入方向与景气一致", "产品卖出时回报放大", "中小标的弹性更大"]
    for l in lines_b:
        draw_centered(draw, l, y, body_font, "#1E293B", 700)
        y += 44
    y += 40
    draw_centered(draw, "排除：ROE高因杠杆，或管理层差", y, get_font(30), "#94A3B8")
    img.convert("RGB").save(out_path, "JPEG", quality=95)

def add_prompt_text(path, out_path):
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    title_font = get_font(56)
    code_font = get_font(30)
    out_font = get_font(28)
    draw_centered(draw, "直接复制这段Prompt", 100, title_font, "#1E293B")
    y = 200
    prompt = "用郑希景气度投资框架扫描当前全球AI产业链。"
    draw_centered(draw, prompt, y, code_font, "#475569", 850)
    y += 50
    steps = [
        "① 通胀层识别",
        "② 产业链分层",
        "③ ROE弹性排序",
        "④ 六维跟踪评估",
        "⑤ 景气阶段判定",
        "⑥ 失败条件分析",
        "⑦ 下一步验证方向",
    ]
    for s in steps:
        draw_centered(draw, s, y, out_font, "#E8655A")
        y += 40
    draw_centered(draw, "GitHub搜 zhengxi-skill 开源免费", y + 10, get_font(32), "#94A3B8")
    img.convert("RGB").save(out_path, "JPEG", quality=95)

def add_ending_text(path, out_path):
    img = Image.open(path).convert("RGBA")
    draw = ImageDraw.Draw(img)
    q_font = get_font(48)
    body_font = get_font(34)
    cta_font = get_font(40)
    draw_centered(draw, "不是荐股", 140, q_font, "#E8655A")
    draw_centered(draw, "是研究工具", 200, q_font, "#1E293B")
    y = 320
    points = [
        "研究辅助，非投资建议",
        "所有判断回到公告和财报",
        "交易决策始终由你控制",
    ]
    for p in points:
        draw_centered(draw, p, y, body_font, "#475569")
        y += 60
    draw_centered(draw, "评论区说说你用的什么AI投研工具", y + 40, cta_font, "#E8655A", 800)
    img.convert("RGB").save(out_path, "JPEG", quality=95)

if __name__ == "__main__":
    os.makedirs(BASE_DIR, exist_ok=True)
    add_cover_text(f"{BASE_DIR}/01-cover-zhengxi-skill.png", f"{BASE_DIR}/01-cover-zhengxi-skill.png")
    print("✓ 封面完成")
    add_painpoint_text(f"{BASE_DIR}/02-painpoint-zhengxi-skill.png", f"{BASE_DIR}/02-painpoint-zhengxi-skill.png")
    print("✓ 痛点卡完成")
    add_process_text(f"{BASE_DIR}/03-process-zhengxi-skill.png", f"{BASE_DIR}/03-process-zhengxi-skill.png")
    print("✓ 流程卡完成")
    add_roe_text(f"{BASE_DIR}/04-roe-zhengxi-skill.png", f"{BASE_DIR}/04-roe-zhengxi-skill.png")
    print("✓ ROE卡完成")
    add_prompt_text(f"{BASE_DIR}/05-prompt-zhengxi-skill.png", f"{BASE_DIR}/05-prompt-zhengxi-skill.png")
    print("✓ Prompt卡完成")
    add_ending_text(f"{BASE_DIR}/06-ending-zhengxi-skill.png", f"{BASE_DIR}/06-ending-zhengxi-skill.png")
    print("✓ 结尾卡完成")
    print(f"\n全部完成！目录: {BASE_DIR}")
