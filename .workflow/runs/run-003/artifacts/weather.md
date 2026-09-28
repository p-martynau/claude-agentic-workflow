# Weather Outlook — Bristol, 6 June 2027

## Status
READY

## Purpose
Provide a weather outlook and a concrete rain contingency for the outdoor 6 June 2027 event in
Bristol, per the user's explicit request for "a real weather check and a solid rain contingency."

## Inputs used
- `artifacts/requirements.md` (location: Bristol, ~51.45°N, -2.58°W; date: Saturday 6 June 2027,
  13:00–18:00; outdoor with required rain contingency)

## Content

### Why this is a seasonal outlook, not a point forecast
6 June 2027 is about 20 months ahead of this run. The Open-Meteo forecast model only returns
skillful daily forecasts roughly 16 days ahead, so a forecast call for a date this far out would
not carry real predictive skill. This artifact is therefore a **climatological seasonal outlook**,
built from real historical data for the same location and time of year, not a forecast, and it
must be re-run closer to the date (within ~2 weeks) for an actual forecast.

### Data used
Location resolved with the `mcp__open-meteo__geocoding` tool: Bristol, UK →
**51.45523°N, -2.59665°W**. Historical daily data for that point, for the five days surrounding
6 June across six recent years (2019–2024), retrieved with six calls to the
`mcp__open-meteo__weather_archive` tool (ERA5 reanalysis, ~5.5 km grid near this point;
`daily=temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_hours`,
`timezone=Europe/London`):

| Date | Max °C | Min °C | Precip (mm) | Precip hours |
|---|---|---|---|---|
| 2019-06-04 | 16.4 | 10.3 | 6.0 | 16 |
| 2019-06-05 | 14.8 | 9.4 | 0.0 | 0 |
| 2019-06-06 | 15.7 | 7.0 | 0.6 | 4 |
| 2019-06-07 | 16.3 | 8.7 | 18.3 | 20 |
| 2019-06-08 | 14.1 | 10.3 | 2.4 | 8 |
| 2020-06-04 | 14.9 | 8.6 | 0.0 | 0 |
| 2020-06-05 | 15.4 | 10.0 | 0.9 | 7 |
| 2020-06-06 | 13.5 | 7.0 | 1.7 | 5 |
| 2020-06-07 | 16.8 | 6.1 | 0.0 | 0 |
| 2020-06-08 | 17.2 | 9.3 | 0.4 | 2 |
| 2021-06-04 | 18.1 | 8.7 | 0.0 | 0 |
| 2021-06-05 | 19.2 | 8.6 | 0.1 | 1 |
| 2021-06-06 | 19.9 | 13.2 | 2.6 | 12 |
| 2021-06-07 | 17.9 | 11.4 | 0.0 | 0 |
| 2021-06-08 | 20.3 | 8.7 | 0.0 | 0 |
| 2022-06-04 | 17.8 | 10.4 | 3.0 | 4 |
| 2022-06-05 | 15.4 | 10.1 | 6.9 | 15 |
| 2022-06-06 | 17.0 | 10.9 | 1.4 | 9 |
| 2022-06-07 | 19.3 | 9.1 | 2.3 | 8 |
| 2022-06-08 | 16.9 | 12.7 | 2.2 | 7 |
| 2023-06-04 | 21.0 | 8.8 | 0.0 | 0 |
| 2023-06-05 | 18.0 | 7.7 | 0.0 | 0 |
| 2023-06-06 | 16.7 | 8.3 | 0.0 | 0 |
| 2023-06-07 | 20.6 | 7.6 | 0.0 | 0 |
| 2023-06-08 | 22.2 | 8.8 | 0.0 | 0 |
| 2024-06-04 | 15.9 | 11.1 | 0.8 | 8 |
| 2024-06-05 | 13.4 | 6.5 | 0.2 | 2 |
| 2024-06-06 | 14.8 | 9.1 | 0.6 | 5 |
| 2024-06-07 | 15.5 | 8.0 | 0.5 | 4 |
| 2024-06-08 | 17.2 | 10.4 | 0.7 | 4 |

Across these 30 day-samples (6 years × 5 days): mean max **17.1°C**, mean min **9.2°C**, range
13.4–22.2°C max; **18 of 30 days (60%) had measurable precipitation** (>0.2mm), averaging 1.7mm/day
across the whole sample, with 2023 fully dry and 2019/2022 the wettest years sampled. This
multi-year sample confirms the earlier single-year check (which had shown 6/10 days with rain, 60%)
was not a fluke, and widens the evidence base from one year to six.

### Outlook for 6 June 2027
**Seasonal expectation (not a forecast):** mild (typically 13–22°C, centred around 17°C by day,
9°C overnight), roughly a **3-in-5 chance of at least light rain** during the day based on the
6-year historical record, low chance of severe weather. **This must be replaced with an actual
short-range forecast once the date is within ~2 weeks out.**

### Contingency plan
Given the outlook above and the venue researched in `venues.md`:

- The recommended venue (Trinity Centre) already includes an **indoor room on the same site**
  (Graffiti Room, capacity 100 standing/60 seated) as part of the £140/day combined booking — this
  is a real, already-costed wet-weather space, not a hypothetical add-on.
- **Contingency trigger:** if the Met Office/Open-Meteo short-range forecast checked 48 hours
  before the event shows ≥50% precipitation probability during 13:00–18:00, the event moves indoors
  to the Graffiti Room from the start; if rain arrives unexpectedly on the day, the on-site move
  takes minutes since both spaces are in the same building.
- Lighter/uncertain forecasts: keep the programme outdoors with the PA system and any electrical
  equipment under cover (see `services.md`), and treat the Graffiti Room as available for guests to
  step into at any time during the event, not only as an all-or-nothing switch.

### Who decides, and what guests are told (added in v2, per rejection feedback on v1)
v1 of this artifact named a trigger threshold but did not say, in plain terms, who acts on it or
what guests are told. This is now made concrete:

- **Decision-maker:** the residents' association's named on-the-day event lead (the same person
  who signs off setup at 11:00 in `schedule.md`) makes the go/no-go call, using the 11:00 forecast
  check plus their own judgement of conditions on site. No other role is authorised to reverse a
  "move indoors" call once announced, to avoid guests getting conflicting instructions.
- **Guest communication if the event moves indoors before opening:** a single announcement is
  posted at the Garden's entrance and on the residents' association's usual community noticeboard
  channel by 12:30 at the latest, reading: *"Due to the weather forecast, today's celebration is
  moving indoors to the Graffiti Room at Trinity Centre — same building, same start time, 13:00."*
- **Guest communication if rain starts mid-event:** the event lead makes one PA announcement
  ("We're moving inside to the Graffiti Room — please make your way through the main door"), and
  volunteers posted at the Garden's two access points redirect guests and help anyone with a
  pushchair or mobility needs move first.
- **Threshold for a mid-event move (not just before opening):** sustained rain (not a brief
  shower) for more than 10 minutes, or any rain heavy enough to affect the PA equipment or food
  safety on the buffet table, triggers the move — this is a deliberately low bar, since the indoor
  room costs nothing extra to use (already booked) and the downside of staying out too long is
  worse than the downside of moving early.

## Sources
- `mcp__open-meteo__geocoding` tool call, `name="Bristol"`, `countryCode="GB"` — resolved
  51.45523°N, -2.59665°W (retrieved 2026-09-28).
- `mcp__open-meteo__weather_archive` tool, six calls for 04–08 June of 2019, 2020, 2021, 2022,
  2023, and 2024 at that point — the historical data table above (retrieved 2026-09-28). This is
  the configured Open-Meteo MCP server (see `.mcp.json`), called directly as a tool in this
  session — not a WebFetch fallback. See `logs/mcp-note.md` for the history of why v1/v2 of this
  artifact had used a WebFetch fallback instead, and why v3 was able to switch to the real MCP
  tool.

## Quality checks
- Clearly labelled as a seasonal outlook, not a forecast, with the reasoning shown.
- Real MCP tool responses quoted, not invented figures.
- Contingency is concrete (named indoor room, named trigger threshold, named re-check timing) —
  not a generic "move indoors if it rains."
- Historical sample widened from one year to six (30 day-samples) so the rain-probability estimate
  is not based on a single potentially unrepresentative year.

## Open issues
- This outlook must be refreshed with a real short-range forecast once the event date is within
  ~2 weeks, and the trigger threshold re-confirmed against that forecast.
- The named "event lead" role is a placeholder for whichever named individual the residents'
  association assigns before the day; this artifact does not invent a specific person's name.

## Provenance
- Run ID: run-003
- Agent: weather-researcher
- Version: 3
- Created at: 2026-09-28T15:20:00Z
- Revision reason: v2 (decision-maker/communication detail) is unchanged in substance; v3 replaces
  v1/v2's WebFetch-sourced single-year data with real `mcp__open-meteo__*` MCP tool calls and a
  six-year historical sample, per a post-approval compliance review that found the MCP server,
  while configured, had not actually been called by name in this run. See `logs/mcp-note.md`.
