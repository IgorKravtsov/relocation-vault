---
run_id: 223
date: 2026-06-27T22:22:40Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-818]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/hungary.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-223-bureaucracy-practicality-hungary.md
proposals_created: []
completed_at: 2026-06-27T22:22:40Z
status: completed
schema_version: 2.0.0
---

# Run 223 - bureaucracy/practicality criterion slice, Hungary

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Hungary, following run-222's next hint.

## What was done

- Converted Hungary's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: White Card consular/Enter Hungary mechanics, guest self-employment evidence burden and 3-year cap, independent partner-status problem, and no captured TP-to-ordinary-status bridge.
- Added one neutral professional-services contact lead, Helpers Hungary Kft in Budapest, with public phone, email, and address details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Hungary frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-818`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Hungary 9.0 -> 10.0.

## Key findings

- Hungary is administratively visible but fragile: White Card has a published 21-day procedure baseline, yet income and partner sponsorship make it awkward for the couple.
- Guest self-employment is the more route-relevant fallback, but it links immigration, NAV tax, social-security/TAJ, VAT, lease, and evidence questions, with a 3-year cap.
- Budapest is the practical services hub; Debrecen and Pecs remain cheaper bases only if local English-speaking healthcare/professional support is confirmed.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Slovakia unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Hungary application-prep should compare independent immigration lawyers and accountants; confirm OIF/Enter Hungary appointment behavior, exact translations/apostilles, White Card vs guest-self-employment sequencing, TAJ/NEAK onboarding, tax/VAT setup, lease evidence, and spouse/family options.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Slovakia unless accepted proposals, verification threshold, or staleness checks take priority.
