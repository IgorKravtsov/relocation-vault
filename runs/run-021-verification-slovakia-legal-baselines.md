---
run_id: 21
date: 2026-05-29T16:06:51Z
agent: hermes
mode: verification
target_country: Slovakia
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 34
sources_added: ["src-108", "src-109"]
facts_added: 2
facts_verified: 2
claims_added: ["claim-slovakia-008", "claim-slovakia-009"]
files_modified:
  - countries/slovakia.md
  - claims/slovakia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-29T16:06:51Z
status: completed
schema_version: 2.0.0
---

# Run 021 — Verification closure: Slovakia legal baselines

## Plan

- Enter verification mode because the pending verification queue reached 11 after run-020.
- Resolve a focused Slovakia legal/status batch before continuing fresh-country rotation.
- Prioritize high-priority blockers where existing EU/UNHCR sources and quickly capturable Slovak official sources can support a safe operational baseline.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Added `src-108`, a Slovak Ministry of Economy official-primary page for foreigners running a business in Slovakia.
- Resolved `vq-036`: Slovakia business/self-employed residence is now anchored to the Ministry of Economy's 2025+ operational filter: applications at Slovak diplomatic missions abroad, mandatory business plan, feasibility/sustainability/economic-contribution assessment, and extension scrutiny of real business activity rather than virtual business.
- Added `src-109`, a Slovak Ministry of Interior official-primary announcement confirming automatic temporary-refuge extension for displaced people from Ukraine to 04 March 2027.
- Resolved `vq-037`: the captured official update confirms extension mechanics but not a TP-to-ordinary-residence bridge, so the Slovakia profile now uses the conservative baseline: plan ordinary Slovak status before TP expiry unless a later official transition appears.
- Updated `countries/slovakia.md`, `claims/slovakia.yml`, `verification-queue.md`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Pending verification queue reduced from 11 to 9.
- Added 2 official-primary sources and 2 Slovakia claims.
- No depth_score change; this was a verification run.

## What remains

- Slovakia still needs direct annual sunny/clear-day counts for Bratislava, Košice, and Poprad (`vq-038`).
- Older pending items remain for Greece DN checklist (`vq-002`), Cyprus/Malta/Czech/Romania/Bulgaria/Hungary climate sunny-day blockers, and Romania DN official checklist (`vq-022`).
- Slovakia still needs future deep dives on taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.

## Recommendation for next iteration

- Resume country-deep-dive rotation because the pending queue is below the verification threshold; open Slovenia sections 5.1 and 5.2 as the next depth-0 Tier-2-hint EU country, unless accepted proposals appear.
