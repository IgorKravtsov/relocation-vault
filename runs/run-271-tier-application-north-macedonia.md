---
run_id: 271
date: 2026-07-04T07:32:10Z
agent: hermes
mode: consolidation
target_country: North Macedonia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/north-macedonia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-271-tier-application-north-macedonia.md
proposals_created: []
completed_at: 2026-07-04T07:32:10Z
status: completed
schema_version: 2.0.0
---

# Run 271 - tier application: North Macedonia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned North Macedonia `tier: X` in `countries/north-macedonia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote North Macedonia Block 1 tier wording to explain why the assignment is screening-negative, high-burden, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect twenty assigned tiers rather than nineteen.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- North Macedonia has attractive cost and rent screens, Balkan proximity, and a conceptual ordinary work/self-employment residence path.
- The country is still Tier X for this couple's current profile: no dedicated DN route or current Ukraine protection bridge is captured, the practical route is a real self-employment/company-backed file rather than simple foreign-client remote work, PR/citizenship counting and spouse inclusion remain unproven, and the conservative tax/contribution downside can compress the one-income budget.
- This is not a final recommendation or TOP-N ranking. North Macedonia could improve if counsel and an accountant confirm a renewable foreign-client IT route, PR counting, spouse inclusion, and manageable tax/VAT/insurance mechanics.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 13 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
