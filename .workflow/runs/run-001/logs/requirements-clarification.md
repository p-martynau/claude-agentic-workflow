# Requirements clarification log — run-001

Agent: `requirements-formalizer`. This log records the clarification questions asked before
`artifacts/requirements.md` was written, and the requester's confirmation.

## Q&A

**Q1. Which part of London (or which travel pattern) should the venue search focus on, and is a
short taxi/tube ride from home acceptable, or does it need to be walkable?**
A1: No fixed home area given. Requester confirmed: search across Greater London broadly, prioritise
venues within easy reach of a London Underground/Overground/rail station (a few minutes' walk) or
with on-site/nearby parking, since guests are travelling from different parts of London.

**Q2. Is the £1,200 an all-inclusive ceiling (venue + activities + food + services + contingency),
and should a 10% contingency be carved out of it or added on top?**
A2: Requester confirmed £1,200 is an all-inclusive fixed ceiling. A contingency line should be
included *within* the £1,200, not added on top — i.e., the sum of venue + activities + catering +
services + contingency must not exceed £1,200.

**Q3. Beyond the nut-allergy and vegetarian requirement, are there other dietary needs (e.g.
gluten-free, halal), and is alcohol required for the parents attending?**
A3: Requester confirmed no other known dietary needs beyond "at least one vegetarian option and one
nut-free/nut-allergy-safe option" for the mixed children+parents group. No alcohol required; soft
drinks/juice for children and tea/coffee for parents is sufficient.

## Confirmation

The requester (synthetic, for demonstration) reviewed the resulting `artifacts/requirements.md`
(version 1) and replied with the literal token `CONFIRM` at 2026-09-28T09:20:00Z. Requirements were
then locked for planning; `workflow-state.json.requirements_confirmed` was set to `true`.
