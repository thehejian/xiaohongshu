# -*- coding: utf-8 -*-
"""仓库读写：序号、素材解析、查重、台账。

只读操作可任意调用；写操作（台账/git）由节点在非演练模式下才执行。
"""
from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]          # 003-Twitter/
LEDGER = REPO / ".feishu_uploaded"
MATERIAL_FILE = REPO / "正文提示词.md"
CARDS = REPO / "image-cards"
DRAFTS_CACHE = Path("/tmp/xhs_drafts.txt")
DRYRUN_ROOT = REPO / "langgraph" / ".state" / "dryrun"


def next_topic_no() -> int:
    """台账中 topic- 行首数字最大值 +1（不用最后一行，见 AGENTS.md 第0步）。"""
    m = 0
    if LEDGER.exists():
        for line in LEDGER.read_text(encoding="utf-8").splitlines():
            parts = line.split("|")
            if len(parts) >= 2 and parts[1].startswith("topic-"):
                try:
                    m = max(m, int(parts[0]))
                except ValueError:
                    pass
    return m + 1


def extract_material(topic_no: int) -> dict[str, str]:
    """从 正文提示词.md 取 `## 主题 N` 整块，解析 title / folder / body。"""
    text = MATERIAL_FILE.read_text(encoding="utf-8")
    pat = re.compile(rf"^## 主题 {topic_no}(?:[:：\s]|$)", re.M)
    m = pat.search(text)
    if not m:
        raise SystemExit(f"素材库无「主题 {topic_no}」，检查 正文提示词.md")
    nxt = re.compile(r"^## 主题 \d+", re.M).search(text, m.end())
    block = text[m.start(): nxt.start() if nxt else len(text)].strip()

    head = block.splitlines()[0]
    raw_title = re.sub(r"^## 主题 \d+[:：]?\s*", "", head).strip()

    fm = re.search(r"^\*\*folder\*\*:\s*(.+)$", block, re.M)
    folder = fm.group(1).strip() if fm else f"topic-{topic_no}"

    bm = re.search(r"^### 正文\s*\n+(.*?)(?=^### |\Z)", block, re.M | re.S)
    body = bm.group(1).strip() if bm else ""

    return {"raw_title": raw_title, "folder": folder, "body": body, "block": block}


def clamp_title(raw: str, limit: int = 20) -> str:
    """素材标题裁到 ≤20 字：优先取「：」前半段，仍超则硬截断。"""
    if len(raw) <= limit:
        return raw
    head = raw.split("：")[0]
    if 0 < len(head) <= limit:
        return head
    return raw[:limit]


def workdir_for(series: str, topic_no: int, slug: str, dry_run: bool, dir_template: str) -> Path:
    """真实=仓库 image-cards/<目录>；演练=.state/dryrun/<目录>（不碰共享目录）。"""
    name = dir_template.format(n=topic_no, slug=slug)
    base = DRYRUN_ROOT if dry_run else CARDS
    return base / name


def ledger_titles(limit: int = 40) -> list[tuple[str, str]]:
    """台账最近条目 → [(slug, ...)]，用于查重参照。"""
    if not LEDGER.exists():
        return []
    rows = [l.split("|") for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]
    out = []
    for parts in rows[-limit:]:
        if len(parts) >= 2:
            out.append((parts[0], parts[1]))
    return out


def scan_article_titles() -> list[tuple[str, str]]:
    """image-cards/*/article.md → [(目录名, 第1行标题)]。"""
    out = []
    if CARDS.exists():
        for art in sorted(CARDS.glob("*/article.md")):
            first = art.read_text(encoding="utf-8", errors="ignore").splitlines()
            if first:
                out.append((art.parent.name, first[0].strip()))
    return out


def dedup_hits(keywords: list[str]) -> list[str]:
    """关键词在已有 article.md 里的命中目录（正文查重第 1 层，确定性部分）。"""
    hits: set[str] = set()
    if not CARDS.exists():
        return []
    for art in CARDS.glob("*/article.md"):
        try:
            content = art.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for kw in keywords:
            if len(kw) >= 2 and kw in content:
                hits.add(art.parent.name)
                break
    return sorted(hits)


def title_keywords(raw_title: str) -> list[str]:
    """素材标题 → 查重关键词：按 标点 切分，保留 ≥2 字的片段。"""
    parts = re.split(r"[：:，、。「」\s]+", raw_title)
    return [p for p in parts if len(p) >= 2]
