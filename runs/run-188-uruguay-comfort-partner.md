---
run_id: 188
date: 2026-06-23T09:27:59Z
agent: hermes
mode: country-deep-dive
target_country: Uruguay
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-779", "src-780"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-uruguay-020", "claim-uruguay-021"]
files_modified:
  - countries/uruguay.md
  - claims/uruguay.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-188-uruguay-comfort-partner.md
proposals_created: []
completed_at: 2026-06-23T09:27:59Z
status: completed
schema_version: 2.0.0
---

# Run 188 - Uruguay comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Uruguay sections 5.8 and 5.9.

## What was done

- Added Uruguay comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, Expat Arrivals adaptation context, and Montevideo / Salto / Punta del Este city tradeoffs.
- Added Uruguay partner/student-fit coverage using existing permanent-residence, citizenship, remote-study, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-779` and `src-780`, plus claims `claim-uruguay-020` and `claim-uruguay-021`.
- Updated Uruguay frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Uruguay sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Uruguay is comfort-screenable: WPR / TravelSafe proxies show GPI 1.784, GTI 0.059, TravelSafe 77 / Low risk, and US News rank #56, but Montevideo still needs street-crime and night-transport caution.
- EF EPI gives Uruguay rank #34 / score 542 and Montevideo 544; English helps in private services, but Spanish remains necessary for bureaucracy, leases, healthcare, schools, tax/accountant work, and citizenship.
- For the student partner, marriage or separate residence files remain the conservative baseline; Ukrainian remote study is practical but not a captured Uruguayan residence basis.
- The one-income plan is plausible only if the permanent-residence means-of-life file and favorable tax/BPS answer hold; Salto is the budget fallback, while Montevideo is services-first but tighter.

## What remains

- Uruguay still needs risk dimensions and bureaucracy/practicality coverage, plus later exact partner/dependent practice, DGI/BPS/VAT accountant alignment, private-insurance/mutualista quotes, lease guarantees, neighborhood/community checks, and final-city service checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Paraguay sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
