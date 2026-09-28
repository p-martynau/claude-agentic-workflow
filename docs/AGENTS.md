# Agents

The workflow uses one coordinator and eleven subagents, defined under
[`.claude/agents/`](../.claude/agents/). Each subagent has exactly one responsibility and owns
exactly one artifact under `.workflow/runs/<run-id>/artifacts/`. The coordinator's job is
orchestration only — it never writes event-planning content itself.

Every artifact follows the same Markdown contract: `# title / ## Status / ## Purpose /
## Inputs used / ## Content / ## Sources / ## Quality checks / ## Open issues / ## Provenance`.

| Agent | File | Responsibility | Owned artifact | Runs after |
|---|---|---|---|---|
| **Coordinator** | [`coordinator.md`](../.claude/agents/coordinator.md) | Orchestration, `workflow-state.json` schema, plan/retry/approval bookkeeping. Never authors content. | `workflow-state.json` | — |
| `requirements-formalizer` | [`requirements-formalizer.md`](../.claude/agents/requirements-formalizer.md) | Turns the raw request + clarification answers into confirmed requirements. Only agent allowed to ask the user questions. | `requirements.md` | user request |
| `venue-researcher` | [`venue-researcher.md`](../.claude/agents/venue-researcher.md) | Finds real venues matching location/capacity/budget/accessibility/parking. | `venues.md` | requirements confirmed |
| `weather-researcher` | [`weather-researcher.md`](../.claude/agents/weather-researcher.md) | Real forecast/outlook via the Open-Meteo MCP (or WebSearch fallback) plus a concrete contingency. Only run for outdoor/weather-sensitive events. | `weather.md` | requirements confirmed |
| `activities-planner` | [`activities-planner.md`](../.claude/agents/activities-planner.md) | Sources activities/entertainment matched to guest groups and preferences. | `activities.md` | requirements confirmed |
| `catering-planner` | [`catering-planner.md`](../.claude/agents/catering-planner.md) | Menus/caterers matching guest count, diets, and allergies. | `catering.md` | requirements confirmed |
| `services-planner` | [`services-planner.md`](../.claude/agents/services-planner.md) | Vendors/services (AV, music, decor, security, transport) actually needed. | `services.md` | requirements confirmed |
| `schedule-builder` | [`schedule-builder.md`](../.claude/agents/schedule-builder.md) | Assembles a conflict-free timeline from every research artifact. | `schedule.md` | all selected research branches READY |
| `budget-aggregator` | [`budget-aggregator.md`](../.claude/agents/budget-aggregator.md) | Aggregates costs, currency, and contingency into one transparent total. | `budget.md` | `schedule.md` READY |
| `validator` | [`validator.md`](../.claude/agents/validator.md) | Applies every named quality gate (see [`HOOKS.md`](HOOKS.md) for the enforcement side); reports only, never edits. | `validation-report.md` | `budget.md` READY |
| `event-plan-builder` | [`event-plan-builder.md`](../.claude/agents/event-plan-builder.md) | Synthesizes every validated artifact into one plan; computes the version hash used for approval. | `event-plan.md` | validation PASS |
| `html-builder` | [`html-builder.md`](../.claude/agents/html-builder.md) | Renders the **approved** plan as standalone HTML via the `event-plan-html-theme` skill. | `output/event-plan.html` | explicit `APPROVE` |

## Dynamic selection and parallelism

The coordinator always runs `venue-researcher`, `activities-planner`, `catering-planner`, and
`services-planner`; it adds `weather-researcher` only for outdoor/weather-sensitive events. All
applicable research branches are dispatched together (one message, multiple Task calls) so they
run in parallel; `schedule-builder` → `budget-aggregator` → `validator` → `event-plan-builder` →
`html-builder` run strictly in sequence. See [`COMMANDS.md`](COMMANDS.md) for the full orchestration
flow and [`RUNS.md`](RUNS.md) for real examples of both parallel dispatch and targeted retry.

## Quality gates (owned by `validator`)

`requirements-completeness`, `artifact-structure`, `budget-limit`, `schedule-feasibility`,
`no-overlapping-activities`, `venue-fit`, `catering-fit`, `services-fit`,
`travel-and-transitions`, `weather-readiness`, `no-duplicate-recommendations`,
`meaningful-program`, `source-validity`, `final-consistency`. A failed gate is mapped to the one
responsible agent, which is retried (with any genuinely-downstream agent) up to 3 times before the
affected work is reported `blocked` — see [`docs/PRACTICAL_TASK.md#8-quality-gates`](PRACTICAL_TASK.md#8-quality-gates)
for the full rule and [`RUNS.md`](RUNS.md) for a real failure + retry.
