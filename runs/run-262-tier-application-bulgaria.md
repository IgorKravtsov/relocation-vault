---
run_id: 262
date: 2026-07-03T03:37:53Z
agent: hermes
mode: consolidation
target_country: Bulgaria
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 24
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/bulgaria.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-262-tier-application-bulgaria.md
proposals_created: []
completed_at: 2026-07-03T03:37:53Z
status: completed
schema_version: 2.0.0
---

# Run 262 - tier application: Bulgaria

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Bulgaria `tier: X` in `countries/bulgaria.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Bulgaria Block 1 tier wording to explain why the assignment is current-profile screening-negative, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect eleven assigned tiers rather than ten.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Bulgaria remains attractive on Plovdiv / Varna cost screens, EU geography, Ukrainian TP support, and simple first-pass tax math.
- The route blockers are material: no captured Bulgaria-specific TP bridge, a business-plan / Employment-Agency self-employment route rather than a lightweight DN status, a three-year self-employment permit cap before leave-and-reapply, unsupported unmarried-partner coverage, and unresolved tax/residence compatibility.
- This is not a final recommendation or TOP-N ranking. Bulgaria could improve if counsel confirms a credible continuity strategy and accountant guidance confirms the favorable self-employed tax model.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 22 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
