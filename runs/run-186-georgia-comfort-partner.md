---
run_id: 186
date: 2026-06-23T03:15:05Z
agent: hermes
mode: country-deep-dive
target_country: Georgia
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-775", "src-776"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-georgia-021", "claim-georgia-022"]
files_modified:
  - countries/georgia.md
  - claims/georgia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-186-georgia-comfort-partner.md
proposals_created: []
completed_at: 2026-06-23T03:15:05Z
status: completed
schema_version: 2.0.0
---

# Run 186 - Georgia comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Georgia sections 5.8 and 5.9.

## What was done

- Added Georgia comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, occupied-territory and road-risk caveats, and Tbilisi / Batumi / Kutaisi city tradeoffs.
- Added Georgia partner/student-fit coverage using existing SDA family-residence, IT residence, remote-study, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-775` and `src-776`, plus claims `claim-georgia-021` and `claim-georgia-022`.
- Updated Georgia frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Georgia sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Georgia is comfort-screenable but not frictionless: WPR / TravelSafe proxies show GPI 2.185, safety index 63, and low risk, with Abkhazia/South Ossetia avoidance plus road/transport/night caution.
- EF EPI gives Georgia rank #35 / score 541, with Tbilisi 550 and Batumi 544; this helps private-service comfort, but Georgian-language help is still needed for leases, filings, healthcare, schools, and taxes.
- For the student partner, marriage remains the conservative family-residence baseline; Ukrainian remote study is practical but not a captured Georgian residence basis.
- The one-income plan is promising only if the IT/small-business tax/residence route holds; under the 20% PIT fallback, Tbilisi rent plus insurance/accountant/family costs becomes tight.

## What remains

- Georgia still needs risk dimensions and bureaucracy/practicality coverage, plus later official Ukraine entry table, IT/work-right filing, accountant/tax, private-insurance, lease/address, language/community, and selected-city application-prep checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Albania sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
