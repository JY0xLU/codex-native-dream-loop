# Nightly Dream Loop Automation

## Recommended Schedule

- Daily
- Local off-hours
- Example: 02:00 local time

## Recommended Prompt

```text
This is the nightly Dream Loop consolidation pass for a Codex-native memory system.

Read:
- ~/.codex/memory/inbox/
- ~/.codex/memory/ACTIVE.md
- ~/.codex/memory/LEARNINGS.md
- ~/.codex/memory/FEATURE_REQUESTS.md

Goals:
1. deduplicate recent inbox items
2. remove or archive expired temporary guidance
3. rewrite relative dates into absolute dates when needed
4. promote only repeated, generalizable, actionable items
5. keep temporary operational guidance in ACTIVE.md
6. keep stable cross-task patterns in LEARNINGS.md
7. keep future capability gaps in FEATURE_REQUESTS.md

Hard constraints:
- do not rewrite AGENTS.md
- do not invent learnings with no traceable source
- do not silently delete evidence; archive it

Output a report that includes:
- files read
- files changed and why
- promotions made
- promotions rejected and why
- archive actions
- remaining cleanup
```
