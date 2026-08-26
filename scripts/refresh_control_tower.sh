#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

python3 build_control_tower.py

if command -v osascript >/dev/null 2>&1; then
  osascript -e 'tell application "System Events" to keystroke "r" using {command down}' >/dev/null 2>&1 || true
fi

echo "Refreshed control tower snapshot"
