#!/usr/bin/env python3
"""Bootstrap a Figma design workspace from the /jfd skill templates.

Dependency-free (pathlib/shutil only) so it runs on macOS, Windows, and
Linux. It only creates missing files and skill copies; it never overwrites
existing project content and never calls Figma or any MCP.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import List, Tuple

SKILL_NAME = "justin-figma-design"

TEMPLATE_FILES: Tuple[str, ...] = (
    "AGENTS.md",
    "docs/README.md",
    "docs/preferences.md",
    "docs/FILES.md",
    "docs/tools/figma-console.md",
    "docs/sessions/_template.md",
    "docs/assets/README.md",
    "docs/assets/icons.md",
    "docs/assets/avatars/README.md",
    "docs/files/_template/design.md",
    "docs/files/_template/screens.md",
)

SKILL_DESTINATIONS: Tuple[str, ...] = (
    f".agents/skills/{SKILL_NAME}",
    f".cursor/skills/{SKILL_NAME}",
)


def package_root() -> Path:
    """Root directory of the installed skill package (parent of scripts/)."""
    return Path(__file__).resolve().parent.parent


def rel(path: Path, root: Path) -> str:
    """Format a path relative to the workspace when possible."""
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def exists_including_broken_link(path: Path) -> bool:
    """Treat a broken symlink as existing so init never replaces it."""
    return path.exists() or path.is_symlink()


def is_same_or_child(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def confirm_non_empty(root: Path, assume_yes: bool) -> bool:
    """Ask before writing into a non-empty workspace."""
    if assume_yes or not any(root.iterdir()):
        return True
    prompt = (
        f"{root} is not empty. Create only missing /jfd files and skill "
        "copies without overwriting existing paths? [y/N] "
    )
    if not sys.stdin.isatty():
        print(
            "Refusing to write into a non-empty workspace from a "
            "non-interactive session. Re-run with --yes after reviewing "
            "the target.",
            file=sys.stderr,
        )
        return False
    try:
        answer = input(prompt)
    except EOFError:
        return False
    return answer.strip().lower() in {"y", "yes"}


def plan_template_copies(root: Path, templates: Path) -> Tuple[List[Tuple[Path, Path]], List[Path]]:
    """Return (missing template copies, existing paths to skip)."""
    to_copy: List[Tuple[Path, Path]] = []
    skipped: List[Path] = []
    for relative in TEMPLATE_FILES:
        source = templates / relative
        destination = root / relative
        if not source.is_file():
            print(f"warning: template missing from package: {relative}", file=sys.stderr)
            continue
        if exists_including_broken_link(destination):
            skipped.append(destination)
        else:
            to_copy.append((source, destination))
    return to_copy, skipped


def plan_skill_installs(root: Path, source_root: Path) -> Tuple[List[Path], List[Path]]:
    """Return (missing skill install destinations, existing ones to skip)."""
    to_install: List[Path] = []
    skipped: List[Path] = []
    for relative in SKILL_DESTINATIONS:
        destination = root / relative
        if exists_including_broken_link(destination):
            skipped.append(destination)
        elif is_same_or_child(source_root, destination) or is_same_or_child(destination, source_root):
            # Never copy the package into (or over) itself.
            skipped.append(destination)
        else:
            to_install.append(destination)
    return to_install, skipped


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Workspace root to initialize (default: current directory).",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the non-empty-workspace confirmation after reviewing the target.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List missing files and skill copies without writing anything.",
    )
    args = parser.parse_args(argv)

    root = args.root.expanduser().resolve()
    if not root.exists():
        print(f"error: workspace root does not exist: {root}", file=sys.stderr)
        return 2
    if not root.is_dir():
        print(f"error: workspace root is not a directory: {root}", file=sys.stderr)
        return 2

    source_root = package_root()
    templates = source_root / "assets" / "templates"
    if not templates.is_dir():
        print(f"error: template directory missing: {templates}", file=sys.stderr)
        return 2

    copies, skipped_files = plan_template_copies(root, templates)
    installs, skipped_skills = plan_skill_installs(root, source_root)

    if not copies and not installs:
        print("Nothing to do: every scaffold path and skill copy already exists.")
        return 0

    print("Missing scaffold files:")
    for _, destination in copies:
        print(f"  + {rel(destination, root)}")
    if not copies:
        print("  (none)")
    print("Missing skill copies:")
    for destination in installs:
        print(f"  + {rel(destination, root)}/")
    if not installs:
        print("  (none)")
    for destination in [*skipped_files, *skipped_skills]:
        print(f"  = exists, skipped: {rel(destination, root)}")

    if args.dry_run:
        print("Dry run: nothing written.")
        return 0

    if not confirm_non_empty(root, args.yes):
        return 1

    for source, destination in copies:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        print(f"created {rel(destination, root)}")

    for destination in installs:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(
            source_root,
            destination,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
        )
        print(f"installed {rel(destination, root)}/")

    print("Init complete. Init never opens Figma; connect Figma Console MCP "
          "and the Desktop Bridge before design work.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
