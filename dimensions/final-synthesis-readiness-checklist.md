# Dimension: Final synthesis readiness checklist

Last updated: 2026-07-15
Mode: consolidation
Inputs: `INDEX.md`, `state.json`, `dimensions/screening-readiness-map.md`, `dimensions/route-durability-5.1.md`, `dimensions/tax-budget-stress-5.3.md`, `dimensions/cost-rent-affordability-5.4-5.5.md`, `dimensions/healthcare-education-access-5.6-5.7.md`, `dimensions/comfort-partner-fit-5.8-5.9.md`, `dimensions/risk-dimensions-5.10.md`, `dimensions/bureaucracy-practicality-5.11.md`, `dimensions/tier-field-consistency-check.md`, `dimensions/application-prep-trigger-map.md`, `dimensions/handoff-maintenance-check.md`
Consolidation status (run-356): handoff checklist for downstream synthesis, linked to a maintenance check that reconfirmed the vault remains in handoff mode when no proposal, verification, staleness, new-evidence, or explicit application-prep trigger exists. This file does not rank countries, change country tiers, update sources, update claims, or reopen resolved verification items.

## Scope

This checklist defines what is ready for a later downstream synthesis process and what must stay out of Hermes normal iterations. It is a handoff artifact, not a final relocation recommendation, TOP-N ranking, visit order, legal advice, tax advice, medical advice, school recommendation, or city shortlist.

## Readiness snapshot

- Country coverage: 33/33 profiles are researched, present in `INDEX.md`, and at depth_score 10.0 in `state.json`.
- Assigned screening tiers: 33/33 countries have assigned country-level screening tiers after runs 252-284; run-285 confirmed cross-file tier consistency.
- Verification queue: 0 pending/open items; country-local `unverified_count` values are reconciled at 0.
- Stale-claim trigger: 0 stale claims at the latest run-356 no-trigger recheck.
- Source and claim registry: 839 source headings and 716 claim entries are available for traceability.
- Non-ranking dimension coverage: route durability (5.1), tax/budget stress (5.3), cost/rent affordability (5.4/5.5), healthcare/education access (5.6/5.7), comfort/partner fit (5.8/5.9), risk dimensions (5.10), and bureaucracy/practicality (5.11) are all available.
- Application-prep handoff: `dimensions/application-prep-trigger-map.md` now defines when to start finalist-specific, filing-grade checks without reopening resolved-for-screening caveats for all countries.
- Maintenance handoff: `dimensions/handoff-maintenance-check.md` records the current no-trigger state and the safe next-action rules for scheduled normal iterations.

## Downstream synthesis input order

1. Start from `dimensions/screening-readiness-map.md` to confirm scope, queue status, and guardrails.
2. Use `dimensions/tier-field-consistency-check.md` to confirm that assigned screening tiers match across country profiles, `countries.yml`, `state.json`, and `INDEX.md`.
3. Use `dimensions/route-durability-5.1.md` as the legal-route filter: distinguish durable settlement files, conditional ordinary-residence files, bridge/base routes, and high-risk weak fits before considering lifestyle positives.
4. Use `dimensions/tax-budget-stress-5.3.md` and `dimensions/cost-rent-affordability-5.4-5.5.md` together: compare each country's tax-screening net against practical rent/city pressure rather than gross USD 3,000 alone.
5. Use `dimensions/healthcare-education-access-5.6-5.7.md` for family and future-child feasibility, preserving the distinction between public-system access, private-care dependence, and international-school cost risk.
6. Use `dimensions/comfort-partner-fit-5.8-5.9.md` to keep partner-dependency, marriage baseline, language adaptation, distance, and independent-status fallback visible.
7. Use `dimensions/risk-dimensions-5.10.md` and `dimensions/bureaucracy-practicality-5.11.md` as stress overlays, not as standalone rejection or ranking engines.
8. Return to the country profiles for the detailed route playbooks, source citations, caveats, and application-prep checks before making any human-facing recommendation.
9. Use `dimensions/application-prep-trigger-map.md` only after finalists, new evidence, stale-source triggers, or explicit application-prep instructions exist; do not use it to create a ranking.
10. Use `dimensions/handoff-maintenance-check.md` to confirm whether a scheduled normal iteration has any substantive trigger before creating additional broad consolidation.

## Required guardrails for any later TOP-N process

- Do not use row order in any dimension file as a ranking.
- Do not treat assigned screening tiers as a final recommendation; they are a screening taxonomy tied to captured evidence and route viability.
- Do not promote partial 5.1, 5.3, or 5.6 sections to completed status without a later country-specific iteration.
- Do not turn resolved-for-screening verification details into open blockers unless new evidence changes the screening answer.
- Do not treat cheap rent, low tax, or warm climate as decisive when route durability is weak or income-gated.
- Do not assume unmarried-partner dependency unless the country profile captured route-specific evidence; marriage or independent status remains the conservative baseline in many profiles.
- Do not assume bridge/base routes such as DN, DTV, DE Rantau, virtual work, or short digital-nomad permissions lead to PR/citizenship unless the country profile proves a durable follow-on route.

## Pre-synthesis checks

Before a downstream final synthesis begins, verify:

- `git status` is clean and the latest `main` is pulled.
- `scripts/validate-frontmatter.py` passes.
- `scripts/check-sources.py` passes.
- `state.json.version` is 2.
- `state.json.verification_queue_size` remains 0 or any new pending/open items are handled before recommendation work.
- Source and claim counts are recomputed from files rather than inferred from max IDs.
- Any country profile edited after run-291 is reread before relying on this checklist.

## Remaining work outside this checklist

- Final ranking, TOP-N selection, recommendation narrative, and visit/order planning remain downstream work and should not be produced by a normal Hermes relocation-vault iteration.
- Application-prep details still belong to later country-specific work once a human chooses finalists or another trigger in `dimensions/application-prep-trigger-map.md` exists: lawyer/accountant review, live insurance quotes, live rent listings, school fee schedules, consular filing instructions, translations/apostilles, and current appointment/fee checks.
- If future evidence changes a country's route, tax, healthcare, education, or partner baseline, update the country profile and the relevant dimension map before using this checklist again.
