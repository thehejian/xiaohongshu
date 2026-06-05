#!/usr/bin/env python3
"""Batch post remaining xhs folders to Twitter, one every 2 minutes."""
import subprocess, time, os, sys

ROOT = "/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

# (folder_name, tweet_text, images_csv)
TWEETS = [
    ("agent-framework-compare-xhs",
     "AI Agent 框架横评 🤖\n\nCoze vs Dify vs N8N vs 扣子\n哪个最适合你的场景？\n\n#AIAgent #低代码 #开源工具",
     "compare-square.png,compare-card-coze.png,compare-card-dify.png,compare-card-n8n.png"),
    ("ai-drawing-xhs",
     "AI 画图工具红黑榜 🎨\n\n哪些真的好用？实测对比\nMJ / SD / DALL-E 谁更强？\n\n#AI绘画 #AIGC #效率工具",
     "ai-drawing-square.png,ai-drawing-banner.png,ai-drawing-card-1.png,ai-drawing-card-2.png"),
    ("ai-graveyard-xhs",
     "AI 产品死亡名单 💀\n\n2025-2026 关停的 AI 产品\n从明星项目到无人问津\n\n#AI #AI产品 #科技",
     "ai-graveyard-cover.png,ai-graveyard-card-1-global.png,ai-graveyard-card-2-cn.png,ai-graveyard-card-3-death-reasons.png"),
    ("ai-interview-xhs",
     "AI 面试模拟 🤯\n\n用 LLM 做模拟面试官\n免费、随时、无限次练习\n\n#AI #面试 #求职 #效率工具",
     "ai-interview-cover.png,ai-interview-card-1-why.png,ai-interview-card-2-how.png,ai-interview-card-3-flow.png"),
    ("ai-paper-tools-xhs",
     "AI 论文工具盘点 📄\n\n5 个神器搞定科研写作\n文献分析、润色一条龙\n\n#AI工具 #科研 #论文",
     "connected_papers.png,connected_papers_v2.png,elicit.png,elicit_v2.png"),
    ("ai-ppt-tools-xhs",
     "AI 做 PPT 四巨头 🔥\n\nGamma vs iSlide vs MindShow vs Tome\n横评对比，选最适合的\n\n#AI #PPT #效率工具",
     "cover.png,card-gamma.png,card-islide.png,card-mindshow.png"),
    ("ai-rice-bowl-xhs",
     "AI 饭量大揭秘 🍚\n\n不同模型吃多少 token？\n谁最省钱？谁最能吃？\n\n#AI #大模型 #省钱",
     "ai-rice-cover.png,ai-rice-banner.png,ai-rice-card-1.png,ai-rice-card-2.png"),
    ("ai-side-hustle-xhs",
     "AI 搞钱 3 条路 💰\n\n普通人也能接的 AI 副业\n画图、写文、做 PPT\n\n#AI副业 #搞钱 #副业",
     "ai-side-hustle-square.png,ai-side-hustle-card-draw.png,ai-side-hustle-card-ppt.png,ai-side-hustle-card-write.png"),
    ("ai-six-tigers-xhs",
     "中国 AI 六小虎现状 🐯\n\n智谱 vs MiniMax vs 月之暗面\n百川 vs 零一万物 vs 阶跃星辰\n\n#AI #中国AI #大模型",
     "cover.png,01ai.png,baichuan.png,kimi.png"),
    ("ai-video-gen-xhs",
     "AI 视频生成工具对比 🎬\n\nSora / Runway / Pika / Kling\n谁生成效果最好？\n\n#AI视频 #AIGC #AI工具",
     "card_cover.png,card_cover_v2.png,card_cover_v3.png,card_1.png"),
    ("api-price-war-xhs",
     "大模型 API 价格战 ⚔️\n\nDeepSeek vs Qwen vs GPT-4o\nClaude vs Gemini 谁最便宜？\n\n#AI #大模型 #API",
     "price-war-cover.png,price-war-claude.png,price-war-deepseek.png,price-war-gemini.png"),
    ("bas-coding-eight-honors-xhs",
     "AI 编程八荣八耻 🔥\n\n治好人机协作的「默契」\n用 AI 写代码的正确姿势\n\n#AI编程 #ClaudeCode #AIAgent",
     "bas-coding-eight-honors-square.png,bas-coding-eight-honors-banner.png,honor-card-01.png,honor-card-02.png"),
    ("codex-plus-plus-xhs",
     "聊聊 Codex++ ✨\n\nCodex App 终于能删会话了\n还有这些隐藏更新\n\n#Codex #AI编程 #OpenAI",
     "codex-card-1-cover.png,codex-card-2-pain.png,codex-card-3-features.png,codex-card-4-relay.png"),
    ("coding-plan-xhs",
     "2026 AI Coding 攻略 🚀\n\n国内 AI 编程套餐对比大全\nClaude / Cursor / Codex 怎么选\n\n#AI编程 #ClaudeCode #Cursor",
     "coding-plan-square.png,coding-plan-banner.png"),
    ("deepseek-api-apply-xhs",
     "DeepSeek API 申请教程 📖\n\n从注册到调用保姆级教程\n手把手教你用上国产最强\n\n#DeepSeek #AI #API",
     "deepseek-gemini-cover.png,deepseek-square-cover.png,deepseek-card-1-signup.png,deepseek-card-2-apikey.png"),
    ("github-skills-top10-xhs",
     "GitHub Skills Top 10 ⭐\n\nStar 最多的 AI 编程 Skills\n你装了几个？\n\n#GitHub #AI编程 #开源",
     "github-skills-square.png,github-skills-banner.png,skill-card-1.png,skill-card-10.png"),
    ("hermes-feishu-xhs",
     "Hermes 对接飞书 🤯\n\n7 个场景看傻\nAI Agent 直接操控飞书全部功能\n\n#Hermes #飞书 #AIAgent",
     "hermes-feishu-cover.png,hermes-feishu-card-1.png,hermes-feishu-card-2.png,hermes-feishu-card-3.png"),
    ("hermes-xhs",
     "Hermes AI Agent 🧠\n\n浏览器自动化 Agent\n操控网页、提取数据、执行任务\n\n#Hermes #AIAgent #自动化",
     "hermes-card-1.png,hermes-card-2.png,hermes-card-3.png,hermes-card-4.png"),
    ("karpathy-skills-xhs",
     "Karpathy 吐槽 AI 写代码 😅\n\n他给的解法是这套 Skill\n专治 AI 过度工程化\n\n#AI编程 #Karpathy #技能",
     "karpathy-skills-square.png,karpathy-skills-banner.png"),
    ("lark-cli-xhs",
     "飞书 CLI 接管一切 🦸\n\nLark CLI 命令行操控飞书\n文档、表格、审批一键搞定\n\n#飞书 #CLI #效率工具",
     "lark-cli-square.png,lark-cli-banner.png,lark-cli-card-1.png,lark-cli-card-2.png"),
    ("mcp-xhs",
     "MCP 是什么？🔌\n\nAI 圈的 USB-C\n让 AI 连接一切工具\n\n#MCP #AI #开源",
     "mcp-cover.png,mcp-card-1-problem.png,mcp-card-2-what.png,mcp-card-3-how.png"),
    ("minimax-m3-xhs",
     "MiniMax M3 发布 💣\n\nBrowseComp 83.5 跑赢 Opus\n首个 frontier 国产开源旗舰\n\n#MiniMax #M3 #大模型",
     "m3-square.png,m3-banner.png,m3-card-1.png,m3-card-2.png"),
    ("nuwa-skill-xhs",
     "女娲 — 让牛人思维给你打工 🧬\n\n输入名字一键蒸馏\n把大师方法论变成你的 Skill\n\n#AI #思维模型 #技能",
     "nuwa-square.png,nuwa-banner.png,nuwa-card-1.png,nuwa-card-2.png"),
    ("ollama-mac-xhs",
     "Ollama 本地跑大模型 🔥\n\nMac 上跑开源 LLM 的正确姿势\n私密、免费、可离线\n\n#Ollama #AI #开源",
     "ollama-square.png,ollama-banner.png,ollama-card-1.png,ollama-card-2.png"),
    ("omo-xhs",
     "OmO — 一个命令拉起 AI 团队 🤯\n\n11 个专业 Agent 各司其职\n比 Cursor 强，比 Claude Code 快\n\n#OmO #AIAgent #开发者工具",
     "omo-square.png,omo-banner.png,omo-card-1.png,omo-card-2.png"),
    ("openclaw-feishu-xhs",
     "AI 助手接入飞书 📱\n\nOpenClaw + 飞书\n让 AI 直接操控企业应用\n\n#飞书 #AI #自动化",
     "openclaw-square.png,openclaw-banner.png,openclaw-card-1.png,openclaw-card-2.png"),
    ("opencut-xhs",
     "OpenCut 开源剪映平替 🔥\n\n免费、开源、功能强大\n视频剪辑的绝佳选择\n\n#OpenCut #视频剪辑 #开源",
     "opencut-cover.png,opencut-card-1.png,opencut-card-2.png,opencut-card-3.png"),
    ("pi-agent-xhs",
     "Pi Agent — 新王登基 👑\n\n编码 Agent 界的黑马\n来自 Pi.dev，重新定义 AI 编程\n\n#PiAgent #AI编程 #AIAgent",
     "pi-square.png,pi-banner.png"),
    ("qwen37-xhs",
     "阿里 Qwen3.7 杀疯了 🎯\n\n视觉榜国产第一\n价格只要 GPT 的 1/90\n\n#Qwen #阿里 #大模型",
     "qwen37-square.png,001.png,qwen37-banner.png"),
    ("suno-udio-music-xhs",
     "Suno 5 vs Udio 🎵\n\n我替你们试了\n结果意外…到底谁更强？\n\n#AI音乐 #Suno #Udio #AIGC",
     "suno-udio-cover.png,suno-udio-card-compare.png,suno-udio-card-suno.png,suno-udio-card-udio.png"),
    ("weibo-top10-xhs",
     "微博热搜 TOP 10 📊\n\n今日最热话题一览\n科技、娱乐、社会热点\n\n#微博 #热搜 #热点",
     "weibo-square.png,weibo-banner.png"),
    ("zhihu-ai-hot5-xhs",
     "知乎 AI 热榜 TOP 5 🔥\n\nAI 圈最热讨论\n知乎高赞回答精选\n\n#知乎 #AI #热榜",
     "zhihu-ai-hot5-cover.png,zhihu-ai-hot5-banner.png,zhihu-ai-hot5-card-1.png,zhihu-ai-hot5-card-2.png"),
]

def check_char_count(text):
    """Estimate Twitter weighted char count (CJK=2, ASCII=1, emoji=2)."""
    count = 0
    for c in text:
        if ord(c) > 0x2E80:  # CJK range
            count += 2
        else:
            count += 1
    return count

def post_tweet(folder, text, images_csv):
    workdir = os.path.join(ROOT, folder)
    cmd = [
        "opencli", "twitter", "post", text,
        "--images", images_csv,
        "--window", "foreground",
        "--site-session", "persistent",
        "-f", "yaml"
    ]
    print(f"\n{'='*60}")
    print(f"[{folder}] Posting...")
    print(f"Chars: {check_char_count(text)}/280")
    print(f"Images: {images_csv}")
    print(f"Text: {text[:80]}...")
    
    result = subprocess.run(cmd, cwd=workdir, capture_output=True, text=True, timeout=120)
    if result.returncode == 0:
        print(f"✅ SUCCESS")
        print(result.stdout[:200])
        return True
    else:
        print(f"❌ FAILED (exit={result.returncode})")
        print(result.stderr[:300])
        return False

# Dry-run: verify all char counts
print("=== Char Count Check ===")
all_ok = True
for folder, text, _ in TWEETS:
    cc = check_char_count(text)
    ok = "✅" if cc <= 280 else "❌ OVER"
    if cc > 280:
        all_ok = False
    print(f"  {ok} {cc:3d}/280  {folder}")

if not all_ok:
    print("\n⚠️ Some tweets exceed 280 chars! Aborting.")
    sys.exit(1)

print(f"\nTotal: {len(TWEETS)} tweets, ~{len(TWEETS)*2} min")
print("Starting in 10 seconds...")
time.sleep(10)

success_count = 0
fail_count = 0
START_INDEX = 21
for i, (folder, text, images_csv) in enumerate(TWEETS):
    if i < START_INDEX:
        continue
    if i > 0:
        print(f"\n⏳ Waiting 120s before next post...")
        time.sleep(120)
    ok = post_tweet(folder, text, images_csv)
    if ok:
        success_count += 1
    else:
        fail_count += 1

print(f"\n{'='*60}")
print(f"Done: {success_count} success, {fail_count} failed out of {len(TWEETS)}")