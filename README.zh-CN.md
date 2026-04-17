# Codex Native Dream Loop

[中文](README.zh-CN.md) | [English](README.md)

![Codex Native Dream Loop logo](assets/hero-logo.png)

**这是一套面向 Codex 的记忆机制 + 自我进化机制：前台只暴露小而清晰的公开接口，后台负责记忆捕获、路线复用、能力进化和离线整理。**

`Codex Native Dream Loop` 适合这样的人：希望 Codex 越做越强，但不想把记忆系统越堆越复杂。目标不只是减少层级，而是把记忆、自我进化和执行优化真正接在一起，让 Codex 下次更快走上已经验证过的好路线。

![Codex Native](https://img.shields.io/badge/Codex-Native-1f6feb)
![Self-Improving](https://img.shields.io/badge/Self--Improving-3fb950)
![Dual Layer Model](https://img.shields.io/badge/Public%20Model-Dual%20Layer-2563eb)
![Path Memory](https://img.shields.io/badge/Path%20Memory-Reuse-0f766e)
![Auditable](https://img.shields.io/badge/Auditable-111827)

**快速导航**

[为什么存在](#为什么存在) | [公开模型](#公开模型) | [闭环如何工作](#闭环如何工作) | [核心 Skills](#核心-skills) | [自动化](#自动化) | [后台机制](#后台机制) | [快速开始](#快速开始)

> 很多 agent 不是不会做事，而是每次都要重新摸路，或者把记忆层级越堆越多。  
> Codex Native Dream Loop 要做的，是把公开模型压缩到最小，把最佳路径复用起来，把必要的审计藏到后台。

## 为什么存在

一个 agent 跑久以后，最大的问题往往不是模型能力不够，而是“路径漂移”。

- 明明走通过的路线，下次还要从零再试
- 有用经验散落在旧对话里，没有被收回来
- 一些临时规则留得太久，开始污染后面的决策
- 有用的 plugin 和 skill 找得太晚
- 记忆系统加出来的层，比真正带来的清晰度还多

这个仓库存在的目的，就是让下一次行动比上一次更省、更快、更稳。

它的做法不是只谈两层 memory，而是把更完整的自我进化闭环收在后台，同时对外只保留两个公开层：

- `ACTIVE.md`
  - 现在就该影响行为的热路径和热规则
- `LEARNINGS.md`
  - 已经验证过、值得复用的路径记忆

其他机制都退到后台。

## 公开模型

这个仓库故意只暴露两层公开模型，但完整系统本身还包括 `capture-memory`、`capability-evolution`、`dream-consolidate` 和自动化审计。

### `ACTIVE.md`

`ACTIVE.md` 是热层。

这里放的是：

- 当前阶段真的重要的规则
- 当前最值得优先走的热路径
- 只要进入下一次任务就会立刻影响决策的内容

如果某条东西已经不再影响近期行为，它就不该继续留在这里。

### `LEARNINGS.md`

`LEARNINGS.md` 是路径记忆层，不是什么 “active learning” 回路。

每条 learning 都不是泛泛的经验句子，而是一条“获胜路径”记录。它至少应该回答：

- 这条路径适用于什么任务模式
- 首选路径是什么
- 它为什么更快、更稳或更准
- 最近一次是什么时候验证的
- 背后证据是什么
- 失败时该退回到什么备选路径

这样系统读起来更像“路线库”，而不是“杂乱的心得库”。

## 闭环如何工作

整个工作循环是：

`recall -> choose -> search if needed -> execute -> capture -> consolidate`

落地成实际步骤就是：

1. 先从 `ACTIVE.md` 和 `LEARNINGS.md` 里只取最小相关片段。
2. 如果已有路径明显适用，就先复用。
3. 如果把握还不够高，再让 `capability-evolution` 按顺序去找：
   已启用官方插件 -> 可安装官方插件 -> 本地 skills -> 可信 GitHub 项目。
4. 当前任务只选一条获胜路径执行，不同时固化多条竞争路线。
5. 用 `capture-memory` 记录高信号结果或阻塞点。
6. 用 `dream-consolidate` 在夜间把 `ACTIVE.md` 保持热，把 `LEARNINGS.md` 维护成路径记忆库，并把淘汰路线归档。

公开模型保持简单，但后台仍然可审计。

## 核心 Skills

当前这套系统主要由三个 skill 组成：

- `capture-memory`
  - 活跃工作时的轻量事件捕获
- `capability-evolution`
  - 路径发现、能力验证、能力选择
- `dream-consolidate`
  - 夜间整理、热层刷新、路径晋升和审计记录

三者共同服务一个目标：

**先复用已经赢过的路线，不够时再主动扩大搜索。**

## 自动化

这个仓库默认只需要一个持续运行的 automation，而不是越拆越多的定时 agent。

这个单 automation 每次运行要同时完成四件事：

- 维护 Dream Loop 的双层 memory
- 审计当前 repo / PR 轮次状态
- 检查 automation 自己的 prompt 有没有落后于仓库
- 给出下一轮最小可执行改进建议

它应该足够强，能跟着仓库演进持续校准；但也必须有边界，在 repo 层只做审计和建议，不静默改跟踪文件。

## 后台机制

系统仍然保留一些后台机制，但它们不该再成为主要心智模型。

后台支持机制包括：

- `inbox/`
  - 原始信号的追加式缓冲区
- `AUDIT_LOG.md`
  - 最小化的晋升、拒绝、归档、回滚痕迹
- `ARCHIVE/`
  - 退役或被替代的内容，用来保留可追溯性

这些东西存在，是为了审计和回滚，不是为了让你每天脑子里再多背几层结构。

## 这个仓库包含什么

- `templates/`
  - 全局 `AGENTS.md` 起始片段
  - 围绕 `ACTIVE.md` 和 `LEARNINGS.md` 的最小骨架
- `skills/`
  - 驱动整套闭环的三个 skill
- `automations/`
  - 负责 memory 维护、repo/PR 审计、drift 检查和下一轮建议的单个 recurring automation prompt
- `references/`
  - 路径记忆、晋升规则、自动化的简明设计说明
- `examples/`
  - 使用双层公开模型的最小全局示例

## 快速开始

如果你想图省事，最简单的方式就是直接把这个仓库交给 Codex，让它帮你接到自己的 Codex home 里。

比如直接说：

```text
帮我从 https://github.com/JY0xLU/codex-native-dream-loop 安装这些 skills，并接进我的 Codex 配置。
```

如果你更想手动安装：

1. 把 `skills/capture-memory/`、`skills/capability-evolution/` 和 `skills/dream-consolidate/` 复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`。
2. 把 `templates/global/` 复制到你的 Codex home 作为起始结构。
3. 把 `AGENTS.md` 片段接入你的全局入口或项目入口。
4. 日常优先读 `ACTIVE.md`，其次才读 `LEARNINGS.md`。
5. 需要找更优路线时，用 `capability-evolution` 扩大搜索。
6. `capture-memory` 只负责记录高信号结果。
7. 运行这一个 Dream Loop recurring automation，让它在夜间刷新热层、审计当前 repo/PR、检查 prompt drift，并给出下一轮建议。

## 什么叫“效果变好了”

这套系统真的跑顺之后，会有这些感觉：

- 新任务不再频繁从零开始
- `ACTIVE.md` 会一直很短，而且一眼能看出现在为什么重要
- `LEARNINGS.md` 更像路线库，不像心得堆
- plugin 和 skill 会在需要时被主动找出来
- 输掉的路线会被归档，而不是静默消失
- 系统变快了，但没有变得更乱
