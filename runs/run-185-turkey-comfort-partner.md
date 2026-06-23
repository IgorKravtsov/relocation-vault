---
run_id: 185
date: 2026-06-23T00:09:08Z
agent: hermes
mode: country-deep-dive
target_country: Turkey
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-773", "src-774"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-turkey-023", "claim-turkey-024"]
files_modified:
  - countries/turkey.md
  - claims/turkey.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-185-turkey-comfort-partner.md
proposals_created: []
completed_at: 2026-06-23T00:09:08Z
status: completed
schema_version: 2.0.0
---

# Run 185 - Turkey comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Turkey sections 5.8 and 5.9.

## What was done

- Added Turkey comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, Expat Arrivals adaptation context, and Istanbul / Izmir / Antalya city tradeoffs.
- Added Turkey partner/student-fit coverage using existing PMM family-residence, GoTurkey DN, remote-study, work-right, education, tax, cost, rent, and healthcare evidence.
- Added sources `src-773` and `src-774`, plus claims `claim-turkey-023` and `claim-turkey-024`.
- Updated Turkey frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Turkey sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Turkey is comfort-usable but not low-risk: WPR / TravelSafe proxies show GPI 2.852, GTI 3.968, safety index 45, and Medium risk, with border-region, transport/scam, earthquake, and protest/security caveats.
- EF EPI puts Turkey at rank #71 / score 488; Izmir and Antalya screen slightly better than Istanbul, but Turkish-language help is still needed for bureaucracy, leases, healthcare, and schools.
- For the student partner, marriage remains the conservative dependent baseline; Ukrainian remote study alone is not a captured Turkish residence basis.
- The one-income plan remains tight because the DN threshold, tax/SGK sensitivity, rent, private insurance, and future schooling all compete for the same USD 3,000/month gross income.

## What remains

- Turkey still needs risk dimensions and bureaucracy/practicality coverage, plus later citizenship, final DN/residence checklist, accountant/tax, insurance, district-closure/address registration, earthquake/neighborhood, and selected-city application-prep checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Georgia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
