# Event plan — Northbridge Analytics internal strategy workshop

## Status
READY

## Purpose
Synthesize every validated artifact into one coherent, human-readable plan for the requester
(Alicia Grant, Operations Manager, Northbridge Analytics Ltd) to review and approve.

## Inputs used
- `artifacts/requirements.md`, `artifacts/venues.md`, `artifacts/activities.md`,
  `artifacts/catering.md`, `artifacts/services.md` (v2), `artifacts/schedule.md`,
  `artifacts/budget.md` (v2), `artifacts/validation-report.md` (v2, all applicable gates PASS)

## Content

### Overview
A one-day internal strategy workshop for Northbridge Analytics Ltd, Manchester, for approximately
40 participants. Business-casual, professional tone, no theme. Target date **18 November 2026**
(±1 week flexible if the venue is unavailable), 09:00–17:00, Europe/London.

### Venue
**King's House Conference Centre**, Sidney Street, Manchester M1 7HB. Step-free access to all main
areas, accessible toilets, lift to every floor; accessible on-street parking on Sidney Street plus
nearby car parks for the few attendees who drive, central-Manchester transit links for everyone
else; each room has high-speed Wi-Fi. Estimated full-day hire: **£480.00** (estimate — no public
day-rate for a 40-person room; confirm firm quote by phone: 0161 276 8194). Flipchart/whiteboard
stock to be confirmed at booking (AV vendor available as fallback).

### Schedule (09:00–17:00)
| Time | Item |
|---|---|
| 08:00–09:00 | AV vendor load-in, setup, and test (outside guest hours) |
| 09:00–09:15 | Arrival & registration, AM tea/coffee |
| 09:15–09:30 | Welcome & objectives |
| 09:30–11:00 | Strategy session 1 |
| 11:00–11:15 | Energiser (no-cost, self-facilitated) |
| 11:15–11:30 | Break |
| 11:30–12:45 | Strategy session 2 (breakout groups) |
| 12:45–13:30 | Working lunch |
| 13:30–14:45 | Strategy session 3 |
| 14:45–15:00 | Break, PM tea/coffee |
| 15:00–16:15 | Strategy session 4 (prioritisation & action planning) |
| 16:15–16:45 | Report-back & next steps |
| 16:45–17:00 | Wrap-up & close |
| 17:00–17:30 | AV vendor teardown & collection (outside guest hours) |

### Activities
Strategy sessions are internally facilitated by Northbridge Analytics (no external cost). One
15-minute energiser is included mid-morning at no cost (self-facilitated icebreaker). An optional
paid alternative, a short conference-energiser session from **Laughtercise** (Manchester), is
available on request but is not included in the budget below pending a direct quote.

### Catering
Provider: **Corporate Lunch** (corporatelunch.co.uk). Working lunch on the Gold buffet tier
(£20.95/head, list price), confirmed vegetarian, vegan, and gluten-free options. AM tea/coffee +
pastries and PM tea/coffee + biscuits are estimated add-ons (£5.00 and £3.00 per head
respectively, not separately published by the provider — to be confirmed). Free delivery applies
(order exceeds £200). Allergen specifics beyond vegetarian/vegan/gluten-free are still to be
confirmed with the provider once final headcount is set.

### Services
AV/equipment vendor: **Event Production Group** (EPG), Trafford Park, Manchester — projector +
screen, two wireless microphones + small PA, and on-site technician support, plus a delivery,
setup, and collection fee for the 08:00 load-in and 17:00 collection. All three AV lines are
estimates pending EPG's firm quote (EPG does not publish a price list). Wi-Fi is provided by the
venue at no extra cost.

### Budget summary (GBP)
| Line item | Cost |
|---|---|
| Venue day hire | £480.00 |
| Catering (lunch + AM/PM refreshments) | £1,158.00 |
| AV/equipment (hire + delivery/setup/collection) | £490.00 |
| Subtotal | £2,128.00 |
| Contingency (10%) | £212.80 |
| **Grand total** | **£2,340.80** |
| **Budget limit** | **£6,000.00** |
| **Headroom** | **£3,659.20** |

All figures are estimates pending firm vendor quotes (see `budget.md` v2 for the full breakdown and
sourcing). The headroom below the £6,000 limit is intentionally retained as a buffer against firm
quotes coming in above these market-rate estimates.

### Validation result
`validation-report.md` v2: all applicable named gates **PASS**. One gate failed on the first pass
(`services-fit` — the AV vendor's delivery/setup/collection fee was initially missing from
`services.md`) and was resolved by a targeted retry of `services-planner`, followed by a
`budget-aggregator` re-run and a full validator re-check. Details in `validation-report.md`.

### Open assumptions carried into this plan
- Venue day-rate, catering AM/PM add-ons, and all three AV lines are estimates, not firm quotes.
- Final date (18 Nov vs. within ±1 week) depends on King's House availability.
- Final allergen specifics beyond vegetarian/vegan/gluten-free pending confirmation with final
  headcount.
- Early (08:00) and late (17:30) venue access for AV load-in/collection needs confirmation at
  booking.

## Sources
- [King's House Conference Centre](https://www.kingshouse.co.uk/)
- [King's House Conference Centre — Tagvenue listing](https://www.tagvenue.com/venues/manchester/4865/king-s-house-conference-centre)
- [First Floor Hall — King's House, Tagvenue](https://www.tagvenue.com/rooms/manchester/9853/kings-house-conference-centre/first-floor-hall)
- [Meeting Rooms & Conference Space Manchester — Hyatt Regency](https://www.hyatt.com/hyatt-regency/en-US/manrm-hyatt-regency-manchester/meetings)
- [The 16 Best Conference Hotels for Hire in Manchester — Tagvenue](https://www.tagvenue.com/hire/conference-hotels/manchester)
- [Office Lunch Catering Manchester — Corporate Lunch](https://www.corporatelunch.co.uk/office-lunch-catering-manchester/)
- [Catering For Meetings Manchester — Corporate Lunch](https://www.corporatelunch.co.uk/catering-for-meetings-manchester/)
- [Corporate Catering Manchester — Manchester Catering Company](https://manchestercateringcompany.com/corporate-catering-manchester/)
- [AV Hire Manchester — Event Production Group](https://eventproductiongroup.co.uk/av-hire-manchester/)
- [Conference AV Hire Manchester — Event Production Group](https://eventproductiongroup.co.uk/conference-av-hire-manchester/)
- [Laughtercise — Manchester team building](https://laughtercise.co.uk/team-building/manchester/)

## Quality checks
- Every fact traces to an upstream artifact; no new claims introduced during synthesis.
- No contradiction found between artifacts during synthesis (final-consistency gate satisfied).
- Budget, schedule, venue, catering, and services sections match their source artifacts exactly.

## Open issues
See "Open assumptions carried into this plan" above.

## Provenance
- Run ID: run-002
- Agent: event-plan-builder
- Version: 1
- Created at: 2026-09-29T10:50:00Z
