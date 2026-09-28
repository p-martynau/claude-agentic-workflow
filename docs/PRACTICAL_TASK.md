# Claude Learning Practical Task

## Self-contained implementation brief for Claude Code

> This document replaces the original PDF assignment. Treat it as the source of truth for implementing the project. Read it completely before changing the repository.

## 0. How to use this brief

Attach this file to a Claude Code session or keep it at `docs/PRACTICAL_TASK.md` in the repository. Use the following first message:

> Read `docs/PRACTICAL_TASK.md` completely and treat it as the authoritative implementation brief. Inspect the repository and available Claude Code capabilities, then implement the workflow described here. Do not ask me to repeat the assignment. Ask questions only when a decision or secret is genuinely required and cannot be inferred safely. Preserve existing work, run verification after each phase, and report the changed files, verification results, known limitations, and run/resume instructions when finished.

The document is intentionally self-contained: the original PDF is not required for implementation.

## 1. Mission

Build a reliable, model-driven agentic workflow with Claude Code. The workflow must accept a natural-language event request, gather and confirm missing requirements, create an execution plan, dynamically select the required subagents, research external sources, validate intermediate artifacts, request explicit human approval, and produce a clear final event plan.

The workflow must be usable from a clean repository checkout and must support resuming an interrupted run without repeating completed work unnecessarily.

The coordinator is responsible for orchestration only. It must not write the event-planning content itself.

## 2. Fixed project decisions

The source assignment's **Domain** section offers three possible domains:

- Event Planner;
- Personalized Learning Assistant;
- Fitness Program Builder.

This implementation brief selects **Event Planner**. Use these decisions unless the user explicitly changes them:

- **Domain:** Event Planner.
- **Entry point:** a custom Claude Code slash command named `/plan-event`.
- **Primary result:** a human-readable event plan in Markdown and a standalone HTML guide.
- **Internal artifacts:** human-readable Markdown files.
- **State:** a persisted `workflow-state.json` for every run.
- **Default language:** the language used by the requester, unless the requester specifies another language.
- **Out of scope:** Travel Planner. It is only an example in the source assignment and must not be copied as the project domain.

The workflow should plan an event based on its occasion, budget, location, guest profile, schedule, preferences, constraints, and required services.

## 3. Required user requirements

Before planning begins, the workflow must collect and explicitly confirm all information needed to create a useful event plan. At minimum, capture:

- event occasion, purpose, and desired atmosphere;
- event date, time, timezone, duration, and date flexibility;
- location, preferred area, venue type, indoor/outdoor needs, and acceptable travel radius;
- expected guest count and relevant guest groups, such as children, older adults, or VIPs;
- budget, currency, and spending priorities;
- event style, theme, formality, and must-have elements;
- food, catering, dietary restrictions, allergies, and beverage preferences;
- required services and vendors, such as catering, decoration, music, photography, security, or equipment rental;
- activity and program preferences, including activities to include or exclude;
- accessibility, parking, transport, scheduling, and technology constraints;
- weather contingency requirements for outdoor or weather-sensitive events;
- preferred source types and the desired final output format.

If information is missing or ambiguous, the requirements-formalizer must ask focused clarification questions. Do not silently invent important constraints. The workflow may proceed only after the user confirms the formalized requirements.

## 4. Target architecture

Use a hub-and-spoke architecture:

```text
User
  |
  v
/plan-event
  |
  v
Coordinator
  |
  +--> Requirements Formalizer
  |
  +--> Venue Researcher --------+
  +--> Weather Researcher ------+---> Schedule and Program Planner
  +--> Activities Planner -------+              |
  +--> Catering Planner ---------+              +--> Budget Aggregator
  +--> Services Planner ---------+                        |
                                                         v
                                                   Validator
                                                         |
                                                         v
                                                Event Plan Builder
                                                         |
                                                Human Approval Loop
                                                         |
                                                         v
                                                   HTML Builder
```

The coordinator must build or update a dependency-aware execution plan from the confirmed requirements and current workflow state. Independent branches must run in parallel where the Claude Code implementation supports it. Dependent branches must run sequentially.

The coordinator must dynamically select applicable agents. For example, the weather branch is required for an outdoor event or when weather affects the plan, while an equipment-rental branch may be selected only when the event requires equipment. Core venue, schedule, budget, and validation work remains common.

## 5. Required subagents and ownership

Implement at least five subagents. The following set is recommended and provides clear artifact ownership:

| Subagent | Single responsibility | Owned artifact | Main dependencies |
|---|---|---|---|
| `requirements-formalizer` | Convert the raw request and clarification answers into confirmed event requirements. | `requirements.md` | User input |
| `venue-researcher` | Find and compare venues that match the location, capacity, budget, accessibility, parking, and event constraints. | `venues.md` | `requirements.md` |
| `weather-researcher` | Research weather outlooks and weather-related risks for outdoor or weather-sensitive events. | `weather.md` | `requirements.md` |
| `activities-planner` | Find or design suitable activities and attractions with duration, cost, suitability, and source links. | `activities.md` | `requirements.md` |
| `catering-planner` | Recommend catering, menus, restaurants, or food services matching guest and dietary requirements. | `catering.md` | `requirements.md`, guest profile |
| `services-planner` | Plan required vendors and services such as music, decoration, photography, equipment, security, or transport. | `services.md` | `requirements.md` |
| `schedule-builder` | Build a feasible event timeline from selected venue, activities, services, and constraints. | `schedule.md` | Domain artifacts |
| `budget-aggregator` | Aggregate estimated costs, currency, assumptions, and contingency into a transparent budget. | `budget.md` | Venues, activities, catering, services, schedule |
| `validator` | Apply named quality gates and report pass/fail findings. It must not rewrite domain content. | `validation-report.md` | All preceding artifacts |
| `event-plan-builder` | Merge validated artifacts into one coherent event plan. | `event-plan.md` | Passed validation |
| `html-builder` | Render the approved event plan as a standalone HTML guide. | `event-plan.html` | Explicit approval |

Every subagent must have one clear responsibility, own its artifact, and return a consistent result. The coordinator must map quality-gate failures to the responsible agent rather than rerunning the entire workflow.

## 6. Artifact contract

All intermediate artifacts must be human-readable Markdown and follow the same structure:

```markdown
# Artifact title

## Status
READY | NEEDS_REVISION | BLOCKED

## Purpose

## Inputs used

## Content

## Sources

## Quality checks

## Open issues

## Provenance
- Run ID:
- Agent:
- Version:
- Created at:
```

Additional rules:

- Every external recommendation must include a real source URL and a short reason for using it.
- Do not present fabricated or unverifiable venues, vendors, prices, schedules, or sources as facts.
- Clearly label estimates, assumptions, availability that has not been confirmed, and information that could not be determined.
- Each recommendation should include the relevant constraints it satisfies and any constraint it does not satisfy.
- Artifacts must contain enough context for a human or a later agent to understand them without reading hidden prompts.
- User-facing messages must not expose internal filenames, private prompts, implementation details, or workflow secrets.

## 7. External research and MCP

The workflow must not rely only on the model's internal knowledge.

It must:

1. use an external web-search capability to discover current venues, vendors, activities, restaurants, and event information;
2. open or verify source pages where possible;
3. integrate and use at least one community or custom MCP server;
4. record source URLs and retrieval dates in research artifacts;
5. document the MCP server, setup, required environment variables, and limitations in `README.md`.

For this domain, use a maintained event-research MCP when appropriate. The default recommendation is an **Open-Meteo MCP server** for weather-sensitive or outdoor events, because the source assignment explicitly identifies Open-Meteo as an example MCP. A maintained search, maps, or fetch MCP may be used instead or in addition when it provides better event-research coverage. The exact server and pinned version must be documented in the repository.

If an MCP requires credentials, read them from environment variables and provide a safe configuration example. Never commit an API key or secret. The final workflow must visibly use the external source and MCP path during at least one sample run; a configuration that is never exercised does not satisfy the requirement.

## 8. Quality gates

The validator must check the following named gates:

- **Requirements completeness:** all required event information is present and confirmed.
- **Artifact structure:** each artifact follows the common Markdown contract.
- **Budget limit:** estimated total cost, including explicitly stated contingency, does not exceed the user's limit unless the user approves an exception.
- **Schedule feasibility:** the event timeline fits the date, time window, venue availability assumptions, setup and cleanup needs, and activity durations.
- **No overlapping activities:** activities, services, meals, and transitions do not conflict without a clear reason.
- **Venue fit:** the venue matches location, guest count, event type, accessibility, parking, indoor/outdoor, and other confirmed preferences.
- **Catering fit:** food and beverage recommendations satisfy guest count, dietary restrictions, allergies, budget, and schedule.
- **Services fit:** every required service is represented and its timing and estimated cost are accounted for.
- **Travel and transitions:** guest, vendor, and activity travel or transition times fit the stated limits.
- **Weather readiness:** outdoor or weather-sensitive events have a weather outlook when available and a practical contingency plan.
- **No duplicate recommendations:** venues, activities, vendors, and services are not unnecessarily repeated.
- **Meaningful program:** every important event segment contains at least one useful or intentional activity.
- **Source validity:** every recommendation links to a real, relevant source page.
- **Final consistency:** the synthesized plan does not contradict validated artifacts.

When a gate fails:

1. record the gate, finding, affected artifact, and responsible agent;
2. increment the retry count for that affected work;
3. rerun only the affected agent and any downstream agents whose inputs changed;
4. rerun validation;
5. stop dependent execution after the third failed attempt and report the unresolved failure clearly.

Do not restart successful independent work. Do not hide a failed gate by weakening or deleting the check.

## 9. Workflow state and resume

Persist state for every run under a predictable repository location, for example:

```text
.workflow/
  runs/
    <run-id>/
      input.md
      workflow-state.json
      artifacts/
      output/
      logs/
```

The persisted state must record at least:

- run ID and creation time;
- original request;
- confirmed event requirements;
- execution-plan version;
- each agent's status: pending, running, completed, failed, blocked, or skipped;
- artifact paths and versions;
- dependency relationships;
- quality-gate results;
- retry counts and failure findings;
- approval status, feedback, and the approved artifact version/hash;
- final output path;
- enough information to resume after a process restart.

On resume, load the state first. Continue from pending or failed work and reuse valid completed artifacts. Do not repeat completed agents unless their inputs or quality-gate status changed.

State files may contain user-provided data, so do not write credentials, API keys, or tokens into them.

## 10. Human approval loop

Final HTML generation requires explicit human approval of the validated synthesized event plan.

The approval mechanism must be deterministic:

- show the user the event summary, budget, schedule, validation result, artifact version, and artifact hash or equivalent identity;
- accept approval only from the expected explicit approval response, such as the exact token `APPROVE` for the displayed version;
- treat any other response as not approved;
- on rejection, capture the feedback, revise only the affected work, rerun the required quality gates, and request approval again;
- do not write the final HTML file before approval is recorded for the current event-plan version.

## 11. Reusable skills

Implement and use at least two reusable skills. Recommended skills:

### `artifact-validator`

Reusable structural, completeness, constraint, and citation checks for every newly created artifact before dependent work proceeds. It should produce findings in a predictable format and identify the responsible artifact or agent.

### `event-plan-html-theme`

Reusable rendering rules and a standalone HTML template for the final guide. It should define readable typography, navigation, event overview, schedule, venue, activities, catering, services, budget, contingency notes, source links, and print-friendly styling without requiring a server at runtime.

Skills must be invoked by the workflow, not merely stored in the repository. Document their input, output, and usage points.

## 12. Required hooks

Implement and use both hook categories:

### `PreToolUse`

- **`approval-gate-guard`:** block the final HTML write unless the persisted state contains a valid approval for the exact current event-plan version/hash.
- **`no-leak-guard`:** prevent internal artifact filenames, private state, secrets, or hidden implementation details from being emitted in user-facing output.

### `PostToolUse`

- **`post-write-state`:** after an artifact is successfully written, update the persisted workflow state with the artifact path, version, status, and timestamp.

Hooks must fail safely. A failed approval check must block the protected action rather than allowing it and reporting the problem afterward.

## 13. Suggested repository deliverables

Use the target Claude Code conventions, while keeping all workflow components version-controlled:

```text
CLAUDE.md
README.md
docs/
  PRACTICAL_TASK.md
.claude/
  commands/
    plan-event.md
  agents/
    coordinator.md
    requirements-formalizer.md
    venue-researcher.md
    weather-researcher.md
    activities-planner.md
    catering-planner.md
    services-planner.md
    schedule-builder.md
    budget-aggregator.md
    validator.md
    event-plan-builder.md
    html-builder.md
  skills/
    artifact-validator/
    event-plan-html-theme/
  hooks/
  mcp/
.workflow/
  runs/
    run-001/
    run-002/
    run-003/
```

The exact file layout may follow the installed Claude Code version, but the responsibilities and persisted artifacts must remain equivalent. Keep implementation and configuration files small, explicit, and easy for a human reviewer to inspect.

## 14. Demonstration runs

Store at least three complete sample runs in the repository. Each run must include its sample input, generated artifacts, persisted state, validation results, and final output where applicable.

Use materially different scenarios:

1. **Family birthday event:** a one-day indoor birthday event for approximately 20 guests, with a fixed budget, children among the guests, catering, activities, and a preferred location.
2. **Corporate workshop:** a professional event for approximately 40 participants with a strict schedule, accessibility and parking requirements, dietary preferences, presentation equipment, and vendor coordination.
3. **Outdoor community celebration:** a weather-sensitive event with activities, catering, services, contingency planning, and a demonstrated rejected plan followed by revision and approval.

At least one run must demonstrate:

- parallel independent agents;
- a quality-gate failure and targeted retry;
- a rejected approval followed by revision;
- resume from persisted state;
- actual use of the external search path and configured MCP server.

Use only safe sample data. Do not include real credentials or private personal information.

## 15. Implementation sequence

Follow this order unless the repository already contains an equivalent implementation:

### Phase 1 — Inspect and scaffold

- inspect the repository and installed Claude Code capabilities;
- document prerequisites and configuration assumptions;
- create the command, coordinator boundary, artifact directories, and state model;
- ensure secrets are excluded from version control.

### Phase 2 — Requirements and planning

- implement the clarification and confirmation loop;
- formalize event requirements into a Markdown artifact;
- create a dependency-aware execution plan;
- implement dynamic agent selection and parallel/sequential behavior.

### Phase 3 — Domain agents

- implement venue, weather, activities, catering, services, schedule, and budget agents as required by the plan;
- define each agent's input, output, ownership, and failure conditions;
- make external citations and cost assumptions part of the relevant artifacts.

### Phase 4 — Validation, skills, hooks, and MCP

- implement the two reusable skills;
- integrate and exercise the MCP server;
- implement all required `PreToolUse` and `PostToolUse` hooks;
- implement named quality gates and targeted retries.

### Phase 5 — Synthesis and approval

- implement the event-plan builder;
- implement deterministic approval and rejection/revision behavior;
- protect final HTML generation with the approval hook;
- implement standalone HTML rendering.

### Phase 6 — Persistence and evidence

- implement state persistence and resume;
- create three complete demonstration runs;
- update `CLAUDE.md` with workflow rules;
- update `README.md` with prerequisites, setup, run, resume, MCP, secret configuration, and verification instructions.

### Phase 7 — Verification

- run the project's available tests, linting, type checks, and build checks;
- manually inspect artifacts, budget calculations, schedule, source links, and final HTML;
- verify a clean checkout can be configured and run after prerequisites and secrets are supplied;
- verify no secret appears in tracked files, logs, artifacts, or user-facing output.

Do not claim completion until the Definition of Done below is satisfied.

## 16. Definition of Done

- [ ] `CLAUDE.md` documents the workflow and execution rules.
- [ ] At least one coordinator and five or more subagents are implemented and used.
- [ ] At least two reusable skills are implemented and used.
- [ ] Both `PreToolUse` and `PostToolUse` hooks are implemented and used.
- [ ] At least one community or custom MCP server is integrated and used.
- [ ] External web search is used and its sources are recorded.
- [ ] Artifacts follow a consistent, human-readable Markdown structure.
- [ ] Named quality gates are implemented.
- [ ] Quality-gate failures trigger targeted retries with a maximum of three attempts.
- [ ] Dependent artifacts are regenerated when an upstream artifact changes.
- [ ] Unresolved failures stop dependent work and are reported clearly.
- [ ] Workflow state survives interruptions and supports resume.
- [ ] Final output is blocked until deterministic human approval is recorded.
- [ ] Rejected output is revised and resubmitted for approval.
- [ ] Final output is delivered as readable Markdown and standalone HTML.
- [ ] Three different demonstration runs, including inputs, artifacts, and state, are committed.
- [ ] `README.md` contains setup, run, resume, verification, MCP, and environment instructions.
- [ ] No credentials, API keys, or secrets are committed.
- [ ] A clean checkout can be set up and run using the documented instructions.

## 17. Instructions to the implementing Claude Code session

When this document is provided to you:

1. Read this entire file before making changes.
2. Inspect the repository, existing instructions, package files, and available Claude Code features.
3. Preserve useful existing work; do not overwrite unrelated changes.
4. Implement the workflow rather than merely describing it.
5. Use the fixed Event Planner domain and `/plan-event` entry point above unless the user explicitly changes them.
6. Ask the user only questions that block implementation or require a secret/configuration that cannot be inferred safely.
7. After each implementation stage, run the most relevant available verification.
8. Keep all artifacts, state examples, hooks, skills, MCP configuration, and documentation in the repository.
9. Never commit or print secrets.
10. At the end, report changed files, verification performed, known limitations, and how to run or resume the workflow.
