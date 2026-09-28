# Setup, MCP, and verification

## Prerequisites

- **Claude Code**, run from the repository root (so `.claude/`, `.mcp.json`, and `.workflow/` are
  picked up automatically).
- **Node.js with `npx`** on `PATH` — launches the Open-Meteo MCP server on demand; nothing needs
  pre-installing beyond Node.js.
- **Web search**, provided by Claude Code's built-in `WebSearch`/`WebFetch` tools — no extra setup,
  but the environment must allow outbound network access.
- **No API keys are required.** Open-Meteo's public forecast API is keyless. If you later add an
  MCP or search provider that needs one, put it in a local `.env` (see
  [`.env.example`](../.env.example)) and never commit it.

## MCP servers

| Server | Package (pinned) | Purpose | Credentials |
|---|---|---|---|
| `open-meteo` | `open-meteo-mcp-server@2.5.0` (via `npx -y -p`, see [`.mcp.json`](../.mcp.json)) | Real weather forecast/outlook for outdoor or weather-sensitive events, used by `weather-researcher` | None |

The version is pinned (not a floating tag) so a clean checkout always gets the same server build.
Claude Code loads `.mcp.json` at session start and prompts to approve the `open-meteo` server the
first time — approve it so `weather-researcher` can call its `mcp__open-meteo__*` tools directly
(confirmed working: a live `mcp__open-meteo__geocoding` call in this repo's own session resolved
"Bristol" to real coordinates). If the MCP genuinely isn't attached in a given session (e.g. it was
added mid-session, after startup), `weather-researcher` falls back to calling the public Open-Meteo
HTTP API via `WebFetch`, which returns the same data, but the MCP tool path should always be tried
and used first, since that's what the brief requires to be demonstrated — see
`.workflow/runs/run-003/logs/mcp-note.md` for a real example of both paths: a WebFetch fallback in
`weather.md` v1/v2, corrected to genuine `mcp__open-meteo__*` tool calls in v3 once the server was
attached.

If you add a second MCP (a maps or richer event-search server), add it to `.mcp.json` with a
pinned version, document it in this table, and reference it from the relevant file in
[`AGENTS.md`](AGENTS.md).

## Repository layout

```text
.
├── CLAUDE.md                     # workflow rules for the coordinator/agents
├── README.md
├── docs/                         # this folder — detailed reference docs
├── .mcp.json                     # Open-Meteo MCP server config (no credentials)
├── .env.example                  # shape for any future secret; no real values
├── .claude/
│   ├── settings.json              # wires PreToolUse/PostToolUse hooks
│   ├── commands/plan-event.md     # /plan-event entry point
│   ├── agents/                    # coordinator + 11 subagents
│   ├── skills/                    # artifact-validator, event-plan-html-theme
│   └── hooks/                     # approval_gate_guard, no_leak_guard, post_write_state
└── .workflow/runs/
    ├── run-001/   # family birthday — parallel independent agents
    ├── run-002/   # corporate workshop — quality-gate failure + targeted retry
    └── run-003/   # outdoor celebration — real weather, rejection + revision, resume
```

## Verification

After any change to `.claude/commands/`, `.claude/agents/`, `.claude/hooks/`, `.claude/skills/`, or
`.mcp.json`, re-run the hook smoke tests and a full dry run:

```bash
# Hook smoke tests — each prints a permissionDecision (allow/deny) as JSON
echo '{"tool_input":{"file_path":"/abs/path/.workflow/runs/run-001/output/event-plan.html","content":"<html></html>"},"cwd":"/abs/path"}' \
  | python3 .claude/hooks/approval_gate_guard.py

echo '{"tool_input":{"file_path":"/abs/path/.workflow/runs/run-001/output/event-plan.html","content":"mentions workflow-state.json"},"cwd":"/abs/path"}' \
  | python3 .claude/hooks/no_leak_guard.py
```

Then run `/plan-event` on a simple scenario end-to-end and confirm: clarification → `CONFIRM` gate,
parallel dispatch of research agents, a validator pass/fail report, the approval prompt showing
version + hash, and that `output/event-plan.html` only appears after the literal `APPROVE`.

Check for accidental secrets in anything tracked or generated:

```bash
grep -riE "api[_-]?key|secret|token|password" .workflow .claude
```

(In this repository, the only matches are the literal approval token `APPROVE`/`CONFIRM` in
prompts/logs and the hooks' own pattern definitions and comments — no real credentials.)
