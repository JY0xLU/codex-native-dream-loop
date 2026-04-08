# Codex Improving

中文 | [English](#english)

## English

`codex-improving` is a Codex-native Dream Loop MVP.

Its core idea is simple:

- Daytime only captures memory.
- Nighttime consolidates memory.

This project does not try to turn Codex into another Claude Code. Instead, it treats Codex's native building blocks as the execution substrate:

- `AGENTS.md`
- skills
- automations
- worktrees
- sandbox and permissions
- subagents

The goal is to reduce repeated rediscovery, reduce avoidable context bloat, and improve consistency without letting automation silently rewrite top-level rules.

## Why This Exists

Most "AI memory" systems fail for one of two reasons:

1. They mix stable rules, temporary context, error logs, and future ideas into one file.
2. They try to rewrite memory while the agent is actively solving the current task.

This repo takes the opposite approach:

- keep rules and learnings separate
- capture first, consolidate later
- only promote memory when it is repeated, generalizable, and actionable
- never auto-edit `AGENTS.md`

## MVP v1

This repository ships a minimal Dream Loop:

- `skills/capture-memory/`
  - a daytime capture skill
  - records structured observations into `inbox/`
- `skills/dream-consolidate/`
  - a nighttime consolidation skill
  - deduplicates, expires, rewrites, and promotes memory
- `templates/`
  - starter `AGENTS.md` snippet
  - starter memory files
- `examples/`
  - a minimal global-memory example
- `automations/`
  - a recommended nightly automation prompt and schedule

## Memory Layers

### 1. Stable Rules Layer

Use `AGENTS.md` as the main entry point.

- Put short, durable operating rules here
- Do not auto-edit it
- Only change it through human review

### 2. Raw Capture Layer

Use `.codex/memory/inbox/` as an append-only event stream.

Capture things like:

- user corrections
- repeated command failures
- stable user preferences
- successful recurring workflows
- capability gaps worth tracking

### 3. Working Memory Layer

Use `ACTIVE.md` for high-frequency, currently useful guidance.

- short-lived workarounds
- sprint-specific rules
- temporary but important operational constraints

### 4. Long-Term Learning Layer

Use `LEARNINGS.md` for stable, reusable lessons.

- cross-task best practices
- stable project patterns
- reusable debugging strategies

### 5. Opportunity Layer

Use `FEATURE_REQUESTS.md` for future capability and productization opportunities.

- missing skills
- repeated workflow pain points
- good candidates for later automation or skill extraction

## Core Rules

- Daytime capture writes only to `.codex/memory/inbox/`
- Nighttime consolidation may rewrite memory files under `.codex/memory/`
- `AGENTS.md` must not be auto-modified
- Every promotion, merge, archive, and rejection should be auditable
- `ACTIVE.md` may contain temporary guidance, but every temporary item should include an expiry condition

## Repo Layout

```text
codex-improving/
├── README.md
├── COMPARISON.md
├── references/
├── templates/
├── examples/
├── automations/
└── skills/
    ├── capture-memory/
    └── dream-consolidate/
```

## Non-Goals For v1

These are intentionally deferred:

- multi-subagent consolidation pipelines
- automatic skill generation
- repo-local vs global automatic switching
- custom `CODEX_HOME` orchestration
- plugin packaging

## Quick Start

1. Copy `skills/capture-memory/` and `skills/dream-consolidate/` into `$CODEX_HOME/skills/` or `~/.codex/skills/` so Codex can discover them.
2. Copy the templates under `templates/global/` into your global Codex home as a starting point.
3. Add the `AGENTS.md` snippet to your global or project entrypoint.
4. Use `capture-memory` during active work.
5. Run `dream-consolidate` on a nightly automation.
6. Review the generated report before trusting promoted rules.

## Relationship To The Earlier Skill

The earlier `self-improving-for-codex` skill is a good first-generation pattern:

- one skill
- one memory loop
- one nightly refinement concept

This repository is the second-generation design:

- split capture from consolidation
- treat memory as a governed pipeline, not just a set of files
- introduce auditability and layer boundaries
- align more directly with Codex-native execution primitives

## 中文说明

`codex-improving` 是一个面向 Codex 的 Dream Loop 最小可用版本。

它的核心原则只有一句：

- 白天只记录
- 夜里才提炼

这个项目不是想把 Codex 做成另一个 Claude Code，而是把 Codex 自己已经擅长的东西当成“执行底座”：

- `AGENTS.md`
- skills
- automations
- worktrees
- sandbox 与权限
- subagents

目标是：

- 减少重复摸索
- 减少无意义的上下文膨胀
- 提高长期一致性
- 避免自动化偷偷重写顶层规则

## 这个项目解决什么问题

很多“AI 长期记忆”方案会失败，通常是因为：

1. 把稳定规则、临时上下文、错误日志、未来需求混在一个文件里
2. 在 agent 正在干活时，就让它大规模重写记忆

这个仓库的做法相反：

- 规则和学习分开
- 先采集，后提炼
- 只有在“重复出现、可泛化、可执行”时才允许升级
- 永不自动改 `AGENTS.md`

## MVP v1 包含什么

- `skills/capture-memory/`
  - 白天采集 skill
  - 只负责把观察写进 `inbox/`
- `skills/dream-consolidate/`
  - 夜间整理 skill
  - 负责去重、失效处理、重写、升级
- `templates/`
  - 初始 `AGENTS.md` 片段
  - 初始 memory 文件模板
- `examples/`
  - 一套最小示例
- `automations/`
  - 推荐的夜间自动化 prompt 与调度样例

## 五层结构

### 1. 稳定规则层

使用 `AGENTS.md` 作为入口。

- 这里只放短、稳、可长期复用的规则
- 不允许自动改
- 只能走人工 review

### 2. 原始采集层

使用 `.codex/memory/inbox/` 作为 append-only 事件流。

适合记录：

- 用户纠正
- 反复失败的命令
- 稳定偏好
- 成功且重复的工作流
- 值得追踪的能力缺口

### 3. 工作记忆层

使用 `ACTIVE.md` 存高频、当前阶段有用的指导。

- 短期 workaround
- sprint 期间必须遵守的约束
- 虽然临时但很重要的操作规则

### 4. 长期学习层

使用 `LEARNINGS.md` 存稳定、跨任务可复用的学习。

- 通用最佳实践
- 项目内稳定模式
- 可复用的排障策略

### 5. 机会层

使用 `FEATURE_REQUESTS.md` 存未来能力与产品化机会。

- 缺少的 skill
- 反复出现的流程痛点
- 未来可以 skill 化或自动化的模式

## 核心行为规则

- 白天采集只写 `.codex/memory/inbox/`
- 夜间整理只改 `.codex/memory/` 下的记忆文件
- `AGENTS.md` 禁止自动改
- 所有升级、合并、删除、拒绝都必须可审计
- `ACTIVE.md` 允许临时规则，但必须写明失效条件

## v1 不做什么

这些能力刻意放到后续版本：

- 多 subagent 并行 consolidation
- 自动生成 skill draft
- 自动切换 global / repo-local / custom `CODEX_HOME`
- plugin 化封装

## 快速上手

1. 把 `skills/capture-memory/` 和 `skills/dream-consolidate/` 复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`，让 Codex 能发现它们
2. 把 `templates/global/` 下的模板复制到全局 Codex home 作为初始结构
3. 把 `AGENTS.md` 片段接进你的入口规则
4. 白天用 `capture-memory`
5. 夜间用 `dream-consolidate`
6. 先 review nightly report，再信任升级结果
