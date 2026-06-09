---
run_id: 81
date: 2026-06-09T10:21:08Z
agent: hermes
mode: country-deep-dive
target_country: Italy
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-396", "src-397", "src-398", "src-399", "src-400"]
facts_added: 8
facts_verified: 0
claims_added: []
files_modified:
  - countries/italy.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-081-italy-cost-rent.md
proposals_created: []
completed_at: 2026-06-09T10:21:08Z
status: completed
schema_version: 2.0.0
---

# Run 081 - Italy cost and rent

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold.
- Use the previous hint to cover Italy sections 5.4 and 5.5.
- Keep the unit focused on first-pass cost-of-living and rent screening for the couple's current one-income budget.

## What was done

- Updated Italy section 5.4 from pending to passed for first-pass screening.
- Updated Italy section 5.5 from pending to passed for first-pass screening.
- Added five Italy cost/rent sources (`src-396` through `src-400`) from Livingcost country and city pages.
- Added `rome-milan-rent-pressure` and `southern-services-tradeoff` as Italy risk flags.
- Updated Italy depth_score from 2.5 to 4.0.

## Verification results

- Facts added: 8 first-pass cost/rent planning facts.
- Sources added: 5.
- Claims added: 0.
- Verification queue remains 5 pending/open items, below the active verification threshold.

## What remains

- Italy healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, and full relocation budget remain pending.
- Exact Italy live-listing checks, lease-registration availability for DN filing, deposit / agency-fee practice, landlord requirements for foreign remote workers, private insurance, commercialista costs, and city-specific bureaucracy remain application-prep or later-section details.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` mode with a lower-depth Tier-1-hint country while avoiding a repeat on Italy. Suggested next focus: Portugal section 5.3 taxes.
