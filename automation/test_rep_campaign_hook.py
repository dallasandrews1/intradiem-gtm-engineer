#!/usr/bin/env python3
"""Tests for rep_campaign_hook's address-pattern checks.

The fixtures are REAL rows: the six ST Water leads Jack hand-loaded on Sep 3 2026 (four
bounced the next morning), their corrected forms, and defects found in his BA Test campaign.
The suite is the regression guard that the hook still catches the failure it was built for.

Run: python3 automation/test_rep_campaign_hook.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rep_campaign_hook import pattern_flags, li_slug, norm, slugify  # noqa: E402


def row(who, email, first, last):
    return {"who": who, "email": email, "first_name": first, "last_name": last}


CASES = [
    ("ST Water as loaded (Cawley reversed, Martin-Rerrie collapsed, Burditt pattern-correct)", [
        row("Stephanie Cawley", "cawley.stephanie@severntrent.co.uk", "Stephanie", "Cawley"),
        row("Jodie Bowen", "jodie.bowen@severntrent.com", "Jodie", "Bowen"),
        row("Deborah Martin-Rerrie", "deborah.martinrerrie@severntrent.co.uk", "Deborah", "Martin-Rerrie"),
        row("Jude Burditt", "jude.burditt@severntrent.co.uk", "Jude", "Burditt"),
        row("Michelle Lancaster", "michelle.lancaster@severntrent.co.uk", "Michelle", "Lancaster"),
        row("Joe Liburd", "joe.liburd@severntrent.co.uk", "Joe", "Liburd"),
    ], 2),
    ("ST Water after the Sep 4 fix (must be silent)", [
        row("Stephanie Cawley", "stephanie.cawley@severntrent.co.uk", "Stephanie", "Cawley"),
        row("Jodie Bowen", "jodie.bowen@severntrent.co.uk", "Jodie", "Bowen"),
        row("Deborah Martin-Rerrie", "deborah.martin-rerrie@severntrent.co.uk", "Deborah", "Martin-Rerrie"),
    ], 0),
    ("False-positive guard: nickname both directions, multi-word surname, apostrophe surname, middle initial", [
        row("Nathan Belfield", "nathan.belfield@intradiem.com", "Nathan", "Belfield"),
        row("Pieter Van Vliet", "pieter.van.vliet@achmea.nl", "Pieter", "Van Vliet"),
        row("Phil Coole", "philip.coole@lv.com", "Phil", "Coole"),
        row("Philip Hunt", "phil.hunt@ba.com", "Philip", "Hunt"),
        row("Daniel Okafor", "dan.okafor@ba.com", "Daniel", "Okafor"),
        row("Finola O'Sullivan", "finola.osullivan@ba.com", "Finola", "O'Sullivan"),
        row("Debbie Rankin", "debbie.a.rankin@hsbc.com", "Debbie", "Rankin"),
    ], 0),
    ("Nickname tolerance must NOT excuse a wrong surname (token match, not substring)", [
        row("Philip Hunt", "phil.hunter@ba.com", "Philip", "Hunt"),
        row("Jane Wood", "jane.woods@ba.com", "Jane", "Wood"),
        row("Ann Smith", "ann.smithers@ba.com", "Ann", "Smith"),
    ], 3),
    ("Whole name run together with no separator is a normal form, must be clean", [
        row("Jodie Bowen", "jodiebowen@severntrent.co.uk", "Jodie", "Bowen"),
    ], 0),
    ("BA Test real defects: misspelled local part, one person with two addresses", [
        row("Jonathan Foster", "johnathan.foster@ba.com", "Jonathan", "Foster"),
        row("Steven Ellis", "steven.ellis@ba.com", "Steven", "Ellis"),
        row("Steven Ellis", "steven.1.ellis@ba.com", "Steven", "Ellis"),
    ], 2),
    ("Rows with no email must never raise", [
        row("No Email", "", "No", "Email"),
        row("Url Only", "", "Url", "Only"),
    ], 0),
]

HELPERS = [
    ("li_slug full url", li_slug("https://www.linkedin.com/in/jodie-bowen-7676534a/"), "in/jodie-bowen-7676534a"),
    ("li_slug empty", li_slug(""), ""),
    ("norm strips punctuation", norm("Martin-Rerrie"), "martinrerrie"),
    ("slugify caps at four words", slugify("UK - Named Accounts / Prospect Clinic (Jack)"), "uk-named-accounts-prospect"),
]


def main():
    failures = 0
    for label, rows, expect in CASES:
        got = pattern_flags(rows)
        ok = len(got) == expect
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'} {label}: {len(got)} flags, expected {expect}")
        for f in got:
            print(f"       {f}")
    for label, got, expect in HELPERS:
        ok = got == expect
        failures += 0 if ok else 1
        print(f"{'PASS' if ok else 'FAIL'} {label}: {got!r}" + ("" if ok else f", expected {expect!r}"))
    total = len(CASES) + len(HELPERS)
    print(f"\n{total - failures}/{total} checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
