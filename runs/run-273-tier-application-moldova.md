---
run_id: 273
date: 2026-07-04T13:45:44Z
agent: hermes
mode: consolidation
target_country: Moldova
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/moldova.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-273-tier-application-moldova.md
proposals_created: []
completed_at: 2026-07-04T13:45:44Z
status: completed
schema_version: 2.0.0
---

# Run 273 - tier application: Moldova

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Moldova `tier: 3` in `countries/moldova.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Moldova Block 1 tier wording to explain why the assignment is bridge/base-oriented and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect twenty-two assigned tiers rather than twenty-one.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Moldova has useful proximity, low Chisinau/Balti cost screens, temporary protection through 01 March 2027, and an official digital-nomad provisional-stay route for foreign remote work.
- Moldova is Tier 3 for this couple's current profile: it can be a plausible nearby bridge/base, but no captured post-TP bridge, unclear DN/IT PR counting, missing citizenship mechanics, current-year salary-threshold checks, dependent/tax/insurance uncertainty, and Transnistria/regional-security caveats keep it below settlement-tier confidence.
- This is not a final recommendation or TOP-N ranking. Moldova could improve if GIM/counsel confirms DN/IT PR counting, family coverage, current threshold affordability, and cheap compliant tax/insurance mechanics.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 11 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
