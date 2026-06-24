---
run_id: 194
date: 2026-06-24T04:22:20Z
agent: hermes
mode: country-deep-dive
target_country: Moldova
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-789", "src-790"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-moldova-020", "claim-moldova-021"]
files_modified:
  - countries/moldova.md
  - claims/moldova.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-194-moldova-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T04:22:20Z
status: completed
schema_version: 2.0.0
---

# Run 194 - Moldova comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Moldova sections 5.8 and 5.9.

## What was done

- Added Moldova comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Chisinau / Balti / Tiraspol practical city tradeoffs.
- Added Moldova partner/student-fit coverage using existing TP, DN, provisional-stay, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-789` and `src-790`, plus claims `claim-moldova-020` and `claim-moldova-021`.
- Updated Moldova frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Moldova sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Moldova is comfort-screenable but medium-risk: WPR gives 2025 GPI 1.918 and TravelSafe-derived safety index 67 / Medium; TravelSafe highlights the nearby Russia-Ukraine war and Transnistria as regional caveats.
- EF EPI gives Moldova global rank #43, score 531, and Chisinau score 572; English is useful in Chisinau, but Romanian/Russian support remains necessary for bureaucracy, leases, healthcare, and public-school integration.
- For the student partner, independent TP or independent ordinary status is the conservative baseline; do not assume foreign-DN dependent coverage until GIM/counsel confirms it.
- Low Chisinau/Balti costs help the one-income plan, but DN threshold, PR-counting, insurance/school costs, and tax/contribution uncertainty keep the margin tight.

## What remains

- Moldova still needs risk dimensions and bureaucracy/practicality coverage, plus official short-entry confirmation, current DN salary-threshold arithmetic, citizenship, PR-counting, foreign-DN dependent mechanics, live lease/provider checks, and accountant/insurance details.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Mexico sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
