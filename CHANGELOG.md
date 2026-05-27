---
document: changelog
version: 1.0.0
last_updated: 2026-05-26
---

# CHANGELOG

Brief delta per iteration. Append-only.

## 2026-05-27 — run-014 — romania-legalization-climate

- Romania profile created from template.
- Romania: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Digital-nomad visa captured: Law 22/2022, €3,300/month income, 12+12 months, no Romanian tax (aggregator source; official-primary confirmation queued).
- OUG 194/2002 (consolidated April 2026) captured as official-primary anchor: defines "nomad digital", visa types, family reunification (Art. 62), EU long-term residence conditions (Art. 71).
- Ukrainians exempt from short-stay visa (MAE Annex 2) confirmed.
- Climate first pass for Bucharest, Cluj-Napoca, and Timișoara completed (continental; cold winters; ~2,030–2,130 sunshine hours/year).
- Sources added: src-068 … src-075.
- Claims added: claim-romania-001 … claim-romania-008.
- Verification queue: 6 → 13 pending/open items (7 new Romania items: `vq-022` through `vq-028`).
- Next: country-deep-dive on Bulgaria (sections 5.1, 5.2) or verification if queue crosses threshold.

## 2026-05-27 — run-013 — poland-legalization-climate

- Poland profile created from template.
- Poland: depth_score 0 → 1.5 (section 5.2 completed; section 5.1 advanced to partial).
- CUKR card (3-year temporary residence for former Ukrainian TP holders) captured from official-primary UdSC sources.
- Family-reunification potential via partner's existing Polish `karta pobytu` flagged for verification.
- Climate first pass for Warsaw, Krakow, and Wroclaw completed.
- Sources added: src-062 … src-067; src-002 usage extended to Poland.
- Claims added: claim-poland-001 … claim-poland-008.
- Verification queue: 5 → 6 pending/open items (`vq-021` added: Poland family-reunification rules for unmarried partners).
- Next: country-deep-dive on Romania (sections 5.1, 5.2) or verification if queue crosses threshold.

## 2026-05-26 — run-012
- Mode: verification; resolved 5 queue items (`vq-004`, `vq-008`, `vq-013`, `vq-017`, `vq-019`).
- Spain, Portugal, Cyprus, and Malta: post-2027 TP bridge blockers closed to conservative “no captured bridge; plan ordinary route before TP expiry” baselines.
- Czech Republic: official-primary special long-term residence anchor added; PR counting rule updated (special residence counts full, prior TP counts one-half).
- Sources added: src-061.
- Verification queue: 10 → 5 pending/open items.

## 2026-05-26 — run-011
- Czech Republic profile created from template.
- Czech Republic: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Sources added: src-053 … src-060; src-002 usage extended to Czech Republic.
- Claims added: claim-czech-001 … claim-czech-005.
- Verification queue: 8 → 10 pending/open items (`vq-019`, `vq-020` added).
- Next: verification pass because the queue has reached the scheduled-run threshold.

## 2026-05-26 — run-010
- Malta profile created from template.
- Malta: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Sources added: src-046 … src-052; src-002 usage extended to Malta.
- Claims added: claim-malta-001 … claim-malta-005.
- Verification queue: 6 → 8 pending/open items (`vq-017`, `vq-018` added).
- Next: country-deep-dive on Czech Republic (sections 5.1, 5.2) unless queue crosses verification threshold.

## 2026-05-26 — run-009
- Mode: verification; resolved 5 queue items (`vq-003`, `vq-011`, `vq-012`, `vq-015`, `vq-016`).
- Greece: depth_score 1.0 → 1.5; §5.2 climate passed using Current Results clear-sky statistics.
- Croatia: depth_score 1.0 → 1.5; §5.2 climate passed using direct sunshine-day counts.
- Sources added: src-044, src-045.
- Verification queue: 11 → 6 pending/open items.

## 2026-05-24 — run-001 — bootstrap-v2

- Vault structure created from scratch
- Foundational docs in place: `criteria.md` v2.0.0, `vault-protocol.md` v1.0.0, `CONTEXT.md` v1.0.0
- 33 countries indexed with tier hints in `countries.yml` and `state.json`
- All boilerplate files and 4 validator scripts created
- Validators passed
- No research performed yet
- Next: country-deep-dive on Greece (sections 5.1, 5.2)

## 2026-05-24 — run-002 — greece-legalization-climate

- Greece profile created from template
- Greece: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-001 … src-010
- Claims added: claim-greece-001 … claim-greece-004
- Verification queue: 0 → 3
- Next: verification pass on DN primary checklist, Polish karta pobytu interaction, and sunny-day counts

## 2026-05-24 — run-003 — spain-legalization-climate

- Spain profile created from template
- Spain: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-011 … src-016
- Claims added: claim-spain-001 … claim-spain-005
- Verification queue: 3 → 6
- Next: country-deep-dive on Portugal (sections 5.1, 5.2)

## 2026-05-24 — run-004 — portugal-legalization-climate

- Portugal profile created from template
- Portugal: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-017 … src-024
- Claims added: claim-portugal-001 … claim-portugal-005
- Verification queue: 6 → 10
- Next: verification pass across Greece / Spain / Portugal blockers because queue threshold reached 10

## 2026-05-25 — run-005 — verification-pass-legalization-climate

- Verification queue: 10 → 5
- Spain: depth_score 1.0 → 1.5 (section 5.2 climate closed to DoD with direct clear-day counts)
- Portugal: official-primary AIMA remote-work residence filing route captured
- Poland-residence interaction clarified for Greece, Spain, and Portugal baseline planning
- Sources added: src-025, src-026
- Facts verified: 5

## 2026-05-25 — run-006 — italy-legalization-climate

- Italy profile created from template
- Italy: depth_score 0 → 1.5 (section 5.2 completed; section 5.1 advanced to partial)
- Sources added: src-027 … src-034
- Claims added: claim-italy-001 … claim-italy-005
- Verification queue: 5 → 7
- Next: country-deep-dive on Cyprus (sections 5.1, 5.2)

## 2026-05-25 — run-007 — cyprus-legalization-climate

- Cyprus profile created from template
- Cyprus: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-035 … src-039
- Claims added: claim-cyprus-001 … claim-cyprus-005
- Verification queue: 7 → 9
- Next: country-deep-dive on Croatia (sections 5.1, 5.2)

## 2026-05-25 — run-008 — croatia-legalization-climate

- Croatia profile created from template
- Croatia: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-040 … src-043
- Claims added: claim-croatia-001 … claim-croatia-005
- Verification queue: 9 → 11
- Next: verification mode because queue threshold is now reached
