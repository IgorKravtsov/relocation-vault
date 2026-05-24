#!/usr/bin/env python3
"""
Find atomic claims older than the staleness threshold for their type
(per vault-protocol.md §16).

Usage:
    python3 scripts/find-stale.py

Exit codes:
    0 — no stale claims
    1 — at least one stale claim found
"""

import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip3 install pyyaml")
    sys.exit(2)


VAULT_ROOT = Path(__file__).resolve().parent.parent
CLAIMS_DIR = VAULT_ROOT / "claims"

# Staleness thresholds in days, by substring match on `topic`.
# First match wins. Keep ordering: more specific keywords first.
THRESHOLDS = [
    ("climate", 0),         # 0 = no staleness check
    ("school", 365),
    ("kindergarten", 365),
    ("tax", 365),
    ("pr_", 365),
    ("citizenship", 365),
    ("visa", 180),
    ("tp_", 180),
    ("vnzh", 180),
    ("rent", 180),
    ("cost", 180),
    ("price", 180),
]
DEFAULT_THRESHOLD_DAYS = 180


def threshold_for_topic(topic: str) -> int:
    topic_lower = (topic or "").lower()
    for keyword, days in THRESHOLDS:
        if keyword in topic_lower:
            return days
    return DEFAULT_THRESHOLD_DAYS


def main():
    if not CLAIMS_DIR.exists():
        print(f"No claims directory at {CLAIMS_DIR}. Nothing to check.")
        sys.exit(0)

    today = date.today()
    stale = []
    parse_errors = 0
    total = 0

    for path in sorted(CLAIMS_DIR.glob("*.yml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            print(f"ERROR parsing {path.name}: {e}")
            parse_errors += 1
            continue
        if not isinstance(data, list):
            continue
        for claim in data:
            total += 1
            if not isinstance(claim, dict):
                continue
            verified_str = claim.get("date_verified")
            if not verified_str:
                continue
            try:
                verified = date.fromisoformat(str(verified_str))
            except ValueError:
                print(f"WARN  {path.name}/{claim.get('id', '?')}: invalid date_verified {verified_str!r}")
                continue
            topic = claim.get("topic", "")
            threshold = threshold_for_topic(topic)
            if threshold == 0:
                continue
            age_days = (today - verified).days
            if age_days > threshold:
                stale.append(
                    {
                        "file": path.name,
                        "id": claim.get("id", "?"),
                        "topic": topic,
                        "age_days": age_days,
                        "threshold_days": threshold,
                    }
                )

    print(f"Total claims scanned: {total}")
    print(f"Stale claims:         {len(stale)}")
    if parse_errors:
        print(f"Parse errors:         {parse_errors}")
    print()

    if stale:
        for c in stale:
            print(
                f"STALE  {c['file']}/{c['id']}  "
                f"topic={c['topic']}  age={c['age_days']}d "
                f"(threshold {c['threshold_days']}d)"
            )

    if not stale:
        print("OK: no stale claims")

    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
