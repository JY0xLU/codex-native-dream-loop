# LEARNINGS

Reusable path memory for the current scope.

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
