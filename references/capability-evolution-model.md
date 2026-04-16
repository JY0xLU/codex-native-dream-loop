# Capability Evolution Model

This repo uses an EvoMap-lite capability loop: lightweight enough for Codex-native work, strict enough to stay auditable.

It extends Dream Loop without replacing it.

## Purpose

Dream Loop already answers:

- how signal is captured
- how memory is promoted
- how review and audit stay trustworthy

Capability evolution adds the missing front half:

- how a task is classified before selecting capabilities
- how plugins, skills, and external projects are discovered in a controlled order
- how new capabilities are validated before adoption

The combined operating cycle is:

`recall -> classify -> discover -> validate -> adopt -> capture -> consolidate`

## Intent Types

Use one of four intents before capability discovery:

### `repair`

Use when something expected is broken or missing.

Examples:
- a plugin path no longer works
- a workflow is blocked by a missing capability
- a previously working setup regressed

### `optimize`

Use when the task already works, but the current path is inefficient or weak.

Examples:
- too many manual steps
- lower confidence than necessary
- better official support exists than the ad hoc workflow currently used

### `innovate`

Use when the task calls for a new meaningful ability.

Examples:
- adding a new repo workflow
- introducing a new supported platform path
- expanding the system beyond memory maintenance alone

### `explore`

Use only when official and local options are insufficient or unclear.

Examples:
- no existing plugin clearly fits
- local skills do not cover the scenario
- multiple external approaches need comparison before adoption

`explore` is an escalation path, not the default.

## Discovery Order

Follow this order and stop at the first sufficient option:

1. enabled official plugins
2. installable official plugins
3. local built-in skills
4. trusted GitHub skills or projects

Why this order:

- official capabilities usually offer the best integration and lowest trust risk
- local skills are easier to inspect and adapt than external projects
- GitHub search is powerful, but should be deliberate because it increases trust and integration risk

## Validation Criteria

A new capability should pass a quick validation gate before adoption.

### Relevance

- directly matches the task and intent
- reduces friction or increases confidence in a meaningful way

### Maintenance Recency

- recently updated, or clearly still maintained
- not obviously abandoned or stale

### Source Trust

- official source preferred
- otherwise, attributable maintainer, strong repo quality, and clear documentation

### Integration Cost vs Benefit

- setup and runtime overhead should be justified by the expected gain
- avoid large, fragile additions for small one-off wins

If the candidate fails the gate, reject it or keep it at reference level.

## GitHub Trust Heuristics

When GitHub discovery is needed, prefer:

- official upstream repositories first
- actively maintained repositories
- clear README and usage docs
- narrow fit to the current scenario
- transparent ownership and licensing

Avoid immediate adoption when the repo looks:

- abandoned
- thinly documented
- overly broad compared to the need
- hard to integrate safely
- difficult to attribute or verify

Third-party GitHub adoption should be reported to the user before or while being applied.

## Capability Adoption Levels

Not every discovered option deserves the same status.

### `reference`

- read or compared, but not used
- useful for orientation only

### `trial`

- used in one task or one limited experiment
- not yet stable enough for promotion

### `stable`

- reused successfully across multiple tasks or contexts
- good candidate for Dream Loop capture and later promotion into `LEARNINGS.md`

### `policy`

- required operating rule
- must go through human-approved policy handling instead of silent promotion

## Relationship To Dream Loop

Capability evolution does not replace Dream Loop responsibilities.

- `capture-memory` records high-signal observations and outcomes during active work
- `dream-consolidate` decides whether the result stays raw, becomes operational guidance, graduates into long-term memory, or is archived

This separation keeps the system honest:

- adoption happens in the task
- promotion happens later, with review and audit
