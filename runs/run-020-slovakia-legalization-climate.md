---
run_id: 20
date: 2026-05-29T10:04:02Z
agent: hermes
mode: country-deep-dive
target_country: Slovakia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 31
sources_added: ["src-100", "src-101", "src-102", "src-103", "src-104", "src-105", "src-106", "src-107"]
facts_added: 10
facts_verified: 0
claims_added: ["claim-slovakia-001", "claim-slovakia-002", "claim-slovakia-003", "claim-slovakia-004", "claim-slovakia-005", "claim-slovakia-006", "claim-slovakia-007"]
files_modified:
  - countries/slovakia.md
  - claims/slovakia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-29T10:04:02Z
status: completed
schema_version: 2.0.0
---

# Run 020 — Slovakia legalization and climate first pass

## Plan

- Resume normal country-deep-dive rotation because no accepted proposals were present and the verification queue was below threshold at pre-flight.
- Open Slovakia as the next fresh Tier-2-hint EU country at depth 0.
- Focus on sections 5.1 and 5.2, using official/EU/UNHCR sources where quickly capturable and queuing ordinary source gaps rather than treating them as recovery issues.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/slovakia.md` from the country template.
- Captured UNHCR Slovakia temporary-protection guidance (`src-100`): eligibility, EU horizon through 04 March 2027, access to healthcare, education, labour market as employee or self-employed person, public social assistance, accommodation support, Foreign Police application channel, 90/180-day EU movement, and Ukraine travel caveat.
- Captured EU Immigration Portal self-employed/business residence guidance (`src-101`): temporary residence for purpose of business, trade licence / Commercial Register mechanics, application location, documents, fees, apostille/translation and 90-day freshness rules, post-approval health-insurance/medical-report steps, and up to 3-year validity.
- Captured EU Immigration Portal family-member guidance (`src-102`): spouse/children/dependent-relative scope, fees, application location, and the operational baseline that unmarried partners are not listed.
- Captured IOM Slovakia permanent-residence guidance (`src-103`) for the 5-year long-term residence anchor; used Wikipedia Slovak nationality law (`src-104`) only as a citizenship placeholder pending official confirmation.
- Added a climate first pass for Bratislava, Košice, and Poprad (`src-105` through `src-107`): continental climate, cold winters, warm/mild summers, 1,890–2,075 annual sunshine hours, humidity/comfort caveats, but no direct sunny-day counts.
- Added 8 sources and 7 atomic claims.
- Added 3 verification items (`vq-036` through `vq-038`) for business-route primary-source fit, post-2027 TP bridge, and direct sunny/clear-day counts.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No queue items were resolved in this country-deep-dive run.
- Pending/open verification queue increased from 8 to 11.

## What remains

- Verify Slovakia business/self-employed residence against official-primary Slovak sources and a practical IT-freelancer application pattern.
- Check whether any Slovakia-specific TP-to-ordinary-residence bridge exists for after 04 March 2027.
- Find direct sunny/clear-day counts for Bratislava, Košice, and Poprad.
- Research Slovakia taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-036` — Slovakia business/self-employed residence official-primary checklist and IT-freelancer fit.
- `vq-037` — Slovakia post-04 March 2027 TP-to-ordinary-residence bridge.
- `vq-038` — Direct annual sunny/clear-day counts for Bratislava, Košice, and Poprad.

## Recommendation for next iteration

- Run a focused verification batch because the pending/open queue reached 11 after opening Slovakia; prioritize high-priority Slovakia route/TP blockers plus one older climate blocker if time permits.
