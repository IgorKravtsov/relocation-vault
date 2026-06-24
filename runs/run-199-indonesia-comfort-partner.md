---
run_id: 199
date: 2026-06-24T19:53:18Z
agent: hermes
mode: country-deep-dive
target_country: Indonesia
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-799", "src-800"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-indonesia-020", "claim-indonesia-021"]
files_modified:
  - countries/indonesia.md
  - claims/indonesia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-199-indonesia-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T19:53:18Z
status: completed
schema_version: 2.0.0
---

# Run 199 - Indonesia comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Indonesia sections 5.8 and 5.9.

## What was done

- Added Indonesia comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Jakarta / Surabaya / Bandung / Denpasar city tradeoffs.
- Added Indonesia partner/student-fit coverage using existing E33G, entry, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-799` and `src-800`, plus claims `claim-indonesia-020` and `claim-indonesia-021`.
- Updated Indonesia frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Indonesia sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Indonesia is comfort-screenable but mixed: WPR reports GPI 1.786, GTI 4.170, safety index 58, risk level Medium, and US News safety rank 51st.
- TravelSafe rates overall risk Medium, with medium transport/pickpocket/mugging/scam/tap-water/women-traveler caveats and high natural-disaster / terrorism risk boxes.
- EF ranks Indonesia #80 with score 471; Jakarta and Surabaya are stronger than Denpasar, but Bahasa Indonesia help remains important outside expat/private-service contexts.
- For the student partner, marriage or independent status is the conservative baseline; unmarried-partner dependency and E33G spouse filing are not captured.
- One-income monthly costs can fit on paper, but the E33G USD 60,000/year gate, private insurance/evacuation, tax/VAT/BPJS advice, and future school costs keep Indonesia bridge-only at current income.

## What remains

- Indonesia still needs risk dimensions and bureaucracy/practicality coverage, plus E33G dependent details, post-E33G/ITAP route checks, tax/source classification, live lease checks, final-city natural-hazard filters, and provider/community checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Kazakhstan sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
