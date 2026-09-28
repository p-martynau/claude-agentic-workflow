# Budget — Manchester strategy workshop (v2)

## Status
READY

## Purpose
Re-aggregate every cost line after `services.md` v2 added the previously missing AV
delivery/setup/collection fee (validator finding, `services-fit`, v1). This supersedes budget.md v1.

## Inputs used
- `artifacts/requirements.md` (£6,000 GBP limit)
- `artifacts/venues.md`, `artifacts/catering.md`, `artifacts/services.md` (v2), `artifacts/schedule.md`

## Content

| Line item | Source artifact | Firm / estimated | Cost (GBP) |
|---|---|---|---|
| Venue day hire — King's House Conference Centre | venues.md | Estimated | £480.00 |
| Catering — working lunch (Gold buffet, 40 x £20.95) | catering.md | List price | £838.00 |
| Catering — AM tea/coffee + pastries (40 x £5.00) | catering.md | Estimated | £200.00 |
| Catering — PM tea/coffee + biscuits (40 x £3.00) | catering.md | Estimated | £120.00 |
| AV/equipment — projector + screen (EPG) | services.md | Estimated | £150.00 |
| AV/equipment — wireless mics x2 + PA (EPG) | services.md | Estimated | £220.00 |
| AV/equipment — delivery, setup & collection fee (EPG) | services.md v2 | Estimated | £120.00 |
| **Subtotal** | | | **£2,128.00** |
| Contingency (10%) | — | — | £212.80 |
| **Grand total** | | | **£2,340.80** |

**What changed from v1:** added the £120.00 AV delivery/setup/collection line from `services.md` v2
(the finding from `validation-report.md` v1's `services-fit` FAIL). Subtotal moved from £2,008.00
to £2,128.00; contingency moved from £200.80 to £212.80; grand total moved from £2,208.80 to
£2,340.80.

**Limit check:** £2,340.80 vs. £6,000.00 limit — **£3,659.20 under limit**. The estimates in this
budget (venue day-rate, AM/PM refreshments, all AV lines) are not yet firm vendor quotes; the
margin below the £6,000 limit is intentionally kept as headroom in case firm quotes run higher than
these market-rate estimates.

## Sources
Aggregated from `venues.md`, `catering.md`, and `services.md` v2; each line traces to the source
URLs cited in those artifacts.

## Quality checks
- Every cost line traces to a specific upstream artifact line item, including the newly added fee.
- Arithmetic re-checked: 480 + 838 + 200 + 120 + 150 + 220 + 120 = 2,128.00; 2,128.00 x 0.10 =
  212.80; 2,128.00 + 212.80 = 2,340.80. Correct.
- Total is within the £6,000 limit with the corrected AV cost included.

## Open issues
- All line items remain estimates pending firm vendor quotes (King's House day-rate, Corporate
  Lunch AM/PM add-ons, EPG's three AV lines). None of this is a blocking gap for this plan version,
  but Northbridge Analytics should re-run this arithmetic once firm quotes are in hand.

## Provenance
- Run ID: run-002
- Agent: budget-aggregator
- Version: 2
- Created at: 2026-09-29T10:32:00Z
