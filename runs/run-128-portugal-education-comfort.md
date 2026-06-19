---
run_id: 128
date: 2026-06-15T13:10:20Z
agent: hermes
mode: country-deep-dive
target_country: Portugal
target_sections: ["5.7", "5.8"]
target_criterion: null
duration_minutes: 48
sources_added: ["src-608", "src-609", "src-610", "src-611", "src-612"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-portugal-015", "claim-portugal-016", "claim-portugal-017", "claim-portugal-018"]
files_modified:
  - countries/portugal.md
  - claims/portugal.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-128-portugal-education-comfort.md
proposals_created: []
completed_at: 2026-06-15T13:10:20Z
status: completed
schema_version: 2.0.0
---

# Run 128 - Portugal education/comfort

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Portugal, but limit the unit to sections 5.7 and 5.8 so the iteration remains focused and does not drift into partner or bureaucracy work.

## What was done

- Added first-pass Portugal section 5.7 education and section 5.8 comfort-of-life sections.
- Added five source registry entries: `src-608` through `src-612`.
- Added four atomic claims: `claim-portugal-015` through `claim-portugal-018`.
- Updated Portugal profile frontmatter, scoring rows, Block 4 adaptation summary, practical verdict pros/cons, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Portugal sections 5.7 and 5.8 moved from pending to completed for first-pass screening. Depth score moved from 4.0 to 6.0.

## Key findings

- Public education is structurally usable: optional pre-primary runs from age 3 to 6 and compulsory basic education starts around age 6.
- Private childcare is the education budget risk: Numbeo screens private preschool around EUR 448/month nationally, EUR 558/month in Lisbon, and EUR 514/month in Porto.
- International school exists but is not a default single-income plan: the national proxy is about EUR 10,560/year, with Lisbon much higher.
- Comfort screens positive overall: Portugal has high crowd-sourced safety, strong English-proficiency indicators, and a formal Ukraine reception channel, but Lisbon rent pressure and public-service friction remain caveats.

## What remains

- Portugal partner/student fit, risk dimensions, bureaucracy, final playbook, and remaining legal/tax/healthcare application-prep gaps are still pending.
- Before choosing a future-child school base, local municipality school assignment, Portuguese-as-additional-language support, nursery waiting lists, and exact private-school fees should be checked.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Spain 5.6/5.7 to rotate across Tier-1-hint countries instead of clustering on Portugal.
