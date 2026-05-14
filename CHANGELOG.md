# Changelog

All notable changes to `Codex Native Dream Loop` will be documented in this file.

## 2026-05-08

### Added
- Added observable capability discovery to `capability-evolution`, requiring searched layers, skipped or blocked layers, selected and rejected candidates, and GitHub/external search status to be visible for non-trivial capability decisions.
- Added `skills/capability-evolution/references/discovery-evidence.md` as the detailed checklist for auditing whether capability discovery actually ran instead of only being described in policy text.
- Added template and example `LEARNINGS.md` guidance for evidence-backed capability evolution so future memory entries can record official plugin checks, local skill checks, GitHub/external search status, and candidate decisions.

### Changed
- Updated the automation prompt model from a four-section audit to a six-section pass: memory summary, repo round audit, custom skill alignment, reviewer check, automation drift, and next round.
- Changed the recommended automation cadence to daily by default, with higher frequency reserved for active evolution windows.
- Updated README docs in English and Chinese to explain observable capability discovery, custom skill alignment, and real reviewer/subagent evidence reporting.
- Updated `capture-memory` and `dream-consolidate` wording so `AGENTS.md` changes are transparent and human-visible rather than silently blocked by outdated "never edit" language.
- Updated `capability-evolution` so explicit strong signal can hand off to `capture-memory`, while weak or still-competing capability signals remain out of public memory.

### Fixed
- Fixed the gap where capability evolution could claim an ordered discovery process without showing which layers were actually checked.
- Fixed automation wording that blurred real reviewer/subagent use with reused policy text by requiring explicit reporting when review was skipped.

## 2026-04-09

### Changed
- Reframed the project around a v2 memory-priority architecture focused on self-improvement and memory optimization.
- Compressed the core model into four parts: Policy, Memory Scopes, Improvement Loop, and Audit.
- Tightened retrieval guidance so the system prefers minimal, scope-aware lookups over broad rereads.

### Skills
- Updated `capture-memory` to record lightweight, scoped events without promoting or consolidating memory during active work.
- Updated `dream-consolidate` to handle candidate generation, reviewer-assisted promotion and rejection, audit-first updates, and nightly consolidation.
- Kept policy-like changes proposal-only and reserved human approval for top-level policy updates.

### Templates
- Updated the global `AGENTS.md` snippet to use `global`, `repo`, and `thread` scopes with minimal retrieval guidance.
- Reworked memory templates so `ACTIVE.md` acts as the Operational projection and `LEARNINGS.md` acts as the LongTerm projection.
- Strengthened audit template fields around source trace, reviewer verdict, final decision, and rollback clues.

### References and Examples
- Updated the reference docs to match the v2 memory-priority model, including scope, promotion, automation, prompt-eval, and audit guidance.
- Refreshed the minimal example to show Observed, Operational, LongTerm, and audit-style nightly reporting in practice.
