"""图片恢复工具：从备份目录恢复图片到原位置"""
import os
import shutil
from pathlib import Path

BACKUP_ROOT = Path("/Volumes/mac_share/007-照片/小红书图片备份")
CARDS_ROOT = Path("/Users/mac/.qclaw/workspace/002-AIagent/03-opencode/003-Twitter/image-cards")

def restore_topic(topic_no: int) -> dict:
    """恢复单个 topic 的图片"""
    backup_dir = BACKUP_ROOT / f"topic-{topic_no}"
    target_dir = CARDS_ROOT / f"topic-{topic_no}"
    
    if not backup_dir.exists():
        return {"success": False, "error": f"备份目录不存在: {backup_dir}"}
    
    target_dir.mkdir(parents=True, exist_ok=True)
    
    copied = 0
    for png in backup_dir.glob("*.png"):
        dest = target_dir / png.name
        shutil.copy2(png, dest)
        copied += 1
    
    return {"success": True, "copied": copied, "topic": topic_no}

def restore_all() -> dict:
    """恢复所有 topic 的图片"""
    results = []
    for backup_dir in BACKUP_ROOT.iterdir():
        if backup_dir.is_dir() and backup_dir.name.startswith("topic-"):
            result = restore_topic(int(backup_dir.name.split("-")[1]))
            results.append(result)
    return {"total": len(results), "results": results}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        topic = int(sys.argv[1])
        print(restore_topic(topic))
    else:
        print("用法: python restore.py <topic_no>")
        print("或运行 restore_all() 恢复所有图片")
