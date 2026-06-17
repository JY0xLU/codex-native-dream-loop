# staged

Staged proposals are audit checkpoints for judgment-heavy Dream Loop changes.

Use this directory for proposal bundles that are not ready to land directly into `ACTIVE.md` or `LEARNINGS.md`.

A staged proposal should include:

- `proposal.md`
- `patch.diff` when a bounded edit exists
- `evidence.json` or a short source-trace note
- `metrics.json` when replay or gate checks ran

Staging is not a third public memory layer. Daily recall should still read `ACTIVE.md` first and `LEARNINGS.md` second.
