---
run_id: 293
date: 2026-07-07T03:28:05Z
agent: hermes
mode: staleness-check
target_country: null
target_sections: []
target_criterion: claim-staleness-sweep
duration_minutes: 15
sources_added: []
facts_added: 0
facts_verified: 0
claims_added: []
files_modified:
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-293-claim-staleness-sweep.md
proposals_created: []
completed_at: 2026-07-07T03:28:05Z
status: completed
schema_version: 2.0.0
---

# Run 293 - claim staleness sweep

## Plan

- Execute one focused `staleness-check` unit because there are no accepted proposals, no pending/open verification items, and all country profiles are already at depth 10.0 with assigned screening tiers.
- Confirm whether any loaded claim has crossed its protocol staleness threshold without reopening resolved-for-screening application-prep caveats.

## What was done

- Reran `scripts/find-stale.py` across the current claims corpus.
- Confirmed 716 claim entries were scanned and 0 stale claims were found.
- Recomputed aggregate counts from files: 839 source headings, 716 claim entries, and 0 pending/open verification items.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md` with the staleness-sweep result and downstream handoff note.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.
- Source headings remain 839.
- Claim entries remain 716.
- No country tier, depth score, section status, or country profile changed.

## Key findings

- The vault remains screening-complete and handoff-ready: no stale claims need refresh, no accepted proposal is waiting, and no verification batch is available.
- Future normal work should stay gated by accepted proposals, stale claims, new evidence, or explicit human-directed finalist/application-prep focus; this run did not create a TOP-N ranking or recommendation.

## What remains

- No normal research blocker is open. Downstream synthesis or country-specific application-prep should begin only with explicit direction or a new trigger.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Keep the vault in handoff mode unless proposals, stale sources/claims, new evidence, or explicit finalist/application-prep direction appears.
