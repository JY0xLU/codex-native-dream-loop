# Codex Improving

[中文](README.zh-CN.md) | English

> A Codex-native workflow for structured memory, review, and nightly consolidation.

![Codex Improving hero](assets/hero-subagent-control-mesh.svg)

- Capture during work
- Consolidate off-hours
- Review with subagents

## What It Solves

Most AI memory setups break in one of two ways:

1. They mix stable rules, temporary context, mistakes, and future ideas into one blob.
2. They try to rewrite long-term memory while the agent is still solving the current task.

`codex-improving` takes the opposite path. It keeps capture and consolidation separate, treats `AGENTS.md` as a stable entrypoint, and pushes important promotion or rejection decisions through review instead of silent rewrites.

This project is not trying to turn Codex into another Claude Code. It uses Codex's native building blocks as the execution substrate:

- `AGENTS.md`
- skills
- automations
- worktrees
- sandbox and permissions
- subagents

## How It Works

![Dream Loop flow](assets/dream-loop-flow.svg)

The operating loop is simple:

- capture high-signal observations during active work
- store them in `inbox/` without touching long-term memory
- run nightly review and consolidation
- promote only repeated, generalizable, actionable items
- keep every decision auditable

### Memory Layers

| Layer | Purpose |
| --- | --- |
| `AGENTS.md` | Stable operating rules and entrypoint guidance |
| `inbox/` | Append-only capture stream |
| `ACTIVE.md` | Short-term but operationally important guidance |
| `LEARNINGS.md` | Stable cross-task lessons |
| `FEATURE_REQUESTS.md` | Future capability gaps and automation ideas |

### Review Model

- `capture-memory` stays lightweight and single-agent by default
- `dream-consolidate` prefers subagent cross-review for promotion, rejection, archive, and conflict decisions
- low-risk cleanup may still use a single-agent fast path
- `AGENTS.md` must never be auto-edited

## What's Included

- [`skills/capture-memory/`](skills/capture-memory/SKILL.md)
  Daytime capture for corrections, repeated failures, stable preferences, and reusable workflow wins.
- [`skills/dream-consolidate/`](skills/dream-consolidate/SKILL.md)
  Nightly review for deduplication, expiry handling, promotion, and audit output.
- [`templates/global/`](templates/global/AGENTS.snippet.md)
  Starter `AGENTS.md` snippet and global-memory setup pieces.
- [`automations/`](automations/nightly-dream-loop.md)
  Recommended nightly automation prompt and schedule.
- [`examples/minimal-global/`](examples/minimal-global/nightly-report-example.md)
  Small example of what a Dream Loop report can look like.
- [`references/`](references/promotion-rules.md)
  Supporting notes for promotion rules, scope, audit, evals, and automation design.

## Quick Start

1. Copy `skills/capture-memory/` and `skills/dream-consolidate/` into `$CODEX_HOME/skills/` or `~/.codex/skills/`.
2. Copy the global templates into your Codex home and wire the snippet into your `AGENTS.md` entrypoint.
3. Use `capture-memory` during active work to append signal into `inbox/`.
4. Run `dream-consolidate` on a nightly automation and review the generated report before trusting promotions.

## In Practice

One practical example:

1. A user corrects a repeated workflow mistake.
2. `capture-memory` writes the observation into `inbox/`.
3. Nightly consolidation reviews similar evidence, often with a reviewer subagent.
4. If the pattern is stable and reusable, it is promoted into `ACTIVE.md` or `LEARNINGS.md`.
5. The report records what changed, what was rejected, and why.

## Project Notes

- This repo is intentionally small and documentation-first.
- The goal is to provide a disciplined Dream Loop workflow, not a giant platform.
- If you want to adapt it for a larger team setup, start with the templates and review model before expanding the automation surface.

## License

[MIT](LICENSE)
