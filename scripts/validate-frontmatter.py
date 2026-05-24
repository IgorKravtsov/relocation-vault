#!/usr/bin/env python3
"""
Validate YAML frontmatter in countries/*.md and runs/*.md.

Schemas per vault-protocol.md §3.1 and §3.2.

Usage:
    python3 scripts/validate-frontmatter.py

Exit codes:
    0 — all files pass
    1 — at least one file has errors
"""

import sys
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip3 install pyyaml")
    sys.exit(2)


VAULT_ROOT = Path(__file__).resolve().parent.parent

# Type for ISO date/datetime fields: PyYAML may auto-parse ISO strings into
# date/datetime objects. Accept str or date/datetime.
DATE_LIKE = (str, date, datetime)

COUNTRY_REQUIRED_FIELDS = {
    "country": str,
    "tier": (int, type(None), str),
    "depth_score": (int, float),
    "last_updated": DATE_LIKE,
    "sections_completed": list,
    "sections_partial": list,
    "sections_pending": list,
    "risk_flags": list,
    "sources_used": list,
    "unverified_count": int,
    "schema_version": str,
}

RUN_REQUIRED_FIELDS = {
    "run_id": int,
    "date": DATE_LIKE,
    "agent": str,
    "mode": str,
    "status": str,
    "schema_version": str,
}

VALID_MODES = {
    "bootstrap",
    "country-deep-dive",
    "criterion-slice",
    "verification",
    "cross-reference",
    "staleness-check",
    "consolidation",
    "proposal-apply",
    "recovery",
}

VALID_STATUSES = {"completed", "aborted", "partial"}
VALID_TIERS = {1, 2, 3, "X", None}


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        end = text.find("\n---", 4)
        if end == -1:
            return None
    try:
        return yaml.safe_load(text[4:end])
    except yaml.YAMLError as e:
        return {"__parse_error__": str(e)}


def validate_fields(data, required):
    errors = []
    for field, expected_type in required.items():
        if field not in data:
            errors.append(f"missing field: {field}")
            continue
        value = data[field]
        if isinstance(expected_type, tuple):
            if not isinstance(value, expected_type):
                names = ", ".join(t.__name__ if hasattr(t, "__name__") else str(t) for t in expected_type)
                errors.append(f"{field}: type {type(value).__name__} not in ({names})")
        else:
            if not isinstance(value, expected_type):
                errors.append(
                    f"{field}: expected {expected_type.__name__}, got {type(value).__name__}"
                )
    return errors


def validate_country_file(path: Path):
    data = parse_frontmatter(path)
    if data is None:
        return ["no valid YAML frontmatter"]
    if "__parse_error__" in data:
        return [f"YAML parse error: {data['__parse_error__']}"]

    errors = validate_fields(data, COUNTRY_REQUIRED_FIELDS)

    if "tier" in data and data["tier"] not in VALID_TIERS:
        errors.append(f"tier: invalid value {data['tier']!r} (must be 1, 2, 3, 'X', or null)")

    if "depth_score" in data:
        d = data["depth_score"]
        if isinstance(d, (int, float)) and not 0 <= d <= 10:
            errors.append(f"depth_score: {d} out of range [0, 10]")

    return errors


def validate_run_file(path: Path):
    data = parse_frontmatter(path)
    if data is None:
        return ["no valid YAML frontmatter"]
    if "__parse_error__" in data:
        return [f"YAML parse error: {data['__parse_error__']}"]

    errors = validate_fields(data, RUN_REQUIRED_FIELDS)

    if "mode" in data and data["mode"] not in VALID_MODES:
        errors.append(f"mode: invalid value {data['mode']!r}")
    if "status" in data and data["status"] not in VALID_STATUSES:
        errors.append(f"status: invalid value {data['status']!r}")

    return errors


def main():
    countries_dir = VAULT_ROOT / "countries"
    runs_dir = VAULT_ROOT / "runs"

    print(f"Validating frontmatter under {VAULT_ROOT}\n")

    total = 0
    failed = 0

    if countries_dir.exists():
        for path in sorted(countries_dir.glob("*.md")):
            if path.name == "_TEMPLATE.md":
                continue
            total += 1
            errors = validate_country_file(path)
            rel = path.relative_to(VAULT_ROOT)
            if errors:
                failed += 1
                print(f"ERROR {rel}")
                for e in errors:
                    print(f"      - {e}")
            else:
                print(f"OK    {rel}")

    if runs_dir.exists():
        for path in sorted(runs_dir.glob("*.md")):
            total += 1
            errors = validate_run_file(path)
            rel = path.relative_to(VAULT_ROOT)
            if errors:
                failed += 1
                print(f"ERROR {rel}")
                for e in errors:
                    print(f"      - {e}")
            else:
                print(f"OK    {rel}")

    print(f"\n{total - failed}/{total} files OK")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
