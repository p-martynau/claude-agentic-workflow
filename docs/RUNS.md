# Demonstration runs

Three materially different, fully real runs live under [`.workflow/runs/`](../.workflow/runs/).
"Real" means: actual `WebSearch`/`WebFetch` calls for every cited source, actual SHA-256 hashes
computed from the actual `event-plan.md` bytes, and actual live enforcement of the
[hooks](HOOKS.md) — every `output/event-plan.html` below was written only after
`approval-gate-guard` independently verified the recorded approval hash against the file on disk.

Each run folder contains: `input.md` (the raw request), `workflow-state.json` (full persisted
state), `artifacts/*.md` (one per agent, see [`AGENTS.md`](AGENTS.md)), `logs/*.md` (clarification
Q&A, execution/approval/resume logs), and `output/event-plan.html` (the final deliverable).

## run-001 — Family birthday (London)

**Requested:** one-day indoor 8th-birthday party, London, ~20 guests (mostly children 6–10 plus
parents), fixed £1,200 GBP budget, kid-friendly activities, vegetarian + nut-allergy catering,
easy parking or transit access, Saturday 14 Nov 2026, 12:00–16:00.
Full text: [`input.md`](../.workflow/runs/run-001/input.md).

**What came out:** venue = Magdalen Hall Main Hall, Bermondsey (free weekend parking, near London
Bridge); a booked-marketplace children's entertainer; M&S vegetarian sandwich/wrap platter plus a
nut-free-factory birthday cake; a conflict-free 11:00–16:30 schedule (including setup/cleanup);
total **£638.55 vs. the £1,200 limit** (10% contingency included, ~47% headroom). One minor gate
finding (`services-fit`: an implicit setup-time assumption wasn't stated explicitly) was found on
the first validator pass, fixed with a targeted retry of `services-planner` alone, and confirmed
on the second pass — demonstrating parallel independent-agent dispatch plus a clean retry cycle.
Approved on the first plan version (hash `ed8fd972...`), literal `APPROVE`.

Details: [`event-plan.md`](../.workflow/runs/run-001/artifacts/event-plan.md) ·
[`validation-report.md`](../.workflow/runs/run-001/artifacts/validation-report.md) ·
[`workflow-state.json`](../.workflow/runs/run-001/workflow-state.json) ·
[`output/event-plan.html`](../.workflow/runs/run-001/output/event-plan.html)

## run-002 — Corporate workshop (Manchester)

**Requested:** one-day internal strategy workshop, Manchester, ~40 participants, strict
09:00–17:00 schedule, step-free access and parking/transit, vegetarian/vegan/gluten-free catering,
projector/mic/Wi-Fi/whiteboard, £6,000 GBP budget, vendor-coordinated AV.
Full text: [`input.md`](../.workflow/runs/run-002/input.md).

**What came out:** venue = King's House Conference Centre (step-free, on-site/nearby parking,
central transit); catering via Corporate Lunch (veg/vegan/gluten-free confirmed); AV via Event
Production Group. **Genuine quality-gate failure on the first validator pass:** `services-fit`
failed because the AV vendor's delivery/setup/collection fee — a real, easy-to-miss line item —
was missing from `services.md`, so the budget understated the true cost. A targeted retry re-ran
only `services-planner` (added a £120 estimated fee) and `budget-aggregator` (recomputed the
total); `schedule-builder` was *not* re-run because timing didn't change. Second validator pass:
all gates PASS. Final total **£2,340.80 vs. the £6,000 limit**. Approved on plan v1 (synthesis only
happens after validation passes, so the retry happened before there was a plan to version), hash
`0688eaff...`, literal `APPROVE`.

Details: [`event-plan.md`](../.workflow/runs/run-002/artifacts/event-plan.md) ·
[`validation-report.md`](../.workflow/runs/run-002/artifacts/validation-report.md) ·
[`workflow-state.json`](../.workflow/runs/run-002/workflow-state.json) ·
[`output/event-plan.html`](../.workflow/runs/run-002/output/event-plan.html)

## run-003 — Outdoor community celebration (Bristol)

**Requested:** outdoor summer celebration in a Bristol park, ~80 residents of all ages, Saturday
6 Jun 2027, 13:00–18:00, real weather check + rain contingency required, £3,000 GBP budget, mixed
activities/music/catering (vegetarian + halal-friendly), PA + waste management, accessibility for
older adults/pushchairs, limited on-street parking.
Full text: [`input.md`](../.workflow/runs/run-003/input.md).

**What came out:** venue = Trinity Centre (outdoor Garden + an adjoining indoor Graffiti Room
booked together, so the rain backup is in the same building); a weather outlook built from real
Open-Meteo historical data — since June 2027 is too far out for a point forecast, this is honestly
labelled a **seasonal climatology outlook**, not a forecast, with a note to re-check closer to the
date. Final total **£2,123.52 vs. the £3,000 limit**, all 14 named gates PASS.

This run specifically demonstrates four things the other two don't:

- **A genuine rejected approval and revision.** Plan v1 (hash `bc6775db...`) was rejected because
  its weather contingency didn't say *who* decides to move the event indoors or *what* guests are
  told. The feedback was routed only to `weather-researcher` (plus `schedule-builder` for
  consistency) — v2 names a specific decision-maker, an exact guest announcement, and a mid-event
  move threshold. Re-validated (all gates PASS again), synthesized as plan v2 (hash `162013ff...`),
  and approved with the literal `APPROVE` only after that. See
  [`logs/approval-prompt-v1.md`](../.workflow/runs/run-003/logs/approval-prompt-v1.md),
  [`logs/approval-prompt-v2.md`](../.workflow/runs/run-003/logs/approval-prompt-v2.md).
- **A genuine resume from persisted state.** The run was frozen right after the five parallel
  research agents completed (`venue`, `weather`, `activities`, `catering`, `services`, all READY)
  with everything downstream still `pending` — see
  [`logs/interruption-note.md`](../.workflow/runs/run-003/logs/interruption-note.md). It was then
  picked back up strictly from `schedule-builder` onward, without repeating any of the five
  completed artifacts — see
  [`logs/resume-log.md`](../.workflow/runs/run-003/logs/resume-log.md).
- **A real, named MCP tool call.** `weather.md` went through three versions: v1/v2 were first
  authored in a session where the Open-Meteo MCP server wasn't yet attached, so they used a
  `WebFetch` call against the same public API as a stand-in (see
  [`logs/mcp-note.md`](../.workflow/runs/run-003/logs/mcp-note.md) for why that doesn't fully
  satisfy the brief's "MCP actually used" requirement). Once the MCP server was attached, v3
  replaced that with genuine `mcp__open-meteo__geocoding` and `mcp__open-meteo__weather_archive`
  tool calls (six years, 2019–2024, 30 day-samples) — a strict upgrade that also resolved v1/v2's
  "only one year sampled" limitation. This flowed through a full re-validation
  (`validation-report.md` v3), a resynthesized plan (`event-plan.md` v3, hash `784de3e8...`), a
  fresh `APPROVE`, and a re-rendered HTML, each step re-verified against the live hooks — see
  [`logs/revision-log.md`](../.workflow/runs/run-003/logs/revision-log.md) and
  [`logs/approval-prompt-v3.md`](../.workflow/runs/run-003/logs/approval-prompt-v3.md).
- **A pinned MCP server version.** `.mcp.json` pins `open-meteo-mcp-server@2.5.0` rather than a
  floating tag, so a clean checkout gets the exact version this run used.

One honest open item was carried through rather than hidden: a halal-catering provider's page
returned HTTP 403 on direct fetch, so its claim/pricing rests on the provider's own public
marketing rather than a confirmed quote — flagged in the plan for the residents' association.

Details: [`event-plan.md`](../.workflow/runs/run-003/artifacts/event-plan.md) ·
[`validation-report.md`](../.workflow/runs/run-003/artifacts/validation-report.md) ·
[`workflow-state.json`](../.workflow/runs/run-003/workflow-state.json) ·
[`output/event-plan.html`](../.workflow/runs/run-003/output/event-plan.html)
