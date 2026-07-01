# Dimension: Tier-normalization worksheet

Last updated: 2026-07-01
Mode: consolidation
Inputs: `dimensions/tier-readiness-audit.md`, `state.json`, `INDEX.md`, country Block 1 summaries, partial-section state, risk flags

## Scope

This worksheet is a non-ranking normalization layer between the completed country profiles and any later write to `tier` fields. It does not assign final tiers in country frontmatter, `countries.yml`, or `state.json`. It records the screening-safe tier band that the next schema-safe tier-application pass should review country by country.

## Guardrails applied

- `tier_hint` was treated as an input signal, not as an automatic final tier.
- Countries are grouped by route type and blockers, not ordered within a group.
- Partial §5.1, §5.3, and §5.6 caveats remain active confidence limits even where screening depth is 10.0.
- Bridge-only countries are not promoted to settlement tiers just because cost, tax, or climate screens well.
- No TOP-N recommendation, visit order, or final relocation advice is made here.

## Normalized screening bands

| Band | Countries | Screening interpretation | Confidence limit |
|---|---|---|---|
| Durable-settlement candidate | Spain, Portugal, Italy, Greece, Cyprus, Croatia | Has a plausible long-stay or remote-work / self-employment route plus an EU-style residence/citizenship ladder, but each still has route, tax, insurance, or budget caveats before final tier assignment. | Medium until exact post-2027 bridge, tax-status, health-insurance, and filing-route details are checked per country. |
| Conditional EU / nearby-Europe candidate | Malta, Czech Republic, Poland, Romania, Bulgaria, Hungary, Slovakia, Slovenia, Montenegro, Serbia, Turkey, Georgia, Albania | Has a plausible residence or ordinary-status path for screening, but the durable ladder is more conditional, income-gated, tax-heavy, evidence-heavy, or dependent on ordinary business/self-employment mechanics. | Medium-low to medium; do not treat these as Tier 1 without country-specific legal/tax confirmation. |
| Ordinary-residence / Latin America candidate | Uruguay, Paraguay, Panama | Has an ordinary residence or lawful-activity route that can screen on the current budget, but exact means-of-life, tax registration, dependent, and long-term-status mechanics need application-prep checks. | Medium; not automatically above EU options because distance, services, healthcare, and professional-support depth differ. |
| Bridge / high-burden / uncertain-settlement candidate | North Macedonia, Bosnia and Herzegovina, Moldova, Mexico, Argentina, UAE, Malaysia, Thailand, Indonesia, Kazakhstan, Armenia | Useful for bridge/base or ordinary-business planning, but the captured route is income-gated, short-term, high-burden, uncertain for remote IT settlement, or weak as a predictable PR/citizenship ladder for the couple's current profile. | Medium-low for final tier; keep final `tier` null until a schema-safe tier application pass writes explicit country rationales. |

## Country-level application notes

- The first application pass should not bulk-convert all rows. It should write explicit tier rationale in each country Block 1 before changing frontmatter/state.
- If a country remains `tier: null`, the run log should name the blocker rather than silently skipping it.
- The safe first batch for actual `tier` writes is probably a small representative set across bands, not all 33 at once, because frontmatter, `countries.yml`, `state.json`, and `INDEX.md` must stay synchronized.
- No new sources are needed for this worksheet; it summarizes already captured country-profile evidence and resolved verification state.

## Next consolidation candidate

Run a schema-safe tier-application pass on a small batch of countries: update Block 1 tier wording, country frontmatter, `countries.yml`, `state.json`, and `INDEX.md` together, then validate that no profile still says `Tier: TBD` after a non-null tier is written.
