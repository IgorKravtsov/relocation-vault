---
document: migrations
version: 1.0.0
last_updated: 2026-05-24
---

# MIGRATIONS

Recipes for schema/format changes between versions of `criteria.md` and `vault-protocol.md`. Append entries when a major or minor version bump occurs.

## 1.0.0 — initial bootstrap-v2 (2026-05-24)

**Type**: Initial release.
**Backwards compatible**: N/A (first version).
**Recipe**:
Bootstrap performed from clean state with three foundational documents:
- `criteria.md` v2.0.0
- `vault-protocol.md` v1.0.0
- `CONTEXT.md` v1.0.0

All previous vault contents (criteria.md v1, criteria-v2.md draft, greece.md profile, old state.json, etc.) were removed prior to this bootstrap and exist only in git history.

No migration of pre-existing data was performed.
