# Dimension: Tier-field consistency check

Last updated: 2026-07-06
Mode: consolidation
Inputs: `state.json`, `countries.yml`, `INDEX.md`, country frontmatter, `verification-queue.md`, `sources/sources.md`, `claims/*.yml`, `scripts/find-stale.py`

## Scope

This is a structural consistency check after the completed tier-application workflow. It does not assign new tiers, rank countries, or recommend a relocation order. It verifies that the tier and aggregate fields exposed to downstream synthesis agree across the live vault files.

## Checks performed

- Compared `tier`, `depth_score`, and `unverified_count` across all 33 country frontmatter blocks, `state.json`, `countries.yml`, and `INDEX.md`.
- Counted actual pending/open verification items in `verification-queue.md` and compared the result with `state.json`.
- Counted actual `## src-NNN` source headings in `sources/sources.md` and compared the result with `state.json`.
- Counted loaded claim entries across `claims/*.yml` and compared the result with `state.json`.
- Ran `scripts/find-stale.py` as the staleness trigger check.

## Results

| Check | Result |
|---|---|
| Countries present in state / countries.yml / INDEX | 33 / 33 / 33 |
| Tier-field mismatches | 0 |
| Depth-score mismatches | 0 |
| Country-local unverified-count mismatches | 0 |
| Pending/open verification queue items | 0 |
| Source headings | 839 |
| Claim entries | 716 |
| Stale claims | 0 |

## Tier distribution confirmed

| Assigned tier | Count | Countries |
|---|---:|---|
| Tier 1 | 2 | Greece, Poland |
| Tier 2 | 13 | Spain, Portugal, Italy, Czech Republic, Slovakia, Slovenia, Montenegro, Serbia, Turkey, Georgia, Albania, Uruguay, Paraguay |
| Tier 3 | 8 | Moldova, Panama, Argentina, Malaysia, Thailand, Indonesia, Kazakhstan, Armenia |
| Tier X | 10 | Cyprus, Croatia, Malta, Romania, Bulgaria, Hungary, North Macedonia, Bosnia and Herzegovina, Mexico, UAE |

## Consolidation conclusion

The tier-application workflow is structurally consistent across the vault. Downstream synthesis can consume assigned screening tiers, `depth_score`, risk flags, and partial-section caveats without first repairing tier-field drift. The assigned tiers are still screening classifications, not a TOP-N ranking or final relocation recommendation.

## Next consolidation candidate

Prepare a non-ranking synthesis-input map for the remaining cross-country dimensions that are not yet consolidated, especially §5.1 route durability, §5.3 tax/budget stress, §5.4/§5.5 cost and rent, §5.6/§5.7 healthcare and education, and §5.8/§5.9 comfort and partner fit.
