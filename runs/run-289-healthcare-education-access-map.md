---
run_id: 289
date: 2026-07-06T15:08:39Z
agent: hermes
mode: consolidation
target_country: null
target_sections: [5.6, 5.7]
target_criterion: healthcare-education-access-map
duration_minutes: 30
sources_added: []
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - dimensions/healthcare-education-access-5.6-5.7.md
  - dimensions/screening-readiness-map.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-289-healthcare-education-access-map.md
proposals_created: []
completed_at: 2026-07-06T15:08:39Z
status: completed
schema_version: 2.0.0
---

# Run 289 - healthcare / education practical-access map

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0 with assigned screening tiers.
- Add a non-ranking synthesis-input map for the uncovered 5.6/5.7 healthcare / education practical-access dimension without changing country profiles, tiers, sources, claims, or verification status.

## What was done

- Added `dimensions/healthcare-education-access-5.6-5.7.md`.
- Grouped the already captured country-profile §5.6/§5.7 baselines into five synthesis-safe buckets: public-system usable with private backup, private-care strong / schooling budget-sensitive, screenable but status/onboarding-sensitive, language/integration-heavy but affordable, and high private-cost / one-income pressure.
- Updated `dimensions/screening-readiness-map.md` and `INDEX.md` so downstream synthesis can find the new 5.6/5.7 healthcare / education practical-access map.
- Updated `state.json` iteration, focus, next-iteration hint, and recomputed aggregate queue/source/claim counts.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.
- Source headings remain 839.
- Claim entries remain 716.
- No country tier, depth score, or country profile changed.

## Key findings

- Healthcare / education access can now be consumed as a non-ranking map: public-system-usable cases, private-care-strong but school-cost-sensitive cases, status/onboarding-sensitive cases, language/integration-heavy cases, and high private-cost / one-income-pressure cases are separated for synthesis.
- The map preserves the guardrail that §5.6 remains partial in many country profiles because exact insurance wording, live quotes, maternity/newborn terms, final-status onboarding, and provider prices are application-prep checks rather than screening blockers.
- This is not a final recommendation, TOP-N ranking, medical recommendation, school recommendation, insurance advice, or city-selection order.

## What remains

- Prepare a non-ranking synthesis-input map for comfort/partner fit (5.8/5.9), or a final synthesis-readiness checklist, if no proposal, verification, or staleness trigger appears.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- If no proposal, verification, or staleness trigger appears, run a non-ranking comfort/partner-fit consolidation pass for 5.8/5.9 or another synthesis-readiness handoff that avoids TOP-N recommendations.
