---
run_id: 170
date: 2026-06-21T01:44:50Z
agent: hermes
mode: country-deep-dive
target_country: Cyprus
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-751", "src-752"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-cyprus-016", "claim-cyprus-017"]
files_modified:
  - countries/cyprus.md
  - claims/cyprus.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-170-cyprus-comfort-partner.md
proposals_created: []
completed_at: 2026-06-21T01:44:50Z
status: completed
schema_version: 2.0.0
---

# Run 170 - Cyprus comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the state hint and rotate to Cyprus sections 5.8 and 5.9.

## What was done

- Added Cyprus comfort-of-life coverage using a country-level safety proxy, existing Ukraine reception evidence, city-comfort synthesis, and EF EPI English-proficiency data.
- Added Cyprus partner/student-fit coverage using the existing DN spouse/civil-union family wording, dependent work-right limitation, TP / ordinary-route baseline, remote-study practicality, and one-income city budget screen.
- Added sources `src-751` and `src-752`, plus claims `claim-cyprus-016` and `claim-cyprus-017`.
- Updated Cyprus frontmatter, scoring row, practical verdict, playbook, source list, Block 8 context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Cyprus sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Cyprus is comfort-positive for warm coastal life, acceptable safety, Ukrainian reception infrastructure, and moderate English usability, but Greek remains needed for administration, healthcare, leases, public schooling, and citizenship.
- The partner route is formalization-dependent: DN family coverage includes a spouse or civil-union partner, while family members cannot work locally.
- The one-income constraint remains severe because the DN sponsor threshold is EUR 3,500/month net, far above the current Cyprus tax-net model.

## What remains

- Cyprus still needs risk dimensions and bureaucracy/practicality coverage, plus later PR/citizenship, private-insurance, dependent route filing, and selected-city application-prep checks.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Croatia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
