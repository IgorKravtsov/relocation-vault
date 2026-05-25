---
run_id: 006
date: 2026-05-25T10:03:22Z
agent: hermes
mode: country-deep-dive
target_country: Italy
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 48
sources_added: ["src-027", "src-028", "src-029", "src-030", "src-031", "src-032", "src-033", "src-034"]
facts_added: 11
facts_verified: 0
claims_added: ["claim-italy-001", "claim-italy-002", "claim-italy-003", "claim-italy-004", "claim-italy-005"]
files_modified:
  - countries/italy.md
  - claims/italy.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - decisions/decisions.md
proposals_created: []
completed_at: 2026-05-25T10:51:22Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run pre-flight including git fetch/status, state schema check, and validators.
- Follow protocol default mode selection: no accepted proposals, verification queue below threshold, and Italy is the next Tier-1-hint country at depth 0.
- Open Italy with one focused first pass on sections 5.1 and 5.2.

## What was done
- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/italy.md` from the country template.
- Added first-pass legalization research for temporary protection and the digital-nomad / remote-worker visa.
- Completed climate section 5.2 to DoD with January/July temperatures, sunshine / clear-day indicators, humidity / comfort notes, and a city-level verdict for Milan, Rome, and Palermo.
- Added 8 sources to `sources/sources.md`.
- Added 5 atomic claims to `claims/italy.yml`.
- Added 2 verification items: `vq-011` and `vq-012`.
- Updated `state.json`, `INDEX.md`, `CHANGELOG.md`, and `decisions/decisions.md`.

## What remains
- Verify whether Italy publishes an official TP-to-ordinary-residence bridge before or after 04 March 2027.
- Cross-check the DN / remote-worker income threshold against a 2026 official source serving Ukrainian or Polish residents.
- Verify whether an unmarried partner can be included under any Italy DN / family-cohesion route, or whether marriage is practically required.
- Extract official citizenship-by-residence details from the captured Prefecture / Interior Ministry PDF.
- Research taxes, cost of living, rent, healthcare, partner status, risk dimensions, and bureaucracy.

## Open questions added
- `vq-011`, `vq-012`.

## Recommendation for next iteration
- Continue `mode: country-deep-dive` with Cyprus sections 5.1 and 5.2, because the verification queue remains below threshold and Cyprus is the next Tier-1-hint country at depth 0.
