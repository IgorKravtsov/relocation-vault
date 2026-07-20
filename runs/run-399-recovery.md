---
run_id: 399
date: 2026-07-20T15:00:09Z
agent: hermes
mode: recovery
target_country: null
target_sections: []
target_criterion: pre-flight
duration_minutes: 1
sources_added: []
facts_added: 0
facts_verified: 0
claims_added: []
files_modified:
  - runs/run-399-recovery.md
proposals_created: []
completed_at: 2026-07-20T15:00:09Z
status: completed
schema_version: 2.0.0
---

# Run 399 — recovery mode

## Trigger
Pre-flight failed because the checkout was dirty before this scheduled iteration began.

## Evidence
`git status --short --branch` reported:

```text
## main...origin/main
 M CHANGELOG.md
 M INDEX.md
 M dimensions/final-synthesis-readiness-checklist.md
 M dimensions/handoff-maintenance-check.md
 M state.json
?? runs/run-391-scheduled-no-trigger-recheck.md
```

## Action taken
Per vault-protocol recovery rules, no country profiles, sources, claims, verification queue, state, index, changelog, proposal, or dimension files were modified by this run. This run wrote only this recovery log so the next iteration has an explicit health record.

## Required next step
Resolve or commit the pre-existing dirty working tree before attempting another normal research iteration.
