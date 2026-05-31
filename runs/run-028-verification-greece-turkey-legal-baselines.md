---
run_id: 28
date: 2026-05-31T10:20:00Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 52
sources_added: ["src-152", "src-154"]
facts_added: 4
facts_verified: 4
claims_added: ["claim-greece-005", "claim-turkey-007", "claim-turkey-008", "claim-turkey-009"]
files_modified:
  - countries/greece.md
  - countries/turkey.md
  - claims/greece.yml
  - claims/turkey.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-028-verification-greece-turkey-legal-baselines.md
proposals_created: []
completed_at: 2026-05-31T10:20:00Z
status: completed
schema_version: 2.0.0
---

# Run 028 — Verification: Greece and Turkey legal baselines

## Plan

- Enter verification mode because the pending/open queue was above threshold after run-027.
- Close a focused legal batch rather than opening the next fresh country.
- Prefer existing official sources when they already support a safe operational answer; add only minimal official-primary / official-secondary anchors.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Added `src-152`, an official Hellenic MFA digital-nomad page, and used it to close Greece `vq-002` at the route/checklist-anchor level.
- Added `src-154`, Turkey PMM residence-permit-types page, and used it with existing Turkey sources to close three Turkey legal blockers.
- Turkey DN operational core (`vq-047`) is now treated as resolved from GoTurkey: age 21-55, USD 3,000/month or USD 36,000/year income proof, diploma, passport/photo, and foreign-employment or freelancer-contract evidence.
- Turkey Ukraine-protection baseline (`vq-048`) is now resolved conservatively: no Ukraine-specific Turkish TP bridge captured; PMM TP material is Syria/mass-influx oriented and TP identification does not transfer to long-term residence.
- Turkey long-term residence (`vq-049`) is now official-primary verified: at least eight years continuous residence; student time counts half, ordinary permit types count in full, and TP/humanitarian residence does not transfer.
- Added 4 atomic claims across Greece and Turkey and updated country profiles, queue, state, index, and changelog.

## Verification results

- `vq-002` resolved: Greece DN official-primary route/checklist anchor captured; consular appointment/payment/localisation details remain application-prep checks.
- `vq-047` resolved: Turkey DN operational core is sufficient for current planning; fees and dependent mechanics can be checked before filing.
- `vq-048` resolved: use ordinary Turkish residence planning, not Ukraine-specific TP conversion.
- `vq-049` resolved for long-term residence counting; Turkey citizenship remains a later nationality pass.

## What remains

- Pending queue still includes older sunny/clear-day blockers for Czech Republic, Hungary, Slovakia, Serbia, and Turkey, plus Romania DN checklist and Slovenia DN numeric-threshold / counting details.
- Because the pending/open queue is back below threshold, resume normal country-deep-dive rotation next.

## Open questions added

- None.

## Recommendation for next iteration

- Resume country-deep-dive rotation with Georgia sections 5.1 and 5.2 as the next fresh depth-0 Tier-2-hint non-EU Europe country, unless accepted proposals appear.
