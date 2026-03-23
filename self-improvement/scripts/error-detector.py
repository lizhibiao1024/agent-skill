#!/usr/bin/env python3
"""
自我改进错误检测钩子
在 PostToolUse 时触发，检测命令失败
读取 CLAUDE_TOOL_OUTPUT 环境变量
"""

import os
import sys

ERROR_PATTERNS = [
    "error:",
    "Error:",
    "ERROR:",
    "failed",
    "FAILED",
    "command not found",
    "No such file",
    "Permission denied",
    "fatal:",
    "Exception",
    "Traceback",
    "npm ERR!",
    "ModuleNotFoundError",
    "SyntaxError",
    "TypeError",
    "exit code",
    "non-zero",
]

output = os.environ.get("CLAUDE_TOOL_OUTPUT", "")

if any(pattern in output for pattern in ERROR_PATTERNS):
    print("""<error-detected>
检测到命令错误。如果满足以下条件，考虑记录到 .learnings/ERRORS.md：
- 错误是意外或非显而易见的
- 需要调查才能解决
- 可能在类似上下文中重复出现
- 解决方案可能使未来会话受益

使用 self-improvement 技能格式: [ERR-YYYYMMDD-XXX]
</error-detected>""")
