# AGENTS.md — 003-Twitter

Social media content farm: XHS articles + PNG cards, reposted to X/Twitter @DubaIGOHGOkTHOk.

## ⚠️ Hard rules

- **Never execute `opencli twitter post`** — prepare text, tell user to send manually
- XHS publish requires Feishu preview first
- `.png` files are gitignored; don't commit them

## PATH

`opencli` + `lark-cli` in `/opt/homebrew/bin/`. Always `export PATH="/opt/homebrew/bin:$PATH"` first.

## Per-content-folder (`<topic>-xhs/`)

- `article.md` — title (line 1, ≤20 chars), body (≤950 chars, plain text, no markdown)
- `gen_cards.py` (Route A/SVG) or `gen_images.py` (Route B/AI + prompts/ folder)

## Route A: SVG + Inkscape

For data/news/infographics. Run `python3 gen_cards.py` → `.svg` → Inkscape auto-converts to `.png`.

- `&` → `&amp;`; use explicit px, never `width="100%"`
- `<50KB PNG` = likely blank/corrupt; 1024×1024 should be >400KB
- Avoid `letter-spacing` with CJK chars (renders as squares)

## Route B: Agnes AI + Pillow

For travel/sports/people. Use `batch_gen.py` or `_gen_runner.py` (prompts/ folder → cover first, rest with cover as ref → Pillow overlay).

- **No hex colors in prompts** (e.g. "cream background", not `#FAF7F2`)
- SSL fail on Python 3.14 → use `curl -s --max-time 300 -d @/tmp/payload.json`
- Safety blocklist: `colonial` `flag` `drape` `poor` `slum` `refugee` `conflict` `war`
- Font: `/System/Library/Fonts/STHeiti Medium.ttc`

**Switching routes**: If user calls output "not attractive", switch routes rather than iterating same approach.

## Card sizes & palettes

| Size | Use |
|------|-----|
| 1024×1024 | Cover + feature cards |
| 800×800 | Content cards (legacy) |
| 1792×1024 | Banner (微博/头条) |

Light (XHS default): cream `#FAF7F2` bg, text `#1E293B`.
Dark (Twitter/English): `#0B1027` bg, text `#F8FAFC`.

## XHS publish

```bash
opencli xiaohongshu publish "$(cat article.md)" \
  --title "$(head -1 article.md)" \
  --images "cover.png,card-1.png,card-2.png,card-3.png" \
  --window foreground --site-session persistent --draft true --format yaml
```

- **Title ≤20**: verify with `python3 -c "print(len('$(head -1 article.md)'.strip()))"` (macOS `wc -m` miscounts CJK)
- Body ≤950, plain text, first line = title
- No `--topics`; put `#话题` in body
- `--draft true` creates new draft each time (accumulates, no overwrite)
- Image paths relative to CWD; naming is flexible (`cover.png,card-*.png`)

## Feishu preview

```bash
lark-cli docs +create --title "标题" --content "$(cat article.md)" --doc-format markdown --as user --format json
lark-cli docs +media-insert --doc <token> --file ./image.png --as user
```

- `--file` must be relative from CWD
- **Update doc**: `+update --command overwrite --content "..." --doc-format markdown` (cannot change title; create new doc if needed)
- Markdown: no H1, use `##`
- `+media-insert` output is multi-line; check JSON line for `"ok": true`

## X/Twitter (reference only — agent does not execute)

```bash
opencli twitter post "<text>" --images "i1.png,i2.png,i3.png,i4.png" --window foreground --format yaml
```
- Max 4 images. ~140 chars (CJK=2, ASCII=1, emoji=2). No threads.
- 120s interval between batch posts.

## Conventions

- Complete 1 topic fully (article → images → feishu → draft) before batching
- Reference existing `*-xhs/` patterns, don't reinvent from scratch
- Test on 1 item before batch

## References

- `MEMORY.md` — 500+ line gotcha collection
- `小红书生产流水线大纲.md` — prompt templates + full pipeline
