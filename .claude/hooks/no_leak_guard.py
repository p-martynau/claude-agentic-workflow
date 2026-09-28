#!/usr/bin/env python3
"""PreToolUse hook: blocks writes to user-facing deliverables (the final Markdown/HTML output
under a run's output/ directory) if they contain internal implementation details — workflow
state file paths, hidden-prompt references, or secret-shaped strings (API keys/tokens).
Intermediate artifacts under artifacts/ are internal working documents and are not restricted
by this guard.
"""
import json
import re
import sys

LEAK_PATTERNS = [
    r"workflow-state\.json",
    r"\.workflow/runs/",
    r"\.claude/agents/",
    r"\.claude/hooks/",
    r"\bsk-[A-Za-z0-9]{16,}\b",
    r"\bAKIA[0-9A-Z]{16}\b",
    r"(?i)\bapi[_-]?key\b\s*[:=]\s*\S+",
    r"(?i)\bsecret\b\s*[:=]\s*\S+",
]


def deny(reason: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_input = data.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "") or ""

    if not re.search(r"\.workflow/runs/[^/]+/output/", file_path):
        sys.exit(0)

    # Write uses "content"; Edit uses "new_string" (and MultiEdit an "edits" list).
    content = tool_input.get("content", "") or tool_input.get("new_string", "") or ""
    if not content and isinstance(tool_input.get("edits"), list):
        content = "\n".join(
            e.get("new_string", "") for e in tool_input["edits"] if isinstance(e, dict)
        )

    for pattern in LEAK_PATTERNS:
        m = re.search(pattern, content)
        if m:
            deny(
                "no-leak-guard: user-facing output contains an internal detail or secret-shaped "
                f"string matching /{pattern}/. Remove it before writing this file."
            )
            return

    sys.exit(0)


if __name__ == "__main__":
    main()
