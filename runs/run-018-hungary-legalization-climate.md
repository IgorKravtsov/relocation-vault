---
run_id: 18
date: 2026-05-28T22:02:49Z
agent: hermes
mode: country-deep-dive
target_country: Hungary
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 23
sources_added: ["src-092", "src-093", "src-094", "src-095", "src-096", "src-097", "src-098", "src-099"]
facts_added: 10
facts_verified: 0
claims_added: ["claim-hungary-001", "claim-hungary-002", "claim-hungary-003", "claim-hungary-004", "claim-hungary-005", "claim-hungary-006", "claim-hungary-007"]
files_modified:
  - countries/hungary.md
  - claims/hungary.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-28T22:25:00Z
status: completed
schema_version: 2.0.0
---

# Run 018 — Hungary legalization and climate first pass

## Plan

- Resume normal country-deep-dive rotation because the verification queue was below the protocol threshold after run-017.
- Open Hungary as the next fresh Tier-2-hint EU country at depth 0.
- Focus on sections 5.1 and 5.2, using official OIF sources where available and queuing ordinary source gaps instead of treating them as recovery issues.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/hungary.md` from the country template.
- Captured OIF official-primary temporary-protection guidance (`src-092`): eligibility, application submission mechanics, work access, and healthcare categories.
- Captured OIF White Card guidance (`src-093`): foreign employment / foreign-company ownership scope, no Hungarian gainful activity or Hungarian company shareholding, EUR 3,000 net/month income threshold for 6 months before entry and throughout stay, extension mechanics, and 21-day procedural administration period.
- Captured OIF guest self-employment guidance (`src-094`): annual self-employment income above 24 times the current minimum wage or business-organisation evidence; 1-year permit, extendable up to 3 years total.
- Captured OIF family-reunification and National Residence Card pages (`src-095`, `src-096`) for spouse/family baseline and the 3-year legal uninterrupted residence PR anchor.
- Added a climate first pass for Budapest, Debrecen, and Pécs (`src-097` through `src-099`): continental climate, cold winters, warm/hot summers, 1,928–2,058 annual sunshine hours, humidity tables, but no direct sunny-day counts.
- Added 8 sources and 7 atomic claims.
- Added 3 verification items (`vq-033` through `vq-035`) for the Hungary TP bridge, White Card consular/family details, and direct sunny-day counts.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No queue items were resolved in this country-deep-dive run.
- Pending/open verification queue increased from 7 to 10.

## What remains

- Capture Hungary-specific official post-04 March 2027 TP-to-ordinary-residence bridge, if any.
- Verify exact White Card consular checklist, fees, translation/apostille rules, and family-reunification availability for a partner of a White Card holder.
- Find direct sunny/clear-day counts for Budapest, Debrecen, and Pécs.
- Research Hungary taxes, cost of living, rent, healthcare, education, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-033` — Hungary post-04 March 2027 TP-to-ordinary-residence bridge.
- `vq-034` — White Card checklist/fees/apostille and partner/family mechanics.
- `vq-035` — Direct annual sunny/clear-day counts for Budapest, Debrecen, and Pécs.

## Recommendation for next iteration

- Continue country-deep-dive rotation with Slovakia (sections 5.1, 5.2) as the next fresh Tier-2-hint EU country, unless accepted proposals appear or the verification queue rises above threshold.
