---
run_id: 52
date: 2026-06-05T14:48:05Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 35
sources_added: []
facts_added: 0
facts_verified: 7
claims_added: []
files_modified:
  - countries/thailand.md
  - countries/indonesia.md
  - countries/kazakhstan.md
  - verification-queue.md
  - state.json
  - CHANGELOG.md
  - runs/run-052-verification-bridge-settlement-baselines.md
proposals_created: []
completed_at: 2026-06-05T14:48:05Z
status: completed
schema_version: 2.0.0
---

# Run 052 - Verification bridge and settlement baselines

## Plan

- Run `verification` because the pending/open verification queue was exactly 10, at the active threshold.
- Close legal route blockers to safe operational baselines where existing captured sources already answer the country-screening question.
- Focus on bridge-vs-settlement blockers for Thailand, Indonesia, and Kazakhstan.

## What was done

- Resolved Thailand `vq-079` and `vq-080`: DTV is a bridge/base route, not a captured PR/citizenship ladder; LTR is above the couple's current income/profile; spouse/children are the captured dependent categories, while unmarried partner and tax microdetails are later checks.
- Resolved Indonesia `vq-081` and `vq-082`: E33G is official but above current income and bridge-only; no captured ITAP/PR/citizenship ladder exists for foreign-client remote IT without local employer.
- Resolved Kazakhstan `vq-083`, `vq-084`, and `vq-085`: Neo Nomad remains secondary-sourced and bridge-only for screening; captured TRP/business-immigrant evidence does not prove a lightweight foreign-client IT route; no captured PR/citizenship ladder exists, and citizenship has dual-nationality risk.
- Updated the three country profiles and the verification queue; no new sources or claims were added.

## Verification results

- Facts verified/resolved: 7 queue items (`vq-079` through `vq-085`, except already-resolved items outside this range).
- Pending/open verification queue decreased from 10 to 3.

## What remains

- Remaining pending queue items: Argentina tourist-exemption official capture (`vq-072`), Albania remote-worker route official extraction (`vq-055`), and Malaysia sunny/clear-day climate verification (`vq-078`).
- Thailand, Indonesia, and Kazakhstan still need later tax/cost/rent/healthcare/comfort passes before practical ranking; this run only closed route-screening blockers.

## Open questions added

- None.

## Recommendation for next iteration

- Return to `country-deep-dive`; Armenia is the only remaining depth-0 country and should be opened with sections 5.1 and 5.2 unless accepted proposals or a new verification threshold trigger appears.
