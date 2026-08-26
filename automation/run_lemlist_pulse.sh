#!/bin/bash
# lemlist-pulse wrapper: logs Lemlist trial activity for the daily rundown. Never DMs.
exec /usr/bin/python3 "$(cd "$(dirname "$0")" && pwd)/lemlist_pulse.py"
