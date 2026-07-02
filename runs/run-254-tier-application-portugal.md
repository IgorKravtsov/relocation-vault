---
run_id: 254
date: 2026-07-02T03:02:51Z
agent: hermes
mode: consolidation
target_country: Portugal
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 24
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/portugal.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-254-tier-application-portugal.md
proposals_created: []
completed_at: 2026-07-02T03:02:51Z
status: completed
schema_version: 2.0.0
---

# Run 254 - tier application: Portugal

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Portugal `tier: 2` in `countries/portugal.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Portugal Block 1 tier wording to explain why the assignment is conditional, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect three assigned tiers rather than two.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Portugal fits Tier 2 at screening confidence: the D8 / remote-worker residence ladder and AIMA residence-authorization stage are real, but the captured D8 income gate sits above the couple's current income and no Portugal-specific post-2027 TP bridge is captured.
- Portugal is therefore not a Tier 1 call in the current vault state; it remains a conditional settlement candidate if income/savings or another ordinary status can carry the file before TP expiry.
- This is not a final recommendation or TOP-N ranking. Portugal still carries application-prep caveats around serving-consulate proof, tax/VAT/social-security structuring, insurance quotes, rent pressure, and Portuguese-language bureaucracy.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 30 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
