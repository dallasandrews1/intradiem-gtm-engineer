#!/usr/bin/env python3
"""Per-account build sheet for the NEW back-office Sales Navigator Relationship Map (max 30 leads).
Roots = distinct-line top officers; every other lead hangs under the root its function implies (inferred, AM confirms).
Reads BO_AccountMap_Roster_Inger.csv (CANDIDATE rows) + inger_backoffice_candidates.csv (kept rows)."""
import csv, os, re, html
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
E = lambda s: html.escape(s or "")
ORDER = {"C":0,"EVP":1,"SVP":2,"VP":3,"AVP":4,"Director":5}
def band(t, hint=""):
    t=re.sub(r"\s+"," ",(t or "").lower().replace("-"," ").replace("(avp)","avp"))
    if re.search(r"\b(associate vice president|assistant vice president|avp)\b",t): return "AVP"
    if re.search(r"\b(evp|executive vice president)\b",t): return "EVP"
    if re.search(r"\b(svp|senior vice president|sr\.? vice president)\b",t): return "SVP"
    if re.search(r"\b(chief|ceo|coo|cfo|cao|president)\b",t) and not re.search(r"vice president",t): return "C"
    if re.search(r"\bmanaging director\b",t): return "VP"
    if re.search(r"\b(avp|assistant vice president)\b",t): return "AVP"
    if re.search(r"\b(vp|vice president|head of|global head)\b",t): return "VP"
    if re.search(r"\b(director|executive director)\b",t): return "Director"
    return hint or "Director"
def func(t):
    t=(t or "").lower()
    if re.search(r"claim",t): return "Claims"
    if re.search(r"fraud|credit|collection|recovery|dispute",t): return "Fraud, credit & disputes"
    if re.search(r"billing|payment|treasury|revenue cycle|patient financial|order management|revenue ops",t): return "Billing, payments & revenue"
    if re.search(r"shared service|accounting|controller|comptroller|finance|fp&a|financial",t): return "Finance & shared services"
    if re.search(r"underwriting",t): return "Underwriting operations"
    if re.search(r"supply chain|procurement|hr |human resources|facilit|administrat",t): return "Administration & supply chain"
    return "Operations"
LANES=[("Operations executives", r"\b(chief|coo|cfo|cao|evp|executive vice president|svp|senior vice president|head of operations)\b|(?<!vice )(?<!vice-)\bpresident\b"),
 ("Workforce planning & product owners", r"workforce|capacity planning|product owner|head of product|scheduling"),
 ("Operations technology", r"operations technology|technology operations|business systems|claims technology|claims systems|operations platform|systems implementation|business technology|application"),
 ("Operations leaders", r".")]
def lane(t):
    tl=(t or "").lower()
    for name,rx in LANES:
        if re.search(rx,tl): return name
    return "Operations leaders"
def is_root(t):
    t=(t or "").lower()
    return bool(re.search(r"\b(chief|coo|cfo|cao|ceo)\b",t) and not re.search(r"vice president",t)) or "chief administrative" in t or bool(re.search(r"\b(evp|executive vice president)\b",t))

# dropped after review Aug 25: technology / product-owner / legal / HR-tech / non-US roles that came through the Jul 26 pull
DROP = {"Pilar López-Aranguren Velarde","Gizelle George-Joseph","Priyanka Jain","Florencia Berazategui Conselo",
        "Umesh Kulkarni","Bill Bannon",
        "Nicolas Lance","Olivia Sarah-Le Lacheur","Anam K.","Javier Martin Almohalla","Ashish K Srivastava","Rachna Singhal","Deepak Mathur",
        "Maj Anoop Bhatt","Adam Girard","Marisol Andrea Sanchez García",
        "Brooke Schwerdt","Corey Bayless","Albert Leong","Dana Cruz",
        "David Burns","Usman Quddoos","Edward Nolan","Jason Sellitti","John Rider","Mitch Krzyzek","Paul Parseghian","Ken Solon","Elaina Becker",
        "Jake Frost","Jianuo (Summer) He","Ritesh Sharma","Stephan Lambert-Melton","Tamara Jeffries","William Plesnarski","Mariya Khan","Jolanta McClintock"}

cands=defaultdict(list)
# live titles confirmed by Dallas in Sales Nav (Aug 25) that the data sources have not caught up with
TITLE_OVERRIDE={("Goldman Sachs","Ericka Leslie"):"Chief Administrative Officer",
 ("Prudential Financial","Cynthia Benjamin"):"VP, Enterprise Finance Operations Shared Services",
 ("Prudential Financial","Scott Hall"):"Vice President, Appeals, Litigation & Complaints",
 ("Prudential Financial","Leigh Foster"):"Director, Process Management"}
# profile check could not find these by name at the company domain (Aug 25): keep, but flag for a Sales Nav check
VERIFY={("Goldman Sachs","John L. Bertrand"),("Goldman Sachs","Przemek Myslecki"),("MetLife","Zeid Khamash"),
 ("Prudential Financial","Priya K.C. Bhatt"),("Prudential Financial","Joseph M. Hayes"),("Prudential Financial","Todd Shriber")}
SF_DROP=set(); SF_FLAG={}
_sf=os.path.join(HERE,"inger_sf_check.csv")
if os.path.exists(_sf):
    for r in csv.DictReader(open(_sf)):
        if r["in_salesforce"]=="yes" or (r["in_salesforce"]=="possible" and r["match_confidence"] in ("high","medium")):
            SF_FLAG[(r["account"],r["full_name"])]="IN_SF:already in Salesforce" + (f" (as {r['sf_company'][:30]})" if r.get("sf_company") else "")
        elif r["in_salesforce"]=="possible":
            SF_FLAG[(r["account"],r["full_name"])]=f"same name in Salesforce at {r['sf_company'][:28] or 'unknown company'}; confirm the CRM badge before adding"
for r in csv.DictReader(open(os.path.join(HERE,"BO_AccountMap_Roster_Inger.csv"))):
    if r["gate_result"]=="CANDIDATE" and r["linkedin_url"] and r["full_name"] not in DROP and (r["account"],r["full_name"]) not in SF_DROP:
        cands[r["account"]].append({"name":r["full_name"],"title":r["title"],"url":r["linkedin_url"],"src":"Jul 26 pull","active":False})
for r in csv.DictReader(open(os.path.join(HERE,"inger_backoffice_candidates.csv"))):
    if not r["excluded_reason"].strip() and r["full_name"] not in DROP and (r["account"],r["full_name"]) not in SF_DROP:
        cands[r["account"]].append({"name":r["full_name"],"title":r["title"],"url":r["linkedin_url"],"src":(r.get("source") or "Aug 25 search").replace(" | in_salesforce",""),"active":(r.get("li_active") or "").lower()=="yes"})
        if "in_salesforce" in (r["source"] or ""): SF_FLAG[(r["account"],r["full_name"])]="IN_SF:already in Salesforce"

# root assignment by function keyword
PHRASES=["transaction banking","group insurance","group benefits","residential","regional hospitals","long term care","rogers bank","claims","disability"]
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
    elif f in ("Finance & shared services","Billing, payments & revenue","Fraud, credit & disputes"): pref=["accounting","financial","cfo","shared services","operating","administrative"]
    elif f=="Underwriting operations": pref=["underwriting","operating","claims"]
    elif f=="Administration & supply chain": pref=["administrative","caregiver","operating","accounting"]
    else: pref=["operating","residential","administrative","regional business","cfo","accounting"]
    for p in pref:
        for r in roots:
            if p in r["title"].lower(): return r["name"]
    # no executive on the map runs this function: finance-type functions may sit under a CAO/CFO, everything else becomes its own top card
    if f in ("Finance & shared services","Billing, payments & revenue","Fraud, credit & disputes"):
        for r in roots:
            if re.search(r"accounting|cfo|financial|finance",r["title"].lower()): return r["name"]
    return ""

md=["# Back-office map build sheets, Inger's twelve\n","Each sheet is one new Sales Navigator Relationship Map (cap 30). Build top-down: senior executive, then the SVP/VP who leads each function, then the directors under them. Reporting lines are inferred from titles and functions until Inger confirms.\n"]
rows_out=[]
def words(t): return set(re.findall(r"[a-z]{4}",(t or "").lower()))-{"vice","president","senior","director","head","operations","assistant","managing","global","chief","officer"}
TOPICS={
 "operations":["operations","operating officer","administrative officer","operational","coo","cao"],
 "business_ops":["business operations"],
 "revenue_ops":["revenue operations","revenue, expense"],
 "claims":["claim"],
 "finance":["finance","financial","accounting","controller","cfo","treasury","fp&a","comptroller"],
 "billing":["billing","receivables","revenue operations","revenue cycle","patient financial","payment"],
 "credit":["credit","collections","fraud","recovery","disputes","investigation","loss prevention"],
 "hr":["human resource","hr "],
 "supply":["supply chain","procurement","support services"],
 "shared":["shared services"],
 "underwriting":["underwriting"],
 "transformation":["transformation","continuous improvement","lean","process management","business process","operational effectiveness"],
 "international":["international","emerging markets"],
 "disability":["disability","absence","return to health"],
 "group":["group insurance","group benefits"],
 "transaction":["transaction banking"],
 "regional":["regional hospitals","regional business"],
 "bond":["bond & specialty","bond and specialty"],
 "covermymeds":["covermymeds"],
 "supplier":["supplier","sourcing","procurement","supply chain"],
 "workforce":["workforce","capacity planning","scheduling"],
 "product":["product owner","head of product","product management"],
 "tech":["technology","business systems","claims systems","operations platform","application","engineering"],
 "personal":["personal insurance"],
 "business_ins":["business insurance"],
}
WEIGHT={"operations":1,"finance":1,"tech":1,"regional":1,"group":1,"international":1,"transformation":1}
def wov(a,b):
    return sum(WEIGHT.get(t,2) for t in (a&b))
def topics(t):
    t=" "+(t or "").lower()+" "
    return {k for k,ws in TOPICS.items() if any(w in t for w in ws)}
LVL={"C":0,"EVP":1,"SVP":2,"VP":3,"AVP":4,"Director":5}
OVERFLOW={}
TIE_RR={}
BUILT_PIN={}
_snap=os.path.join(HERE,"_built_snapshot.csv")
if os.path.exists(_snap):
    for r in csv.DictReader(open(_snap)):
        BUILT_PIN.setdefault(r["account"],{})[r["full_name"]]="" if r["reports_up_to"]=="Top of the map" else r["reports_up_to"]
for acct in sorted(cands):
    TIE_RR.clear()
    cs=cands[acct]
    for c in cs:
        c["title"]=TITLE_OVERRIDE.get((acct,c["name"]),c["title"])
        c["band"]=band(c["title"]); c["func"]=func(c["title"]); c["top"]=c["band"]=="C"; c["tp"]=topics(c["title"]); c["lane"]=lane(c["title"])
    # cap at Sales Nav's 30 leads per map: everyone sourced before the roster sweep stays; sweep rows are ranked by
    # (a) whether they sit above an existing lead in the same topic (they close a management gap), then (b) seniority
    built_names=set(BUILT_PIN.get(acct,{}).keys())
    base=[c for c in cs if c["src"]!="Aug 25 VP sweep" or c["name"] in built_names]   # anyone already built in Sales Nav is base, whatever sourced them
    sweep=[c for c in cs if c not in base and (c["tp"] or c["band"] in ("C","EVP","SVP"))]   # a sweep row with no function in its title never fills a map slot
    generic=[c for c in cs if c not in base and c not in sweep]
    if generic: OVERFLOW.setdefault(acct,[]).extend((d["name"],d["title"],d["url"]) for d in generic)
    def gap_score(c):
        below=[b for b in base if LVL.get(b["band"],9)>LVL.get(c["band"],9) and (c["tp"]&b["tp"])]
        return (c.get("active",False), len(below)>0, len(below), -ORDER.get(c["band"],9))
    sweep.sort(key=gap_score, reverse=True)
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
    # manager = the closest higher-level person whose title shares the most topics; else the executive the function implies
    execs=[c for c in cs if c["top"]]
    for c in cs:
        c["under"]=""
        if c["top"]: continue
        higher=[h for h in cs if LVL.get(h["band"],9)<LVL.get(c["band"],9)]
        scored=[(wov(c["tp"],h["tp"]), len(c["tp"]&h["tp"])/len(c["tp"]|h["tp"]), -(LVL[c["band"]]-LVL[h["band"]]), h) for h in higher if c["tp"]&h["tp"]]
        if scored and c["band"] in ("Director","AVP"):
            near=[x for x in scored if x[3]["band"] in ("VP","AVP")]
            if near: scored=near   # a director sits under a VP/AVP when one exists in the function, never straight under an SVP or officer
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
            if c["func"] in ("Billing, payments & revenue","Fraud, credit & disputes","Finance & shared services"):
                fin=[h for h in higher if "finance" in h["tp"] and h["band"]!="C"]
                if fin: c["under"]=max(fin,key=lambda h:(LVL[h["band"]],))["name"]
            if not c["under"]:
                c["under"]=pick_root(c,execs) if execs else ""
            if not c["under"]:
                same=[h for h in higher if h["func"]==c["func"]]
                if same: c["under"]=max(same,key=lambda h:LVL[h["band"]])["name"]
    # maps already built in Sales Nav keep the reporting lines Dallas built from (only adds/removes may change)
    if acct in BUILT_PIN:
        names={c["name"] for c in cs}
        for c in cs:
            pinned=BUILT_PIN[acct].get(c["name"])
            if pinned is not None and (pinned=="" or pinned in names): c["under"]=pinned; c.pop("tie",None)
    # same-level "Head of" with a broad remit manages narrower heads beside them (Guardian pattern)
    for c in cs:
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
    md.append("| # | Lead | Title | Level | Function | Reports up to (inferred) | LinkedIn |")
    md.append("|---|---|---|---|---|---|---|")
    for i,c in enumerate(ordered,1):
        indent="&nbsp;&nbsp;&nbsp;"*c["depth"]
        fv=SF_FLAG.get((acct,c["name"]),""); flag=" (in Salesforce)" if fv.startswith("IN_SF:") else (" (confirm CRM badge)" if fv else "")
        md.append(f"| {i} | {indent}**{c['name']}**{flag} | {c['title']} | {c['band']} | {c['func']} | {c['under'] or 'Top of the map'}{(' ; ' + c['tie']) if c.get('tie') else ''} | {c['url']} |")
        rows_out.append({"account":acct,"map_name":f"{acct} - Back Office","order":i,"depth":c["depth"],"full_name":c["name"],"title":c["title"],"level":c["band"],"function":c["func"],"reports_up_to":c["under"] or "Top of the map","executive":c["exec"],"linkedin_url":c["url"],"source":c["src"],"badge_check":("VERIFY:not found by the profile check; confirm current role" if (acct,c["name"]) in VERIFY else SF_FLAG.get((acct,c["name"]),"")),"li_active":"yes" if c.get("active") else "","note":c.get("tie",""),"lane":c.get("lane","")})
    md.append("\nPaste list for the map search box: " + "; ".join(c["name"] for c in ordered) + "\n")
if OVERFLOW:
    md.append("\n## Bench: sourced but not on a map (30-lead cap)\n")
    for a,v in sorted(OVERFLOW.items()):
        md.append(f"\n**{a}** ({len(v)}): " + "; ".join(f"{n} ({t[:40]})" for n,t,u in v))
    with open(os.path.join(HERE,"BO_Map_Bench_Inger.csv"),"w",newline="") as fh:
        w=csv.writer(fh); w.writerow(["account","full_name","title","linkedin_url"])
        for a,v in sorted(OVERFLOW.items()):
            for n,t,u in v: w.writerow([a,n,t,u])
open(os.path.join(HERE,"BO_Map_Build_Sheets_Inger.md"),"w").write("\n".join(md))
with open(os.path.join(HERE,"BO_Map_Build_Sheets_Inger.csv"),"w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows_out[0].keys())); w.writeheader(); w.writerows(rows_out)
print("\n".join(md))
