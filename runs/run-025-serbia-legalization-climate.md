---
run_id: 25
date: 2026-05-30T16:06:08Z
agent: hermes
mode: country-deep-dive
target_country: Serbia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 61
sources_added: ["src-132", "src-133", "src-134", "src-135", "src-136", "src-137", "src-138", "src-139", "src-140", "src-141", "src-142"]
facts_added: 12
facts_verified: 0
claims_added: ["claim-serbia-001", "claim-serbia-002", "claim-serbia-003", "claim-serbia-004", "claim-serbia-005", "claim-serbia-006", "claim-serbia-007", "claim-serbia-008"]
files_modified:
  - countries/serbia.md
  - claims/serbia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-30T16:06:08Z
status: completed
schema_version: 2.0.0
---

# Run 025 — Serbia legalization and climate first pass

## Plan

- Continue normal country-deep-dive rotation because no accepted proposals were present and the pre-run pending verification queue was below the verification threshold.
- Open Serbia as the next fresh depth-0 Tier-2-hint non-EU Europe country.
- Focus on sections 5.1 and 5.2, using official Serbian sources for immigration baselines and queuing ordinary gaps instead of treating them as recovery issues.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/serbia.md` from the country template.
- Captured Serbia MFA visa-regime page for Ukraine (`src-132`): Ukrainian ordinary-passport holders have visa-free entry up to 90 days within 180 days.
- Captured Serbian temporary-protection anchors (`src-133`, `src-134`): the Government decision covers displaced persons from Ukraine, MUP registration, Article 76 rights, and amendments allowing yearly extension while reasons persist.
- Captured official Serbian temporary-residence / single-permit sources (`src-135`, `src-136`, `src-137`): Article 40 grounds, self-employment / single-permit framework, general document evidence, up-to-3-year permit duration, 15-day single-permit decision deadline, and PR after 3 years continuous residence.
- Captured Serbia MFA citizenship baseline (`src-138`): ordinary naturalization after permanent residence includes a 3-year registered-permanent-residence condition and release/proof of release from foreign citizenship.
- Used a 2026 secondary Serbia digital-nomad/self-employment guide (`src-139`) only as a medium-confidence operational placeholder for the self-employment / entrepreneur route, fees, processing time, and financial-threshold caveats.
- Captured climate first-pass sources for Belgrade, Novi Sad, and Niš (`src-140` through `src-142`), including January/July temperatures, humidity, precipitation, sunshine hours, and comfort caveats.
- Added 11 sources and 8 atomic claims.
- Added 3 verification items (`vq-044` through `vq-046`) for Serbia DN/self-employment official checklist and dependent mechanics, Serbia TP bridge / Polish-status interaction, and direct sunny/clear-day counts.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No queue items were resolved in this country-deep-dive run.
- Pending/open verification queue increased from 9 to 12.

## What remains

- Verify Serbia's current official self-employment / digital-nomad implementing checklist, exact financial threshold, official fees, processing route, and dependent/family mechanics for spouse vs unmarried partner.
- Verify whether Serbian temporary protection has any ordinary-residence bridge or explicit interaction with an existing Polish residence/temporary-protection status.
- Verify direct annual sunny/clear-day counts for Belgrade, Novi Sad, and Niš.
- Research Serbia taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-044` — Serbia digital-nomad / self-employment official checklist, threshold, fees, and dependent mechanics.
- `vq-045` — Serbia post-TP bridge and Polish residence/TP interaction.
- `vq-046` — Serbia direct sunny/clear-day counts for Belgrade, Novi Sad, and Niš.

## Recommendation for next iteration

- Enter verification mode because the pending/open queue is now above threshold; close a focused batch of legal and/or sunny-day blockers before continuing the non-EU Europe country rotation.
