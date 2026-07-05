---
run_id: 284
date: 2026-07-05T23:40:35Z
agent: hermes
mode: consolidation
target_country: Armenia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/armenia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-284-tier-application-armenia.md
proposals_created: []
completed_at: 2026-07-05T23:40:35Z
status: completed
schema_version: 2.0.0
---

# Run 284 - tier application: Armenia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Complete the schema-safe tier-application pass with the last remaining tier-null country rather than making a ranking or recommendation.

## What was done

- Assigned Armenia `tier: 3` in `countries/armenia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Armenia Block 1 tier wording to explain why the assignment is bridge/base rather than Tier 1/2 settlement or Tier X rejection.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect all 33 countries having assigned screening tiers.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Armenia has Ukrainian visa-free scouting, official business-activity temporary/permanent residence categories, a potentially short lawful-residence citizenship headline, and workable secondary-city cost/rent screens.
- Armenia is Tier 3 for this profile because the captured route is an adviser-led ordinary business/IE or LLC file, not a proven DN or lightweight foreign-client IT settlement ladder; tax/VAT, insurance, spouse, language, lease, renewal/counting, and border-security caveats remain active.
- This is not a final recommendation or TOP-N ranking. Armenia could improve if Armenian counsel/accountant evidence confirms a renewable foreign-client IT business-residence path and clean tax/dependent setup; it could weaken if business-substance, Yerevan budget, private health/school costs, or security/language friction dominate.

## What remains

- Tier application is complete for all 33 countries.
- Future consolidation can run consistency checks or prepare non-ranking synthesis inputs, but final TOP-N ranking remains out of scope.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- If no proposal, verification, or staleness trigger appears, run a tier-field consistency check or non-ranking synthesis-readiness consolidation pass.
