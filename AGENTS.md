# AGENTS.md — 003-Twitter

Social media content farm: markdown articles + PNG cards for 小红书, reposted to X/Twitter.

## Per-content-folder convention

Each `<topic>-xhs/` folder contains:
- `article.md` — XHS publish draft (title ≤20 chars, body ≤950 chars, no markdown)
- `README.md` — full blog version with sources
- `gen_cards.py` — Python SVG generator (stdlib only, no pip deps)
- `*.svg` + `*.png` — card source and rendered output

Run `python3 gen_cards.py` — it writes `.svg` then calls Inkscape to produce `.png`.

Non-xhs directories also exist — `twitter/`, `github-skills/`, `github-trending/`, `openrouter-top10/`, `codex-plugin-deep-dive/`, `grok-civilization-collapse/`. They use different card generation approaches (Puppeteer, HTML→PNG, etc.).

## Card sizes & palettes

| Size | Use |
|------|-----|
| 1024×1024 | Cover + feature cards |
| 800×800 | Content cards |
| 1792×1024 | Banner (微博) |

Palettes:
- **Light** (preferred): cream `#FAF7F2` → `#F5F0E8` gradient, deep text `#1E293B`, brand accent colors. **No large white rects** — use cream bg directly.
- **Dark**: `#0B1027` radial bg, for single-product deep dives.

## 小红书 publish

```bash
opencli xiaohongshu publish "$(cat article.md)" \
  --title "≤20字标题" \
  --images "cover.png,card-1.png,card-2.png" \
  --window foreground \
  --site-session persistent \
  -f yaml
```
- **No `--topics`** for niche topics (causes publish failure). Put `#话题` in body text instead. Use common tags or omit entirely.
- **No `--draft`** for direct publish; add `--draft true` for draft.
- Image paths must be **relative to CWD**.
- Content is plain text — no markdown (`###`, `---`, `**` render as-is).
- Body first line = title (user preference).
- Content with newlines: `"$(cat /tmp/body.txt)"` to avoid shell splitting.
- Each `--draft true` creates a NEW draft, never overwrites old ones.

## X/Twitter publish

```bash
opencli twitter post "<text>" \
  --images "img1.png,img2.png,img3.png,img4.png" \
  --window foreground \
  --site-session persistent \
  -f yaml
```
- **Max 4 images**.
- **280 weighted characters** (CJK=2, ASCII=1, emoji=2). ~140 max Chinese chars.
- Text supports `\n` for line breaks.
- Must use `--window foreground` (background can't interact with UI).
- For threads: `opencli twitter reply <url> "<text>"`.
- Use `batch_post_twitter.py` or `post_remaining.sh` for bulk posting (2min interval).

### XHS→Twitter adaptation
- Compress ~950 chars XHS body to ≤280 weighted chars.
- Select 2-4 best cards (square/cover + content cards).
- Drop XHS colloquialisms ("姐妹们", "评论区聊聊"), use Twitter short-hand.
- 2-4 hashtags at end.

## Feishu preview

```bash
lark-cli docs +create --title "..." --markdown "$(cat README.md)" --as user
lark-cli docs +media-insert --doc <id> --file ./card.png --as user
lark-cli docs +update --doc <id> --mode overwrite --markdown "..." --as user
```
- `--file` must be a relative path.
- `+media-insert` always appends; doesn't replace existing images.
- `+update --mode overwrite` clears everything including media — re-insert all images after.
- Markdown must not contain H1 (title is the doc title).
- `+create`/`+media-insert` return `doc_id`; use `+fetch` to verify image token count.

## SVG pitfalls (critical)

- `&` in text must be `&amp;` or Inkscape renders blank.
- `height="{h}>` missing closing `"` → Inkscape silently outputs blank PNG. Use explicit pixel values, never `100%`.
- **No text glow/shadow**: `<text>` must never carry `filter="url(#glow)"` or `filter="url(#shadow)"`. Rect container shadows are fine only if explicitly asked.
- **No `#FFF` on light cards**: light palette must use deep text (`#1E293B`) everywhere. White fill only on dark backgrounds.
- Use `<tspan x="..." dy="...">` for multiline — `<text>` doesn't support `\n`.
- `letter-spacing` + CJK chars ("评测", "发布") causes squares in Inkscape. Use English for small labels.
- SVG f-string: use `}}` for literal `}`.

## Card design rules

- **先算后画**: Pre-compute text extents in Python (`text_extent(y, fontsize)`), check gap ≥ 10px between elements.
- `<text>` y is baseline, not visual center. Single-line offset ≈ `fontsize * 0.15`.
- X-axis separation preferred over Y-axis stacking for text vs icon.
- **Always generate cover in gen_cards.py** — `opencli gemini image` is unreliable, returns `no-images` frequently.
- Verify PNGs immediately: `ls -la *.png` — 1024×1024 <50KB = blank. Use `PIL.Image` + `np.unique(colors)` if unsure.

## Constraints

- Title ≤20 Unicode chars (`echo -n '...' | wc -m`).
- Body ≤950 chars (XHS hard limit 1000).
- Images ≤9 per XHS post, ≤4 per Twitter post.
- No timestamps/version numbers in body or cards.

## References

- `MEMORY.md` — exhaustive gotcha collection across 30+ sessions
- `小红书生产流水线大纲.md` — full pipeline spec with all card style variants
- `batch_post_twitter.py` — Python batch Twitter poster (37 topics)
- `待办.txt` — content backlog
