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
    run.add_argument("--auto-archive", action="store_true",
                     help="到审核闸门后自动 resume archive（仅归档不发布，批量用）")
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
        # 调试模式：从目标节点本身重跑（不重跑上游，保住已通过的产物）
        snap = graph.get_state(config)
        inp = dict(snap.values or {})
        inp["series"] = args.series
        if args.topic:
            inp["topic_no"] = args.topic
        if args.resume:
            inp["review_decision"] = args.resume
        inp["dry_run"] = dry_run
        # 找目标节点的前驱，以它的身份写状态 → 图下一步执行的目标节点本身
        # （StateSnapshot 无 checkpoint_id，旧实现调用不存在的 _run_loop，从未跑通过）
        preds = [e.source for e in graph.get_graph().edges
                 if e.target == args.jump_to and e.source not in ("__start__",)]
        if not preds:
            print(f"❌ 找不到 {args.jump_to} 的前驱节点，无法定位重跑起点")
            return 2
        graph.update_state(config, inp, as_node=preds[0])
        inp = None  # 从新 checkpoint 继续执行
        print(f"▶ 调试 jump-to={args.jump_to} thread={thread}（前驱 {preds[0]}）")

    elif args.resume:
        # 守卫：只允许对停在审核闸门的线程续跑（516 教训：对空线程 --resume 会
        # KeyError 'series' 还留下毒 checkpoint，白跑一轮）
        snap0 = graph.get_state(config)
        nxt = list(snap0.next or ())
        if not snap0.values or nxt != ["human_review"]:
            print(f"❌ --resume 无效：线程 {thread} 未停在审核闸门"
                  f"（已有状态={bool(snap0.values)}, next={nxt}）。")
            print("   全新任务 → 去掉 --resume 直接跑（report_error 后重跑同理）；")
            print("   已到闸门 → --thread 用运行时打印的线程号（可能带 -2/-3 后缀）。")
            return 2
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
        if args.auto_archive and pending == ["human_review"]:
            # 批量模式：同进程内直接归档（线程号无需人工记录），绝不触达 publish
            print("⏵ --auto-archive：自动 archive（仅记台账+commit+push，不存草稿）")
            try:
                for _ in graph.stream(Command(resume="archive"), config, stream_mode="updates"):
                    pass
            except Exception as exc:  # noqa: BLE001
                print(f"  ⚠ archive 失败: {type(exc).__name__}: {exc}")
                return 3
            fin = graph.get_state(config).values or {}
            print(f"   doc_url: {fin.get('doc_url')}")
            print(f"   record_note: {fin.get('record_note')}")
            return 0 if not fin.get("errors") else 1
        return 3

    final = snapshot.values or {}
    print("\n✅ 运行结束")
    for k in ("dedup_verdict", "doc_url", "publish_result", "record_note", "errors"):
        if final.get(k):
            print(f"   {k}: {final[k]}")
    return 0 if not final.get("errors") else 1


if __name__ == "__main__":
    sys.exit(main())
