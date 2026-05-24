---
document: glossary
version: 1.0.0
last_updated: 2026-05-24
---

# GLOSSARY

Terms, scales, markers, modes, autonomy levels, and tags used across the vault.

## Tier scale (countries)

| Tier | Definition |
|------|------------|
| **Tier 1** | Realistic path to citizenship ≤10 years for remote IT freelancer without local employer. VNZh available now, post-03.2027 transition is clear. |
| **Tier 2** | Realistic path to PR. Citizenship difficult (language, terms, dual citizenship constraints). VNZh stable and renewable. |
| **Tier 3** | Only renewable VNZh. PR path blocked or impractical. Suitable as long-term base, not as path to citizenship. |
| **Tier X** | Serious problems: no clear path post-03.2027, high refusal risk, political/currency instability, $3000 income doesn't qualify. |

Tier is assigned **by research outcome**, not before research. Justification with sources required in profile Block 1.

## depth_score scale

| Value | Meaning |
|-------|---------|
| 0 | Not started |
| 1–3 | Initial pass, few sections covered |
| 4–6 | Most sections drafted, some pending |
| 7–9 | All sections covered, gaps and verification pending |
| 10 | All 11 sections completed (DoD passed), Practical Playbook present, sources verified |

Computed as: `count(sections_completed) + 0.5 × count(sections_partial)`, capped at 10.

## confidence scale

| Level | Definition |
|-------|------------|
| **high** | Official primary source 2025–2026; or ≥2 independent official sources. |
| **medium-high** | Official primary 2023–2024 (may be outdated); or 2+ cross-referenced reputable secondary 2025–2026. |
| **medium** | One reputable secondary 2025–2026; or 3+ community posts 2025–2026 with consistent data. |
| **low** | Single community post; expert opinion without confirmation; old data (≤2023) without cross-reference. |
| **N/A** | `[требует верификации]` — fact not used in scoring. |

## Markers

All markers use **English** form (per language rule in `vault-protocol.md`). Russian aliases listed for reference only — do not use in new content.

| Marker (canonical English) | Meaning | Russian alias (legacy) |
|----------------------------|---------|------------------------|
| `[verification required]` | Fact not confirmed by primary source. Not used in scoring. | `[требует верификации]` |
| `[stale, last verified YYYY-MM-DD]` | Fact older than staleness threshold for its type. Confidence downgraded by one step. | — |
| `[single source]` | Fact from only one source. Pending cross-reference. | `[единственный источник]` |
| `[no date, verification required]` | Community-source statement without identifiable date. Not used in scoring. | `[без даты, требует верификации]` |
| `[archive: failed YYYY-MM-DD]` | Wayback archive attempt failed for this URL. | — |
| `[2024 data, check freshness]` | Data from 2024, may need refresh. | — |
| `[L2-editable]` | Section of `vault-protocol.md` that Hermes may edit at L2 autonomy after a single accepted proposal. | — |

## Modes of iteration

| Mode | When to use | Target output |
|------|-------------|---------------|
| `bootstrap` | Initial vault creation | Full vault skeleton |
| `country-deep-dive` | Deepen one country profile | +2 to depth_score, 2+ sections to DoD |
| `criterion-slice` | One criterion across multiple countries | 4+ countries covered, `dimensions/<criterion>.md` updated |
| `verification` | Close `[требует верификации]` markers | 5+ queue items resolved |
| `cross-reference` | Resolve conflicts between sources/facts | Decisions added to `decisions/decisions.md` |
| `staleness-check` | Refresh facts older than thresholds | Stale claims re-verified |
| `consolidation` | Merge duplicates, normalize structure | Duplicates removed/merged |
| `proposal-apply` | Apply accepted self-improvement proposals | All accepted proposals applied, versions bumped |
| `recovery` | Internal mode after pre-flight failure | Issue logged, no data changes |

## Autonomy levels

| Level | Scope | When |
|-------|-------|------|
| **L1 — free** | Append data to `countries/`, `claims/`, `sources/`, `state.json`, `runs/`, `verification-queue.md`, `decisions.md`, `CHANGELOG.md`, `INDEX.md`, `digests/`. | Always allowed. |
| **L2 — log-and-apply** | `countries/_TEMPLATE.md`, new tags in `GLOSSARY.md`, scripts, `[L2-editable]` sections of `vault-protocol.md`. | After one accepted proposal — free thereafter. |
| **L3 — propose-only** | `criteria.md`, core `vault-protocol.md`, DoD checklists, weights, confidence scale. | Only via explicit proposal + human approval. |

## Starter tag set

Tags for `claims/*.yml` `tags:` list. New tags may be added via L2 process.

### Visa / legalization
- `#dn-visa` — digital nomad visa related
- `#tp-extension` — temporary protection mechanism
- `#income-threshold` — minimum income for visa/permit
- `#married-only` — option requires marriage
- `#unmarried-ok` — option works without marriage
- `#polish-kp-conflict` — known interaction with Polish karta pobytu
- `#post-2027-clear` — explicit legislated post-03.2027 transition
- `#post-2027-unclear` — no announced transition

### Tax
- `#flat-tax` — flat tax regime available
- `#progressive-tax` — progressive tax
- `#new-resident-relief` — special relief for new residents

### Cost of living
- `#rent-expensive` — rent significant share of $3000 budget
- `#rent-affordable` — rent comfortable share

### Citizenship / PR
- `#fast-pr` — PR in ≤3 years
- `#slow-pr` — PR in 7+ years
- `#citizenship-fast` — citizenship in ≤7 years
- `#citizenship-slow` — citizenship in >10 years
- `#dual-citizenship-allowed` — can keep Ukrainian citizenship
- `#dual-citizenship-blocked` — must renounce

### Language / culture
- `#language-requirement` — language exam required for status
- `#ukrainian-diaspora` — significant Ukrainian community
- `#russian-speaking` — Russian widely understood

### Climate
- `#climate-cold-winter` — average January below +3°C in main cities
- `#climate-warm` — Mediterranean / subtropical
- `#climate-tropical` — tropical

### Geography / logistics
- `#non-eu` — outside EU
- `#schengen` — Schengen member
- `#far-from-ukraine` — ≥10h travel from Ukraine

### Risk
- `#bank-friendly` — easy banking for Ukrainians
- `#currency-risk` — local currency volatile
- `#political-risk` — political instability noted
