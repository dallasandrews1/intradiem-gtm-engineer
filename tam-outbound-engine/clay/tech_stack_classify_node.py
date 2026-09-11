ACD = {"NICE CXone":"NICE","NICE inContact":"NICE","Five9":"Five9","Genesys":"Genesys","Genesys Cloud":"Genesys","Genesys Cloud CX":"Genesys","Amazon Connect":"Amazon Connect","TalkDesk":"Talkdesk","Talkdesk":"Talkdesk","Avaya":"Avaya","Avaya Aura":"Avaya","Avaya CentreVu Supervisor":"Avaya","Avaya Call Management System":"Avaya","Avaya Experience Portal":"Avaya","Cisco Unified Contact Center":"Cisco","Webex Contact Center":"Cisco","RingCentral":"RingCentral"}
WFM = {"NICE Workforce Management":"NICE","NICE IEX":"NICE","NICE":"NICE","Verint":"Verint","Verint Workforce Management":"Verint","Calabrio":"Calabrio","Calabrio ONE":"Calabrio","Aspect Workforce Management":"Aspect","Alvaria":"Aspect"}

ACD_L = {k.lower(): v for k, v in ACD.items()}
WFM_L = {k.lower(): v for k, v in WFM.items()}


def handler(context):
    r = context.get_input("tech") or {}
    techs = r.get("technologies") or []
    domain = context.get_input("domain") or r.get("domain") or ""
    def best(table):
        top = None
        for t in techs:
            title = (t.get("title") or "").lower()
            if title not in table:
                continue
            seen = (t.get("last_seen_at") or "")[:10]
            score = float(t.get("score") or 0)
            key = (seen, score)
            if top is None or key > top[3]:
                top = (table[title], seen, title, key)
        return top
    acd, wfm = best(ACD_L), best(WFM_L)
    def known(t): return (t.get("title") or "").lower() in ACD_L or (t.get("title") or "").lower() in WFM_L
    allhits = sorted({(t.get("title") or "") for t in techs if known(t)})
    latest_seen = max([(t.get("last_seen_at") or "")[:10] for t in techs if known(t)] or [""])
    return {
        "domain": domain,
        "cc_platform_latest": acd[0] if acd else "",
        "cc_platform_last_seen": acd[1] if acd else "",
        "wfm_platform_latest": wfm[0] if wfm else "",
        "cc_platforms_all": ", ".join(f"{h} ({next(((t.get('last_seen_at') or '')[:10] for t in techs if t.get('title')==h), '')})" for h in allhits),
        "latest_seen": latest_seen,
        "has_read": bool(acd or wfm),
        "read_date": _today(),
        "read_status": ("read: " + "/".join(x for x in ((acd[0] if acd else ""), (wfm[0] if wfm else "")) if x)) if (acd or wfm) else "read: none found",
    }


def _today():
    """The workflow runtime has no datetime module. Blank is acceptable; the queues drain on read_status."""
    try:
        import time
        return time.strftime("%Y-%m-%d")
    except Exception:
        return ""
