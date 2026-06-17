#!/usr/bin/env python3
"""Small memory control actions for Dream Loop memory roots."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


RECALL_FILES = ("ACTIVE.md", "LEARNINGS.md")


@dataclass(frozen=True)
class ForgetResult:
    source_file: Path
    archived_path: Path


def _now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _split_entry_blocks(text: str) -> list[str]:
    lines = text.splitlines(keepends=True)
    blocks: list[str] = []
    current: list[str] = []
    for line in lines:
        if line.startswith("- [") and current:
            blocks.append("".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append("".join(current))
    return blocks


def _remove_entry(text: str, entry_id: str) -> tuple[str, str]:
    kept: list[str] = []
    removed = ""
    for block in _split_entry_blocks(text):
        first_line = block.splitlines()[0] if block.splitlines() else ""
        if f"[{entry_id}]" in first_line:
            removed = block
        else:
            kept.append(block)
    return "".join(kept).rstrip() + "\n", removed


def _append_audit(memory_root: Path, *, entry_id: str, reason: str, scope: str, source_file: Path, archived_path: Path) -> None:
    audit_path = memory_root / "AUDIT_LOG.md"
    if not audit_path.exists():
        audit_path.write_text("# AUDIT_LOG\n\n## Audit Trail\n", encoding="utf-8")
    stamp = _now_stamp()
    audit = (
        f"\n## [AUDIT-{stamp}-{entry_id}]\n"
        f"Timestamp: {datetime.now(timezone.utc).isoformat()}\n"
        "Action: forget\n"
        f"Scope: {scope}\n"
        f"Source trace: {source_file.name}:{entry_id}\n"
        "Reviewer verdict: user requested\n"
        "Final decision: retire from default recall\n"
        f"Rollback clue: restore `{archived_path.relative_to(memory_root)}` to `{source_file.name}` if the forget action is reversed\n"
        f"Target: {archived_path.relative_to(memory_root)}\n"
        f"Reason: {reason}\n"
    )
    with audit_path.open("a", encoding="utf-8") as handle:
        handle.write(audit)


def forget_entry(memory_root: Path, entry_id: str, reason: str, scope: str = "repo") -> ForgetResult:
    memory_root = memory_root.resolve()
    for filename in RECALL_FILES:
        path = memory_root / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        updated, removed = _remove_entry(text, entry_id)
        if not removed:
            continue
        archive_dir = memory_root / "ARCHIVE" / "forgotten"
        archive_dir.mkdir(parents=True, exist_ok=True)
        archived_path = archive_dir / f"{_now_stamp()}-{entry_id}.md"
        archived_path.write_text(
            f"# Forgotten Entry\n\nSource: `{filename}`\nEntry: `{entry_id}`\nReason: {reason}\n\n## Original\n\n{removed}",
            encoding="utf-8",
        )
        path.write_text(updated, encoding="utf-8")
        _append_audit(
            memory_root,
            entry_id=entry_id,
            reason=reason,
            scope=scope,
            source_file=path,
            archived_path=archived_path,
        )
        return ForgetResult(source_file=path, archived_path=archived_path)
    raise ValueError(f"entry id not found in recall files: {entry_id}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Control Dream Loop memory entries.")
    sub = parser.add_subparsers(dest="command", required=True)
    forget = sub.add_parser("forget", help="Remove an entry from default recall and write a tombstone audit.")
    forget.add_argument("entry_id")
    forget.add_argument("--memory-root", required=True)
    forget.add_argument("--reason", required=True)
    forget.add_argument("--scope", default="repo", choices=("global", "repo", "thread"))
    args = parser.parse_args()

    if args.command == "forget":
        result = forget_entry(Path(args.memory_root), args.entry_id, args.reason, args.scope)
        print(f"Forgot {args.entry_id}")
        print(f"Archived: {result.archived_path}")
        print(f"Source file updated: {result.source_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
