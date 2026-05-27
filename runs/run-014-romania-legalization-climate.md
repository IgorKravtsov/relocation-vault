---
run_id: 14
date: 2026-05-27T10:00:00Z
agent: hermes
mode: country-deep-dive
target_country: Romania
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 48
sources_added: ["src-068", "src-069", "src-070", "src-071", "src-072", "src-073", "src-074", "src-075"]
facts_added: 12
facts_verified: 0
claims_added: ["claim-romania-001", "claim-romania-002", "claim-romania-003", "claim-romania-004", "claim-romania-005", "claim-romania-006", "claim-romania-007", "claim-romania-008"]
files_modified:
  - countries/romania.md
  - claims/romania.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-27T10:48:00Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run default `country-deep-dive` mode: open Romania sections 5.1 and 5.2 as the next fresh Tier-2-hint EU country at depth 0, following the run-013 recommendation.
- Focus on Romania's digital-nomad visa (Law 22/2022) as the most relevant route for a remote IT worker.
- Capture the official-primary immigration law anchor (OUG 194/2002 consolidated April 2026).
- Queue missing primary-source gaps rather than forcing recovery mode.

## What was done
- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, both validators passed before edits.
- Created `countries/romania.md` from the country template.
- Captured OUG 194/2002 (republished, consolidated April 2026) as `src-068`: official-primary Romanian immigration law defining "nomad digital" (Art. 2), visa types (D/AM, D/AC, D/SD), family reunification (Art. 62), and EU long-term residence conditions (Art. 71).
- Captured the IGI online application portal (`src-069`) and the E-VISA portal (`src-072`).
- Captured the digital-nomad visa details from Nomad Girl (`src-070`): €3,300/month income threshold, 12+12 months duration, tax treatment (no Romanian tax assumed), application at embassy/consulate or via e-visa.
- Confirmed Ukrainian biometric passport holders are exempt from Romanian short-stay visa (`src-071`).
- Added climate first pass for Bucharest, Cluj-Napoca, and Timișoara (`src-073`, `src-074`, `src-075`): continental climate, cold winters, ~2,030–2,130 annual sunshine hours.
- Added 8 sources to `sources/sources.md`.
- Added 8 atomic claims to `claims/romania.yml`.
- Added 7 verification items (`vq-022` through `vq-028`) for Romania gaps.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## What remains
- Capture official-primary digital-nomad visa checklist (documents, health insurance, processing time).
- Capture Romania-specific temporary-protection registration procedure and rights for Ukrainians.
- Capture post-04 March 2027 TP transition mechanism, if any.
- Find direct sunny-day counts for Romanian cities.
- Verify whether digital-nomad residence counts toward the 5-year EU long-term residence period.
- Capture D/AC commercial-activity visa requirements for self-employed IT freelancers.
- Verify unmarried partner eligibility for family reunification.
- Research taxes, cost of living, rent, healthcare, education, partner/student status, risk dimensions, and bureaucracy.

## Open questions added
- `vq-022` — Romania DN visa exact document checklist and processing time.
- `vq-023` — Romania TP registration procedure and rights for Ukrainians.
- `vq-024` — Romania post-04 March 2027 TP-to-ordinary-residence bridge.
- `vq-025` — Direct annual sunny-day counts for Bucharest, Cluj-Napoca, and Timișoara.
- `vq-026` — Whether DN residence counts toward EU long-term residence in Romania.
- `vq-027` — D/AC commercial-activity visa requirements for self-employed IT freelancers.
- `vq-028` — Unmarried partner eligibility for family reunification in Romania.

## Recommendation for next iteration
- Continue country-deep-dive rotation with Bulgaria (sections 5.1, 5.2) as the next fresh Tier-2-hint EU country at depth 0, unless the verification queue crosses the threshold or accepted proposals appear.
