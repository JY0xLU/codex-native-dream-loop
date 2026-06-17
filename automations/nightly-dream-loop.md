# Dream Loop Evolution Automation

## Recommended Schedule

- daily by default; increase frequency only while the loop is actively evolving
- local off-hours whenever possible
- keep one recurring automation rather than splitting memory and audit into separate schedules

## Recommended Prompt

```text
This is the recurring Dream Loop evolution pass for a Codex-native route-memory system.

Work in six sections:

1. Memory Maintenance
- maintain Dream Loop memory only inside the canonical `.codex/memory` root
- treat `ACTIVE.md` and `LEARNINGS.md` as the only public memory layers
- treat `inbox` as a short-lived quarantine for inferred or unresolved signal, not as a holding area for explicit strong signal
- read inbox plus only the relevant slices of ACTIVE.md, LEARNINGS.md, and ARCHIVE when needed
- use dream-consolidate to refresh hot entries, strengthen route memory, archive stale or losing routes, and preserve a minimal audit trail
- emit a compact nightly report with promoted, archived, rejected, stale active, unresolved inbox, fixture status, source-trace coverage, and next action
- if explicit user directives, corrections, or durable preferences are still sitting in inbox, move them out immediately instead of waiting another cycle
- review inbox entries older than one automation cycle and auto-land only the contradiction-free, source-backed, executable inferred items whose destination is now clear
- write hot temporary guidance into `ACTIVE.md`, stable reusable preferences or routes into `LEARNINGS.md`, and archive noise or rejected evidence
- do not promote by age alone; require stronger evidence for inferred routes before landing in `LEARNINGS.md`
- run a lightweight validation gate before durable promotion: source evidence, outcome link, blast radius, rejection condition, and rollback path
- for judgment-heavy promotions, stage a proposal with accepted edits, rejected candidates, target layer, reviewer/subagent notes, and rollback notes before changing public memory

2. Repo Round Audit
- read only the minimum repo context needed to understand the current round
- inspect current branch status, recent commits, current PR if one exists, and key route-memory or automation docs
- summarize what changed this round, which routes were reused, what is already aligned, and what gap still remains

3. Custom Skill Alignment
- compare the active automation prompt against installed custom skills, especially `dream-consolidate`, `capture-memory`, `capability-evolution`, and any recovery skill when relevant
- check that explicit strong signal direct-lands, inbox stays limited to unresolved inferred signal, `AGENTS.md` changes are transparent rather than silent, policy-like changes remain proposal-first, and GitHub discovery stays an escalation path
- for `capability-evolution`, audit whether recent evidence shows real searched layers and candidate decisions; if only policy text exists, report weak capability discovery
- give each checked skill one compact verdict: `strong` when real behavior evidence matches the prompt, `weak` when only wording or indirect evidence exists, and `blocked` when the required files, tools, or runtime evidence are missing
- if a local CLI, bundled script, plugin path, dependency, or environment setup needed for the audit is missing, repair it directly when the fix is low risk or report the blocked path

4. Reviewer Check
- use reviewer or subagent cross-checking for promotion, rejection, archive, and conflict decisions when available and useful
- if tool policy blocks subagents, or the pass is low-risk cleanup with no judgment-heavy decision, use the single-agent fast path and report why review was skipped
- distinguish real reviewer/subagent evidence from reused policy text
- include reviewer/subagent feedback in staged proposals when a candidate changes durable route memory

5. Automation Drift Check
- compare this automation's assumptions against the repo's current automation and route-memory model
- inspect at least the nightly automation doc, automation design reference, AGENTS snippet, and README automation language
- if drift exists, report the stale assumption, the replacement wording, and why it should change
- do not self-edit repo files as part of this drift check

6. Next-Round Recommendation
- recommend the single highest-leverage next improvement
- explain why it wins
- list which existing route it reuses
- list any rejected alternatives and why they lost
- explain how the proposed next round should make the system faster or stronger

Hard constraints:
- do not rewrite AGENTS.md
- do not invent learnings with no traceable source
- do not silently delete evidence; archive it
- do not treat staged proposals as a third public memory layer
- do not modify repo-tracked files
- do not commit, push, or open PRs

Output in Chinese with these sections:
- Memory Summary
- Repo Round Audit
- Custom Skill Alignment, with one `strong` / `weak` / `blocked` verdict per checked skill
- Reviewer Check
- Automation Drift
- Next Round
```
