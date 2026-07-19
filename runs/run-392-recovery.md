---
run_id: 392
date: 2026-07-19T17:49:52Z
agent: hermes
mode: recovery
target_country: null
target_sections: []
target_criterion: pre-flight-dirty-working-tree
duration_minutes: 5
sources_added: []
facts_added: 0
facts_verified: 0
claims_added: []
files_modified:
  - runs/run-392-recovery.md
proposals_created: []
completed_at: 2026-07-19T17:49:52Z
status: completed
schema_version: 2.0.0
---

# Run 392 - recovery log

## Trigger

Pre-flight repository hygiene failed before the normal relocation-vault iteration could start. `git fetch origin && git status --short --branch` reported a dirty working tree on `main...origin/main`.

## Observed dirty files

- Modified: `CHANGELOG.md`
- Modified: `INDEX.md`
- Modified: `dimensions/final-synthesis-readiness-checklist.md`
- Modified: `dimensions/handoff-maintenance-check.md`
- Modified: `state.json`
- Untracked: `runs/run-391-scheduled-no-trigger-recheck.md`

## Action taken

- Entered recovery mode per vault protocol.
- Did not apply proposals, modify country profiles, edit sources, edit claims, edit verification statuses, update `state.json`, or run a normal research/consolidation unit.
- Wrote only this recovery log for auditability.

## Suggested fix

Inspect the uncommitted run-391 maintenance changes and either complete/commit them if valid or manually reconcile them before the next scheduled iteration. The next iteration should rerun the normal pre-flight checks from a clean working tree.
