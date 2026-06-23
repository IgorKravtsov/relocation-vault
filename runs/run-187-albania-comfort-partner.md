---
run_id: 187
date: 2026-06-23T06:22:25Z
agent: hermes
mode: country-deep-dive
target_country: Albania
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-777", "src-778"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-albania-021", "claim-albania-022"]
files_modified:
  - countries/albania.md
  - claims/albania.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-187-albania-comfort-partner.md
proposals_created: []
completed_at: 2026-06-23T06:22:25Z
status: completed
schema_version: 2.0.0
---

# Run 187 - Albania comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Albania sections 5.8 and 5.9.

## What was done

- Added Albania comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, Expat Arrivals adaptation context, and Tirana / Durres / Vlore city tradeoffs.
- Added Albania partner/student-fit coverage using existing Unique Permit, remote-study, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-777` and `src-778`, plus claims `claim-albania-021` and `claim-albania-022`.
- Updated Albania frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Albania sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Albania is comfort-screenable: WPR / TravelSafe proxies show GPI 1.812 and TravelSafe 75 / Low risk, with low petty-crime/transport labels but medium scam and natural-disaster caveats.
- EF EPI gives Albania rank #42 / score 532 and Tirana 557, enough for some private-service comfort but not enough to avoid Albanian-language help for bureaucracy, leases, healthcare, taxes, and schools.
- For the student partner, marriage remains the conservative dependent baseline; Ukrainian remote study is practical but not a captured Albanian residence basis.
- The one-income plan is plausible only if the Type D + Unique Permit route and favorable tax screen hold; Tirana services can narrow the budget, while Durres/Vlore require healthcare/transport checks.

## What remains

- Albania still needs risk dimensions and bureaucracy/practicality coverage, plus later official route/dependent checklist, PR-counting, accountant/tax, private-insurance, lease/address, language/community, and selected-city application-prep checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Uruguay sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
