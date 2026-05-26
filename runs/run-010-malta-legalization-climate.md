---
run_id: 10
date: 2026-05-26T10:17:40Z
agent: hermes
mode: country-deep-dive
target_country: Malta
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 58
sources_added: ["src-046", "src-047", "src-048", "src-049", "src-050", "src-051", "src-052"]
facts_added: 12
facts_verified: 0
claims_added: ["claim-malta-001", "claim-malta-002", "claim-malta-003", "claim-malta-004", "claim-malta-005"]
files_modified:
  - countries/malta.md
  - claims/malta.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-26T10:17:40Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run default `country-deep-dive` mode because there were no accepted proposals and the open verification queue was below threshold.
- Respect anti-clustering and target Malta, the remaining Tier-1-hint country at depth 0.
- Open sections 5.1 and 5.2 with official-first sources and queue any missing primary-source or climate blockers.

## What was done
- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/malta.md` from the country template.
- Added first-pass legalization research for temporary protection, the Malta Nomad Residence Permit, long-term residence, and ordinary naturalisation.
- Captured the NRP threshold (EUR 42,000/year gross = EUR 3,500/month), remote-foreign-work scope, checklist, processing target, fees, one-year duration / renewals, and the explicit warning that the NRP does not lead to long-term residence or citizenship.
- Added climate first pass for Malta / Valletta with mild winter, hot dry summer, humidity, precipitation days, 3,055 sunshine hours, and sirocco / heat-wave caveats.
- Added 7 sources to `sources/sources.md` and updated `src-002` to include Malta.
- Added 5 atomic claims to `claims/malta.yml`.
- Added 2 verification items: `vq-017` and `vq-018`.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## What remains
- Capture Malta-specific official TP filing mechanics and any post-04 March 2027 transition rule.
- Verify whether NRP de facto partner inclusion is accepted in practice for an unmarried Ukrainian couple.
- Find direct sunny-day / clear-day counts for Valletta, Sliema/St Julian's, and Victoria/Gozo.
- Research Malta taxes, cost of living, rent, healthcare, education, partner/student status, risk dimensions, and bureaucracy.

## Open questions added
- `vq-017`, `vq-018`.

## Recommendation for next iteration
- Continue `country-deep-dive` rotation with Czech Republic sections 5.1 and 5.2, unless accepted proposals appear or the verification queue crosses the threshold.
