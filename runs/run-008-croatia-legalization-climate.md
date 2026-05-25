---
run_id: 8
date: 2026-05-25T22:03:58Z
agent: hermes
mode: country-deep-dive
target_country: Croatia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 58
sources_added: ["src-040", "src-041", "src-042", "src-043"]
facts_added: 12
facts_verified: 0
claims_added: ["claim-croatia-001", "claim-croatia-002", "claim-croatia-003", "claim-croatia-004", "claim-croatia-005"]
files_modified:
  - countries/croatia.md
  - claims/croatia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - decisions/decisions.md
proposals_created: []
completed_at: 2026-05-25T22:03:58Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run pre-flight including git fetch/status, state schema check, and validators.
- Follow protocol default mode selection: no accepted proposals, verification queue below threshold at invocation, and Croatia is the next Tier-1-hint country at depth 0.
- Open Croatia with one focused first pass on sections 5.1 and 5.2.

## What was done
- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/croatia.md` from the country template.
- Added first-pass legalization research for temporary protection and Croatia's digital-nomad temporary stay.
- Captured the DN threshold (€3,622.50/month), up-to-18-month duration, remote-foreign-work scope, document checklist, online / consular / in-country filing channels, and common-law partner family-reunification note.
- Added climate first pass for Zagreb, Split, and Dubrovnik with January/July temperatures, humidity, precipitation days, annual sunshine hours, and comfort caveats.
- Added 4 sources to `sources/sources.md` and updated `src-002` to include Croatia.
- Added 5 atomic claims to `claims/croatia.yml`.
- Added 2 verification items: `vq-015` and `vq-016`.
- Updated `state.json`, `INDEX.md`, `CHANGELOG.md`, and `decisions/decisions.md`.

## What remains
- Verify whether Croatia publishes an official TP-to-ordinary-residence bridge before or after 04 March 2027.
- Extract official long-term-residence / permanent-stay requirements.
- Verify how an existing Polish residence title interacts with Croatia TP or DN planning.
- Find direct city-level sunny-day counts for Zagreb, Split, and Dubrovnik.
- Research taxes, cost of living, rent, healthcare, partner/student status, risk dimensions, and bureaucracy.

## Open questions added
- `vq-015`, `vq-016`.

## Recommendation for next iteration
- Run `mode: verification`, because the pending/open verification queue is now 11 items after Croatia and meets the threshold.
