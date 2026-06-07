---
run_id: 67
date: 2026-06-07T15:45:00Z
agent: hermes
mode: verification
target_country: Greece
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-337"]
facts_added: 1
facts_verified: 1
claims_added: ["claim-greece-012"]
files_modified:
  - countries/greece.md
  - claims/greece.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-067-greece-efka-verification.md
proposals_created: []
completed_at: 2026-06-07T15:45:00Z
status: completed
schema_version: 2.0.0
---

# Run 067 - Greece EFKA verification

## Plan

- Run `verification` mode because the pending/open verification queue started at 10, meeting the active threshold.
- Focus on one high-priority tax blocker: Greece `vq-089`, the missing official EFKA 2026 self-employed / freelancer contribution table.
- Keep Greece section 5.3 partial unless Article 5C foreign-client IT fit is also resolved.

## What was done

- Captured EFKA's official 2026 self-employed / freelancer insurance-category table as `src-337`.
- Updated Greece section 5.3 with the 2026 EFKA categories and a conservative category-1 baseline.
- Added `claim-greece-012` for the EFKA minimum contribution baseline.
- Recomputed Greece's ordinary USD 3,000/month tax stress test: ordinary PIT leaves about EUR 2,105/month, and subtracting EFKA category-1 main pension + health plus unemployment contribution leaves about EUR 1,844/month, or about USD 2,131/month, before accountant and VAT filing costs.
- Removed the `greece-efka-self-employed-contribution-gap` risk flag while keeping `greece-article-5c-foreign-client-fit-gap`.

## Verification results

- Resolved `vq-089` for screening: EFKA category 1 is EUR 250.77/month for main pension + health in 2026, and EFKA adds EUR 10/month unemployment contribution.
- Exact profession/category choice, branch-specific add-ons, deductibility, and filing posture remain accountant/application-prep checks, not a screening blocker.
- Pending/open verification queue is now 9, below the active verification threshold.

## What remains

- Greece section 5.3 remains partial because Article 5C applicability to a Ukrainian foreign-client IT freelancer / DN-style file is still unresolved (`vq-090`).
- Greece cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` mode because the queue is below threshold. Prefer Slovakia section 5.3 taxes to continue low-depth Tier-2-hint tax coverage without clustering on Greece.
