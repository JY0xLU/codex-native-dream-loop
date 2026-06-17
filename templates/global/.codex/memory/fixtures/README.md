# fixtures

Fixtures are small replay checks for validating route-memory changes.

Keep them lightweight. A fixture should prove that a proposed route does not break a known workflow.

Suggested first fixtures:

- `readme-visual-style.yaml`
- `pr-audit-route.yaml`
- `install-skill-route.yaml`
- `repo-vs-global-memory.yaml`
- `nightly-report-generation.yaml`

Fixtures are optional until a workflow has a clear correctness signal. Do not block urgent hot `ACTIVE.md` corrections on missing fixtures.
