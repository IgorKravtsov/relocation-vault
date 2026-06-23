---
run_id: 190
date: 2026-06-23T15:57:13Z
agent: hermes
mode: country-deep-dive
target_country: Panama
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-783", "src-784"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-panama-020", "claim-panama-021"]
files_modified:
  - countries/panama.md
  - claims/panama.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-190-panama-comfort-partner.md
proposals_created: []
completed_at: 2026-06-23T15:57:13Z
status: completed
schema_version: 2.0.0
---

# Run 190 - Panama comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Panama sections 5.8 and 5.9.

## What was done

- Added Panama comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Panama City / David / Santiago / Boquete city tradeoffs.
- Added Panama partner/student-fit coverage using existing remote-worker, friendly-countries/dependent, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-783` and `src-784`, plus claims `claim-panama-020` and `claim-panama-021`.
- Updated Panama frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Panama sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Panama is comfort-screenable but not effortless: WPR / TravelSafe proxies show GPI 2.006, WPR rank #52, TravelSafe safety index 65 / Medium, and TravelSafe overall risk Medium.
- EF EPI gives Panama global rank #70 / score 491; English helps in private services, but Spanish remains necessary for bureaucracy, leases, healthcare, schools, tax/accountant work, and long-term residence.
- For the student partner, marriage or separate residence files remain the conservative baseline; Ukrainian remote study is practical but not a captured Panamanian residence basis.
- The one-income plan is fragile because the remote-worker threshold is exactly USD 3,000/month and Panama City rent, insurance, schooling, lawyers, and accountants can erase the tax upside; David/Boquete/Santiago reduce rent but weaken service depth.

## What remains

- Panama still needs risk dimensions and bureaucracy/practicality coverage, plus later exact remote-worker dependent checklist, friendly-countries/foreign-professional route fit, DGI/RUC/CSS/ITBMS accountant alignment, private-insurance quotes, live lease checks, and selected-city community/provider checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Portugal section 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
