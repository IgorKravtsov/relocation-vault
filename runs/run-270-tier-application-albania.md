---
run_id: 270
date: 2026-07-04T04:23:57Z
agent: hermes
mode: consolidation
target_country: Albania
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/albania.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-270-tier-application-albania.md
proposals_created: []
completed_at: 2026-07-04T04:23:57Z
status: completed
schema_version: 2.0.0
---

# Run 270 - tier application: Albania

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Albania `tier: 2` in `countries/albania.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Albania Block 1 tier wording to explain why the assignment is conditional, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect nineteen assigned tiers rather than eighteen.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Albania has a plausible Tier 2 structure: a Type D + Unique Permit remote-worker baseline for foreign-client IT work, secondary income thresholds below the couple's current income, a favorable but time-limited self-employed tax screen if confirmed, and strong Durres / Vlore / rent-controlled Tirana budget screens.
- The route remains conditional: clean official-primary route capture is missing, Albania is outside the EU temporary-protection bridge framework, PR / citizenship counting for the remote-worker permit is unproven, unmarried-partner coverage is unconfirmed, and tax / VAT / insurance / lease-address mechanics need adviser confirmation.
- This is not a final recommendation or TOP-N ranking. Albania could improve if counsel confirms a clean renewable Unique Permit path and tax setup; it could weaken if official route evidence, PR counting, or private healthcare / schooling / dependent mechanics are stricter than the screening baseline.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 14 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
