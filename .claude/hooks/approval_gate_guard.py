#!/usr/bin/env python3
"""PreToolUse hook: blocks writing the final event-plan HTML unless workflow-state.json
records an explicit approval matching the current event-plan.md hash. Fails safe: any
error or missing evidence of approval blocks the write.
"""
import hashlib
import json
import re
import sys
from pathlib import Path


def deny(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def allow() -> None:
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        deny("approval-gate-guard: could not parse hook input; blocking to fail safe.")
        return

    tool_input = data.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "") or ""

    # Only this hook's concern: the final rendered HTML guide under a run's output/ dir.
    match = re.search(r"\.workflow/runs/([^/]+)/output/event-plan\.html$", file_path)
    if not match:
        allow()
        return

    run_id = match.group(1)
    cwd = Path(data.get("cwd", "."))
    run_dir = cwd / ".workflow" / "runs" / run_id
    state_path = run_dir / "workflow-state.json"
    plan_path = run_dir / "artifacts" / "event-plan.md"

    if not state_path.is_file():
        deny(f"approval-gate-guard: no workflow-state.json for {run_id}; final HTML is blocked.")
        return

    try:
        state = json.loads(state_path.read_text())
    except Exception:
        deny("approval-gate-guard: workflow-state.json is unreadable; blocking to fail safe.")
        return

    approval = state.get("approval", {}) or {}
    if approval.get("status") != "approved":
        deny(
            "approval-gate-guard: event-plan.md has not received an explicit APPROVE for the "
            "current version. Request approval before writing the final HTML."
        )
        return

    approved_hash = approval.get("approved_hash")
    if not approved_hash:
        deny("approval-gate-guard: approval record has no approved_hash; blocking to fail safe.")
        return

    if not plan_path.is_file():
        deny("approval-gate-guard: artifacts/event-plan.md is missing; blocking to fail safe.")
        return

    current_hash = hashlib.sha256(plan_path.read_bytes()).hexdigest()
    if current_hash != approved_hash:
        deny(
            "approval-gate-guard: event-plan.md has changed since approval "
            f"(approved {approved_hash[:12]}..., current {current_hash[:12]}...). "
            "Re-request approval for the new version before writing the final HTML."
        )
        return

    allow()


if __name__ == "__main__":
    main()
