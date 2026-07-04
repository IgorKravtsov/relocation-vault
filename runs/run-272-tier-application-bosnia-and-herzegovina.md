---
run_id: 272
date: 2026-07-04T10:37:53Z
agent: hermes
mode: consolidation
target_country: Bosnia and Herzegovina
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/bosnia-and-herzegovina.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-272-tier-application-bosnia-and-herzegovina.md
proposals_created: []
completed_at: 2026-07-04T10:37:53Z
status: completed
schema_version: 2.0.0
---

# Run 272 - tier application: Bosnia and Herzegovina

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Bosnia and Herzegovina `tier: X` in `countries/bosnia-and-herzegovina.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Bosnia and Herzegovina Block 1 tier wording to explain why the assignment is screening-negative, high-burden, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect twenty-one assigned tiers rather than twenty.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Bosnia and Herzegovina has low rent/cost screens, a five-year permanent-residence ladder on paper, and acceptable Sarajevo / Mostar service and comfort baselines.
- The country is still Tier X for this couple's current profile: no dedicated DN route or Ukraine-specific post-2027 bridge is captured, the visible route is a high-burden ordinary work/company/founder file, the founder checklist can require five local employees per foreign founder, and tax/SSC/VAT, insurance, family, and local-language bureaucracy remain adviser-dependent.
- This is not a final recommendation or TOP-N ranking. Bosnia and Herzegovina could improve if counsel confirms a workable renewable foreign-client IT route without disproportionate local-company obligations.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 12 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
