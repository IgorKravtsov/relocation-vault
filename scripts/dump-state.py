#!/usr/bin/env python3
"""
Print a concise summary of state.json: countries by tier, depth_score
distribution, queue sizes.

Usage:
    python3 scripts/dump-state.py

Exit codes:
    0 — success
    1 — state.json invalid or missing
"""

import json
import sys
from collections import Counter
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE = VAULT_ROOT / "state.json"


def depth_bucket(d):
    if d == 0:
        return "0"
    if d < 4:
        return "1-3"
    if d < 7:
        return "4-6"
    if d < 10:
        return "7-9"
    return "10"


def main():
    if not STATE_FILE.exists():
        print(f"ERROR: {STATE_FILE} not found")
        sys.exit(1)

    try:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERROR parsing state.json: {e}")
        sys.exit(1)

    print(f"=== Vault state ===")
    print(f"Iteration:       {state.get('iteration', '?')}")
    print(f"Last run:        {state.get('last_run_timestamp', '?')}")
    print(f"Schema doc:      {state.get('schema_doc', '?')} v{state.get('schema_doc_version', '?')}")
    print(f"Protocol doc:    {state.get('protocol_doc', '?')} v{state.get('protocol_doc_version', '?')}")
    print()

    current = state.get("current_focus")
    if current:
        print("Current focus:")
        print(f"  mode:     {current.get('mode')}")
        print(f"  country:  {current.get('country')}")
        print(f"  sections: {current.get('sections')}")
    else:
        print("Current focus: (none)")
    print()

    nxt = state.get("next_iteration_hint")
    if nxt:
        print("Next iteration hint:")
        print(f"  mode:     {nxt.get('suggested_mode')}")
        print(f"  country:  {nxt.get('suggested_country')}")
        print(f"  sections: {nxt.get('suggested_sections')}")
        print(f"  reason:   {nxt.get('reason')}")
    print()

    countries = state.get("countries", {})
    total = len(countries)
    tiers = Counter()
    tier_hints = Counter()
    depth_buckets = Counter()

    for name, info in countries.items():
        tier = info.get("tier")
        tiers[tier if tier is not None else "unassigned"] += 1
        tier_hints[info.get("tier_hint", "?")] += 1
        depth_buckets[depth_bucket(info.get("depth_score", 0))] += 1

    print(f"Countries: {total}")
    print()
    print("By assigned tier:")
    for t in [1, 2, 3, "X", "unassigned"]:
        print(f"  Tier {t}: {tiers.get(t, 0)}")
    print()
    print("By tier hint:")
    for h in [1, 2, 3]:
        print(f"  hint {h}: {tier_hints.get(h, 0)}")
    print()
    print("By depth_score bucket:")
    for b in ["0", "1-3", "4-6", "7-9", "10"]:
        print(f"  {b}: {depth_buckets.get(b, 0)}")
    print()

    print(f"Verification queue size: {state.get('verification_queue_size', 0)}")
    print(f"Sources count:           {state.get('sources_count', 0)}")
    print(f"Claims count:            {state.get('claims_count', 0)}")
    print(f"Proposals pending:       {state.get('proposals_pending', 0)}")


if __name__ == "__main__":
    main()
