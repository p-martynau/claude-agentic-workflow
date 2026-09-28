# Validation Report — run-001

## Status
READY

## Purpose
Apply every named quality gate from `docs/PRACTICAL_TASK.md#8-quality-gates` across all run-001
artifacts and report pass/fail findings with the responsible agent, before synthesis. This report
covers two attempts: attempt 1 found one minor gate failure and routed a targeted retry to the
responsible agent; attempt 2 confirms the fix and reports the final, current result.

## Inputs used
All artifacts under `artifacts/`: `requirements.md`, `venues.md`, `activities.md`, `catering.md`,
`services.md` (v2, revised after attempt 1), `schedule.md`, `budget.md`. The `artifact-validator`
skill was invoked against all seven files in attempt 1, and re-invoked against `services.md` v2
alone in attempt 2 (the other six files were unchanged, so they were not re-validated, per the
coordinator's targeted-retry rule).

## Content

### Attempt 2 (current, final result)

`services-fit` re-checked against `services.md` v2: the revised `## Open issues` section now states
the services-planner's own accepted 30-minute setup-duration assumption explicitly, rather than
leaving it as an unresolved question. **Result: PASS.** No other gate was affected by this change
(no cost or fact changed, only a timing assumption was made explicit), so `schedule.md` and
`budget.md` did not need to be regenerated.

| # | Gate | Result (attempt 2) |
|---|---|---|
| 1 | requirements-completeness | PASS |
| 2 | artifact-structure | PASS |
| 3 | budget-limit | PASS |
| 4 | schedule-feasibility | PASS |
| 5 | no-overlapping-activities | PASS |
| 6 | venue-fit | PASS |
| 7 | catering-fit | PASS |
| 8 | services-fit | PASS (was FAIL in attempt 1; resolved by a targeted `services-planner` retry — see attempt 1 below) |
| 9 | travel-and-transitions | PASS |
| 10 | weather-readiness | N/A — event is fully indoor |
| 11 | no-duplicate-recommendations | PASS |
| 12 | meaningful-program | PASS |
| 13 | source-validity | PASS |
| 14 | final-consistency | N/A — `event-plan.md` not yet written at validation time |

**Overall: READY.** All applicable gates pass; the workflow may proceed to `event-plan-builder`.

### Attempt 1 (superseded — kept for audit trail)

`artifact-validator` skill results (mechanical checks, all 7 files, attempt 1): structure PASS
(exact section order present in every file), status-validity PASS, provenance-completeness PASS,
non-empty-content PASS, source-validity PASS (every external claim has a matching real
`http(s)://` URL; generic commodity estimates explicitly labelled rather than presented as sourced
facts), no-unmarked-estimates PASS, no internal leakage PASS.

| # | Gate | Result | Finding | Affected artifact | Responsible agent |
|---|---|---|---|---|---|
| 1 | requirements-completeness | PASS | All required categories present and confirmed (`CONFIRM` received). | requirements.md | requirements-formalizer |
| 2 | artifact-structure | PASS | See skill results above. | all | all |
| 3 | budget-limit | PASS | £638.55 total (incl. 10% contingency) vs. £1,200 limit — well under. | budget.md | budget-aggregator |
| 4 | schedule-feasibility | PASS | Full 12:00–16:00 window accounted for; setup/cleanup fit the assumed 11:00–17:00 hire block. | schedule.md | schedule-builder |
| 5 | no-overlapping-activities | PASS | No unexplained double-booking; continuous backdrops (drinks, decoration) explicitly marked as intentional. | schedule.md | schedule-builder |
| 6 | venue-fit | PASS | Magdalen Hall matches location, guest count (20 ≪ 120 cap), indoor, and parking/transport requirement. | venues.md | venue-researcher |
| 7 | catering-fit | PASS | Guest count, vegetarian requirement, and nut-allergy requirement each covered by a sourced product. | catering.md | catering-planner |
| 8 | services-fit | **FAIL** | Decoration setup/teardown duration is not stated by the source and `services.md` only raised it as an open issue without a stated resolution/assumption; `schedule.md` assumed it fits the 1-hour setup block, but this assumption was not explicitly recorded in `services.md` itself, so the service's timing was not fully "accounted for" as the gate requires. | services.md | services-planner |
| 9 | travel-and-transitions | PASS | No stated travel-time limits between segments; guests arrive/depart from a single venue. | schedule.md | schedule-builder |
| 10 | weather-readiness | N/A | Event is fully indoor; gate does not apply (no `weather.md` required per `requirements.md`). | — | — |
| 11 | no-duplicate-recommendations | PASS | No venue, vendor, or activity is repeated across artifacts. | all | — |
| 12 | meaningful-program | PASS | Every schedule segment has an intentional activity (`schedule.md`). | schedule.md | schedule-builder |
| 13 | source-validity | PASS | See skill results above. | all | — |
| 14 | final-consistency | N/A | `event-plan.md` does not exist yet at this stage. | — | — |

**Resolution:** the finding was routed back to `services-planner` alone (retry_count 1 of 3 for
`services.md`); no downstream agent needed to re-run because no cost or scheduling fact changed,
only an explicit assumption was added to `services.md` (bumped to v2). `validator` then re-ran
(attempt 2, above) and confirmed PASS.

## Sources
N/A — this report evaluates prior artifacts; see each artifact's own `## Sources` section.

## Quality checks
- Every one of the 14 named gates was explicitly evaluated in both attempts (2 marked N/A with a
  stated reason, rather than silently skipped).
- The one failing gate in attempt 1 (`services-fit`) named the specific artifact and responsible
  agent so the coordinator could retry precisely that one component rather than the whole workflow.
- No gate was weakened, skipped, or deleted to force a pass; the fix was a genuine, verifiable
  change to `services.md` (v1 → v2).

## Open issues
None outstanding. The single attempt-1 finding (`services-fit`) is resolved and verified in
attempt 2.

## Provenance
- Run ID: run-001
- Agent: validator
- Version: 2
- Created at: 2026-09-28T10:25:00Z
