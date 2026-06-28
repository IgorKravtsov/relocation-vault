---
run_id: 224
date: 2026-06-28T01:27:33Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-819]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/slovakia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-224-bureaucracy-practicality-slovakia.md
proposals_created: []
completed_at: 2026-06-28T01:27:33Z
status: completed
schema_version: 2.0.0
---

# Run 224 - bureaucracy/practicality criterion slice, Slovakia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Slovakia, following run-223's next hint.

## What was done

- Converted Slovakia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: embassy-first business-residence filing, mandatory Ministry of Economy business-plan opinion, Slovak translation / apostille-superlegalisation burden, post-approval insurance and medical-report deadlines, and no captured TP-to-ordinary-status bridge.
- Added one neutral professional-services contact lead, AKMV Law Firm in Bratislava, with public phone, email, and address details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Slovakia frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-819`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Slovakia 9.0 -> 10.0.

## Key findings

- Slovakia's route is visible but adviser-dependent: the ordinary self-employed/business route is a business-plan and real-business file, not a digital-nomad substitute.
- The filing calendar must coordinate embassy submission, accommodation, insurance within three working days after residence-document collection, medical report within 30 days, SZCO/tax/VAT setup, and partner status.
- Bratislava is the practical legal/accounting hub; Kosice remains the services/cost compromise; Poprad is affordability-first only if professional and healthcare support can be confirmed.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Slovenia unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Slovakia application-prep should compare independent immigration lawyers and accountants; confirm embassy appointment behavior, business-plan practice for foreign-client IT, trade-office/SZCO setup, VAT/reverse-charge reporting, insurer choice, medical-report provider, lease evidence, and spouse/family sequencing.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Slovenia unless accepted proposals, verification threshold, or staleness checks take priority.
