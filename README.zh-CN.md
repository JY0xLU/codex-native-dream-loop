# Codex Improving

中文 | [English](README.md)

[![Codex Native](https://img.shields.io/badge/Codex-Native-0f172a?style=flat-square&logo=openai&logoColor=white)](https://github.com/JY0xLU/codex-improving)
[![Subagent Reviewed](https://img.shields.io/badge/Subagent-Reviewed-1d4ed8?style=flat-square)](https://github.com/JY0xLU/codex-improving/tree/codex/readme-story-refresh)
[![Automation Ready](https://img.shields.io/badge/Automation-Ready-0f766e?style=flat-square)](automations/)
[![Auditable Memory](https://img.shields.io/badge/Memory-Auditable-f59e0b?style=flat-square)](references/audit-model.md)

> 一个面向 Codex 的 Dream Loop 系统，用来做结构化记忆、审查与夜间整理。

**快速跳转：** [项目动机](#项目动机) · [仓库包含什么](#仓库包含什么) · [记忆分层](#记忆分层) · [核心规则](#核心规则) · [快速开始](#快速开始)

![Codex Improving 横幅](assets/hero-subagent-control-mesh.svg)

### 项目亮点

- 工作中采集，空闲时整理
- 让 `AGENTS.md` 保持稳定并坚持人工 review
- 重要的升级与拒绝判断优先走 subagent 交叉复核
- 保留原始证据，让记忆升级可以回溯解释

## 项目动机

很多“AI 长期记忆”方案会失败，通常是因为：

1. 把稳定规则、临时上下文、错误日志、未来需求混在一个文件里。
2. 在 agent 正在干活时，就让它大规模重写记忆。

这个仓库的做法相反：

- 规则和学习分开
- 先采集，后提炼
- 只有在“重复出现、可泛化、可执行”时才允许升级
- 永不自动改 `AGENTS.md`
- 重要的升级、拒绝、审计判断优先走 subagent 交叉复核

这个项目不是想把 Codex 做成另一个 Claude Code，而是把 Codex 自己已经擅长的东西当成“执行底座”：

- `AGENTS.md`
- skills
- automations
- worktrees
- sandbox 与权限
- subagents

目标是减少重复摸索、减少无意义的上下文膨胀、提高长期一致性，同时避免自动化偷偷重写顶层规则。

## 它怎么工作

![Dream Loop 流程图](assets/dream-loop-flow.svg)

整条 Dream Loop 很简单：

- 在工作中记录高信号观察
- 先写进 `inbox/`，不动长期记忆
- 夜间做 review 和 consolidation
- 只有在“重复出现、可泛化、可执行”时才升级
- 所有改动都要留下审计痕迹

## 仓库包含什么

这个仓库提供了一套可直接上手的 Dream Loop 起步组合：

- [`skills/capture-memory/`](skills/capture-memory/)
  - 白天采集 skill
  - 负责把观察写进 `inbox/`
- [`skills/dream-consolidate/`](skills/dream-consolidate/)
  - 夜间整理 skill
  - 负责去重、失效处理、重写、升级
- [`templates/`](templates/)
  - 初始 `AGENTS.md` 片段
  - memory 文件与全局接线模板
- [`examples/`](examples/)
  - 一套最小示例
- [`automations/`](automations/)
  - 推荐的夜间自动化 prompt 与调度样例
- [`references/`](references/)
  - promotion rules、scope、audit、evals 和 automation 设计说明

## 记忆分层

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

## 核心规则

- 白天采集只写 `.codex/memory/inbox/`
- 夜间整理只改 `.codex/memory/` 下的记忆文件
- `AGENTS.md` 禁止自动改
- 所有升级、合并、删除、拒绝都必须可审计
- `ACTIVE.md` 允许临时规则，但必须写明失效条件
- `capture-memory` 应保持轻量；多 agent 复核主要留给 Dream Loop 审核阶段

## Subagent 倾向

这个仓库现在更推荐“subagent-assisted review”模式：

- `capture-memory` 继续保持单 agent 轻量工作流
- `dream-consolidate` 在 promotion、rejection、archive、冲突判断时，优先使用至少一个 subagent 做交叉复核
- 纯低风险清理可以继续走单 agent fast path
- 如果主 agent 和 reviewer subagent 出现分歧，最终报告必须写清楚分歧与裁决

## 仓库结构

- [`README.md`](README.md)
- [`README.zh-CN.md`](README.zh-CN.md)
- [`references/`](references/)
- [`templates/`](templates/)
- [`examples/`](examples/)
- [`automations/`](automations/)
- [`skills/capture-memory/`](skills/capture-memory/)
- [`skills/dream-consolidate/`](skills/dream-consolidate/)

## 快速开始

1. 把 `skills/capture-memory/` 和 `skills/dream-consolidate/` 复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`，让 Codex 能发现它们。
2. 把 `templates/global/` 下的模板复制到全局 Codex home 作为初始结构。
3. 把 `AGENTS.md` 片段接进你的入口规则。
4. 白天用 `capture-memory`。
5. 夜间用 `dream-consolidate`。
6. 对重要的 nightly 提升/拒绝判断，优先走 subagent 交叉复核。
7. 先 review nightly report，再信任升级结果。

## 实际会怎么用

一个很典型的场景：

1. 用户纠正被采集进 `inbox/`。
2. 类似证据在多个 session 中逐步累积。
3. 夜间整理读取这些证据，并用 reviewer subagent 做交叉判断。
4. 重复出现的操作性规则进入 `ACTIVE.md`，稳定的跨任务经验进入 `LEARNINGS.md`。
5. 报告会说明改了什么、拒绝了什么、原因是什么。

## License

[MIT](LICENSE)
