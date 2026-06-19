---
run_id: 127
date: 2026-06-15T10:00:28Z
agent: hermes
mode: country-deep-dive
target_country: UAE
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-604", "src-605", "src-606", "src-607"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-uae-010", "claim-uae-011", "claim-uae-012", "claim-uae-013"]
files_modified:
  - countries/uae.md
  - claims/uae.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-127-uae-cost-rent.md
proposals_created: []
completed_at: 2026-06-15T10:00:28Z
status: completed
schema_version: 2.0.0
---

# Run 127 - UAE cost/rent

## Plan

- Use `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Select UAE because it was the only remaining sub-3.0 depth country after the cost/rent rotation; open sections 5.4 and 5.5 with one focused first-pass cost/rent screen.

## What was done

- Added first-pass UAE section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-604` through `src-607`.
- Added four atomic cost/rent claims: `claim-uae-010` through `claim-uae-013`.
- Updated UAE profile frontmatter, scoring rows, practical verdict, relocation-budget rent row, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- UAE sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.5 to 4.5.

## Key findings

- Livingcost screens the UAE nationally at about USD 2,071/month for one person with rent and USD 4,510/month for a family-of-four proxy.
- Dubai is services-rich but very tight: about USD 2,420/month one-person total, USD 5,315 family proxy, and a 40 m2 rent proxy around USD 1,244-1,988.
- Abu Dhabi is slightly cheaper but still rent-sensitive: about USD 2,070/month one-person total, USD 4,485 family proxy, and a 40 m2 proxy around USD 1,151-1,520.
- Sharjah is the first affordability screen, with about USD 1,473/month one-person total and a 40 m2 proxy around USD 667, but commute, lease-registration, and residence-document fit remain practical checks.

## What remains

- UAE healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and legal application-prep details are still pending.
- Live rental listings, Bayut / Property Finder / Dubizzle checks, deposits, broker fees, chiller/utilities, Ejari/Tawtheeq, landlord document support, health insurance, and residence-route income proof remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably to Tier-1-hint countries' remaining practical sections such as Portugal 5.7/5.8.
