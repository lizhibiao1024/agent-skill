#!/usr/bin/env python3
"""
自我改进激活器钩子
在 UserPromptSubmit 时触发，提醒 Claude 捕获学习经验
保持输出最小（约 50-100 tokens）以减少开销
"""

print("""<self-improvement-reminder>
完成任务后，评估是否产生了可提取的知识：
- 通过调查发现的非显而易见解决方案？
- 意外行为的变通方法？
- 学到的项目特定模式？
- 错误需要调试才能解决？

如果是：使用 self-improvement 技能格式记录到 .learnings/。
如果是高价值（重复、广泛适用）：考虑技能提取。
</self-improvement-reminder>""")
