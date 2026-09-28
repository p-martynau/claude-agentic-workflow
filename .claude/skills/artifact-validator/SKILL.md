---
name: artifact-validator
description: Reusable structural, completeness, and citation checks for any Event Planner workflow artifact (requirements.md, venues.md, weather.md, activities.md, catering.md, services.md, schedule.md, budget.md, event-plan.md). Use after any agent writes or revises one of these artifacts, before dependent work proceeds.
---

# artifact-validator

Mechanical checks that any subagent or the `validator` agent can run against one artifact file,
before the domain-specific judgement gates (budget limit, schedule feasibility, venue fit, etc.)
are applied by the `validator` agent.

## Input

A single artifact file path under `.workflow/runs/<run-id>/artifacts/`.

## Checks to perform

1. **Structure** — the file has, in order, the exact headings: `# <title>`, `## Status`,
   `## Purpose`, `## Inputs used`, `## Content`, `## Sources`, `## Quality checks`,
   `## Open issues`, `## Provenance`. Flag any missing or reordered section.
2. **Status validity** — `## Status` contains exactly one of `READY`, `NEEDS_REVISION`, `BLOCKED`.
3. **Provenance completeness** — `## Provenance` lists Run ID, Agent, Version, Created at, all
   non-empty.
4. **Non-empty content** — `## Content` is not empty when `## Status` is `READY`.
5. **Source validity** — every external factual claim in `## Content` (a venue, vendor, activity,
   menu item, or price attributed to a real provider) has a corresponding entry in `## Sources`
   that is a real, well-formed URL (starts with `http://` or `https://`, not a placeholder like
   `example.com` or `TODO`). Flag any claim without a matching source.
6. **No unmarked estimates** — any cost, availability, or capacity presented as fact must be
   marked "estimated", "assumed", or "unconfirmed" if the source artifact does not state it as
   firm. Flag unmarked-looking numeric claims that a firm-quote citation does not support.
7. **No internal leakage** — the artifact must not reference hidden prompt files, other agents'
   internal instructions, or secrets/API keys.

## Output

Return a findings list: `{check, result: PASS|FAIL, detail}` for each of the 7 checks above, plus
an overall `PASS`/`FAIL`. The calling agent (typically `validator`) folds this into
`validation-report.md` under the `artifact-structure` and `source-validity` named gates, citing
the specific artifact and the responsible agent (the artifact's `## Provenance` → `Agent` field).
