# Automation Design

Use one recurring automation for the Dream Loop.

Do not split the system into one automation for memory, one for repo review, one for drift, and one for planning. Keep the model small and let one automation perform one integrated audit-style pass.

## Public Model It Must Respect

- `ACTIVE.md` for what is hot now
- `LEARNINGS.md` for reusable winning routes

Everything else is support machinery.

## Responsibilities

The single automation should cover six responsibilities in one run:

### 1. Memory Maintenance

- refresh or retire stale `ACTIVE.md` entries
- strengthen `LEARNINGS.md` with validated winning routes
- merge duplicate evidence that supports the same route
- move stale or losing routes into `ARCHIVE/`
- preserve rollback context for reversions and superseded routes
- keep `inbox/` as a short-lived quarantine buffer only for inferred, ambiguous, or still-unresolved signal
- immediately move any misplaced explicit strong signal out of `inbox/`
- review inferred inbox items older than one automation cycle
- auto-land only inferred items that are contradiction-free, source-backed, executable, and now have a clear destination
- route hot temporary guidance into `ACTIVE.md`, stable reusable guidance into `LEARNINGS.md`, and archive noise or rejected evidence
- never treat age alone as sufficient evidence for promotion

### 2. Repo Round Audit

- inspect the current branch state
- inspect recent commits
- inspect the current PR when present
- inspect key route-memory and automation docs
- summarize what the current round already changed and what gap remains

### 3. Custom Skill Alignment

- compare the automation prompt against installed custom skills
- check `dream-consolidate`, `capture-memory`, `capability-evolution`, and recovery skills when relevant
- verify that capability discovery has observable evidence, not just policy text
- report missing CLIs, plugin paths, or dependencies and repair low-risk local setup gaps when allowed

### 4. Reviewer Check

- use reviewer or subagent cross-checking for promotion, rejection, archive, and conflict decisions when available and useful
- report when review is skipped because the pass is low risk, has no judgment-heavy decision, or tool policy blocks subagents
- distinguish real reviewer evidence from reused prompt or policy language

### 5. Automation Drift Check

- compare the automation prompt against the repo's current model
- identify stale prompt assumptions
- recommend wording changes without directly editing repo-tracked files

### 6. Next-Round Recommendation

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

Write directly to `ACTIVE.md` when the signal is explicit, hot, temporary, urgent, or phase-specific and should change behavior immediately.

Write directly to `LEARNINGS.md` when the signal is explicit, durable, reusable across tasks, and already written as an executable preference, route, capability choice, or failure pattern.

Keep the item in `inbox/` only when it is inferred, ambiguous, still competing, or still too weak to guide future behavior.

Archive the item when it is noise, superseded, or useful only for lineage.

## Outputs

The automation should emit one structured Chinese run summary with:

- `Memory Summary`
- `Repo Round Audit`
- `Custom Skill Alignment`
- `Reviewer Check`
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
