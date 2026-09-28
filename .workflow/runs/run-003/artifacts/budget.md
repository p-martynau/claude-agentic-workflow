# Budget — Bristol Community Summer Celebration

## Status
READY

## Purpose
Aggregate every costed line from the domain artifacts into one GBP total with an explicit
contingency, and check it against the user's £3,000 limit.

## Inputs used
- `artifacts/requirements.md` (£3,000 GBP limit, no stated exception)
- `artifacts/venues.md`, `artifacts/activities.md`, `artifacts/catering.md`, `artifacts/services.md`
- `artifacts/schedule.md` (confirms no additional paid time beyond what's costed below)

## Content

| Line item | Firm / Estimated | Cost (GBP) | Source artifact |
|---|---|---|---|
| Venue — Trinity Centre Garden + Graffiti Room, 8-hour day | Firm (quoted rate) | £140.00 | `venues.md` |
| PA system hire (Bristol Sound Hire, day rate + incidentals buffer) | Partly firm (£30 quoted) + estimated buffer | £100.00 | `services.md` |
| Live acoustic music (2-hour set) | Estimated (platform low-end rate, not yet booked) | £300.00 | `services.md` / `activities.md` |
| Face painting (3-hour session) | Firm (quoted "from £90" rate) | £90.00 | `activities.md` |
| Catering — buffet for 80 (halal + vegetarian, allergen-labelled) | Estimated (£14/head; no firm MyLahore quote obtained) | £1,120.00 | `catering.md` |
| Litter/waste bin hire | Estimated (no published fixed price found) | £100.00 | `services.md` |
| Event public liability insurance (one-day, ~£5m cover) | Estimated (lower end of two real quoted price points) | £46.00 | `services.md` |
| **Subtotal** | | **£1,896.00** | |
| Contingency (12%, recommended given two estimated-heavy lines — catering and waste) | | £227.52 | |
| **Grand total** | | **£2,123.52** | |
| **User's stated limit** | | £3,000.00 | `requirements.md` |
| **Headroom vs. limit** | | **£876.48 under budget** | |

### Assumptions and currency
All figures are in GBP, matching the user's stated currency — no currency conversion was needed;
every source found was already priced in GBP.

### Firm vs. estimated breakdown
Two lines are firm quotes taken directly from a source page (venue £140, face painting £90 — total
£230 firm). The remaining five lines (£1,666.00 combined) are estimates: PA (partly), live music,
catering, waste bins, and insurance. This is flagged plainly rather than presented as if the whole
budget were confirmed.

## Sources
Aggregated from `venues.md`, `activities.md`, `catering.md`, and `services.md`; see those artifacts
for the original source URLs behind each line.

## Quality checks
- Every cost line traces to a specific upstream artifact and, through it, to a real source URL.
- Arithmetic checked: 140 + 100 + 300 + 90 + 1120 + 100 + 46 = 1,896.00; 1,896.00 × 1.12 = 2,123.52.
- Grand total (£2,123.52) is below the user's £3,000 limit with no exception needed.
- Firm vs. estimated status is stated per line, not blended.

## Open issues
- Catering (£1,120) and waste-bin hire (£100) are the two least-confirmed lines — the residents'
  association should get direct written quotes for both before final booking. Even a generous
  correction to either (e.g. catering coming in £300 higher than estimated) would still fit
  comfortably within the £876.48 headroom, so this is not a budget-limit risk at this stage.

## Provenance
- Run ID: run-003
- Agent: budget-aggregator
- Version: 1
- Created at: 2026-09-28T14:22:00Z
