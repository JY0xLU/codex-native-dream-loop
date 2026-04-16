---
name: capability-evolution
description: Use when a task needs controlled capability discovery, validation, and adoption before memory capture or off-hours consolidation. Handles plugins, local skills, and GitHub-sourced capability research with a stable EvoMap-lite workflow.
---

# Capability Evolution

Use this skill during active work when the current task may need a better capability than the ones already in hand.

Its job is to discover, validate, and adopt capabilities. It does not capture memory events or rewrite long-term memory.

## Use This Skill When

- the task should be classified before choosing tools or workflows
- an official plugin might solve the task better than ad hoc work
- a new local skill may be needed for the current repo or workflow
- the assistant should compare multiple capability options instead of choosing one blindly
- official and local options may be insufficient, unclear, or not obviously fit for the scenario
- the user wants a controlled self-improvement workflow rather than improvised tool selection

## Do Not Use This Skill When

- the task only needs a normal tool invocation with no capability decision
- the user only wants to record a preference, correction, or outcome in memory
- the user wants off-hours Dream Loop cleanup, promotion, rejection, or archival
- the user wants to rewrite `AGENTS.md` directly instead of following a review path

## Intent Classification

Classify the task into one intent before capability discovery:

- `repair`
  - restore a broken workflow, failed integration, or missing capability
- `optimize`
  - improve speed, quality, confidence, or repeatability without changing the task shape
- `innovate`
  - add a meaningful new capability or workflow that the current setup does not yet cover
- `explore`
  - search for new options only when official and local choices are insufficient or unclear

`explore` is not the default. Use it only after official and local options fail to cover the task cleanly.

## Discovery Order

Check options in this order and stop at the first sufficient fit:

1. enabled official plugins
2. installable official plugins
3. local built-in skills
4. trusted GitHub skills or projects

Do not jump straight to GitHub search if a good official or local option already exists.

## Validation Gate

Before adopting a new plugin, skill, or GitHub-sourced capability, check:

- relevance
  - does it directly fit the current task and intent
- maintenance recency
  - is it still being maintained or recently updated
- source trust
  - is it official, clearly attributable, or from a high-signal maintainer
- integration cost
  - is setup cost justified by the expected gain in accuracy, speed, or coverage

If one or more checks fail, do not adopt automatically. Report the tradeoff or fallback choice.

## Reporting Requirements

Report to the user before or while doing either of these:

- adopting a third-party GitHub skill or project
- making a material global setup change, such as changing core configuration or installing a broad new dependency path

The report can be short, but it must make the change visible.

## Working Loop

1. recall the smallest relevant memory slice
2. classify the task intent
3. discover capabilities in the fixed order
4. validate the best candidate
5. adopt or invoke the capability only if the validation clears
6. finish the task work
7. if the new capability produced a high-signal result, hand off the event to `capture-memory`

## Relationship To Other Skills

- `capture-memory`
  - use after the task when a high-signal outcome, blocker, preference, or workflow win should be recorded
- `dream-consolidate`
  - use later for off-hours candidate generation, promotion, rejection, archive, and audit work

This skill sits before both:

`discover -> validate -> adopt -> capture -> consolidate`

## Hard Constraints

- do not rewrite `ACTIVE.md` or `LEARNINGS.md` during active work
- do not treat GitHub search as a default step
- do not silently import third-party capabilities
- do not confuse one-off experimentation with stable policy
- keep capability evolution separate from memory promotion

## Output Expectations

When this skill influences a decision, the final answer should make these visible when relevant:

- chosen intent
- discovery path used
- why a capability was selected or rejected
- whether the result should later be captured into Dream Loop memory
