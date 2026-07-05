---
run_id: 283
date: 2026-07-05T20:36:26Z
agent: hermes
mode: consolidation
target_country: Kazakhstan
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/kazakhstan.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-283-tier-application-kazakhstan.md
proposals_created: []
completed_at: 2026-07-05T20:36:26Z
status: completed
schema_version: 2.0.0
---

# Run 283 - tier application: Kazakhstan

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Kazakhstan `tier: 3` in `countries/kazakhstan.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Kazakhstan Block 1 tier wording to explain why the assignment is bridge/base rather than Tier 1/2 settlement or Tier X rejection.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect thirty-two assigned tiers rather than thirty-one.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Kazakhstan has official Ukrainian visa-free scouting, a captured eGov TRP-purpose framework, workable PIT-only tax screening, and low Shymkent / Aktau cost and rent screens.
- Kazakhstan is Tier 3 for this profile because the remote-work / Neo Nomad route is still secondary-sourced, ordinary TRP evidence does not prove a lightweight foreign-client IT route, and no durable PR/citizenship ladder is captured for TRP / Neo Nomad / foreign-client IT.
- This is not a final recommendation or TOP-N ranking. Kazakhstan could improve if official/counsel evidence confirms a renewable remote-work or business route, spouse mechanics, tax/VAT/contribution fit, and PR counting; it could weaken if route, language, insurance, lease, winter, school, or Almaty cost risks dominate.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 1 country as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with the last remaining tier-null country unless accepted proposals, verification threshold, or staleness checks take priority.
