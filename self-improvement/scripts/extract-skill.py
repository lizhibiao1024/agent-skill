#!/usr/bin/env python3
"""
技能提取帮助程序
从学习条目创建新技能
用法: python extract-skill.py <skill-name> [--dry-run] [--output-dir <path>]
"""

import argparse
import os
import re
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="从学习条目创建新技能",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python extract-skill.py docker-m1-fixes
  python extract-skill.py api-timeout-patterns --dry-run
  python extract-skill.py pnpm-setup --output-dir ./skills/custom
        """
    )
    parser.add_argument("name", help="技能名称（小写，空格用连字符）")
    parser.add_argument("--dry-run", action="store_true", help="显示将要创建的内容而不创建文件")
    parser.add_argument("--output-dir", default="./skills", help="当前路径下的相对输出目录（默认: ./skills）")
    
    args = parser.parse_args()
    
    # 验证技能名称格式
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', args.name):
        print("[ERROR] 无效的技能名称格式。仅使用小写字母、数字和连字符。", file=sys.stderr)
        print("[ERROR] 示例: 'docker-fixes', 'api-patterns', 'pnpm-setup'", file=sys.stderr)
        sys.exit(1)
    
    # 验证输出路径
    if args.output_dir.startswith('/'):
        print("[ERROR] 输出目录必须是当前目录下的相对路径。", file=sys.stderr)
        sys.exit(1)
    
    if '..' in args.output_dir:
        print("[ERROR] 输出目录不能包含 '..' 路径段。", file=sys.stderr)
        sys.exit(1)
    
    skill_path = Path(args.output_dir) / args.name
    
    # 检查技能是否已存在
    if skill_path.exists() and not args.dry_run:
        print(f"[ERROR] 技能已存在: {skill_path}", file=sys.stderr)
        print("[ERROR] 使用不同的名称或先删除现有技能。", file=sys.stderr)
        sys.exit(1)
    
    # 生成技能标题
    skill_title = ' '.join(word.capitalize() for word in args.name.split('-'))
    
    # 技能模板
    skill_template = f'''---
name: {args.name}
description: "[TODO: 添加此技能功能和使用时机的简明描述]"
---

# {skill_title}

[TODO: 简要介绍技能的目的]

## 快速参考

| 情况 | 操作 |
|------|------|
| [触发条件] | [要做什么] |

## 使用方法

[TODO: 详细使用说明]

## 示例

[TODO: 添加具体示例]

## 来源学习

此技能从学习条目提取。
- Learning ID: [TODO: 添加原始学习 ID]
- Original File: .learnings/LEARNINGS.md
'''
    
    # 试运行输出
    if args.dry_run:
        print("[INFO] 试运行 - 将创建:")
        print(f"  {skill_path}/")
        print(f"  {skill_path}/SKILL.md")
        print()
        print("模板内容将是:")
        print("---")
        print(skill_template, end='')
        print("---")
        sys.exit(0)
    
    # 创建技能目录结构
    print(f"[INFO] 创建技能: {args.name}")
    
    skill_path.mkdir(parents=True, exist_ok=True)
    
    # 创建 SKILL.md
    skill_file = skill_path / "SKILL.md"
    skill_file.write_text(skill_template, encoding='utf-8')
    
    print(f"[INFO] 已创建: {skill_file}")
    
    # 建议后续步骤
    print()
    print("[INFO] 技能脚手架创建成功!")
    print()
    print("后续步骤:")
    print(f"  1. 编辑 {skill_file}")
    print("  2. 用学习内容填充 TODO 部分")
    print("  3. 如有详细文档，添加 references/ 目录")
    print("  4. 如有可执行代码，添加 scripts/ 目录")
    print("  5. 更新原始学习条目:")
    print("     **Status**: promoted_to_skill")
    print(f"     **Skill-Path**: skills/{args.name}")


if __name__ == "__main__":
    main()
