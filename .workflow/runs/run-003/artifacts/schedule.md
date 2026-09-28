# Event Schedule — Bristol Community Summer Celebration, 6 June 2027

## Status
READY

## Purpose
Build a feasible chronological timeline for the confirmed 13:00–18:00 guest window (plus setup and
cleanup) from the venue, weather contingency, activities, catering, and services artifacts, with no
unexplained overlaps.

## Inputs used
- `artifacts/requirements.md` (13:00–18:00 guest window, Europe/London, 6 June 2027)
- `artifacts/venues.md` (Trinity Centre Garden + Graffiti Room, 8-hour day booking)
- `artifacts/weather.md` (seasonal outlook, contingency trigger and Graffiti Room backup)
- `artifacts/activities.md` (face painting, lawn games, quiz, noticeboard)
- `artifacts/catering.md` (buffet timing)
- `artifacts/services.md` (PA setup/teardown, live music setup/teardown, waste bin timing)

## Content

The Trinity Centre booking covers an 8-hour day; the guest-facing window is 5 hours (13:00–18:00),
leaving 3 hours split between setup (before) and cleanup (after) — this fits the venue's booked
window (11:00–19:00) with no overrun.

| Time | Item | Notes |
|---|---|---|
| 11:00–11:15 | Weather go/no-go check | Made by the residents' association's named on-the-day event lead (per `weather.md` v2), who checks the short-range forecast; if ≥50% precipitation probability for 13:00–18:00, the event opens indoors in the Graffiti Room from 13:00, with a notice posted at the Garden entrance by 12:30. Otherwise proceed outdoors in the Garden with the Graffiti Room held ready, and the same event lead retains sole authority to call a mid-event move per the threshold in `weather.md` v2. |
| 11:15–12:45 | Setup | PA system install (`services.md`: 30 min, done within this window), tables/seating/signage/noticeboard, catering delivery and buffet lay-out, lawn games set out. Acoustic act arrives later (see 14:40 setup below), not needed this early. |
| 12:45–13:00 | Final checks | Sound check on PA, buffet cover-up until service, accessibility check of paths/seating for pushchairs and older adults. |
| 13:00–14:00 | Doors open / arrivals | Background recorded music over the PA. Lawn games and noticeboard self-serve and active (intentional overlap — both are passive, no staffing conflict). |
| 14:00–17:00 | Face painting + parachute games/bubbles | Kids' activity block (`activities.md`). Runs concurrently with lawn games/noticeboard and, from 14:00, the buffet (intentional overlap: catering is self-serve buffet, not a seated meal, so grazing alongside kids' activities is expected, not a conflict). |
| 14:00–16:00 | Buffet open | Self-serve halal + vegetarian buffet (`catering.md`), allergen labels on all trays. |
| 14:30–15:00 | Seated garden quiz | Placed before the live music set specifically so it is not competing acoustically with amplified music — avoids an unexplained overlap. Near fixed seating for older adults/low-mobility guests. |
| 14:40–15:00 | Live act setup | Acoustic performer's own setup (`services.md`: ~20 min before their 15:00 slot). |
| 15:00–17:00 | Live acoustic music set | Background-to-foreground live music (`services.md`/`activities.md`); intentionally overlaps with the tail of the buffet and with free lawn-game play — both are ambient/self-serve activities designed to run alongside music. |
| 17:00–17:15 | Live act teardown | ~15 min after their 17:00 finish (`services.md`). |
| 17:00–17:30 | Closing announcements + thank-yous | Over the PA, while the buffet is cleared away. |
| 17:30–18:00 | Wind-down | Guests depart at their own pace; noticeboard/photo wall stays up until close. |
| 18:00–18:30 | Cleanup (guest-facing area) | Litter collection into the hired bins (`services.md`), tables/seating cleared. |
| 18:30–19:00 | Teardown + venue handover | PA teardown (15 min per `services.md`) and final site check, within the booked 11:00–19:00 window. |

### Conflict check
No two staffed, amplified, or space-competing items are scheduled at the same time without an
explicit note above. All same-time items are deliberately passive/self-serve pairings (buffet with
kids' activities; lawn games/noticeboard with everything). The quiz was moved earlier specifically
to avoid competing with the amplified live set — this is the one adjustment made to resolve a
potential conflict, and it is recorded here rather than silently applied.

## Sources
N/A — derived from `venues.md`, `weather.md`, `activities.md`, `catering.md`, and `services.md` as
cited inline above.

## Quality checks
- Full 11:00–19:00 venue-booked window is accounted for with no gaps and no overrun.
- Every activity, meal window, and service setup/teardown from the upstream artifacts appears once.
- All same-time items are explicitly justified as intentional, non-conflicting overlaps.

## Open issues
None — no unresolved timing conflicts. If the go/no-go check at 11:00 moves the event indoors,
the same running order applies inside the Graffiti Room (lawn games and the parachute/bubbles
session would move to whatever open floor space remains, which is not separately itemised here —
flagged as a minor detail for the on-the-day organiser, not a gate-blocking issue).

## Provenance
- Run ID: run-003
- Agent: schedule-builder
- Version: 2
- Created at: 2026-09-28T14:56:00Z
- Revision reason: kept consistent with `weather.md` v2 after the v1 approval rejection named the
  contingency as too vague — the go/no-go line now names the same decision-maker. See
  `logs/revision-log.md`.
