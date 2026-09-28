#!/bin/bash
# Daily auto-commit and push for xiaohongshu repo
cd /Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter || exit 1

/usr/bin/git add -A
CHANGES=$(/usr/bin/git diff --cached --stat)

if [ -n "$CHANGES" ]; then
    /usr/bin/git commit -m "Auto-commit: $(date '+%Y-%m-%d %H:%M')"
    /usr/bin/git push origin main 2>&1
fi
