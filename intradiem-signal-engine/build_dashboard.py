#!/usr/bin/env python3
"""
Inject fresh signal data into the dashboard.

Reads data/signals.json (produced by signal_processor.py --output) and replaces
the inlined <script id="signal-data"> block in the dashboard index.html, so the
page shows current numbers with no live server required. Run after regenerating
signals.json.

Usage:
    python signal_processor.py --output data/signals.json
    python build_dashboard.py --html /path/to/intradiem-deploy/index.html

Also copy data/signals.json next to index.html if you want the page to
auto-refresh from it on load (the page fetches ./signals.json when present and
falls back to the inlined data otherwise).
"""
import argparse
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SIGNALS = os.path.join(HERE, "data", "signals.json")


def inject(html_path, signals_path, marker="signal-data"):
    payload = open(signals_path).read().strip()
    n = len(json.loads(payload).get("accounts", []))
    html = open(html_path).read()
    pat = re.compile(
        r'(<script type="application/json" id="' + re.escape(marker) + r'">)(.*?)(</script>)', re.S
    )
    if not pat.search(html):
        raise SystemExit(f'No <script id="{marker}"> marker found in {html_path}')
    html = pat.sub(lambda m: m.group(1) + payload + m.group(3), html)
    open(html_path, "w").write(html)
    print(f"Injected {n} accounts into #{marker} of {html_path}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Inject signal data into the dashboard")
    p.add_argument("--html", required=True, help="path to the dashboard index.html")
    p.add_argument("--signals", default=DEFAULT_SIGNALS)
    p.add_argument("--marker", default="signal-data", help="script block id to inject into")
    args = p.parse_args()
    inject(args.html, args.signals, args.marker)
