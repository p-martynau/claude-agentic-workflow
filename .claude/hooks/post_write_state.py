#!/usr/bin/env python3
"""PostToolUse hook: after a Write succeeds under a run's artifacts/ or output/ directory,
update workflow-state.json with that artifact's path, parsed Status, version, and timestamp.
Best-effort and non-blocking: PostToolUse cannot block the tool call, and a bookkeeping failure
here must never be reported as a workflow failure.
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_input = data.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "") or ""

    match = re.search(
        r"\.workflow/runs/([^/]+)/(artifacts|output)/([^/]+)$", file_path
    )
    if not match:
        sys.exit(0)

    run_id, kind, filename = match.groups()
    cwd = Path(data.get("cwd", "."))
    run_dir = cwd / ".workflow" / "runs" / run_id
    state_path = run_dir / "workflow-state.json"
    if not state_path.is_file():
        sys.exit(0)

    try:
        state = json.loads(state_path.read_text())
    except Exception:
        sys.exit(0)

    status = "READY"
    try:
        text = Path(file_path).read_text()
        m = re.search(r"^##\s*Status\s*\n\s*(READY|NEEDS_REVISION|BLOCKED)", text, re.MULTILINE)
        if m:
            status = m.group(1)
    except Exception:
        pass

    artifacts = state.setdefault("artifacts", {})
    existing = artifacts.get(filename, {})
    artifacts[filename] = {
        "path": f"{kind}/{filename}",
        "version": existing.get("version", 0) + 1,
        "status": status,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    state["updated_at"] = datetime.now(timezone.utc).isoformat()

    try:
        state_path.write_text(json.dumps(state, indent=2) + "\n")
    except Exception:
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()
