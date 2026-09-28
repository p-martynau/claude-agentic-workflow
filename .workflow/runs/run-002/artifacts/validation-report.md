# Validation report — Manchester strategy workshop (v2)

## Status
READY

## Purpose
Re-check every named quality gate after the targeted retry (`services.md` v2, `budget.md` v2) that
followed the v1 `services-fit` failure, and confirm the plan is ready for synthesis.

## Inputs used
- `artifacts/requirements.md`, `artifacts/venues.md`, `artifacts/activities.md`,
  `artifacts/catering.md`, `artifacts/services.md` (v2), `artifacts/schedule.md`,
  `artifacts/budget.md` (v2)
- `artifact-validator` skill (re-run on the two changed artifacts, `services.md` and `budget.md`)

## Content

### artifact-validator skill pass (mechanical checks)
`services.md` v2 and `budget.md` v2 re-checked: heading structure, valid `## Status`, complete
`## Provenance` (version bumped to 2 on both), non-empty content, sourced claims, and the new fee
line correctly marked "estimated." **PASS.** The other five artifacts are unchanged from v1's
already-passing mechanical check.

### Named gates

| Gate | Result | Finding | Affected artifact | Responsible agent |
|---|---|---|---|---|
| requirements-completeness | PASS | Unchanged from v1. | requirements.md | requirements-formalizer |
| artifact-structure | PASS | All artifacts, including the two revised ones, follow the shared contract. | all | — |
| budget-limit | PASS | £2,340.80 vs. £6,000 limit, recomputed with the corrected AV cost — still well under. | budget.md | budget-aggregator |
| schedule-feasibility | PASS | Unchanged — schedule.md was not affected by the services.md fee addition (no timing change). | schedule.md | schedule-builder |
| no-overlapping-activities | PASS | Unchanged from v1. | schedule.md | schedule-builder |
| venue-fit | PASS | Unchanged from v1. | venues.md | venue-researcher |
| catering-fit | PASS | Unchanged from v1. | catering.md | catering-planner |
| **services-fit** | **PASS (resolved)** | `services.md` v2 now includes the delivery/setup/collection fee (£120.00, estimated) as its own line, alongside the original equipment lines. The AV service is now fully represented, timed (against the schedule.md 08:00/17:00 access windows), and costed. | services.md | services-planner |
| travel-and-transitions | PASS | Unchanged from v1. | schedule.md | schedule-builder |
| weather-readiness | N/A | Indoor event; weather branch correctly not dispatched. | — | — |
| no-duplicate-recommendations | PASS | Unchanged from v1. | all | — |
| meaningful-program | PASS | Unchanged from v1. | schedule.md / activities.md | schedule-builder / activities-planner |
| source-validity | PASS | Unchanged from v1; the new fee line cites the same EPG source already listed in `services.md`. | all | — |
| final-consistency | N/A | `event-plan.md` does not exist yet — checked once synthesis happens. | — | — |

**Overall: READY** — every applicable gate passes. `event-plan-builder` may now synthesize
`event-plan.md`.

## Sources
Derived from the artifacts listed above; no new external sources retrieved by this agent.

## Quality checks
- The previously failing gate (`services-fit`) is explicitly marked resolved with the specific fix
  that resolved it, not silently dropped from the report.
- Only the two artifacts whose inputs actually changed (`services.md`, `budget.md`) were re-checked
  in detail; the rest are carried forward as still-valid, per the "do not restart successful
  independent work" rule.

## Open issues
None blocking. All cost figures remain estimates pending firm vendor quotes, disclosed in
`budget.md` v2's own open issues — this is a disclosed assumption, not an unresolved gate failure.

## Provenance
- Run ID: run-002
- Agent: validator
- Version: 2
- Created at: 2026-09-29T10:40:00Z
