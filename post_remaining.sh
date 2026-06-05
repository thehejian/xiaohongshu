#!/bin/bash
# Post remaining xhs topics to Twitter, one every 2 minutes
ROOT="/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter"

post() {
  folder="$1"
  text="$2"
  images="$3"
  echo "=== $(date '+%H:%M:%S') Posting: $folder ==="
  (cd "$ROOT/$folder" && \
   opencli twitter post "$text" \
    --images "$images" \
    --window foreground \
    --site-session persistent \
    -f yaml) 2>&1 | head -5
  echo ""
}

# nuwa-skill-xhs
post "nuwa-skill-xhs" \
  "女娲 — 让牛人思维给你打工 🧬\n\n输入名字一键蒸馏\n把大师方法论变成你的 Skill\n\n#AI #思维模型 #技能" \
  "nuwa-square.png,nuwa-banner.png,nuwa-card-1.png,nuwa-card-2.png"

sleep 120

# ollama-mac-xhs
post "ollama-mac-xhs" \
  "Ollama 本地跑大模型 🔥\n\nMac 上跑开源 LLM 的正确姿势\n私密、免费、可离线\n\n#Ollama #AI #开源" \
  "ollama-square.png,ollama-banner.png,ollama-card-1.png,ollama-card-2.png"

sleep 120

# omo-xhs
post "omo-xhs" \
  "OmO — 一个命令拉起 AI 团队 🤯\n\n11 个专业 Agent 各司其职\n比 Cursor 强，比 Claude Code 快\n\n#OmO #AIAgent #开发者工具" \
  "omo-square.png,omo-banner.png,omo-card-1.png,omo-card-2.png"

sleep 120

# openclaw-feishu-xhs
post "openclaw-feishu-xhs" \
  "AI 助手接入飞书 📱\n\nOpenClaw + 飞书\n让 AI 直接操控企业应用\n\n#飞书 #AI #自动化" \
  "openclaw-square.png,openclaw-banner.png,openclaw-card-1.png,openclaw-card-2.png"

sleep 120

# opencut-xhs
post "opencut-xhs" \
  "OpenCut 开源剪映平替 🔥\n\n免费、开源、功能强大\n视频剪辑的绝佳选择\n\n#OpenCut #视频剪辑 #开源" \
  "opencut-cover.png,opencut-card-1.png,opencut-card-2.png,opencut-card-3.png"

sleep 120

# pi-agent-xhs
post "pi-agent-xhs" \
  "Pi Agent — 新王登基 👑\n\n编码 Agent 界的黑马\n来自 Pi.dev，重新定义 AI 编程\n\n#PiAgent #AI编程 #AIAgent" \
  "pi-square.png,pi-banner.png"

sleep 120

# qwen37-xhs
post "qwen37-xhs" \
  "阿里 Qwen3.7 杀疯了 🎯\n\n视觉榜国产第一\n价格只要 GPT 的 1/90\n\n#Qwen #阿里 #大模型" \
  "qwen37-square.png,001.png,qwen37-banner.png"

sleep 120

# suno-udio-music-xhs
post "suno-udio-music-xhs" \
  "Suno 5 vs Udio 🎵\n\n我替你们试了\n结果意外…到底谁更强？\n\n#AI音乐 #Suno #Udio #AIGC" \
  "suno-udio-cover.png,suno-udio-card-compare.png,suno-udio-card-suno.png,suno-udio-card-udio.png"

sleep 120

# weibo-top10-xhs
post "weibo-top10-xhs" \
  "微博热搜 TOP 10 📊\n\n今日最热话题一览\n科技、娱乐、社会热点\n\n#微博 #热搜 #热点" \
  "weibo-square.png,weibo-banner.png"

sleep 120

# zhihu-ai-hot5-xhs
post "zhihu-ai-hot5-xhs" \
  "知乎 AI 热榜 TOP 5 🔥\n\nAI 圈最热讨论\n知乎高赞回答精选\n\n#知乎 #AI #热榜" \
  "zhihu-ai-hot5-cover.png,zhihu-ai-hot5-banner.png,zhihu-ai-hot5-card-1.png,zhihu-ai-hot5-card-2.png"

echo "=== All done! ==="