---
run_id: 53
date: 2026-06-05T17:59:29Z
agent: hermes
mode: country-deep-dive
target_country: Armenia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-274", "src-275", "src-276", "src-277", "src-278"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-armenia-001", "claim-armenia-002", "claim-armenia-003", "claim-armenia-004", "claim-armenia-005"]
files_modified:
  - countries/armenia.md
  - claims/armenia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-053-armenia-legalization-climate.md
proposals_created: []
completed_at: 2026-06-05T17:59:29Z
status: completed
schema_version: 2.0.0
---

# Run 053 - Armenia legalization and climate

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue is below the active threshold.
- Open Armenia as the last depth-0 country in the current research set.
- Focus on sections 5.1 and 5.2: entry, ordinary residence / business-activity route fit, PR/citizenship baseline, partner mechanics, and climate.

## What was done

- Created `countries/armenia.md` and `claims/armenia.yml`.
- Added five Armenia sources (`src-274` through `src-278`): MFA visa framework / visa-free lists, MFA residency, MFA citizenship, Climate to Travel, and WeatherSpark.
- Advanced section 5.1 to partial: Ukrainian passport holders have an official visa-free regime baseline for scouting; Armenia MFA lists temporary residence for study, work permit, close family, business activity, Armenian nationality, and other legal cases; temporary residence is up to one year and extendable.
- Captured residence documents, fees, filing office, and up-to-30-day processing from MFA: passport + copy + notarized Armenian translation, photos, residence-ground evidence, medical certificate, fee receipt; AMD 105,000 temporary card and AMD 140,000 permanent card.
- Treated Armenia as an ordinary business/self-employment residence candidate, not a confirmed digital-nomad route. The exact foreign-client IT / IE / LLC evidence pattern remains queued.
- Captured the MFA citizenship baseline: adults may apply through the 2026 electronic system if they meet one of the listed grounds, including at least three years of permanent and lawful residence, but counting for business residence needs verification.
- Completed section 5.2: Yerevan, Gyumri, and Sevan now have January/July temperature baselines; Yerevan/Gyumri have WeatherSpark clearer-sky day-equivalent proxies; humidity/muggy burden is low, but Yerevan summer heat and cold highland winters are major comfort risks.
- Added risk flags `ordinary-business-residence-not-dn`, `settlement-ladder-needs-business-substance`, `partner-baseline-marriage`, and `cold-winters-hot-yerevan-summers`.
- Added `vq-086`, `vq-087`, and `vq-088` for Ukraine-specific protection/bridge, foreign-client IT business-residence mechanics, and spouse/unmarried-partner mechanics.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 3 to 6.

## What remains

- Armenia taxes, cost of living, rent, healthcare, education, comfort, partner mechanics, risk dimensions, bureaucracy, and practical budget remain pending.
- Core legal blockers: whether any Ukraine-specific protection / humanitarian stay exists; whether a foreign-client IT worker can use a business-activity temporary residence via individual entrepreneur or LLC; whether that path counts cleanly toward permanent residence and citizenship; and whether unmarried partner sponsorship exists.
- Climate section is complete for first-pass screening, but later city-selection work should compare Yerevan heat/air quality, Gyumri winter cold, and Sevan as a summer-only comfort hedge.

## Open questions added

- `vq-086` — Armenia Ukraine-specific protection / humanitarian stay / post-2027 bridge.
- `vq-087` — Armenia business-activity residence fit for foreign-client IT and PR/citizenship counting.
- `vq-088` — Armenia spouse vs unmarried-partner dependent mechanics.

## Recommendation for next iteration

- Continue country-deep-dive mode because the queue remains below the active threshold. Malaysia has the lowest depth_score after Armenia was opened; it should receive either climate closure plus one practical section, or another low-depth country should receive a practical-section pass depending on anti-clustering and queue pressure.
