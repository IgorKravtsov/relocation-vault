---
run_id: 183
date: 2026-06-22T17:54:04Z
agent: hermes
mode: country-deep-dive
target_country: Montenegro
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-769", "src-770"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-montenegro-027", "claim-montenegro-028"]
files_modified:
  - countries/montenegro.md
  - claims/montenegro.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-183-montenegro-comfort-partner.md
proposals_created: []
completed_at: 2026-06-22T17:54:04Z
status: completed
schema_version: 2.0.0
---

# Run 183 - Montenegro comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Montenegro sections 5.8 and 5.9.

## What was done

- Added Montenegro comfort-of-life coverage using WPR / TravelSafe safety proxies, Expat Arrivals adaptation context, language caveats, and Podgorica vs Budva/Kotor city tradeoffs.
- Added Montenegro partner/student-fit coverage using existing TP, DN spouse/family, remote-study, education, tax, cost, and one-income budget evidence.
- Added sources `src-769` and `src-770`, plus claims `claim-montenegro-027` and `claim-montenegro-028`.
- Updated Montenegro frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Montenegro sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Montenegro is comfort-acceptable for screening: WPR / TravelSafe proxies show GPI 1.685, TravelSafe safety index 70, and Low risk, with transport, pickpocketing, scams, roads, and summer tourist crowds as practical caveats.
- Podgorica is the conservative first base for services, administration, school and budget control; Budva is the warm-coast compromise; Kotor/prime bay should stay a rent-pressured lifestyle exception.
- For the student partner, Montenegro does not solve unmarried-partner dependency automatically: she needs independent TP/status or marriage before relying on the DN family route.
- The one-income margin is plausible but sensitive to coastal rent, private insurance, accountant/immigration costs, tax/SSC downside, and any international-school use.

## What remains

- Montenegro still needs risk dimensions and bureaucracy/practicality coverage, plus later citizenship, DN threshold, PR-counting, accountant/tax, insurance, partner-proof, language/community, and selected-city application-prep checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Serbia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
