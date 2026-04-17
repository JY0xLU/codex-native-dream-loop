# Codex Native Dream Loop

[中文](README.zh-CN.md) | English

![Codex Native Dream Loop logo](assets/hero-logo.png)

**A Codex-native memory and self-evolution system: memory capture, route reuse, capability evolution, and off-hours consolidation working together behind a small public interface.**

Codex Native Dream Loop is for people who want Codex to get stronger through repeated work without turning memory into a maze. The goal is not just to expose fewer layers. The goal is to combine memory, self-evolution, and execution optimization so Codex can reuse the best path faster the next time.

![Codex Native](https://img.shields.io/badge/Codex-Native-1f6feb)
![Self-Improving](https://img.shields.io/badge/Self--Improving-3fb950)
![Dual Layer Model](https://img.shields.io/badge/Public%20Model-Dual%20Layer-2563eb)
![Path Memory](https://img.shields.io/badge/Path%20Memory-Reuse-0f766e)
![Auditable](https://img.shields.io/badge/Auditable-111827)

**Quick Navigation**

[Why It Exists](#why-it-exists) | [Public Model](#public-model) | [How The Loop Works](#how-the-loop-works) | [Core Skills](#core-skills) | [Automation](#automation) | [Internal Mechanics](#internal-mechanics) | [Quick Start](#quick-start)

> Most agents do not really improve. They either keep re-solving the same problem, or they bury themselves under too much memory structure.
> Codex Native Dream Loop keeps the public model small, reuses good routes, and hides the bookkeeping behind the scenes.

## Why It Exists

The biggest failure after an agent has worked with you for a while is usually not raw model capability. It is path drift.

- useful routes are rediscovered from scratch
- old lessons stay trapped inside long conversations
- urgent temporary rules linger longer than they should
- promising plugins or skills get found too late
- memory systems add layers faster than they add clarity

This repo exists to make the next run cheaper than the last one.

It does that by pairing a broader self-evolution loop with a small public memory surface:

- `ACTIVE.md`
  - what should change behavior right now
- `LEARNINGS.md`
  - route memory for paths that already proved they win

Everything else stays in the background.

## Public Model

This repo deliberately exposes only two public layers, even though the full system also includes capability evolution, capture, consolidation, and audit.

### `ACTIVE.md`

`ACTIVE.md` is the hot layer.

Use it for:

- temporary but important rules
- current hot routes
- phase-specific behavior that should influence the next task immediately

If an item stops affecting near-term decisions, it should not stay here.

### `LEARNINGS.md`

`LEARNINGS.md` is the path memory layer.

It is route memory, not an "active-learning" loop.

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

`recall -> choose -> search if needed -> execute -> capture -> consolidate`

In practice:

1. Read the smallest relevant slice from `ACTIVE.md` and `LEARNINGS.md`.
2. If a known route already fits, reuse it first.
3. If confidence is not high enough, let `capability-evolution` search in order:
   enabled official plugins -> installable official plugins -> local skills -> trusted GitHub projects.
4. Execute with one chosen route, not multiple competing routes.
5. Use `capture-memory` to record only the high-signal result or blocker.
6. Use `dream-consolidate` off-hours to keep `ACTIVE.md` hot, strengthen `LEARNINGS.md`, and archive stale paths.

The public model stays small even though the internal machinery is still auditable.

## Core Skills

This repo currently ships three main skills:

- `capture-memory`
  - lightweight event capture during active work
- `capability-evolution`
  - route discovery, validation, and capability selection
- `dream-consolidate`
  - off-hours cleanup, hot-layer refresh, route promotion, and audit reporting

Together, they support a single idea:

**reuse the best known route first, and only search wider when needed.**

## Automation

This repo assumes a single recurring automation, not a growing stack of separate scheduled agents.

That automation should do four things in one pass:

- maintain Dream Loop memory under the dual-layer public model
- audit the current repo and PR round
- check whether the automation prompt itself has drifted behind the repo
- recommend the next smallest useful round of improvement

It should be strong enough to stay aligned with the repo as the system evolves, but bounded enough that it only audits and recommends at the repo layer instead of silently editing tracked files.

## Internal Mechanics

The system still keeps some internal machinery, but it should not become the main user-facing mental model.

Internal support mechanisms include:

- `inbox/`
  - append-only capture buffer for raw signal
- `AUDIT_LOG.md`
  - minimal trail for promotion, rejection, archive, and rollback decisions
- `ARCHIVE/`
  - retired or superseded material kept for traceability

These exist to support rollback and review. They are not meant to become extra public layers that people have to reason about every day.

## What This Repo Includes

- `templates/`
  - a global `AGENTS.md` starter snippet
  - a minimal memory skeleton centered on `ACTIVE.md` and `LEARNINGS.md`
- `skills/`
  - the three skills that run the loop
- `automations/`
  - the single recurring automation prompt for memory maintenance, repo round audit, drift check, and next-round recommendations
- `references/`
  - concise design notes for route memory, promotion, and automation behavior
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
6. Use `capture-memory` only for high-signal results.
7. Run the single recurring Dream Loop automation off-hours to refresh the hot layer, audit the current repo/PR state, check prompt drift, and recommend the next round.

## What “Good” Looks Like

This repo is working well when:

- the next task starts from an existing winning route instead of from zero
- `ACTIVE.md` stays short and obviously current
- `LEARNINGS.md` reads like a library of reusable routes, not a graveyard of vague rules
- plugins and skills are discovered proactively when needed
- rejected or stale paths are archived instead of silently disappearing
- the system gets faster without becoming more confusing
