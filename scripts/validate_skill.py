"""Validate the repository's Codex skill without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = (
    "## 1. Establish the task boundary",
    "## 2. Separate evidence from interpretation",
    "## 3. Gather the cheapest sufficient evidence",
    "## 4. Decide when to ask the user",
    "## 5. Respect action and authorization boundaries",
    "## 6. Report conclusions honestly",
    "## 7. Stop at the evidence boundary",
    "## 8. Avoid over-application",
)


def fail(message: str) -> int:
    print(f"ERROR: {message}")
    return 1


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) == 2 else ".").resolve()
    skill_path = root / "SKILL.md"
    metadata_path = root / "agents" / "openai.yaml"

    if not skill_path.is_file():
        return fail("SKILL.md is missing")
    if not metadata_path.is_file():
        return fail("agents/openai.yaml is missing")

    content = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
    if not match:
        return fail("SKILL.md frontmatter is missing or malformed")

    frontmatter = match.group(1)
    name_match = re.search(r"^name:\s*([^\r\n]+)$", frontmatter, re.MULTILINE)
    description_match = re.search(
        r"^description:\s*(.+)$", frontmatter, re.MULTILINE
    )
    if not name_match or name_match.group(1).strip() != "evidence-discipline":
        return fail("frontmatter name must be evidence-discipline")
    if not description_match or not description_match.group(1).strip():
        return fail("frontmatter description is missing")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name_match.group(1).strip()):
        return fail("frontmatter name must use lowercase hyphen-case")
    if "[TODO:" in content or "[TODO:" in metadata_path.read_text(encoding="utf-8"):
        return fail("unfinished TODO marker found")

    missing_sections = [section for section in REQUIRED_SECTIONS if section not in content]
    if missing_sections:
        return fail("missing required sections: " + ", ".join(missing_sections))

    metadata = metadata_path.read_text(encoding="utf-8")
    if "display_name:" not in metadata or "short_description:" not in metadata:
        return fail("openai.yaml interface metadata is incomplete")

    print("Skill validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
