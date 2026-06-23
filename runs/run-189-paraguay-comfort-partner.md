---
run_id: 189
date: 2026-06-23T12:49:14Z
agent: hermes
mode: country-deep-dive
target_country: Paraguay
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-781", "src-782"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-paraguay-020", "claim-paraguay-021"]
files_modified:
  - countries/paraguay.md
  - claims/paraguay.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-189-paraguay-comfort-partner.md
proposals_created: []
completed_at: 2026-06-23T12:49:14Z
status: completed
schema_version: 2.0.0
---

# Run 189 - Paraguay comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Paraguay sections 5.8 and 5.9.

## What was done

- Added Paraguay comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, Expat Arrivals adaptation context, and Asuncion / Encarnacion / Ciudad del Este city tradeoffs.
- Added Paraguay partner/student-fit coverage using existing temporary-residence, remote-study, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-781` and `src-782`, plus claims `claim-paraguay-020` and `claim-paraguay-021`.
- Updated Paraguay frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Paraguay sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Paraguay is comfort-screenable but not low-friction: WPR / TravelSafe proxies show GPI 1.981, GTI 0.073, TravelSafe-derived index 45 / Medium, and TravelSafe low overall risk with several medium everyday-risk labels.
- EF EPI gives Paraguay rank #43 / score 531 and Asuncion 563; English helps in some private services, but Spanish and sometimes Guarani remain important for bureaucracy, leases, healthcare, taxes, schools, and smaller-city life.
- For the student partner, marriage or separate residence files remain the conservative baseline; Ukrainian remote study is practical but not a captured Paraguayan residence basis.
- The one-income plan is plausible only if the lawful-activity residence, tax/VAT/IPS, and private-healthcare setup hold; Asuncion is services-first, while Encarnacion is the budget/climate fallback.

## What remains

- Paraguay still needs risk dimensions and bureaucracy/practicality coverage, plus later exact family/dependent checklist, residence-visa sequence, lawyer/accountant contacts, DNIT/RUC/VAT/IPS fit, private-insurance quotes, live lease checks, and selected-city community/provider checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Panama sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
