#!/usr/bin/env python3
"""Generate a compact Dream Loop nightly report from a memory root."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
from html import escape
from pathlib import Path


@dataclass(frozen=True)
class ReplayResult:
    passed: int
    total: int
    failures: list[str]


def count_files(root: Path, pattern: str = "*.md", *, skip_readme: bool = True) -> int:
    if not root.exists():
        return 0
    count = 0
    for path in root.rglob(pattern):
        if not path.is_file():
            continue
        if skip_readme and path.name.lower() == "readme.md":
            continue
        count += 1
    return count


def count_stale_active(active_path: Path) -> int:
    if not active_path.exists():
        return 0
    text = active_path.read_text(encoding="utf-8")
    stale_markers = ("expired", "stale", "needs review", "YYYY-MM-DD")
    return sum(1 for line in text.splitlines() if any(marker in line for marker in stale_markers))


def fixture_status(fixtures_root: Path) -> str:
    total = count_files(fixtures_root, "*.yaml", skip_readme=False) + count_files(fixtures_root, "*.yml", skip_readme=False)
    if total == 0:
        return "0/0"
    passed = 0
    for path in list(fixtures_root.rglob("*.yaml")) + list(fixtures_root.rglob("*.yml")):
        if fixture_passes(path):
            passed += 1
    return f"{passed}/{total}"


def replay_fixtures(fixtures_root: Path) -> ReplayResult:
    fixture_paths = sorted(list(fixtures_root.rglob("*.yaml")) + list(fixtures_root.rglob("*.yml")))
    failures: list[str] = []
    for path in fixture_paths:
        if not fixture_passes(path):
            failures.append(str(path.relative_to(fixtures_root)))
    return ReplayResult(passed=len(fixture_paths) - len(failures), total=len(fixture_paths), failures=failures)


def fixture_passes(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    has_id = any(line.startswith("id:") and line.split(":", 1)[1].strip() for line in lines)
    has_description = any(line.startswith("description:") and line.split(":", 1)[1].strip() for line in lines)
    has_expects = False
    in_expects = False
    for line in lines:
        stripped = line.strip()
        if stripped == "expects:":
            in_expects = True
            continue
        if in_expects:
            if stripped.startswith("- ") and stripped[2:].strip():
                has_expects = True
            elif stripped and not line.startswith((" ", "\t", "-")):
                in_expects = False
    return has_id and has_description and has_expects


def render_report(memory_root: Path) -> str:
    summary = build_summary(memory_root)
    lines = [
        "# Dream Loop Nightly Report",
        "",
        f"Date: {summary['date']}",
        f"Memory root: `{summary['memory_root']}`",
        "",
        "| Promoted | Archived | Rejected | Staged | Stale Active | Unresolved Inbox | Fixtures | Source Trace | Next Action |",
        "|---:|---:|---:|---:|---:|---:|---|---|---|",
        (
            f"| {summary['promoted']} | {summary['archived']} | {summary['rejected']} | "
            f"{summary['staged']} | {summary['stale_active']} | {summary['unresolved_inbox']} | "
            f"{summary['fixtures']} | {summary['source_trace']} | {summary['next_action']} |"
        ),
        "",
        "## Notes",
        "",
        "- This report is a summary artifact, not a recall layer.",
        "- Use `ACTIVE.md` and `LEARNINGS.md` for daily recall.",
        "- Use `staged/` and `rejected/` as audit evidence for judgment-heavy changes.",
    ]
    return "\n".join(lines) + "\n"


def build_summary(memory_root: Path) -> dict[str, str | int]:
    active = memory_root / "ACTIVE.md"
    inbox = memory_root / "inbox"
    archive = memory_root / "ARCHIVE"
    staged = memory_root / "staged"
    rejected = memory_root / "rejected"
    fixtures = memory_root / "fixtures"

    staged_count = count_files(staged)
    rejected_count = count_files(rejected)
    archived_count = count_files(archive)
    unresolved_inbox = count_files(inbox)
    stale_active = count_stale_active(active)
    fixtures_summary = fixture_status(fixtures)
    trace_coverage = "n/a"
    proposal_files = list(staged.rglob("proposal.md")) if staged.exists() else []
    if proposal_files:
        with_trace = 0
        for path in proposal_files:
            text = path.read_text(encoding="utf-8").lower()
            if "source_trace" in text or "source trace" in text:
                with_trace += 1
        trace_coverage = f"{with_trace}/{len(proposal_files)}"
    return {
        "date": date.today().isoformat(),
        "memory_root": str(memory_root),
        "promoted": 0,
        "archived": archived_count,
        "rejected": rejected_count,
        "staged": staged_count,
        "stale_active": stale_active,
        "unresolved_inbox": unresolved_inbox,
        "fixtures": fixtures_summary,
        "source_trace": trace_coverage,
        "next_action": "Review staged proposals and gate evidence",
    }


def render_html_report(memory_root: Path) -> str:
    summary = build_summary(memory_root)
    cells = [
        "promoted",
        "archived",
        "rejected",
        "staged",
        "stale_active",
        "unresolved_inbox",
        "fixtures",
        "source_trace",
        "next_action",
    ]
    headers = [
        "Promoted",
        "Archived",
        "Rejected",
        "Staged",
        "Stale Active",
        "Unresolved Inbox",
        "Fixtures",
        "Source Trace",
        "Next Action",
    ]
    header_html = "".join(f"<th>{escape(label)}</th>" for label in headers)
    row_html = "".join(f"<td>{escape(str(summary[key]))}</td>" for key in cells)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Dream Loop Nightly Report</title>
  <style>
    body {{ font-family: system-ui, sans-serif; margin: 32px; color: #111827; }}
    table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
    th, td {{ border: 1px solid #d1d5db; padding: 8px 10px; text-align: left; }}
    th {{ background: #f3f4f6; }}
    code {{ background: #f3f4f6; padding: 2px 4px; border-radius: 4px; }}
  </style>
</head>
<body>
  <h1>Dream Loop Nightly Report</h1>
  <p>Date: {escape(str(summary["date"]))}</p>
  <p>Memory root: <code>{escape(str(summary["memory_root"]))}</code></p>
  <table>
    <thead><tr>{header_html}</tr></thead>
    <tbody><tr>{row_html}</tr></tbody>
  </table>
  <h2>Notes</h2>
  <ul>
    <li>Reports are not recall layers.</li>
    <li>Use <code>ACTIVE.md</code> and <code>LEARNINGS.md</code> for daily recall.</li>
    <li>Use <code>staged/</code> and <code>rejected/</code> as audit evidence for judgment-heavy changes.</li>
  </ul>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a compact Dream Loop nightly report.")
    sub = parser.add_subparsers(dest="command")
    replay = sub.add_parser("replay", help="Replay lightweight fixture shape checks.")
    replay.add_argument(
        "--fixtures-root",
        default=str(Path(__file__).resolve().parents[1] / "examples" / "minimal-global" / ".codex" / "memory" / "fixtures"),
        help="Path to fixture yaml files.",
    )
    parser.add_argument(
        "--memory-root",
        default=str(Path(__file__).resolve().parents[1] / "templates" / "global" / ".codex" / "memory"),
        help="Path to the Dream Loop memory root.",
    )
    parser.add_argument("--output", help="Optional file path for the generated markdown report.")
    parser.add_argument("--format", choices=("markdown", "html"), default="markdown", help="Report output format.")
    args = parser.parse_args()

    if args.command == "replay":
        result = replay_fixtures(Path(args.fixtures_root).resolve())
        print(f"Replay fixtures: {result.passed}/{result.total}")
        for failure in result.failures:
            print(f"- failed: {failure}")
        return 0 if not result.failures else 1

    memory_root = Path(args.memory_root).resolve()
    report = render_html_report(memory_root) if args.format == "html" else render_report(memory_root)

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
