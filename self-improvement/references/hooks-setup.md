# 钩子配置指南

为 AI 编码代理配置自动自我改进触发器。

## 概述

钩子通过在关键时刻注入提醒来实现主动学习捕获：
- **UserPromptSubmit**：每次提示后提醒评估学习经验
- **PostToolUse (Bash)**：命令失败时检测错误

## Claude Code 设置

### 方案 1：项目级配置

在项目根目录创建 `.claude/settings.json`：

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python ./skills/self-improvement/scripts/activator.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python ./skills/self-improvement/scripts/error-detector.py"
          }
        ]
      }
    ]
  }
}
```

### 方案 2：用户级配置

添加到 `~/.claude/settings.json` 实现全局激活：

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python ~/.claude/skills/self-improvement/scripts/activator.py"
          }
        ]
      }
    ]
  }
}
```

### 最小设置（仅激活器）

如需降低开销，仅使用 UserPromptSubmit 钩子：

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python ./skills/self-improvement/scripts/activator.py"
          }
        ]
      }
    ]
  }
}
```

## Codex CLI 设置

Codex 使用与 Claude Code 相同的钩子系统。创建 `.codex/settings.json`：

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python ./skills/self-improvement/scripts/activator.py"
          }
        ]
      }
    ]
  }
}
```

## GitHub Copilot 设置

Copilot 不直接支持钩子。改为在 `.github/copilot-instructions.md` 中添加指导：

```markdown
## Self-Improvement

完成涉及以下内容的任务后：
- 调试非显而易见的问题
- 发现变通方法
- 学习项目特定模式
- 解决意外错误

考虑使用 self-improvement 技能格式将学习经验记录到 `.learnings/`。

对于会使其他会话受益的高价值学习经验，考虑技能提取。
```

## 验证

### 测试激活器钩子

1. 启用钩子配置
2. 启动新的 Claude Code 会话
3. 发送任意提示
4. 验证在上下文中看到 `<self-improvement-reminder>`

### 测试错误检测钩子

1. 启用 PostToolUse 钩子用于 Bash
2. 运行一个失败的命令：`ls /nonexistent/path`
3. 验证看到 `<error-detected>` 提醒

### 试运行提取脚本

```bash
python ./skills/self-improvement/scripts/extract-skill.py test-skill --dry-run
```

预期输出显示将要创建的技能脚手架。

## 故障排除

### 钩子未触发

1. **验证路径**：使用绝对路径或相对于项目根目录的路径
2. **检查设置位置**：项目级 vs 用户级设置
3. **重启会话**：钩子在会话开始时加载
4. **确认 Python 已安装**：运行 `python --version` 检查

### 脚本未找到

如果使用相对路径，确保在正确的目录中或使用绝对路径：

```json
{
  "command": "python /absolute/path/to/skills/self-improvement/scripts/activator.py"
}
```

### 开销过大

如果激活器感觉侵入性太强：

1. **使用最小设置**：仅 UserPromptSubmit，跳过 PostToolUse
2. **添加匹配器过滤器**：仅对特定提示触发：

```json
{
  "matcher": "fix|debug|error|issue",
  "hooks": [...]
}
```

## 钩子输出预算

激活器设计为轻量级：
- **目标**：每次激活约 50-100 tokens
- **内容**：结构化提醒，非冗长说明
- **格式**：XML 标签便于解析

如需进一步减少开销，可以编辑 `activator.py` 输出更少文本。

## 安全考虑

- 钩子脚本以与 Claude Code 相同的权限运行
- 脚本仅输出文本；不修改文件或运行命令
- 错误检测器读取 `CLAUDE_TOOL_OUTPUT` 环境变量
- 所有脚本都是可选的（必须显式配置）

## 禁用钩子

要在不删除配置的情况下临时禁用：

1. **在设置中注释掉**：
```json
{
  "hooks": {
    // "UserPromptSubmit": [...]
  }
}
```

2. **或删除设置文件**：没有配置钩子不会运行

## 跨平台兼容性

Python 脚本（`.py`）可在以下平台运行：
- Windows（需安装 Python）
- macOS（系统自带或通过 Homebrew 安装）
- Linux（系统自带或通过包管理器安装）

### 前提条件

确保系统已安装 Python 3：

```bash
# 检查 Python 版本
python --version
# 或
python3 --version
```

如果未安装，请从 [python.org](https://www.python.org/downloads/) 下载安装。
