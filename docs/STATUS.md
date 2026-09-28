# Definition of Done — status

This tracks the checklist from
[`docs/PRACTICAL_TASK.md#16-definition-of-done`](PRACTICAL_TASK.md#16-definition-of-done) against
concrete evidence in this repository. The brief itself (`PRACTICAL_TASK.md`) is left unmodified as
the authoritative assignment text; this file is the implementation's own progress record.

- [x] `CLAUDE.md` documents the workflow and execution rules. → [`../CLAUDE.md`](../CLAUDE.md)
- [x] At least one coordinator and five or more subagents are implemented and used. → 1
  coordinator + 11 subagents, [`AGENTS.md`](AGENTS.md); all 11 are exercised across the three runs
  ([`RUNS.md`](RUNS.md)).
- [x] At least two reusable skills are implemented and used. → `artifact-validator`,
  `event-plan-html-theme`, [`SKILLS.md`](SKILLS.md); invoked in every run (validation reports, HTML
  output).
- [x] Both `PreToolUse` and `PostToolUse` hooks are implemented and used. →
  [`HOOKS.md`](HOOKS.md); live-verified in every run — every `output/event-plan.html` write went
  through `approval-gate-guard`/`no-leak-guard`, and a real tamper test (modify `event-plan.md`,
  re-check the hook) confirmed it blocks a hash mismatch, not just a hand-wavy "should block."
- [x] At least one community or custom MCP server is integrated and used. → Open-Meteo MCP,
  pinned `open-meteo-mcp-server@2.5.0` ([`.mcp.json`](../.mcp.json)). Genuinely called via
  `mcp__open-meteo__geocoding` and `mcp__open-meteo__weather_archive` in `run-003`'s `weather.md`
  v3 — see [`RUNS.md#run-003`](RUNS.md#run-003-outdoor-community-celebration-bristol) and
  `.workflow/runs/run-003/logs/mcp-note.md` for the full history (v1/v2 used a `WebFetch` fallback
  before the MCP was attached; v3 corrected this to real MCP tool calls).
- [x] External web search is used and its sources are recorded. → every `venues.md`,
  `activities.md`, `catering.md`, `services.md` across all three runs cites real, retrieved URLs.
- [x] Artifacts follow a consistent, human-readable Markdown structure. → shared contract defined
  in [`AGENTS.md`](AGENTS.md); every artifact in all three runs follows it.
- [x] Named quality gates are implemented. → 14 gates, [`AGENTS.md`](AGENTS.md#quality-gates-owned-by-validator).
- [x] Quality-gate failures trigger targeted retries with a maximum of three attempts. → real
  example in `run-002` (`services-fit` failure → targeted retry of `services-planner` only,
  `retry_count: 1`) — [`RUNS.md#run-002`](RUNS.md#run-002-corporate-workshop-manchester).
- [x] Dependent artifacts are regenerated when an upstream artifact changes. → `run-002`'s retry
  also re-ran `budget-aggregator` (input changed) but not `schedule-builder` (input didn't);
  `run-003`'s v3 MCP correction re-ran `validator` and `event-plan-builder` but not the unaffected
  domain artifacts.
- [x] Unresolved failures stop dependent work and are reported clearly. → documented behavior in
  [`AGENTS.md`](AGENTS.md) and `.claude/agents/coordinator.md`'s retry-limit rule; no run hit the
  3-attempt ceiling (all resolved within one retry), so this is implemented and specified but not
  yet exercised to its limit by a demo run — a known limitation, see below.
- [x] Workflow state survives interruptions and supports resume. → real example in `run-003`:
  frozen after 5 parallel research agents, resumed strictly from `schedule-builder` onward —
  [`RUNS.md#run-003`](RUNS.md#run-003-outdoor-community-celebration-bristol),
  `.workflow/runs/run-003/logs/interruption-note.md` / `resume-log.md`.
- [x] Final output is blocked until deterministic human approval is recorded. → enforced by
  `approval-gate-guard` ([`HOOKS.md`](HOOKS.md)), independently tamper-tested (see above).
- [x] Rejected output is revised and resubmitted for approval. → real example in `run-003`: v1
  rejected with specific feedback, v2 revised and approved —
  [`RUNS.md#run-003`](RUNS.md#run-003-outdoor-community-celebration-bristol).
- [x] Final output is delivered as readable Markdown and standalone HTML. → every run has both
  `artifacts/event-plan.md` and `output/event-plan.html`.
- [x] Three different demonstration runs, including inputs, artifacts, and state, are committed. →
  runs exist under `.workflow/runs/run-001` … `run-003` ([`RUNS.md`](RUNS.md)). **"Committed"
  specifically (a git commit, not just tracked/staged files) depends on the user's explicit
  go-ahead** — this repository's working agreement is to only commit when asked; see the note
  below.
- [x] `README.md` contains setup, run, resume, verification, MCP, and environment instructions. →
  [`../README.md`](../README.md) plus [`SETUP.md`](SETUP.md), [`COMMANDS.md`](COMMANDS.md).
- [x] No credentials, API keys, or secrets are committed. → verified with
  `grep -riE "api[_-]?key|secret|token|password" .workflow .claude` — only the literal approval
  tokens (`APPROVE`/`CONFIRM`) and the hooks' own pattern definitions match, no real credentials.
- [x] A clean checkout can be set up and run using the documented instructions. → no API keys
  needed (Open-Meteo is keyless); prerequisites are Claude Code + Node/`npx` + web search, all
  documented in [`SETUP.md`](SETUP.md).

## Known limitations

- The 3-retry-then-`blocked` ceiling is implemented and specified (see
  `.claude/agents/coordinator.md`) but not exercised end-to-end by a demo run — every gate failure
  in the three runs resolved on the first retry, so no run shows an artifact actually reaching
  `blocked`.
- A full interactive `/plan-event` session (live user answering clarification questions in real
  time, live rejecting/approving through actual back-and-forth) has not been independently run
  outside of this authoring process — the three demonstration runs were authored by an agent
  faithfully playing every role end-to-end, including real `WebSearch`/`WebFetch`/MCP calls for
  every cited fact, rather than a human operator typing into a live `claude` session turn by turn.
  The command, agents, hooks, and skills are exactly what a live session would use — see
  [`COMMANDS.md`](COMMANDS.md) — but this distinction is worth being explicit about.
- **Committing the three runs to git** is a deliberate separate step, not yet taken as of this
  writing, in line with only committing when the user asks. Run `git status` to see everything
  currently staged and ready.
