# AGENTS.md — 003-Twitter

Social media content farm: XHS image-card articles (+ Twitter/X text) for @DubaIGOHGOkTHOk.

## Hard rules

- **Never execute Twitter/X post commands** — prepare text, user sends manually
- XHS: Feishu preview + user approval, THEN save draft (never auto-publish)
- `.png`/`.jpg`/`.jpeg` gitignored — don't commit images
- Finish one topic fully (article → 6 images → feishu preview → xhs draft) before switching

## Setup

```bash
export PATH="/opt/homebrew/bin:$PATH"
source ~/.baoyu-skills/.env      # provides AGNES_API_KEY (image gen needs this)
```

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
- Source material from 史记/资治通鉴 — no 古文 quotes
- **Never include `#渤海小吏` tag**
- Exactly 6 image cards per topic

## Image pipeline (Agnes screen-print)

Style (confirmed 2026-07-07): warm cream paper background, navy/crimson/gold duotone, halftone texture, vintage poster feel, bold condensed Chinese font, ancient Chinese people in scenes (never abstract metaphors), 3:4 (720×1280). No hex colors in prompts (write "cream background"); specify East-Asian people explicitly.

Workflow:
1. Write `article.md`, then 6 prompts `prompts/01-cover.md`…`06-*.md` (Chinese text directly — no Pillow overlay).
2. Generate cover 01 **without** ref; 02–06 **with** image 01 as `--ref` for style consistency.
3. Use Agnes `agnes-image-2.1-flash` via curl (Python 3.14 SSL fails → curl only). Payload `{model, prompt, n:1, size:"720x1280"}`; for 02+ add `"image":"data:image/png;base64,<b64 of 01-cover.png>"`. Write JSON to `/tmp/payload.json`, then `curl -d @/tmp/payload.json`.

**Gotcha — cover filename MUST be `01-cover.png`.** The ref step reads `01-cover.png`; a different name (e.g. `01-cover-chencang.png`) silently skips ref and breaks style consistency.

**Gotcha — Agnes `content_policy_violation`.** Avoid `colonial`, `slum`, `war`, `refugee`. Chinese harem/seductive scenes are also blocked: `楚宫美人` / `后宫` / `harem` / reclining-in-harem prompts get rejected (returns empty URL). Rephrase to neutral (e.g. "耽于安乐，忘了身后是战场"). Always check the raw response for `content_policy_violation` and reword when URL is empty.

(Legacy scripts `_gen_runner.py` / `batch_gen.py` target `*-xhs/` at 1024×1024 and read the key from `~/.hermes/config.yaml` — NOT for the image-cards Agnes flow.)

## Feishu preview (account: qcnh2b60jsx1)

Feishu CLI now uses a **self-built app `cli_aadef45343f91cc3`** (user 何健) on tenant **qcnh2b60jsx1.feishu.cn**. The old shared app "Feishu CLI-[mac][pi]" has NO permission on this tenant.

```bash
lark-cli docs +create --title "<title>" --content "$(cat article.md)" --doc-format markdown --as user --format json
lark-cli docs +media-insert --doc <token> --file ./01-cover.png --as user
```

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

## References

- `MEMORY.md` — exhaustive gotcha collection (legacy SVG pipeline, XHS/Twitter limits, opencli bugs)
- `.baoyu-skills/baoyu-xhs-images/EXTEND.md` — local pipeline config (currently empty)
