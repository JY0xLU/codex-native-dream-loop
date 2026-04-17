# Automation Design

Use one recurring automation for the Dream Loop.

Do not split the system into one automation for memory, one for repo review, one for drift, and one for planning. Keep the model small and let one automation perform one integrated audit-style pass.

## Public Model It Must Respect

- `ACTIVE.md` for what is hot now
- `LEARNINGS.md` for reusable winning routes

Everything else is support machinery.

## Responsibilities

The single automation should cover four responsibilities in one run:

### 1. Memory Maintenance

- refresh or retire stale `ACTIVE.md` entries
- strengthen `LEARNINGS.md` with validated winning routes
- merge duplicate evidence that supports the same route
- move stale or losing routes into `ARCHIVE/`
- preserve rollback context for reversions and superseded routes
- keep `inbox/` as a short-lived staging buffer rather than a long-term candidate pool
- review entries older than one automation cycle, which defaults to 6 hours in the active setup
- auto-land only entries that are contradiction-free, source-backed, and already expressed in executable form
- route hot temporary guidance into `ACTIVE.md`, stable reusable guidance into `LEARNINGS.md`, and archive noise or rejected evidence
- never treat age alone as sufficient evidence for promotion

### 2. Repo Round Audit

- inspect the current branch state
- inspect recent commits
- inspect the current PR when present
- inspect key route-memory and automation docs
- summarize what the current round already changed and what gap remains

### 3. Automation Drift Check

- compare the automation prompt against the repo's current model
- identify stale prompt assumptions
- recommend wording changes without directly editing repo-tracked files

### 4. Next-Round Recommendation

- propose the single most valuable next improvement
- explain the winning route
- record rejected alternatives
- show why the next round should make the system faster or stronger

## Inputs

Read:

- `.codex/memory/inbox/`
- only the relevant slices of `.codex/memory/ACTIVE.md`
- only the relevant slices of `.codex/memory/LEARNINGS.md`
- `.codex/memory/ARCHIVE/` only when lineage matters
- the current repo's branch, recent commits, PR, and automation-alignment docs

## Promotion Classifier

Promote to `ACTIVE.md` when the item is hot, temporary, urgent, or phase-specific and should change behavior immediately.

Promote to `LEARNINGS.md` when the item is stable, reusable across tasks, and already written as an executable preference, route, capability choice, or failure pattern.

Keep the item in `inbox/` for at most one additional cycle when it still lacks a contradiction check, a clear destination layer, or enough evidence.

Archive the item when it is noise, superseded, or useful only for lineage.

## Outputs

The automation should emit one structured Chinese run summary with:

- `Memory Summary`
- `Repo Round Audit`
- `Winning Route`
- `Rejected Routes`
- `Automation Drift`
- `Next Round`

## Guardrails

The automation may:

- maintain memory files inside the canonical memory root
- inspect repo-tracked files for audit and alignment
- recommend the next round

The automation must not:

- rewrite `AGENTS.md`
- invent learnings with no source trace
- delete raw evidence without archiving it
- modify repo-tracked files
- commit, push, or open PRs
