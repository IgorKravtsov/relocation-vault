---
document: sources-registry
version: 1.0.0
last_updated: 2026-05-24
---

# Sources Registry

Central registry of all sources cited across the vault. Country profiles and claims reference sources by ID `[src-NNN]`. URLs and metadata live here once; profiles cite by ID without duplicating.

## Schema (per `vault-protocol.md` §3.4)

Each source entry:

- **Title**: human-readable
- **URL**: original
- **Archive**: Wayback Machine snapshot URL (mandatory except for stable gov domains; `[archive: failed YYYY-MM-DD]` if unavailable)
- **Type**: one of `official-primary` | `official-secondary` | `reputable-secondary` | `community` | `commercial` | `aggregator`
- **Date published**: YYYY-MM-DD or `unknown`
- **Date accessed**: YYYY-MM-DD
- **Used by**: country names (or `global` if applies to many)
- **Facts supporting**: brief topic list with claim IDs
- **Confidence ceiling**: max confidence this source can support
- **Stale at**: YYYY-MM-DD (when this source's data becomes stale per `vault-protocol.md` §16)

## ID convention

`src-NNN` where NNN is a zero-padded 3-digit integer. Allocate sequentially.

---

## src-001
- **Title**: Greece Ministry of Migration and Asylum — Information for Displaced Persons from Ukraine
- **URL**: https://migration.gov.gr/en/ukraine/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2022-06-15
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: TP extension to 2027 (claim-greece-001); Article 194 TP→Immigration Code bridge (claim-greece-002); one-Member-State TP rule; document-translation warning
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-002
- **Title**: Council Implementing Decision (EU) 2025/1460 extending temporary protection introduced by Decision (EU) 2022/382
- **URL**: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202501460
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-07-15
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: EU-level TP extension chain to 04 March 2027; one-Member-State TP principle
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-003
- **Title**: Hellenic Republic Ministry of Foreign Affairs — Digital Nomad Visa
- **URL**: https://www.mfa.gr/en/services/working-in-greece-as-a-digital-nomad/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: official DN route exists; MFA points applicants to practical DN guidance; DN consular application channel
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-004
- **Title**: Work From Greece FAQ
- **URL**: https://workfromgreece.gr/faq/
- **Archive**: [archive: failed 2026-05-24]
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: DN €3,500/month after-tax threshold (claim-greece-003); spouse/child uplift (claim-greece-004); 1-year visa then 2-year permit; no Greek-employer work; fast-track / 10-day response
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-24

## src-005
- **Title**: Greece Ministry of Migration and Asylum — Residence Permit Categories for Third Country Citizens & Documents to be Submitted
- **URL**: https://migration.gov.gr/en/migration-policy/metanasteusi-stin-ellada/katigories-adeion-diamonis-politon-triton-choron-dikaiologitika%E2%80%8B/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2020-06-25
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Immigration Code residence-permit categories exist beyond TP and DN
- **Confidence ceiling**: high
- **Stale at**: 2027-05-24

## src-006
- **Title**: Greece Ministry of Migration and Asylum — Exclusive electronic renewal of all categories of residence permits for third country nationals
- **URL**: https://migration.gov.gr/en/ilektroniki-ananeosi-olon-ton-katigorion-titlon-diamonis-ton-politon-triton-choron/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2021-11-12
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: renewals handled electronically through ministry e-services
- **Confidence ceiling**: high
- **Stale at**: 2027-05-24

## src-007
- **Title**: Greece Ministry of Interior — Acquisition of the Greek Citizenship (supporting documents page)
- **URL**: https://www.ypes.gr/en/?post_type=page&p=18427
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: citizenship pathway categories include third-country nationals with long-term resident status and foreigners holding permanent residence permits
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-24

## src-008
- **Title**: Wikipedia — Athens climate table
- **URL**: https://en.wikipedia.org/wiki/Athens
- **Archive**: [archive: failed 2026-05-24]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Athens January/July temperatures; humidity; sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-009
- **Title**: Wikipedia — Thessaloniki climate table
- **URL**: https://en.wikipedia.org/wiki/Thessaloniki
- **Archive**: [archive: failed 2026-05-24]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Thessaloniki January/July temperatures; humidity; sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-010
- **Title**: Wikipedia — Heraklion climate table
- **URL**: https://en.wikipedia.org/wiki/Heraklion
- **Archive**: [archive: failed 2026-05-24]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Heraklion January/July temperatures; humidity; sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31
