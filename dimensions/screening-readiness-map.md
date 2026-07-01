# Dimension: Screening readiness map

Last updated: 2026-07-01
Mode: consolidation
Inputs: `state.json`, `INDEX.md`, `dimensions/risk-dimensions-5.10.md`, `dimensions/bureaucracy-practicality-5.11.md`
Consolidation status (run-248): Portugal 5.2 climate moved to completed for screening, so all 33 profiles now show depth 10.0; this file remains a handoff map, not a recommendation or ranking.

## Scope

This scaffold records what the downstream synthesis process can safely consume without turning the vault into a final TOP-N recommendation. It does not assign new tiers, scores, or rankings. It only separates completed screening coverage from known partial sections and names the next safe research gates.

## Current coverage snapshot

- Country profiles: 33/33 researched and represented in `INDEX.md`.
- Average depth score: 10.00 from live `state.json` values.
- Full 10.0 depth profiles: 33/33 countries.
- Below-full-depth profile: none; Portugal is now 10.0, with 5.1, 5.3, and 5.6 still partial but sufficient for screening-depth coverage.
- Verification queue: 0 pending/open items at run-248 pre-flight.
- Staleness queue: 0 stale claims at run-248 pre-flight.
- Completed cross-country dimensions available for synthesis support: 5.10 risk dimensions, 5.11 bureaucracy/practicality, and the run-249 tier-readiness audit.

## Safe synthesis inputs available now

- Use `INDEX.md` for country coverage, depth, and completed/partial section state.
- Use `state.json` as the source of truth for current depth scores, partial sections, risk flags, source count, claim count, and queue size.
- Use `dimensions/risk-dimensions-5.10.md` for cross-country operational risk categories and risk-driver wording.
- Use `dimensions/bureaucracy-practicality-5.11.md` for filing practicality, timing, and professional-support leads.
- Use country profiles for detailed route, tax, healthcare, school, cost, rent, comfort, partner, and bureaucracy caveats.
- Use `dimensions/tier-readiness-audit.md` only as a workflow-readiness check; it is not a tier assignment or ranking.

## Do-not-use-as-final-ranking guardrails

- Do not infer a final country order from row order in any dimension file.
- Do not treat `tier_hint` as assigned final `tier`; current country `tier` fields are still null.
- Do not promote partial 5.1, 5.3, or 5.6 sections into passed sections unless a later iteration explicitly completes them.
- Do not treat bridge routes such as DN / DTV / DE Rantau / virtual work as settlement ladders unless the country profile already proves a durable follow-on route.
- Do not collapse application-prep checks into active verification blockers when the queue is already resolved for screening.

## Open gates before any downstream TOP-N process

- Decide whether Portugal's remaining partial 5.1, 5.3, and 5.6 sections need application-prep deepening or whether screening-depth coverage is sufficient for downstream use.
- Run a dedicated non-ranking tier-normalization pass before writing assigned tiers into country frontmatter/state; run-249 confirmed the vault is structurally ready but still needs explicit rationale/confidence per country.
- Decide whether cross-country dimensions are needed for 5.1, 5.3, 5.4/5.5, 5.6/5.7, and 5.8/5.9 before synthesis.
- Keep final recommendations, ranking, and visit order out of Hermes iterations unless the downstream synthesis process explicitly owns them.

## Next consolidation candidate

If no proposal, verification, or staleness trigger appears, the next safe consolidation unit is a dedicated non-ranking tier-normalization pass, using `dimensions/tier-readiness-audit.md` as the guardrail checklist and avoiding TOP-N recommendations.
