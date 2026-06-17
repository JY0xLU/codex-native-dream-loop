# Validation Gate

Dream Loop can borrow validation discipline from skill-optimization systems without becoming a heavy optimizer.

The gate answers one question:

> Is this memory change proven enough to affect future behavior?

## Gate Checks

Use these checks before durable promotion into `LEARNINGS.md`:

- source evidence: a real task, explicit correction, audit finding, or repeated failure supports the candidate
- outcome link: the candidate explains how a future run becomes faster, safer, or more reliable
- blast radius: the candidate is narrow enough to avoid unrelated behavior changes
- rejection condition: the audit names what evidence would make the candidate wrong or stale
- rollback path: the audit preserves enough context to retire or reverse the route later

If any check is weak, do not promote by default. Keep the candidate in `inbox/`, stage it for review, or archive it as rejected evidence.

## Staged Proposals

Use staged proposals for judgment-heavy changes, especially durable route memory changes.

A staged proposal should include:

- target layer: `ACTIVE.md`, `LEARNINGS.md`, `ARCHIVE/`, or `inbox/`
- accepted edits
- rejected candidates
- source evidence
- reviewer or subagent notes when available
- rollback notes

Staging is an audit checkpoint, not a third public memory layer. The public model remains `ACTIVE.md` and `LEARNINGS.md`.

## Bounded Patch

Durable memory changes should be expressed as bounded edits:

- `ADD`: introduce one scoped route, rule, fixture, or report note
- `DELETE`: remove or archive one stale or rejected item
- `REPLACE`: update one existing item while preserving source trace

Avoid whole-file rewrites during consolidation. If a proposal needs a whole-file rewrite, stage it for human review and explain why a bounded edit is not enough.

Patch records should include:

- target file
- operation
- anchor or entry id
- proposed content
- source trace
- rollback clue

## Replay Evidence

Replay does not need to become a full benchmark harness.

For Dream Loop, replay can be lightweight:

- cite a previous task where the candidate route would have changed the outcome
- rerun a small local check when one exists
- compare the candidate against a rejected alternative
- preserve a before/after rationale in `AUDIT_LOG.md`

When no replay evidence exists, say so and keep the candidate out of durable memory.

## First Fixture Set

Start with five fixtures:

- `readme-visual-style`: README refreshes reuse a proven structure instead of rewriting from scratch
- `pr-audit-route`: PR/repo audits include branch state, reviewer evidence, and next action
- `install-skill-route`: skill installation follows skills -> templates -> AGENTS -> verify
- `repo-vs-global-memory`: repo rules do not leak into global memory
- `nightly-report-generation`: nightly reports summarize staged, rejected, stale, and unresolved state
