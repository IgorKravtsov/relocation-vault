---
run_id: 281
date: 2026-07-05T14:25:56Z
agent: hermes
mode: consolidation
target_country: Thailand
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/thailand.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-281-tier-application-thailand.md
proposals_created: []
completed_at: 2026-07-05T14:25:56Z
status: completed
schema_version: 2.0.0
---

# Run 281 - tier application: Thailand

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Thailand `tier: 3` in `countries/thailand.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Thailand Block 1 tier wording to explain why the assignment is bridge/base rather than Tier 1/2 settlement or Tier X rejection.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect thirty assigned tiers rather than twenty-nine.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Thailand has a real official DTV workcation route for foreign remote workers/freelancers, with 5-year multiple-entry validity, 180-day stay blocks, and spouse/children dependent coverage if the couple marries.
- Thailand is Tier 3 for this profile because DTV is a bridge/base rather than a captured settlement ladder, and LTR Work-from-Thailand is above or awkward for the current USD 36,000/year freelance/client profile.
- This is not a final recommendation or TOP-N ranking. Thailand could improve if counsel confirms a durable post-DTV route and tax/status mechanics; it could weaken if extension, tax-remittance, insurance, school, road/transport, English-language, or Bangkok/Phuket cost risks dominate.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 3 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
