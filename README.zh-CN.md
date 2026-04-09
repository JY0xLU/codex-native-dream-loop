# Codex Native Dream Loop

中文 | [English](README.md)

![Codex Native Dream Loop logo](assets/hero-logo.png)

**一个面向 Codex 的自我进化记忆系统：按作用域管理记忆，按需检索，在夜间完成可审计的整理与晋升。**

`Codex Native Dream Loop` 适合这样的人：希望 Codex 记住真正有用的经验，忘掉无意义的噪音，并在长期使用中越跑越顺，而不是单纯把上下文堆得越来越长。

![Codex Native](https://img.shields.io/badge/Codex-Native-1f6feb)
![Self-Improving](https://img.shields.io/badge/Self--Improving-3fb950)
![Scoped Memory](https://img.shields.io/badge/Scoped%20Memory-8b5cf6)
![Nightly Consolidation](https://img.shields.io/badge/Nightly%20Consolidation-f59e0b)
![Subagent Review](https://img.shields.io/badge/Subagent%20Review-0ea5e9)
![Auditable](https://img.shields.io/badge/Auditable-111827)

**快速导航**

[为什么存在](#为什么存在) | [核心能力](#核心能力) | [如何工作](#如何工作) | [记忆模型](#记忆模型) | [审核与审计](#审核与审计) | [快速开始](#快速开始)

> 大多数 agent 不是不会干活，而是每次都得重新摸路。
> `Codex Native Dream Loop` 想解决的，就是“做过的经验不能白做，学到的东西不能白丢”。
> 白天采集高信号，夜间整理成真正能复用的记忆。

## 为什么存在

当一个 agent 跟着你跑了很多项目之后，最大的问题往往不是“能力不够”，而是“记忆开始变脏”。

- 有些经验只是今天临时救火，明天就失效了
- 有些规则其实已经稳定成立，却一直散落在旧对话里
- 有些错误明明出现过很多次，却还是要重新踩一遍
- 有些上下文越堆越长，但真正有用的部分越来越难被重新取回

这个仓库想做的，不是再造一个更重的控制面，而是把 Codex 已经有的原生能力串成一个更自然的闭环：

- 白天工作时，只轻量采集高信号
- 当前任务进行中，不碰长期记忆
- 夜间空闲时，统一整理、去重、归档和晋升
- 下一次任务，只取回真正相关的一小段记忆
- 每一次记忆变化，都留下足够的审计线索

它不是在“堆 memory”，而是在让 memory 真正变得有用。

## 核心能力

| 能力 | 它做什么 | 对你的好处 |
|---|---|---|
| `Scoped Memory` | 把记忆拆成 `global / repo / thread` 三层，而不是混成一团 | 不同项目、不同线程不会互相污染 |
| `Daytime Capture` | 白天把高信号观察写入 `inbox/` | 不打断主任务，也不会把长期记忆写脏 |
| `Nightly Consolidation` | 夜间去重、过期清理、改写模糊项、整理候选 | 让零散经验慢慢收敛成稳定规则 |
| `Reviewer-Assisted Promotion` | 关键晋升、拒绝、归档、冲突判断可走 reviewer 复核 | 降低单代理误判，提升记忆质量 |
| `Operational vs LongTerm` | 临时但重要的规则进 `ACTIVE.md`，稳定跨任务规律进 `LEARNINGS.md` | 记忆有层次，重要信息更容易被重新用上 |
| `Audit Trail` | 保留 source id、决定理由、拒绝原因和回滚线索 | 以后能解释“为什么会有这条规则” |
| `Minimal Retrieval` | 新任务开始时只读最相关的片段，而不是整份重读 | 更省 token，也更少上下文噪音 |
| `Codex-Native Workflow` | 直接利用 `AGENTS.md`、skills、automations、worktrees、sandbox、subagents | 顺着 Codex 原生能力去构建，而不是绕开它 |

## 如何工作

整个闭环故意做得很简单：

1. 白天，`capture-memory` 只负责记录高信号观察。
2. 这些观察先进入 `inbox/`，不直接污染长期记忆。
3. 夜间，`dream-consolidate` 读取最近的信号并生成候选。
4. 重复项会被合并，过期项会被清理，模糊项会被重写。
5. 当前阶段仍然重要的临时规则进入 `ACTIVE.md`。
6. 足够稳定、跨任务可复用的规律进入 `LEARNINGS.md`。
7. 关键变更都会留下审计痕迹，方便复查和回滚。

你提供的 logo 就是在表达这个结构：

- 左半边是 **白天采集**
- 右半边是 **夜间整理**
- 中间是把原始信号转成可复用记忆的 Dream Loop 核心

## 记忆模型

Codex Native Dream Loop 故意把记忆模型压得很短，不走过重设计。

### 1. Policy

`AGENTS.md` 仍然是面向人的顶层规则入口。

- 永久操作规则放这里
- 安全边界放这里
- 像 Policy 的改动只能提案，不能自动落盘
- 这一层绝不自动改写

### 2. Memory Scopes

整个系统只保留三层 scope：

- `global`：跨项目稳定规律
- `repo`：某个仓库自己的习惯和规则
- `thread`：短命的当前工作上下文

可读投影保持简单：

- `ACTIVE.md` 是 operational projection
- `LEARNINGS.md` 是 long-term projection

### 3. Improvement Loop

主循环由两个 skill 完成：

- `capture-memory`
  - 只负责采集高信号观察
  - 保持轻量
  - 不负责 consolidation 和 promotion
- `dream-consolidate`
  - 负责夜间整理
  - 生成候选
  - 做 reviewer-assisted 的 promotion / rejection 决策
  - 更新 memory projection 和 audit 记录

## 审核与审计

这个仓库明确偏向 reviewer-assisted 的记忆维护方式。

- `capture-memory` 保持轻量单 agent
- `dream-consolidate` 在 promotion、rejection、archive、conflict review 上优先走 reviewer 复核
- 低风险清理仍然可以走单 agent fast path
- 如果主代理和 reviewer 有分歧，最终报告必须写出分歧和裁决结果

审计不是附加功能，而是整套自我进化机制可信的原因。

每次有意义的记忆变化，都应该保留：

- source event 或 source id
- reviewer verdict
- final decision
- rollback clue

这样长期记忆才不是静默漂移出来的，而是可以追问、可以解释、也可以回退的。

## 这个仓库包含什么

这个仓库提供了运行 Dream Loop 所需的最小组件：

- `skills/capture-memory/`
  - 白天采集 skill
  - 负责把结构化观察写入 `inbox/`
- `skills/dream-consolidate/`
  - 夜间整理 skill
  - 负责去重、过期处理、晋升、归档和报告
- `templates/`
  - `AGENTS.md` 起始片段
  - memory 文件与 projection 模板
- `examples/`
  - 最小示例
  - 报告样例和参考结构
- `automations/`
  - 推荐的夜间自动整理 prompt 和调度方式
- `references/`
  - promotion、scope、audit、consolidation 的说明文档

## 核心规则

- 白天采集只写入 `.codex/memory/inbox/`
- 夜间整理才允许更新 `.codex/memory/` 下的记忆文件
- `AGENTS.md` 绝不能自动修改
- 每一次 promotion、merge、archive、rejection、rollback 都必须可审计
- 临时指导优先留在 `ACTIVE.md`，不要轻易直接写进 `LEARNINGS.md`
- `capture-memory` 必须保持轻量；subagent-heavy 的工作留给 Dream Loop review 和 audit

## 仓库结构

```text
repo/
├── README.md
├── README.zh-CN.md
├── assets/
│   └── hero-logo.png
├── references/
├── templates/
├── examples/
├── automations/
└── skills/
    ├── capture-memory/
    └── dream-consolidate/
```

## 快速开始

1. 把 `skills/capture-memory/` 和 `skills/dream-consolidate/` 复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`。
2. 把 `templates/global/` 下的模板复制到你的 Codex home 作为起始结构。
3. 把 `AGENTS.md` 片段接入你的全局入口或项目入口。
4. 在日常工作中，用 `capture-memory` 记录值得留下的高信号观察。
5. 用 nightly automation 运行 `dream-consolidate`。
6. 对重要的 promotion 或 rejection 决策，优先走 reviewer-assisted 的复核。
7. 在信任新晋升的规则之前，先查看生成的审计报告。

## 实际效果应该是什么样

这套闭环的目标不是“让 memory 变多”，而是让它变得更准。

- 一个模式第一次出现时，它只是 `Observed`
- 重复出现之后，它才会进入候选
- 当它在当前阶段真的有用时，它会进入 `ACTIVE.md`
- 当它跨任务稳定成立时，它才会进入 `LEARNINGS.md`
- 当它不再有效时，它会被归档，并留下解释线索

只有当记忆保持短、分层、可质疑、可回滚时，自我进化才不会反过来拖累系统本身。
