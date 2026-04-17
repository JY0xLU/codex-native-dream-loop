## Dream Loop

Use the global memory directory at `~/.codex/memory/`.

Scope model:
- global: shared memory across workspaces
- repo: repo-specific memory
- thread: current conversation memory

Keep the system at these three scopes. Avoid adding extra task or session files unless a human explicitly approves a new pattern.

Before starting any task:
1. Determine the narrowest relevant scope: `global`, `repo`, or `thread`
2. Retrieve only the relevant slices from `~/.codex/memory/ACTIVE.md` and `~/.codex/memory/LEARNINGS.md`
3. Treat `ACTIVE.md` as the hot layer and `LEARNINGS.md` as the reusable route-memory layer
4. Apply only that minimal memory context before analyzing the request

Capability evolution workflow:
1. Classify the task intent as `repair`, `optimize`, `innovate`, or `explore`
2. Discover capabilities in this order and stop at the first sufficient option:
   enabled official plugins -> installable official plugins -> local built-in skills -> trusted GitHub skills or projects
3. Validate any newly adopted capability before using it:
   relevance to the task, maintenance recency, source trustworthiness, and integration cost versus expected benefit
4. Use GitHub discovery only when official and local options are insufficient or unclear; it is an escalation path, not the default
5. Report to the user before or while adopting third-party GitHub capabilities or making material global setup changes
6. Reuse a known winning route first when it clearly fits; only search wider when confidence is too low
7. Treat successful capability use as future memory signal; capture it now and let Dream Loop decide whether it belongs in `ACTIVE.md` or `LEARNINGS.md`

During active work:
1. Capture high-signal observations into `~/.codex/memory/inbox/`
2. Keep raw Observed items short and source-backed
3. Do not rewrite long-term memory while solving the current task
4. Use `capture-memory` for event capture only
5. Use `capability-evolution` for capability discovery, validation, and adoption only

Memory policy:
1. Policy is human-approved only
2. If a rule seems like policy, propose it for human review; do not auto-write it

Off-hours and maintenance:
1. Use a single recurring automation that maintains Dream Loop memory, audits the current repo or PR round, checks automation drift, and recommends the next round
2. Use `dream-consolidate` within that automation, or during manual maintenance, for hot-layer refresh, route promotion, archive decisions, and audit support
3. Prefer subagent review for promotion, rejection, archive, and conflict decisions
4. Keep low-risk cleanup on a single-agent fast path when no judgment call is needed

Promotion rules:
1. Promote temporary but high-impact hot routes or hot rules into `~/.codex/memory/ACTIVE.md`
2. Promote validated reusable winning paths into `~/.codex/memory/LEARNINGS.md`
3. Preserve `~/.codex/memory/AUDIT_LOG.md` and `~/.codex/memory/ARCHIVE/` for traceability

Behavior expectations:
- Prefer short, auditable memory entries over long narratives
- Keep temporary rules out of long-term memory unless they recur
- Preserve enough raw evidence to explain promotions later
- Keep `capture-memory` lightweight; reserve subagent-heavy work for Dream Loop review and audit decisions
- Prefer official plugin-based workflows when they cover the task well
- Do not turn one successful experiment into policy without repeated evidence
- Keep the public model small: `ACTIVE.md` and `LEARNINGS.md` should stay readable without exposing extra layers as daily operating concepts
- A recurring automation may read repo-tracked files for audit and alignment, but it should not modify repo-tracked files unless a human explicitly asks for implementation
