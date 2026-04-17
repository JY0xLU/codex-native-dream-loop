# ACTIVE

Hot routes and hot rules for the current scope.

## Repo Scope
- [ACT-20260408-001] temporary deploy safeguard
  Intent: repair
  Scope: repo
  Pattern: deploy work during the April auth migration window
  Best Path: verify secrets before rollout -> confirm migration-specific checks -> deploy
  Why Hot: this safeguard still affects deploy decisions right now
  Source trace: OBS-20260408-002, AUDIT-20260408-002
  Last validated: 2026-04-08
  Reviewer verdict: approved
  Rollback clue: remove this entry after the auth migration closes
  Expiry: retire when the migration checklist is removed

## Last Reviewed
- 2026-04-08
