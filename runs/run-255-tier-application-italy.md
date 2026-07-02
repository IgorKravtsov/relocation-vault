---
run_id: 255
date: 2026-07-02T06:07:47Z
agent: hermes
mode: consolidation
target_country: Italy
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 26
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/italy.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-255-tier-application-italy.md
proposals_created: []
completed_at: 2026-07-02T06:07:47Z
status: completed
schema_version: 2.0.0
---

# Run 255 - tier application: Italy

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Italy `tier: 2` in `countries/italy.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Italy Block 1 tier wording to explain why the assignment is conditional, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect four assigned tiers rather than three.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Italy fits Tier 2 at screening confidence: it has a real TP framework to 04 March 2027, a formal DN / remote-worker route, workable tax screening under forfetario if confirmed, and lower-rent southern city options.
- Italy is not a Tier 1 call in the current vault state because no Italy-specific TP bridge is captured, the DN file requires specialized-worker proof and a registered lease, unmarried-partner coverage is unsupported, and budget fit depends on Palermo / Naples rather than Rome / Milan.
- This is not a final recommendation or TOP-N ranking. Italy still carries application-prep caveats around consular filing, commercialista confirmation, lease registration, private-insurance quotes, ASL/Questura timing, and Italian-language bureaucracy.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 29 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
