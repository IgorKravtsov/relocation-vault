---
run_id: 202
date: 2026-06-25T05:13:59Z
agent: hermes
mode: country-deep-dive
target_country: UAE
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 49
sources_added: ["src-805", "src-806"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-uae-018", "claim-uae-019"]
files_modified:
  - countries/uae.md
  - claims/uae.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-202-uae-comfort-partner.md
proposals_created: []
completed_at: 2026-06-25T05:13:59Z
status: completed
schema_version: 2.0.0
---

# Run 202 - UAE comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to UAE sections 5.8 and 5.9.

## What was done

- Added UAE comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Dubai / Abu Dhabi / Sharjah city tradeoffs.
- Added UAE partner/student-fit coverage using existing virtual-work, Green Residence, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-805` and `src-806`, plus claims `claim-uae-018` and `claim-uae-019`.
- Updated UAE frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- UAE sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 6.0 to 8.0.

## Key findings

- UAE is comfort-screenable: WPR reports GPI 1.812, GTI 1.178, TravelSafe-derived safety index 79 / Low risk, and US News safest-country rank 25th; TravelSafe also reports overall risk Low.
- Main comfort caveats are medium transport/taxi, terrorism, scams/rental-fraud, and women-traveler/social-norm risks, plus the already captured extreme summer heat.
- EF ranks the UAE #72 with score 487, just below the global average; Dubai is stronger than the national baseline, but Arabic/PRO support remains important.
- For the student partner, marriage/spouse or independent status remains the conservative baseline; Ukrainian remote university study is not a captured UAE residence ground.
- One-income fit remains weak because USD 3,000/month is below the USD 3,500/month virtual-work gate and Dubai/Abu Dhabi costs are fragile even with near-zero tax.

## What remains

- UAE still needs risk dimensions and bureaucracy/practicality coverage, plus final route filing mechanics, exact family-sponsorship documents, live lease/deposit checks, accepted insurance wording, and final-city school/clinic/community checks.

## Commit / push status

- Initial commit completed with canonical identity in `git log`, but the typed command failed the pre-execution identity-string gate by containing placeholder/redacted author values. Three follow-up documentation commits repeated the same command-gate miss. Per the commit-identity pitfall, history was not rewritten; this note records all four command-gate misses.

## Open questions added

- None.

## Recommendation for next iteration

- Since all 33 countries are now at depth_score >= 7 and the verification queue remains below threshold, rotate to `criterion-slice` for §5.10 risk dimensions unless an accepted proposal or staleness trigger takes priority.
