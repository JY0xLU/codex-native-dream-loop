<p align="center">
  <img src="assets/hero-logo.png" width="144" alt="Codex Native Dream Loop logo">
</p>

<h1 align="center">Codex Native Dream Loop</h1>

<p align="center">
  A local-first route memory layer for Codex.
  <br>
  Keep the path that worked, reject weak lessons, and start the next thread from evidence.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Codex-Native-1f6feb" alt="Codex Native">
  <img src="https://img.shields.io/badge/Plugin-Installable-7c3aed" alt="Installable plugin">
  <img src="https://img.shields.io/badge/Memory-ACTIVE%20%2B%20LEARNINGS-2563eb" alt="ACTIVE plus LEARNINGS">
  <img src="https://img.shields.io/badge/Runtime-Zero%20Server-0f766e" alt="Zero runtime server">
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#why-it-exists">Why</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#commands">Commands</a> ·
  <a href="README.zh-CN.md">中文</a>
</p>

```bash
codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
```

Dream Loop is for people who use Codex across many threads, repositories, and
days. It gives Codex a small operating memory: `ACTIVE.md` for what matters
right now, `LEARNINGS.md` for reusable winning routes, and a promotion gate
before anything becomes durable.

It is not a memory database, an agent runtime, or a model-training framework.
It is the missing housekeeping layer between "Codex solved this once" and
"Codex should start from that route next time."

## What You Get

| Surface | Purpose |
| --- | --- |
| `ACTIVE.md` | Hot instructions and current routes that should affect the next task. |
| `LEARNINGS.md` | Durable route memory with evidence, scope, rejection conditions, and rollback clues. |
| `inbox/` | Short-lived quarantine for weak or inferred signal. |
| `staged/` | Reviewable proposals before a memory change becomes durable. |
| `reports/` | Maintenance summaries for stale hot entries, rejected routes, fixtures, and coverage. |

The public model stays small on purpose. Most tasks should only need a relevant
slice of `ACTIVE.md` and `LEARNINGS.md`.

## Install

### Codex Plugin

From a local checkout:

```bash
git clone https://github.com/JY0xLU/codex-native-dream-loop.git
cd codex-native-dream-loop

codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
codex plugin list
```

Expected status:

```text
codex-native-dream-loop@codex-native-dream-loop  installed, enabled
```

The repository ships a marketplace-ready plugin package at
`plugins/codex-native-dream-loop/`, wired by `.agents/plugins/marketplace.json`.
Start a new Codex thread after installation so the skills load cleanly.

### Manual File Copy

Use this when plugin support is unavailable or when you want to inspect the
copy plan first:

```bash
python scripts/install.py --codex-home ~/.codex
python scripts/install.py --codex-home ~/.codex --apply
```

Windows PowerShell:

```powershell
python scripts/install.py --codex-home "$env:USERPROFILE\.codex"
python scripts/install.py --codex-home "$env:USERPROFILE\.codex" --apply
```

## Why It Exists

Long-running Codex work usually fails by path drift, not by raw capability:

- the same install, debug, or publish path gets rediscovered from scratch
- useful corrections stay buried in old conversations
- temporary rules keep affecting new work after they expire
- plugin and skill discovery happens too late
- memory grows faster than a human can audit it

Dream Loop makes the next run cheaper than the last one. It keeps known-good
routes visible, forces weak lessons to wait, and leaves enough audit trail to
undo a bad promotion.

## How It Works

```text
recall -> choose route -> execute -> capture signal -> consolidate
```

1. Read only the relevant slices of `ACTIVE.md` and `LEARNINGS.md`.
2. Reuse a known winning route when it clearly fits.
3. Search wider only when confidence is low.
4. Capture explicit strong signal directly into the right layer.
5. Keep inferred or competing signal in `inbox/` until review.
6. Promote durable memory only after the validation gate passes.
7. Run consolidation to archive stale routes and keep the public model small.

This keeps day-to-day recall simple while still making maintenance auditable.

## Promotion Gate

A durable learning should answer five questions before it lands in
`LEARNINGS.md`:

| Gate | Question |
| --- | --- |
| Evidence | What task, correction, or repeated failure supports it? |
| Impact | What becomes faster, safer, or more reliable? |
| Scope | Which repo, workflow, tool, or task class does it apply to? |
| Stop condition | When should Codex stop using this route? |
| Rollback clue | What should future maintenance remove or replace if it fails? |

This is the difference between route memory and vague advice. A good entry is
specific enough to reuse and bounded enough to reject.

## Commands

```bash
# Structural health check
python scripts/doctor.py

# Generate a maintenance report
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory

# Replay lightweight report fixtures
python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures

# Remove a recalled entry while preserving a tombstone audit
python scripts/memoryctl.py forget LRN-YYYYMMDD-001 --memory-root ~/.codex/memory --reason "no longer valid"
```

## Skills

| Skill | Role |
| --- | --- |
| `capture-memory` | Land explicit strong signal or quarantine unresolved inferred signal. |
| `capability-evolution` | Discover and validate better tools in a controlled order. |
| `dream-consolidate` | Review hot memory, staged proposals, reports, drift, archives, and next actions. |

## Repository Layout

```text
.
|-- .agents/plugins/marketplace.json
|-- .codex-plugin/plugin.json
|-- plugins/codex-native-dream-loop/
|   |-- .codex-plugin/plugin.json
|   |-- assets/
|   `-- skills/
|-- skills/
|   |-- capture-memory/
|   |-- capability-evolution/
|   `-- dream-consolidate/
|-- scripts/
|   |-- doctor.py
|   |-- install.py
|   |-- memoryctl.py
|   `-- nightly_report.py
|-- references/
|-- templates/global/
|-- tests/
|-- README.md
`-- README.zh-CN.md
```

The root `.codex-plugin/plugin.json` is the source manifest used by repository
validation. The packaged copy under `plugins/codex-native-dream-loop/` is the
installable plugin exposed through the marketplace file.

## Design Principles

- **Small public model**: daily recall stays limited to `ACTIVE.md` and `LEARNINGS.md`.
- **Route-first memory**: store reusable paths, not generic summaries.
- **Evidence before durability**: strong signal can land; weak signal waits.
- **Local-first operation**: no server, database, or dashboard required.
- **Auditable maintenance**: promotion, rejection, archive, and rollback leave a trail.

## Status

Dream Loop's core loop is complete: plugin installation, manual installation,
doctor checks, maintenance reports, fixture replay, and forget/audit flow are
in place. Future work is refinement: more fixture coverage, sharper report
output, and clearer examples for `ACTIVE.md`, `LEARNINGS.md`, and `inbox/`
decisions.

## License

MIT. See [LICENSE](LICENSE).
