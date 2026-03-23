# 学习经验

在开发过程中捕获的纠正、见解和知识差距。

**类别**：correction | insight | knowledge_gap | best_practice
**领域**：frontend | backend | infra | tests | docs | config
**状态**：pending | in_progress | resolved | wont_fix | promoted | promoted_to_skill

## 状态定义

| 状态 | 含义 |
|------|------|
| `pending` | 尚未处理 |
| `in_progress` | 正在积极处理 |
| `resolved` | 问题已修复或知识已整合 |
| `wont_fix` | 决定不处理（原因在 Resolution 中） |
| `promoted` | 提升到 CLAUDE.md、AGENTS.md 或 copilot-instructions.md |
| `promoted_to_skill` | 提取为可重用技能 |

## 技能提取字段

当学习经验被提升为技能时，添加这些字段：

```markdown
**Status**: promoted_to_skill
**Skill-Path**: skills/skill-name
```

示例：
```markdown
## [LRN-20250115-001] best_practice

**Logged**: 2025-01-15T10:00:00Z
**Priority**: high
**Status**: promoted_to_skill
**Skill-Path**: skills/docker-m1-fixes
**Area**: infra

### Summary
Docker 构建在 Apple Silicon 上因平台不匹配而失败
...
```

---
