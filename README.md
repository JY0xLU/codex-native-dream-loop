# Codex Native Dream Loop

[中文](README.zh-CN.md) | English

![Codex Native Dream Loop logo](assets/hero-logo.png)

**A Codex-native route memory governance layer with a simple public model: `ACTIVE.md` for what is hot now, `LEARNINGS.md` for reusable winning routes.**

Codex forgets which routes you already proved. Dream Loop keeps the useful routes visible, rejects weak lessons, and makes each night of consolidation auditable.

It is for high-frequency Codex users who repeat workflows across threads, repos, and days. It is not a general memory platform and not a model-training framework. The goal is to help Codex start from the winning route next time without turning memory into a maze.

![Codex Native](https://img.shields.io/badge/Codex-Native-1f6feb)
![Self-Improving](https://img.shields.io/badge/Self--Improving-3fb950)
![Dual Layer Model](https://img.shields.io/badge/Public%20Model-Dual%20Layer-2563eb)
![Path Memory](https://img.shields.io/badge/Path%20Memory-Reuse-0f766e)
![Auditable](https://img.shields.io/badge/Auditable-111827)

**Quick Navigation**

[Why It Exists](#why-it-exists) | [Public Model](#public-model) | [How The Loop Works](#how-the-loop-works) | [Validation Gate](#validation-gate) | [Core Skills](#core-skills) | [Automation](#automation) | [Internal Mechanics](#internal-mechanics) | [Quick Start](#quick-start)

> Most agents do not really improve. They either keep re-solving the same problem, or they bury themselves under too much memory structure.
> Codex Native Dream Loop keeps the public model small, validates durable changes, and hides the bookkeeping behind the scenes.

## Why It Exists

The biggest failure after an agent has worked with you for a while is usually not raw model capability. It is path drift.

- useful routes are rediscovered from scratch
- old lessons stay trapped inside long conversations
- urgent temporary rules linger longer than they should
- promising plugins or skills get found too late
- memory systems add layers faster than they add clarity

This repo exists to make the next run cheaper than the last one.

It does that by keeping only two public memory surfaces:

- `ACTIVE.md`
  - what should change behavior right now
- `LEARNINGS.md`
  - route memory for paths that already proved they win

Everything else stays in the background.

## Public Model

This repo deliberately exposes only two public layers.

### `ACTIVE.md`

`ACTIVE.md` is the hot layer.

Use it for:

- temporary but important rules
- current hot routes
- phase-specific behavior that should influence the next task immediately

If an item stops affecting near-term decisions, it should not stay here.

### `LEARNINGS.md`

`LEARNINGS.md` is the path memory layer.

It uses progressive disclosure: start from the index, choose the relevant section, and only then read the specific route entries that match the task.

Each learning is a route entry, not just a generic life lesson. A good entry answers:

- what kind of task this route fits
- which path should be tried first
- why that path wins
- when it was last validated
- what evidence supports it
- what fallback or avoid condition matters

This makes the system feel less like “memory storage” and more like “route reuse.”

## How The Loop Works

The operating cycle is:

`recall -> choose -> search if needed -> execute -> land or quarantine -> consolidate`

In practice:

1. Read the smallest relevant slice from `ACTIVE.md` and `LEARNINGS.md`.
2. If a known route already fits, reuse it first.
3. If confidence is not high enough, let `capability-evolution` search in order:
   enabled official plugins -> installable official plugins -> local skills -> trusted GitHub projects.
4. Make discovery observable: record searched layers, skipped or blocked layers, selected and rejected candidates, and whether GitHub or external search was reached.
5. Execute with one chosen route, not multiple competing routes.
6. Use `capture-memory` to land explicit strong signal directly into `ACTIVE.md` or `LEARNINGS.md`, and only quarantine unresolved inferred signal in `inbox/`.
7. Use `dream-consolidate` off-hours to keep `ACTIVE.md` hot, strengthen `LEARNINGS.md`, drain unresolved inbox items, and archive stale paths.

The public model stays small even though the internal machinery is still auditable.

## Validation Gate

Dream Loop borrows the discipline of validation-gated skill improvement without importing a heavy training framework.

Before a route, preference, or procedure becomes durable memory, the maintenance pass should ask:

- what real task, correction, repo audit, or repeated failure supports it
- whether the candidate would have changed the previous outcome for the better
- whether a smaller hot `ACTIVE.md` entry is safer than a durable `LEARNINGS.md` route
- what evidence would reject it, retire it, or send it back to quarantine
- how to roll it back if it later proves wrong

For judgment-heavy changes, `dream-consolidate` should stage a proposal first: accepted edits, rejected candidates, evidence, reviewer or subagent notes, and the exact target layer. Staging is an audit artifact, not a third public memory layer. The day-to-day model remains `ACTIVE.md` and `LEARNINGS.md`.

This keeps Dream Loop closer to a route-memory operating system than a research optimizer: lightweight enough to read, strict enough to avoid self-reinforcing bad lessons.

## Quality Without Bloat

Dream Loop improves by making route choices sharper, not by adding more public layers. Reuse known routes first, require observable discovery only when confidence is low, keep validation evidence compact, and reject candidates that need a large framework to justify a small memory change.

Implementation rounds can use the [Trellis workflow](references/trellis-workflow.md): keep one trunk objective, split independent branches for docs/skills/automation/verification, use subagents on side branches, and land only after the gate has evidence.

## Core Skills

This repo currently ships three main skills:

- `capture-memory`
  - direct landing for explicit strong signal, plus quarantine for unresolved inferred signal
- `capability-evolution`
  - route discovery, validation, capability selection, and observable search evidence
- `dream-consolidate`
  - off-hours cleanup, hot-layer refresh, route promotion, and audit reporting

Together, they support a single idea:

**reuse the best known route first, and only search wider when needed.**

## Automation

This repo assumes a single recurring automation, not a growing stack of separate scheduled agents.

That automation should do six things in one pass:

- maintain Dream Loop memory under the dual-layer public model
- audit the current repo and PR round
- check whether installed custom skills still match the automation prompt
- report real reviewer/subagent evidence or explain a low-risk no-review fast path
- check whether the automation prompt itself has drifted behind the repo
- recommend the next smallest useful round of improvement

It should be strong enough to stay aligned with the repo as the system evolves, but bounded enough that it only audits and recommends at the repo layer instead of silently editing tracked files.

## Internal Mechanics

The system still keeps some internal machinery, but it should not become the main user-facing mental model.

Internal support mechanisms include:

- `inbox/`
  - short-lived quarantine buffer only for unresolved inferred signal
- `AUDIT_LOG.md`
  - minimal trail for promotion, rejection, archive, and rollback decisions
- `ARCHIVE/`
  - retired or superseded material kept for traceability

These exist to support rollback and review. They are not meant to become extra public layers that people have to reason about every day.

## What This Repo Includes

- `templates/`
  - a global `AGENTS.md` starter snippet
  - a minimal memory skeleton centered on `ACTIVE.md` and `LEARNINGS.md`
- `.codex-plugin/`
  - a Codex plugin manifest for direct plugin registration
- `skills/`
  - the three skills that run the loop
- `automations/`
  - the single recurring automation prompt for memory maintenance, repo round audit, drift check, and next-round recommendations
- `references/`
  - concise design notes for route memory, promotion, and automation behavior
  - a research adoption trace showing which external projects influenced which mechanisms
- `scripts/`
  - dependency-free local checks for repo structure and install readiness
- `examples/`
  - a minimal global example using the dual-layer public model

## Quick Start

If you want the fastest setup, give this repo to Codex and let it wire the pieces into your Codex home.

For example:

```text
Install the skills from https://github.com/JY0xLU/codex-native-dream-loop and wire them into my Codex setup.
```

If you want to install it manually:

1. Copy `skills/capture-memory/`, `skills/capability-evolution/`, and `skills/dream-consolidate/` into `$CODEX_HOME/skills/` or `~/.codex/skills/`.
2. Copy `templates/global/` into your Codex home as the starter structure.
3. Merge the `AGENTS.md` snippet into your global or project entrypoint.
4. During work, rely on `ACTIVE.md` first and `LEARNINGS.md` second.
5. Use `capability-evolution` when you need to search for a better route.
6. Use `capture-memory` to land explicit strong signal immediately and quarantine only unresolved inferred signal.
7. Run the single recurring Dream Loop automation off-hours to refresh the hot layer, drain unresolved inbox items, audit the current repo/PR state, check custom-skill alignment and prompt drift, report real reviewer evidence, and recommend the next round.

If your Codex build supports local plugin registration, this repo also includes `.codex-plugin/plugin.json`. Keep the manual path as the fallback while plugin packaging continues to evolve.

For a dry-run manual install:

```bash
python scripts/install.py --codex-home ~/.codex
```

To copy files after reviewing the planned actions:

```bash
python scripts/install.py --codex-home ~/.codex --apply
```

To verify the repo structure before installing or publishing:

```bash
python scripts/doctor.py
```

To generate a compact maintenance report from a Dream Loop memory root:

```bash
python scripts/nightly_report.py --memory-root templates/global/.codex/memory
```

To run the lightweight fixture replay check:

```bash
python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures
```

For a static HTML report:

```bash
python scripts/nightly_report.py --memory-root templates/global/.codex/memory --format html --output report.html
```

To remove an entry from default recall while preserving a tombstone audit:

```bash
python scripts/memoryctl.py forget LRN-YYYYMMDD-001 --memory-root ~/.codex/memory --reason "user requested removal"
```

## What “Good” Looks Like

This repo is working well when:

- the next task starts from an existing winning route instead of from zero
- `ACTIVE.md` stays short and obviously current
- `LEARNINGS.md` reads like a library of reusable routes, not a graveyard of vague rules
- explicit corrections and durable preferences land quickly instead of sitting in `inbox/`
- plugins and skills are discovered proactively when needed
- rejected or stale paths are archived instead of silently disappearing
- the system gets faster without becoming more confusing
