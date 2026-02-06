#!/usr/bin/env python3
"""Generate data/crons.json for Mission Control board from `openclaw cron list`.

Notes:
- `openclaw` CLI sometimes prints non-JSON doctor warnings before JSON.
  We therefore parse from the first '{' or '['.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "data" / "crons.json"


def _load_openclaw_crons() -> dict:
    cmd = ["openclaw", "cron", "list", "--all", "--json"]
    p = subprocess.run(cmd, text=True, capture_output=True)
    s = (p.stdout or "") + ("\n" + p.stderr if p.stderr else "")

    # Extract JSON payload (skip any leading warnings)
    start_obj = s.find("{")
    start_arr = s.find("[")
    starts = [i for i in (start_obj, start_arr) if i != -1]
    if not starts:
        raise RuntimeError(f"No JSON found in output. Exit={p.returncode}. Output head: {s[:400]!r}")
    start = min(starts)
    payload = s[start:]

    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse JSON: {e}. Payload head: {payload[:400]!r}")

    return data


def main() -> None:
    data = _load_openclaw_crons()
    jobs = data.get("jobs", [])

    crons = []
    for j in jobs:
        schedule = j.get("schedule", {}) or {}
        state = j.get("state", {}) or {}

        if schedule.get("kind") == "cron":
            schedule_str = schedule.get("expr")
            tz = schedule.get("tz")
        elif schedule.get("kind") == "every":
            every_ms = int(schedule.get("everyMs") or 0)
            schedule_str = f"every {every_ms}ms"
            tz = None
        elif schedule.get("kind") == "at":
            schedule_str = schedule.get("at")
            tz = None
        else:
            schedule_str = None
            tz = None

        def _iso(ms):
            if not ms:
                return None
            return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).isoformat()

        crons.append(
            {
                "id": j.get("id"),
                "name": j.get("name") or j.get("id"),
                "enabled": bool(j.get("enabled")),
                "scheduleKind": schedule.get("kind"),
                "schedule": schedule_str,
                "timezone": tz or "America/Detroit",
                "nextRunAt": _iso(state.get("nextRunAtMs")),
                "lastRunAt": _iso(state.get("lastRunAtMs")),
                "lastStatus": state.get("lastStatus"),
                "lastDurationMs": state.get("lastDurationMs"),
                "sessionTarget": j.get("sessionTarget"),
            }
        )

    out = {
        "crons": crons,
        "note": "Auto-generated mirror of OpenClaw cron jobs for Mission Control display. Source of truth is OpenClaw cron scheduler.",
        "lastSyncedAt": datetime.now(timezone.utc).isoformat(),
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2) + "\n")


if __name__ == "__main__":
    main()
