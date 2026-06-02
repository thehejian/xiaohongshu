# AGENTS.md — 003-Twitter

Social media content farm: markdown articles + PNG cards for Chinese platforms (小红书, 微博).

## Content folders

Each content folder (`<topic>-xhs/`) typically contains:
- `article.md` — XHS publish draft (title ≤20 chars, body ≤950 chars, image mapping)
- `README.md` — full blog version (publish-ready prose + file manifest + sources)
- `gen_cards.py` — Python SVG generator, invoked via `python3 gen_cards.py`
- `*.svg` / `*.png` — card source and output (size depends on style, see below)

Current folders (2026-06):

| Folder | Type |
|--------|------|
| `bas-coding-eight-honors-xhs/` | 文章 |
| `cc-switch-xhs/` | 文章 |
| `codex-plus-plus-xhs/` | 文章 |
| `coding-plan-xhs/` | 文章 |
| `github-skills-top10-xhs/` | 排行榜 |
| `github-skills/` | 排行榜 assets |
| `github-trending/` | 排行榜 assets |
| `hermes-xhs/` | 文章 (7 cards) |
| `karpathy-skills-xhs/` | 文章 |
| `minimax-m3-xhs/` | 文章 |
| `nuwa-skill-xhs/` | 文章 |
| `openrouter-top10/` | 排行榜 |
| `pi-agent-xhs/` | 文章 |
| `pua-xhs/` | 文章 |
| `qwen37-xhs/` | 文章 |
| `twitter/` | 推文 |
| `weibo-top10-xhs/` | 排行榜 |

## Workflow

```
write article.md + README.md
  → python3 gen_cards.py  (SVG → Inkscape → PNG)
  → lark-cli docs +create/+update + +media-insert × N  (Feishu preview)
  → git add + commit + push
  → opencli xiaohongshu publish --draft true  (XHS draft)
  → user reviews & publishes via creator.xiaohongshu.com
```

## Card sizes & styles

| Size | Use case |
|------|----------|
| 1024×1024 | XHS square cover, feature cards |
| 800×800 | Alternate card size (hermes, codex++) |
| 1792×1024 | Banner (微博/headline) |

Two palettes:
- **Light** (preferred, XHS-friendly): cream `#FAF7F2` bg, white cards, brand accent colors
- **Dark**: deep `#0B1027` radial bg, metallic accent, for single-product deep-dives

## Toolchain

| Tool | Purpose | Notes |
|------|---------|-------|
| `inkscape` | SVG → PNG rendering | Must use explicit pixel dimensions; `100%` and missing closing quotes → blank images |
| `opencli` | XHS publish | `--draft true --window foreground --site-session persistent -f yaml` |
| `lark-cli` | Feishu doc mgmt | `+create` / `+update --mode overwrite` / `+media-insert --file` |
| `python3` | SVG generation, body extraction | No external deps beyond stdlib |

## Constraints

- **Title**: ≤20 Unicode chars (`printf '...' | wc -m`)
- **Body**: ≤950 chars (XHS hard cap 1000, user prefers 950)
- **Images**: ≤9 per post, comma-separated relative paths from CWD
- **Topics**: comma-separated, no `#` prefix

## SVG pitfalls (critical)

- `height="{h}>` missing closing `"` → Inkscape outputs blank PNG silently
- `<rect width="100%">` not supported → use explicit `width="1024"`
- Verify PNGs after generation: `PIL.Image` → `np.unique(colors)` < 10 → blank

## References

- `MEMORY.md` — exhaustive gotcha collection (opencli/lark-cli/Inkscape/XHS style)
- `待办.txt` — content backlog + user feedback on card style
