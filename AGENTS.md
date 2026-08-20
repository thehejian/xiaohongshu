# AGENTS.md — 003-Twitter

Social media content farm: XHS image-card articles (西汉风云 history/literature) for @DubaIGOHGOkTHOk.

## Hard rules

- **Never execute Twitter/X post commands** — prepare text, user sends manually
- `.png`/`.jpg`/`.jpeg` gitignored — never commit images
- **🚨 审核→存草稿流程（强制）**: 每次完成场景制作后，必须先**新建飞书文档**保存内容，**仅停留在飞书文档阶段**。待用户审核确认无误并明确说"存草稿"或"OK"后，**再执行**`opencli xiaohongshu publish --draft true`存小红书草稿。**严禁**在完成飞书文档后自动存草稿，必须等用户明确指示才可执行。**场景/游记通用此流程**。
- **每次写一个**：当前场景全部完成后，停止并等待用户审核指令。不要再自动推进到下一个场景。
- **每次修改（正文/配图）后必须新建飞书文档保存**，不能更新已有文档
- **飞书审核→确认无误→才存草稿**：先 `creator-profile` 验证 session，再 `publish --draft true`
- XHS 标题≤20 CJK字（含标点），正文≤950字纯文本，tags 用 `#话题` 附在正文末尾
- **`article.md` 第1行必须是独立标题行（≤20字），此即 XHS 标题**。若第1行是正文首句，`publish --title "$(head -1 article.md)"` 会报 "Title is NNN chars — must be ≤ 20"。177 曾因此失败，写入后即成功
- **写article.md前必须先确认标题≤20字**，避免-publish时失败重做
- **飞书文档ID必须立即记录**：`lark-cli docs +create`成功后立即提取document_id并写入.feishu_uploaded，**严禁使用占位符`_doc_id_`**
- **gen_one.py必须从上一成功案例copy**：每次新建文件夹后立即执行`cp image-cards/<上一个>/gen_one.py image-cards/<当前>/gen_one.py`
- **插入图片前必须确认工作目录**：先`pwd`确认在正确文件夹，再用相对路径`./01-cover.png`
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
- **飞书文档存放文件夹**：
  - `两汉风云`（folder_token: `JUBNfa8TyldTHsd9pzNcOTbynWf`，https://qcnh2b60jsx1.feishu.cn/drive/folder/JUBNfa8TyldTHsd9pzNcOTbynWf）— 场景文档
  - `游记`（folder_token: `L8MKfqrG6lNMJkdf79ZcrB8inJg`，https://qcnh2b60jsx1.feishu.cn/drive/folder/L8MKfqrG6lNMJkdf79ZcrB8inJg）— 游记文档

## Folder layout

- `image-cards/<topic>/` — CURRENT pipeline. Only create new topics here.
- `*-xhs/` (300+ dirs) — LEGACY SVG+Inkscape pipeline, do not touch
- `_gen_runner.py` / `batch_gen.py` — LEGACY, do not use

## 世说新语 series

- Feishu drive folder「世说新语」 at root: `W729fRxeAlXePBdj1fMcWjoCnMb` (https://qcnh2b60jsx1.feishu.cn/drive/folder/W729fRxeAlXePBdj1fMcWjoCnMb)
- **All 世说新语 docs MUST be created inside this folder** (create doc with `--folder-token W729fRxeAlXePBdj1fMcWjoCnMb`, or `drive +move` afterwards)
- Local topic folders under `image-cards/shixi-xinyu/<topic>/`; Feishu title prefix = `世说N：{标题}`
- Sample content: 周处除三害（自新门，西晋）

## 游记系列

- Feishu drive folder「游记」 at root: `L8MKfqrG6lNMJkdf79ZcrB8inJg` (https://qcnh2b60jsx1.feishu.cn/drive/folder/L8MKfqrG6lNMJkdf79ZcrB8inJg)
- **All 游记 docs MUST be created inside this folder** (create doc with `--parent-token L8MKfqrG6lNMJkdf79ZcrB8inJg`, or `drive +move` afterwards)
- Local topic folders under `wohuling/` (first游记 topic); future topics: `<destination>/`
- XHS title prefix = `场景N：{标题}` or 直接标题（如「秦岭深处的阿勒泰」）
- 游记文章风格：**干货攻略型**，含导航地址、路线、用时、装备、最佳季节、轨迹链接
- 游记配图：用户自拍真实照片，无需AI生成；顺序：远景封面→核心景观→细节特写→收尾
- 游记含两步路轨迹链接：`https://www.2bulu.com/track/track_detail.htm?trackId={id}`

### 游记 workflow

1. 用户提供照片 + 目的地信息（海拔/难度/交通等）
2. 上网查证目的地资料（百度百科/抖音/8264等），确保信息准确
3. 写 `article.md` — 干货攻略风，**~650-800字**，含阴阳割昏晓等文学引用（如适用）
4. 创建飞书文档（`--parent-token L8MKfqrG6lNMJkdf79ZcrB8inJg`）+ 逐张插入图片
5. 用户审核 → 说"存草稿" → `opencli xiaohongshu publish --draft true`

### 游记 gotchas

- `lark-cli drive +move --file-token <token> --type docx --folder-token <folder>` — **type参数是 `--type` 不是 `--file-type`**（2026-08-15 实测）
- `lark-cli drive +search --doc-types folder` 可搜索文件夹
- 游记文档创建时用 `--parent-token` 而非 `--folder-token`（与场景文档一致）

## Article pipeline

### Writing style — must be engaging

Write like you're telling a friend a fascinating story. 情感真挚, avoid textbook tone. Use vivid details, concrete scenes, and narrative tension. The title should spark curiosity — a question, a contrast, or an unexpected angle. Aim for readers to think "I didn't know that" and want to share.

### Historical accuracy — must verify

Cite specific events, names, numbers, and years. **Verify any lesser-known claim** before writing — check against `book/两汉风云.epub` and structured references (史记/资治通鉴). Don't invent or approximate. If unsure, omit rather than guess.

**Primary source hierarchy for verification** (must use when writing 东汉题材):
1. `后汉书` (范晔) — first stop for Eastern Han facts
2. `资治通鉴` (司马光) — most comprehensive narrative, cross-reference with 后汉书
3. `世说新语` — for biographical anecdotes (use with caution, not all are factual)
4. `东观汉记` (佚文) — when available, earliest Eastern Han source
5. 网路检索验证关键细节（人名/地名/年份/谥号/卒年等）

**Three Kingdoms (三国) topics**: verify against `三国志` (陈寿) first, cross-reference `资治通鉴`, use `后汉书` for late-Han events/careers (董卓/曹操/刘备 up to 曹丕篡汉). 演义 (《三国演义》) fictional scenes (锦囊、火烧博望坡、走马荐诸葛等) must be distinguished from 正史 — label as 演义加工.

**Common pitfalls from recent sessions (175–185)**:
- 181/183 岑彭、来歙之死：均被**公孙述刺客**所杀（资治通鉴卷42明确），原稿误作"隗嚣刺客"。来歙死在攻蜀前线（河池/下辨），不在陇右
- 181 浮桥：是**征蜀时荆门浮桥**（岑彭派鲁奇焚桥），非渭河浮桥
- 181 岑彭"年仅五十八"：后汉书未载，**删去**
- 181 "连克夷陵、江州"：江州田戎据守未下，**改为"长驱入江关"**
- 181 "关中饥荒班师"无据：刘秀班师主因是颍川变乱+军中乏粮
- 181 "天下豪杰归我"虚构台词：改为间接叙述
- 183 "揽衣痛哭"：通鉴原文是"省书揽涕"（擦泪）
- 183 刘秀"下令严查降兵""此后再无刺杀"：查无实据，**删去**，改写史实收尾
- 178 吴汉"退休送行"：吴汉实为病逝于征蜀后，**删去**
- 178 贾复"刘秀探病落泪"：无据，**删去**
- 178 "早一百多年杯酒释兵权"：应是"早九百多年"
- 185 岑彭"麦城破秦丰"：岑彭主要战场在荆楚（江关/武阳/彭亡），**删"麦城"**
- 185 "功多者人忌"引文归属：是**刘秀说的**，非韩信原话，引文需标注"刘秀评价"
- 184 标题超20字：「同样打蜀地：一个稳得吓人，一个冒进差点赔光」→ 21字，需删"地"字改为「同样打蜀：一个稳得吓人，一个差点输光」
- 187 冯异卒年46岁（后汉书明确），非48岁；"刘秀封冯异为大将军"玩笑无据，已删

**Rule**: 写任何正文前，先用 webfetch/grep 查证核心史实点（人名、时间、地点、事件），有疑处宁可删掉不写

### New topic workflow

1. Write `article.md` — **5±2 paragraphs, 2–5 sentences each, ~800 chars total**. No 古文 quotes unless asked.
2. Write **3 English prompts** `prompts/01-cover.md` … `03-*.md` (was 6, changed from topic 150 onward)
3. Translate prompts to Chinese → user approves → proceed
4. Generate 3 images via `gen_one.py` (already in each topic folder)
5. Upload to Feishu (see below) → user reviews → XHS draft

### Article char count — critical

Target: **~800 chars** (after stripping spaces/newlines), approx 750–900 acceptable. No 古文 quotes unless asked. Do NOT waste time fine-tuning to an exact number — 800左右 is fine. No 后世影响/现代启示 sections.

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
# Create doc (passing content via stdin) — always use --parent-token:
echo "$article_text" | lark-cli docs +create --title "场景N：标题" --content - --doc-format markdown --as user --format json --parent-token JUBNfa8TyldTHsd9pzNcOTbynWf

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
- Chinese prompts also trigger. Check for exact string `content_policy_violation` (not `content_policy`)
- Policy-violated prompts: rewrite immediately, don't retry
- 181-01 `辎重`/`浮桥` in Chinese prompt triggered policy — remove military logistics words even if seemingly neutral. Batch gen: only failed image need re-gen, others already saved

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

## Style Preferences

- 两汉内容（场景1-214）：写实历史画风格，精细描绘人物表情服饰，光线戏剧性，历史厚重感
- 三国内容（场景215起）：写实历史画风格，精细描绘人物表情服饰，光线戏剧性，历史厚重感

### 历史画人物服饰规范（2026-08-17 新增）

- **所有汉代场景**人物必须穿汉代服饰（深衣/曲裾/直裾/宽袖长袍），禁止现代或错误朝代服装（西装、和服、明清服饰等）
- **年龄感准确**：如曹操假中风时约18-20岁青年，非孩童；段颎被毒死时须发花白老者
- **器物符合时代**：杯子用青铜卮/爵，不用玻璃杯；桌案用几榻，不用现代桌椅
- **背景建筑**：汉代庭院有柱廊、瓦当、夯土墙，避免唐宋及以后的建筑风格
- **Prompt中必须明确标注"汉代""深衣""宽袖长袍"** 等关键词确保AI不画错
- 图二、图三必须与图一有明显场景差异（不同地点/人物/活动），避免三张图雷同
