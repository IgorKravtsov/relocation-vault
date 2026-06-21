---
run_id: 172
date: 2026-06-21T07:57:44Z
agent: hermes
mode: country-deep-dive
target_country: Malta
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-755"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-malta-016", "claim-malta-017"]
files_modified:
  - countries/malta.md
  - claims/malta.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-172-malta-comfort-partner.md
proposals_created: []
completed_at: 2026-06-21T07:57:44Z
status: completed
schema_version: 2.0.0
---

# Run 172 - Malta comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the state hint and rotate to Malta sections 5.8 and 5.9.

## What was done

- Added Malta comfort-of-life coverage using safety proxies, existing NRP / public-service English evidence, Ukrainian/foreigner support context, and city-comfort synthesis.
- Added Malta partner/student-fit coverage using the existing NRP spouse / de facto partnership evidence, remote-study posture, local-work-right caution, and one-income budget screen.
- Added source `src-755`, plus claims `claim-malta-016` and `claim-malta-017`.
- Updated Malta frontmatter, scoring row, practical verdict, playbook, source list, Block 8 context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Malta sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Malta is comfort-positive for English-language practicality, warm island life, official NRP materials, and moderate safety, but small-island crowding, rent pressure, and tourist-market dynamics are material comfort constraints.
- The partner route is plausible through spouse or documented de facto partnership, but marriage remains the cleaner dependent file and Residency Malta confirmation is needed before relying on an unmarried partner case.
- The one-income constraint remains severe because the NRP requires EUR 42,000/year gross and Malta rent/tax pressure is high at the couple's current USD 3,000/month gross income.

## What remains

- Malta still needs risk dimensions and bureaucracy/practicality coverage, plus later post-TP ordinary route, PR/citizenship, tax/accountant, insurance, dependent-work-right, and selected-city application-prep checks.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Czech Republic sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
