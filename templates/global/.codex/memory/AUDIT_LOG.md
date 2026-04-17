# AUDIT_LOG

Record every promotion, rejection, merge, archive, and rollback decision here.

## Entry Format
- [AUDIT-YYYYMMDD-###]
  Timestamp: ISO-8601 timestamp
  Action: promote-active | promote-learning | revise-route | reject | archive | rollback
  Scope: global | repo | thread
  Source trace: inbox ids, report ids, or prior memory ids
  Reviewer verdict: approved | needs review | rejected
  Final decision: keep | revise | retire
  Rollback clue: what to undo if the decision is reversed
  Target: ACTIVE.md | LEARNINGS.md | ARCHIVE/
  Winning route: optional short label
  Rejected routes: optional short labels

## Audit Trail
- ...
