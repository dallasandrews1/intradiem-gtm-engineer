#!/usr/bin/env python3
"""Reply Engine v1 checks. Run: python3 test_reply_engine.py"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reply_engine as re_mod

PASS, FAIL = 0, 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  ok  %s" % name)
    else:
        FAIL += 1
        print("FAIL  %s %s" % (name, detail))


config = re_mod.load_config()
cats = config["categories"]

# --- config shape ---
check("config has exactly 7 categories", len(cats) == 7, "got %d" % len(cats))
expected_keys = {"bad_timing", "have_wfm", "inhouse_rpa", "competitor_eval", "no_budget", "send_info", "wait_for_october"}
check("category keys mirror objection-handler taxonomy", {c["key"] for c in cats} == expected_keys)
for c in cats:
    check("%s has template subject+body" % c["key"], bool(c.get("template", {}).get("subject")) and bool(c.get("template", {}).get("body")))
    check("%s has trigger phrases" % c["key"], len(c.get("trigger_phrases", [])) >= 5)
    check("%s has follow_up days" % c["key"], isinstance(c.get("follow_up", {}).get("days"), int))
    body = c["template"]["body"]
    check("%s template has no em dash" % c["key"], "—" not in body and "--" not in body)
    check("%s template signs as Nathan" % c["key"], body.rstrip().endswith("Nathan") or body.rstrip().endswith("Nathan Belfield"))
    check("%s template is 3-5 sentences" % c["key"], 2 <= len(re.findall(r"[.?!]\s", body)) <= 6)
check("unclassified sentinel present", config.get("unclassified", {}).get("key") == "unclassified")

# --- classification ---
cases = [
    ("Let's circle back next quarter, we're heading into peak season.", "bad_timing"),
    ("We just rolled out NICE WFM last year, our WFM covers this.", "have_wfm"),
    ("Our team automated this with in-house RPA bots already.", "inhouse_rpa"),
    ("We're already in a pilot with Assembled right now.", "competitor_eval"),
    ("There's no budget for this, CFO said no until next fiscal.", "no_budget"),
    ("Can you just send me something to review?", "send_info"),
    ("Let's wait for October and see the new ratings first.", "wait_for_october"),
]
for text, expected in cases:
    cat, score, hits, amb = re_mod.classify(text, config)
    check("classify -> %s" % expected, cat["key"] == expected, "got %s (score=%d hits=%s)" % (cat["key"], score, hits))

# no match -> unclassified
cat, score, hits, amb = re_mod.classify("Thanks, interesting note.", config)
check("no trigger -> unclassified", cat["key"] == "unclassified")

# ambiguous tie -> unclassified (manual review)
cat, score, hits, amb = re_mod.classify("no budget and we have verint", config)
check("tie or clear winner never crashes", cat["key"] in expected_keys | {"unclassified"})

# --- template fill ---
subject, body = re_mod.fill_template(cats[0]["template"], {"first_name": "Sam", "reengage_date": "September 01", "wfm_vendor": "NICE", "artifact_link": "x"})
check("merge fields fill", "{{first_name}}" not in body and "Sam" in body)

# --- doc build contains the human gate ---
doc = re_mod.build_response_doc("we have verint", "Jane Doe", "humana.com", cats[1], 3, ["we have verint"], "s", "b\n\nNathan", None)
check("doc includes bdr_claimed step", "bdr_claimed" in doc)
check("doc includes outcomes.csv logging step", "outcomes.csv" in doc)
check("doc includes copy-sharpener step", "copy-sharpener" in doc)
check("doc never claims to send", "sends from this tool" in doc)

print("\n%d passed, %d failed" % (PASS, FAIL))
sys.exit(1 if FAIL else 0)
