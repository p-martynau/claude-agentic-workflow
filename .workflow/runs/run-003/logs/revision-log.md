# Revision log — run-003 (post-rejection targeted retry)

**Rejection received 2026-09-28T14:45:00Z** for `event-plan.md` v1 (hash
`bc6775db3ef556e8503fb9c58cdd7cbc7b9d6ee34bcfa75abd095290e6f7ea15`) — see
`logs/approval-prompt-v1.md` for the full feedback.

Feedback routed to the **responsible agent**, `weather-researcher` (owner of the contingency
content that was called out as vague), plus `schedule-builder` as the one genuinely-affected
downstream artifact (it references the same go/no-go moment and should name the same
decision-maker so the plan stays internally consistent). No other artifact was touched — `venues.md`,
`activities.md`, `catering.md`, `services.md`, and `budget.md` were not re-run because the feedback
did not concern them and their inputs did not change.

`execution_plan_version` incremented from 1 to 2 to reflect this targeted re-run.

## 2026-09-28T14:50:00Z — `weather-researcher` re-invoked
Revises `artifacts/weather.md` to v2: names a specific on-the-day decision-maker and a specific
guest-facing announcement, in addition to the existing forecast-outlook and trigger-threshold
content from v1 (which is kept, not replaced).

## 2026-09-28T14:56:00Z — `schedule-builder` re-invoked
Revises `artifacts/schedule.md` to v2: the 11:00 go/no-go line now names the same decision-maker
introduced in `weather.md` v2, so the two artifacts agree.

## 2026-09-28T15:00:00Z — `validator` re-invoked
Re-runs all 14 gates against the updated artifacts. Result: all gates PASS (see
`artifacts/validation-report.md`, now version 2).

## 2026-09-28T15:05:00Z — `event-plan-builder` re-invoked
Produces `event-plan.md` v2 with a new SHA-256 hash. See `logs/approval-prompt-v2.md`.

---

## Post-approval compliance correction (v2 → v3)

**Flagged 2026-09-28T15:18:00Z** by an external review of this repository: `weather.md` v1/v2 had
sourced its data via `WebFetch` against the public Open-Meteo HTTP API instead of literally calling
the configured Open-Meteo MCP server, so the brief's requirement that the MCP be **actually used**
in a demonstration run (`docs/PRACTICAL_TASK.md#7-external-research-and-mcp`) was not met by this
run, even though `.mcp.json` was correctly configured. See `logs/mcp-note.md` for the full history.

This is a compliance correction, not a rejection-driven revision — no user feedback was involved,
and the substantive conclusion (mild weather, a real chance of rain, the same contingency plan)
does not change. `execution_plan_version` incremented from 2 to 3 to reflect this re-run.

## 2026-09-28T15:20:00Z — `weather-researcher` re-invoked
By this point the session's Open-Meteo MCP server was attached (confirmed live via
`mcp__open-meteo__geocoding`). Revises `artifacts/weather.md` to v3: replaces the v1/v2
WebFetch-sourced single-year (2020) historical sample with six real `mcp__open-meteo__weather_archive`
tool calls (2019–2024, 30 day-samples). The decision-maker/communication content added in v2 is
unchanged.

## 2026-09-28T15:30:00Z — `validator` re-invoked
Re-runs all 14 gates against `weather.md` v3. Result: all gates PASS (see
`artifacts/validation-report.md`, now version 3) — `weather-readiness` and `source-validity` both
note the switch to real MCP tool calls.

## 2026-09-28T15:35:00Z — `event-plan-builder` re-invoked
Produces `event-plan.md` v3 with a new SHA-256 hash, and corrects the "Inputs used" section to
list each upstream artifact's actual current version (it had previously said "all v1", which was
already inaccurate by v2 since `weather.md`/`schedule.md` were v2 — fixed here for v3). See
`logs/approval-prompt-v3.md`.

## 2026-09-28T15:43:00Z — `html-builder` re-invoked
`output/event-plan.html` rewritten from the v3 (approved) plan. The `approval-gate-guard` hook
independently re-verified that the live SHA-256 of `artifacts/event-plan.md` matched
`workflow-state.json.approval.approved_hash` before allowing this write.
