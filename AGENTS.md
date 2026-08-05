# AGENTS.md — 003-Twitter

Social media content farm: XHS image-card articles (西汉风云 history/literature) for @DubaIGOHGOkTHOk.

## Hard rules

- **Never execute Twitter/X post commands** — prepare text, user sends manually
- `.png`/`.jpg`/`.jpeg` gitignored — never commit images
- **🚨 Two mandatory review gates, NEVER skip: (1) Chinese prompts pre-review → user confirms → generate images; (2) Feishu doc → user reviews → ONLY after user says OK → save XHS draft. DO NOT auto-save XHS draft after Feishu upload**
- **每次修改（正文/配图）后必须新建飞书文档保存**，不能更新已有文档
- **飞书审核→确认无误→才存草稿**：先 `creator-profile` 验证 session，再 `publish --draft true`
- XHS 标题≤20 CJK字（含标点），正文≤950字纯文本，tags 用 `#话题` 附在正文末尾
- All Python scripts with Chinese text need `# -*- coding: utf-8 -*-` (system Python 3.9)

## Setup

```bash
export PATH="/opt/homebrew/bin:$PATH"
set -a; source ~/.baoyu-skills/.env; set +a
```

- Agnes API: `apihub.agnes-ai.com` (NOT `api.agnesai.com`)
- 3 keys: `AGNES_API_KEY`, `AGNES_API_KEY2`, `AGNES_API_KEY3`
- lark-cli at `/opt/homebrew/bin/lark-cli`; auth: `cli_aadef45343f91cc3` on `qcnh2b60jsx1.feishu.cn` (user 何健)
- Feishu re-login: `lark-cli auth login --no-wait --json --domain all` → device code → `lark-cli auth login --device-code <code>`

## Folder layout

- `image-cards/<topic>/` — CURRENT pipeline. Only create new topics here.
- `*-xhs/` (300+ dirs) — LEGACY SVG+Inkscape pipeline, do not touch
- `_gen_runner.py` / `batch_gen.py` — LEGACY, do not use

## Article pipeline

### Writing style — must be engaging

Write like you're telling a friend a fascinating story. 情感真挚, avoid textbook tone. Use vivid details, concrete scenes, and narrative tension. The title should spark curiosity — a question, a contrast, or an unexpected angle. Aim for readers to think "I didn't know that" and want to share.

### Historical accuracy — must verify

Cite specific events, names, numbers, and years. **Verify any lesser-known claim** before writing — check against `book/两汉风云.epub` and structured references (史记/资治通鉴). Don't invent or approximate. If unsure, omit rather than guess.

Primary source hierarchy:
1. `book/两汉风云.epub` — current series, topics 22–35
2. `book/让人拍案叫绝的中国史(套装共2册).epub` — finished 楚汉争霸 series
3. Structured references: 史记/资治通鉴/汉书

### New topic workflow

1. Write `article.md` — **5±2 paragraphs, 2–5 sentences each, ~800 chars total**. No 古文 quotes unless asked.
2. Write **3 English prompts** `prompts/01-cover.md` … `03-*.md` (was 6, changed from topic 150 onward)
3. Translate prompts to Chinese → user approves → proceed
4. Generate 3 images via `gen_one.py` (already in each topic folder)
5. Upload to Feishu (see below) → user reviews → XHS draft

### Article char count — critical

Target: **750–850 chars** (after stripping spaces/newlines). No 古文 quotes unless asked.

```python
# Verify:
len(article.replace('\n','').replace(' ',''))
```

If <700 chars, expand the main narrative with more vivid scenes and details — **do NOT** add 后世影响/现代启示 sections (phased out).

### Existing enrichment scripts

| Script | Topics | Purpose |
|--------|--------|---------|
| `enrich_v2.py` | 56–100 | Base article content (~450 chars each) in dict `A` |
| `enrich_v3_batch1.py` | 56–77 | Enrichment (~400 chars) + Feishu upload |
| `enrich_v3_batch2.py` | 78–100 | Enrichment (~400 chars) + Feishu upload |

All topics **1–100** are enriched and uploaded to Feishu (they still use the old 后世影响+现代启示 enrichment, but new topics from 144 onward must NOT).

### Feishu title format

`场景{num}：{title}` — e.g. `场景56：武帝双标——卜式与相如追星`

### Feishu upload

```bash
export PATH="/opt/homebrew/bin:$PATH"
# Create doc (passing content via stdin):
echo "$article_text" | lark-cli docs +create --title "场景N：标题" --content - --doc-format markdown --as user --format json

# Insert images sequentially (parallel → 429):
lark-cli docs +media-insert --doc <token> --file ./01-cover.png --as user
lark-cli docs +media-insert --doc <token> --file ./02-cover.png --as user
lark-cli docs +media-insert --doc <token> --file ./03-cover.png --as user
# ... 3 total, sleep 3s between each
```

**Tracking**: `.feishu_uploaded` records `NNN|folder-name|doc-token` — always append, never deduplicate.

### Enrichment/upload via script

```bash
# Run in background, check enrich_batch{N}.log:
python3 -u enrich_v3_batch1.py 56 77 > enrich_batch1.log 2>&1 &
```

Each topic takes ~30–90s to upload (create doc + 3 image inserts).

## Image generation (`gen_one.py`)

- Model: `agnes-image-2.1-flash` (falls back to `agnes-image-2.0-flash`)
- 3 parallel threads using `AGNES_API_KEY{i % 3}`
- Cover (`python3 gen_one.py 1`) has no reference image
- Subsequent images (`python3 gen_one.py 2 3`, `4 5`, `6`) use `01-cover.png` as ref
- 20 max retries per image; 503 / 000 empty responses are normal
- Prompt file: `prompts/{num:02d}-cover.md`; output: `{num:02d}-cover.png`
- Cover filename **must** be `01-cover.png` (ref step reads this exact name)

### Content policy — critical

- English prompt = **neutral scene description only**. Chinese subtitle carries meaning.
- NEVER: `corpse`/`blood`/`collapse`/`torture`/`starving`/`cannibalism`/`abyss`/`suffocating`/`harem`/`reclining`/`dark plot`/`scheming`
- Check for exact string `content_policy_violation` (not `content_policy`)
- Policy-violated prompts: rewrite immediately, don't retry

### Regeneration

User says "图X重画" → regenerate that image with ref → rebuild ENTIRE Feishu doc.
User says "不要第X张" → omit from `--images` list.

## XHS publish (draft only)

```bash
# 1. Probe session
opencli xiaohongshu creator-profile --site-session persistent --keep-tab true
# 2. Publish
export OPENCLI_BROWSER_COMMAND_TIMEOUT=180000
opencli xiaohongshu publish "$(cat article.md)" --title "$(head -1 article.md)" --images "/abs/path/01-cover.png,..." --window foreground --site-session persistent --draft true --format yaml
```

- Always `creator-profile` before `publish` (avoids 60s timeout)
- `--keep-tab true` prevents re-navigation
- **Prefer absolute paths** for `--images` (relative fails when workdir differs)
- Max 9 images per draft; `--draft true` accumulates drafts

## Performance notes

- 3-key parallel gen: ~30–60s per image (503 can double). Plan ~2 min/image
- Batch gen: Sweet spot is 2–3 per call. Never ≥4 (timeout risk). Never 1 (overhead)
- Feishu inserts: ~15s each, 6 sequential = 2 min min. Timeout 180s
- Each topic (article+prompts → pre-review → 3 images → Feishu → review → draft): ~8–12 min

## References

- `MEMORY.md` — exhaustive gotcha collection (platform limits, opencli bugs)
- `.opencode/memory/SUMMARY.md` — anchored session memory
- `正文提示词.md` — master document with 127 topics (24–150), each with article body + 3–6 image prompts
- `book/两汉风云.epub` — primary source for current series
