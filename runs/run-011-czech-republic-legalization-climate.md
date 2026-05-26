---
run_id: 11
date: 2026-05-26T16:03:44Z
agent: hermes
mode: country-deep-dive
target_country: Czech Republic
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 64
sources_added: ["src-053", "src-054", "src-055", "src-056", "src-057", "src-058", "src-059", "src-060"]
facts_added: 13
facts_verified: 0
claims_added: ["claim-czech-001", "claim-czech-002", "claim-czech-003", "claim-czech-004", "claim-czech-005"]
files_modified:
  - countries/czech-republic.md
  - claims/czech-republic.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-26T16:03:44Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run default `country-deep-dive` mode because there were no accepted proposals and the verification queue was below the scheduled-run threshold at pre-flight.
- Respect anti-clustering and target Czech Republic, the first fresh Tier-2-hint country at depth 0 after all Tier-1-hint countries had an initial pass.
- Open sections 5.1 and 5.2 with official-first sources and queue any missing primary-source or climate blockers.

## What was done
- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/czech-republic.md` from the country template.
- Added first-pass legalization research for EU/Czech temporary-protection planning, Czech special long-term residence for Ukrainian TP holders, business/self-employed long-term visa, permanent residence, and document translation/apostille mechanics.
- Captured the special long-term residence baseline from UNHCR Czechia: two years of Czech temporary-protection residence, CZK 440,000/year taxable income for one person plus CZK 110,000 per additional household member, no benefit/debt issues, health-insurance continuity, and household application mechanics.
- Captured the business-purpose long-term visa baseline from Czech official sources: embassy filing, proof of funds/accommodation, register confirmation, criminal-record extract, 5,000 CZK fee, and 90-day processing target.
- Added climate first pass for Prague, Brno, and Ostrava with January/July temperatures, humidity, annual sunshine hours, and winter-grayness caveats.
- Added 8 sources to `sources/sources.md` and updated `src-002` to include Czech Republic.
- Added 5 atomic claims to `claims/czech-republic.yml`.
- Added 2 verification items: `vq-019` and `vq-020`.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## What remains
- Capture Czech official-primary page / legal basis for the special long-term residence route and any later-round or post-04 March 2027 transition details.
- Verify which Czech statuses count toward permanent residence: TP, special long-term residence, business residence, student/dependent statuses.
- Find direct sunny-day or clear-day counts for Prague, Brno, and Ostrava.
- Research Czech taxes, cost of living, rent, healthcare, education, partner/student status, risk dimensions, and bureaucracy.

## Open questions added
- `vq-019`, `vq-020`.

## Recommendation for next iteration
- Run `verification` mode because the pending/open verification queue has reached 10 items after this pass.
