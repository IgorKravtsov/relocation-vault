---
run_id: 17
date: 2026-05-28T16:08:19Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 8
sources_added: ["src-089", "src-090", "src-091"]
facts_added: 6
facts_verified: 5
claims_added: ["claim-bulgaria-009", "claim-bulgaria-010", "claim-bulgaria-011", "claim-poland-009", "claim-poland-010", "claim-romania-009"]
files_modified:
  - countries/bulgaria.md
  - countries/poland.md
  - countries/romania.md
  - claims/bulgaria.yml
  - claims/poland.yml
  - claims/romania.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-28T16:16:16Z
status: completed
schema_version: 2.0.0
---

# Run 017 — Verification closure: Bulgaria TP, Poland family, Romania D/AC baseline

## Plan

- Enter verification mode because the pending verification queue was at 12 items, above the scheduled-run threshold.
- Resolve a focused batch of legal/status blockers using existing-source baselines where possible and one new administrative source for Poland.
- Avoid country-deep-dive work and stop after one verification unit.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Resolved `vq-030` using UNHCR Bulgaria's Arrival from Ukraine page (`src-089`): Bulgaria TP registration creates PFN/ЛНЧ and a temporary registration document, may require an address card, and gives residence/work/medical/education/social-support rights.
- Resolved `vq-031` using UNHCR Bulgaria's 2026 extension notice (`src-090`) plus the EU TP source (`src-002`): TP/card renewal is confirmed through 04 March 2027, but no Bulgaria-specific automatic ordinary-residence bridge is captured; baseline is to plan an ordinary route before TP expiry.
- Resolved `vq-029` to an operational baseline from the existing EU Immigration Portal source (`src-079`): Bulgaria self-employment is not a fixed-threshold DN substitute; the key gate is an Employment Agency permit based on a detailed business plan and economic/social impact.
- Resolved `vq-021` with Polish voivodeship administrative guidance (`src-091`): family reunification via an existing Polish residence permit is safely spouse/marriage-based; no unmarried-partner beneficiary was captured; income baseline is PLN 776 net single / PLN 600 net per family member.
- Resolved `vq-027` with OUG 194/2002 Art. 43 (`src-068`): Romania D/AC is a company/shareholder-or-associate investment route with business-plan requirements, not a simple solo IT-freelancer fallback.
- Added 3 sources and 6 atomic claims.
- Updated Bulgaria, Poland, and Romania country profiles; updated `verification-queue.md`, `state.json`, and `CHANGELOG.md`.

## Verification results

- Pending verification queue reduced from 12 to 7.
- No depth_score changes; this was a verification run.

## What remains

- High-priority pending items still include Greece DN official checklist (`vq-002`) and Romania DN official checklist (`vq-022`).
- Climate sunny/clear-day blockers remain for Cyprus, Malta, Czechia, Romania, and Bulgaria.
- Bulgaria still needs direct sunny/clear-day counts and deeper sections 5.3–5.11.

## Next iteration hint

- Because the verification queue is now below threshold, resume normal country rotation with Hungary sections 5.1 and 5.2 as the next fresh Tier-2-hint EU country, unless accepted proposals appear.
