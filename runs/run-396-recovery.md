---
run_id: 396
date: 2026-07-20T05:56:08Z
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
  - runs/run-396-recovery.md
proposals_created: []
completed_at: 2026-07-20T05:56:08Z
status: completed
schema_version: 2.0.0
---

# Run 396 - recovery log

## Trigger

Pre-flight repository hygiene failed before a normal relocation-vault iteration could start. `git fetch origin` succeeded, but `git status --short --branch` reported a dirty working tree on `main` before any normal work began.

## Observed dirty files

- Modified: `CHANGELOG.md`
- Modified: `INDEX.md`
- Modified: `dimensions/final-synthesis-readiness-checklist.md`
- Modified: `dimensions/handoff-maintenance-check.md`
- Modified: `state.json`
- Untracked: `runs/run-391-scheduled-no-trigger-recheck.md`
- Untracked: `runs/run-396-recovery.md` (this recovery log, created after the failed pre-flight check)

## Action taken

- Entered recovery mode per vault protocol.
- Did not pull, apply proposals, modify country profiles, edit sources, edit claims, edit verification statuses, update `state.json`, or run a normal research/consolidation unit.
- Wrote only this recovery log for auditability.

## Suggested fix

The uncommitted run-391 maintenance changes are still present after previous recovery logs. Inspect and either complete/commit them if valid or manually reconcile them before the next scheduled iteration. The next normal iteration should rerun pre-flight checks from a clean working tree.
