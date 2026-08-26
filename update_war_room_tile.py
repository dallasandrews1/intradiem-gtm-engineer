#!/usr/bin/env python3
"""
update_war_room_tile.py - inject the morning war-room result into the hub's
War Room tile, in place, between the <!--WARROOM:START--> / <!--WARROOM:END-->
markers in Start_Here_Index.html.

Why a helper instead of hand-editing the HTML: the daily scheduled task should
overwrite exactly one region deterministically, never the surrounding page. This
does a marker-bounded replace, so it is safe to run every morning.

Usage:
    # from a JSON file: [{"priority":"P1","text":"..."}, ...]
    python3 update_war_room_tile.py --json war_room_today.json
    # or inline (pipe): echo '[{"priority":"P1","text":"..."}]' | python3 update_war_room_tile.py -
    # clear back to the empty state:
    python3 update_war_room_tile.py --clear
"""
import json, sys, os, html, datetime, argparse

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = os.path.join(ROOT, "Start_Here_Index.html")
START = "<!--WARROOM:START-->"
END = "<!--WARROOM:END-->"

def esc(s): return html.escape(str(s), quote=True)

def build_tile(items, updated):
    if not items:
        body = '<div class="wrempty">No signals logged yet today.</div>'
        u = "no run yet"
    else:
        rows = []
        for it in items[:5]:
            p = esc(it.get("priority", "P?"))
            t = esc(it.get("text", ""))
            rows.append('<div class="writem"><span class="p">%s</span>%s</div>' % (p, t))
        body = "".join(rows)
        u = "updated " + updated
    return ('%s\n  <div class="warroom">\n'
            '    <div class="wrhd"><span class="t">War Room · what fired overnight</span>'
            '<span class="u">%s</span></div>\n    %s\n  </div>\n  %s'
            % (START, esc(u), body, END))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", nargs="?", help="'-' to read JSON from stdin")
    ap.add_argument("--json", help="path to a JSON file of items")
    ap.add_argument("--clear", action="store_true")
    a = ap.parse_args()

    items = []
    if a.clear:
        items = []
    elif a.json:
        items = json.load(open(a.json, encoding="utf-8"))
    elif a.source == "-":
        items = json.load(sys.stdin)
    else:
        ap.error("give --json FILE, --clear, or pipe JSON with '-'")

    updated = datetime.datetime.now().strftime("%b %-d, %-I:%M%p").lower()
    with open(HUB, encoding="utf-8") as f:
        doc = f.read()
    if START not in doc or END not in doc:
        sys.exit("markers not found in %s" % HUB)
    pre = doc[:doc.index(START)]
    post = doc[doc.index(END) + len(END):]
    # Build the full document BEFORE opening for write: if build_tile raises
    # (e.g. malformed JSON input), the hub must never be left truncated.
    # (Jul 8 2026: the old inline open().write(pre + build_tile(...)) truncated
    # the hub to 0 bytes when build_tile raised; recovered via session replay.)
    new_doc = pre + build_tile(items, updated) + post
    tmp = HUB + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(new_doc)
    os.replace(tmp, HUB)
    print("War Room tile updated (%d signal%s)." % (len(items), "" if len(items) == 1 else "s"))

if __name__ == "__main__":
    main()
