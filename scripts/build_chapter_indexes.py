#!/usr/bin/env python3
"""Add or refresh lesson indexes inside chapter README files."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "docs" / "lessons"
START = "<!-- lesson-index:start -->"
END = "<!-- lesson-index:end -->"


def title_from_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip().strip("`")
        if stripped.startswith("**") and stripped.endswith("**"):
            return stripped.strip("*").strip()
    return path.stem.replace("_", " ").replace("-", ": ").title()


def sort_key(path: Path) -> tuple[int, int, str]:
    match = re.match(r"(\d+)\.(\d+)", path.name)
    if match:
        return int(match.group(1)), int(match.group(2)), path.name
    return 999, 999, path.name


def main() -> None:
    updated = 0
    for chapter in sorted(p for p in LESSONS.iterdir() if p.is_dir()):
        readme = chapter / "README.md"
        if not readme.exists():
            continue
        lessons = sorted([p for p in chapter.glob("*.md") if p.name != "README.md"], key=sort_key)
        rows = [START, "", "## Lessons in this chapter", ""]
        for lesson in lessons:
            rows.append(f"- [{title_from_file(lesson)}]({lesson.name})")
        rows.extend(["", END, ""])
        block = "\n".join(rows)
        text = readme.read_text(encoding="utf-8")
        if START in text and END in text:
            text = re.sub(f"{re.escape(START)}.*?{re.escape(END)}\n?", block, text, flags=re.S)
        else:
            text = text.rstrip() + "\n\n" + block
        readme.write_text(text, encoding="utf-8")
        updated += 1
    print(f"Updated chapter indexes: {updated}")


if __name__ == "__main__":
    main()
