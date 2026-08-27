#!/usr/bin/env python3
"""Validate every skill folder in this repository without third-party packages."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    path = skill_dir / "SKILL.md"
    if not path.exists():
        return ["SKILL.md not found"]

    content = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return ["invalid or missing YAML frontmatter"]

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip().strip('"')

    unexpected = set(fields) - ALLOWED_FRONTMATTER
    if unexpected:
        errors.append(f"unexpected frontmatter keys: {', '.join(sorted(unexpected))}")
    name = fields.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("name must be lowercase hyphen-case")
    if len(name) > 64:
        errors.append("name is longer than 64 characters")
    description = fields.get("description", "")
    if not description or description.startswith("[TODO:"):
        errors.append("description is missing or unfinished")
    if "<" in description or ">" in description or len(description) > 1024:
        errors.append("description contains invalid characters or is too long")

    body = content[match.end():]
    fenced = False
    for line in body.splitlines():
        if re.match(r"^\s*(`{3,}|~{3,})", line):
            fenced = not fenced
        elif not fenced and re.fullmatch(r" {0,3}\[TODO:[^\n]*\]\s*", line):
            errors.append("body contains an unfinished TODO")
    return errors


def main() -> int:
    skill_dirs = sorted((ROOT / "skills").iterdir())
    failures = 0
    checked = 0
    for skill_dir in skill_dirs:
        if not skill_dir.is_dir():
            continue
        checked += 1
        errors = validate_skill(skill_dir)
        if errors:
            print(f"{skill_dir.name}: {'; '.join(errors)}", file=sys.stderr)
            failures += 1
    if failures:
        print(f"{failures} skill(s) failed validation.", file=sys.stderr)
        return 1
    print(f"Validated {checked} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
