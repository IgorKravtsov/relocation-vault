---
run_id: 286
date: 2026-07-06T05:54:00Z
agent: hermes
mode: consolidation
target_country: null
target_sections: [5.1]
target_criterion: route-durability-map
duration_minutes: 30
sources_added: []
facts_added: 4
facts_verified: 0
claims_added: []
files_modified:
  - dimensions/route-durability-5.1.md
  - dimensions/screening-readiness-map.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-286-route-durability-map.md
proposals_created: []
completed_at: 2026-07-06T05:54:00Z
status: completed
schema_version: 2.0.0
---

# Run 286 - route durability map

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0 with assigned screening tiers.
- Add a non-ranking synthesis-input map for the uncovered 5.1 legal-route durability dimension without changing country profiles, tiers, sources, claims, or verification status.

## What was done

- Added `dimensions/route-durability-5.1.md`.
- Grouped the already captured country-profile legal-route patterns into four synthesis-safe buckets: durable settlement file captured, conditional ordinary-residence file, bridge/base route, and high-risk / weak fit.
- Updated `dimensions/screening-readiness-map.md` and `INDEX.md` so downstream synthesis can find the new 5.1 route-durability map.
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

- Route durability can now be consumed as a non-ranking map: durable settlement files, conditional ordinary-residence files, bridge/base routes, and high-risk / weak-fit routes are separated for synthesis.
- The map preserves the key guardrail that bridge visas, DTV/DE Rantau/virtual-work-style bases, and income-gated DN routes are not settlement ladders unless the country profile already proves a follow-on route.
- This is not a final recommendation, TOP-N ranking, or visit order.

## What remains

- Prepare non-ranking synthesis-input maps for another uncovered cross-country dimension: tax/budget stress (5.3), cost/rent pressure (5.4/5.5), healthcare/education access (5.6/5.7), or comfort/partner fit (5.8/5.9).

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- If no proposal, verification, or staleness trigger appears, run a non-ranking tax/budget-stress consolidation pass for 5.3 or another uncovered synthesis-input dimension.
