# -*- coding: utf-8 -*-
"""红线测试：未经 approve 不可能触达 publish；写后验证三条判定。"""
from __future__ import annotations

import pytest
from langgraph.types import Command

from xhs_graph import nodes, repo
from xhs_graph.graph import build_graph

TOPIC = 454  # 素材库有该主题


@pytest.fixture()
def graph(tmp_path, monkeypatch):
    monkeypatch.setattr(repo, "DRYRUN_ROOT", tmp_path / "dryrun")
    return build_graph(db_path=tmp_path / "ck.db")


def _cfg(thread: str) -> dict:
    return {"configurable": {"thread_id": thread}}


def _run_to_gate(graph, thread: str) -> dict:
    cfg = _cfg(thread)
    for _ in graph.stream({"series": "history", "dry_run": True, "topic_no": TOPIC}, cfg):
        pass
    snap = graph.get_state(cfg)
    assert tuple(snap.next) == ("human_review",), f"应在审核闸门暂停, 实际 {snap.next}"
    return cfg


def test_gate_stops_before_publish(graph):
    cfg = _run_to_gate(graph, "t-gate")
    vals = graph.get_state(cfg).values
    assert "publish_result" not in vals  # 未 approve 绝不产出发布结果


def test_archive_never_publishes(graph):
    cfg = _run_to_gate(graph, "t-archive")
    graph.invoke(Command(resume="archive"), cfg)
    vals = graph.get_state(cfg).values
    assert "publish_result" not in vals
    assert vals.get("record_note", "").startswith("dry-run")


def test_approve_reaches_publish(graph):
    cfg = _run_to_gate(graph, "t-approve")
    graph.invoke(Command(resume="approve"), cfg)
    vals = graph.get_state(cfg).values
    assert "dry-run" in vals.get("publish_result", "")


def test_publish_node_hard_guard():
    with pytest.raises(RuntimeError, match="红线拦截"):
        nodes.publish_draft({"review_decision": "archive", "dry_run": True})


def test_verify_rejects_long_title(tmp_path):
    art = tmp_path / "article.md"
    art.write_text("这是一个超过二十个字的超级长标题绝对不合格\n\n" + "正文" * 400, encoding="utf-8")
    out = nodes.verify_article({"article_path": str(art), "series": "history"})
    assert out["verify"]["passed"] is False
    assert any("标题" in p for p in out["verify"]["problems"])


def test_verify_rejects_cliche_title(tmp_path):
    """509/513 用户连续打回「我没想到」句式 → verify 硬校验必须打回。"""
    art = tmp_path / "article.md"
    art.write_text("我没想到诸葛亮还玩过这一手\n\n" + "正文" * 400, encoding="utf-8")
    out = nodes.verify_article({"article_path": str(art), "series": "history"})
    assert out["verify"]["passed"] is False
    assert any("我没想到" in p for p in out["verify"]["problems"])


def test_verify_accepts_concrete_title(tmp_path):
    art = tmp_path / "article.md"
    art.write_text("斩马谡贬自己：诸葛亮的赏罚组合拳\n\n" + "正文" * 400, encoding="utf-8")
    out = nodes.verify_article({"article_path": str(art), "series": "history"})
    assert out["verify"]["passed"] is True, out["verify"]["problems"]


def test_inkwash_closing_has_style_anchor():
    """499/509 教训：收尾约束必须含正反双面风格锚点，防线描平涂漂移。"""
    from xhs_graph.nodes import INKWASH_CLOSING
    assert "ink-and-wash" in INKWASH_CLOSING
    assert "No clean digital outlines" in INKWASH_CLOSING
    assert "paper grain" in INKWASH_CLOSING
