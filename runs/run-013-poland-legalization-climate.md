---
run_id: 13
date: 2026-05-27T04:00:00Z
agent: hermes
mode: country-deep-dive
target_country: Poland
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 52
sources_added: ["src-062", "src-063", "src-064", "src-065", "src-066", "src-067"]
facts_added: 13
facts_verified: 0
claims_added: ["claim-poland-001", "claim-poland-002", "claim-poland-003", "claim-poland-004", "claim-poland-005", "claim-poland-006", "claim-poland-007", "claim-poland-008"]
files_modified:
  - countries/poland.md
  - claims/poland.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-27T04:52:00Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run default `country-deep-dive` mode: open Poland sections 5.1 and 5.2 as the next fresh Tier-2-hint EU country at depth 0, as recommended by run-012.
- Focus on Poland's unique advantage: one partner already holds a Polish `karta pobytu`, which may unlock family reunification.
- Capture the new CUKR card (May 2026) as the post-2027 TP bridge.
- Queue any missing primary-source gaps rather than forcing recovery mode.

## What was done
- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, both validators passed before edits.
- Created `countries/poland.md` from the country template.
- Captured the CUKR card procedure from official-primary UdSC sources (`src-062`, `src-063`): 3-year temporary residence on special conditions for former Ukrainian TP holders, electronic MOS filing, 340 PLN + 100 PLN fees, deadline 04 March 2027, eligibility conditions (365 days continuous UKR, PESEL UKR on 04 June 2025), family scope, rights (full labour market, Schengen travel, business activity), and CUKR time counting toward EU long-term residence.
- Added TP extension confirmation for Poland (`src-064`).
- Flagged the partner's existing Polish `karta pobytu` as a potential family-reunification path under Article 159 of the Act on Foreigners, with explicit `[verification required]` markers for unmarried-partner rules, income requirements, and marriage effect.
- Noted that Poland has no dedicated digital-nomad visa; remote workers must use business-activity or work routes.
- Added climate first pass for Warsaw, Krakow, and Wroclaw (`src-065`, `src-066`, `src-067`): temperatures, sunshine hours, precipitation, and comfort caveats.
- Added 6 sources to `sources/sources.md` and updated `src-002` to include Poland.
- Added 8 atomic claims to `claims/poland.yml`.
- Added verification item `vq-021` for Poland family-reunification rules.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## What remains
- Capture official-primary family-reunification rules under Art. 159 (unmarried partner eligibility, sponsor minimum income, document checklist).
- Capture business-activity temporary residence requirements (minimum capital, business plan, processing time).
- Capture permanent residence and citizenship rules with primary-source anchors.
- Find direct sunny-day counts for Polish cities (currently only sunshine-hour totals).
- Research taxes, cost of living, rent, healthcare, education, partner/student status, risk dimensions, and bureaucracy.

## Open questions added
- `vq-021` — Poland family-reunification rules for unmarried partners under Art. 159.

## Recommendation for next iteration
- Continue country-deep-dive rotation with Romania (sections 5.1, 5.2) as the next fresh Tier-2-hint EU country at depth 0.
