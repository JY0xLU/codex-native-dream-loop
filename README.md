# Codex Improving

[中文](README.zh-CN.md) | English

[![Codex Native](https://img.shields.io/badge/Codex-Native-0f172a?style=flat-square&logo=openai&logoColor=white)](https://github.com/JY0xLU/codex-improving)
[![Subagent Reviewed](https://img.shields.io/badge/Subagent-Reviewed-1d4ed8?style=flat-square)](https://github.com/JY0xLU/codex-improving/tree/codex/readme-story-refresh)
[![Automation Ready](https://img.shields.io/badge/Automation-Ready-0f766e?style=flat-square)](automations/)
[![Auditable Memory](https://img.shields.io/badge/Memory-Auditable-f59e0b?style=flat-square)](references/audit-model.md)

> A Codex-native Dream Loop system for structured memory, review, and nightly consolidation.

**Quick links:** [Why This Exists](#why-this-exists) · [What This Repository Includes](#what-this-repository-includes) · [Memory Layers](#memory-layers) · [Core Rules](#core-rules) · [Quick Start](#quick-start)

![Codex Improving hero](assets/hero-subagent-control-mesh.svg)

### Project Highlights

- Capture during work, consolidate off-hours
- Keep `AGENTS.md` stable and human-reviewed
- Use subagent cross-review for important promotion and rejection decisions
- Preserve raw evidence so memory upgrades stay explainable later

## Why This Exists

Most "AI memory" systems fail for one of two reasons:

1. They mix stable rules, temporary context, error logs, and future ideas into one file.
2. They try to rewrite memory while the agent is actively solving the current task.

This repo takes the opposite approach:

- keep rules and learnings separate
- capture first, consolidate later
- only promote memory when it is repeated, generalizable, and actionable
- never auto-edit `AGENTS.md`
- prefer subagent cross-review for promotion, rejection, and audit decisions

This project does not try to turn Codex into another Claude Code. Instead, it treats Codex's native building blocks as the execution substrate:

- `AGENTS.md`
- skills
- automations
- worktrees
- sandbox and permissions
- subagents

The goal is to reduce repeated rediscovery, reduce avoidable context bloat, and improve consistency without letting automation silently rewrite top-level rules.

## How It Works

![Dream Loop flow](assets/dream-loop-flow.svg)

The operating loop is simple:

- capture high-signal observations during active work
- store them in `inbox/` without touching long-term memory
- run nightly review and consolidation
- promote only repeated, generalizable, actionable items
- keep every decision auditable

## What This Repository Includes

This repository ships a practical Dream Loop starter set:

- [`skills/capture-memory/`](skills/capture-memory/)
  - a daytime capture skill
  - records structured observations into `inbox/`
- [`skills/dream-consolidate/`](skills/dream-consolidate/)
  - a nighttime consolidation skill
  - deduplicates, expires, rewrites, and promotes memory
- [`templates/`](templates/)
  - starter `AGENTS.md` snippet
  - starter memory files and global setup pieces
- [`examples/`](examples/)
  - a minimal global-memory example
- [`automations/`](automations/)
  - a recommended nightly automation prompt and schedule
- [`references/`](references/)
  - promotion rules, scope notes, audit model, evals, and automation design notes

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
- `capture-memory` should stay lightweight; subagent-heavy work belongs in Dream Loop review and audit passes

## Subagent Bias

This repo now prefers a subagent-assisted review model for Dream Loop maintenance:

- `capture-memory` remains a lightweight single-agent workflow
- `dream-consolidate` should prefer at least one subagent for promotion, rejection, archive, and conflict review
- low-risk cleanup may still use a single-agent fast path
- if the main agent and reviewer disagree, the final report should record the disagreement and the resolution

## Repo Layout

- [`README.md`](README.md)
- [`README.zh-CN.md`](README.zh-CN.md)
- [`references/`](references/)
- [`templates/`](templates/)
- [`examples/`](examples/)
- [`automations/`](automations/)
- [`skills/capture-memory/`](skills/capture-memory/)
- [`skills/dream-consolidate/`](skills/dream-consolidate/)

## Quick Start

1. Copy `skills/capture-memory/` and `skills/dream-consolidate/` into `$CODEX_HOME/skills/` or `~/.codex/skills/` so Codex can discover them.
2. Copy the templates under `templates/global/` into your global Codex home as a starting point.
3. Add the `AGENTS.md` snippet to your global or project entrypoint.
4. Use `capture-memory` during active work.
5. Run `dream-consolidate` on a nightly automation.
6. Prefer subagent cross-review for important nightly promotion or rejection decisions.
7. Review the generated report before trusting promoted rules.

## In Practice

One practical example:

1. A user correction gets captured into `inbox/`.
2. Similar evidence accumulates over multiple sessions.
3. Nightly consolidation reviews the pattern, often with a reviewer subagent.
4. Repeated operational guidance is promoted into `ACTIVE.md`; stable cross-task guidance is promoted into `LEARNINGS.md`.
5. The report explains what changed, what was rejected, and why.

## License

[MIT](LICENSE)
