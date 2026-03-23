# 技能模板

从学习经验中提取技能时使用的模板。复制并自定义。

---

## SKILL.md 模板

```markdown
---
name: skill-name-here
description: "何时以及为何使用此技能的简明描述。包含触发条件。"
---

# 技能名称

简要介绍此技能解决的问题及其来源。

## 快速参考

| 情况 | 操作 |
|------|------|
| [触发器 1] | [操作 1] |
| [触发器 2] | [操作 2] |

## 背景

为什么这些知识很重要。它能防止什么问题。原始学习经验的上下文。

## 解决方案

### 步骤

1. 第一步，包含代码或命令
2. 第二步
3. 验证步骤

### 代码示例

\`\`\`language
// 演示解决方案的示例代码
\`\`\`

## 常见变体

- **变体 A**：描述及处理方法
- **变体 B**：描述及处理方法

## 注意事项

- 警告或常见错误 #1
- 警告或常见错误 #2

## 相关

- 相关文档链接
- 相关技能链接

## 来源

从学习条目提取。
- **Learning ID**: LRN-YYYYMMDD-XXX
- **Original Category**: correction | insight | knowledge_gap | best_practice
- **Extraction Date**: YYYY-MM-DD
```

---

## 最小模板

对于不需要所有部分的简单技能：

```markdown
---
name: skill-name-here
description: "此技能做什么以及何时使用。"
---

# 技能名称

[一句话问题陈述]

## 解决方案

[直接解决方案，包含代码/命令]

## 来源

- Learning ID: LRN-YYYYMMDD-XXX
```

---

## 带脚本的模板

对于包含可执行帮助程序的技能：

```markdown
---
name: skill-name-here
description: "此技能做什么以及何时使用。"
---

# 技能名称

[介绍]

## 快速参考

| 命令 | 用途 |
|------|------|
| `./scripts/helper.sh` | [功能描述] |
| `./scripts/validate.sh` | [功能描述] |

## 使用方法

### 自动化（推荐）

\`\`\`bash
./skills/skill-name/scripts/helper.sh [args]
\`\`\`

### 手动步骤

1. 第一步
2. 第二步

## 脚本

| 脚本 | 描述 |
|------|------|
| `scripts/helper.sh` | 主工具 |
| `scripts/validate.sh` | 验证检查器 |

## 来源

- Learning ID: LRN-YYYYMMDD-XXX
```

---

## 命名约定

- **技能名称**：小写，空格用连字符
  - 好：`docker-m1-fixes`、`api-timeout-patterns`
  - 差：`Docker_M1_Fixes`、`APITimeoutPatterns`

- **描述**：以动作动词开头，提及触发器
  - 好："处理 Apple Silicon 上的 Docker 构建失败。当构建因平台不匹配失败时使用。"
  - 差："Docker 相关内容"

- **文件**：
  - `SKILL.md` - 必需，主文档
  - `scripts/` - 可选，可执行代码
  - `references/` - 可选，详细文档
  - `assets/` - 可选，模板

---

## 提取检查清单

从学习经验创建技能前：

- [ ] 学习经验已验证（状态：resolved）
- [ ] 解决方案广泛适用（非一次性）
- [ ] 内容完整（有所有需要的上下文）
- [ ] 名称遵循约定
- [ ] 描述简洁但信息丰富
- [ ] 快速参考表可操作
- [ ] 代码示例已测试
- [ ] 来源学习 ID 已记录

创建后：

- [ ] 用 `promoted_to_skill` 状态更新原始学习经验
- [ ] 在学习经验元数据中添加 `Skill-Path: skills/skill-name`
- [ ] 在新会话中阅读技能以测试其自包含性
