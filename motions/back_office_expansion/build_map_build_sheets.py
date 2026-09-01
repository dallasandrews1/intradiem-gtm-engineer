#!/usr/bin/env python3
"""Per-account build sheet for the NEW back-office Sales Navigator Relationship Map (max 30 leads).
Roots = distinct-line top officers; every other lead hangs under the root its function implies (inferred, AM confirms).
Reads the rep set's roster (CANDIDATE rows, optional) + candidates CSV (kept rows). Run with --set <name> (sets/<name>.json)."""
import csv, os, re, html
from collections import defaultdict
from bo_set import load_set
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = load_set(); P = CFG["_paths"]
E = lambda s: html.escape(s or "")
from bo_titles import *
configure(CFG)
# hand-curated placements live in sets/<name>.json (drop / priority / manual_under / title_override / dual / verify)
DROP=CFG["_drop"]
cands=defaultdict(list)
PRIORITY=CFG["_priority"]
MANUAL_UNDER=CFG["_manual_under"]
TITLE_OVERRIDE=CFG["_title_override"]
DUAL=CFG["_dual"]
VERIFY=CFG["_verify"]
COLLISION=CFG["_collision"]   # people already in another live sequence at this account: never on the map, listed on the bench with the reason
SF_DROP=set(); SF_FLAG={}
_sf=P["sf_check"]
if os.path.exists(_sf):
    for r in csv.DictReader(open(_sf)):
        if r["in_salesforce"]=="yes" or (r["in_salesforce"]=="possible" and r["match_confidence"] in ("high","medium")):
            SF_FLAG[(r["account"],r["full_name"])]="IN_SF:already in Salesforce" + (f" (as {r['sf_company'][:30]})" if r.get("sf_company") else "")
        elif r["in_salesforce"]=="possible":
            SF_FLAG[(r["account"],r["full_name"])]=f"same name in Salesforce at {r['sf_company'][:28] or 'unknown company'}; confirm the CRM badge before adding"
COLLIDED=defaultdict(list)
if P["roster"] and os.path.exists(P["roster"]):
    for r in csv.DictReader(open(P["roster"])):
        if r["gate_result"]=="CANDIDATE" and r["linkedin_url"] and r["full_name"] not in DROP and (r["account"],r["full_name"]) not in SF_DROP:
            cands[r["account"]].append({"name":r["full_name"],"title":r["title"],"url":r["linkedin_url"],"src":CFG.get("roster_source_label","Jul 26 pull"),"active":False})
for r in csv.DictReader(open(P["candidates"])):
    if not r["excluded_reason"].strip() and r["full_name"] not in DROP and (r["account"],r["full_name"]) not in SF_DROP:
        if (r["account"],r["full_name"]) in COLLISION:
            COLLIDED[r["account"]].append((r["full_name"],r["title"]+"  ["+COLLISION[(r["account"],r["full_name"])]+"]",r["linkedin_url"])); continue
        cands[r["account"]].append({"name":r["full_name"],"title":r["title"],"url":r["linkedin_url"],"src":(r.get("source") or CFG.get("candidate_default_source","Aug 25 search")).replace(" | in_salesforce",""),"active":(r.get("li_active") or "").lower()=="yes"})
        if "in_salesforce" in (r["source"] or ""): SF_FLAG[(r["account"],r["full_name"])]="IN_SF:already in Salesforce"

# root assignment by function keyword
PHRASES=CFG["phrases"]
def pick_root(c, roots):
    t=c["title"].lower(); f=func(c["title"])
    # a root whose title shares a division phrase with the candidate wins outright
    for ph in PHRASES:
        if ph in t:
            for r in roots:
                if ph in r["title"].lower(): return r["name"]
    if f=="Claims" or "disability" in t:
        for r in roots:
            if "chief operations officer" in r["title"].lower() or "chief operating officer" in r["title"].lower(): return r["name"]
    pref=[]
    if f=="Claims": pref=["claims","operating","administrative"]
    elif f in ("Finance & shared services","Billing, payments & revenue","Fraud, credit & disputes"): pref=CFG.get("root_prefs_finance",["accounting","financial","cfo","shared services","operating","administrative"])
    elif f=="Underwriting operations": pref=["underwriting","operating","claims"]
    elif f=="Administration & supply chain": pref=["administrative","caregiver","operating","accounting"]
    else: pref=CFG.get("root_prefs_generic",["operating","residential","administrative","regional business","cfo","accounting"])
    for p in pref:
        for r in roots:
            if p in r["title"].lower(): return r["name"]
    # no executive on the map runs this function: finance-type functions may sit under a CAO/CFO, everything else becomes its own top card
    if CFG.get("finance_rollup",True) and f in ("Finance & shared services","Billing, payments & revenue","Fraud, credit & disputes"):
        for r in roots:
            if re.search(r"accounting|cfo|financial|finance",r["title"].lower()): return r["name"]
    return ""

md=[CFG["md_title"],CFG["md_intro"]]
rows_out=[]
def words(t): return set(re.findall(r"[a-z]{4}",(t or "").lower()))-{"vice","president","senior","director","head","operations","assistant","managing","global","chief","officer"}
WEIGHT={"operations":1,"finance":1,"tech":1,"regional":1,"group":1,"international":1,"transformation":1}
def wov(a,b):
    return sum(WEIGHT.get(t,2) for t in (a&b))
LVL={"C":0,"EVP":1,"SVP":2,"VP":3,"AVP":4,"Director":5}
OVERFLOW={}
TIE_RR={}
BUILT_PIN={}
_snap=P["snapshot_csv"]
if os.path.exists(_snap):
    for r in csv.DictReader(open(_snap)):
        BUILT_PIN.setdefault(r["account"],{})[r["full_name"]]="" if r["reports_up_to"]=="Top of the map" else r["reports_up_to"]

def select_balanced(cs, cap=30):
    """From-scratch map: distinct-line executives, then the SVP/VP/AVP layer spread across functions, then directors that
    have a manager on the map (max three per manager), lanes 3 and 4 held to three each where the sourcing allows."""
    sen=lambda c: ORDER.get(c["band"],9)
    act=lambda c: 0 if c.get("active") else 1
    chosen=[]
    execs=[c for c in cs if c["band"] in ("C","EVP") and (c["tp"] or is_root(c["title"]))]
    def etier(c):
        t=c["title"].lower()
        if re.search(r"\bcfo\b|chief financial",t) and re.search(r" - |, | for |\blob\b|\bof\b",t): return 3   # line-of-business CFO: never a map root
        if re.search(r"operat|administrat|claims|shared service|service|servicing|payment|processing|head of enterprise|customer",t): return 0
        if re.search(r"financ|cfo|controller",t): return 1
        return 2
    execs.sort(key=lambda c:(etier(c),sen(c),len(c["title"]),act(c),c["name"]))
    _seen=set(); _e=[]
    for c in execs:   # one card per identical officer title (two "Chief Financial Officer" rows are a subsidiary and the parent)
        k=re.sub(r"[^a-z]","",c["title"].lower())
        if k in _seen: continue
        _seen.add(k); _e.append(c)
    execs=[c for c in _e if etier(c)<3] or _e
    ECAP=CFG.get("exec_cap_by_account",{}).get(acct_name,CFG.get("exec_cap",4))
    pri=[c for c in cs if (acct_name,c["name"]) in PRIORITY]   # researched or pinned people always fill a slot, whatever their band
    chosen+=pri
    chosen+=[c for c in execs if c not in chosen][:max(0,ECAP-sum(1 for c in chosen if c["band"] in ("C","EVP")))]
    mids=[c for c in cs if c["band"] in ("SVP","VP","AVP") and c["tp"] and c not in chosen]
    picked0=[c for c in chosen if c["band"] in ("SVP","VP","AVP")]
    dirs=[c for c in cs if c["band"]=="Director" and c["tp"] and c not in chosen]
    for c in mids:
        if (acct_name,c["name"]) in PRIORITY and c not in chosen: chosen.append(c)
    byf=defaultdict(list)
    for c in mids:
        if c not in chosen: byf[c["func"]].append(c)
    for f in byf: byf[f].sort(key=lambda c:(sen(c),-len(c["tp"]),act(c),c["name"]))
    mid_budget=min(len(mids),cap-len(chosen)-min(len(dirs),12))
    picked=list(picked0)
    while len(picked)<mid_budget and any(byf.values()):
        for f in sorted(byf):
            if byf[f] and len(picked)<mid_budget:
                c=byf[f].pop(0); picked.append(c); chosen.append(c)
    # lanes 3 and 4 (workforce planning / product owners, operations technology): three each when the sourcing has them
    for ln in ("Workforce planning & product owners","Operations technology"):
        have=sum(1 for c in chosen if c["lane"]==ln)
        pool=[c for c in mids+dirs if c["lane"]==ln and c not in chosen]
        pool.sort(key=lambda c:(sen(c),act(c),c["name"]))
        for c in pool[:max(0,3-have)]:
            if len(chosen)<cap: chosen.append(c); picked.append(c) if c["band"]!="Director" else None
    per=defaultdict(int)
    for c in chosen:
        if c["band"]=="Director":
            m=[x for x in picked if x["tp"]&c["tp"]]
            if m: per[max(m,key=lambda x:(len(x["tp"]&c["tp"]),-sen(x)))["name"]]+=1
    dirs.sort(key=lambda c:(act(c),-len(c["tp"]),c["name"]))
    for d in dirs:
        if len(chosen)>=cap: break
        if d in chosen: continue
        m=[x for x in picked if x["tp"]&d["tp"]]
        if not m: continue
        best=max(m,key=lambda x:(len(x["tp"]&d["tp"]),-sen(x)))
        if per[best["name"]]>=3: continue
        per[best["name"]]+=1; chosen.append(d)
    if CFG.get("pad_to_cap", True):
        rest=[c for c in cs if c not in chosen and c["tp"] and c["band"] in ("SVP","VP","AVP")]
        rest.sort(key=lambda c:(sen(c),act(c),c["name"]))
        for c in rest:
            if len(chosen)>=cap: break
            chosen.append(c)
    return chosen,[c for c in cs if c not in chosen]

for acct in sorted(cands):
    acct_name=acct
    TIE_RR.clear()
    cs=cands[acct]
    for c in cs:
        c["title"]=TITLE_OVERRIDE.get((acct,c["name"]),c["title"])
        c["band"]=CFG["_band_override"].get((acct,c["name"]),band(c["title"])); c["func"]=func(c["title"]); c["top"]=c["band"]=="C"; c["tp"]=topics(c["title"]); c["lane"]=lane(c["title"])
    if CFG.get("select","gap")=="balanced":
        # from-scratch map (no AM roster, no built base): executives, then the VP layer per function, then directors under them
        nourl=[c for c in cs if not c["url"]] if CFG.get("require_url") else []
        if nourl: OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"]+"  [no LinkedIn URL yet]",d["url"]) for d in nourl)
        cs,over=select_balanced([c for c in cs if c not in nourl])
        if over: OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"],d["url"]) for d in over)
    else:
     # cap at Sales Nav's 30 leads per map: everyone sourced before the roster sweep stays; sweep rows are ranked by
     # (a) whether they sit above an existing lead in the same topic (they close a management gap), then (b) seniority
     built_names=set(BUILT_PIN.get(acct,{}).keys())
     SWEEP_SRC=set(CFG.get("sweep_sources",["Aug 25 VP sweep"]))
     base=[c for c in cs if c["src"] not in SWEEP_SRC or c["name"] in built_names]   # anyone already built in Sales Nav is base, whatever sourced them
     sweep=[c for c in cs if c not in base and (c["tp"] or c["band"] in ("C","EVP","SVP"))]   # a sweep row with no function in its title never fills a map slot
     generic=[c for c in cs if c not in base and c not in sweep]
     if generic: OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"],d["url"]) for d in generic)
     def gap_score(c):
         below=[b for b in base if LVL.get(b["band"],9)>LVL.get(c["band"],9) and (c["tp"]&b["tp"])]
         return (c.get("active",False), len(below)>0, len(below), -ORDER.get(c["band"],9))
     sweep.sort(key=gap_score, reverse=True)
     sweep=[c for c in sweep if (acct,c["name"]) in PRIORITY]+[c for c in sweep if (acct,c["name"]) not in PRIORITY]
     for ln in ("Workforce planning & product owners","Operations technology"):
         have=[c for c in base if c["lane"]==ln]
         need=max(0,3-len(have))
         picks=[c for c in sweep if c["lane"]==ln][:need]
         sweep=picks+[c for c in sweep if c not in picks]
     protected=set(BUILT_PIN.get(acct,{}).keys())   # people Dallas already built in Sales Nav are never trimmed
     if len(base)>30:
         managers={c["under"] for c in base if c.get("under")}
         def keep_score(c):
             return (c["name"] in protected, c["band"] in ("C","EVP","SVP"), c["name"] in managers, c["lane"] in ("Workforce planning & product owners","Operations technology"), -ORDER.get(c["band"],9), c.get("active",False))
         base.sort(key=keep_score, reverse=True)
         OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"],d["url"]) for d in base[30:])
         base=base[:30]
     room=max(0,30-len(base))
     dropped=sweep[room:]
     cs=base+sweep[:room]
     if dropped: OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"],d["url"]) for d in dropped)
    cs.sort(key=lambda c:(ORDER.get(c["band"],9),c["func"],c["name"]))
    # profile check could not find these at the company domain: bench them until Sales Nav confirms (Khamash from the same set was a dead link)
    unv=[c for c in cs if (acct,c["name"]) in VERIFY and c["name"] not in BUILT_PIN.get(acct,{})]
    if unv:
        OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"]+"  [unverified: confirm in Sales Nav]",d["url"]) for d in unv)
        cs=[c for c in cs if c not in unv]
    # manager = the closest higher-level person whose title shares the most topics; else the executive the function implies
    execs=[c for c in cs if c["top"]]
    for c in cs:
        c["under"]=""
        if c["top"]: continue
        higher=[h for h in cs if LVL.get(h["band"],9)<LVL.get(c["band"],9) and (acct,h["name"]) not in CFG["_root_exclude"]]
        scored=[(wov(c["tp"],h["tp"]), len(c["tp"]&h["tp"])/len(c["tp"]|h["tp"]), -(LVL[c["band"]]-LVL[h["band"]]), h) for h in higher if c["tp"]&h["tp"]]
        if CFG.get("specific_overlap_for_vp") and c["band"] in ("SVP","VP"):
            # a VP attaches to an SVP/VP only on a specific shared function; a generic "operations" overlap goes to the executive instead
            GEN={"operations","business_ops","transformation","process","finance"}
            scored=[x for x in scored if x[3]["band"] in ("C","EVP") or (c["tp"]&x[3]["tp"])-GEN]
        if scored and c["band"] in ("Director","AVP"):
            best=max(x[0] for x in scored)
            near=[x for x in scored if x[3]["band"] in ("VP","AVP") and x[0]>=best]
            if near: scored=near   # a director sits under a VP/AVP in the same function when one exists, never straight under an SVP or officer
        if scored:
            scored.sort(key=lambda x:(x[0],x[1],x[2]),reverse=True)
            def tw(t): return set(re.findall(r"[a-z]{3}",(t or "").lower()))-{"the","and","of"}
            top=[x for x in scored if x[:3]==scored[0][:3]]
            t0=tw(scored[0][3]["title"])
            top=[x for x in top if len(tw(x[3]["title"])&t0)/max(1,len(tw(x[3]["title"])|t0))>=0.7]
            if len(top)>1 and len({x[3]["band"] for x in top})==1:
                # tie between same-titled managers: spread the reports across them (a placement, not a fact) and say who else it could be
                names=[x[3]["name"] for x in top]
                TIE_RR.setdefault(tuple(names),0); i=TIE_RR[tuple(names)]; TIE_RR[tuple(names)]+=1
                c["under"]=names[i%len(names)]
                others=[n for n in names if n!=c["under"]]
                c["tie"]="could also be under "+" or ".join(others)
            else:
                c["under"]=scored[0][3]["name"]
        elif c["band"]!="EVP":
            # billing, credit, collections, shared services roll up to the senior finance officer below the CFO when no billing VP exists
            if CFG.get("finance_rollup",True) and c["func"] in ("Billing, payments & revenue","Fraud, credit & disputes","Finance & shared services"):
                fin=[h for h in higher if "finance" in h["tp"] and h["band"]!="C"]
                if fin: c["under"]=max(fin,key=lambda h:(LVL[h["band"]],))["name"]
            if not c["under"]:
                c["under"]=pick_root(c,[e for e in execs if (acct,e["name"]) not in CFG["_root_exclude"]]) if execs else ""
            if not c["under"]:
                same=[h for h in higher if h["func"]==c["func"]]
                if same: c["under"]=max(same,key=lambda h:LVL[h["band"]])["name"]
    names_now={c["name"] for c in cs}
    for c in cs:
        m=MANUAL_UNDER.get((acct,c["name"]))
        if m is not None and (m=="" or m in names_now): c["under"]=m; c.pop("tie",None)   # "" pins a person to the top of the map
    # maps already built in Sales Nav keep the reporting lines Dallas built from (only adds/removes may change)
    if acct in BUILT_PIN:
        names={c["name"] for c in cs}
        for c in cs:
            pinned=BUILT_PIN[acct].get(c["name"])
            if pinned is not None and (pinned=="" or pinned in names): c["under"]=pinned; c.pop("tie",None)
    # same-level "Head of" with a broad remit manages narrower heads beside them (Guardian pattern)
    for c in cs:
        if not CFG.get("peer_head_rule",True): break
        if c["under"] or c["top"] or c["band"] not in ("VP","AVP"): continue
        peers=[h for h in cs if h is not c and h["band"]==c["band"] and not h["under"]==c["name"] and len(h["tp"])>len(c["tp"]) and len(c["tp"]&h["tp"])>=1 and "operations" in h["tp"] and len(h["tp"])>=3]
        if peers: c["under"]=max(peers,key=lambda h:len(h["tp"]))["name"]
    # no more than three near-identical siblings under one manager (same level, same function); senior directors first, rest to the bench
    def sib_key(c): return (c["under"],c["band"],c["func"])
    groups={}
    for c in cs:
        if c["under"] and c["band"] in ("Director","AVP"): groups.setdefault(sib_key(c),[]).append(c)
    trimmed=[]
    has_reports={c["under"] for c in cs if c["under"]}
    for k,g in groups.items():
        keep_n=3-sum(1 for c in g if c["name"] in BUILT_PIN.get(acct,{}))   # built siblings count toward the three
        g=[c for c in g if c["name"] not in has_reports and c["name"] not in BUILT_PIN.get(acct,{})]   # never trim a manager or anyone already built in Sales Nav
        if len(g)>max(0,keep_n):
            g.sort(key=lambda c:(0 if c.get("active") else 1, 0 if re.search(r"senior|sr\.?|executive director",c["title"],re.I) else 1, c["name"]))
            trimmed+=g[max(0,keep_n):]
    if trimmed:
        OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"],d["url"]) for d in trimmed)
        cs=[c for c in cs if c not in trimmed]
    # depths from the tops
    byname={c["name"]:c for c in cs}
    def depth_of(c,seen=()):
        if not c["under"] or c["under"] not in byname or c["name"] in seen: return 0
        return 1+depth_of(byname[c["under"]],seen+(c["name"],))
    for c in cs:
        c["depth"]=depth_of(c)
        if c["under"] and c["under"] not in byname: c["under"]=""
    for c in cs:
        e=c
        while e["under"] and e["under"] in byname: e=byname[e["under"]]
        c["exec"]=e["name"] if e is not c else c["name"]
    def walk(parent,depth,out):
        for c in sorted([x for x in cs if x["under"]==parent and x["depth"]==depth],key=lambda x:(ORDER.get(x["band"],9),x["name"])):
            out.append(c); walk(c["name"],depth+1,out)
    ordered=[]
    for t in sorted([x for x in cs if x["depth"]==0],key=lambda x:(ORDER.get(x["band"],9),x["name"])): ordered.append(t); walk(t["name"],1,ordered)
    for c in cs:
        if c not in ordered: ordered.append(c)
    md.append(f"\n## {acct}: back office map ({len(cs)} leads)\n")
    md.append(f"Map name in Sales Nav: `{acct} - Back Office`\n")
    if CFG.get("account_notes",{}).get(acct): md.append(CFG["account_notes"][acct]+"\n")
    md.append("| # | Lead | Title | Level | Function | Reports up to (inferred) | LinkedIn |")
    md.append("|---|---|---|---|---|---|---|")
    for i,c in enumerate(ordered,1):
        indent="&nbsp;&nbsp;&nbsp;"*c["depth"]
        fv=SF_FLAG.get((acct,c["name"]),""); flag=" (in Salesforce)" if fv.startswith("IN_SF:") else (" (confirm CRM badge)" if fv else "")
        md.append(f"| {i} | {indent}**{c['name']}**{flag} | {c['title']} | {c['band']} | {c['func']} | {c['under'] or 'Top of the map'}{(' ; ' + c['tie']) if c.get('tie') else ''} | {c['url']} |")
        rows_out.append({"account":acct,"map_name":f"{acct} - Back Office","order":i,"depth":c["depth"],"full_name":c["name"],"title":c["title"],"level":c["band"],"function":c["func"],"reports_up_to":c["under"] or "Top of the map","executive":c["exec"],"linkedin_url":c["url"],"source":c["src"],"badge_check":("VERIFY:not found by the profile check; confirm current role" if (acct,c["name"]) in VERIFY else ("VERIFY:two LinkedIn profiles, ours may be the old one; confirm" if (acct,c["name"]) in DUAL else ("VERIFY:"+CFG["_confirm"][(acct,c["name"])] if (acct,c["name"]) in CFG["_confirm"] else SF_FLAG.get((acct,c["name"]),"")))),"li_active":"yes" if c.get("active") else "","note":c.get("tie",""),"lane":c.get("lane","")})
    md.append("\nPaste list for the map search box: " + "; ".join(c["name"] for c in ordered) + "\n")
    _t=[x for x in CFG.get("trim",[]) if x[0]==acct]
    if _t:
        md.append("\n**Removed in review (take off the Sales Nav map if already placed):** "+"; ".join(f"{n} ({why})" for _,n,why in _t)+"\n")
for a,v in COLLIDED.items(): OVERFLOW.setdefault(a,[]).extend(v)
if OVERFLOW:
    md.append("\n## Bench: sourced but not on a map (30-lead cap)\n")
    for a,v in sorted(OVERFLOW.items()):
        md.append(f"\n**{a}** ({len(v)}): " + "; ".join(f"{n} ({t[:40]})" for n,t,u in v))
    with open(P["bench_csv"],"w",newline="") as fh:
        w=csv.writer(fh); w.writerow(["account","full_name","title","linkedin_url"])
        for a,v in sorted(OVERFLOW.items()):
            for n,t,u in v: w.writerow([a,n,t,u])
open(P["build_sheets_md"],"w").write("\n".join(md))
with open(P["build_sheets_csv"],"w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows_out[0].keys())); w.writeheader(); w.writerows(rows_out)
print("\n".join(md))
