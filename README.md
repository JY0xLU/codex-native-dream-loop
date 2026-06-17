<p align="center">
  <img src="assets/hero-logo.png" width="156" alt="Codex Native Dream Loop logo">
</p>

<h1 align="center">Codex Native Dream Loop</h1>

<p align="center">
  Route memory for Codex: keep the winning path visible, reject weak lessons, and keep recall small.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Codex-Native-1f6feb" alt="Codex Native">
  <img src="https://img.shields.io/badge/Plugin-Installable-7c3aed" alt="Installable plugin">
  <img src="https://img.shields.io/badge/Public%20Model-ACTIVE%20%2B%20LEARNINGS-2563eb" alt="ACTIVE plus LEARNINGS">
  <img src="https://img.shields.io/badge/Runtime-Zero%20Server-0f766e" alt="Zero runtime server">
  <img src="https://img.shields.io/badge/Privacy-Local--First-111827" alt="Local first">
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#why-it-exists">Why</a> ·
  <a href="#public-model">Public Model</a> ·
  <a href="#how-the-loop-works">Loop</a> ·
  <a href="#commands">Commands</a> ·
  <a href="README.zh-CN.md">中文</a>
</p>

```bash
git clone https://github.com/JY0xLU/codex-native-dream-loop.git
cd codex-native-dream-loop

codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
```

Codex often forgets which route already worked. Dream Loop gives it a small
operating memory: `ACTIVE.md` for current instructions, `LEARNINGS.md` for
reusable routes, and a validation gate before anything becomes durable.

It is built for people who use Codex across many threads, repos, and days. It
is not a general memory platform, an agent runtime, or a training framework.
The goal is to help Codex start from the winning route next time without
making memory harder to audit.

## Highlights

- **Small public model**: daily recall stays limited to `ACTIVE.md` and `LEARNINGS.md`.
- **Route reuse**: strong lessons become reusable paths, not vague notes.
- **Validation gate**: durable memory changes need source evidence, rejection conditions, and rollback clues.
- **Plugin-first install**: the repo ships a Codex marketplace entry and installable plugin package.
- **Local-first tooling**: install, doctor, report, fixture replay, and forget commands are dependency-free.

## Requirements

- Codex CLI with plugin support for the recommended install path
- Python 3.10+ for local scripts
- A local filesystem-backed Codex home
- No server, database, dashboard, or cloud sync requirement

## Quick Start

```bash
git clone https://github.com/JY0xLU/codex-native-dream-loop.git
cd codex-native-dream-loop

codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
python scripts/doctor.py
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory
```

After installation, start a new Codex thread so the Dream Loop skills are
loaded. The expected first win is simple: Codex should consult the smallest
relevant slice of `ACTIVE.md` and `LEARNINGS.md` before choosing a route.

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

Manual installation copies the three Dream Loop skills, the global starter
template, and the `AGENTS.md` snippet. Keep it as the fallback path when plugin
support is not available.

## Use Cases

- **Recurring repo work**: keep install, test, release, and PR routes from being rediscovered each time.
- **README and release hygiene**: preserve proven publishing preferences without burying them in old threads.
- **Long-running agent preferences**: turn repeated explicit corrections into scoped, auditable behavior.

## Not For

Dream Loop is intentionally narrow. It is not:

- a general vector memory or graph memory product
- an autonomous agent runtime
- a benchmark optimizer or model-training loop
- a cloud memory sync layer

## Why It Exists

The biggest failure after an agent has worked with you for a while is usually
not raw model capability. It is path drift.

- useful routes are rediscovered from scratch
- old lessons stay trapped inside long conversations
- urgent temporary rules linger longer than they should
- promising plugins or skills get found too late
- memory systems add layers faster than they add clarity

Dream Loop exists to make the next run cheaper than the last one.

It does that by keeping only two public memory surfaces:

- `ACTIVE.md`
  - what should change behavior right now
- `LEARNINGS.md`
  - route memory for paths that already proved they win

Everything else stays in the background for review, traceability, and rollback.

## Public Model

Dream Loop deliberately exposes only two daily layers.

### `ACTIVE.md`

`ACTIVE.md` is the hot layer.

Use it for:

- temporary but important rules
- current hot routes
- phase-specific behavior that should influence the next task immediately
- explicit corrections that must change the very next run

If an item stops affecting near-term decisions, it should not stay here.

### `LEARNINGS.md`

`LEARNINGS.md` is the route memory layer.

It uses progressive disclosure: start from the index, choose the relevant
section, and only then read the route entries that match the task.

Each learning is a route entry, not just a generic life lesson. A good entry
answers:

- what kind of task this route fits
- which path should be tried first
- why that path wins
- when it was last validated
- what evidence supports it
- what fallback or avoid condition matters

This makes the system feel less like memory storage and more like route reuse.

```text
Daily recall:
  ACTIVE.md       -> current instructions and hot routes
  LEARNINGS.md    -> proven reusable routes

Review support:
  inbox/          -> unresolved or inferred signal
  staged/         -> proposed memory edits
  rejected/       -> candidates that should not land
  AUDIT_LOG.md    -> promotion, rejection, archive, rollback trace
```

## How The Loop Works

The operating cycle is:

```text
recall -> choose -> search if needed -> execute -> land or quarantine -> consolidate
```

In practice:

1. Read the smallest relevant slice from `ACTIVE.md` and `LEARNINGS.md`.
2. If a known route already fits, reuse it first.
3. If confidence is not high enough, let `capability-evolution` search in order:
   enabled official plugins -> installable official plugins -> local skills -> trusted GitHub projects.
4. Make discovery observable: record searched layers, skipped or blocked layers, selected and rejected candidates, and whether GitHub or external search was reached.
5. Execute with one chosen route, not multiple competing routes.
6. Use `capture-memory` to land explicit strong signal directly into `ACTIVE.md` or `LEARNINGS.md`.
7. Quarantine only unresolved, inferred, or competing signal in `inbox/`.
8. Use `dream-consolidate` off-hours to refresh the hot layer, strengthen route memory, drain unresolved inbox items, and archive stale paths.

The public model stays small even though the internal machinery is still
auditable.

## Example Flow

1. A user corrects Codex: "For this repo, run `python scripts/doctor.py` before publishing."
2. `capture-memory` treats it as explicit strong signal and lands a short `ACTIVE.md` entry.
3. The next related task reads that hot entry before choosing a route.
4. If the route proves useful across several publishing rounds, `dream-consolidate` stages a `LEARNINGS.md` candidate with evidence and a rejection condition.
5. If the route later becomes stale, `memoryctl.py forget` or a consolidation pass moves it out of default recall and leaves an audit trail.

Weak inferred signal follows a different path: it goes to `inbox/`, not straight
to durable memory.

## Validation Gate

Dream Loop validates durable memory changes without importing a heavy
optimization framework.

Before a route, preference, or procedure becomes durable memory, the
maintenance pass should ask:

- what real task, correction, repo audit, or repeated failure supports it
- whether the candidate would have changed the previous outcome for the better
- whether a smaller hot `ACTIVE.md` entry is safer than a durable `LEARNINGS.md` route
- what evidence would reject it, retire it, or send it back to quarantine
- how to roll it back if it later proves wrong

For judgment-heavy changes, `dream-consolidate` should stage a proposal first:
accepted edits, rejected candidates, evidence, reviewer or subagent notes, and
the exact target layer. Staging is an audit artifact, not a third public memory
layer. The day-to-day model remains `ACTIVE.md` and `LEARNINGS.md`.

This keeps Dream Loop as a Codex-native memory maintenance loop: lightweight
enough to read, strict enough to avoid self-reinforcing bad lessons.

## Quality Without Bloat

Dream Loop improves by making route choices sharper, not by adding more public
layers.

- Reuse known routes first.
- Search wider only when confidence is low.
- Keep validation evidence compact.
- Reject candidates that need a large framework to justify a small memory change.
- Archive stale or rejected routes instead of letting them silently disappear.

The system should get faster without becoming harder to understand.

## Core Skills

This repo currently ships three main skills:

| Skill | When Invoked | Changes | Refuses |
| --- | --- |
| `capture-memory` | A correction, proven route, or durable preference appears. | Lands explicit strong signal or quarantines weak signal. | Turning every observation into long-term memory. |
| `capability-evolution` | The known route is not enough. | Checks official plugins, local skills, then trusted external options with evidence. | Claiming discovery happened without showing searched or skipped layers. |
| `dream-consolidate` | A maintenance pass is needed. | Refreshes hot memory, reviews staged proposals, archives stale routes, reports drift. | Silently editing tracked repo files without a human request. |

Together, they support a single idea:

**Reuse the best known route first, and only search wider when needed.**

## Automation

Dream Loop assumes a single recurring automation, not a growing stack of
separate scheduled agents.

That automation should do six things in one pass:

- maintain Dream Loop memory under the dual-layer public model
- audit the current repo or PR round
- check whether installed custom skills still match the automation prompt
- report real reviewer or subagent evidence, or explain a low-risk no-review fast path
- check whether the automation prompt itself has drifted behind the repo
- recommend the next smallest useful round of improvement

It should be strong enough to stay aligned with the repo as the system evolves,
but bounded enough that it only audits and recommends at the repo layer instead
of silently editing tracked files.

## Internal Mechanics

The system still keeps supporting machinery, but it should not become the main
user-facing mental model.

| Area | Purpose |
| --- | --- |
| `inbox/` | Short-lived quarantine buffer for unresolved inferred signal. |
| `staged/` | Proposed edits waiting for judgment before they touch public memory. |
| `rejected/` | Rejected candidates and the reason they did not land. |
| `AUDIT_LOG.md` | Minimal trace for promotion, rejection, archive, and rollback decisions. |
| `ARCHIVE/` | Retired or superseded material kept for traceability. |

These exist to support rollback and review. They are not extra public layers
that people have to reason about every day.

## Commands

```bash
# Structural health check
python scripts/doctor.py

# Generate a maintenance report
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory

# Generate a static HTML report
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory --format html --output report.html

# Replay lightweight report fixtures
python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures

# Remove a recalled entry while preserving a tombstone audit
python scripts/memoryctl.py forget LRN-YYYYMMDD-001 --memory-root ~/.codex/memory --reason "no longer valid"
```

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

## Docs Map

- [CHANGELOG.md](CHANGELOG.md) - release notes and notable changes
- [references/](references/) - design notes for scope, validation, automation, and capability evolution
- [templates/global/](templates/global/) - starter memory and AGENTS snippet
- [plugins/codex-native-dream-loop/](plugins/codex-native-dream-loop/) - marketplace-ready plugin package
## Contributing

Keep changes aligned with the small public model:

- do not add a new public memory layer unless the workflow genuinely requires it
- keep examples concrete and source-backed
- run `python scripts/doctor.py` and fixture replay before publishing
- keep plugin install instructions and manual fallback in sync

## What Good Looks Like

Dream Loop is working well when:

- the next task starts from an existing winning route instead of from zero
- `ACTIVE.md` stays short and obviously current
- `LEARNINGS.md` reads like a library of reusable routes, not a graveyard of vague rules
- explicit corrections and durable preferences land quickly instead of sitting in `inbox/`
- plugins and skills are discovered proactively when needed
- rejected or stale paths are archived instead of silently disappearing
- the system gets faster without becoming more confusing

## Status

Dream Loop's core loop is complete: plugin installation, manual installation,
doctor checks, maintenance reports, fixture replay, and forget/audit flow are
in place. Future work is refinement: more fixture coverage, sharper report
output, and clearer examples for `ACTIVE.md`, `LEARNINGS.md`, and `inbox/`
decisions.

## License

MIT. See [LICENSE](LICENSE).
