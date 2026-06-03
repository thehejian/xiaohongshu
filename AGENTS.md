# AGENTS.md — 003-Twitter

Social media content farm: markdown articles + PNG cards for 小红书.

## Per-content-folder convention

Each `<topic>-xhs/` folder contains:
- `article.md` — XHS publish draft (title ≤20 chars, body ≤950 chars, no markdown)
- `README.md` — full blog version with sources
- `gen_cards.py` — Python SVG generator (stdlib only, no pip deps)
- `*.svg` + `*.png` — card source and rendered output

Run `python3 gen_cards.py` — it writes `.svg` then calls Inkscape to produce `.png`.

## Card sizes & palettes

| Size | Use |
|------|-----|
| 1024×1024 | Cover + feature cards |
| 800×800 | Content cards |
| 1792×1024 | Banner (微博) |

Palettes:
- **Light** (preferred): cream `#FAF7F2` → `#F5F0E8` gradient, deep text `#1E293B`, brand accent colors. **No large white rects** — use cream bg directly.
- **Dark**: `#0B1027` radial bg, for single-product deep dives.

## Workflow & commands

```
调研 → article.md + README.md
  → python3 gen_cards.py  (SVG → Inkscape → PNG)
  → git add + commit + push
  → opencli xiaohongshu publish ... --draft true
```

### XHS publish
```bash
opencli xiaohongshu publish "$(cat article.md)" \
  --title "≤20字标题" \
  --images "cover.png,card-1.png,card-2.png" \
  --window foreground \
  --site-session persistent \
  -f yaml
```
- **No `--topics`**: niche topic names cause publish failure. Put `#话题` in body text instead.
- **No `--draft`** for direct publish; add `--draft true` for draft.
- Image paths must be **relative to CWD**.
- Content is plain text — no markdown (`###`, `---`, `**` render as-is).

### Feishu preview
```bash
lark-cli docs +create --title "..." --markdown "$(cat README.md)" --as user
lark-cli docs +media-insert --doc <id> --file ./card.png --as user
lark-cli docs +update --doc <id> --mode overwrite --markdown "..." --as user
```
- `--file` must be a relative path.
- `+media-insert` always appends; doesn't replace existing images.
- `+update --mode overwrite` clears everything including media — re-insert all images after.

## SVG pitfalls (critical)

- `&` in text must be `&amp;` or Inkscape renders blank.
- `height="{h}>` missing closing `"` → Inkscape silently outputs blank PNG. Use explicit pixel values, never `100%`.
- **No text glow/shadow**: `<text>` must never carry `filter="url(#glow)"` or `filter="url(#shadow)"`. Rect container shadows are fine.
- **No `#FFF` on light cards**: light palette must use deep text (`#1E293B`) everywhere. White fill only on dark backgrounds.
- Use `<tspan x="..." dy="...">` for multiline — `<text>` doesn't support `\n`.

## Constraints

- Title ≤20 Unicode chars (`echo -n '...' | wc -m`).
- Body ≤950 chars.
- Images ≤9 per post.
- Body first line = title (user preference).
- No timestamps/version numbers in body or cards.
- **Verify PNGs**: `ls -la *.png` — 1024×1024 <50KB = blank. Use `PIL.Image` + `np.unique(colors)` check if unsure.

## References

- `MEMORY.md` — exhaustive gotcha collection across 27+ sessions
- `待办.txt` — content backlog
