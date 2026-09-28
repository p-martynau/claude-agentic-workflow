# Budget — 8th Birthday Party (run-001)

## Status
READY

## Purpose
Aggregate every cost line from the domain artifacts into one GBP total, add a contingency line, and
show the result against the requester's fixed £1,200 limit.

## Inputs used
- `artifacts/requirements.md` (currency GBP, fixed all-inclusive ceiling £1,200, contingency to be
  included within the ceiling, not on top)
- `artifacts/venues.md`, `artifacts/activities.md`, `artifacts/catering.md`, `artifacts/services.md`,
  `artifacts/schedule.md`

## Content

| Line item | Amount (GBP) | Firm / Estimated | Source artifact |
|---|---|---|---|
| Venue hire — Magdalen Hall Main Hall, 6 hours @ £35/hr | £210.00 | Estimated (source gives a "from" rate; two pages differ £32 vs £35, higher figure used) | venues.md |
| Children's entertainer (45–60 min show) | £150.00 | Estimated (marketplace "from" price for a mid-range named act) | activities.md |
| Decoration — number-8 balloon bouquet + latex bunch | £90.00 | Estimated ("from" prices) | services.md |
| Party extras — pass-the-parcel prizes + craft supplies | £20.00 | Estimated (commodity items) | services.md, activities.md |
| Catering — M&S Kids Sandwich Platter ×2 (16pc each) | £20.00 | Firm (quoted product price) | catering.md |
| Catering — M&S Vegetarian Sandwich & Wrap Selection ×1 (20pc) | £17.50 | Firm (quoted product price) | catering.md |
| Catering — Just Love Food Co. nut-free Happy Birthday Cake ×2 | £18.00 | Firm (quoted product price) | catering.md |
| Catering — crisps/fruit/snack bowls | £30.00 | Estimated (commodity items) | catering.md |
| Beverages — juice cartons, squash, tea/coffee | £25.00 | Estimated (commodity items) | catering.md |
| **Subtotal** | **£580.50** | — | — |
| Contingency (10% of subtotal, per `requirements.md` guidance and default recommendation) | £58.05 | Explicit contingency line | budget-aggregator |
| **Grand total** | **£638.55** | — | — |
| **Requester's fixed limit** | **£1,200.00** | — | requirements.md |
| **Headroom under limit** | **£561.45 (≈47% of the budget unused)** | — | — |

### Arithmetic check
£210.00 + £150.00 + £90.00 + £20.00 + £20.00 + £17.50 + £18.00 + £30.00 + £25.00 = **£580.50**
subtotal. £580.50 × 0.10 = £58.05 contingency. £580.50 + £58.05 = **£638.55** grand total.
£1,200.00 − £638.55 = **£561.45** headroom. Verified by direct addition (see
`logs/execution-log.md` for the coordinator's cross-check note).

### Notes on scope of the total
- The Magdalen Hall **£250 refundable booking deposit** (`venues.md`) is a deposit, not a net
  spend, and is excluded from the total above; it is a cash-flow consideration for the family, not
  a budget-limit concern.
- Every firm price traces to a specific product listing in `catering.md`; every estimated price is
  explicitly labelled as such and traces to a "from" rate in `venues.md`, `activities.md`, or
  `services.md`.

## Sources
Aggregated from `venues.md`, `activities.md`, `catering.md`, and `services.md`; see those artifacts
for the underlying source URLs.

## Quality checks
- Every cost line traces to a specific upstream artifact and, through it, to a real source URL
  (except clearly labelled commodity/generic estimates, which do not claim a specific vendor).
- Arithmetic re-checked by direct addition; grand total £638.55 is correctly computed from the nine
  line items plus 10% contingency.
- Grand total (£638.55) is well within the requester's £1,200 fixed ceiling — **budget-limit gate
  passes with substantial headroom (≈47%)**, not just a narrow pass.
- Contingency is included within the £1,200 ceiling, not added on top, per the confirmed
  requirement.

## Open issues
- The £561.45 headroom means the family has room to upgrade (e.g., a longer entertainer booking, a
  larger/firmer-quoted venue booking, or professional catering instead of supermarket platters) and
  still stay under budget — this is noted as an opportunity, not a defect.
- Several line items are "from" estimates rather than firm quotes (venue, entertainer, decoration);
  the 10% contingency provides some headroom against modest overruns in those lines, but a large
  jump in any one of them (e.g., choosing a premium entertainer act at £300+) could still fit within
  the remaining £561.45 headroom without breaching the £1,200 limit.

## Provenance
- Run ID: run-001
- Agent: budget-aggregator
- Version: 1
- Created at: 2026-09-28T09:55:00Z
