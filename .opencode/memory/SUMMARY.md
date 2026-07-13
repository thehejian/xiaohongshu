# ANCHORED SUMMARY (updated 2026-07-13)

## Objective
- Write XHS historical articles (渤海小吏《让人拍案叫绝的中国史》based) with 6 screen-print image cards, preview on Feishu, save to XHS drafts.

## Important Details
- Screen-print style: warm cream paper, varied duotone per image, halftone texture, vintage poster feel
- 6 images per article (3:4, 720×1280), title ≤20 CJK chars, body ≤950 CJK chars
- Image gen: Agnes API (`agnes-image-2.1-flash`) via curl; first image w/o ref, rest with image 01 as `image` param (base64 in payload JSON). Helper `/tmp/gen_payload.py <prompt.md>` builds /tmp/payload.json (reads topic dir's 01-cover.png as ref)
- Prompt template: `Screen-print poster art, warm cream paper background.` + visual + `[varied duotone]. Halftone texture. Chinese title "..." in bold condensed font. Subtitle "..." Vintage poster feel. No outlines. Ample whitespace.`
- Feishu preview: sequential media-insert, new doc per iteration
- XHS publish: `opencli xiaohongshu publish` (max 9 images), `--draft true`; set `OPENCLI_BROWSER_COMMAND_TIMEOUT=180000`
- Book at `book/让人拍案叫绝的中国史(套装共2册).epub` (chapters after Hongmen = epub part 27-30: 暗度陈仓/彭城/背水一战/拉锯荥阳)
- **Feishu account CHANGED**: now uses self-built app `cli_aadef45343f91cc3` (App Secret in keychain), user 何健, tenant `qcnh2b60jsx1.feishu.cn`. Re-login via `lark-cli auth login --no-wait` → QR → `lark-cli auth login --device-code`. Old shared app "Feishu CLI-[mac][pi]" (cli_a97b1b3970fa9cb3) had no permission on this tenant.
- XHS browser: extension must be manually connected (`opencli daemon restart` + launch Chrome with UnpackedExtensions); publish fails with "Image injection failed: No file input found on page" unless 上传图文 tab selected — fix by navigating browser to creator page and clicking 上传图文 first, OR retry
- `draft-clear` clears ALL drafts (accidentally ran twice earlier: 51 then 54) — re-saved 37 unpublished after
- 20 notes already published on XHS account (from `creator-note-detail` API); these NOT in drafts
- Max 9 images per XHS draft

## Work State
### Completed (this session + prior)
- 27 pre-session articles + prior-session drafts
- liubang-xianyang, liubang-xianyang-resist, xiangyu-hongmen, xiangyu-bawang — XHS drafted
- generals-cursed-fate — PUBLISHED (creator rank 1, Jul 10)
- xiaohe-zhui-hanxin (萧何月下追韩信) — article+6img+Feishu(qcnh2b60jsx1)+XHS drafted ✅ (img04 regen'd as 古人)
- 37 unpublished topics re-saved as drafts (excl 20 published + football)

### Active
- andu-chencang (暗度陈仓为何千年唯一成功): STARTING — article + 6 prompts to write, then images

### Blocked
- (none)

## Next Move
1. Write article.md + 6 prompts for andu-chencang
2. Generate images 01-06 (01 w/o ref, 02-06 w/ ref)
3. Feishu preview (qcnh2b60jsx1) → user confirmation → XHS draft

## Relevant Files
- `book/让人拍案叫绝的中国史(套装共2册).epub`
- `image-cards/andu-chencang/` (new topic, in progress)
- `image-cards/xiaohe-zhui-hanxin/` (done)
- `image-cards/*/article.md` and `prompts/`: all topics
- `topic-list.md`
- `/tmp/gen_payload.py` (image gen helper)
