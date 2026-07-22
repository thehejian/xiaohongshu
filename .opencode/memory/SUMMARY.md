# ANCHORED SUMMARY (updated 2026-07-13)

## Objective
- Write XHS historical articles (渤海小吏 based) with 6 screen-print image cards, preview on Feishu, save to XHS drafts.

## Important Details
- Screen-print style: warm cream paper, varied duotone per image, halftone texture, vintage poster feel, ancient Chinese people (never abstract), 3:4 (720×1280)
- 6 images per article, title ≤20 CJK chars, body ≤950 CJK chars
- Image gen: Agnes API (`agnes-image-2.1-flash`) via curl; cover first w/o ref, rest with image 01 as ref. Helper: `/tmp/gen_payload.py`
- Feishu: self-built app `cli_aadef45343f91cc3` (user 何健) on tenant **qcnh2b60jsx1.feishu.cn**
- XHS publish: `opencli xiaohongshu publish` (max 9 images), `--draft true`; `OPENCLI_BROWSER_COMMAND_TIMEOUT=180000`
- Books:
  - `book/让人拍案叫绝的中国史(套装共2册).epub` — 楚汉争霸卷 FINISHED
  - `book/两汉风云.epub` — 白登之围→王莽篡汉 (STARTING)
- **每次修改后必须新建飞书文档保存**
- Agnes content_policy: avoid colonial/slum/war/refugee/美人/后宫/harem/reclining scenes; rephrase to neutral (e.g. "耽于安乐")

## Work State
### Completed — 楚汉争霸系列（14篇）
1. **萧何月下追韩信** (xiaohe-zhui-hanxin)
2. **暗度陈仓为何千年唯一成功** (andu-chencang)
3. **彭城之战：3万破56万** (pengcheng-battle)
4. **刘邦占彭城后瞬间崩盘** (liubang-pengcheng-collapse)
5. **韩信北伐：背水一战只是开始** (hanxin-beifa-backshui)
6. **安邑之战：木罂渡军** (anyi-muying)
7. **汉灭三秦之战** (han-mie-sanqin)
8. **拉锯荥阳** (xingyang-stalemate)
9. **纪信替死：史上最野逃生** (jixin-sacrifice)
10. **项羽的打地鼠困境** (xiangyu-mole)
11. **张良借箸劝退分封** (zhangliang-chopsticks)
12. **广武涧一箭：刘邦中箭骂脚趾** (guangwu-arrow)
13. **垓下十面埋伏：韩信30万围项羽10万** (gaixia-battle)
14. **乌江自刎：项羽的最后三天** (wujiang-suicide)

### Active
- 《两汉风云》系列 — 选择下一主题

### Blocked
- (none)

## Next Move
1. From 两汉风云: 白登之围/灭诸王/诸吕之变/七国之乱/马邑阴谋/漠南无王庭/打通河西走廊
2. User picks topic → article → 6 prompts → images → Feishu → XHS draft

## Relevant Files
- `book/两汉风云.epub`: 第22-35战（白登之围→王莽篡汉）
- `/tmp/gen_payload.py`: Agnes image gen helper
- `AGENTS.md`: hard rules + performance tips
- `.opencode/memory/SUMMARY.md`: this file
- `MEMORY.md`: exhaustive gotcha collection
