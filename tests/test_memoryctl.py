import shutil
import unittest
from pathlib import Path

from scripts.memoryctl import forget_entry


TMP_ROOT = Path(__file__).resolve().parent / "tmp_memoryctl"


class MemoryCtlTests(unittest.TestCase):
    def setUp(self):
        shutil.rmtree(TMP_ROOT, ignore_errors=True)
        TMP_ROOT.mkdir(parents=True, exist_ok=True)
        (TMP_ROOT / "LEARNINGS.md").write_text(
            "# LEARNINGS\n\n"
            "- [LRN-20260617-001] route to forget\n"
            "  Evidence: source session\n\n"
            "- [LRN-20260617-002] route to keep\n"
            "  Evidence: source session\n",
            encoding="utf-8",
        )
        (TMP_ROOT / "AUDIT_LOG.md").write_text("# AUDIT_LOG\n\n## Audit Trail\n", encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(TMP_ROOT, ignore_errors=True)

    def test_forget_removes_entry_from_default_recall_and_writes_tombstone(self):
        result = forget_entry(
            memory_root=TMP_ROOT,
            entry_id="LRN-20260617-001",
            reason="user requested removal",
            scope="repo",
        )

        learnings = (TMP_ROOT / "LEARNINGS.md").read_text(encoding="utf-8")
        audit = (TMP_ROOT / "AUDIT_LOG.md").read_text(encoding="utf-8")
        forgotten_files = list((TMP_ROOT / "ARCHIVE" / "forgotten").glob("*.md"))

        self.assertTrue(result.archived_path.exists())
        self.assertEqual(len(forgotten_files), 1)
        self.assertNotIn("LRN-20260617-001", learnings)
        self.assertIn("LRN-20260617-002", learnings)
        self.assertIn("Action: forget", audit)
        self.assertIn("user requested removal", audit)


if __name__ == "__main__":
    unittest.main()
