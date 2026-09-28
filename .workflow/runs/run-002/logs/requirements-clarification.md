# Requirements clarification log — run-002

The original request left several checklist items unstated. The `requirements-formalizer`
inferred conservative defaults for low-risk logistics and asked the synthetic requester directly
for anything that would materially change cost or feasibility. Both are recorded here for
transparency, per `docs/PRACTICAL_TASK.md#3-required-user-requirements`.

## Questions asked to the requester

**Q1. Who is the requester and what company/team is this for (for the plan header only)?**
A1. Alicia Grant, Operations Manager, Northbridge Analytics Ltd (synthetic company for this
demonstration run).

**Q2. Do you have a target date, or is the date flexible?**
A2. Target date: Wednesday 18 November 2026. Some flexibility (+/- one week) if the preferred
venue is unavailable, but 18 Nov is preferred.

**Q3. Is this workshop formal/business-casual, and are there VIP or leadership attendees needing
any special handling (e.g., a keynote slot, reserved seating)?**
A3. Business casual, no VIP staging needed. All 40 participants are treated equally; no head-table
or stage requirement.

**Q4. Beyond vegetarian/vegan/gluten-free, any allergies or other dietary needs (halal, kosher,
nut allergy, etc.)?**
A4. None known beyond vegetarian, vegan, and gluten-free. Requester will confirm allergies with
final headcount closer to the date; caterer should still be asked to confirm allergen handling.

**Q5. Preferred source types for research (e.g., only established platforms, or any bookable
listing is fine)?**
A5. No strong preference — real, currently listed venues/vendors with a working booking or
contact page are acceptable.

**Q6. Desired output format and language?**
A6. English. Markdown working plan plus a standalone HTML guide the team can print or share.

## Items inferred without asking (low risk, stated so a reviewer can check them)

- **Atmosphere:** professional, focused, low-frills — inferred from "internal strategy workshop"
  framing; not separately confirmed.
- **Timezone:** Europe/London — inferred from "Manchester" location.
- **Duration:** 8 hours (09:00–17:00) — explicitly stated by the requester.
- **Guest groups:** all 40 are adult employees; no children, older-adult access needs beyond the
  explicitly stated step-free/parking requirement, or VIPs — inferred from "internal ... workshop"
  and A3.
- **Weather contingency:** not applicable — this is an entirely indoor event, so `weather-researcher`
  is not dispatched for this run (documented in `workflow-state.json` execution plan, which omits
  the weather branch).
- **Activities:** the request does not mention team-building or activities; a single optional
  short energiser slot is included at low/no cost so the "meaningful program" gate has an
  intentional element in the mid-morning segment, per the coordinator's discretion to keep the
  program from being a flat run of back-to-back sessions. This is flagged as an addition, not a
  stated requirement, in `activities.md`.
