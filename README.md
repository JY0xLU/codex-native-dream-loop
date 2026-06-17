<div align="center" id="readme-top">

<img src="assets/hero-logo.png" width="220" alt="Codex Native Dream Loop logo">

# Codex Native Dream Loop

**Local-first route memory for Codex.**

Two-file recall surface, audited promotion workflow, and a Codex plugin path for keeping the winning route visible across threads.

<p align="center">
  <img src="https://img.shields.io/badge/Codex-Native-1f6feb?style=for-the-badge" alt="Codex Native">
  <img src="https://img.shields.io/badge/Public_Model-ACTIVE_%2B_LEARNINGS-2563eb?style=for-the-badge" alt="ACTIVE plus LEARNINGS">
  <img src="https://img.shields.io/badge/Local_First-Zero_Runtime_Server-0f766e?style=for-the-badge" alt="Local first">
  <img src="https://img.shields.io/badge/Plugin-Installable-7c3aed?style=for-the-badge" alt="Installable plugin">
  <img src="https://img.shields.io/badge/License-MIT-111827?style=for-the-badge" alt="MIT license">
</p>

[Quick Start](#quick-start) · [Plugin Installation](#plugin-installation) · [Architecture](#architecture-at-a-glance) · [中文](README.zh-CN.md)

</div>

<br>

<details>
  <summary><kbd>Table of Contents</kbd></summary>

<br>

- [Codex Native Dream Loop 0.1](#codex-native-dream-loop-01)
- [What It Is](#what-it-is)
- [Why It Exists](#why-it-exists)
- [Design Choices](#design-choices)
- [Quick Start](#quick-start)
- [Plugin Installation](#plugin-installation)
- [Manual File-Copy Installation](#manual-file-copy-installation)
- [Architecture At A Glance](#architecture-at-a-glance)
- [Memory Layout](#memory-layout)
- [Core Skills](#core-skills)
- [Promotion Gate](#promotion-gate)
- [Maintenance Commands](#maintenance-commands)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)

<br>

</details>

## Codex Native Dream Loop 0.1

> [!IMPORTANT]
>
> Dream Loop is for people who run Codex repeatedly across threads,
> repositories, and days. It keeps memory small enough to read, strict enough
> to audit, and practical enough to install as a Codex plugin.
>
> The public model is intentionally tiny: `ACTIVE.md` is the hot layer, and
> `LEARNINGS.md` is the reusable route library. Everything else supports
> review, staging, rejection, replay, reporting, and rollback.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## What It Is

Codex can preserve conversation context but still lose the route that actually
worked. Dream Loop gives Codex a disciplined operating memory:

<table>
<tr>
<td width="33%" valign="top">
<strong>ACTIVE.md</strong><br><br>
The hot layer. Short-lived directives, current repository routes, active
corrections, and anything that should affect the next task immediately.
</td>
<td width="33%" valign="top">
<strong>LEARNINGS.md</strong><br><br>
The route library. Durable, reusable paths with evidence, scope, failure
conditions, and a reason to be tried first.
</td>
<td width="33%" valign="top">
<strong>Promotion Gate</strong><br><br>
The control point before a lesson becomes durable. It checks source evidence,
outcome impact, blast radius, rejection condition, and rollback clue.
</td>
</tr>
<tr>
<td width="33%" valign="top">
<strong>Staging Area</strong><br><br>
Judgment-heavy proposals can wait in <code>staged/</code> with accepted edits,
rejected candidates, reviewer notes, and target layer.
</td>
<td width="33%" valign="top">
<strong>Replay Fixtures</strong><br><br>
Small YAML fixtures keep the loop honest without turning the repository into
a benchmark framework.
</td>
<td width="33%" valign="top">
<strong>Maintenance Reports</strong><br><br>
Reports summarize unresolved inbox items, staged proposals, rejected routes,
stale active entries, fixtures, and source-trace coverage.
</td>
</tr>
</table>

It is not a general memory database, not an agent runtime, and not a model
training framework. It is a compact governance layer for Codex route memory.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Why It Exists

The recurring failure mode in long-running Codex work is path drift:

- the same setup, debug, or publishing route is rediscovered from scratch
- useful corrections stay buried in long conversations
- temporary rules stay hot after they stop mattering
- plugin and skill discovery happens too late
- memory grows faster than the operator can audit it

Dream Loop keeps the recall surface small while making the supporting machinery
auditable. The next run should begin from the best known route, not another
blank reasoning pass.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Design Choices

<table>
<tr>
<th width="30%">Choice</th>
<th width="35%">Dream Loop</th>
<th width="35%">Avoids</th>
</tr>
<tr>
<td><strong>Public memory model</strong></td>
<td>Two readable files: <code>ACTIVE.md</code> and <code>LEARNINGS.md</code></td>
<td>Daily recall spread across many opaque layers</td>
</tr>
<tr>
<td><strong>Durable lessons</strong></td>
<td>Promoted only with evidence, scope, rejection condition, and rollback clue</td>
<td>Generic advice that silently changes unrelated future behavior</td>
</tr>
<tr>
<td><strong>Weak signal handling</strong></td>
<td>Unresolved or inferred signal stays short-lived in <code>inbox/</code></td>
<td>Letting every observation become long-term memory</td>
</tr>
<tr>
<td><strong>Automation</strong></td>
<td>One recurring maintenance pass for memory, repo audit, drift check, and next action</td>
<td>A growing set of overlapping scheduled agents</td>
</tr>
<tr>
<td><strong>Tooling</strong></td>
<td>Dependency-free scripts for install, doctor, report, replay, and forget</td>
<td>Mandatory servers, databases, dashboards, or cloud services</td>
</tr>
<tr>
<td><strong>Plugin path</strong></td>
<td>Ships a Codex plugin package and repo-local marketplace file</td>
<td>Forcing users to copy skill folders before trying the system</td>
</tr>
</table>

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Quick Start

Install the plugin, verify the repository, and run one local maintenance report.

### 0. Prerequisites

- Codex CLI with plugin support
- Python 3.10+
- A local checkout of this repository

### 1. Install as a Codex plugin

From the repository root:

```bash
codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
codex plugin list
```

You should see `codex-native-dream-loop` listed as installed and enabled. Start
a new Codex thread after installation so the plugin skills are loaded cleanly.

### 2. Verify the repo

```bash
python scripts/doctor.py
```

Expected result:

```text
Dream Loop doctor: OK
Severity: must checks passed
```

### 3. Generate a report

```bash
python scripts/nightly_report.py --memory-root examples/minimal-global/.codex/memory
```

### 4. Replay fixtures

```bash
python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures
```

Expected result:

```text
Replay fixtures: 5/5
```

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Plugin Installation

The repository contains a marketplace-ready plugin package:

- `.agents/plugins/marketplace.json` - repo-local marketplace entry
- `plugins/codex-native-dream-loop/.codex-plugin/plugin.json` - installable plugin manifest
- `plugins/codex-native-dream-loop/skills/` - bundled Dream Loop skills
- `plugins/codex-native-dream-loop/assets/` - plugin logo and composer icon

Clone and install:

```bash
git clone https://github.com/JY0xLU/codex-native-dream-loop.git
cd codex-native-dream-loop
codex plugin marketplace add .
codex plugin add codex-native-dream-loop@codex-native-dream-loop
```

Confirm:

```bash
codex plugin list
```

Update after pulling new changes:

```bash
git pull
codex plugin remove codex-native-dream-loop
codex plugin add codex-native-dream-loop@codex-native-dream-loop
```

The root `.codex-plugin/plugin.json` is kept as the source manifest used by
repository validation. The packaged copy under `plugins/codex-native-dream-loop/`
is the path exposed through the marketplace file.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Manual File-Copy Installation

Use manual installation when plugin support is unavailable or when you want to
inspect every copied file first.

Dry run:

```bash
python scripts/install.py --codex-home ~/.codex
```

Windows PowerShell:

```powershell
python scripts/install.py --codex-home "$env:USERPROFILE\.codex"
```

Apply the copy plan:

```bash
python scripts/install.py --codex-home ~/.codex --apply
```

Manual installation copies:

- `skills/capture-memory/`
- `skills/capability-evolution/`
- `skills/dream-consolidate/`
- `templates/global/`
- the global `AGENTS.md` starter snippet

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Architecture At A Glance

```text
Codex task thread
  recall -> choose route -> execute -> capture signal
        |
        v
Public route memory
  ACTIVE.md + LEARNINGS.md
        |
        v
Governance artifacts
  inbox / staged / rejected / archive / audit
        |
        v
Maintenance tools
  doctor / report / replay / forget / install
```

Even when governance artifacts grow, the public model stays small. Ordinary
tasks only need the relevant slices of `ACTIVE.md` and `LEARNINGS.md`; maintenance
commands inspect the supporting directories.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Memory Layout

```text
.codex/memory/
|-- ACTIVE.md                 # current hot behavior and routes
|-- LEARNINGS.md              # durable reusable route memory
|-- AUDIT_LOG.md              # promotion, rejection, archive, rollback trace
|-- inbox/                    # unresolved inferred signal
|-- staged/                   # proposals waiting for judgment
|-- rejected/                 # rejected candidates and reasons
|-- fixtures/                 # lightweight replay expectations
|-- reports/                  # maintenance reports
`-- ARCHIVE/                  # retired or superseded material
```

Only `ACTIVE.md` and `LEARNINGS.md` are the daily recall surface. Everything
else is there for review, traceability, and maintenance.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Core Skills

<table>
<tr>
<th width="28%">Skill</th>
<th width="36%">Responsibility</th>
<th width="36%">Use When</th>
</tr>
<tr>
<td><code>capture-memory</code></td>
<td>Land explicit strong signal or quarantine unresolved inferred signal.</td>
<td>A user correction, repeated failure, proven route, or durable preference appears.</td>
</tr>
<tr>
<td><code>capability-evolution</code></td>
<td>Discover and validate better capabilities in a controlled order.</td>
<td>Local routes are insufficient and plugins, skills, or trusted projects may improve the task.</td>
</tr>
<tr>
<td><code>dream-consolidate</code></td>
<td>Review hot memory, staged proposals, archives, reports, drift, and next actions.</td>
<td>A scheduled or manual Dream Loop maintenance pass is needed.</td>
</tr>
</table>

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Promotion Gate

A durable learning should answer five questions before it lands in
`LEARNINGS.md`:

| Gate | Question |
| --- | --- |
| Source evidence | Where did the signal come from? |
| Outcome impact | What became faster, safer, or more reliable? |
| Scope | Which workspace, repo, tool, or task class does it apply to? |
| Rejection condition | When should Codex stop using this route? |
| Rollback clue | What should future maintenance remove or replace if it fails? |

Example durable entry shape:

```md
- For README and GitHub-facing presentation work, keep the public page visual,
  plugin-installable, and concrete about verification.
  scope: public repo presentation
  evidence: repeated README polish requests and plugin install validation
  reject_when: repository is no longer distributed through Codex plugins
```

Weak, inferred, or competing signal belongs in `inbox/` until it has enough
evidence to promote or reject.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Maintenance Commands

| Command | Purpose |
| --- | --- |
| `python scripts/doctor.py` | Validate repository health, docs, plugin metadata, fixtures, and UTF-8 safety checks. |
| `python scripts/nightly_report.py --memory-root <path>` | Generate a maintenance report for a Dream Loop memory root. |
| `python scripts/nightly_report.py replay --fixtures-root <path>` | Replay fixture expectations and catch reporting drift. |
| `python scripts/memoryctl.py forget --memory-root <path> --target <id>` | Move stale or rejected memory out of the hot path. |
| `python scripts/install.py --codex-home <path> --apply` | Copy skills and templates into a Codex home when plugin install is unavailable. |

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Project Structure

```text
.
|-- .agents/plugins/marketplace.json
|-- .codex-plugin/plugin.json
|-- assets/
|   |-- 32x32.png
|   `-- hero-logo.png
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

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## Roadmap

- **Install path** - keep the repo-local marketplace and packaged plugin smoke-tested.
- **Report quality** - make maintenance output easier to scan without expanding the public memory model.
- **Replay coverage** - add fixtures for promotion, rejection, archive, stale-active, and rollback cases.
- **Operator ergonomics** - keep Windows, PowerShell, and Codex Desktop workflows first-class.
- **Governance clarity** - improve examples for when a memory belongs in `ACTIVE.md`, `LEARNINGS.md`, or `inbox/`.

<div align="right">

[![](https://img.shields.io/badge/-Back_to_top-gray?style=flat-square)](#readme-top)

</div>

## License

MIT. See [LICENSE](LICENSE).
