---
run_id: 174
date: 2026-06-21T14:09:50Z
agent: hermes
mode: country-deep-dive
target_country: Poland
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-758", "src-759"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-poland-026", "claim-poland-027"]
files_modified:
  - countries/poland.md
  - claims/poland.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-174-poland-comfort-partner.md
proposals_created: []
completed_at: 2026-06-21T14:09:50Z
status: completed
schema_version: 2.0.0
---

# Run 174 - Poland comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the state hint and rotate to Poland sections 5.8 and 5.9.

## What was done

- Added Poland comfort-of-life coverage using safety proxies, existing Ukraine / CUKR / NFZ / education support infrastructure, EF EPI English-proficiency evidence, and city-comfort synthesis for Warsaw, Krakow, and Wroclaw.
- Added Poland partner/student-fit coverage using the existing family-reunification spouse evidence, CUKR / PESEL UKR alternatives, remote-study posture, work-right caution, and one-income budget screen.
- Added sources `src-758` and `src-759`, plus claims `claim-poland-026` and `claim-poland-027`.
- Updated Poland frontmatter, scoring row, practical verdict, playbook source list, Block 8 checks, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Poland sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Poland is comfort-positive for safety, high English proficiency, Ukrainian support infrastructure, and practical large-city services, especially Wroclaw/Krakow.
- Polish language remains important for bureaucracy, leases, healthcare, schooling, and long-term integration; Warsaw is services-rich but rent-stressed.
- For the student partner, marriage or independent CUKR / PESEL UKR eligibility is the conservative residence baseline; remote Ukrainian study does not create Polish residence rights, and the one-income margin depends on confirming ZUS/tax and rent.

## What remains

- Poland still needs risk dimensions and bureaucracy/practicality coverage, plus later PR/citizenship counting, business-residence, accountant/ZUS/VAT, exact voivode income-document, insurance, and selected-city application-prep checks.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Romania sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
