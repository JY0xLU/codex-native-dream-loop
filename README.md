# Codex Improving

[中文](README.zh-CN.md) | English

`codex-improving` is a Codex-native Dream Loop system.

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
- prefer subagent cross-review for promotion, rejection, and audit decisions

## What This Repository Includes

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
- `capture-memory` should stay lightweight; subagent-heavy work belongs in Dream Loop review and audit passes

## Subagent Bias

This repo now prefers a subagent-assisted review model for Dream Loop maintenance:

- `capture-memory` remains a lightweight single-agent workflow
- `dream-consolidate` should prefer at least one subagent for promotion, rejection, archive, and conflict review
- low-risk cleanup may still use a single-agent fast path
- if the main agent and reviewer disagree, the final report should record the disagreement and the resolution

## Repo Layout

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

## Quick Start

1. Copy `skills/capture-memory/` and `skills/dream-consolidate/` into `$CODEX_HOME/skills/` or `~/.codex/skills/` so Codex can discover them.
2. Copy the templates under `templates/global/` into your global Codex home as a starting point.
3. Add the `AGENTS.md` snippet to your global or project entrypoint.
4. Use `capture-memory` during active work.
5. Run `dream-consolidate` on a nightly automation.
6. Prefer subagent cross-review for important nightly promotion or rejection decisions.
7. Review the generated report before trusting promoted rules.
