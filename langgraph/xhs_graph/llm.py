# -*- coding: utf-8 -*-
"""Agnes chat 封装（OpenAI 兼容）。

- 3 个 key 从 ~/.baoyu-skills/.env 读取（AGNES_API_KEY / KEY2 / KEY3），按序轮换
- 401/402/403 → 换 key；429/5xx → 退避重试；多次失败才抛错
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

import requests

BASE = "https://apihub.agnes-ai.com/v1"
ENV_FILE = Path.home() / ".baoyu-skills" / ".env"

WRITE_MODEL = os.environ.get("XHS_WRITE_MODEL", "agnes-2.5-flash")
CHECK_MODEL = os.environ.get("XHS_CHECK_MODEL", "agnes-2.5-flash")


def _keys() -> list[str]:
    keys: list[str] = []
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\s*(AGNES_API_KEY\d*)\s*=\s*(.+?)\s*$", line)
            if m:
                keys.append(m.group(2).strip().strip('"').strip("'"))
    for env in ("AGNES_API_KEY", "AGNES_API_KEY2", "AGNES_API_KEY3"):
        if os.environ.get(env):
            keys.append(os.environ[env])
    seen, out = set(), []
    for k in keys:
        if k and k not in seen:
            seen.add(k)
            out.append(k)
    return out


def chat(messages: list[dict], model: str | None = None,
         temperature: float = 0.7, max_tokens: int = 4096, tries: int = 9) -> str:
    model = model or WRITE_MODEL
    keys = _keys()
    if not keys:
        raise RuntimeError(f"无可用 AGNES key（{ENV_FILE} 与环境变量均空）")
    last = "unknown"
    for i in range(tries):
        key = keys[i % len(keys)]
        try:
            r = requests.post(
                f"{BASE}/chat/completions",
                json={"model": model, "messages": messages,
                      "temperature": temperature, "max_tokens": max_tokens},
                headers={"Authorization": f"Bearer {key}"},
                timeout=180,
            )
        except requests.RequestException as e:
            last = f"network: {e}"
            time.sleep(2)
            continue
        if r.status_code == 200:
            try:
                return r.json()["choices"][0]["message"]["content"]
            except Exception:  # noqa: BLE001
                last = f"bad payload: {r.text[:200]}"
        elif r.status_code in (401, 402, 403):
            last = f"HTTP {r.status_code}: {r.text[:150]}"
            time.sleep(1)
        elif r.status_code == 429 or r.status_code >= 500:
            last = f"HTTP {r.status_code}"
            time.sleep(3)
        else:
            raise RuntimeError(f"Agnes {model} HTTP {r.status_code}: {r.text[:300]}")
    raise RuntimeError(f"Agnes {model} 重试 {tries} 次仍失败: {last}")


def extract_json(text: str):
    """容错解析：剥掉 ``` 围栏，规范化引号/破折号，取第一个 JSON 对象/数组。"""
    t = text.strip()
    if t.startswith("```"):
        t = re.sub(r"^```[a-zA-Z]*\s*", "", t)
        t = re.sub(r"\s*```$", "", t)
    t = t.strip()
    # 中文弯引号 → ASCII 直引号（模型偶尔会混用）
    t = t.replace("\u201c", '"').replace("\u201d", '"')
    t = t.replace("\u2018", "'").replace("\u2019", "'")
    # 中文括号/书名号保留（JSON字符串值内合法），但中文逗号/顿号可能破坏结构，替换为逗号
    t = t.replace("\uff0c", ",").replace("\u3001", ",")
    s = re.search(r"[\[{]", t)
    if not s:
        raise ValueError(f"响应中无 JSON: {text[:200]}")
    # 找匹配的闭合括号（处理嵌套）
    bracket = "{" if t[s.start()] == "{" else "["
    end_bracket = "}" if bracket == "{" else "]"
    depth = 0
    in_str = False
    escape = False
    for i in range(s.start(), len(t)):
        c = t[i]
        if escape:
            escape = False
            continue
        if c == "\\" and in_str:
            escape = True
            continue
        if c == '"' and not escape:
            in_str = not in_str
            continue
        if in_str:
            continue
        if c == bracket:
            depth += 1
        elif c == end_bracket:
            depth -= 1
            if depth == 0:
                return json.loads(t[s.start(): i + 1])
    raise ValueError(f"响应中无完整 JSON: {text[:200]}")
