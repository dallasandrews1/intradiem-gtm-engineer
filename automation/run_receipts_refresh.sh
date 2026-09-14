#!/bin/bash
# receipts-refresh wrapper (Mondays 7:25 when the plist is loaded; on demand any time). Pure python, no Claude call.
# Drafts the proposed receipts-ledger block into automation/logs; never writes the ledger. Never DMs.
exec /usr/bin/python3 "$(cd "$(dirname "$0")" && pwd)/receipts_refresh.py" "$@"
