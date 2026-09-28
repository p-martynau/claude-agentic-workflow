# Event Plan — Bristol Community Summer Celebration (v3)

## Status
READY

## Purpose
Synthesize every validated artifact into one coherent, human-readable event plan for the
residents' association to review and approve.

## Inputs used
`requirements.md` (v1), `venues.md` (v1), `weather.md` (**v3**), `activities.md` (v1),
`catering.md` (v1), `services.md` (v1), `schedule.md` (**v2**), `budget.md` (v1),
`validation-report.md` (**v3**) — all `READY`/`PASS`.

## Content

### Event overview
An outdoor community summer celebration for ~80 local residents of all ages, at **Trinity Centre
(Garden + Graffiti Room), Trinity Road, Bristol BS2 0NW**, on **Saturday 6 June 2027, 13:00–18:00**
(venue booked 11:00–19:00 to cover setup/cleanup). Casual, family-friendly community-fete style; no
alcohol, no fairground rides.

### Venue
Trinity Centre's outdoor Garden (25m × 20m) plus the adjoining indoor Graffiti Room (capacity 100
standing/60 seated), booked together for £140 for the 8-hour day. On-site 75-space car park
resolves the limited on-street parking constraint. Compared against Eastville Park, which was not
selected due to Council licensing lead time and no bundled indoor backup. Source:
https://www.trinitybristol.org.uk/booking.

### Weather and contingency
6 June 2027 is too far out for a point forecast, so this plan uses a **seasonal outlook** built
from real Open-Meteo historical data (via the `mcp__open-meteo__weather_archive` MCP tool) for
Bristol across six recent years (2019–2024, 30 day-samples around 6 June): typically mild
(mean 17°C day / 9°C night, range 13–22°C), with measurable rain on **18 of 30 sampled days
(60%)**. **Contingency:** the Graffiti Room is already booked as part of the venue and sits in the
same building — if a short-range forecast checked 48 hours out shows ≥50% precipitation
probability for 13:00–18:00, the event moves indoors from the start; otherwise it stays outdoors
with the room held ready. This must be re-checked with a real forecast once the date is within
~2 weeks.

**Decision-maker and guest communication (added in v2, after v1 was rejected for being too
vague on this point):** the residents' association's named on-the-day event lead makes the go/no-go
call at 11:00 and retains sole authority to call a mid-event move, so guests never get conflicting
instructions. If the event opens indoors, a notice is posted at the Garden entrance and on the
association's community noticeboard channel by 12:30: *"Due to the weather forecast, today's
celebration is moving indoors to the Graffiti Room at Trinity Centre — same building, same start
time, 13:00."* If rain starts mid-event (sustained more than 10 minutes, or heavy enough to affect
the PA or the buffet), the event lead makes one PA announcement and volunteers at the Garden's two
access points help guests — including anyone with a pushchair or mobility needs — move indoors
first.

### Schedule
| Time | Item |
|---|---|
| 11:00–13:00 | Setup; weather go/no-go check by the named event lead; PA and buffet lay-out |
| 13:00–14:00 | Arrivals, background music, lawn games, noticeboard |
| 14:00–17:00 | Face painting + kids' games; buffet open 14:00–16:00 |
| 14:30–15:00 | Seated garden quiz (accessible, low-mobility friendly) |
| 15:00–17:00 | Live acoustic music set |
| 17:00–17:30 | Closing announcements |
| 17:30–19:00 | Wind-down and teardown |

### Activities
Face painting (from £90, sourced), parachute games/bubbles, lawn games, a seated community quiz
placed for accessibility, and a photo/memory noticeboard. No fairground rides, per the confirmed
exclusion.

### Catering
Buffet for 80 with a halal-branded option (MyLahore) and a vegetarian option (paneer/vegetarian
curry), allergen labelling on all trays. Estimated at £14/head (£1,120 total) — **no firm quote
was obtained from MyLahore directly; the site returned an access-blocked page, so this cost and the
halal claim rest on the provider's own public marketing rather than a confirmed booking.**

### Services
PA system (Bristol Sound Hire, £100 estimated), live acoustic music (£300 estimated), litter/waste
bin hire (McCarthy Marland, £100 estimated), and one-day public liability insurance (£46 estimated,
~£5m cover).

### Budget summary
| | GBP |
|---|---|
| Subtotal | £1,896.00 |
| Contingency (12%) | £227.52 |
| **Grand total** | **£2,123.52** |
| User's limit | £3,000.00 |
| Headroom | £876.48 |

### Sources
Aggregated and deduplicated from all upstream artifacts:
- https://www.trinitybristol.org.uk/booking (venue)
- http://www.bristolparksforum.org.uk/information/events-in-parks/ (venue comparison)
- `mcp__open-meteo__geocoding` and `mcp__open-meteo__weather_archive` MCP tool calls (weather;
  six years of historical data, see `artifacts/weather.md` v3 for the full data table)
- https://www.poptop.uk.com/bristol/suppliers/childrenentertainment/facepainter/ (activities)
- https://togather.com/listings/catering/bristol/bristol/halal and
  https://bymylahore.co.uk/halal-catering-bristol/ (catering)
- http://bristolsoundhire.weebly.com/, https://www.lastminutemusicians.com/search/duos_small_groups/bristol.html,
  https://www.mccarthywaste.co.uk/service/event-waste/,
  https://www.events-insurance.co.uk/event-insurance-policies/one-day-event-insurance,
  https://www.protectivity.com/product/one-off-event-insurance/ (services)

### Open assumptions
- Catering cost and halal certification rest on MyLahore's own public claims, not a direct quote —
  flagged for the residents' association to confirm before booking.
- Waste bin hire has no published fixed price and is an estimate.
- The weather outlook is a seasonal climatology, not a forecast, and must be refreshed nearer the
  date.

## Sources
See the deduplicated list above.

## Quality checks
- Every fact traces to an upstream artifact; no new claims introduced during synthesis.
- No contradiction found between artifacts during synthesis.
- Budget, schedule, and validation summaries match `budget.md`, `schedule.md`, and
  `validation-report.md` exactly.

## Open issues
Carried from upstream: catering cost/halal-certification not independently confirmed; waste-bin
cost is an estimate; weather outlook must be refreshed nearer the date.

## Provenance
- Run ID: run-003
- Agent: event-plan-builder
- Version: 3
- Created at: 2026-09-28T15:35:00Z
- Revision reason: v1 (hash `bc6775db3ef556e8503fb9c58cdd7cbc7b9d6ee34bcfa75abd095290e6f7ea15`) was
  rejected — see `logs/approval-prompt-v1.md` — because the weather contingency did not say who
  decides or what guests are told; `weather.md`/`schedule.md` were revised to v2 to fix that, and
  v2 (hash `162013ff07b6868528f6cdfb1da5b2fc49e2ba89defda34a03fb653d4ddceb2c`) was approved and
  rendered to HTML. v3 (this version) followed a post-approval compliance review which found that
  `weather.md` v1/v2 had sourced its data via `WebFetch` instead of the configured Open-Meteo MCP
  server; `weather.md` was revised to v3 using real `mcp__open-meteo__*` tool calls (see
  `logs/mcp-note.md`), re-validated (`validation-report.md` v3, all gates PASS), and this v3 plan
  was resynthesized and re-approved before the HTML was regenerated.
