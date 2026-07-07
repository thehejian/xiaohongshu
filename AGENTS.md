# AGENTS.md — 003-Twitter

Social media content farm: XHS articles + PNG cards for @DubaIGOHGOkTHOk.

## Hard rules

- **Never execute any Twitter/X post command** — prepare text, tell user to send manually
- XHS publish requires Feishu preview + user approval first
- `.png` files are gitignored; don't commit them
- Complete 1 topic fully (article → images → feishu → draft) before switching

## PATH + API keys

`opencli` + `lark-cli` in `/opt/homebrew/bin/`. Always `export PATH="/opt/homebrew/bin:$PATH"` first.

Agnes API key: `source ~/.baoyu-skills/.env` (stores `AGNES_API_KEY`).

`bun` may not be on PATH; use `npx -y bun` to run baoyu-image-gen scripts.

## XHS article (`article.md`)

- Title: line 1, ≤20 CJK chars. Verify: `python3 -c "print(len('$(head -1 article.md)'.strip()))"`
- Body: plain text (no markdown), first line = title, ≤950 chars
- Tags: `#话题` at end of body. **Never** `--topics` flag
- Source material from 史记/资治通鉴 in modern language — no 古文 quotes
- **Never include `#渤海小吏` tag**

## Image pipeline

Route: `baoyu-xhs-images` skill → `baoyu-image-gen` skill, provider `agnes`, model `agnes-image-2.1-flash`

1. Write `article.md`
2. Run `baoyu-xhs-images` — writes `analysis.md` + `outline.md` + `prompts/`
3. Generate cover (image 01) **without** `--ref` first
4. Generate images 02+ with image 01 as `--ref` for style consistency
5. Chinese text rendered in Agnes prompts directly — no Pillow overlay

Style: `screen-print` poster art (flat color blocks, halftone grain, duotone pair). Color palette depends on topic (historical: 黑金/crimson/cream; modern: varies).
Canvas: 3:4 portrait via `--ar 3:4` (baoyu-xhs-images default). 1:1 square also works for simpler layouts.

⚠️ `--image` parameter must be an **exact filename**, not a glob pattern like `$i-*.png` — the shell won't expand it before the file exists, resulting in literal `*-` in the filename.

**Two folder patterns coexist:**
- Old: `*-xhs/` (~375 dirs) — with `gen_cards.py`, prompts/, overlay scripts
- New: `image-cards/<topic>/` (~32 dirs) — with `article.md`, `prompts/*.md`, `analysis.md`, `outline.md`, images

Prefer `image-cards/<topic>/` for new topics.

When using `baoyu-xhs-images`, the prompts follow the screen-print prompt template from `references/workflows/prompt-assembly.md`:
- Core Principles (flat color blocks, symbolic shapes, negative space)
- Color Rules (2-5 flat colors max, duotone pair)
- Text Style (integrated, bold condensed, stencil-cut)
- Composition (geometric framing, no outlines)

The EXTEND.md at `.baoyu-skills/baoyu-xhs-images/EXTEND.md` pins preferred backend to `baoyu-image-gen`.

## Feishu preview

```bash
lark-cli docs +create --title "标题" --content "$(cat article.md)" --doc-format markdown --as user --format json
lark-cli docs +media-insert --doc <token> --file ./image.png --as user
```

- `--file` must be **relative** from CWD (cd into image dir first)
- Cannot change title after creation; create new doc if title needs changing
- Insert images **sequentially** (parallel triggers 429 rate limit)
- `--command overwrite` clears all media — re-insert everything. Safer to just create a new doc.

## XHS publish

```bash
opencli xiaohongshu publish "$(cat article.md)" \
  --title "$(head -1 article.md)" \
  --images "cover.png,card-1.png,..." \
  --window foreground --site-session persistent --draft true --format yaml
```

- Default timeout is 60s. If it fails: `export OPENCLI_BROWSER_COMMAND_TIMEOUT=180000` and retry (no `--timeout` flag)
- Browser freeze recovery: `pkill -f "Google Chrome"` + `opencli daemon restart`

## Notes

- `/Volumes/mac_share/` mounted at `/Volumes/mac_share/` (not `/mac_share/`)
- `MEMORY.md` — long-form gotcha collection (keep as reference for Agnes model quirks, sensitive keywords, workflow edge cases)
