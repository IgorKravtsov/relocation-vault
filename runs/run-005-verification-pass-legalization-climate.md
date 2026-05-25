---
run_id: 005
date: 2026-05-25T03:14:15Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-025", "src-026"]
facts_added: 0
facts_verified: 5
claims_added: []
files_modified:
  - countries/greece.md
  - countries/spain.md
  - countries/portugal.md
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-25T04:09:15Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run pre-flight including git fetch / status and validators.
- Follow protocol priority and execute `mode: verification` because the queue reached 10 items.
- Close one focused batch of legalization/climate verification blockers across Greece, Spain, and Portugal.

## What was done
- Pre-flight passed: repository clean, remote aligned, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Resolved 5 verification items: `vq-001`, `vq-005`, `vq-006`, `vq-007`, and `vq-009`.
- Added `src-025` for direct annual clear-day counts in Madrid, Valencia, and Málaga, which let Spain section 5.2 pass DoD.
- Added `src-026` for Portugal's official AIMA remote-work residence-authorization filing route and document list.
- Clarified the operational baseline for an existing Polish residence title in Greece, Spain, and Portugal: it does not substitute for the destination country's own long-stay status, and TP remains constrained by the one-Member-State rule.
- Updated `verification-queue.md`, all touched country profiles, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## What remains
- Greece: capture an official-primary DN checklist / fee schedule and a direct sunny-day-count source.
- Spain: verify whether any official TP-to-ordinary-residence bridge is published before or after 04 March 2027.
- Portugal: verify whether any official TP-to-ordinary-residence bridge is published and find direct sunny-day counts for Lisbon, Porto, and Faro.

## Open questions added
- None.

## Recommendation for next iteration
- Return to `mode: country-deep-dive` and open Italy on sections 5.1 and 5.2, because the verification queue is back below threshold and Italy is the next Tier-1-hint country at depth 0.
