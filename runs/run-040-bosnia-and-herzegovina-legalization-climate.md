---
run_id: 40
date: 2026-06-03T10:08:32Z
agent: hermes
mode: country-deep-dive
target_country: Bosnia and Herzegovina
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 58
sources_added: ["src-213", "src-214", "src-215", "src-216", "src-217", "src-218"]
facts_added: 8
facts_verified: 0
claims_added: ["claim-bosnia-herzegovina-001", "claim-bosnia-herzegovina-002", "claim-bosnia-herzegovina-003", "claim-bosnia-herzegovina-004", "claim-bosnia-herzegovina-005", "claim-bosnia-herzegovina-006"]
files_modified:
  - countries/bosnia-and-herzegovina.md
  - claims/bosnia-and-herzegovina.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-040-bosnia-and-herzegovina-legalization-climate.md
proposals_created: []
completed_at: 2026-06-03T10:08:32Z
status: completed
schema_version: 2.0.0
---

# Run 040 - Bosnia and Herzegovina legalization and climate

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold after run-039.
- Open Bosnia and Herzegovina as the next fresh depth-0 Tier-3-hint country in the anti-clustering rotation.
- Focus on sections 5.1 and 5.2: entry / ordinary residence / long-term ladder / climate DoD.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/bosnia-and-herzegovina.md` and `claims/bosnia-and-herzegovina.yml`.
- Reused `src-204` as a medium-confidence Ukrainian-passport entry placeholder and added six Bosnia and Herzegovina sources (`src-213` through `src-218`): Service for Foreigners' Affairs entry / stay / required-documents pages and PDFs, Climate to Travel, WeatherSpark, and UNHCR Help Bosnia and Herzegovina.
- Advanced section 5.1 to partial: 90/180 visa-free mechanics, temporary-residence filing, work-permit and company-founder checklists, permanent residence after five uninterrupted years, Polish residence-card baseline, and conservative no-captured-Ukraine-protection-bridge baseline.
- Completed section 5.2 at medium confidence with Sarajevo, Tuzla, and Mostar temperature baselines, low muggy-day burden, and WeatherSpark clearer-sky day-equivalent proxies.
- Added risk flags `no-dedicated-digital-nomad-visa`, `company-founder-route-high-burden`, `ukraine-protection-status-gap`, and `cold-inland-winters`.
- Added `vq-066` and `vq-067` for official Ukraine entry / protection and ordinary-route / partner / PR / citizenship mechanics.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 5 to 7 due to two Bosnia and Herzegovina legal follow-up items.

## What remains

- Bosnia and Herzegovina taxes, cost of living, rent, healthcare, education, comfort, partner fit, risk dimensions, bureaucracy, and citizenship remain pending.
- The main legal blockers are official Ukraine entry/protection status and whether a foreign-client IT worker can use an ordinary company / self-employment file without the heavy five-local-employee founder burden.

## Open questions added

- `vq-066` — Bosnia and Herzegovina official Ukraine entry, Ukraine protection / humanitarian status, and post-2027 bridge.
- `vq-067` — Bosnia and Herzegovina company-founder / self-employment / foreign-client IT fit, partner mechanics, PR counting, and citizenship consequences.

## Recommendation for next iteration

- Continue `country-deep-dive` with a fresh depth-0 country, preferably Moldova sections 5.1 and 5.2, while the pending/open verification queue remains below the active threshold.
