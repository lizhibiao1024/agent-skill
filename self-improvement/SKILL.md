---
name: self-improvement
description: "捕获学习经验、错误和纠正以实现持续改进。使用场景：(1) 命令或操作意外失败时，(2) 用户纠正 Claude（'不对...'、'实际上...'），(3) 用户请求不存在的功能，(4) 外部 API 或工具失败，(5) Claude 意识到知识过时或不正确，(6) 发现重复任务的更好方法。在执行主要任务前也应查看学习记录。"
metadata:
---

# 自我改进技能

将学习经验和错误记录到 Markdown 文件中，实现持续改进。编码助手可以后续处理这些记录以修复问题，重要的学习经验会被提升到项目记忆中。

## 快速参考

| 情况 | 操作 |
|------|------|
| 命令/操作失败 | 记录到 `.learnings/ERRORS.md` |
| 用户纠正你 | 记录到 `.learnings/LEARNINGS.md`，类别为 `correction` |
| 用户想要缺失的功能 | 记录到 `.learnings/FEATURE_REQUESTS.md` |
| API/外部工具失败 | 记录到 `.learnings/ERRORS.md`，包含集成详情 |
| 知识过时 | 记录到 `.learnings/LEARNINGS.md`，类别为 `knowledge_gap` |
| 发现更好的方法 | 记录到 `.learnings/LEARNINGS.md`，类别为 `best_practice` |
| 简化/加固重复模式 | 记录/更新 `.learnings/LEARNINGS.md`，设置 `Source: simplify-and-harden` 和稳定的 `Pattern-Key` |
| 与现有条目相似 | 用 `**See Also**` 链接，考虑提升优先级 |
| 广泛适用的学习经验 | 提升到 `CLAUDE.md`、`AGENTS.md` 和/或 `.github/copilot-instructions.md` |

## 项目设置

在项目中创建 `.learnings/` 目录：

```bash
mkdir -p .learnings
```

从 `assets/` 复制模板或创建带标题的文件。

### 将引用添加到代理文件

在 `AGENTS.md`、`CLAUDE.md` 或 `.github/copilot-instructions.md` 中添加引用，提醒自己记录学习经验。

#### 自我改进工作流

当错误或纠正发生时：
1. 记录到 `.learnings/ERRORS.md`、`LEARNINGS.md` 或 `FEATURE_REQUESTS.md`
2. 审查并将广泛适用的学习经验提升到：
   - `CLAUDE.md` - 项目事实和约定
   - `AGENTS.md` - 工作流和自动化
   - `.github/copilot-instructions.md` - Copilot 上下文

## 日志格式

### 学习条目

追加到 `.learnings/LEARNINGS.md`：

```markdown
## [LRN-YYYYMMDD-XXX] category

**Logged**: ISO-8601 时间戳
**Priority**: low | medium | high | critical
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
学习内容的单行描述

### Details
完整上下文：发生了什么，哪里错了，正确的做法是什么

### Suggested Action
具体的修复或改进建议

### Metadata
- Source: conversation | error | user_feedback
- Related Files: path/to/file.ext
- Tags: tag1, tag2
- See Also: LRN-20250110-001（如果与现有条目相关）
- Pattern-Key: simplify.dead_code | harden.input_validation（可选，用于重复模式跟踪）
- Recurrence-Count: 1（可选）
- First-Seen: 2025-01-15（可选）
- Last-Seen: 2025-01-15（可选）

---
```

### 错误条目

追加到 `.learnings/ERRORS.md`：

```markdown
## [ERR-YYYYMMDD-XXX] skill_or_command_name

**Logged**: ISO-8601 时间戳
**Priority**: high
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Summary
失败内容的简要描述

### Error
```
实际错误消息或输出
```

### Context
- 尝试的命令/操作
- 使用的输入或参数
- 相关的环境详情

### Suggested Fix
如果可识别，可能的解决方案

### Metadata
- Reproducible: yes | no | unknown
- Related Files: path/to/file.ext
- See Also: ERR-20250110-001（如果重复出现）

---
```

### 功能请求条目

追加到 `.learnings/FEATURE_REQUESTS.md`：

```markdown
## [FEAT-YYYYMMDD-XXX] capability_name

**Logged**: ISO-8601 时间戳
**Priority**: medium
**Status**: pending
**Area**: frontend | backend | infra | tests | docs | config

### Requested Capability
用户想要做什么

### User Context
为什么需要它，解决什么问题

### Complexity Estimate
simple | medium | complex

### Suggested Implementation
如何构建，可能扩展什么

### Metadata
- Frequency: first_time | recurring
- Related Features: existing_feature_name

---
```

## ID 生成

格式：`TYPE-YYYYMMDD-XXX`
- TYPE: `LRN`（学习）、`ERR`（错误）、`FEAT`（功能）
- YYYYMMDD: 当前日期
- XXX: 顺序号或随机 3 字符（如 `001`、`A7B`）

示例：`LRN-20250115-001`、`ERR-20250115-A3F`、`FEAT-20250115-002`

## 解决条目

当问题被修复时，更新条目：

1. 将 `**Status**: pending` 改为 `**Status**: resolved`
2. 在 Metadata 后添加解决块：

```markdown
### Resolution
- **Resolved**: 2025-01-16T09:00:00Z
- **Commit/PR**: abc123 或 #42
- **Notes**: 完成内容的简要描述
```

其他状态值：
- `in_progress` - 正在积极处理
- `wont_fix` - 决定不处理（在 Resolution notes 中添加原因）
- `promoted` - 提升到 CLAUDE.md、AGENTS.md 或 .github/copilot-instructions.md

## 提升到项目记忆

当学习经验广泛适用（不是一次性修复）时，将其提升到永久项目记忆。

### 何时提升

- 学习经验适用于多个文件/功能
- 任何贡献者（人类或 AI）都应该知道的知识
- 防止重复错误
- 记录项目特定约定

### 提升目标

| 目标 | 适合内容 |
|------|----------|
| `CLAUDE.md` | 项目事实、约定、所有 Claude 交互的注意事项 |
| `AGENTS.md` | 代理特定工作流、工具使用模式、自动化规则 |
| `.github/copilot-instructions.md` | GitHub Copilot 的项目上下文和约定 |

### 如何提升

1. **提炼**学习经验为简洁的规则或事实
2. **添加**到目标文件的适当部分（如需要则创建文件）
3. **更新**原始条目：
   - 将 `**Status**: pending` 改为 `**Status**: promoted`
   - 添加 `**Promoted**: CLAUDE.md`、`AGENTS.md` 或 `.github/copilot-instructions.md`

### 提升示例

**学习经验**（详细）：
> 项目使用 pnpm workspaces。尝试 `npm install` 但失败了。
> 锁文件是 `pnpm-lock.yaml`。必须使用 `pnpm install`。

**在 CLAUDE.md 中**（简洁）：
```markdown
## Build & Dependencies
- Package manager: pnpm (not npm) - use `pnpm install`
```

**学习经验**（详细）：
> 修改 API 端点时，必须重新生成 TypeScript 客户端。
> 忘记这一点会导致运行时类型不匹配。

**在 AGENTS.md 中**（可操作）：
```markdown
## After API Changes
1. Regenerate client: `pnpm run generate:api`
2. Check for type errors: `pnpm tsc --noEmit`
```

## 重复模式检测

如果记录的内容与现有条目相似：

1. **先搜索**：`grep -r "keyword" .learnings/`
2. **链接条目**：在 Metadata 中添加 `**See Also**: ERR-20250110-001`
3. **提升优先级**如果问题持续出现
4. **考虑系统性修复**：重复问题通常表明：
   - 缺少文档（→ 提升到 CLAUDE.md 或 .github/copilot-instructions.md）
   - 缺少自动化（→ 添加到 AGENTS.md）
   - 架构问题（→ 创建技术债务工单）

## 简化与加固反馈

使用此工作流从 `simplify-and-harden` 技能中获取重复模式，并将其转化为持久的提示指导。

### 获取工作流

1. 从任务摘要中读取 `simplify_and_harden.learning_loop.candidates`。
2. 对于每个候选项，使用 `pattern_key` 作为稳定的去重键。
3. 在 `.learnings/LEARNINGS.md` 中搜索具有该键的现有条目：
   - `grep -n "Pattern-Key: <pattern_key>" .learnings/LEARNINGS.md`
4. 如果找到：
   - 增加 `Recurrence-Count`
   - 更新 `Last-Seen`
   - 添加 `See Also` 链接到相关条目/任务
5. 如果未找到：
   - 创建新的 `LRN-...` 条目
   - 设置 `Source: simplify-and-harden`
   - 设置 `Pattern-Key`、`Recurrence-Count: 1` 和 `First-Seen`/`Last-Seen`

### 提升规则（系统提示反馈）

当以下条件全部满足时，将重复模式提升到代理上下文/系统提示文件：

- `Recurrence-Count >= 3`
- 至少跨 2 个不同任务出现
- 在 30 天时间窗口内发生

提升目标：
- `CLAUDE.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`

将提升的规则编写为简短的预防规则（在编码前/编码时做什么），而不是长篇的事故报告。

## 定期审查

在自然断点处审查 `.learnings/`：

### 何时审查
- 开始新的主要任务之前
- 完成功能之后
- 在有过去学习经验的领域工作时
- 活跃开发期间的每周

### 快速状态检查
```bash
# 统计待处理项
grep -h "Status\*\*: pending" .learnings/*.md | wc -l

# 列出待处理的高优先级项
grep -B5 "Priority\*\*: high" .learnings/*.md | grep "^## \["

# 查找特定领域的学习经验
grep -l "Area\*\*: backend" .learnings/*.md
```

### 审查操作
- 解决已修复的项目
- 提升适用的学习经验
- 链接相关条目
- 升级重复出现的问题

## 检测触发器

当你注意到以下情况时自动记录：

**纠正**（→ 类别为 `correction` 的学习）：
- "不对，那不是..."
- "实际上，应该是..."
- "你错了..."
- "那是过时的..."

**功能请求**（→ 功能请求）：
- "你能不能也..."
- "我希望你能..."
- "有没有办法..."
- "为什么你不能..."

**知识差距**（→ 类别为 `knowledge_gap` 的学习）：
- 用户提供你不知道的信息
- 你参考的文档已过时
- API 行为与你的理解不同

**错误**（→ 错误条目）：
- 命令返回非零退出码
- 异常或堆栈跟踪
- 意外输出或行为
- 超时或连接失败

## 优先级指南

| 优先级 | 使用场景 |
|--------|----------|
| `critical` | 阻塞核心功能、数据丢失风险、安全问题 |
| `high` | 重大影响、影响常见工作流、重复问题 |
| `medium` | 中等影响、存在变通方法 |
| `low` | 轻微不便、边缘情况、锦上添花 |

## 领域标签

用于按代码库区域筛选学习经验：

| 领域 | 范围 |
|------|------|
| `frontend` | UI、组件、客户端代码 |
| `backend` | API、服务、服务端代码 |
| `infra` | CI/CD、部署、Docker、云 |
| `tests` | 测试文件、测试工具、覆盖率 |
| `docs` | 文档、注释、README |
| `config` | 配置文件、环境、设置 |

## 最佳实践

1. **立即记录** - 问题发生后上下文最新鲜
2. **具体明确** - 未来的代理需要快速理解
3. **包含复现步骤** - 特别是对于错误
4. **链接相关文件** - 使修复更容易
5. **建议具体修复** - 不只是"调查"
6. **使用一致的类别** - 启用筛选
7. **积极提升** - 如有疑问，添加到 CLAUDE.md 或 .github/copilot-instructions.md
8. **定期审查** - 过时的学习经验会失去价值

## Gitignore 选项

**保持学习经验本地**（每个开发者）：
```gitignore
.learnings/
```

**在仓库中跟踪学习经验**（团队共享）：
不要添加到 .gitignore - 学习经验成为共享知识。

**混合方式**（跟踪模板，忽略条目）：
```gitignore
.learnings/*.md
!.learnings/.gitkeep
```

## 自动技能提取

当学习经验足够有价值可以成为可重用技能时，使用提供的帮助程序提取它。

### 技能提取标准

当满足以下任一条件时，学习经验有资格进行技能提取：

| 标准 | 描述 |
|------|------|
| **重复出现** | 有 2+ 个类似问题的 `See Also` 链接 |
| **已验证** | 状态为 `resolved` 且有可行的修复 |
| **非显而易见** | 需要实际调试/调查才能发现 |
| **广泛适用** | 非项目特定；跨代码库有用 |
| **用户标记** | 用户说"保存为技能"或类似 |

### 提取工作流

1. **识别候选项**：学习经验符合提取标准
2. **运行帮助程序**（或手动创建）：
   ```bash
   python ./skills/self-improvement/scripts/extract-skill.py skill-name --dry-run
   python ./skills/self-improvement/scripts/extract-skill.py skill-name
   ```
3. **自定义 SKILL.md**：用学习内容填充模板
4. **更新学习经验**：将状态设置为 `promoted_to_skill`，添加 `Skill-Path`
5. **验证**：在新的会话中阅读技能以确保其自包含

### 手动提取

如果你更喜欢手动创建：

1. 创建 `skills/<skill-name>/SKILL.md`
2. 使用 `assets/SKILL-TEMPLATE.md` 中的模板
3. 遵循 [Agent Skills 规范](https://agentskills.io/specification)：
   - 带有 `name` 和 `description` 的 YAML 前置内容
   - 名称必须匹配文件夹名称
   - 技能文件夹内不要有 README.md

### 提取检测触发器

注意这些信号，表明学习经验应该成为技能：

**在对话中：**
- "把这个保存为技能"
- "我一直遇到这个问题"
- "这对其他项目也有用"
- "记住这个模式"

**在学习条目中：**
- 多个 `See Also` 链接（重复问题）
- 高优先级 + 已解决状态
- 类别：`best_practice` 且具有广泛适用性
- 用户反馈赞扬解决方案

### 技能质量门

提取前，验证：

- [ ] 解决方案已测试且可行
- [ ] 描述在没有原始上下文的情况下也清晰
- [ ] 代码示例是自包含的
- [ ] 没有项目特定的硬编码值
- [ ] 遵循技能命名约定（小写、连字符）

## 多代理支持

此技能适用于不同的 AI 编码代理，具有代理特定的激活方式。

### Claude Code

**激活方式**：钩子（UserPromptSubmit、PostToolUse）
**设置**：带钩子配置的 `.claude/settings.json`
**检测**：通过钩子脚本自动

### Codex CLI

**激活方式**：钩子（与 Claude Code 相同的模式）
**设置**：带钩子配置的 `.codex/settings.json`
**检测**：通过钩子脚本自动

### GitHub Copilot

**激活方式**：手动（无钩子支持）
**设置**：添加到 `.github/copilot-instructions.md`：

```markdown
## Self-Improvement

解决非显而易见的问题后，考虑记录到 `.learnings/`：
1. 使用 self-improvement 技能的格式
2. 用 See Also 链接相关条目
3. 将高价值学习经验提升为技能

在聊天中询问："我应该把这个记录为学习经验吗？"
```

**检测**：会话结束时手动审查

### 代理无关指导

无论使用哪个代理，在以下情况下应用自我改进：

1. **发现非显而易见的事情** - 解决方案不是立即明显的
2. **纠正自己** - 最初的方法是错误的
3. **学习项目约定** - 发现未记录的模式
4. **遇到意外错误** - 特别是如果诊断很困难
5. **找到更好的方法** - 改进了你原来的解决方案

### Copilot Chat 集成

对于 Copilot 用户，在相关时将此添加到你的提示中：

> 完成此任务后，评估是否应该使用 self-improvement 技能格式将学习经验记录到 `.learnings/`。

或使用快速提示：
- "把这个记录到学习经验"
- "从这个解决方案创建一个技能"
- "检查 .learnings/ 中的相关问题"
