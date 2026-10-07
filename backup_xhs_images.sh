#!/bin/bash
# 小红书图片备份脚本
# 用法: ./backup_xhs_images.sh

BACKUP_DIR="/Volumes/mac_share/007-照片/小红书图片备份"
SOURCE_DIR="/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/image-cards"

# 检查备份目录
if [ ! -d "$BACKUP_DIR" ]; then
    echo "Error: Backup directory not found: $BACKUP_DIR"
    exit 1
fi

# 检查源目录
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory not found: $SOURCE_DIR"
    exit 1
fi

count=0
# 扫描所有 topic 目录
for dir in $SOURCE_DIR/topic-*/; do
    topic=$(basename "$dir")
    mkdir -p "$BACKUP_DIR/$topic"
    
    # 复制 png 图片
    for img in "$dir"*.png; do
        if [ -f "$img" ]; then
            cp "$img" "$BACKUP_DIR/$topic/"
            count=$((count + 1))
        fi
    done
done

echo "Backup completed: $count images to $BACKUP_DIR"
echo "Time: $(date)"
