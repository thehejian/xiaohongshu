# -*- coding: utf-8 -*-
"""图组装 + SQLite checkpointer（断点续跑、interrupt 均依赖它）。"""
from __future__ import annotations

import sqlite3
from pathlib import Path

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, StateGraph

from . import nodes
from .state import XhsState

CHECKPOINT_DB = Path(__file__).resolve().parents[1] / ".state" / "graph.db"


def build_graph(db_path: Path | None = None):
    db = Path(db_path) if db_path else CHECKPOINT_DB
    db.parent.mkdir(parents=True, exist_ok=True)
    saver = SqliteSaver(sqlite3.connect(str(db), check_same_thread=False))

    g = StateGraph(XhsState)
    for name, fn in [
        ("resolve_topic", nodes.resolve_topic),
        ("dedup", nodes.dedup),
        ("write_article", nodes.write_article),
        ("verify_article", nodes.verify_article),
        ("fact_check", nodes.fact_check),
        ("write_prompts", nodes.write_prompts),
        ("gen_images", nodes.gen_images),
        ("verify_images", nodes.verify_images),
        ("create_feishu", nodes.create_feishu),
        ("human_review", nodes.human_review),
        ("publish_draft", nodes.publish_draft),
        ("record", nodes.record),
        ("report_skip", nodes.report_skip),
        ("report_error", nodes.report_error),
    ]:
        g.add_node(name, fn)

    g.set_entry_point("resolve_topic")
    g.add_edge("resolve_topic", "dedup")
    g.add_conditional_edges("dedup", nodes.route_dedup, {
        "write_article": "write_article",
        "report_skip": "report_skip",
    })
    g.add_edge("write_article", "verify_article")
    g.add_conditional_edges("verify_article", nodes.route_verify, {
        "fact_check": "fact_check",
        "write_article": "write_article",
        "report_error": "report_error",
    })
    g.add_conditional_edges("fact_check", nodes.route_fact, {
        "write_prompts": "write_prompts",
        "create_feishu": "create_feishu",
        "write_article": "write_article",
        "report_error": "report_error",
    })
    g.add_edge("write_prompts", "gen_images")
    g.add_edge("gen_images", "verify_images")
    g.add_conditional_edges("verify_images", nodes.route_images, {
        "gen_images": "gen_images",
        "create_feishu": "create_feishu",
        "report_error": "report_error",
    })
    g.add_edge("create_feishu", "human_review")
    g.add_conditional_edges("human_review", nodes.route_review, {
        "publish_draft": "publish_draft",
        "write_article": "write_article",
        "gen_images": "gen_images",
        "record": "record",
        "human_review": "human_review",
    })
    g.add_edge("publish_draft", "record")
    g.add_edge("report_skip", END)
    g.add_edge("report_error", END)
    g.add_edge("record", END)
    return g.compile(checkpointer=saver)
