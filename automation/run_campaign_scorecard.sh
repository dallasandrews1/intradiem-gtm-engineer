#!/bin/bash
# campaign-scorecard wrapper (on demand; the hourly lemlist relay also chains it after the pulse).
# Read-only lemlist read, 0 Clay credits, never DMs. Writes logs/campaign-scorecard-<date>.md,
# logs/campaign_scorecard_history.csv, logs/receipts_candidates.csv (append) and the council CSV.
exec /usr/bin/python3 "$(cd "$(dirname "$0")" && pwd)/campaign_scorecard.py" "$@"
