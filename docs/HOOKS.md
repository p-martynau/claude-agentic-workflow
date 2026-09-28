# Hooks

Both required hook categories are implemented under [`.claude/hooks/`](../.claude/hooks/) and
wired in [`.claude/settings.json`](../.claude/settings.json), matched on `Write|Edit|MultiEdit` so
both full writes and partial edits are covered. All three fail safe: on any error or missing
evidence, they block rather than allow.

## PreToolUse

### `approval-gate-guard` — [`approval_gate_guard.py`](../.claude/hooks/approval_gate_guard.py)

Blocks writing `.workflow/runs/<run-id>/output/event-plan.html` unless:

1. `workflow-state.json` has `approval.status == "approved"`, and
2. `approval.approved_hash` equals the **live** SHA-256 of the current `artifacts/event-plan.md`
   (recomputed on every check, not cached) — so an edit made after approval, even a small one,
   re-blocks the write until re-approved.

Any missing file, unparsable JSON, or mismatch returns
`{"permissionDecision": "deny", "permissionDecisionReason": "..."}` explaining exactly why.

### `no-leak-guard` — [`no_leak_guard.py`](../.claude/hooks/no_leak_guard.py)

Blocks writes/edits under a run's `output/` directory (the user-facing deliverables) whose content
matches internal-path patterns (`workflow-state.json`, `.workflow/runs/`, `.claude/agents/`,
`.claude/hooks/`) or secret-shaped strings (`sk-...`, `AKIA...`, `api_key: ...`, `secret: ...`).
Intermediate artifacts under `artifacts/` are internal working documents and are not restricted.

## PostToolUse

### `post-write-state` — [`post_write_state.py`](../.claude/hooks/post_write_state.py)

After any write/edit under a run's `artifacts/` or `output/`, re-reads that file's own
`## Status` line from disk and updates `workflow-state.json.artifacts[<file>]` with its path,
bumped version, status, and an ISO 8601 timestamp. Best-effort bookkeeping only — a PostToolUse
hook cannot block, and a failure here is never reported as a workflow failure. The coordinator
still owns `execution_plan`, `quality_gates`, and `approval` itself.

## Verified, not just configured

All three hooks were smoke-tested directly (piping representative JSON into each script) and
confirmed live during the real demonstration runs: every `output/event-plan.html` write in
[`RUNS.md`](RUNS.md) went through `approval-gate-guard` and `no-leak-guard` for real, and the
approved hash recorded in each run's `workflow-state.json` was independently re-verified against
the live file hash (see the smoke-test commands in [`SETUP.md`](SETUP.md#verification)).
