# LEARNINGS

Reusable path memory for the current scope.

Use the index first, then read only the section relevant to the current task.

## Index

- `Core Workflow`: global execution style and validation routes
- `Project-Specific Routes`: routes that only matter when the same project appears again

## Core Workflow

## [LRN-20260408-001] narrow-first validation
Intent: optimize
Scope: repo
Pattern: frontend validation work where the changed area is already clear
Best Path: run the narrow web test target -> confirm local UI behavior -> run repo lint after the narrow target passes
Why It Wins: this path repeatedly catches local breakage faster than lint-first or full-suite-first validation
Last validated: 2026-04-08
Evidence: OBS-20260406-002, OBS-20260407-001, OBS-20260408-001, AUDIT-20260408-001
Fallback / Avoid: avoid using broad lint-first validation as the default when the changed area is already narrow and obvious
Reviewer verdict: approved
Rollback clue: revise or archive if repeated tasks stop benefiting from narrow-first validation

## [LRN-20260508-001] observable capability discovery
Intent: optimize
Scope: global
Pattern: capability search, third-party tool adoption, or self-evolution audit work
Best Path: show searched layers in order -> explain skipped or blocked layers -> list selected and rejected candidates -> only then claim the capability route is strong
Why It Wins: capability evolution is only useful when the evidence shows what was actually checked; this prevents prompt text from being mistaken for execution
Last validated: 2026-05-08
Evidence: user skepticism about weak third-party search and cross-review, followed by capability-evolution update
Fallback / Avoid: avoid claiming GitHub or third-party discovery worked unless GitHub/external search was reached or explicitly skipped with a concrete reason
Reviewer verdict: needs review
Rollback clue: revise if a dedicated capability-discovery ledger replaces manual searched-layer reporting

## Project-Specific Routes

- ...
