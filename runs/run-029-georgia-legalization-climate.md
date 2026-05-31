---
run_id: 29
date: 2026-05-31T16:03:39Z
agent: hermes
mode: country-deep-dive
target_country: Georgia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 62
sources_added: ["src-155", "src-156", "src-157", "src-158", "src-159", "src-160", "src-161"]
facts_added: 10
facts_verified: 0
claims_added: ["claim-georgia-001", "claim-georgia-002", "claim-georgia-003", "claim-georgia-004", "claim-georgia-005", "claim-georgia-006", "claim-georgia-007"]
files_modified:
  - countries/georgia.md
  - claims/georgia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-029-georgia-legalization-climate.md
proposals_created: []
completed_at: 2026-05-31T16:03:39Z
status: completed
schema_version: 2.0.0
---

# Run 029 — Georgia legalization and climate first pass

## Plan

- Run a normal country-deep-dive because there were no accepted proposals and the pending verification queue was below threshold after run-028.
- Open Georgia as the next fresh depth-0 Tier-2-hint non-EU Europe country per the rotation hint.
- Focus on sections 5.1 and 5.2, using official Georgian sources where possible and queuing ordinary source gaps rather than treating them as recovery issues.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/georgia.md` from the country template.
- Captured Georgian MFA GeoConsul as the official entry-information portal anchor (`src-155`), but the Ukraine-specific dynamic table was not cleanly extractable.
- Captured a reputable 2025 Georgia Today report quoting the Prime Ministerial decree that Ukrainian citizens may stay visa-free for one full year, with transitional treatment for Ukrainians already present before 24 February 2025 (`src-156`); queued official-primary verification.
- Captured Georgia SDA residence-permit guidance (`src-157`) for lawful-stay filing, work / entrepreneurial residence, IT residence permit, family reunification, and permanent residence after 10 years on temporary residence.
- Captured Georgia SDA citizenship guidance (`src-158`) for ordinary naturalization after 10 consecutive years, language/history/law tests, and economic/property/business ties.
- Captured climate first-pass sources for Tbilisi, Batumi, and Kutaisi (`src-159` through `src-161`), including January/summer temperatures, rain, humidity/comfort caveats, and sunshine hours where available.
- Added 7 sources and 7 atomic claims.
- Added 3 verification items (`vq-051` through `vq-053`) for the official Ukraine-stay decree/table, IT residence practical mechanics, and direct sunny/clear-day counts.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No queue items were resolved in this country-deep-dive run.
- Pending/open verification queue increased from 7 to 10.

## What remains

- Verify the current official Georgian decree / GeoConsul table for Ukrainian citizens' visa-free duration and any transitional stay rules.
- Verify the IT residence permit's 2026 State Employment Support Agency work-right step, small-business / foreign-client mechanics, and spouse / unmarried-partner dependent treatment.
- Verify direct sunny/clear-day counts for Tbilisi, Batumi, and Kutaisi.
- Research Georgia taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-051` — Georgia current official Ukraine visa-free stay duration and transitional treatment.
- `vq-052` — Georgia IT residence 2026 work-right / small-business / foreign-client mechanics and dependent treatment.
- `vq-053` — Georgia direct sunny/clear-day counts for Tbilisi, Batumi, and Kutaisi.

## Recommendation for next iteration

- Enter verification mode because the pending/open queue reached threshold. Close a focused batch, preferably Georgia legal blockers and one or more older climate sunny-day blockers, before opening the next fresh country.
