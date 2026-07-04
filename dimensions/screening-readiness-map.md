# Dimension: Screening readiness map

Last updated: 2026-07-04
Mode: consolidation
Inputs: `state.json`, `INDEX.md`, `dimensions/risk-dimensions-5.10.md`, `dimensions/bureaucracy-practicality-5.11.md`
Consolidation status (run-273): all 33 profiles remain depth 10.0, the global verification queue has 0 pending/open items, legacy country-local `unverified_count` values are reconciled, and schema-safe tier application has assigned Greece / Poland Tier 1, Spain / Portugal / Italy / Czech Republic / Slovakia / Slovenia / Montenegro / Serbia / Turkey / Georgia / Albania Tier 2, Moldova Tier 3, and Cyprus / Croatia / Malta / Romania / Bulgaria / Hungary / North Macedonia / Bosnia and Herzegovina Tier X; the remaining 11 countries stay `tier: null`.

## Scope

This scaffold records what the downstream synthesis process can safely consume without turning the vault into a final TOP-N recommendation. It does not assign new tiers, scores, or rankings. It only separates completed screening coverage from known partial sections and names the next safe research gates.

## Current coverage snapshot

- Country profiles: 33/33 researched and represented in `INDEX.md`.
- Average depth score: 10.00 from live `state.json` values.
- Full 10.0 depth profiles: 33/33 countries.
- Below-full-depth profile: none; Portugal is now 10.0, with 5.1, 5.3, and 5.6 still partial but sufficient for screening-depth coverage.
- Verification queue: 0 pending/open items at run-250 pre-flight; country-local unverified counters are also 0 after reconciliation.
- Staleness queue: 0 stale claims at run-250 pre-flight.
- Completed cross-country dimensions available for synthesis support: 5.10 risk dimensions, 5.11 bureaucracy/practicality, the run-249 tier-readiness audit, the run-250 unverified-count reconciliation note, and the run-251 tier-normalization worksheet.

## Safe synthesis inputs available now

- Use `INDEX.md` for country coverage, depth, and completed/partial section state.
- Use `state.json` as the source of truth for current depth scores, partial sections, risk flags, source count, claim count, and queue size.
- Use `dimensions/risk-dimensions-5.10.md` for cross-country operational risk categories and risk-driver wording.
- Use `dimensions/bureaucracy-practicality-5.11.md` for filing practicality, timing, and professional-support leads.
- Use country profiles for detailed route, tax, healthcare, school, cost, rent, comfort, partner, and bureaucracy caveats.
- Use `dimensions/tier-readiness-audit.md` only as a workflow-readiness check; use `dimensions/tier-normalization-worksheet.md` as a non-ranking screening-band worksheet, not as final assigned tiers.

## Do-not-use-as-final-ranking guardrails

- Do not infer a final country order from row order in any dimension file.
- Do not treat `tier_hint` as assigned final `tier`; only Greece, Spain, Portugal, Italy, Cyprus, Croatia, Malta, Czech Republic, Poland, Romania, Bulgaria, Hungary, Slovakia, Slovenia, Montenegro, Serbia, Turkey, Georgia, Albania, North Macedonia, Bosnia and Herzegovina, and Moldova have assigned final tiers after run-273, while all other countries remain null until explicit rationale is written.
- Do not promote partial 5.1, 5.3, or 5.6 sections into passed sections unless a later iteration explicitly completes them.
- Do not treat bridge routes such as DN / DTV / DE Rantau / virtual work as settlement ladders unless the country profile already proves a durable follow-on route.
- Do not collapse application-prep checks into active verification blockers when the queue is already resolved for screening.

## Open gates before any downstream TOP-N process

- Continue schema-safe small-batch tier application before writing assigned tiers broadly into country frontmatter/state; run-249 confirmed structural readiness, run-250 removed the last legacy unverified-counter mismatch, run-251 added the non-ranking worksheet, run-252 applied Greece, run-253 applied Spain, run-254 applied Portugal, run-255 applied Italy, run-256 applied Cyprus, run-257 applied Croatia, run-258 applied Malta, run-259 applied Czech Republic, run-260 applied Poland, run-261 applied Romania, run-262 applied Bulgaria, run-263 applied Hungary, and run-264 applied Slovakia, run-265 applied Slovenia, run-266 applied Montenegro, run-267 applied Serbia, run-268 applied Turkey, run-269 applied Georgia, and run-270 applied Albania, run-271 applied North Macedonia, run-272 applied Bosnia and Herzegovina, and run-273 applied Moldova.
- Decide whether cross-country dimensions are needed for 5.1, 5.3, 5.4/5.5, 5.6/5.7, and 5.8/5.9 before synthesis.
- Keep final recommendations, ranking, and visit order out of Hermes iterations unless the downstream synthesis process explicitly owns them.

## Next consolidation candidate

If no proposal, verification, or staleness trigger appears, the next safe consolidation unit is another schema-safe small-batch tier-application pass that uses `dimensions/tier-readiness-audit.md` and `dimensions/tier-normalization-worksheet.md` as guardrails while avoiding TOP-N recommendations.
