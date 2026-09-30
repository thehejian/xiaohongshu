# -*- coding: utf-8 -*-
"""全部图节点 + 路由函数。

安全约定：
- 演练（dry_run=True，默认）：读类节点真实执行，花钱/外部节点走占位分支
- 真实（--real）：LLM/生图/飞书/publish 全部实现；发布仍只经 approve 闸门
"""
from __future__ import annotations

import json
import os
import re
import shutil
import struct
import subprocess
import time
from pathlib import Path

from langgraph.types import interrupt

from . import llm, repo
from .profiles import PROFILES, SeriesProfile
from .prompts.style import STYLE_HISTORY, with_feedback

INKWASH_PREFIX = (
    "Ink wash painting style, light rice paper texture, flowing ink strokes, "
    "subtle crimson and grey colors, sparse composition with negative space, "
    "misty atmosphere."
)
INKWASH_CLOSING = (
    "Ancient Chinese people, period clothing. No heavy outlines. Ample whitespace. "
    "Unified series style, consistent brushwork and tone. "
    # 风格锚点（2026-09-30 加，499/509 教训：带参考图仍会漂成"线描平涂"，
    # 画风锁定必须靠 prompt 文字；正反两面都写）
    "Traditional Chinese ink-and-wash figure painting, wet brush washes with soft bleeding edges, "
    "visible watercolor gradients and paper grain, muted desaturated earth tones, hand-painted loose brushwork. "
    "No clean digital outlines, no flat cel shading, no cartoon style, no glossy digital rendering."
)
FLAT_TECH_PREFIX = (
    "Flat vector illustration, clean modern tech aesthetic, soft gradients, "
    "generous whitespace, cohesive cool color palette."
)
BANNED_PROMPT_WORDS = [
    "corpse", "blood", "collapse", "torture", "starving", "cannibalism", "abyss",
    "suffocating", "harem", "reclining", "dark plot", "scheming",
    "delicate pale colors", "strictly limited", "calligraphy", "chinese title",
]


def _tool_env() -> dict:
    env = dict(os.environ)
    env["PATH"] = "/opt/homebrew/bin:/Users/mac/.npm-global/bin:" + env.get("PATH", "")
    return env


def _p(state: dict) -> SeriesProfile:
    return PROFILES[state["series"]]


def _n(state: dict, key: str, cap: int = 3) -> int:
    att = dict(state.get("attempts") or {})
    att[key] = att.get(key, 0) + 1
    state["attempts"] = att
    return att[key]


def _strip_fences(text: str) -> str:
    """剥掉 ``` 围栏（全文任何位置）、JSON 外壳、markdown 头标记，并规范化空行。"""
    t = text.strip()
    if not t:
        return ""
    # 剥 fence：正文中任意位置的整段代码块都删掉（LLM 偶发在文末塞元信息代码块，475 教训）
    t = re.sub(r"```[a-zA-Z]*\s*[\s\S]*?```", "", t)
    t = t.strip()
    # 剥文末元信息段：孤立 --- 分隔线 + 字数统计/说明文字
    body_lines = t.splitlines()
    while body_lines:
        s = body_lines[-1].strip()
        if not s or s == "---" or s.startswith("**字数统计") or s.startswith("字数统计"):
            body_lines.pop()
        else:
            break
    t = "\n".join(body_lines).strip()
    # 剥 JSON 外壳（LLM 偶尔把整个响应包在 {…} 里）
    if t.startswith("{") and t.endswith("}"):
        try:
            j = json.loads(t)
            t = j.get("content") or j.get("text") or json.dumps(j, ensure_ascii=False)
        except Exception:  # noqa: BLE001
            pass
    # 剥 markdown 标题 # 前缀（仅第1行）
    lines = t.splitlines()
    if lines and re.match(r"^#+\s+", lines[0]):
        lines[0] = re.sub(r"^#+\s+", "", lines[0])
    # 强制规范：第1行标题，第2行必须空，其余正文
    out = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i == 0 and stripped:
            out.append(stripped)  # 标题行压缩空白
        elif i == 1 and stripped:
            out.append("")  # 第2行强制空行
            out.append(stripped)  # 原内容放到第3行起
        elif stripped or out:  # 跳过纯空行，但保留有意义的空段落
            out.append(line)
    return "\n".join(out).rstrip()


# ── 1. 选题 ──────────────────────────────────────────────
def resolve_topic(state: dict) -> dict:
    p = _p(state)
    topic_no = state.get("topic_no") or (repo.next_topic_no() if p.name == "history" else 0)
    slug = state.get("slug") or (p.dir_template.format(n=topic_no, slug="") if p.name == "history" else "")
    if not slug:
        raise SystemExit(f"series={p.name} 需要 --slug <英文目录名>")

    wd = repo.workdir_for(p.name, topic_no, slug, state["dry_run"], p.dir_template)
    wd.mkdir(parents=True, exist_ok=True)

    out: dict = {"topic_no": topic_no, "slug": slug, "workdir": str(wd)}
    if p.name == "history":
        mat = repo.extract_material(topic_no)
        out["material"] = mat["block"]
        out["title"] = repo.clamp_title(mat["raw_title"], 20)
    return out


# ── 2. 查重（三步法：确定性 grep + 真实模式 LLM 判重）────
def dedup(state: dict) -> dict:
    mat = state.get("material", "")
    raw_title = ""
    m = re.search(r"^## 主题 \d+[:：]?\s*(.+)$", mat, re.M)
    if m:
        raw_title = m.group(1).strip()

    art = Path(state["workdir"]) / "article.md"
    if art.exists():
        return {"dedup_verdict": "skip", "dedup_notes": "article.md 已存在（该主题已成文）"}

    kws = repo.title_keywords(raw_title)
    hits = repo.dedup_hits(kws)
    titles = repo.scan_article_titles()
    same = [t for t in titles if raw_title and t[1] == raw_title]
    notes = []
    if same:
        return {"dedup_verdict": "skip", "dedup_notes": f"标题完全相同: {same}"}
    if repo.DRAFTS_CACHE.exists():
        notes.append(f"草稿缓存 {repo.DRAFTS_CACHE} 存在（P1 接入逐条比对）")

    if hits and not state["dry_run"]:
        # LLM 判重（4.2 判定标准）
        excerpts = []
        for slug in hits[:4]:
            f = repo.CARDS / slug / "article.md"
            if f.exists():
                head = f.read_text(encoding="utf-8", errors="ignore")[:500]
                excerpts.append(f"【已有成文 {slug}】\n{head}")
        sys = (
            "判定「新选题」是否与「已有成文」重复。标准：主体人物/事件/战役相同 → skip；"
            "仅次要提及重叠但主体角度不同（人物深挖 vs 主题综述、单事件 vs 通史）→ continue。"
            '只输出 JSON：{"verdict":"skip|continue","reason":"一句话"}'
        )
        user = f"新选题标题：{raw_title}\n新选题素材（截断）：{mat[:600]}\n\n" + "\n\n".join(excerpts)
        try:
            j = llm.extract_json(llm.chat([{"role": "system", "content": sys},
                                           {"role": "user", "content": user}], model=llm.CHECK_MODEL))
            verdict = j.get("verdict", "continue")
            notes.append(f"LLM判重: {j.get('reason','')}")
            if verdict == "skip":
                return {"dedup_verdict": "skip", "dedup_notes": "; ".join(notes)}
        except Exception as e:  # noqa: BLE001 — 判重失败不拦路，留痕继续
            notes.append(f"LLM判重失败(继续): {e}")
    elif hits:
        notes.append(f"关键词命中(演练不判重): {hits}")

    return {"dedup_verdict": "continue", "dedup_notes": "; ".join(notes) or "无命中"}


# ── 3. 写正文 ────────────────────────────────────────────
def write_article(state: dict) -> dict:
    p = _p(state)
    _n(state, "write")  # 记录一次重试机会（由图路由控制总次数）
    if p.name != "history":
        raise NotImplementedError("P1.5：科技/游记正文提示词（清单体 / 攻略体）")

    if not state["dry_run"]:
        sys_msg = STYLE_HISTORY
        fb: list[str] = list((state.get("verify") or {}).get("problems") or [])
        fc = state.get("fact_check") or {}
        if fc and not fc.get("passed") and fc.get("issues"):
            # 史实问题必须喂给重写（486 教训：只喂 verify problems 时 fact 打回的稿
            # 重写拿不到原因，盲改必然二次失败）
            fb += [f"史实问题（必须修正）：{i}" for i in fc["issues"]]
            # 数字类问题的修法提示（514 教训：自造「三十万」连改两轮都过不了，
            # 改用素材原文说法或删掉该数字才过）
            fb.append("涉及具体数字/日期时：只用素材原文的原始说法（素材写「数十万」就写「数十万」），"
                      "或直接把该数字从标题和正文删除，严禁自造精确数字")
        if state.get("attempts", {}).get("write", 0) > 1 and fb:
            sys_msg = with_feedback(STYLE_HISTORY, fb)
        user = (
            f"素材原文：\n{state['material']}\n\n"
            f"硬性要求（违反任一条即为废稿）：\n"
            f"1. 全文去空格换行后 {p.words_min}-{p.words_max} 字（含标题与 tags，严禁低于下限；字数不足必须扩写具体场景，严禁缩写）\n"
            "2. 全中文正文零英文单词（人名地名一律音译；年份用「公元219年」写法）\n"
            "3. 第1行标题从正文核心内容提炼，≤18字，要有吸引力——写**具体动作/人物对比/反差事实**（如「斩马谡贬自己：诸葛亮的赏罚组合拳」）；"
            "**禁止「我没想到」「竟然」开头的空悬惊叹句式**；第2行为空行；第3行起正文；末尾 3-5 个 #话题 tags\n"
            "4. 禁止任何代码围栏（```）、禁止 JSON、禁止解释性文字，只输出 article.md 文件内容本身。\n"
            "若上一稿未过验证，本次必须逐条修正后再输出。"
        )
        # 内部循环：LLM 偶发空响应或字数不足时自动重试（不计入 attempts）
        content = ""
        for _attempt in range(6):
            raw = llm.chat(
                [{"role": "system", "content": sys_msg}, {"role": "user", "content": user}],
                model=llm.WRITE_MODEL, temperature=0.5)
            content = _strip_fences(raw)
            if not content:
                # 空输出/全是元信息被剥空：必须带反馈重试（499 教训——静默 continue
                # 等于 6 轮盲试，最后写入空文件白耗一次图 attempts）
                sys_msg = (f"{sys_msg}\n\n⚠️ 上次输出为空或只有元信息（被清理后无正文）。"
                           "必须直接输出 article.md 内容本身：第1行标题、第2行空行、第3行起正文、末尾 #话题 tags。")
                continue
            # 字数不足时追加反馈继续要
            chars = len(re.sub(r"\s", "", content))
            if chars >= p.words_min:
                break
            sys_msg = f"{sys_msg}\n\n⚠️ 上次输出仅 {chars} 字，低于下限 {p.words_min} 字。必须扩写至 {p.words_min} 字以上，多写具体场景与细节，严禁概述式缩写。"
        if len(re.sub(r"\s", "", content)) < p.words_min:
            # 所有轮都未达标，仍写入（让 verify 环节报错由图路由处理）
            pass
    else:
        # 演练：素材正文拼合规占位稿，验证 verify 判定逻辑
        mat = re.search(r"^### 正文\s*\n+(.*?)(?=^### |\Z)", state["material"], re.M | re.S)
        body = mat.group(1).strip() if mat else ""
        paras = [x for x in re.split(r"\n\s*\n", body) if x.strip()]
        acc, chosen = 0, []
        for para in paras:
            chosen.append(para)
            acc = len(re.sub(r"\s", "", para))
            if acc >= p.words_min:
                break
        text = "\n\n".join(chosen)
        cnt = len(re.sub(r"\s", "", text))
        if cnt > p.words_max:
            for sent in reversed(re.split(r"(?<=[。！？])", text)):
                if len(re.sub(r"\s", "", text)) - len(sent) >= p.words_min:
                    text = text[: text.rfind(sent)]
                else:
                    break
        elif cnt < p.words_min:
            text += "\n\n（演练占位：真实模式由 LLM 扩写至 700 字以上，此处仅用于跑通校验。）" * (
                (p.words_min - cnt) // 40 + 1
            )
        content = f"{state['title']}\n\n{text}\n"

    path = Path(state["workdir"]) / "article.md"
    path.write_text(content, encoding="utf-8")
    # 从生成的文章第1行提取实际标题（可能不同于素材标题）
    actual_title = content.splitlines()[0].strip() if content.splitlines() else state["title"]
    return {"article_path": str(path), "attempts": state["attempts"], "title": actual_title}


# ── 4. 写后验证（三条，纯代码）────────────────────────────
def verify_article(state: dict) -> dict:
    p = _p(state)
    path = Path(state["article_path"])
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    problems = []
    title = lines[0].strip() if lines else ""
    if not title:
        problems.append("第1行缺标题")
    elif len(title) > 18:
        problems.append(f"标题 {len(title)} 字 > 18")
    if title and "我没想到" in title:
        # 509/513 用户连续打回此句式：空悬惊叹、看不出讲什么
        problems.append("标题禁用「我没想到」句式——改从正文提炼具体动作/人物对比/反差事实")
    if len(lines) < 2 or lines[1].strip():
        problems.append("第2行必须是空行")

    chars = len(re.sub(r"\s", "", text))
    if not (p.words_min <= chars <= p.words_max):
        problems.append(f"字数 {chars} 不在 {p.words_min}-{p.words_max}")

    en = re.search(r"[A-Za-z]{2,}", text)
    if en:
        problems.append(f"含英文单词「{en.group(0)}」")

    if "```" in text:
        problems.append("正文含代码围栏 ```（LLM 元信息残留）")
    if re.search(r"(?m)^.{0,3}字数统计", text):
        problems.append("正文含「字数统计」元信息行")

    res = {"passed": not problems, "title_len": len(title), "chars": chars, "problems": problems}
    return {"verify": res}


def route_verify(state: dict) -> str:
    if state["verify"]["passed"]:
        return "fact_check"
    if state.get("attempts", {}).get("write", 0) >= 3:
        return "report_error"
    return "write_article"


# ── 5. 史实核查 ──────────────────────────────────────────
def fact_check(state: dict) -> dict:
    _n(state, "fact")
    if state["dry_run"]:
        return {"fact_check": {"passed": True, "notes": "演练跳过"},
                "attempts": state["attempts"]}
    sys = (
        "你是史实核查员。只报以下三类硬错误（其余一律放过）：\n"
        "①与素材明确矛盾的人物关系/时间线/地点/事件（如素材说A死在200年，正文说死在210年）；\n"
        "②素材未提供且无把握的具体数字/日期/直接引语；\n"
        "③把演义当正史且未标注。\n"
        "✅ 以下情况一律不报错：合理缩写/概括、用词简化（如「曹洪拒绝借钱」→「曹洪拒绝曹丕」）、"
        "常识性补充、情感渲染、视角转换。文风字数问题不用管。\n"
        '只输出 JSON：{"passed":true|false,"issues":["..."]}'
    )
    user = f"素材原文：\n{state['material'][:3000]}\n\n待发布正文：\n{Path(state['article_path']).read_text(encoding='utf-8')}"
    raw = llm.chat([{"role": "system", "content": sys},
                    {"role": "user", "content": user}], model=llm.CHECK_MODEL)
    try:
        j = llm.extract_json(raw)
    except Exception as e:  # noqa: BLE001 — LLM 偶发非 JSON，降级为 pass + 记录
        return {"fact_check": {"passed": True, "issues": [], "notes": f"LLM 解析失败(降级通过): {e}"},
                "attempts": state["attempts"]}
    issues = [str(x) for x in (j.get("issues") or [])]
    return {"fact_check": {"passed": bool(j.get("passed")), "issues": issues},
            "attempts": state["attempts"]}


# ── 6. 生图提示词 ────────────────────────────────────────
def _prompts_validation(profile: SeriesProfile, prompts: list[str]) -> list[str]:
    problems = []
    if len(prompts) != 3:
        return [f"应为 3 条，实际 {len(prompts)} 条"]
    for i, t in enumerate(prompts, 1):
        low = t.lower()
        if profile.image_style == "inkwash":
            # 前缀允许前后有空白/换行，只要内容包含即可
            if INKWASH_PREFIX not in t:
                problems.append(f"第{i}条缺统一风格前缀")
            if INKWASH_CLOSING not in t:
                problems.append(f"第{i}条缺收尾约束")
        for w in BANNED_PROMPT_WORDS:
            if w in low:
                problems.append(f"第{i}条含禁词「{w}」")
    if profile.image_style == "inkwash":
        lights = [t for t in prompts if "soft diffused daylight" in t or "soft light from paper window" in t]
        if len(lights) < 3:
            problems.append("光线未统一（三条都要 soft diffused daylight / soft light from paper window）")
    return problems


def write_prompts(state: dict) -> dict:
    p = _p(state)
    if p.name != "history":
        raise NotImplementedError("P1.5：科技/游记提示词（扁平科技大字 / 无需生图）")

    if state["dry_run"]:
        prefix = INKWASH_PREFIX
        out = []
        for i in range(1, p.image_count + 1):
            f = Path(state["workdir"]) / "prompts" / f"0{i}-cover.md"
            f.parent.mkdir(exist_ok=True)
            f.write_text(prefix + f" [演练占位场景 {i}] {state['title']}\n", encoding="utf-8")
            out.append(str(f))
        return {"prompts": out}

    sys = (
        "你是水墨历史系列的美术指导。输出严格 JSON：{\"prompts\":[\"...\",\"...\",\"...\"]}，"
        "三条均为单段英文生图提示词，每条必须以如下格式严格输出（顺序不可调换，缺一不可）：\n"
        f"[统一风格] {INKWASH_PREFIX}\n"
        "[光线] soft diffused daylight（或夜景 soft light from paper window，三条必须相同）\n"
        "[时代+服饰+人物] 具体朝代标注 + 正确服饰 + 人物特征（武将→armor/military commander；老人→white-haired/elderly；禁光头矮胖）\n"
        "[动作+环境] 具体动作/表情 + 环境细节，三张图场景必须明显不同（不同地点/人物/活动）\n"
        "[构图] wide empty sky above、fading into mist\n"
        f"[收尾] {INKWASH_CLOSING}\n"
        "7) 图内绝不出现文字：不提 Chinese title / calligraphy / writing\n"
        f"8) 禁词（出现即废）：{' '.join(BANNED_PROMPT_WORDS)}\n"
        "9) 参考正文情节对应：图1封面主视觉、图2另一关键情节、图3第三个情节或收尾意象"
    )
    user = (
        f"标题：{state['title']}\n\n素材：\n{state['material'][:2500]}\n\n"
        f"正文：\n{Path(state['article_path']).read_text(encoding='utf-8')}"
    )

    problems: list[str] = []
    prompts: list[str] = []
    for attempt in range(4):
        extra = f"\n上次输出问题（必须修正）：{problems}" if problems else ""
        j = llm.extract_json(llm.chat([{"role": "system", "content": sys + extra},
                                       {"role": "user", "content": user}], model=llm.WRITE_MODEL, max_tokens=4096))
        prompts = [str(x).strip() for x in (j.get("prompts") or [])]
        # 自动修补：风格前缀/收尾是固定公式，LLM 漏写或改写时直接补齐再验（487 教训：
        # 三条全缺前缀时两轮重试全废 → 整图崩溃；禁词/条数问题不修补，仍靠重试）
        if len(prompts) == p.image_count:
            prompts = [(INKWASH_PREFIX + "\n" + t) if (p.image_style == "inkwash" and INKWASH_PREFIX not in t) else t
                       for t in prompts]
            prompts = [(t + "\n" + INKWASH_CLOSING) if (p.image_style == "inkwash" and INKWASH_CLOSING not in t) else t
                       for t in prompts]
            # 光线同属固定公式，按多数派自动补齐（516 教训：LLM 四轮统一不了光线措辞
            # 直接 raise——公式类一律修补，别赌重试）
            if p.image_style == "inkwash":
                if any("soft light from paper window" in t for t in prompts) and \
                        not any("soft diffused daylight" in t for t in prompts):
                    std = "soft light from paper window"
                else:
                    std = "soft diffused daylight"
                prompts = [(t if ("soft diffused daylight" in t or "soft light from paper window" in t)
                            else t + "\n" + std) for t in prompts]
        problems = _prompts_validation(p, prompts)
        if not problems:
            break
    if problems:
        raise RuntimeError(f"提示词校验失败: {problems}")

    out = []
    for i, t in enumerate(prompts, 1):
        f = Path(state["workdir"]) / "prompts" / f"0{i}-cover.md"
        f.parent.mkdir(exist_ok=True)
        f.write_text(t + "\n", encoding="utf-8")
        out.append(str(f))
    return {"prompts": out}


# ── 7. 生图（红线：gen 脚本必须 copy 自上一成功案例）─────
def _last_gen_source(workdir: Path) -> Path:
    best: tuple[int, Path] | None = None
    for script in repo.CARDS.glob("*/gen_fixed.py"):
        if script.parent.resolve() == workdir.resolve():
            continue
        m = re.fullmatch(r"topic-(\d+)", script.parent.name)
        rank = int(m.group(1)) if m else -1
        if best is None or rank > best[0]:
            best = (rank, script.parent)
    if best is None:
        raise RuntimeError("找不到含 gen_fixed.py 的上一成功案例（红线：脚本必须 copy，禁手写）")
    return best[1]


def gen_images(state: dict) -> dict:
    p = _p(state)
    _n(state, "images")
    wd = Path(state["workdir"])

    if state["dry_run"]:
        files = []
        for i in range(1, p.image_count + 1):
            f = wd / f"0{i}-cover.png"
            f.write_bytes(b"\x89PNG\r\n\x1a\nDRYRUN")
            files.append(str(f))
        return {"images": files, "image_issues": [], "attempts": state["attempts"]}

    if p.name != "history":
        raise NotImplementedError("P1.5：科技逐张/游记照片配图分支")

    expected = [wd / f"0{i}-cover.png" for i in range(1, p.image_count + 1)]
    missing = [f for f in expected if not f.exists() or f.stat().st_size == 0]
    if not missing:  # 幂等续跑：三张都在就不重生成
        return {"images": [str(f) for f in expected], "image_issues": [],
                "attempts": state["attempts"]}

    src = _last_gen_source(wd)
    for name in ("gen_fixed.py", "gen_one.py", "gen_no_ref.py"):
        if (src / name).exists():
            shutil.copy(src / name, wd / name)

    env = _tool_env()
    for i, key in enumerate(llm._keys()):  # noqa: SLF001 — gen_fixed 只认这 3 个变量名
        env[["AGNES_API_KEY", "AGNES_API_KEY2", "AGNES_API_KEY3"][i]] = key

    r = subprocess.run(["python3", "gen_fixed.py"], cwd=wd, env=env,
                       capture_output=True, text=True, timeout=900)
    still = [f.name for f in expected if not f.exists() or f.stat().st_size == 0]
    if r.returncode != 0 or still:
        tail = (r.stdout or "")[-800:] + (r.stderr or "")[-400:]
        raise RuntimeError(f"gen_fixed.py 失败(rc={r.returncode}), 缺失={still}\n{tail}")

    return {"images": [str(f) for f in expected], "image_issues": [],
            "attempts": state["attempts"]}


def verify_images(state: dict) -> dict:
    """真实分支：结构检查（存在/大小/PNG 魔数/宽高比≈3:4）。10 项视觉自查留给人审。"""
    if state["dry_run"]:
        return {"image_issues": []}
    issues = []
    for f in state.get("images", []):
        p = Path(f)
        if not p.exists():
            issues.append(f"{p.name}: 不存在")
            continue
        data = p.read_bytes()[:24]
        if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
            issues.append(f"{p.name}: 非 PNG")
            continue
        w, h = struct.unpack(">II", data[16:24])
        # XHS 接受 3:4 左右的比例，尺寸 600-1200 均可（API 偶发 864x1152 等变体）
        if abs(w * 4 - h * 3) > 100:
            issues.append(f"{p.name}: 宽高比异常 {w}x{h}（期望≈3:4）")
        if p.stat().st_size < 50_000:
            issues.append(f"{p.name}: 仅 {p.stat().st_size} 字节（疑似截断）")
    return {"image_issues": issues}


def route_images(state: dict) -> str:
    if state.get("image_issues"):
        return "gen_images" if state.get("attempts", {}).get("images", 0) < 3 else "report_error"
    return "create_feishu"


# ── 8. 飞书文档 + 串行插图 ───────────────────────────────
def create_feishu(state: dict) -> dict:
    p = _p(state)
    title = (p.title_prefix.format(n=state["topic_no"]) + state["title"]) if p.title_prefix else state["title"]
    wd = Path(state["workdir"])

    if state["dry_run"]:
        doc_id = "DRYRUN-DOC"
        line = f"{state['topic_no']}|{state['slug']}|{doc_id}" if state["topic_no"] else f"0|{state['slug']}|{doc_id}"
        return {"doc_id": doc_id,
                "doc_url": f"https://qcnh2b60jsx1.feishu.cn/docx/{doc_id}",
                "ledger_line": line}

    # 正文跳过第 1 行标题（标题单独传 --title），对应 tail -n +3
    lines = Path(state["article_path"]).read_text(encoding="utf-8").splitlines()
    body = "\n".join(lines[2:])
    r = subprocess.run(
        ["lark-cli", "docs", "+create", "--title", title, "--content", "-",
         "--doc-format", "markdown", "--as", "user", "--format", "json",
         "--parent-token", p.folder_token],
        input=body.encode("utf-8"), capture_output=True, cwd=wd, env=_tool_env(), timeout=180,
    )
    out = (r.stdout or b"").decode("utf-8", "replace")
    if r.returncode != 0:
        raise RuntimeError(f"lark-cli docs +create 失败: {(r.stderr or b'').decode('utf-8','replace')[:400]}")
    m = re.search(r'"document_id"\s*:\s*"([^"]+)"', out)
    if not m:
        raise RuntimeError(f"未取到 document_id（严禁占位符），原始输出: {out[:500]}")
    doc_id = m.group(1)

    # 只认 01/02/03-cover.png 规范名（glob 兜底时排除 *.bak.png 等手工备份，509 教训）
    images = state.get("images") or [
        str(f) for f in sorted(wd.glob("0*-cover.png")) if re.fullmatch(r"0\d-cover\.png", f.name)
    ]
    expected_names = [Path(img).name for img in images]

    # 🔴 media-insert 只允许此处单点串行（508/514 教训：并行调用各插一遍 → 每图×2，
    # 文档重复图且全部返回 ok:true 无告警）；并行必 429，且 --file 必须相对路径
    def _insert(rel: str) -> None:
        ir = subprocess.run(["lark-cli", "docs", "+media-insert", "--doc", doc_id,
                             "--file", rel, "--as", "user"],
                            capture_output=True, cwd=wd, env=_tool_env(), timeout=180)
        if ir.returncode != 0:
            raise RuntimeError(f"media-insert {rel} 失败: "
                               f"{(ir.stderr or b'').decode('utf-8','replace')[:300]}")
        time.sleep(3)

    def _doc_images() -> list[tuple[str, str]]:
        """fetch 文档，返回 [(img_name, file_token)]；解析失败返回 [] 并由调用方决定。"""
        fr = subprocess.run(["lark-cli", "docs", "+fetch", "--doc", doc_id, "--as", "user",
                             "--format", "json"],
                            capture_output=True, cwd=wd, env=_tool_env(), timeout=120)
        try:
            content = json.loads((fr.stdout or b"").decode("utf-8", "replace"))["data"]["document"]["content"]
        except Exception:  # noqa: BLE001
            return []
        return re.findall(r'<img name="([^"]+)"[^>]*src="([^"]+)"', content)

    for img in images:
        _insert(f"./{Path(img).name}")

    # 插完必须验图：数量 == 预期、无重复；缺图自动补插（最多补 2 轮），验不过即报错
    # （2026-09-30 教训：508/514 双循环插入 6 图无人察觉，用户翻文档才发现）
    verified = False
    for _pass in range(3):
        imgs = _doc_images()
        if not imgs:
            raise RuntimeError("docs +fetch 未能取回图片列表，无法验证插图结果（严禁跳过验图直接归档）")
        names = [n for n, _ in imgs]
        srcs = [s for _, s in imgs]
        if len(srcs) != len(set(srcs)):
            raise RuntimeError(f"文档存在重复插图 {names}——删除该文档后重建（508/514 教训）")
        missing = [n for n in expected_names if names.count(n) < 1]
        if not missing and len(names) == len(expected_names):
            verified = True
            break
        for rel in missing:
            _insert(f"./{rel}")
    if not verified:
        raise RuntimeError(f"插图验证未通过（期望 {expected_names}，实际 {names}），"
                           "补齐重试已耗尽——禁止带着不完整文档归档")

    line = f"{state['topic_no']}|{state['slug']}|{doc_id}" if state["topic_no"] else f"0|{state['slug']}|{doc_id}"
    return {"doc_id": doc_id, "doc_url": f"https://qcnh2b60jsx1.feishu.cn/docx/{doc_id}",
            "ledger_line": line}


# ── 9. 人工审核（唯一 interrupt 点 = 发布闸门）────────────
def human_review(state: dict) -> dict:
    decision = interrupt(
        {
            "type": "xhs_review",
            "topic": state["slug"],
            "title": state["title"],
            "doc_url": state["doc_url"],
            "verify": state.get("verify"),
            "fact_check": state.get("fact_check"),
            "image_issues": state.get("image_issues"),
            "options": ["approve=存草稿", "rewrite=重写正文", "redraw=重新生图", "archive=仅归档"],
        }
    )
    return {"review_decision": str(decision)}


def route_review(state: dict) -> str:
    d = state.get("review_decision", "")
    return {
        "approve": "publish_draft",
        "rewrite": "write_article",
        "redraw": "gen_images",
        "archive": "record",
    }.get(d, "human_review")  # 非法输入 → 重新 interrupt


# ── 10. 存草稿（红线：只有 approve 能到这）───────────────
def publish_draft(state: dict) -> dict:
    if state.get("review_decision") != "approve":
        raise RuntimeError("红线拦截：未经 approve 不得触达 publish")
    if state["dry_run"]:
        return {"publish_result": "dry-run skip — 实际执行："
                "opencli xiaohongshu creator-profile && opencli xiaohongshu publish --draft true"}

    art = Path(state["article_path"])
    lines = art.read_text(encoding="utf-8").splitlines()
    imgs = ",".join(state.get("images", []))
    env = _tool_env()

    r = subprocess.run(["opencli", "xiaohongshu", "creator-profile",
                        "--site-session", "persistent", "--keep-tab", "true"],
                       capture_output=True, cwd=repo.REPO, env=env, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(f"creator-profile 失败: "
                           f"{(r.stderr or b'').decode('utf-8','replace')[:300]}")

    env["OPENCLI_BROWSER_COMMAND_TIMEOUT"] = "180000"
    r2 = subprocess.run(["opencli", "xiaohongshu", "publish", "\n".join(lines),
                         "--title", lines[0].strip(), "--images", imgs,
                         "--window", "foreground", "--site-session", "persistent",
                         "--draft", "true", "--format", "yaml"],
                        capture_output=True, cwd=repo.REPO, env=env, timeout=300)
    out = (r2.stdout or b"").decode("utf-8", "replace")
    err = (r2.stderr or b"").decode("utf-8", "replace")
    if r2.returncode != 0 or "暂存成功" not in out + err:
        raise RuntimeError(f"publish 失败(rc={r2.returncode}):\n{out[-600:]}\n{err[-400:]}")
    return {"publish_result": next((l for l in (out + err).splitlines() if "暂存" in l), "暂存成功")}


# ── 11. 记录台账（真实 = 追加 + 只提交本主题文件）─────────
def record(state: dict) -> dict:
    line = state.get("ledger_line", "")
    if state["dry_run"]:
        return {"record_note": f"dry-run 不写台账；将追加: {line!r} 并 git add/commit/push 本主题文件"}
    if not line:
        raise RuntimeError("缺 ledger_line，严禁占位符")
    with repo.LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(line + "\n")
    subprocess.run(["git", "add", str(repo.LEDGER), state["workdir"]],
                   cwd=repo.REPO, check=True)
    subprocess.run(["git", "commit", "-m",
                    f"Add topic {state['topic_no']} {state['slug']} (feishu {state['doc_id']})"],
                   cwd=repo.REPO, check=True)
    # 推送 GitHub：失败不致命（本地已提交有兜底，网络/代理抖动时后续补推即可）
    push_note = ""
    try:
        pr = subprocess.run(["git", "push", "origin", "HEAD"],
                            cwd=repo.REPO, capture_output=True, timeout=300)
        if pr.returncode == 0:
            push_note = "，已推送 GitHub"
        else:
            tail = (pr.stderr or b"").decode("utf-8", "replace").strip()[-200:]
            push_note = f"，⚠ push 失败（本地已提交，稍后 git push 补推）: {tail}"
    except subprocess.TimeoutExpired:
        push_note = "，⚠ push 超时（本地已提交，稍后 git push 补推）"
    return {"record_note": f"已追加台账并提交: {line}{push_note}"}


# ── 终端节点 ─────────────────────────────────────────────
def report_skip(state: dict) -> dict:
    return {"record_note": f"查重跳过: {state.get('dedup_notes')}"}


def report_error(state: dict) -> dict:
    return {"errors": [f"验证/生图重试超限，停止。verify={state.get('verify')} "
                       f"fact_check={state.get('fact_check')} "
                       f"image_issues={state.get('image_issues')} "
                       f"attempts={state.get('attempts')}"]}


# ── 路由 ─────────────────────────────────────────────────
def route_dedup(state: dict) -> str:
    return "report_skip" if state["dedup_verdict"] == "skip" else "write_article"


def route_fact(state: dict) -> str:
    if not state["fact_check"]["passed"]:
        if state.get("attempts", {}).get("fact", 0) >= 2:
            return "report_error"
        return "write_article"
    return "write_prompts" if _p(state).needs_image_gen else "create_feishu"



