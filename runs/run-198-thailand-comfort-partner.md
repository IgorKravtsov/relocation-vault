---
run_id: 198
date: 2026-06-24T16:49:33Z
agent: hermes
mode: country-deep-dive
target_country: Thailand
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 43
sources_added: ["src-797", "src-798"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-thailand-021", "claim-thailand-022"]
files_modified:
  - countries/thailand.md
  - claims/thailand.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-198-thailand-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T16:49:33Z
status: completed
schema_version: 2.0.0
---

# Run 198 - Thailand comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Thailand sections 5.8 and 5.9.

## What was done

- Added Thailand comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Bangkok / Chiang Mai / Phuket / Pattaya city tradeoffs.
- Added Thailand partner/student-fit coverage using existing DTV, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-797` and `src-798`, plus claims `claim-thailand-021` and `claim-thailand-022`.
- Updated Thailand frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Thailand sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Thailand is a workable bridge comfort screen, but not a low-friction integration screen: WPR/TravelSafe show GPI 2.017, GTI 4.630, safety index 48, and far-south / road / taxi / petty-crime caveats despite low overall tourist risk in normal areas.
- EF EPI ranks Thailand #116 with score 402, with Bangkok 467, Chiang Mai 453, and Phuket 431; English is an expat/private-service fallback rather than a broad daily-life default.
- For the student partner, marriage is the conservative DTV dependent baseline; unmarried-partner treatment and spouse work rights are not captured.
- One-income fit is plausible in Chiang Mai or capped Bangkok/Pattaya, but DTV savings, private insurance, visa trips, tax advice, and future school costs preserve `thailand-one-income-margin-risk`.

## What remains

- Thailand still needs risk dimensions and bureaucracy/practicality coverage, plus DTV extension practice, tax/source classification, spouse work-right details, live lease checks, smoke-season/provider/community checks, and any post-DTV route.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Indonesia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
