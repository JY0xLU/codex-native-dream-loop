# Codex Native Dream Loop

中文 | [English](README.md)

![Codex Native Dream Loop logo](assets/hero-logo.png)

**一个面向 Codex 的自我进化系统：按作用域管理记忆，用受控方式演化能力，并在夜间完成可审计的整理与晋升。**

`Codex Native Dream Loop` 适合这样的人：希望 Codex 记住真正有用的经验，在合适的时候发现合适的能力，并在长期使用中越跑越顺，而不是一边堆上下文，一边临场乱找工具。

![Codex Native](https://img.shields.io/badge/Codex-Native-1f6feb)
![Self-Improving](https://img.shields.io/badge/Self--Improving-3fb950)
![Scoped Memory](https://img.shields.io/badge/Scoped%20Memory-8b5cf6)
![Capability Evolution](https://img.shields.io/badge/Capability%20Evolution-2563eb)
![Nightly Consolidation](https://img.shields.io/badge/Nightly%20Consolidation-f59e0b)
![Subagent Review](https://img.shields.io/badge/Subagent%20Review-0ea5e9)
![Auditable](https://img.shields.io/badge/Auditable-111827)

**快速导航**

[为什么存在](#为什么存在) | [核心能力](#核心能力) | [如何工作](#如何工作) | [记忆模型](#记忆模型) | [能力进化](#能力进化) | [审核与审计](#审核与审计) | [快速开始](#快速开始)

> 大多数 agent 不是不会干活，而是要么只会堆上下文，要么每次都重新摸索工具链。
> `Codex Native Dream Loop` 解决的是这两个前后半场：白天按规则发现能力、记录信号，夜间做整理和晋升，只把真正还重要的东西带回下一次任务。

## 为什么存在

当一个 agent 跟着你跑了很多项目之后，最大的问题往往不是“能力不够”，而是“操作开始漂移”。

- 有些经验只是今天临时救火，明天就失效了
- 有些规则其实已经稳定成立，却一直散落在旧对话里
- 有些错误明明出现过很多次，却还是要重新踩一遍
- 有些新工具明明有用，却总是装得太晚、装得太乱，或者每次都换一套说法
- 有些上下文越堆越长，但真正有用的部分越来越难被重新取回

这个仓库想做的，不是再造一个更重的控制面，而是把 Codex 已经有的原生能力串成一个更自然的闭环：

- 只取回当前任务真正需要的那一小段记忆
- 先判断任务意图，再决定怎么找能力
- 按固定顺序发现插件、skills 和外部方案
- 在采用新能力前先过验证门
- 白天只轻量记录高信号结果
- 夜间统一整理、去重、晋升和归档
- 让每一次重要判断都留下可审计线索

它不是在“堆 memory”，而是在让 memory 和 capability 都真正变得有用。

## 核心能力

| 能力 | 它做什么 | 对你的好处 |
|---|---|---|
| `Scoped Memory` | 把记忆拆成 `global / repo / thread` 三层，而不是混成一团 | 不同项目、不同线程不会互相污染 |
| `Daytime Capture` | 白天把高信号观察写入 `inbox/` | 不打断主任务，也不会把长期记忆写脏 |
| `Capability Evolution` | 先判断任务意图，再按固定顺序发现能力：已启用官方插件、可安装官方插件、本地技能、可信 GitHub 项目 | 不会一上来就乱搜工具，也不会错过更合适的原生能力 |
| `Validation Gate` | 对新能力检查相关性、维护活跃度、来源可信度、接入成本与收益 | 降低坏安装、乱接入、一次性试验直接固化的问题 |
| `Nightly Consolidation` | 夜间去重、过期清理、改写模糊项、整理候选 | 让零散经验慢慢收敛成稳定规则 |
| `Reviewer-Assisted Promotion` | 关键晋升、拒绝、归档、冲突判断可走 reviewer 或 subagent 复核 | 降低单路径误判，提升长期记忆质量 |
| `Operational vs LongTerm` | 临时但重要的规则进 `ACTIVE.md`，稳定跨任务规律进 `LEARNINGS.md` | 记忆有层次，重要信息更容易被重新用上 |
| `Audit Trail` | 保留 source id、决定理由、拒绝原因和回滚线索 | 以后能解释“为什么会有这条规则” |
| `Codex-Native Workflow` | 直接利用 `AGENTS.md`、skills、automations、worktrees、sandbox、plugins、subagents | 顺着 Codex 原生能力去构建，而不是绕开它 |

## 如何工作

整个闭环故意拆成几段明确职责：

1. 先从 `ACTIVE.md` 和 `LEARNINGS.md` 中只取回最小相关记忆片段。
2. 把任务归类成 `repair`、`optimize`、`innovate`、`explore` 之一。
3. 按固定顺序发现能力：
   已启用官方插件 -> 可安装官方插件 -> 本地内置技能 -> 可信 GitHub 技能或项目。
4. 对任何新采用的能力先做验证，再决定是否接入。
5. 用选定能力完成当前任务。
6. 用 `capture-memory` 把高信号结果、阻塞点或工作流收益写入 `inbox/`。
7. 夜间再用 `dream-consolidate` 去重、审核、晋升、拒绝或归档。

完整工作循环是：

`recall -> classify -> discover -> validate -> adopt -> capture -> consolidate`

## 记忆模型

Codex Native Dream Loop 故意把记忆模型压得很短，不走过重设计。

### 1. Policy

`AGENTS.md` 仍然是面向人的顶层规则入口。

- 永久操作规则放这里
- 安全边界放这里
- 像 Policy 的改动必须走人工 review
- 这一层不应该被当成随手记录板

### 2. Memory Scopes

整个系统只保留三层 scope：

- `global`：跨项目稳定规律
- `repo`：某个仓库自己的习惯和规则
- `thread`：短命的当前工作上下文

可读投影保持简单：

- `ACTIVE.md` 是 operational projection
- `LEARNINGS.md` 是 long-term projection

### 3. Improvement Loop

主循环现在由三个 skill 分工完成：

- `capture-memory`
  - 只负责在活跃工作中记录高信号观察
  - 保持轻量
  - 不负责 consolidation 和 promotion
- `capability-evolution`
  - 负责判断任务意图
  - 负责发现、比较、验证能力路径
  - 把“采用能力”和“写入长期记忆”两件事拆开
- `dream-consolidate`
  - 负责夜间整理
  - 生成候选
  - 做晋升、拒绝、归档和审计报告

## 能力进化

这个仓库采用的是 EvoMap-lite 思路，而不是把整套 EvoMap 协议原样搬进来。

目标不是把 Gene、Capsule 或分布式演化网络都塞进 Codex，而是给 Codex 一套轻量、可执行、可审计的能力进化工作流。

### 四类任务意图

- `repair`
  - 修复坏掉的能力路径或缺失的能力
- `optimize`
  - 不改变任务形状，只把现有路径做得更稳、更快或更准
- `innovate`
  - 新增一个有意义的新能力或新工作流
- `explore`
  - 只有当官方和本地方案都不够或不清楚时，才升级到 GitHub 搜索

### 固定发现顺序

始终按这个顺序查找，并在找到足够好的方案后停止：

1. 已启用官方插件
2. 可安装官方插件
3. 本地内置技能
4. 可信 GitHub 技能或项目

### 采用前验证

在引入任何新能力前，先检查：

- 跟当前任务是否真的相关
- 最近是否还在维护
- 来源是否可信
- 接入成本是否值得预期收益

### 职责拆分

这件事很重要，因为“今天怎么做事”和“以后什么该变成长久规则”不能在同一步里草率决定。

- 能力采用发生在当前任务里
- 记忆晋升发生在之后的 Dream Loop review 里

## 审核与审计

这个仓库明确偏向 reviewer-assisted 和 subagent-assisted 的维护方式，而不是一条路径说了算。

- `capture-memory` 保持轻量和事件导向
- `capability-evolution` 可以在采用前比较多条能力路径
- `dream-consolidate` 在 promotion、rejection、archive、conflict review 上优先走 reviewer 或 subagent 复核
- 低风险清理仍然可以走单 agent fast path

审计不是附加功能，而是整套自我进化机制可信的原因。

每次有意义的变化，都应该能回答：

- 是哪条 source event 触发了它
- 最后采用了什么路径
- 哪些选项被拒绝了，为什么
- reviewer 或 subagent 有没有分歧
- 以后如何回滚

## 这个仓库包含什么

这个仓库提供了运行 Dream Loop + Capability Evolution 所需的最小组件：

- `skills/capture-memory/`
  - 白天采集 skill
  - 负责把结构化观察写入 `inbox/`
- `skills/capability-evolution/`
  - 活跃工作中的能力发现与验证 skill
  - 负责把插件、skills、GitHub 搜索放进一个受控顺序
- `skills/dream-consolidate/`
  - 夜间整理 skill
  - 负责去重、过期处理、晋升、归档和报告
- `templates/`
  - 全局 `AGENTS.md` 起始片段
  - memory 文件与 projection 模板
- `references/`
  - scope、promotion、audit、capability-evolution 的设计说明
- `automations/`
  - 推荐的夜间自动整理 prompt 和调度方式

## 核心规则

- 活跃工作只把新信号写入 `inbox/`，不直接改长期记忆
- `capture-memory` 只做捕获，不做晋升
- `capability-evolution` 只做发现、比较、验证和采用，不做长期记忆落盘
- GitHub 搜索是升级路径，不是默认动作
- 采用第三方 GitHub 能力或做明显的全局配置变更时，要向用户汇报
- 只有夜间 consolidation 才应该改长期记忆状态
- 每一次 promotion、merge、archive、rejection、rollback 都必须可审计

## 仓库结构

```text
repo/
├── README.md
├── README.zh-CN.md
├── assets/
│   └── hero-logo.png
├── references/
│   ├── audit-model.md
│   ├── capability-evolution-model.md
│   ├── promotion-rules.md
│   └── scope-model.md
├── templates/
├── examples/
├── automations/
└── skills/
    ├── capture-memory/
    ├── capability-evolution/
    └── dream-consolidate/
```

## 快速开始

如果你想图省事，最简单的方式就是直接把这个仓库丢给 Codex，让它帮你安装。

比如直接说：

```text
帮我从 https://github.com/JY0xLU/codex-native-dream-loop 安装这些 skills，并接进我的 Codex 配置。
```

如果你更想手动安装：

1. 把 `skills/capture-memory/`、`skills/capability-evolution/` 和 `skills/dream-consolidate/` 复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`。
2. 把 `templates/global/` 下的模板复制到你的 Codex home 作为起始结构。
3. 把 `AGENTS.md` 片段接入你的全局入口或项目入口。
4. 在活跃工作中，当任务需要受控地发现工具或工作流时，使用 `capability-evolution`。
5. 用 `capture-memory` 记录高信号结果、阻塞点或工作流收益到 `inbox/`。
6. 用 `dream-consolidate` 做夜间或显式维护整理。
7. 对重要的晋升或拒绝决策，优先走 reviewer 或 subagent 复核。

## 实际效果应该是什么样

这套闭环的目标不是“让 memory 变多”，而是让整个系统变得更准、更稳。

- 一个模式第一次出现时，它只是 `Observed`
- 重复出现之后，它才会进入候选
- 当前阶段真正重要的临时指导进入 `ACTIVE.md`
- 稳定跨任务成立的规律进入 `LEARNINGS.md`
- 一次性的能力试验可以停留在 `reference` 或 `trial`，不必直接固化成规则
- 失效或被替代的内容会被归档，并留下解释线索

只有当记忆保持分层、能力采用保持受控、晋升保持可质疑和可回滚时，自我进化才不会反过来拖累系统本身。
