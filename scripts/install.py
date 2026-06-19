#!/usr/bin/env python3
"""Install Dream Loop skills and templates into a Codex home directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CODEX_HOME = Path.home() / ".codex"


def copy_tree(src: Path, dst: Path, *, apply: bool) -> list[str]:
    actions: list[str] = []
    if not src.exists():
        raise FileNotFoundError(src)
    for path in src.rglob("*"):
        rel = path.relative_to(src)
        target = dst / rel
        if path.is_dir():
            if apply:
                target.mkdir(parents=True, exist_ok=True)
            continue
        actions.append(f"{path} -> {target}")
        if apply:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
    return actions


def install(codex_home: Path, *, apply: bool) -> list[str]:
    actions: list[str] = []
    actions.extend(copy_tree(ROOT / "skills", codex_home / "skills", apply=apply))
    actions.extend(copy_tree(ROOT / "templates" / "global", codex_home, apply=apply))
    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description="Install CoDream Loop into a Codex home directory.")
    parser.add_argument("--codex-home", default=str(DEFAULT_CODEX_HOME), help="Target Codex home directory.")
    parser.add_argument("--apply", action="store_true", help="Actually copy files. Omit for dry-run.")
    args = parser.parse_args()

    codex_home = Path(args.codex_home).expanduser().resolve()
    actions = install(codex_home, apply=args.apply)

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"Dream Loop install: {mode}")
    print(f"Target Codex home: {codex_home}")
    print(f"Planned file copies: {len(actions)}")
    for action in actions:
        print(f"- {action}")
    if not args.apply:
        print("Run again with --apply to copy files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
