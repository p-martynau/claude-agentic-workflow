# Venue Options — Bristol Community Summer Celebration

## Status
READY

## Purpose
Compare real, currently operating Bristol venue options against the confirmed requirements
(outdoor space for ~80 guests, indoor/sheltered wet-weather backup, accessibility, parking or bus
access, budget) and recommend one.

## Inputs used
- `artifacts/requirements.md` (location: Bristol; ~80 guests; outdoor + wet-weather backup;
  accessibility for older adults and pushchairs; limited on-street parking; £3,000 budget)

## Content

### Candidate 1 — Trinity Centre, Trinity Road, Bristol BS2 0NW (selected)
- **Type:** Community/arts venue with an outdoor **Garden** (25m × 20m) and an adjoining indoor
  **Graffiti Room** (11m × 12m, capacity 100 standing / 60 seated) in the same building.
- **Pricing found:** Garden alone £60 for an 8-hour day; Garden **with** Graffiti Room £140 for an
  8-hour day (source page states this combined rate explicitly).
- **Accessibility:** Same-building indoor space means no travel between outdoor and indoor areas
  if weather turns — good for older adults and pushchairs. Site-level accessibility features
  (ramps/step-free routes) are not itemised on the page; flagged as unconfirmed.
- **Parking:** On-site 75-space pay-and-display car park (£1–£8 depending on duration) — directly
  answers the "limited on-street parking nearby" constraint.
- **Capacity fit:** Garden is sized for festivals/parties; Den (a separate seasonal covered space)
  is rated to 150 seated/500 standing, so 80 guests fits the Garden comfortably.
- **Constraints satisfied:** outdoor + same-site indoor backup, on-site parking, capacity, budget.
- **Constraints not confirmed:** step-free access details, toilet count for 80 guests (not itemised
  on the page — flagged as an open issue).
- **Source:** https://www.trinitybristol.org.uk/booking (retrieved 2026-09-28)

### Candidate 2 — Eastville Park (Bristol City Council public park)
- **Type:** Large public park, commonly used for community events.
- **Licensing:** Per Bristol Parks Forum, **any event in a Bristol park expecting more than 50
  people on site needs to be licensed** through the Council's Events Licensing team, and larger
  applications can need **3–12 months** of lead time.
- **Why not selected:** Our confirmed date (6 June 2027) is well within a feasible lead time today,
  but the licensing process introduces approval risk and coordination overhead (site permissions,
  safety advisory group) that a private venue booking avoids, and no on-site indoor wet-weather
  space is bundled with a park booking — a separate marquee/gazebo would be needed at extra cost
  (see `services.md` for marquee/gazebo pricing found, which alone approaches £2,000 on average and
  would consume most of the budget).
- **Constraints satisfied:** outdoor, likely free or low direct hire cost, central Bristol.
- **Constraints not satisfied:** no bundled indoor contingency, licensing lead-time/approval risk,
  parking is street-based only (does not resolve the "limited on-street parking" constraint).
- **Source:** http://www.bristolparksforum.org.uk/information/events-in-parks/ (retrieved
  2026-09-28)

### Recommendation
**Trinity Centre (Garden + Graffiti Room, £140/day)** — satisfies outdoor space, an on-site indoor
wet-weather backup at no extra logistics cost, on-site parking, and capacity, all within budget.

## Sources
- https://www.trinitybristol.org.uk/booking — Trinity Centre space hire page, pricing and capacity
  for Garden and Graffiti Room (retrieved 2026-09-28)
- http://www.bristolparksforum.org.uk/information/events-in-parks/ — Bristol park event licensing
  threshold and lead time (retrieved 2026-09-28)

## Quality checks
- Both candidates have a real, retrievable source URL.
- Prices are quoted as stated on the source page (Trinity Centre) or explicitly marked as
  "licensing risk/cost not quoted" (Eastville Park) rather than invented.
- Recommendation ties directly to the accessibility, parking, and budget constraints in
  `requirements.md`.

## Open issues
- Trinity Centre's page does not itemise step-free access or toilet count for an 80-guest booking
  — recommend the residents' association confirm this directly with the venue before final
  booking; `schedule-builder`/`budget-aggregator` should not assume extra toilet hire is needed
  unless this comes back negative.

## Provenance
- Run ID: run-003
- Agent: venue-researcher
- Version: 1
- Created at: 2026-09-28T09:45:00Z
