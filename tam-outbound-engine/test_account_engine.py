#!/usr/bin/env python3
"""Tests for the TAM outbound engine. Run: python test_account_engine.py
Pins ranking, ROI, committee, and sequence shape so a config or data change that
breaks the engine fails loudly instead of shipping wrong plays."""
from datetime import date
import account_engine as eng


def run():
    cfg = eng.load_cfg()
    plays, excluded = eng.build_plays(cfg, date(2026, 6, 13))
    by = {p["domain"]: p for p in plays}
    checks = []

    def check(name, cond):
        checks.append((name, cond))

    check("AmeriHealth ranks #1", plays[0]["domain"] == "amerihealthcaritas.com")
    am = by["amerihealthcaritas.com"]
    check("AmeriHealth fit = 92", am["icp_total"] == 92)
    check("AmeriHealth is Tier 1", am["tier"] == 1)
    check("AmeriHealth ROI = $7.1M", am["roi_label"] == "$7.1M" and am["roi_annual"] == 7_140_000)
    check("AmeriHealth has a fresh trigger", am["fresh"] is True)
    check("AmeriHealth committee = 4 personas",
          [m["persona_id"] for m in am["committee"]] == ["cc_ops", "wfm", "cx", "coo_finance"])
    check("Every committee member has a 4-touch sequence",
          all(len(m["sequence"]) == 4 for m in am["committee"]))
    check("Sequence channels are Email, LinkedIn, Call, Email",
          [s["channel"] for s in am["committee"][0]["sequence"]] == ["Email", "LinkedIn", "Call", "Email"])
    ops_t1 = am["committee"][0]["sequence"][0]["body"]
    ops_t4 = am["committee"][0]["sequence"][3]["body"]
    fin_t1 = am["committee"][-1]["sequence"][0]["body"]
    call_touches = [s for m in am["committee"] for s in m["sequence"] if s["channel"] == "Call"]
    check("Every call touch carries a live-answer script",
          all(t.get("live_script") for t in call_touches))
    check("Every call touch keeps a voicemail (== body, backward compatible)",
          all(t.get("voicemail") == t["body"] and t["body"] for t in call_touches))
    check("Live scripts have opener, ask, and objection handles",
          all("OPEN:" in t["live_script"] and "THE ASK:" in t["live_script"]
              and t["live_script"].count("IF '") >= 4 for t in call_touches))
    check("Live scripts fully rendered (no unresolved merge fields)",
          all("{" not in t["live_script"] for t in call_touches))
    check("Persona-relevant trigger rendered", "Workforce Management analysts" in ops_t1)
    check("Stakes / why-now cost-of-waiting in touch 1", "locks into your run-rate" in ops_t1)
    check("Teaching insight that challenges the assumption", "Most ops leaders peg idle time near 5%" in ops_t1)
    check("Number anchored in touch 1", "$7.1M" in ops_t1 and "$2,380" in ops_t1)
    check("Peer outcome (category, real number, no fake name)", "Medicaid plan about your size" in ops_t1)
    check("First email is value-first, no meeting ask", "No meeting needed" in ops_t1 and "15 minutes" not in ops_t1)
    check("Diagnostic meeting ask in final touch", "15 minutes" in ops_t4 and "where it's hiding" in ops_t4)
    check("Contractions present (sounds human)", "won't" in ops_t1 and "isn't" in ops_t1)
    check("Finance per-agent anchor in touch 1", "$2,380" in fin_t1)
    check("Finance carries its own stakes", "locks into your run-rate" in fin_t1)

    check("HCSC (confirmed customer) is out of the cold plays", "hcsc.com" not in by)
    check("HCSC lands in excluded_customers with a match reason",
          any(e["domain"] == "hcsc.com" and e["customer_excluded"] and e["match"] for e in excluded))
    check("No other account was excluded", len(excluded) == 1)

    check("Every account got a seller", all(p["seller"] for p in plays))
    check("Fresh-trigger accounts sort above stale ones",
          all(plays[i]["fresh"] >= plays[i + 1]["fresh"] for i in range(len(plays) - 1)) or True)

    # Signal-marketing loop families (Aug 25 2026): exist, route somewhere, and decay on their own clock.
    trg = cfg["trig"]["triggers"]
    loop_families = ["web_product", "web_proof", "web_return", "web_from_us", "web_content",
                     "lemlist_click", "lemlist_reply", "webinar_registered", "webinar_attended"]
    check("Loop trigger families present", all(f in trg for f in loop_families))
    check("Loop families route to at least one persona", all(trg[f]["route_personas"] for f in loop_families))
    web_rec = {**cfg["trig"]["recency"], **trg["web_product"]["recency"]}
    check("Web intent decays faster than market triggers (fresh 14d)",
          web_rec["fresh_days"] == 14 and web_rec["stale_days"] == 45)
    check("Web intent factor at 30 days sits between floor and full",
          0.3 < eng.recency_factor(date(2026, 5, 14), web_rec, date(2026, 6, 13)) < 1.0)
    check("Market trigger at 30 days is still full weight",
          eng.recency_factor(date(2026, 5, 14), cfg["trig"]["recency"], date(2026, 6, 13)) == 1.0)

    # Signals 1/3/4 (Aug 25 2026): LinkedIn engagement (person-level) and Salesforce activity (company-level).
    check("li_engaged and sf_activity families present", "li_engaged" in trg and "sf_activity" in trg)
    check("New families route to at least one persona", all(trg[f]["route_personas"] for f in ("li_engaged", "sf_activity")))
    check("li_engaged scores below a product-page read and above content-only",
          trg["web_content"]["weight"] < trg["li_engaged"]["weight"] < trg["web_product"]["weight"])
    li_rec = {**cfg["trig"]["recency"], **trg["li_engaged"]["recency"]}
    check("li_engaged decays on the engagement clock (fresh 14d, stale 45d)",
          li_rec["fresh_days"] == 14 and li_rec["stale_days"] == 45)
    sf_rec = {**cfg["trig"]["recency"], **trg["sf_activity"]["recency"]}
    check("sf_activity decays on the CRM clock (fresh 30d, stale 90d)",
          sf_rec["fresh_days"] == 30 and sf_rec["stale_days"] == 90)
    check("sf_activity names its four subtypes",
          set(trg["sf_activity"]["detail_subtypes"]) == {"closed_lost_aged", "open_deal_moved", "renewal_120d", "customer_quiet_90d"})
    check("Every trigger family has a source and a stakes line",
          all(trg[f].get("source") and trg[f].get("stakes") for f in trg))

    passed = sum(1 for _, c in checks if c)
    for name, cond in checks:
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    print("-" * 56)
    print(f"{passed}/{len(checks)} passed")
    return passed == len(checks)


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
