#!/usr/bin/env python3
"""Dependency-free structural checks for CoDream Loop."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "assets/hero-logo.png",
    "assets/32x32.png",
    ".codex-plugin/plugin.json",
    "automations/nightly-dream-loop.md",
    "templates/global/AGENTS.snippet.md",
    "templates/global/.codex/memory/ACTIVE.md",
    "templates/global/.codex/memory/LEARNINGS.md",
    "templates/global/.codex/memory/AUDIT_LOG.md",
    "templates/global/.codex/memory/inbox/README.md",
    "templates/global/.codex/memory/staged/README.md",
    "templates/global/.codex/memory/rejected/README.md",
    "templates/global/.codex/memory/fixtures/README.md",
    "templates/global/.codex/memory/reports/README.md",
    "templates/global/.codex/memory/ARCHIVE/README.md",
    "examples/minimal-global/.codex/memory/ACTIVE.md",
    "examples/minimal-global/.codex/memory/LEARNINGS.md",
    "examples/minimal-global/.codex/memory/AUDIT_LOG.md",
    "examples/minimal-global/.codex/memory/staged/2026-06-17-nightly/proposal.md",
    "examples/minimal-global/.codex/memory/rejected/2026-06-17-nightly/reject_reason.md",
    "examples/minimal-global/.codex/memory/fixtures/readme-visual-style.yaml",
    "examples/minimal-global/.codex/memory/fixtures/pr-audit-route.yaml",
    "examples/minimal-global/.codex/memory/fixtures/install-skill-route.yaml",
    "examples/minimal-global/.codex/memory/fixtures/repo-vs-global-memory.yaml",
    "examples/minimal-global/.codex/memory/fixtures/nightly-report-generation.yaml",
    "examples/minimal-global/.codex/memory/reports/2026-06-17-nightly.md",
    "skills/capture-memory/SKILL.md",
    "skills/capability-evolution/SKILL.md",
    "skills/dream-consolidate/SKILL.md",
    "references/validation-gate.md",
    "references/trellis-workflow.md",
    "references/research-adoption-trace.md",
    "scripts/install.py",
    "scripts/memoryctl.py",
    "scripts/nightly_report.py",
]

SKILL_FILES = [
    "skills/capture-memory/SKILL.md",
    "skills/capability-evolution/SKILL.md",
    "skills/dream-consolidate/SKILL.md",
]

MOJIBAKE_MARKERS = [
    "\ufffd",
    "鈥",
    "涓",
    "锛",
    "闂",
    "鎶",
    "瀵",
    "鑷",
    "渚",
    "乣",
    "绋",
    "惧",
]


def rel(path: str) -> Path:
    return ROOT / path


def check_required_paths(errors: list[str]) -> None:
    for item in REQUIRED_PATHS:
        if not rel(item).exists():
            errors.append(f"missing required path: {item}")


def check_skill_frontmatter(errors: list[str]) -> None:
    for item in SKILL_FILES:
        path = rel(item)
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"missing frontmatter start: {item}")
            continue
        end = text.find("\n---", 4)
        if end == -1:
            errors.append(f"missing frontmatter end: {item}")
            continue
        frontmatter = text[4:end]
        for key in ("name:", "description:"):
            if key not in frontmatter:
                errors.append(f"missing {key} in frontmatter: {item}")


def check_local_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            for match in link_pattern.finditer(line):
                target = match.group(1).strip()
                if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = target.split("#", 1)[0]
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                if not (path.parent / target).exists():
                    errors.append(f"missing local markdown target: {path.relative_to(ROOT)}:{line_no} -> {target}")


def check_mojibake(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), 1):
            if any(marker in line for marker in MOJIBAKE_MARKERS):
                errors.append(f"possible mojibake: {path.relative_to(ROOT)}:{line_no}")


def main() -> int:
    errors: list[str] = []
    check_required_paths(errors)
    check_skill_frontmatter(errors)
    check_local_markdown_links(errors)
    check_mojibake(errors)

    if errors:
        print("Dream Loop doctor: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Dream Loop doctor: OK")
    print("Severity: must checks passed")
    print(f"- checked {len(REQUIRED_PATHS)} required paths")
    print(f"- checked {len(SKILL_FILES)} skill frontmatter blocks")
    print("- checked local markdown links")
    print("- checked markdown/yaml UTF-8 mojibake markers")
    print("Info: optional runtime checks such as live automation status and transcript replay are outside this structural doctor.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
