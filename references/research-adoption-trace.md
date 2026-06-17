# Research Adoption Trace

This file records which external projects informed Dream Loop changes, what was adopted, and what was intentionally left out.

## Checked Projects

| Project | Current role | Borrowed | Landed in this repo | Not borrowed |
|---|---|---|---|---|
| `microsoft/SkillOpt` / SkillOpt-Sleep | Primary adjacent reference for validated skill improvement | validation gate, staged proposals, bounded patch, replay fixtures, thin plugin shell | `references/validation-gate.md`, `skills/dream-consolidate/SKILL.md`, `templates/global/.codex/memory/staged/`, `rejected/`, example fixtures, `scripts/nightly_report.py replay`, plugin manifest | epochs, optimizer knobs, heavy training loop, WebUI |
| Cline Memory Bank | Onboarding and file-based memory reference | simple setup, structured markdown, project-local instructions | README onboarding, `scripts/install.py`, template skeleton | "read everything every time" context dump behavior |
| Claude Code memory-bank style projects | Product packaging reference | first-screen value, health/doctor framing, progressive loading idea | README repositioning, `scripts/doctor.py`, "Quality Without Bloat" section | three-tier public memory model |
| `alioshr/memory-bank-mcp` | MCP and project isolation reference | project isolation, structure validation, MCP as possible future layer | scope language, doctor structural checks, repo/global memory fixture | default MCP server dependency |
| `mem0ai/mem0` | Market signal for agent memory | long-term memory has demand | positioning as route memory governance rather than generic memory | generic memory platform architecture |
| `letta-ai/letta` | Stateful-agent boundary reference | stateful agents can learn over time | non-goal statement: Dream Loop is not an agent runtime | agent runtime replacement |
| `getzep/graphiti` | Provenance and temporal validity reference | source trace, why remembered, supersede/archive thinking | `LEARNINGS.md` metadata, `promotion-rules.md`, `validation-gate.md` | graph database or temporal knowledge graph |
| agentmemory-style systems | Observability reference | audit trail, why remembered, nightly report, forget with tombstone | `scripts/nightly_report.py`, `scripts/memoryctl.py`, reports template, source-trace fields | hooks server, REST API, large tool surface |

## Adoption Rules

- Borrow mechanism, not complexity.
- Keep daily recall limited to `ACTIVE.md` and `LEARNINGS.md`.
- Treat `staged/`, `rejected/`, `fixtures/`, and `reports/` as governance artifacts.
- Prefer dependency-free scripts until a runtime need is proven.
- Keep plugin registration and manual install paths side by side.

## Landed Lightweight Borrowing

- fixture replay now has a dependency-free CLI check via `python scripts/nightly_report.py replay --fixtures-root examples/minimal-global/.codex/memory/fixtures`
- HTML report output is available through `python scripts/nightly_report.py --format html --output report.html`
- explicit forget support is available through `python scripts/memoryctl.py forget ...`, with archived original content and an audit tombstone

## Remaining Optional Research-Plan Items

- optional MCP layer for remote or team use
- stronger source-trace extraction from real Codex transcripts
- richer replay harness only if real failures show that shape checks are too weak
