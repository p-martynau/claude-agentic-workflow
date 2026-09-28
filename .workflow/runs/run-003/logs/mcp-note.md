# MCP note — run-003

`.mcp.json` at the repository root configures an **Open-Meteo MCP server**
(`open-meteo-mcp-server@2.5.0`, launched via `npx -y -p open-meteo-mcp-server@2.5.0
open-meteo-mcp-server`), which `weather-researcher` is written to call (`mcp__open-meteo__*`
tools) for real weather data.

## v1/v2 (2026-09-28, first authoring pass): WebFetch fallback

**MCP servers only attach at Claude Code session start.** The session that first authored this
demonstration run did not have the `open-meteo` MCP server attached (it was not part of that
session's startup configuration), so `weather-researcher` could not literally call an
`mcp__open-meteo__*` tool for `weather.md` v1/v2. To still give a real (not fabricated)
demonstration of external weather data, it called the same public Open-Meteo HTTP API that the MCP
server wraps, directly via `WebFetch` (forecast-horizon check plus a single year, 2020-06-01 to
2020-06-10, of the historical archive endpoint). This was real, live, keyless data — just not
routed through the named MCP tool.

## v3 (2026-09-28, same day, corrected): real MCP tool calls

A later review of this repository correctly flagged that using a WebFetch equivalent, rather than
literally invoking an `mcp__open-meteo__*` tool, does not satisfy the brief's requirement that the
configured MCP server be **actually used** in at least one demonstration run
(`docs/PRACTICAL_TASK.md#7-external-research-and-mcp`). By the time of this correction, the
`open-meteo` MCP server *was* attached to the active session (confirmed via a live
`mcp__open-meteo__geocoding` call resolving "Bristol" to real coordinates), so `weather.md` was
revised to v3 using genuine MCP tool calls:

- `mcp__open-meteo__geocoding` — `name: "Bristol"`, `countryCode: "GB"` → 51.45523°N, -2.59665°W.
- `mcp__open-meteo__weather_archive` — six calls, one per year 2019–2024, each for 04–08 June at
  that point, `daily=[temperature_2m_max, temperature_2m_min, precipitation_sum,
  precipitation_hours]`, `timezone=Europe/London`.

This both closes the "MCP configured but not used" gap and, as a side benefit, upgrades the
climatology from one sampled year (2020) to six (2019–2024, 30 day-samples), resolving the
`weather.md` v1/v2 "Open issues" note about single-year sampling. See `artifacts/weather.md` v3 for
the resulting data and `workflow-state.json` for how this revision flowed back through validation,
a new `event-plan.md` v3, and a fresh approval before the final HTML was rewritten.

**Takeaway for future runs:** `weather-researcher` should always attempt the real
`mcp__open-meteo__*` tools first and only fall back to `WebFetch` against the public HTTP API if
the MCP server genuinely isn't attached in that session — and should say so explicitly in its
`## Sources` section either way, so this kind of gap is visible immediately rather than found later
by review.
