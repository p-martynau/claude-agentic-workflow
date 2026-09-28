# Services Plan — Bristol Community Summer Celebration

## Status
READY

## Purpose
Plan the vendors/services the confirmed requirements actually call for: PA system, litter/waste
management, live or recorded music, and (flagged by `requirements-formalizer`) event public
liability insurance — with real sourced options, estimated costs, and setup/teardown timing for
`schedule-builder`.

## Inputs used
- `artifacts/requirements.md` (required services: PA system, litter/waste management, live or
  recorded music; inferred need: public liability insurance for an 80-guest public gathering)

## Content

### PA system
**Bristol Sound Hire** — Yamaha PA system package, day rate £30 plus a £400 refundable deposit (no
purchase/loss cost unless equipment is damaged/lost). Setup: allow 30 minutes before the 13:00 open
for a simple self-collect/self-return package; if an operator/mixing is wanted instead of
self-service, budget more (not sourced here — self-service is what this vendor's listed package
covers).
- **Source:** http://bristolsoundhire.weebly.com/ (retrieved 2026-09-28)
- **Estimated line cost (incl. cabling/incidentals buffer):** £100

### Live music
**Last Minute Musicians — Bristol duos & small groups** — acoustic duo/solo listings for Bristol
start from £300 (platform-quoted range £150–£4,056, average £733; £300 is the realistic low end for
a single afternoon set at a community event, and is what is costed here).
- **Source:** https://www.lastminutemusicians.com/search/duos_small_groups/bristol.html (retrieved
  2026-09-28)
- **Estimated line cost:** £300 for a 2-hour set (15:00–17:00), most acts bring their own small PA
  and can play at background or full volume — no separate PA rental conflict.

### Litter / waste management
**McCarthy Marland — event waste management** — offers short-term loan bins/skips for one-off
events. No fixed public price is listed on the page (quote-on-request), so this is costed as an
estimate based on typical short-term event bin hire for a gathering this size.
- **Source:** https://www.mccarthywaste.co.uk/service/event-waste/ (retrieved 2026-09-28)
- **Estimated line cost:** £100 (delivery, 2–3 bins/bags for the afternoon, collection)

### Event public liability insurance (flagged by requirements-formalizer, confirmed needed here)
Most UK venues/councils require a minimum of £5,000,000 public liability cover for a public
gathering of this size; one-day event organiser cover for this level is available from real UK
providers.
- **Source:** https://www.events-insurance.co.uk/event-insurance-policies/one-day-event-insurance
  (quoted from £46.46 for a one-day event-organiser policy) and
  https://www.protectivity.com/product/one-off-event-insurance/ (£31/day quoted for £5m cover,
  plus admin fee and Insurance Premium Tax) (both retrieved 2026-09-28)
- **Estimated line cost:** £46 (using the lower, all-in quoted figure)

### Setup/teardown summary for schedule-builder
| Service | Setup | Teardown |
|---|---|---|
| PA system | 30 min before 13:00 | 15 min after 18:00 |
| Live music | Act's own setup ~20 min before their 15:00 slot | ~15 min after their 17:00 finish |
| Waste bins | Delivered morning of event, before 13:00 | Collected next working day (no same-day teardown needed) |
| Insurance | N/A (administrative, arranged in advance) | N/A |

## Sources
- http://bristolsoundhire.weebly.com/ — PA system package and day rate (retrieved 2026-09-28)
- https://www.lastminutemusicians.com/search/duos_small_groups/bristol.html — Bristol acoustic
  duo/small-group pricing range (retrieved 2026-09-28)
- https://www.mccarthywaste.co.uk/service/event-waste/ — event waste/bin service existence
  (retrieved 2026-09-28)
- https://www.events-insurance.co.uk/event-insurance-policies/one-day-event-insurance and
  https://www.protectivity.com/product/one-off-event-insurance/ — one-day public liability
  insurance pricing (retrieved 2026-09-28)

## Quality checks
- Every service category the requirements actually call for (PA, waste, music) plus the one
  reasonably inferred and flagged category (insurance) has a real sourced option.
- No service was invented that the requirements don't call for (e.g. no security vendor, since
  nothing in requirements indicates a need for one at an 80-guest daytime family event).
- Costs without a firm public quote (waste bins) are explicitly marked "estimated."

## Open issues
- Waste bin hire has no published fixed price; the residents' association should get an exact
  quote from McCarthy Marland (or a comparable local provider) before booking. The £100 estimate
  here is a planning placeholder, not a quote.

## Provenance
- Run ID: run-003
- Agent: services-planner
- Version: 1
- Created at: 2026-09-28T09:55:00Z
