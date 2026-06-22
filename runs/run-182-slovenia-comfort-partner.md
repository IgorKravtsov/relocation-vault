---
run_id: 182
date: 2026-06-22T14:47:46Z
agent: hermes
mode: country-deep-dive
target_country: Slovenia
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-768"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-slovenia-023", "claim-slovenia-024"]
files_modified:
  - countries/slovenia.md
  - claims/slovenia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-182-slovenia-comfort-partner.md
proposals_created: []
completed_at: 2026-06-22T14:47:46Z
status: completed
schema_version: 2.0.0
---

# Run 182 - Slovenia comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Slovenia sections 5.8 and 5.9.

## What was done

- Added Slovenia comfort-of-life coverage using safety proxies, EU/services infrastructure context, city-comfort tradeoffs, and Slovenian-language integration caveats.
- Added Slovenia partner/student-fit coverage using the existing TP, digital-nomad family, family-reunification, remote-study, and one-income budget evidence.
- Added source `src-768`, plus claims `claim-slovenia-023` and `claim-slovenia-024`.
- Updated Slovenia frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Slovenia sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Slovenia is safe and comfortable enough for screening: WPR / TravelSafe proxies show GPI 1.409, safety index 87 / Low risk, and US News safest-country rank #32.
- Daily comfort is strongest in Ljubljana for services but financially tighter; Maribor is the best services/cost compromise, and Nova Gorica is the warmer western fallback.
- For the student partner, Slovenia is workable on paper through independent TP/status or family routes, but marriage/civil documentation or strong long-term-partner proof is the conservative filing baseline.
- The one-income constraint is material because the DN threshold and conservative self-employed tax net remain binding.

## What remains

- Slovenia still needs risk dimensions and bureaucracy/practicality coverage, plus later citizenship, DN/single-permit checklist, accountant/tax, insurance, partner-proof, and selected-city application-prep checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Montenegro sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
