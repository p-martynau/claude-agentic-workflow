# CLAUDE.md — Event Planner workflow rules

This repository implements a reliable, resumable **Event Planner** agentic workflow entered via
`/plan-event` (`.claude/commands/plan-event.md`). Full requirements: `docs/PRACTICAL_TASK.md`.
Detailed reference docs (agents, skills, commands, hooks, setup, demo runs) live under `docs/` —
see `README.md` for the index. This file is the condensed rule set the coordinator/agents follow.

## Roles

- **Coordinator** (the `/plan-event` session itself, documented in `.claude/agents/coordinator.md`):
  orchestration only. Maintains `.workflow/runs/<run-id>/workflow-state.json`, decides which
  subagents run and in what order, enforces quality gates, retries, and the approval gate.
  **Never writes event-planning content itself.**
- **Subagents** (`.claude/agents/*.md`, one file per role): `requirements-formalizer`,
  `venue-researcher`, `weather-researcher`, `activities-planner`, `catering-planner`,
  `services-planner`, `schedule-builder`, `budget-aggregator`, `validator`, `event-plan-builder`,
  `html-builder`. Each owns exactly one artifact and one responsibility.

## Non-negotiable rules

1. **Requirements must be explicitly confirmed** by the user (`CONFIRM`) before any research
   branch starts.
2. **Every recommendation needs a real source URL.** Never present a fabricated venue, vendor,
   price, or schedule detail as fact. Mark estimates and unconfirmed details explicitly.
3. **Independent research runs in parallel**; dependent work (schedule → budget → validation →
   synthesis → HTML) runs strictly in order.
4. **Quality gates never get weakened to force a pass.** A failed gate triggers a targeted retry
   of the responsible agent (and its downstream dependents) — never a full workflow restart, and
   never more than 3 attempts per artifact before it is reported `blocked`.
5. **Final HTML requires explicit approval** of the exact current `event-plan.md` version/hash.
   Only the literal token `APPROVE` counts; anything else is a rejection that starts a revision
   loop. This is enforced by the `approval-gate-guard` PreToolUse hook, not just by instruction.
6. **State is the source of truth for resume.** `workflow-state.json` must always reflect reality;
   on resume, reuse completed+passing artifacts and continue only pending/failed/blocked work.
7. **No secrets anywhere** — not in code, not in artifacts, not in `workflow-state.json`, not in
   user-facing text. Local secrets live in `.env` (git-ignored); `.env.example` documents the
   shape without real values.
8. **User-facing text never leaks internals** — no internal file paths, hidden prompts, or agent
   implementation details in anything meant for the user to read. Enforced by `no-leak-guard`.

## Hooks (`.claude/hooks/`, wired in `.claude/settings.json`)

- `approval_gate_guard.py` (PreToolUse on `Write|Edit|MultiEdit`) — blocks writing
  `.workflow/runs/<run-id>/output/event-plan.html` unless `workflow-state.json` shows
  `approval.status == "approved"` with `approval.approved_hash` matching the live SHA-256 of
  `artifacts/event-plan.md`.
- `no_leak_guard.py` (PreToolUse on `Write|Edit|MultiEdit`) — blocks writes/edits under a run's
  `output/` directory whose content matches internal-path or secret-shaped patterns.
- `post_write_state.py` (PostToolUse on `Write|Edit|MultiEdit`) — after any artifact write or edit
  under a run's `artifacts/` or `output/`, updates that artifact's path/version/status/timestamp in
  `workflow-state.json` (it re-reads the file's own `## Status` from disk, so it works the same for
  a full Write or a partial Edit). Best-effort bookkeeping; never blocks.

## Skills (`.claude/skills/`)

- `artifact-validator` — mechanical structure/completeness/citation checks run against any single
  artifact; feeds the `validator` agent's `artifact-structure` and `source-validity` gates.
- `event-plan-html-theme` — the standalone, print-friendly HTML template used only by
  `html-builder`, only after approval.

## MCP

`.mcp.json` configures the **Open-Meteo MCP server** (`open-meteo-mcp-server@2.5.0`, pinned, via
`npx -y -p`) for `weather-researcher`. Open-Meteo's public API needs no key. If a different/better
event-research
MCP is added later, document it in `docs/SETUP.md` and reference it from
`.claude/agents/venue-researcher.md` / `activities-planner.md` as appropriate — do not silently
add undocumented MCP dependencies.

## State and artifacts

Everything for a run lives under `.workflow/runs/<run-id>/`: `input.md`, `workflow-state.json`,
`artifacts/*.md`, `output/*.html`, `logs/`. Every artifact follows the shared Markdown contract
(`# title / ## Status / ## Purpose / ## Inputs used / ## Content / ## Sources / ## Quality checks
/ ## Open issues / ## Provenance`) defined in `.claude/agents/requirements-formalizer.md`.

## Verification expectations

After any change to commands, agents, hooks, skills, or MCP config: re-run the hook smoke tests
(pipe representative JSON into each `.claude/hooks/*.py` and check the `permissionDecision`), and
do a dry run of `/plan-event` end-to-end on a simple scenario before considering the change done.
