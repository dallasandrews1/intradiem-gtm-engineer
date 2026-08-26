#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

PORT="${PORT:-8000}"
URL="http://127.0.0.1:${PORT}/Control_Tower.html"

if lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Preview server already running on $URL"
else
  python3 -m http.server "$PORT" --directory "$ROOT_DIR" >/tmp/control_tower_preview.log 2>&1 &
  sleep 1
  echo "Started preview server at $URL"
fi

open "$URL"
