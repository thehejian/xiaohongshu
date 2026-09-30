# -*- coding: utf-8 -*-
"""CLI — 小红书创作发布流水线。

用法（默认演练模式，`--real` 才真实执行；P0 阶段真实分支会显式报错）:

  uv run cli.py run --series history                # 用台账最大序号+1，跑到审核闸门
  uv run cli.py run --series history --topic 454    # 指定序号
  uv run cli.py run --series history --resume approve   # 审核续跑: approve/rewrite/redraw/archive
"""
from __future__ import annotations

import argparse
import json
import sys

from langgraph.types import Command

from xhs_graph.graph import build_graph


def parse() -> argparse.Namespace:
    ap = argparse.ArgumentParser(prog="xhs-graph")
    sub = ap.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run", help="执行流水线（默认 dry-run）")
    run.add_argument("--series", choices=["history", "tech", "travel"], default="history")
    run.add_argument("--topic", type=int, help="主题序号（history 默认取台账最大+1）")
    run.add_argument("--slug", help="tech/travel 的英文目录名")
    run.add_argument("--real", action="store_true", help="真实执行（P0 阶段会 NotImplementedError）")
    run.add_argument("--resume", choices=["approve", "rewrite", "redraw", "archive"],
                     help="从审核闸门续跑")
    run.add_argument("--jump-to", choices=["resolve_topic","dedup","write_article","verify_article",
                        "fact_check","write_prompts","gen_images","verify_images",
                        "create_feishu","human_review","publish_draft","record"],
                     help="调试：从指定节点重新跑（覆盖 checkpoint）")
    run.add_argument("--thread", help="checkpoint 线程 id（默认 <series>-<topic>）")
    return ap.parse_args()


def main() -> int:
    args = parse()
    if args.cmd != "run":
        return 2
    if args.resume and not (args.topic or args.thread):
        print("❌ --resume 必须带 --topic 或 --thread（否则找不到闸门断点）")
        return 2
    dry_run = not args.real
    thread = args.thread or f"{args.series}-{args.topic or 'auto'}"
    config = {"configurable": {"thread_id": thread}}
    graph = build_graph()

    if not args.resume and not args.jump_to:
        # 全新启动：旧 thread 若有残留 checkpoint（attempts/verify 等会污染本次运行，
        # 474/476/483 曾因此误报"重试超限"），自动换新线程号
        if graph.get_state(config).values:
            base, i = thread, 2
            while True:
                config["configurable"]["thread_id"] = f"{base}-{i}"
                if not graph.get_state(config).values:
                    break
                i += 1
            thread = config["configurable"]["thread_id"]
            print(f"⚠ 旧线程 {base} 有残留状态，改用新线程 {thread}")

    if args.jump_to:
        # 调试模式：直接注入目标节点输入，从该节点继续
        print(f"▶ 调试 jump-to={args.jump_to} thread={thread}")
        # 先获取最新 state（含之前所有节点产出）
        snap = graph.get_state(config)
        # 如果状态里有中断信息，先清除
        inp = dict(snap.values or {})
        inp["series"] = args.series
        if args.topic:
            inp["topic_no"] = args.topic
        if args.resume:
            inp["review_decision"] = args.resume
        inp["dry_run"] = dry_run
        # 让 graph 从 jump_to 节点开始重新跑（清除后续节点 state 以确保干净）
        cfg2 = {"configurable": {"thread_id": thread, "checkpoint_id": snap.checkpoint_id}}
        # 清空目标节点之后的 state，从该节点重跑
        cfg2["__restart_at"] = args.jump_to
        return _run_loop(graph, cfg2, inp, args)

    if args.resume:
        inp = Command(resume=args.resume)
        print(f"▶ 续跑 thread={thread} resume={args.resume}（dry_run={dry_run}）")
    else:
        inp = {"series": args.series, "dry_run": dry_run}
        if args.topic:
            inp["topic_no"] = args.topic
        if args.slug:
            inp["slug"] = args.slug
        print(f"▶ 启动 thread={thread}（dry_run={dry_run}）")

    try:
        for update in graph.stream(inp, config, stream_mode="updates"):
            for node, val in (update or {}).items():
                if node == "__end__":
                    continue
                if not isinstance(val, dict):
                    print(f"  · {node}: {str(val)[:160]}")
                    continue
                brief = {k: v for k, v in val.items()
                         if k in ("topic_no", "slug", "title", "dedup_verdict", "verify",
                                  "doc_url", "review_decision", "publish_result",
                                  "record_note", "errors", "image_issues")}
                print(f"  · {node}: {json.dumps(brief, ensure_ascii=False, default=str)}")
    except Exception as exc:  # noqa: BLE001 — interrupt 以异常形态冒出，统一收口
        print(f"  ⚠ {type(exc).__name__}: {exc}")

    snapshot = graph.get_state(config)
    pending = list(snapshot.next or ())
    if pending:
        payload = {}
        for task in snapshot.tasks:
            for it in getattr(task, "interrupts", ()) or ():
                payload = getattr(it, "value", {})
        print(f"\n⏸ 闸门暂停于 {pending}")
        print(f"   审核入口: {json.dumps(payload, ensure_ascii=False, default=str)}")
        print(f"   续跑命令: uv run cli.py run --series {args.series}"
              + (f" --topic {args.topic}" if args.topic else " --topic <N>")
              + f" --resume <approve|rewrite|redraw|archive> --thread {thread}"
              + (" --real" if args.real else ""))
        return 3

    final = snapshot.values or {}
    print("\n✅ 运行结束")
    for k in ("dedup_verdict", "doc_url", "publish_result", "record_note", "errors"):
        if final.get(k):
            print(f"   {k}: {final[k]}")
    return 0 if not final.get("errors") else 1


if __name__ == "__main__":
    sys.exit(main())
