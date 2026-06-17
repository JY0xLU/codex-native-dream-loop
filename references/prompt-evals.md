# Prompt Evals

Use these examples to verify that the two Dream Loop skills stay separate and memory-priority focused.

## Should Trigger `capture-memory`

1. "Record this repeated npm failure so we stop rediscovering it."
2. "The user corrected our default deploy path again; log that."
3. "Capture this repo-specific validation order for future sessions."
4. "Add this stable communication preference into memory capture."
5. "Track this recurring missing capability in the inbox."

## Should Not Trigger `capture-memory`

1. "Clean up and deduplicate my existing memory files."
2. "Run the nightly memory review now."
3. "Promote these repeated items into LEARNINGS.md."
4. "Rewrite AGENTS.md with the new operating rules."
5. "Initialize the entire Dream Loop from scratch."

## Should Trigger `dream-consolidate`

1. "Run a nightly consolidation pass over the latest inbox entries."
2. "Deduplicate memory and promote repeated patterns with a report."
3. "Archive expired ACTIVE.md items and explain why."
4. "Review recent inbox entries and decide what belongs in LEARNINGS.md."
5. "Do an off-hours Dream Loop cleanup without touching AGENTS.md."

## Should Not Trigger `dream-consolidate`

1. "Log this user correction for later."
2. "Capture this repeated failure into inbox."
3. "Remember this preference but do not reorganize memory yet."
4. "While we are still debugging, just record the signal."
5. "Add one raw observation to today's inbox file."

## Should Trigger `capability-evolution`

1. "Find the right plugin or skill before we build this workflow."
2. "Check whether an official tool already covers this before using a GitHub project."
3. "Compare available Codex plugins, local skills, and external repos for this task."
4. "Show which capability candidates were checked and why one won."
5. "This current route works but feels slow; find a better capability path."

## Should Not Trigger `capability-evolution`

1. "Run the known install command from our existing route memory."
2. "Use the already-selected plugin to finish this task."
3. "Capture this successful route after the work is done."
4. "Clean up old memory entries without changing capability choices."
5. "Summarize the repo README without adopting new tools."

## Observable Evidence Evals

These examples test whether the agent reports evidence instead of policy text.

### Strong

1. "Checked enabled plugins: GitHub available but insufficient for screenshots; checked local skills: playwright selected; skipped GitHub search because local browser testing covers the task."
2. "Compared `capture-memory` and `dream-consolidate`; selected `capture-memory` because this is an active explicit correction, rejected `dream-consolidate` because no maintenance pass was requested."
3. "Subagent reviewer inspected `LEARNINGS.md` and found contradiction-free source trace; promotion passed with rollback note."

### Weak

1. "I followed the capability-evolution policy" with no checked tools, files, candidates, or skipped layers.
2. "Reviewer check passed" when no reviewer, subagent, command output, or concrete evidence is named.
3. "GitHub discovery was considered" without naming whether it was reached, skipped, blocked, or unnecessary.
