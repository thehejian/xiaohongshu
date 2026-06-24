# AGENTS.md — 003-Twitter

Social media content farm: markdown articles + PNG cards for 小红书, reposted to X/Twitter @DubaIGOHGOkTHOk.

## ⚠️ 硬规则

- **Agent 不得执行任何 Twitter 发布命令**（`opencli twitter post`、browser 手动操作）。只准备文案，通知用户手动发送。
- 小红书发布前必须先飞书预览审核。

## Per-content-folder

`<topic>-xhs/` contains:
- `article.md` — title (first line, ≤20 chars), body (≤950 chars, plain text, no markdown)
- `README.md`, `gen_cards.py` (Route A/SVG), or `image-cards/<slug>/` (Route B/AI)

## Two image generation routes

| Route | When | How |
|-------|------|-----|
| **A: SVG + Inkscape** | Data/rankings/infographics | `python3 gen_cards.py` → .svg → Inkscape auto-converts to .png |
| **B: AI photorealistic + Pillow** | Travel/sports/people (default) | Agnes API (curl) + Pillow overlays Chinese text |

**Decision**: If user calls output "not attractive", switch routes. Don't grind the same route.

### Route B critical gotchas
- **No hex color codes in prompts** (`#FAF7F2` → AI renders as text). Use natural language ("cream background").
- **No `Chinese text` in prompt** → AI renders garbled characters. Generate pure image, overlay text with Pillow.
- **SSL failure** (Python 3.14): use `curl -s --max-time 300 -d @/tmp/payload.json` instead of `requests`.
- **Specify ethnicity explicitly** in prompts — AI defaults to East Asian faces.
- **Content safety**: avoid `colonial`, `flag`, `drape`, `poor`, `slum`, `refugee`, `conflict`, `war` (non-sports context) → 400 errors.
- **Cover first** (no ref image), then cards 2+ with cover as `--image` ref for style consistency.
- **Pillow font**: `/System/Library/Fonts/STHeiti Medium.ttc`. Center text via `textbbox`.

### Route A (SVG) gotchas
- `&` → `&amp;`, `height="{h}>` missing `"` → blank PNG. No `rect width="100%"` (use explicit px).
- `letter-spacing` + CJK chars → squares. `<50KB .png` = blank; 1024×1024 >400KB normal.

## Card sizes & palettes

| Size | Use |
|------|-----|
| 1024×1024 | Cover + feature cards |
| 800×800 | Content cards (legacy) |
| 1792×1024 | Banner (微博/头条) |

Light (XHS default): cream `#FAF7F2` bg, text `#1E293B`. **No `#FFF`.**
Dark (Twitter/English): `#0B1027` bg, text `#F8FAFC`.

## 小红书 publish

```bash
opencli xiaohongshu publish "$(cat article.md)" \
  --title "≤20字标题" \
  --images "cover.png,card-1.png" \
  --window foreground --site-session persistent --draft true -f yaml
```
- **No `--topics`** (niche topic attach fails) → `#话题` in body only
- `--draft true` = new draft each time (never overwrites; accumulates)
- Images paths **relative to CWD**. Body plain text only, first line = title.

## X/Twitter publish (reference only — agent does not execute)

```bash
opencli twitter post "<text>" --images "i1.png,i2.png,i3.png,i4.png" --window foreground -f yaml
```
- Max 4 images. ~140 Chinese chars (CJK=2, ASCII=1, emoji=2). No threads (user preference).
- 120s interval between batch posts. X.com often blocked by proxy — user's network issue.

## 今日头条 publish

See `今日头条生产流水线大纲.md`. Browser-based via `opencli browser`. Key diffs from XHS: ≤30 char title, ≤2500 char body, form selectors differ (`div[contenteditable=true]`).

## Feishu preview

```bash
lark-cli docs +create --title "..." --markdown "$(cat README.md)" --as user
lark-cli docs +media-insert --doc <id> --file ./card.png --as user
```
- `+update --mode overwrite` clears everything (incl. media) — re-insert all images after.
- Markdown must not contain H1. `--file` must be relative.

## `opencli upload` markerAttr bug

`const markerAttr` in `base-page.js:381,630` → duplicate declaration. Fix: change both `const`→`var`, restart daemon.

## Constraints

- Title ≤20 Unicode chars (`echo -n '...' | wc -m`). Body ≤950 (XHS), ≤2500 (头条).
- Images ≤9 per XHS, ≤4 per Twitter. No timestamps/version numbers in body or cards.

## References

- `MEMORY.md` — 400+ line gotcha collection across 30+ sessions
- `小红书生产流水线大纲.md` — full XHS pipeline with prompt templates
- `今日头条生产流水线大纲.md` — 头条 selector-by-selector workflow
- `twitter生产流水线大纲.md` — Twitter adaptor quirks & selector refs
