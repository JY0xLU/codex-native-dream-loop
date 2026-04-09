# Codex Native Dream Loop

[中文](README.zh-CN.md) | English

![Codex Native Dream Loop logo](assets/hero-logo.png)

**A Codex-native system for self-improvement, scoped memory, and auditable nightly consolidation.**

Codex Native Dream Loop is built for people who want Codex to remember the right things, forget the noise, and keep getting better without turning context into a landfill.

![Codex Native](https://img.shields.io/badge/Codex-Native-1f6feb)
![Self-Improving](https://img.shields.io/badge/Self--Improving-3fb950)
![Scoped Memory](https://img.shields.io/badge/Scoped%20Memory-8b5cf6)
![Nightly Consolidation](https://img.shields.io/badge/Nightly%20Consolidation-f59e0b)
![Subagent Review](https://img.shields.io/badge/Subagent%20Review-0ea5e9)
![Auditable](https://img.shields.io/badge/Auditable-111827)

**Quick Navigation**

[Why It Exists](#why-it-exists) | [Core Capabilities](#core-capabilities) | [How It Works](#how-it-works) | [Memory Model](#memory-model) | [Review and Audit](#review-and-audit) | [Quick Start](#quick-start)

> Most agents do not really learn. They just accumulate context.
> Codex Native Dream Loop captures signal during work, consolidates it off-hours, and brings back only the memory that still matters.

## Why It Exists

Once an agent has worked with you for a while, the biggest failure is usually not raw capability. It is memory quality.

- temporary workarounds start looking like permanent rules
- stable preferences stay trapped inside old conversations
- useful patterns never graduate into reusable guidance
- the same mistakes get rediscovered again and again
- context gets longer, but not smarter

This project exists to fix that loop.

Instead of treating memory as a pile of notes, Codex Native Dream Loop treats it as a small operating cycle:

- capture high-signal observations during active work
- keep long-term memory untouched while solving the task
- consolidate, deduplicate, and promote memory off-hours
- retrieve only the slices that match the next task
- keep every meaningful memory decision auditable

The goal is simple: **make Codex improve through work, not just sit on more context.**

## Core Capabilities

| Capability | What It Does | Why It Matters |
|---|---|---|
| Scoped Memory | Splits memory into `global`, `repo`, and `thread` scope. | Prevents cross-project pollution and keeps retrieval targeted. |
| Daytime Capture | Records high-signal observations into `inbox/` during active work. | Keeps the main task lightweight and avoids rewriting long-term memory mid-flight. |
| Nightly Consolidation | Deduplicates, expires, rewrites, and promotes memory off-hours. | Lets the system improve without interrupting active work. |
| Reviewer-Assisted Promotion | Uses reviewer checks for important promotion, rejection, archive, and conflict decisions. | Reduces bad promotion and keeps the loop honest. |
| Operational vs LongTerm Memory | Separates temporary but important guidance from stable cross-task patterns. | Makes memory reusable without turning everything into a permanent rule. |
| Audit Trail | Preserves source IDs, verdicts, and rollback clues. | Makes every memory change explainable and recoverable. |
| Minimal Retrieval | Reads only the slices needed for the current task. | Controls token cost and avoids broad rereads. |
| Codex-Native Workflow | Fits `AGENTS.md`, skills, automations, worktrees, sandboxing, and subagents. | Uses Codex the way it is designed to work instead of fighting the platform. |

## How It Works

The loop is intentionally simple.

1. During work, `capture-memory` records only high-signal observations.
2. Those observations land in `inbox/` first, not directly in long-term memory.
3. Off-hours, `dream-consolidate` reads recent signal and builds candidates.
4. Duplicates are merged, stale rules are expired, vague items are rewritten.
5. Temporary but operational guidance is projected into `ACTIVE.md`.
6. Stable cross-task patterns are promoted into `LEARNINGS.md`.
7. Important decisions leave an audit trail with traceable evidence and rollback clues.

This is what the logo represents:

- **daytime capture** on the left
- **nighttime consolidation** on the right
- a controlled loop in the middle that turns raw signal into reusable memory

## Memory Model

Codex Native Dream Loop keeps the memory model short on purpose.

### 1. Policy

`AGENTS.md` remains the human-facing policy layer.

- permanent operating rules live here
- safety boundaries live here
- policy-like changes must be proposed for review
- this layer must never be auto-edited

### 2. Memory Scopes

Only three scopes are used:

- `global` for stable cross-project patterns
- `repo` for project-specific habits and rules
- `thread` for short-lived working context

Readable projections stay simple:

- `ACTIVE.md` is the operational projection
- `LEARNINGS.md` is the long-term projection

### 3. Improvement Loop

The loop is split across two installed skills:

- `capture-memory`
  - records high-signal observations
  - stays lightweight
  - does not consolidate or promote memory
- `dream-consolidate`
  - performs off-hours cleanup and consolidation
  - builds candidates
  - reviews promotion or rejection paths
  - updates projections and audit records

## Review and Audit

This project deliberately favors reviewer-assisted memory maintenance.

- `capture-memory` remains a lightweight single-agent workflow
- `dream-consolidate` should prefer at least one reviewer step for promotion, rejection, archive, and conflict review
- low-risk cleanup may still use a single-agent fast path
- if the main agent and reviewer disagree, the final report should record both the disagreement and the resolution

Audit is not an extra. It is the reason the loop stays trustworthy.

Every meaningful change should preserve:

- the source event or source ID
- the reviewer verdict
- the final decision
- a rollback clue

That way, promoted memory can be questioned, traced, and reverted instead of silently drifting into policy.

## What This Repository Includes

This repository ships the pieces needed to run the loop:

- `skills/capture-memory/`
  - a daytime capture skill
  - records structured observations into `inbox/`
- `skills/dream-consolidate/`
  - a nighttime consolidation skill
  - deduplicates, expires, rewrites, promotes, and reports memory changes
- `templates/`
  - starter `AGENTS.md` snippet
  - starter memory files and projections
- `examples/`
  - a minimal memory example
  - example reports and reference structure
- `automations/`
  - a recommended nightly automation prompt and schedule
- `references/`
  - guidance for promotion, scope, audit, and consolidation behavior

## Core Rules

- Daytime capture writes only to `.codex/memory/inbox/`
- Nighttime consolidation may update files under `.codex/memory/`
- `AGENTS.md` must not be auto-modified
- every promotion, merge, archive, rejection, and rollback must be auditable
- temporary guidance belongs in `ACTIVE.md`, not automatically in `LEARNINGS.md`
- `capture-memory` should stay lightweight; reviewer-heavy work belongs in Dream Loop review and audit passes

## Repo Layout

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

## Quick Start

1. Copy `skills/capture-memory/` and `skills/dream-consolidate/` into `$CODEX_HOME/skills/` or `~/.codex/skills/`.
2. Copy the templates under `templates/global/` into your Codex home as a starting point.
3. Add the `AGENTS.md` snippet to your global or project entrypoint.
4. Use `capture-memory` during active work whenever a high-signal observation is worth keeping.
5. Run `dream-consolidate` on a nightly automation.
6. Prefer reviewer-assisted promotion or rejection for important memory decisions.
7. Review the generated audit report before trusting promoted rules.

## In Practice

Here is the behavior this project is aiming for:

- when a pattern appears once, it is observed
- when a pattern appears again, it becomes a candidate
- when it becomes operationally useful, it enters `ACTIVE.md`
- when it proves stable across tasks, it graduates into `LEARNINGS.md`
- if it stops being useful, it is archived with enough trace to explain why

The loop stays useful only if memory remains short, scoped, reviewable, and easy to challenge.
