# Codex Native Dream Loop

[中文](README.zh-CN.md) | English

![Codex Native Dream Loop logo](assets/hero-logo.png)

**A Codex-native system for self-improvement, scoped memory, controlled capability evolution, and auditable nightly consolidation.**

Codex Native Dream Loop is built for people who want Codex to remember the right things, discover the right capabilities at the right time, and keep getting better without turning context into a landfill.

![Codex Native](https://img.shields.io/badge/Codex-Native-1f6feb)
![Self-Improving](https://img.shields.io/badge/Self--Improving-3fb950)
![Scoped Memory](https://img.shields.io/badge/Scoped%20Memory-8b5cf6)
![Capability Evolution](https://img.shields.io/badge/Capability%20Evolution-2563eb)
![Nightly Consolidation](https://img.shields.io/badge/Nightly%20Consolidation-f59e0b)
![Subagent Review](https://img.shields.io/badge/Subagent%20Review-0ea5e9)
![Auditable](https://img.shields.io/badge/Auditable-111827)

**Quick Navigation**

[Why It Exists](#why-it-exists) | [Core Capabilities](#core-capabilities) | [How It Works](#how-it-works) | [Memory Model](#memory-model) | [Capability Evolution](#capability-evolution) | [Review and Audit](#review-and-audit) | [Quick Start](#quick-start)

> Most agents do not really learn. They either accumulate context, or improvise tooling one task at a time.
> Codex Native Dream Loop fixes both halves: it captures signal during work, chooses capabilities through a controlled path, consolidates off-hours, and brings back only the memory that still matters.

## Why It Exists

Once an agent has worked with you for a while, the biggest failure is usually not raw capability. It is operational drift.

- temporary workarounds start looking like permanent rules
- stable preferences stay trapped inside old conversations
- useful patterns never graduate into reusable guidance
- the same mistakes get rediscovered again and again
- promising new tools get adopted inconsistently or too late
- context gets longer, but not smarter

This project exists to fix that loop.

Instead of treating memory as a pile of notes, Codex Native Dream Loop treats self-improvement as a small operating cycle:

- recall only the narrowest memory slice that matters
- classify the task before deciding how to solve it
- discover capabilities in a controlled order
- validate new plugins, skills, or projects before adoption
- capture high-signal outcomes during active work
- consolidate, deduplicate, and promote memory off-hours
- keep every meaningful decision auditable

The goal is simple: **make Codex improve through work, not just sit on more context.**

## Core Capabilities

| Capability | What It Does | Why It Matters |
|---|---|---|
| Scoped Memory | Splits memory into `global`, `repo`, and `thread` scope. | Prevents cross-project pollution and keeps retrieval targeted. |
| Daytime Capture | Records high-signal observations into `inbox/` during active work. | Keeps the main task lightweight and avoids rewriting long-term memory mid-flight. |
| Capability Evolution | Classifies tasks and discovers capabilities in a fixed order: official plugins, installable official plugins, local skills, then trusted GitHub projects. | Prevents random tool drift and keeps self-improvement deliberate. |
| Validation Gate | Checks relevance, maintenance recency, source trust, and integration cost before adopting new capabilities. | Reduces bad installs and weak one-off experiments. |
| Nightly Consolidation | Deduplicates, expires, rewrites, and promotes memory off-hours. | Lets the system improve without interrupting active work. |
| Reviewer-Assisted Promotion | Uses reviewer checks for important promotion, rejection, archive, and conflict decisions. | Reduces bad promotion and keeps the loop honest. |
| Operational vs LongTerm Memory | Separates temporary but important guidance from stable cross-task patterns. | Makes memory reusable without turning everything into a permanent rule. |
| Audit Trail | Preserves source IDs, verdicts, and rollback clues. | Makes every memory change explainable and recoverable. |
| Codex-Native Workflow | Fits `AGENTS.md`, skills, automations, worktrees, sandboxing, plugins, and subagents. | Uses Codex the way it is designed to work instead of fighting the platform. |

## How It Works

The loop is intentionally simple and split into distinct responsibilities.

1. Recall only the smallest relevant slice from `ACTIVE.md` and `LEARNINGS.md`.
2. Classify the task as `repair`, `optimize`, `innovate`, or `explore`.
3. Discover capabilities in this order:
   enabled official plugins -> installable official plugins -> local built-in skills -> trusted GitHub skills or projects.
4. Validate any newly adopted capability before using it.
5. Finish the task with the chosen capability path.
6. Use `capture-memory` to record high-signal outcomes, blockers, or workflow wins into `inbox/`.
7. Off-hours, use `dream-consolidate` to deduplicate, review, promote, reject, or archive with audit-first discipline.

This is the full operating cycle:

`recall -> classify -> discover -> validate -> adopt -> capture -> consolidate`

## Memory Model

Codex Native Dream Loop keeps the memory model short on purpose.

### 1. Policy

`AGENTS.md` remains the human-facing policy layer.

- permanent operating rules live here
- safety boundaries live here
- policy-like changes must be proposed for review
- this layer must not be treated as a casual scratchpad

### 2. Memory Scopes

Only three scopes are used:

- `global` for stable cross-project patterns
- `repo` for project-specific habits and rules
- `thread` for short-lived working context

Readable projections stay simple:

- `ACTIVE.md` is the operational projection
- `LEARNINGS.md` is the long-term projection

### 3. Improvement Loop

The improvement loop is now split across three installed skills:

- `capture-memory`
  - records high-signal observations during active work
  - stays lightweight
  - does not consolidate or promote memory
- `capability-evolution`
  - classifies the task intent
  - discovers and validates capability options
  - separates adoption from long-term memory decisions
- `dream-consolidate`
  - performs off-hours cleanup and consolidation
  - builds candidates
  - reviews promotion or rejection paths
  - updates projections and audit records

## Capability Evolution

This repo adopts an EvoMap-lite stance rather than a full protocol stack.

The goal is not to recreate Genes, Capsules, or a distributed evolution network. The goal is to give Codex a stable, auditable way to improve how it works inside normal tasks.

### Intent Types

- `repair`
  - restore a broken or missing capability path
- `optimize`
  - improve an existing path without changing the task shape
- `innovate`
  - add a meaningful new capability or workflow
- `explore`
  - escalate to GitHub discovery only when official and local options are insufficient or unclear

### Discovery Order

Always search in this order and stop at the first sufficient option:

1. enabled official plugins
2. installable official plugins
3. local built-in skills
4. trusted GitHub skills or projects

### Validation Gate

Before adopting a new capability, check:

- relevance to the task
- maintenance recency
- source trustworthiness
- integration cost versus expected benefit

### Separation Of Duties

This matters because the same action should not both change how the system works and decide what becomes long-term memory.

- capability adoption happens during the task
- memory promotion happens later, through Dream Loop review

## Review and Audit

This project deliberately favors reviewer-assisted maintenance instead of a single unchallenged path.

- `capture-memory` stays lightweight and event-oriented
- `capability-evolution` can compare multiple capability options before adoption
- `dream-consolidate` should prefer reviewer or subagent review for promotion, rejection, archive, and conflict decisions
- low-risk cleanup can still use a single-agent fast path

Audit is not a bonus feature. It is what keeps self-improvement trustworthy.

Every meaningful change should preserve enough evidence to answer:

- what source event triggered it
- what path was chosen
- what was rejected and why
- what reviewer disagreed, if any
- how to roll the change back later

## What This Repo Includes

This repo provides the minimum moving parts for a Codex-native improvement loop:

- `skills/capture-memory/`
  - daytime signal capture
  - writes structured observations into `inbox/`
- `skills/capability-evolution/`
  - active-work capability discovery and validation
  - keeps plugins, skills, and GitHub discovery in a controlled order
- `skills/dream-consolidate/`
  - off-hours cleanup, promotion, archive, and reporting
- `templates/`
  - global `AGENTS.md` starter snippet
  - memory structure and projection templates
- `references/`
  - scope, promotion, audit, and capability-evolution design notes
- `automations/`
  - recommended nightly prompts and scheduling ideas

## Core Rules

- active work writes new signal to `inbox/`, not directly to long-term memory
- `capture-memory` stays event-oriented and lightweight
- `capability-evolution` handles discovery and validation, not promotion
- GitHub search is an escalation path, not the default
- third-party capability adoption and material global changes should be surfaced to the user
- only off-hours consolidation should rewrite long-term memory state
- every promotion, merge, archive, rejection, or rollback should be auditable

## Repo Structure

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

## Quick Start

If you want the fastest path, hand this repo to Codex and let it install the pieces for you.

For example:

```text
Install the skills from https://github.com/JY0xLU/codex-native-dream-loop and wire them into my Codex setup.
```

If you want to install manually:

1. Copy `skills/capture-memory/`, `skills/capability-evolution/`, and `skills/dream-consolidate/` into `$CODEX_HOME/skills/` or `~/.codex/skills/`.
2. Copy `templates/global/` into your Codex home as the starter structure.
3. Merge the `AGENTS.md` snippet into your global or project entrypoint.
4. During active work, use `capability-evolution` when the task needs controlled tool or workflow discovery.
5. Use `capture-memory` to record validated high-signal outcomes into `inbox/`.
6. Run `dream-consolidate` during nightly or explicit maintenance passes.
7. Prefer reviewer or subagent review for important promotion and rejection decisions.

## What “Working Well” Should Look Like

The goal is not to make memory bigger. The goal is to make the whole system sharper.

- a new pattern starts as `Observed`
- repeated signal becomes a candidate
- current-phase guidance becomes `ACTIVE.md`
- stable cross-task guidance becomes `LEARNINGS.md`
- one-off capability experiments can stay at reference or trial level without becoming policy
- stale or superseded material gets archived with an explanation trail

When memory stays scoped, capability adoption stays controlled, and promotion stays auditable, Codex can keep improving without becoming messy, brittle, or overconfident.
