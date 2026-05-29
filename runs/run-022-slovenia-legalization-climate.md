---
run_id: 22
date: 2026-05-29T22:05:09Z
agent: hermes
mode: country-deep-dive
target_country: Slovenia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-110", "src-111", "src-112", "src-113", "src-114", "src-115", "src-116", "src-117"]
facts_added: 11
facts_verified: 0
claims_added: ["claim-slovenia-001", "claim-slovenia-002", "claim-slovenia-003", "claim-slovenia-004", "claim-slovenia-005", "claim-slovenia-006", "claim-slovenia-007", "claim-slovenia-008"]
files_modified:
  - countries/slovenia.md
  - claims/slovenia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-29T22:05:09Z
status: completed
schema_version: 2.0.0
---

# Run 022 — Slovenia legalization and climate first pass

## Plan

- Resume normal country-deep-dive rotation because no accepted proposals were present and the pending verification queue was below threshold at pre-flight.
- Open Slovenia as the next fresh Tier-2-hint EU country at depth 0.
- Focus on sections 5.1 and 5.2, using official GOV.SI / EU sources where available and queuing ordinary source gaps rather than treating them as recovery issues.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/slovenia.md` from the country template.
- Captured GOV.SI temporary-protection guidance (`src-110`): eligibility, police registration, administrative-unit application within three working days, TP card as temporary residence permit, fee exemption, residence registration, and a post-TP 10-day application window for ordinary temporary residence.
- Captured GOV.SI Ministry of the Interior digital-nomad route (`src-111`): foreign remote-work definition, no Slovenian labour-market entry, filing abroad or in Slovenia while legally present, up to one-year validity, non-extendability, six-month wait before reapplication, twice-average-net-salary funds formula, and immediate family-reunification feature.
- Captured EU Immigration Portal self-employed and family-member guidance (`src-112`, `src-113`): self-employed single-permit baseline, one-year prior-residence rule / professional-activity exception, five-year permanent-residence anchor, and family-reunification coverage including spouse, civil partner/civil union partner, and long-term relationship partner.
- Captured GOV.SI citizenship baseline (`src-114`): ordinary naturalisation after at least 10 years in Slovenia, including five continuous years before application.
- Added a climate first pass for Ljubljana, Maribor, and Portorož/coastal Slovenia (`src-115` through `src-117`): inland continental climate, milder/sunnier coast, 1,955–2,415 annual sunshine hours, humidity/comfort caveats, but no direct sunny-day counts.
- Added 8 sources and 8 atomic claims.
- Added 2 verification items (`vq-039`, `vq-040`) for the DN exact numeric threshold/checklist/counting questions and direct sunny/clear-day counts.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No queue items were resolved in this country-deep-dive run.
- Pending/open verification queue increased from 9 to 11.

## What remains

- Verify Slovenia DN current numeric income threshold from the latest Official Gazette salary value, detailed checklist/fees, family evidence, and whether DN time counts toward permanent residence.
- Find direct annual sunny/clear-day counts for Ljubljana, Maribor, and Portorož/Koper.
- Research Slovenia taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-039` — Slovenia DN exact numeric threshold, application checklist/fees, partner evidence, and PR-counting rule.
- `vq-040` — Direct annual sunny/clear-day counts for Ljubljana, Maribor, and Portorož/Koper.

## Recommendation for next iteration

- Run a focused verification batch because the pending queue reached 11 after opening Slovenia; prioritize `vq-039` because it determines whether the DN route fits the couple's ~$3,000/month budget, then close one climate sunny-day blocker if time permits.
