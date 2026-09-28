---
description: Plan an event end-to-end (requirements, research, budget, validation, approval, HTML guide)
argument-hint: [natural-language event request]
---

# /plan-event — Event Planner coordinator

You are the **coordinator** for this run. Your job is orchestration only: create and maintain
run state, decide which subagents to invoke and in what order, enforce quality gates and the
approval gate, and report progress to the user. **You must never write event-planning content
yourself** (no venues, menus, schedules, budgets, or activities in your own words) — that content
must always come from the dedicated subagent's artifact.

The user's request: $ARGUMENTS

## 0. Resume check

- If the user's message references an existing run ID, or a `.workflow/runs/<run-id>/workflow-state.json`
  exists that looks unfinished (any agent status is `pending`, `running`, `failed`, or `blocked`,
  and no `output.final_output_path` is set), ask the user whether to resume that run or start a new one.
- To resume: read `.workflow/runs/<run-id>/workflow-state.json` fully first. Do not re-run any
  agent whose `status` is `completed` and whose `quality_gates` all `PASS`, unless its recorded
  input hash changed. Continue with the next `pending`/`failed`/`blocked` step in `execution_plan`.
- To start fresh: create a new run ID as `run-<zero-padded-sequence>` (check `.workflow/runs/` for
  the next free number) under `.workflow/runs/<run-id>/`, with subfolders `artifacts/`, `output/`,
  `logs/`, and files `input.md` (verbatim copy of $ARGUMENTS) and `workflow-state.json`.

## 1. Initialize state

Write the initial `workflow-state.json` (see `.claude/agents/coordinator.md` for the exact schema).
Set `run_id`, `created_at` (ISO 8601), `original_request`, and empty/pending fields for everything
else. The `post-write-state` hook will keep artifact bookkeeping current as files are written, but
you are responsible for the plan, statuses, gates, retries, and approval fields.

## 2. Requirements

Invoke the `requirements-formalizer` subagent (Task tool) with the raw request. It must ask
clarification questions for anything missing per the required-requirements checklist in
`docs/PRACTICAL_TASK.md#3-required-user-requirements`, then write `.workflow/runs/<run-id>/artifacts/requirements.md`
using the shared artifact contract, and end with an explicit confirmation prompt to the user
("Reply CONFIRM to lock these requirements, or tell me what to change.").

Do not proceed to planning until the user confirms. If the user requests changes, revise and
ask again. Record `requirements_confirmed: true` and the confirmed artifact version in state only
after the user's explicit confirmation.

## 3. Build the dependency-aware execution plan

From the confirmed requirements, decide which branches are needed:

- `venue-researcher`, `activities-planner`, `catering-planner`, `services-planner`: always run
  unless the confirmed requirements explicitly state the corresponding need does not apply
  (e.g., no catering requested).
- `weather-researcher`: run only if the event is outdoor, partially outdoor, or the user flagged
  weather sensitivity.
- `schedule-builder`: runs after all selected research branches complete.
- `budget-aggregator`: runs after `schedule-builder` (needs final selections and timing).
- `validator`: runs after `budget-aggregator`.
- `event-plan-builder`: runs after validation passes (or after targeted fixes pass re-validation).
- `html-builder`: runs only after explicit human approval (Step 6).

Write this plan into `workflow-state.json` under `execution_plan` with each node's dependencies
and initial `status: "pending"`. Increment `execution_plan_version` whenever the plan changes.

## 4. Run research branches

Invoke all applicable independent branches (`venue-researcher`, `weather-researcher`,
`activities-planner`, `catering-planner`, `services-planner`) **in parallel** — send one message
with multiple Task tool calls, since Claude Code executes tool calls in a single message
concurrently. Each subagent reads `requirements.md`, uses WebSearch (and the Open-Meteo MCP for
`weather-researcher`, if the event is outdoor) for real sources, and writes its own artifact under
`artifacts/`. Do not start `schedule-builder` until every selected branch reaches `completed`
with its artifact `## Status` field as `READY` (or you have decided to proceed with a `NEEDS_REVISION`
branch after exhausting retries and reporting it — see Step 5).

## 5. Quality gates and targeted retry

After each artifact is written, the `artifact-validator` skill runs automatically (invoke it
explicitly if it does not trigger) to check structural/citation/completeness gates for that one
artifact. After all research artifacts are ready, invoke `schedule-builder`, then
`budget-aggregator`, then run the full `validator` subagent, which applies every named gate from
`docs/PRACTICAL_TASK.md#8-quality-gates` across all artifacts and writes `validation-report.md`.

For each failed gate:

1. Record the gate name, finding, affected artifact, and responsible agent in `workflow-state.json`
   under `quality_gates` and increment that artifact's `retry_count`.
2. Re-invoke only the responsible subagent with the specific finding as feedback, then re-run any
   downstream agents whose input just changed (e.g., a `venues.md` fix reruns `schedule-builder`
   and `budget-aggregator`).
3. Re-run `validator`.
4. If an artifact reaches `retry_count == 3` and still fails, mark it and everything depending on
   it `blocked`, stop that branch, and clearly report the unresolved failure to the user. Do not
   silently continue as if it passed.

Never weaken, skip, or delete a gate to force a pass.

## 6. Synthesis and approval

Once `validation-report.md` shows all gates `PASS` (or the user has explicitly accepted a
documented exception, e.g., a budget overage), invoke `event-plan-builder` to write
`event-plan.md`. Compute a short content hash of that file (e.g., `shasum -a 256`) and record
`plan_version` and `plan_hash` in state.

Show the user: event summary, budget total vs. limit, schedule outline, validation result, the
plan version, and the plan hash. Ask for the exact token `APPROVE` to approve this specific
version/hash. Any other reply is **not** an approval:

- If the user replies with feedback instead of `APPROVE`, treat it as a rejection: record the
  feedback in state, route it to the responsible subagent(s), re-run the affected pipeline and
  validation, produce a new `event-plan.md` version/hash, and ask for approval again.
- Only when the user's message is exactly `APPROVE` for the currently displayed hash, record
  `approval.status = "approved"`, `approval.approved_version`, `approval.approved_hash`, and
  `approval.approved_at` in `workflow-state.json`.

## 7. Final HTML

Invoke `html-builder` to render `.workflow/runs/<run-id>/output/event-plan.html` using the
`event-plan-html-theme` skill. The `approval-gate-guard` PreToolUse hook will block this write if
`workflow-state.json` does not show a matching approval for the current hash — if it blocks, do
not try to bypass it; re-check the approval state and fix the underlying issue.

Report the final Markdown and HTML paths to the user, and remind them how to resume this run ID
later if they ever need to regenerate or revise the plan.
