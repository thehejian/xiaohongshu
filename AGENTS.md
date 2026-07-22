# AGENTS.md — 003-Twitter

Social media content farm: XHS image-card articles (+ Twitter/X text) for @DubaIGOHGOkTHOk.

## Hard rules

- **Never execute Twitter/X post commands** — prepare text, user sends manually
- XHS: Feishu preview + user approval, THEN save draft (never auto-publish)
- `.png`/`.jpg`/`.jpeg` gitignored — don't commit images
- Finish one topic fully (article → 6 images → feishu preview → xhs draft) before switching
- **每次修改（正文/配图）后必须新建飞书文档保存**，让用户能在飞书审核最新版本。不能只更新本地文件不建文档
- **飞书审核→确认无误→才保存到小红书草稿**：任何时候修改正文或配图后，必须先建飞书文档，等用户打字确认OK，再执行 `creator-profile` + `publish --draft true`。不得在飞书文档未经审核时提前发布草稿。

## Setup

```bash
export PATH="/opt/homebrew/bin:$PATH"
set -a; source ~/.baoyu-skills/.env; set +a      # provides AGNES_API_KEY — set -a needed for Python os.environ
```

The correct Agnes API base is `https://apihub.agnes-ai.com` (NOT `api.agnesai.com` — that domain returns SSL `tlsv1 unrecognized name`).

## Folder layout

- `*-xhs/` (375): legacy SVG+Inkscape pipeline — `article.md`, `gen_cards.py`, `prompts/`
- `image-cards/<topic>/` (89): CURRENT pipeline — `article.md`, `prompts/*.md`, `01-cover.png`…`06-*.png`

**Only create new topics under `image-cards/<topic>/`.**

## XHS article (`article.md`)

- Line 1 = title, ≤20 CJK chars. Verify:
  ```bash
  python3 -c "print(len('$(head -1 article.md)'.strip()))"
  ```
- Body: plain text (no markdown), ≤950 chars
- Tags: `#话题` at end of body. **Never** `--topics` flag
- **Never include `#渤海小吏` tag**
- Exactly 6 image cards per topic
- **情感真挚优先** — 用户重视正文的情感动人，避免纯分析和说教口吻。尤其文学类话题，正文要像在跟朋友聊天
- Source material from 史记/资治通鉴/两汉风云 — no 古文 quotes (unless user explicitly requests original text, e.g., classical essays like 张岱)

## Image pipeline (Agnes ink-wash)

Style (confirmed 2026-07-13): ink wash painting style, light rice paper texture, flowing ink strokes, subtle crimson and grey colors (no duotone), sparse composition with negative space, misty atmosphere, calligraphic brush style for titles, ancient Chinese people in scenes (never abstract metaphors), **3:4 (720×960)**. Prompt template: `Ink wash painting style, light rice paper texture, flowing ink strokes, subtle crimson and grey colors, sparse composition with negative space, misty atmosphere. <scene description>. Ancient Chinese people, period clothing. Chinese title <title> in calligraphic brush style. Subtitle <sub>. No heavy outlines. Ample whitespace.`

Workflow:
1. Write `article.md`, then 6 prompts `prompts/01-cover.md`…`06-*.md`.
2. **Chinese prompt pre-review**: Before generating, translate all 6 prompts to Chinese and present to user for approval. Only proceed to English generation after user says OK.
3. Generate cover 01 **without** ref; 02–06 **with** image 01 as `--ref` for style consistency.
4. Use Agnes `agnes-image-2.1-flash` with size `720×960` (3:4 XHS card format). Payload `{model, prompt, n:1, size:"720x960"}`; for 02+ add `"image":"data:image/png;base64,<b64 of 01-cover.png>"`. Use Python `urllib.request` with **`ssl._create_unverified_context()` directly** — `ssl.create_default_context()` fails with "Remote end closed connection without response" on `apihub.agnes-ai.com`. Copy `gen_images.py` from previous topic (it has the CERT_NONE fallback + curl fallback baked in). **SSL failures are intermittent** — even CERT_NONE can return `EOF occurred in violation of protocol`. Have curl as ultimate fallback.

**Gotcha — cover filename MUST be `01-cover.png`.** The ref step reads `01-cover.png`; a different name (e.g. `01-cover-chencang.png`) silently skips ref and breaks style consistency.

**Gotcha — Agnes content policy.** Avoid `colonial`, `slum`, `war`, `refugee`. Chinese harem/seductive scenes also blocked: `楚宫美人` / `后宫` / `harem` / reclining-in-harem. Rephrase to neutral. Always check response for `content_policy_violation` (returns empty URL).

**Gotcha — Topic scope includes literary essays too.** Beyond 两汉风云 history, user also enjoys classical Chinese essays (e.g., 张岱's 湖心亭看雪). For literary essays: include original text in article body, prioritize emotional sincerity, match image tone to poetic mood.

**Gotcha — Historical accuracy details.** User values precise details. E.g., 吕后 used female warriors (not regular guards) to arrest Han Xin, killed him in bell chamber so he wouldn't see heaven or earth (不见天地). Always verify lesser-known specifics.

**Gotcha — Last image: 英年早逝 for subjects who died young.** When a historical figure died young (e.g., Han Huidi at 22), use title like "英年早逝" instead of "惠帝七年". Emphasize wasted potential.

(Legacy scripts `_gen_runner.py` / `batch_gen.py` target `*-xhs/` at 1024×1024 and read the key from `~/.hermes/config.yaml` — NOT for the image-cards Agnes flow.)

## Feishu preview (account: qcnh2b60jsx1)

Feishu CLI now uses a **self-built app `cli_aadef45343f91cc3`** (user 何健) on tenant **qcnh2b60jsx1.feishu.cn**. The old shared app "Feishu CLI-[mac][pi]" has NO permission on this tenant.

```bash
export PATH="/opt/homebrew/bin:$PATH"    # required — lark-cli not in default PATH
lark-cli docs +create --title "<title>" --content "$(cat article.md)" --doc-format markdown --as user --format json
lark-cli docs +media-insert --doc <token> --file ./01-cover.png --as user
```

- **Always `export PATH` first** — `lark-cli` is at `/opt/homebrew/bin/lark-cli`, not in default PATH. First call will fail silently if PATH not set.
- `--file` must be **relative** from CWD (cd into topic dir first)
- Insert images **sequentially** (parallel → 429)
- Cannot change title after creation; make a new doc if title changes
- Re-login when token expires: `lark-cli auth login --no-wait --json --domain all` → `lark-cli auth qrcode --output qr.png <verification_url>` (show user) → after user authorizes, `lark-cli auth login --device-code <code>`

## XHS publish (draft only)

```bash
opencli xiaohongshu publish "$(cat article.md)" \
  --title "$(head -1 article.md)" \
  --images "01-cover.png,02-*.png,..." \
  --window foreground --site-session persistent --draft true --format yaml
```

- Max **9 images** per draft (a 12-image post failed)
- `--draft true` creates a NEW draft each run — drafts accumulate; `opencli xiaohongshu draft-clear` clears ALL drafts (use only when intentional)
- Default timeout 60s → `export OPENCLI_BROWSER_COMMAND_TIMEOUT=180000` if slow
- Extension must be connected; if "Image injection failed: No file input found on page", navigate browser to the 上传图文 tab first, then retry
- **Session probe — always run `creator-profile` first**: Before `publish`, run `opencli xiaohongshu creator-profile --site-session persistent` to verify session is alive. If it fails, re-login. Otherwise `publish` wastes 60s timing out on a dead session.
- **`--keep-tab true` after `creator-profile`**: Add `--keep-tab true` to keep browser on creator center. Then `publish` doesn't need to re-navigate to the upload page.
- **First-time publish may fail on image injection**: The extension needs the upload tab already rendered. Run a throwaway `publish --keep-tab true` first to warm up the page.
- **Prefer absolute file paths for `--images`**: Relative paths can fail when `workdir` is not the topic directory. Use full paths like `/Users/mac/.../01-cover.png` for reliability.

## Performance tips (learned the hard way)

- **Image generation timeout**: Each Agnes call takes 30-60s. 6 images = 3-6 min. Use `timeout=600000` (10 min), NOT 300s. If timeout hit mid-loop, remaining images fail silently — check `ls *.png` count before proceeding.
- **600s timeout still not enough with SSL fallback**: Python SSL fallback chain (default → CERT_NONE → curl) adds ~2-3 min per slow image. 6 images can take 12+ min total. Better to generate in smaller batches (2-3 at a time) or use larger timeout.
- **Skip Python SSL entirely — use curl directly**: `ssl.create_default_context()` and `ssl._create_unverified_context()` both fail intermittently on `apihub.agnes-ai.com` with `EOF occurred in violation of protocol`. The curl fallback via subprocess is the only reliable path. Update `gen_images.py` to try curl first, bypass Python urllib entirely.
- **Prefer per-image generation with curl**: A single `bash` with `timeout=600000` looping 6 images is fragile — one slow image kills the process. Generate each image individually with a dedicated curl call. Use a small Python wrapper but with curl subprocess (not urllib) for the API call.
- **Feishu upload timeout**: Each `+media-insert` takes 10-20s. 6 images = 60-120s. Use `timeout=180000` (3 min), NOT 120s.
- **Don't loop everything in one bash call**: If any step fails (Agnes timeout, content_policy), the whole loop dies. Generate images one-by-one or in batches of 2-3. Better: generate cover first, verify, then batch the rest.
- **Content policy kills retries**: If a prompt triggers `content_policy_violation` (returns empty URL), the loop continues but the image is missing. Always check `ls *.png | wc -l` after generation to confirm 6 files exist. If missing, reword prompt and retry individually.
- **Feishu sequential insert cannot be parallelized**: Parallel triggers 429. Each insert is ~15s. Plan for 2 min minimum for 6 images.
- **User may ask to regenerate specific images**: If user says "图X重新生成", regenerate only that image with ref, then re-create the ENTIRE Feishu doc (can't update individual images in existing doc).
- **User may ask to skip images in XHS draft**: When user requests "不要第X张图", include only requested images in `--images`.
- **Don't regenerate `gen_images.py` from scratch**: Copy from previous topic's `gen_images.py` — it already has the SSL fallback, ref logic, and prompt reading pattern baked in. Only change the `WORKDIR` behavior (uses `os.path.dirname` of script itself, so same directory pattern works automatically).
- **Always prep `export PATH` before lark-cli**: The PATH setup isn't sticky across `bash` invocations. Every Feishu call must explicitly set PATH, even if the parent shell has it.
- **Content policy triggers on implied negativity too**: `empty chamber`, `abandoned`, `absence`, `cold calculation`, `scheming`, `dark plot` — all trigger `content_policy_violation` even without explicit keywords. Reword to neutral scene description with human figures doing everyday actions.
- **Test sensitive-topic prompts individually**: When a topic involves death/palace intrigue, test each prompt one-by-one before batch generation. A single content policy kill breaks the gen_images.py loop and wastes 3-5 min per retry.
- **For death/inheritance topics, keep prompts scenic not narrative**: Don't describe the event (boys dying, queen disappearing) — describe a peaceful scene with subtle emotional cues. Let the Chinese subtitle carry the dark meaning while the English prompt stays safe.
- **Cover ref is critical but content policy can block ref too**: If ref 01-cover triggers policy on a 02+ prompt, try without ref first. If no-ref works, then the issue is prompt language, not the ref image.

## Speed & workflow optimization (learned 2026-07-17)

### 2026-07-20 lessons (topic 18 — cost 25 min, 16 min avoidable)

**1. Content policy: never describe dark/scary events in English prompt.**
`corpse`, `collapse`, `abyss`, `suffocating`, `blood`, `torture`, `starving`, `cannibalism` — all trigger `content_policy_violation`. Each violation costs 30-60s curl + full 8-retry cycle. Fix: **English prompt = neutral scene description only.** Let Chinese subtitle (on the image) carry the dark meaning. Test sensitive prompts individually before batch gen.

**2. Never batch >3 images per bash call.**
Batch of 5 exceeded 600s timeout and returned nothing — wasted 10+ min. Sweet spot is 2-3 per call. For 6 images: do 01 solo (no ref) → 02-03 → 04-05 → 06. Each batch has 300s timeout max.

**3. Add `-w "\nHTTP_CODE:%{http_code}"` to every curl call.**
Empty responses (HTTP_CODE:000) don't produce valid JSON — Python tries to parse an empty file and crashes with JSONDecodeError. Without HTTP_CODE in output, you can't distinguish "got empty string" from "timed out". Always include it so retry logic can detect empty responses.

**4. Content policy retries are pointless — just rewrite immediately.**
All 8 retries of a policy-violated prompt will fail identically. Skip retries: check response for `content_policy_violation` (or `content_policy` in the error), rewrite prompt, retry immediately. Don't waste 8×30s on a dead prompt.

**Root cause of slowness**: The pipeline has 3 sequential user-wait-for-AI cycles per topic (pre-review → image gen → Feishu review → XHS) × 6 images each taking 30-60s. Each topic takes 10-20 min wall-clock.

**Two review gates are MANDATORY, never skip**: (1) Chinese prompts pre-review before generating images, (2) Feishu doc review before XHS draft. Both require explicit user OK.

**Batch intelligently within each gate**:
- Gate 1: write article + 6 Chinese prompts → user approves ALL at once → generate all 6 without interruption. Don't do per-prompt back-and-forth.
- Gate 2: create Feishu doc with images → user reviews → on OK → XHS draft.

**Image gen — always batch 2-3 per call, NOT one-by-one, NOT all 6**:
- One-per-call is too slow (5 min overhead per image from bash setup + curl + download).
- All-6 in one bash with `timeout=600000` is fragile — one slow image kills the entire batch.
- Sweet spot: 2-3 per bash call, with `sleep 2` between each. Covers fail if one times out; retry the failed one individually.

**gen_images.py is not worth copying — use inline Python**:
- Every topic needs a slightly different prompt path or naming. Editing gen_images.py wastes time.
- Faster: write a compact inline Python script per batch (or edit the same template). It's 15 lines, not 121.
- The script's try/except is fragile: `json.loads(r.stdout)['data'][0]['url']` breaks on transient failures even when the API actually returned a valid URL. Always handle with `'data' in data` guard and retry 2x before giving up.

**XHS warm-up draft creates orphan drafts**:
- `--keep-tab true` with 1 throwaway image creates a draft that needs manual cleanup.
- Instead, navigate browser to the upload tab manually before the first publish call (or accept the warm-up cost once). Don't bother clearing orphan drafts — just let them accumulate until user asks.

**Full cycle time budget (optimized)**:
| Step | Time |
|------|------|
| Article + 6 prompts | 3-5 min |
| Chinese pre-review (wait) | user dependent |
| Generate 6 images in 2-3 batches | 3-6 min |
| Feishu doc + 6 inserts | 2-3 min |
| Feishu review (wait) | user dependent |
| creator-profile + publish | 1-2 min |
| **Total (excluding user wait)** | **10-16 min** |

**Full cycle time budget (real-world, 2026-07-18 session)**:
| Topic | Image gen time | Notes |
|-------|---------------|-------|
| 主题一臧荼 | 6 images, 4 503 retries total, ~10 min | 503 持续频繁 |
| 主题二修成君 | 6 images, 7 503 retries total, ~12 min | 05-06 各 retry 2x |
| 主题四卫霍 | 6 images, 3 503 retries total, ~8 min | 相对顺利 |
| 主题三平阳 | 6 images, 6 503 retries total, ~12 min | 01 retry 2x, 03/04/06 各 1x |
| **4 个主题总计** | **~42 min image gen alone** | **503 是绝对瓶颈** |

### 2026-07-21 lessons (topic 23 霍去病 — ~8 min, fastest session yet)

**1. Model alternation beats fixed-priority retry.**
The old script tried `2.0-flash` 5 times before falling back to `2.1-flash`. Better: alternate models (`attempt % 2`) — catches the case where one model is having 503 issues while the other works fine.

**2. Content policy false alarm from generic 400.**
Old script checked `'content_policy' in body.lower()`, which triggered on any 400 response even when the body had no policy error. Fix: check for `'content_policy_violation'` specifically.

**3. Base64 ref image in `-d` arg causes "Argument list too long".**
01-cover.png is ~1.8 MB → base64 ~2.4 MB, exceeds macOS curl CLI arg limit. Fix: write JSON payload to a temp file and use `-d @file`.

**4. User providing article + 6 prompts in one message saves 3-5 min.**
The biggest speedup came from the user composing the full package upfront, eliminating the write→review→rewrite cycle. Encourage this in Gate 1.

**5. Neutral English prompts bypass content policy entirely.**
Today's zero CP violations: all 6 prompts describe only neutral scenery (galloping cavalry, marching, landscape). No battle violence, no death, no darkness. The Chinese subtitle carries all the historical weight. This is the ideal pattern.

**6. `agnes-image-2.0-flash` returned faster than `2.1-flash`.**
Today 2.0 handled 6/6 requests with only 3 empty-response retries. When 2.0 works, it's ~30s per image. Keep 2.0 as primary, fall back to 2.1.

**7. Usage-based script is cleaner than hardcoding loop vars.**
`gen_batch.py 2 3` / `gen_batch.py 4 5` / `gen_batch.py 6` — avoids editing the file between batches. Template is generic.

**Lessons from 2026-07-18 session (4 topics in one go)**:
- **503 没有缓解迹象** — 每张图平均 retry 1-2 次，偶尔连续 3 次。这是常态，不是异常。规划时要按 1 img / 2 min 算（非 1 img / 30s）。
- **单个 bash call timeout 600s 在 503 爆发期仍然不够** — 宁可 batch 2 个（300s 够），更安全是逐个生成（600s 够）。绝对不能 batch ≥4。
- **Feishu 并行插入防碰撞的教训** — 02-cover 覆盖了 01-cover 在索引 10 的位置（两者同时看到 10 children）。原因：`sleep 2` 在两个独立 bash 间不确保真正串行。修正：**必须严格串行，前一个返回后才发下一个**（同一个 bash 里 sequential 调用，或逐个发）。
- **XHS 标题不要超过 20 字（含标点）** — 今天的 24 字标题被自动截断为「私生子天团：卫青霍去病的野性逆袭」（16 字），说明小红书客户端/API 对超长标题做静默处理。

## References

- `MEMORY.md` — exhaustive gotcha collection (legacy SVG pipeline, XHS/Twitter limits, opencli bugs)
- `.baoyu-skills/baoyu-xhs-images/EXTEND.md` — local pipeline config (currently empty)
