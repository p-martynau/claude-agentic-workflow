# Event Schedule — 8th Birthday Party (run-001)

## Status
READY

## Purpose
Build a feasible, non-overlapping timeline for Saturday 14 November 2026, covering setup through
cleanup, that places every activity, catering moment, and service from the upstream artifacts.

## Inputs used
- `artifacts/requirements.md` (date/time window 12:00–16:00, Europe/London)
- `artifacts/venues.md` (Magdalen Hall Main Hall; hall bookable 11:00–17:00 window assumed for a
  6-hour hire block)
- `artifacts/activities.md` (entertainer show, games, cake moment, free play/craft)
- `artifacts/catering.md` (buffet + cake timing)
- `artifacts/services.md` (balloon decoration setup time)

## Content

| Time (Europe/London) | Block | Details | Source artifact |
|---|---|---|---|
| 11:00–12:00 | Setup (pre-event, not guest-facing) | Venue access begins; balloon decoration installed (`services.md`); buffet platters and cake laid out in the kitchen/serving area (`catering.md`). | venues.md, services.md, catering.md |
| 12:00–12:15 | Arrival & welcome | Guests arrive; informal mingling as everyone gathers. | activities.md |
| 12:15–13:00 | Entertainer show | 45-minute children's entertainer show (magic/games/balloon modelling). | activities.md |
| 13:00–13:45 | Buffet lunch | Sandwich platters (incl. vegetarian selection) and snacks served; drinks available throughout. | catering.md |
| 13:45–14:15 | Party games | Pass-the-parcel and musical statues, run by parents/host. | activities.md |
| 14:15–14:30 | Cake & candles | Birthday cake (nut-free) cut, "Happy Birthday" sung. | catering.md, activities.md |
| 14:30–15:15 | Free play / craft table | Supervised free play and craft table; parents socialise. | activities.md |
| 15:15–15:45 | Wind-down & goodbyes | Goodie-bag handout (party extras, `services.md`), informal photos, guests start leaving. | services.md |
| 15:45–16:00 | Departure | Remaining guests depart; event officially ends at 16:00 as required. | requirements.md |
| 16:00–16:30 | Cleanup (post-event, not guest-facing) | Pack-down of decorations and catering remnants, hall vacated within the 6-hour hire block. | venues.md |

**Total guest-facing programme:** 12:00–16:00 (the full required 4-hour window), fully accounted
for with no gaps and no unexplained overlaps. Background elements (drinks available "throughout,"
decoration visible throughout) are intentional, continuous backdrops, not scheduling conflicts.

**Venue hire block:** 11:00–17:00 (6 hours: 1h setup + 4h event + up to 1h buffer/cleanup, hire
budgeted for 6 hours in `budget.md`), which fits inside a hall bookable 7am–10pm.

## Sources
N/A — derived entirely from prior artifacts (`venues.md`, `activities.md`, `catering.md`,
`services.md`), as cited per row above.

## Quality checks
- Every activity, catering moment, and service from the upstream artifacts appears exactly once in
  the timeline.
- No two guest-facing blocks overlap without an explicit, intentional reason (drinks/decoration are
  continuous backdrops, not scheduled events).
- Setup and cleanup are scheduled outside the guest-facing 12:00–16:00 window, within the venue's
  assumed availability.
- The full required 4-hour guest window (12:00–16:00) is covered without gaps.

## Open issues
- The exact venue hire block (11:00–17:00, 6 hours) is an assumption consistent with the "6 hours"
  used for budgeting in `venues.md`; the family should confirm the precise bookable hours with
  Magdalen Hall directly, since Tagvenue's listing did not specify a fixed access window beyond
  general opening hours.
- Decoration setup time was not confirmed precisely by the source in `services.md`; it is assumed
  to fit within the 1-hour pre-event setup block.

## Provenance
- Run ID: run-001
- Agent: schedule-builder
- Version: 1
- Created at: 2026-09-28T09:45:00Z
