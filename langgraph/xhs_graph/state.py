# -*- coding: utf-8 -*-
"""XHS 创作发布流水线的共享状态（LangGraph State）。

字段只增不改名：checkpointer 里已存的历史 state 依赖这些键。
"""
from __future__ import annotations

from typing import Any, NotRequired, TypedDict


class XhsState(TypedDict, total=False):
    # ── 运行参数 ────────────────────────────────
    series: str          # history | tech | travel
    topic_no: int        # 历史类序号（tech/travel 为 0，用 slug）
    slug: str            # 目录名：topic-454 或 tech 英文 slug
    dry_run: bool        # True=演练（默认），False=真实执行
    # ── 素材与产物 ──────────────────────────────
    title: str           # article.md 第 1 行标题
    material: str        # 素材块原文（正文提示词.md 的 ## 主题 N 段）
    workdir: str         # 产物绝对目录
    article_path: str
    verify: dict[str, Any]        # 三条写后验证结果
    fact_check: dict[str, Any]
    prompts: list[str]            # 3 条 prompt 文件路径
    images: list[str]             # 生成的图片路径
    image_issues: list[str]       # 验图失败记录
    # ── 查重 ───────────────────────────────────
    dedup_verdict: str   # skip | continue | rewrite-angle
    dedup_notes: str
    # ── 飞书 / 审核 ────────────────────────────
    doc_id: str
    doc_url: str
    ledger_line: str             # 待追加进 .feishu_uploaded 的行
    review_decision: str         # approve | rewrite | redraw | archive
    # ── 发布 / 记录 ────────────────────────────
    publish_result: str
    record_note: str
    # ── 控制 ───────────────────────────────────
    attempts: dict[str, int]     # 各环节重试计数，防死循环
    errors: list[str]
