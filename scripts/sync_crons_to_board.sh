#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

python3 scripts/gen_crons_json.py

# Only commit/push if file changed
if git diff --quiet -- data/crons.json; then
  echo "No changes in data/crons.json"
  exit 0
fi

git add data/crons.json

git commit -m "Auto-sync crons.json from OpenClaw cron scheduler" || true

git push
