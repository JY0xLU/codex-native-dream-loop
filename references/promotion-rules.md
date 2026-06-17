# Promotion Rules

Use these rules when deciding whether a signal should land immediately in `ACTIVE.md`, land immediately in `LEARNINGS.md`, stay quarantined in `inbox/`, or be archived.

## Minimum Bar

Record a signal only when it is:

- source-backed
- actionable as a route or rule
- likely to improve the next task, not just describe the last one

## Direct-Land To `ACTIVE.md`

Write directly to `ACTIVE.md` when the signal is:

- explicit
- important right now
- likely to affect the next few tasks immediately
- temporary, phase-specific, or tied to a current platform or incident

Every `ACTIVE.md` item should include one of:

- an expiry date
- a removal condition
- a superseding condition

## Direct-Land To `LEARNINGS.md`

Write directly to `LEARNINGS.md` when the signal is:

- explicit
- already validated as a winning path or durable preference
- reusable across tasks or sessions
- specific enough to tell the next run what to try first
- able to explain why the route wins and when it should be reused

A good `LEARNINGS.md` entry should capture:

- intent
- pattern
- best path
- why it wins
- last validated time
- evidence
- source trace
- why remembered
- fallback or avoid notes
- rejection condition

Durable promotion should pass the validation gate:

- source evidence
- outcome link
- blast radius
- rejection condition
- rollback path

If a candidate is useful but fails one of these checks, stage it for review or keep it in `inbox/` instead of promoting it by confidence alone.

## Keep In `inbox/`

Keep the signal quarantined when it is:

- inferred rather than directly stated
- only seen once
- still ambiguous
- still competing with another route
- useful as evidence later, but not yet worth surfacing in `ACTIVE.md` or `LEARNINGS.md`

## Archive

Archive when the item is:

- superseded by a better route
- expired and no longer hot
- rejected after review
- no longer worth keeping in public memory

## Audit Requirements

Every promotion or archive decision should preserve:

- source entry id
- target file
- why the route won or lost
- accepted or rejected alternatives when the choice is non-obvious
- rollback clue
- reviewer path when reviewer or subagent review was used

## Control Actions

Use archive instead of silent deletion. Use forget only when the user explicitly asks to remove an entry from default recall.

Suggested outcomes:

- `adopt`: bounded patch lands in `ACTIVE.md` or `LEARNINGS.md`
- `stage`: candidate waits for reviewer or gate evidence
- `reject`: candidate failed a gate check and moves to `rejected/`
- `archive`: stale, superseded, or wrong-scope item moves to `ARCHIVE/`
- `forget`: user-requested removal from default recall, with a minimal tombstone in audit history
