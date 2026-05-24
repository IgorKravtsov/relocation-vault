#!/usr/bin/env python3
"""
Verify all [src-NNN] references in *.md files resolve in sources/sources.md,
and detect unused (orphan) sources.

Usage:
    python3 scripts/check-sources.py

Exit codes:
    0 — no missing references
    1 — missing references (unused sources are warnings, not errors)
"""

import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = VAULT_ROOT / "sources" / "sources.md"

SRC_REF_PATTERN = re.compile(r"\[(src-[a-zA-Z0-9_-]+)\]")
SRC_DEF_PATTERN = re.compile(r"^## (src-[a-zA-Z0-9_-]+)", re.MULTILINE)

IGNORE_DIRS = {"archive", ".git", "scripts"}

# Literal placeholders that appear in documentation/templates as examples,
# not as real references.
PLACEHOLDER_IDS = {
    "src-NNN",
    "src-XXX",
    "src-YYY",
    "src-N",
}


def main():
    if not SOURCES_FILE.exists():
        print(f"ERROR: {SOURCES_FILE} not found")
        sys.exit(2)

    sources_text = SOURCES_FILE.read_text(encoding="utf-8")
    defined = set(SRC_DEF_PATTERN.findall(sources_text))

    referenced = set()
    references_by_file: dict[Path, set[str]] = {}

    for path in VAULT_ROOT.rglob("*.md"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path == SOURCES_FILE:
            continue
        text = path.read_text(encoding="utf-8")
        refs = set(SRC_REF_PATTERN.findall(text)) - PLACEHOLDER_IDS
        if refs:
            references_by_file[path] = refs
            referenced.update(refs)

    missing = referenced - defined
    unused = defined - referenced

    print(f"Sources defined:    {len(defined)}")
    print(f"Sources referenced: {len(referenced)}\n")

    if missing:
        print("MISSING (referenced but not defined in sources.md):")
        for ref in sorted(missing):
            files = [
                str(p.relative_to(VAULT_ROOT))
                for p, r in references_by_file.items()
                if ref in r
            ]
            print(f"  - {ref}  used in: {', '.join(files)}")
        print()

    if unused:
        print("WARN UNUSED (defined but not referenced anywhere):")
        for ref in sorted(unused):
            print(f"  - {ref}")
        print()

    if not missing and not unused:
        print("OK: all source references resolved, no orphans")
    elif not missing:
        print("OK: all referenced sources resolved (unused sources are warnings only)")

    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
