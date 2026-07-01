#!/usr/bin/env python3
"""Install HTML Presentation Skill globally or into a project."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


SKILL_NAME = "html-presentation-skill"
MARKER_START = "<!-- html-presentation-skill:start -->"
MARKER_END = "<!-- html-presentation-skill:end -->"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_ignore(directory: str, names: list[str]) -> set[str]:
    ignored = {".git", ".codex", ".claude", "__pycache__", ".DS_Store"}
    ignored.update(name for name in names if name.endswith(".pyc"))
    return ignored


def copy_skill(source: Path, target: Path, *, force: bool = False, dry_run: bool = False) -> None:
    if target.exists():
        if not force:
            raise FileExistsError(f"Target already exists: {target}. Re-run with --force to replace it.")
        if dry_run:
            return
        shutil.rmtree(target)
    if dry_run:
        return
    shutil.copytree(source, target, ignore=copy_ignore)


def codex_target(scope: str, project: Path) -> Path:
    if scope == "global":
        codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
        return codex_home / "skills" / SKILL_NAME
    return project / ".codex" / "skills" / SKILL_NAME


def upsert_marked_block(path: Path, title: str, body: str, *, dry_run: bool = False) -> None:
    if dry_run:
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    block = f"{MARKER_START}\n# {title}\n\n{body.strip()}\n{MARKER_END}\n"

    if path.exists():
        current = path.read_text(encoding="utf-8")
    else:
        current = ""

    if MARKER_START in current and MARKER_END in current:
        before = current.split(MARKER_START, 1)[0].rstrip()
        after = current.split(MARKER_END, 1)[1].lstrip()
        new_content = "\n\n".join(part for part in [before, block.strip(), after] if part).rstrip() + "\n"
    else:
        separator = "\n\n" if current.strip() else ""
        new_content = current.rstrip() + separator + block

    path.write_text(new_content, encoding="utf-8")


def bridge_body(relative_skill_path: str) -> str:
    return f"""
Use the HTML Presentation Skill when asked to create, convert, or improve an HTML presentation from documents, notes, reports, briefs, outlines, or raw content.

Before generating a presentation, read:

- `{relative_skill_path}/SKILL.md`
- `{relative_skill_path}/references/workflow.md`
- `{relative_skill_path}/references/style-presets.md`
- `{relative_skill_path}/references/agent-decisions.md`
- `{relative_skill_path}/references/brand-assets.md` when brand assets are provided
- `{relative_skill_path}/references/presentation-pattern-library.md` when choosing section layouts

Default behavior:

- Generate a standalone `.html` file with embedded CSS and JavaScript.
- Ask for a visual style preset when the user has not specified one and the task allows clarification.
- Scan the workspace for brand/product assets or use a user-provided asset folder when available.
- Validate output with `python3 {relative_skill_path}/scripts/validate_presentation.py path/to/presentation.html`.
- Use `--strict` validation for release-ready presentations and examples.
"""


def install_codex(source: Path, scope: str, project: Path, *, force: bool, dry_run: bool) -> Path:
    target = codex_target(scope, project)
    if not dry_run:
        target.parent.mkdir(parents=True, exist_ok=True)
    copy_skill(source, target, force=force, dry_run=dry_run)
    return target


def install_claude(scope: str, project: Path, *, dry_run: bool) -> Path:
    if scope == "global":
        path = Path.home() / ".claude" / "CLAUDE.md"
        skill_path = f"{Path.home() / '.codex' / 'skills' / SKILL_NAME}"
    else:
        path = project / "CLAUDE.md"
        skill_path = f".codex/skills/{SKILL_NAME}"
    upsert_marked_block(path, "HTML Presentation Skill", bridge_body(skill_path), dry_run=dry_run)
    return path


def install_copilot(scope: str, project: Path, *, dry_run: bool) -> Path:
    if scope == "global":
        raise ValueError("GitHub Copilot repository instructions are local to a repository. Use --scope local for copilot.")
    path = project / ".github" / "copilot-instructions.md"
    upsert_marked_block(path, "HTML Presentation Skill", bridge_body(f".codex/skills/{SKILL_NAME}"), dry_run=dry_run)
    return path


def install_antigravity(scope: str, project: Path, *, dry_run: bool) -> Path:
    if scope == "global":
        raise ValueError("Antigravity project instructions are best installed locally. Use --scope local for antigravity.")
    path = project / "AGENTS.md"
    upsert_marked_block(path, "HTML Presentation Skill", bridge_body(f".codex/skills/{SKILL_NAME}"), dry_run=dry_run)
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install HTML Presentation Skill for coding agents.")
    parser.add_argument("--scope", choices=["global", "local"], default="global", help="Install globally or into a project.")
    parser.add_argument(
        "--agents",
        default="codex",
        help="Comma-separated agents: codex,claude,copilot,antigravity,all.",
    )
    parser.add_argument("--project", default=".", help="Project directory for local installs.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes without writing files.")
    parser.add_argument("--force", action="store_true", help="Replace an existing installed Codex skill directory.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = repo_root()
    project = Path(args.project).resolve()

    if args.scope == "local":
        if not project.exists():
            print(f"ERROR: project directory not found: {project}")
            return 2
        if not project.is_dir():
            print(f"ERROR: project path is not a directory: {project}")
            return 2

    requested = {agent.strip().lower() for agent in args.agents.split(",") if agent.strip()}
    if "all" in requested:
        requested = {"codex", "claude", "copilot", "antigravity"}

    installed: list[str] = []
    errors: list[str] = []
    prefix = "DRY-RUN" if args.dry_run else "OK"

    if "codex" in requested or requested & {"claude", "copilot", "antigravity"}:
        try:
            target = install_codex(source, args.scope, project, force=args.force, dry_run=args.dry_run)
            installed.append(f"Codex skill files -> {target}")
        except FileExistsError as exc:
            errors.append(str(exc))

    for agent in sorted(requested - {"codex"}):
        try:
            if agent == "claude":
                installed.append(f"Claude instructions -> {install_claude(args.scope, project, dry_run=args.dry_run)}")
            elif agent == "copilot":
                installed.append(f"Copilot instructions -> {install_copilot(args.scope, project, dry_run=args.dry_run)}")
            elif agent == "antigravity":
                installed.append(
                    f"Antigravity/generic agent instructions -> {install_antigravity(args.scope, project, dry_run=args.dry_run)}"
                )
            else:
                errors.append(f"Unknown agent: {agent}")
        except ValueError as exc:
            errors.append(str(exc))

    for item in installed:
        print(f"{prefix}: {item}")
    for error in errors:
        print(f"WARNING: {error}")

    if args.dry_run:
        print("DRY-RUN: no files changed.")
    elif installed:
        print("NEXT: Ask your agent to use $html-presentation-skill for an HTML presentation task.")

    if errors and not installed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
