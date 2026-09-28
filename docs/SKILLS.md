# Skills

Two reusable skills live under [`.claude/skills/`](../.claude/skills/). Skills are invoked by the
workflow itself (not just stored in the repo) — see the usage points below and their real
invocations in [`RUNS.md`](RUNS.md).

## `artifact-validator`

[`.claude/skills/artifact-validator/SKILL.md`](../.claude/skills/artifact-validator/SKILL.md)

Mechanical, reusable checks run against any single artifact before dependent work proceeds:

- heading structure matches the shared contract exactly;
- `## Status` is one of `READY` / `NEEDS_REVISION` / `BLOCKED`;
- `## Provenance` is complete (Run ID, Agent, Version, Created at);
- `## Content` is non-empty when `## Status` is `READY`;
- every external factual claim has a matching real-URL entry in `## Sources`;
- estimates/assumptions are marked as such, not presented as firm facts;
- no internal-implementation or secret leakage in the artifact.

**Input:** one artifact file path. **Output:** a `{check, result, detail}` list plus an overall
PASS/FAIL, folded by the `validator` agent into `validation-report.md` under the
`artifact-structure` and `source-validity` named gates.

## `event-plan-html-theme`

[`.claude/skills/event-plan-html-theme/SKILL.md`](../.claude/skills/event-plan-html-theme/SKILL.md)

The rendering rules and template contract for the final standalone HTML guide: inline CSS only (no
external requests), a section per plan area (overview, venue, schedule, activities, catering,
services, budget, weather/contingency, sources), schedule and budget as tables, real source links,
and a `@media print` block for clean printing. No JavaScript.

**Input:** the approved `event-plan.md`, split into its sections. **Output:**
`output/event-plan.html`. **Used exclusively by** `html-builder`, and only after the
`approval-gate-guard` hook (see [`HOOKS.md`](HOOKS.md)) has permitted the write.
