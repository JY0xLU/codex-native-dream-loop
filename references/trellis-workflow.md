# Trellis Workflow

Use a Trellis-shaped workflow for Dream Loop improvement rounds:

`trunk -> branches -> leaves -> gate -> land`

The trunk is the user goal. Branches are independent work streams. Leaves are concrete edits, checks, or rejected candidates. The gate decides what lands.

## Trunk

State the real objective without shrinking it.

For this repo, the trunk is usually one of:

- make route memory more reliable
- make capability discovery more observable
- make automation drift easier to catch
- improve public documentation without adding memory layers
- package or validate the skills for installation

## Branches

Split work into branches only when they can progress independently.

Common branches:

- `docs`: README, references, examples
- `skills`: `capture-memory`, `capability-evolution`, `dream-consolidate`
- `automation`: nightly prompt and automation design
- `verification`: doctor checks, link checks, UTF-8 checks, plugin validation when a manifest exists
- `review`: subagent or reviewer pass over promotion, rejection, archive, and conflict decisions

Avoid creating branches that need to edit the same file at the same time.

## Leaves

Each leaf should be small enough to verify:

- one paragraph added to README
- one skill rule tightened
- one prompt-eval example added
- one doctor check added
- one rejected alternative recorded

Leaves should name their target file and expected evidence before landing.

## Subagent Pattern

Use subagents for sidecar work that does not block the next local edit:

- explorer for repo gap analysis
- explorer for verification and test-surface discovery
- worker for a disjoint file or script
- reviewer for judgment-heavy memory promotion or conflict decisions

The main agent keeps the trunk and final integration. Subagents should not receive vague ownership like "improve everything."

## Dream Loop Improvement Roles

For larger Dream Loop improvement rounds, use one main orchestrator plus seven bounded side branches:

| # | Agent name | Core responsibility | Write permission |
|---:|---|---|---|
| 1 | `dreamloop-repo-auditor` | Read the original repo, confirm current structure, existing features, gaps, and files that must not change | Mostly read-only |
| 2 | `dreamloop-product-readme` | Improve README positioning, first-screen value, demos, onboarding, and install clarity | Docs |
| 3 | `dreamloop-memory-governance` | Design `ACTIVE.md`, `LEARNINGS.md`, `inbox`, `staged`, `rejected`, `archive`, and audit rules | Schema, templates, docs |
| 4 | `dreamloop-gate-replay` | Design validation gate, bounded patch rules, replay fixtures, and anti-bloat checks | Gate docs, fixtures, consolidation rules |
| 5 | `dreamloop-doctor-report` | Build `dream-loop doctor` and nightly report output so users can inspect system health | CLI, report, docs |
| 6 | `dreamloop-plugin-install` | Package Codex plugin manifest, install structure, and manual fallback | Plugin and install files |
| 7 | `dreamloop-harness` | Directional reviewer that checks all edits still follow the original Dream Loop design | Review/block only |

In inline mode, the main session may execute these branches directly, but it should still keep the ownership boundaries visible and verify each branch before landing.

## Gate

Before landing a branch, check:

- Does it move the trunk objective forward?
- Is the edit smaller than the problem it solves?
- Does it preserve the public model: `ACTIVE.md` and `LEARNINGS.md`?
- Is there current evidence from files, commands, reviewer notes, or docs?
- Are rejected alternatives named when the choice is non-obvious?

If the gate fails, keep the branch as a staged proposal or reject it.

## Land

Landing means:

- files changed in the intended scope
- verification run matches the branch scope
- drift found by subagents is either fixed or listed as remaining work
- the final report names evidence, not just intent

Do not call the round complete until the trunk objective is proven against current repo state.
