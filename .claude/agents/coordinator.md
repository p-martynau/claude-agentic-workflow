---
name: coordinator
description: Orchestration rules and workflow-state.json schema for the Event Planner workflow. Reference document used by /plan-event; not normally invoked as a delegate.
tools: Read, Write, Bash
model: inherit
---

# Coordinator

This agent definition documents the **workflow-state.json schema** and the orchestration
contract enforced by `/plan-event` (`.claude/commands/plan-event.md`). The coordinator role is
played by the top-level session running `/plan-event`, not by a delegated subagent — it owns
sequencing, retries, and approval, and must never author event-planning content itself.

## workflow-state.json schema

```json
{
  "run_id": "run-001",
  "created_at": "2026-01-10T09:00:00Z",
  "updated_at": "2026-01-10T09:42:00Z",
  "original_request": "verbatim user text",
  "requirements_confirmed": true,
  "execution_plan_version": 2,
  "execution_plan": [
    {
      "agent": "requirements-formalizer",
      "depends_on": [],
      "status": "completed"
    },
    {
      "agent": "venue-researcher",
      "depends_on": ["requirements-formalizer"],
      "status": "completed"
    }
  ],
  "artifacts": {
    "requirements.md": {
      "path": "artifacts/requirements.md",
      "version": 1,
      "status": "READY",
      "written_by": "requirements-formalizer",
      "updated_at": "2026-01-10T09:05:00Z"
    }
  },
  "quality_gates": [
    {
      "gate": "budget-limit",
      "artifact": "budget.md",
      "result": "FAIL",
      "finding": "Total with contingency exceeds the stated limit by 12%.",
      "responsible_agent": "budget-aggregator",
      "retry_count": 1,
      "resolved": true,
      "resolved_at": "2026-01-10T09:30:00Z"
    }
  ],
  "approval": {
    "status": "pending",
    "requested_version": null,
    "requested_hash": null,
    "approved_version": null,
    "approved_hash": null,
    "approved_at": null,
    "feedback_history": []
  },
  "output": {
    "final_markdown_path": null,
    "final_html_path": null
  }
}
```

Rules:

- `status` values for plan nodes and artifacts: `pending`, `running`, `completed`, `failed`,
  `blocked`, `skipped`.
- Never write secrets, API keys, or tokens into this file.
- Every artifact write must be reflected here (the `post-write-state` PostToolUse hook does this
  automatically for files under `artifacts/` and `output/`; the coordinator is responsible for
  plan, gates, retries, and approval fields, which the hook does not touch).
- A quality gate's `retry_count` maxes out at 3. At 3 unresolved failures, the affected artifact
  and everything depending on it become `blocked`, and the coordinator must report this plainly to
  the user instead of continuing as if validation passed.
- `approval.status` moves `pending` → `approved` only on the literal token `APPROVE` matched
  against `requested_hash`. Any other reply keeps it `pending` and appends to `feedback_history`.
