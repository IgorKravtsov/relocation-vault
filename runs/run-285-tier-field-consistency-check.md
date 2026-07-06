---
run_id: 285
date: 2026-07-06T02:50:02Z
agent: hermes
mode: consolidation
target_country: null
target_sections: []
target_criterion: tier-field-consistency-check
duration_minutes: 30
sources_added: []
facts_added: 7
facts_verified: 0
claims_added: []
files_modified:
  - dimensions/tier-field-consistency-check.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-285-tier-field-consistency-check.md
proposals_created: []
completed_at: 2026-07-06T02:50:02Z
status: completed
schema_version: 2.0.0
---

# Run 285 - tier-field consistency check

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0 with assigned screening tiers.
- Validate that the completed tier-application workflow is structurally consistent across live vault files without changing any country tier or producing a TOP-N ranking.

## What was done

- Added `dimensions/tier-field-consistency-check.md` as a non-ranking structural audit artifact.
- Compared every country's tier, depth score, and local unverified counter across country frontmatter, `state.json`, `countries.yml`, and `INDEX.md`.
- Recomputed aggregate counts from live files: pending/open verification queue items, source headings, and claim entries.
- Ran the staleness trigger check with `scripts/find-stale.py`.
- Updated `dimensions/tier-readiness-audit.md`, `dimensions/screening-readiness-map.md`, `INDEX.md`, `state.json`, and `CHANGELOG.md` to point to the consistency-check result.

## Verification results

- Tier-field mismatches: 0.
- Depth-score mismatches: 0.
- Country-local unverified-count mismatches: 0.
- Pending/open verification queue items: 0, matching `state.json`.
- Source headings: 839, matching `state.json`.
- Claim entries: 716, matching `state.json`.
- Stale claims: 0.

## Key findings

- The live assigned screening-tier distribution is structurally consistent: Tier 1 = 2 countries, Tier 2 = 13, Tier 3 = 8, Tier X = 10.
- All 33 countries remain at depth 10.0 and have synchronized tier fields across the checked files.
- This check confirms data readiness for downstream non-ranking synthesis inputs, but it is not a final country ranking or relocation recommendation.

## What remains

- Prepare non-ranking synthesis-input maps for cross-country dimensions not yet consolidated, especially route durability, tax/budget stress, cost/rent, healthcare/education, and comfort/partner fit.
- Keep final TOP-N ranking and visit-order recommendations out of Hermes iterations unless a downstream synthesis process explicitly owns them.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- If no proposal, verification, or staleness trigger appears, run a non-ranking synthesis-readiness consolidation pass for one remaining cross-country dimension.
