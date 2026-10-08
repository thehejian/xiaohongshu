# -*- coding: utf-8 -*-
"""XHS 单图重画 — 镜像 gen_fixed.py 逻辑（单模型 / 只轮换 key / 无参考图 / 720x960），
只重跑指定那一张，不重复生成已成功图片。

用法:
    python3 tools/xhs_regen.py image-cards/topic-453 2        # 重画第 2 张
    python3 tools/xhs_regen.py image-cards/topic-453 2 --dry-run   # 只看 prompt

行为:
    - 旧图先备份为 NN-cover.png.bak（png 本就不入库，备份可留档对比）
    - key 缺失时自动读 ~/.baoyu-skills/.env
    - 503/000/429 自动换 key 重试最多 20 次；content_policy 立即退出并提示重写

退出码: 0 成功 / 1 失败 / 2 用法错误 / 3 content_policy_violation
"""
import json
import os
import subprocess
import sys
import tempfile
import time

API_URL = 'https://apihub.agnes-ai.com/v1/images/generations'
MODEL = 'agnes-image-2.1-flash'  # 固定单一模型，风格统一，绝不换模型
SIZE = '720x960'
ENV_FILE = os.path.expanduser('~/.baoyu-skills/.env')


def load_keys():
    keys = [os.environ.get('AGNES_API_KEY', ''),
            os.environ.get('AGNES_API_KEY2', ''),
            os.environ.get('AGNES_API_KEY3', '')]
    if not any(keys) and os.path.exists(ENV_FILE):
        with open(ENV_FILE) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
        keys = [os.environ.get('AGNES_API_KEY', ''),
                os.environ.get('AGNES_API_KEY2', ''),
                os.environ.get('AGNES_API_KEY3', '')]
    return keys


def api_call(key, prompt):
    payload = {'model': MODEL, 'prompt': prompt, 'n': 1, 'size': SIZE}
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(payload, f)
        tmpfile = f.name
    try:
        r = subprocess.run([
            'curl', '-s', '--max-time', '120',
            '-H', 'Content-Type: application/json',
            '-H', 'Authorization: Bearer %s' % key,
            '-d', '@%s' % tmpfile,
            '-w', '\nHTTP_CODE:%{http_code}',
            API_URL
        ], capture_output=True, text=True)
    finally:
        os.unlink(tmpfile)
    lines = r.stdout.strip().split('\n')
    http_code = next((l.split(':')[-1] for l in lines if 'HTTP_CODE:' in l), '000')
    body = '\n'.join(lines[:-1]) if 'HTTP_CODE:' in r.stdout else r.stdout
    return http_code, body


def regen(topic_dir, num, dry_run=False):
    prompt_file = os.path.join(topic_dir, 'prompts', '%02d-cover.md' % num)
    outfile = os.path.join(topic_dir, '%02d-cover.png' % num)
    if not os.path.exists(prompt_file):
        print('找不到 prompt: %s' % prompt_file)
        return 2
    with open(prompt_file, encoding='utf-8') as f:
        prompt = f.read().strip()
    if dry_run:
        print('== %s ==\n%s' % (prompt_file, prompt))
        return 0

    keys = load_keys()
    if not any(keys):
        print('缺少 API key（%s 未找到，且环境变量为空）' % ENV_FILE)
        return 2

    backup = outfile + '.bak'
    if os.path.exists(outfile):
        import shutil
        shutil.copy2(outfile, backup)
        print('旧图已备份: %s' % backup)

    key_idx = num % 3  # 与 gen_fixed 同款错位，避开同题三图共用一 key
    for attempt in range(20):
        key = keys[key_idx]
        print('[%02d] attempt %d/%d, %s, key#%d...' % (num, attempt + 1, 20, MODEL, key_idx + 1))
        http_code, body = api_call(key, prompt)
        print('  HTTP_CODE: %s' % http_code)

        if 'content_policy_violation' in body.lower():
            print('  内容策略拒绝！不要原样重试——请改写 prompt 后再跑。响应片段:')
            print('  %s' % body[:300])
            return 3

        if http_code == '200':
            try:
                url = json.loads(body)['data'][0].get('url')
            except Exception as e:
                print('  解析失败: %s' % e)
                url = None
            if url:
                subprocess.run(['curl', '-s', url, '-o', outfile])
                sz = os.path.getsize(outfile)
                if sz < 10000:
                    print('  下载文件过小 (%d bytes)，疑似截断，重试' % sz)
                else:
                    print('  已保存 %s (%d bytes)' % (outfile, sz))
                    return 0

        if http_code in ('503', '000', '429'):
            time.sleep(3)
        key_idx = (key_idx + 1) % 3

    print('20 次重试后仍失败')
    return 1


def main(argv):
    args = [a for a in argv if a != '--dry-run']
    dry = '--dry-run' in argv
    if len(args) != 2 or not args[1].isdigit() or not 1 <= int(args[1]) <= 3:
        print('用法: xhs_regen.py <topic-dir> <1|2|3> [--dry-run]')
        return 2
    return regen(args[0], int(args[1]), dry)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
