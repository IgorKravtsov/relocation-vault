---
run_id: 228
date: 2026-06-28T18:30:13Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-823]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/turkey.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-228-bureaucracy-practicality-turkey.md
proposals_created: []
completed_at: 2026-06-28T18:30:13Z
status: completed
schema_version: 2.0.0
---

# Run 228 - bureaucracy/practicality criterion slice, Turkey

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Turkey, following run-227's next hint.

## What was done

- Converted Turkey's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: PMM / e-ikamet and GoTurkey online anchors, USD 3,000/month DN evidence, eight-year ordinary long-term-residence planning, address/open-district caution, insurance, tax/SGK/VAT, and partner/marriage sequencing.
- Added one neutral contact lead, Ata Kurumsal, with public English work/residence-permit and company-establishment services plus contact email.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Turkey frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-823`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Turkey 9.0 -> 10.0.

## Key findings

- Turkey is operationally screenable because PMM / e-ikamet and GoTurkey give visible online anchors for residence and DN evidence.
- The binding practicality risk is margin and coordination: USD 3,000/month is only the DN floor, and the couple needs a residence-usable address, Turkish-language help, tax/SGK/VAT advice, insurance evidence, and partner/marriage sequencing before a long lease.
- Izmir remains the first practical base; Antalya is the warm-coast alternative; Istanbul is mainly for professional services, airports, diaspora, or private services despite rent/crowding pressure.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Georgia unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Turkey application-prep should compare immigration advisers and accountants; confirm current e-ikamet / DN checklist, fees, residence-open districts, translation/notarisation rules, insurance wording, SGK/Bag-Kur base, VAT/export-of-services handling, lease/address evidence, and family-residence proof.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Georgia unless accepted proposals, verification threshold, or staleness checks take priority.
