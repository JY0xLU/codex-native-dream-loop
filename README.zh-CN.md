# Codex Improving

中文 | [English](README.md)

`codex-improving` 是一个面向 Codex 的 Dream Loop 系统。

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
- 重要的升级、拒绝、审计判断优先走 subagent 交叉复核

## 仓库包含什么

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
- `capture-memory` 应保持轻量；多 agent 复核主要留给 Dream Loop 审核阶段

## Subagent 倾向

这个仓库现在更推荐“subagent-assisted review”模式：

- `capture-memory` 继续保持单 agent 轻量工作流
- `dream-consolidate` 在 promotion、rejection、archive、冲突判断时，优先使用至少一个 subagent 做交叉复核
- 纯低风险清理可以继续走单 agent fast path
- 如果主 agent 和 reviewer subagent 出现分歧，最终报告必须写清楚分歧与裁决

## 仓库结构

```text
codex-improving/
├── README.md
├── README.zh-CN.md
├── references/
├── templates/
├── examples/
├── automations/
└── skills/
    ├── capture-memory/
    └── dream-consolidate/
```

## 快速上手

1. 把 `skills/capture-memory/` 和 `skills/dream-consolidate/` 复制到 `$CODEX_HOME/skills/` 或 `~/.codex/skills/`，让 Codex 能发现它们
2. 把 `templates/global/` 下的模板复制到全局 Codex home 作为初始结构
3. 把 `AGENTS.md` 片段接进你的入口规则
4. 白天用 `capture-memory`
5. 夜间用 `dream-consolidate`
6. 对重要的 nightly 提升/拒绝判断，优先走 subagent 交叉复核
7. 先 review nightly report，再信任升级结果
