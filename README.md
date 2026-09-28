# Claude Agentic Workflow

> A reliable, resumable Event Planner workflow for Claude Code — built as a learning/practical
> task for Claude Code multi-agent workflows.

This is an **educational project**. It implements the practical assignment described in
[`docs/PRACTICAL_TASK.md`](docs/PRACTICAL_TASK.md) — a self-contained brief that replaces the
original PDF task and is the authoritative source for every requirement below. The chosen domain
is **Event Planner**: turn a natural-language event request into a researched, validated,
human-approved event plan.

**Status: implemented and verified**, with known limitations tracked honestly — see
[`docs/STATUS.md`](docs/STATUS.md) for the full Definition-of-Done checklist mapped to evidence
(including two real tamper tests of the approval hook and a genuine MCP tool call verified live in
this session).

## Quick start

```bash
git clone <this-repo>
cd claude-agentic-workflow
claude    # start Claude Code in the repo root
```

Claude Code loads `.mcp.json` and `.claude/settings.json` automatically; approve the `open-meteo`
MCP server the first time it's requested. No API keys are needed (see
[`docs/SETUP.md`](docs/SETUP.md)).

```text
/plan-event Plan a one-day indoor family birthday event for 20 guests in London.
Fixed budget of £1,200 GBP, include children-friendly activities and catering,
and recommend a venue near public transport.
```

The coordinator asks any missing clarification questions, waits for the literal reply `CONFIRM`,
runs the applicable research agents in parallel, builds the schedule and budget, validates
everything (retrying only the responsible agent on a failed gate, up to 3 attempts), and shows you
the plan's version and hash — reply with the exact token `APPROVE` to generate the final HTML, or
anything else to send it back for revision.

To resume an interrupted run, just reference its run ID (e.g. "resume run-003") — the coordinator
reloads `.workflow/runs/<run-id>/workflow-state.json` and continues only the unfinished work.

## Documentation

| Topic | Where |
|---|---|
| The original assignment / Definition of Done | [`docs/PRACTICAL_TASK.md`](docs/PRACTICAL_TASK.md) |
| Definition-of-Done checklist mapped to evidence, known limitations | [`docs/STATUS.md`](docs/STATUS.md) |
| Coordinator + all 11 subagents, quality gates | [`docs/AGENTS.md`](docs/AGENTS.md) |
| The `/plan-event` command and its full flow | [`docs/COMMANDS.md`](docs/COMMANDS.md) |
| The two reusable skills | [`docs/SKILLS.md`](docs/SKILLS.md) |
| The `PreToolUse`/`PostToolUse` hooks | [`docs/HOOKS.md`](docs/HOOKS.md) |
| Prerequisites, MCP config, repo layout, verification | [`docs/SETUP.md`](docs/SETUP.md) |
| The three demonstration runs — requested vs. delivered | [`docs/RUNS.md`](docs/RUNS.md) |
| Workflow rules for the coordinator/agents | [`CLAUDE.md`](CLAUDE.md) |

## Security

- No credentials are required by default (Open-Meteo's API is keyless); local secrets, if ever
  needed, go in an untracked `.env` (see [`.env.example`](.env.example)).
- No secrets are written into workflow state, logs, artifacts, or user-facing output — enforced by
  the `no-leak-guard` hook ([`docs/HOOKS.md`](docs/HOOKS.md)).
- All demonstration runs use synthetic requester/personal data; only sourced venues/vendors/prices
  are real.
