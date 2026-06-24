---
run_id: 197
date: 2026-06-24T13:42:05Z
agent: hermes
mode: country-deep-dive
target_country: Malaysia
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-795", "src-796"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-malaysia-022", "claim-malaysia-023"]
files_modified:
  - countries/malaysia.md
  - claims/malaysia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-197-malaysia-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T13:42:05Z
status: completed
schema_version: 2.0.0
---

# Run 197 - Malaysia comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Malaysia sections 5.8 and 5.9.

## What was done

- Added Malaysia comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Kuala Lumpur / Penang / Johor Bahru / Ipoh city tradeoffs.
- Added Malaysia partner/student-fit coverage using existing DE Rantau, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-795` and `src-796`, plus claims `claim-malaysia-022` and `claim-malaysia-023`.
- Updated Malaysia frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Malaysia sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Malaysia is comfort-screenable: WPR gives 2025 GPI 1.469, GTI 1.626, safety index 69 / Medium, and US News safest-country rank 44th; TravelSafe gives Safety Index 69 and overall Low risk.
- East Malaysia warnings, taxi/night-driving cautions, scams/petty-crime filtering, and final neighbourhood checks still matter.
- EF EPI gives Malaysia global rank #24 and score 581, with Kuala Lumpur 588, Ipoh 582, and Johor Bahru 577; English fallback is strong, but Bahasa/local help remains relevant for public schools and bureaucracy.
- For the student partner, marriage is the conservative DE Rantau dependent baseline; unmarried-partner eligibility and spouse local-work rights are not captured.

## What remains

- Malaysia still needs risk dimensions and bureaucracy/practicality coverage, plus official Ukrainian short-stay capture, DE Rantau post-24-month route verification, tax/source classification, spouse work-right details, live lease checks, and city provider/community checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Thailand sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
