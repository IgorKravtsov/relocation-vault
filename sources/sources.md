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

_(no sources yet — first sources will be added during the first research iteration)_
