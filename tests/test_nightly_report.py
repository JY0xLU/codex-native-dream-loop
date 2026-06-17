import subprocess
import sys
import shutil
import unittest
from pathlib import Path

from scripts.nightly_report import fixture_status, render_html_report, render_report, replay_fixtures


TMP_ROOT = Path(__file__).resolve().parent / "tmp_nightly_report"


class NightlyReportTests(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(TMP_ROOT, ignore_errors=True)
        TMP_ROOT.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(TMP_ROOT, ignore_errors=True)

    def test_fixture_status_requires_non_empty_expectations(self):
        root = TMP_ROOT / "fixtures"
        root.mkdir()
        (root / "good.yaml").write_text(
            "id: good\n"
            "description: good fixture\n"
            "critical: true\n"
            "expects:\n"
            "  - has source trace\n"
            "  - has rollback clue\n",
            encoding="utf-8",
        )
        (root / "bad.yaml").write_text(
            "id: bad\n"
            "description: bad fixture\n"
            "critical: true\n"
            "expects:\n",
            encoding="utf-8",
        )

        self.assertEqual(fixture_status(root), "1/2")

    def test_render_report_counts_source_trace_coverage(self):
        root = TMP_ROOT / "memory"
        root.mkdir()
        (root / "ACTIVE.md").write_text("# ACTIVE\n", encoding="utf-8")
        (root / "inbox").mkdir()
        (root / "ARCHIVE").mkdir()
        (root / "rejected").mkdir()
        (root / "fixtures").mkdir()
        staged_a = root / "staged" / "a"
        staged_b = root / "staged" / "b"
        staged_a.mkdir(parents=True)
        staged_b.mkdir(parents=True)
        (staged_a / "proposal.md").write_text("source_trace: session-1\n", encoding="utf-8")
        (staged_b / "proposal.md").write_text("no trace yet\n", encoding="utf-8")

        report = render_report(root)

        self.assertIn("| 0 | 0 | 0 | 2 | 0 | 0 | 0/0 | 1/2 |", report)

    def test_render_html_report_contains_table_and_escapes_paths(self):
        root = TMP_ROOT / "memory html"
        root.mkdir()
        (root / "ACTIVE.md").write_text("# ACTIVE\n", encoding="utf-8")
        (root / "inbox").mkdir()
        (root / "ARCHIVE").mkdir()
        (root / "rejected").mkdir()
        (root / "fixtures").mkdir()

        html = render_html_report(root)

        self.assertIn("<table>", html)
        self.assertIn("Dream Loop Nightly Report", html)
        self.assertIn("memory html", html)
        self.assertIn("Reports are not recall layers", html)

    def test_replay_fixtures_reports_passed_and_failed_fixture_files(self):
        root = TMP_ROOT / "replay"
        root.mkdir()
        (root / "good.yaml").write_text(
            "id: good\n"
            "description: good fixture\n"
            "expects:\n"
            "  - source trace exists\n",
            encoding="utf-8",
        )
        (root / "bad.yaml").write_text(
            "id: bad\n"
            "description: missing expected checks\n"
            "expects:\n",
            encoding="utf-8",
        )

        result = replay_fixtures(root)

        self.assertEqual(result.passed, 1)
        self.assertEqual(result.total, 2)
        self.assertEqual(result.failures, ["bad.yaml"])

    def test_replay_cli_returns_nonzero_when_a_fixture_fails(self):
        root = TMP_ROOT / "cli-replay"
        root.mkdir()
        (root / "bad.yaml").write_text(
            "id: bad\n"
            "description: missing expected checks\n"
            "expects:\n",
            encoding="utf-8",
        )

        completed = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).resolve().parents[1] / "scripts" / "nightly_report.py"),
                "replay",
                "--fixtures-root",
                str(root),
            ],
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(completed.returncode, 1)
        self.assertIn("Replay fixtures: 0/1", completed.stdout)
        self.assertIn("bad.yaml", completed.stdout)


if __name__ == "__main__":
    unittest.main()
