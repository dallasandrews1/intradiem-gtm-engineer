#!/usr/bin/env python3
"""Shared title vocabulary for the back-office map pipeline: level (band), function, lane, top-officer test, topics.
One definition read by the sweep filter and the build sheets so the two never drift."""
import re
ORDER = {"C":0,"EVP":1,"SVP":2,"VP":3,"AVP":4,"Director":5}
def band(t, hint=""):
    t=re.sub(r"\s+"," ",(t or "").lower().replace("-"," ").replace("(avp)","avp"))
    if re.search(r"\b(associate vice president|assistant vice president|avp|2nd vice president|second vice president|2vp)\b",t): return "AVP"
    if re.search(r"\b(evp|executive vice president)\b",t): return "EVP"
    if re.search(r"\b(svp|senior vice president|sr\.? vice president)\b",t): return "SVP"
    if re.search(r"chief product owner|chief of staff",t): return "VP"
    if re.search(r"\b(chief|ceo|coo|cfo|cao|president)\b",t) and not re.search(r"vice president",t): return "C"
    if re.search(r"\bmanaging director\b",t): return "VP"
    if re.search(r"\b(avp|assistant vice president)\b",t): return "AVP"
    if re.search(r"\b(vp|vice president|head of|global head)\b",t): return "VP"
    if re.search(r"\b(director|executive director)\b",t): return "Director"
    return hint or "Director"
FUNC_EXTRA=[]
def configure(cfg):
    """Apply a rep set's vocabulary: extra function labels (checked first) and extra topics."""
    FUNC_EXTRA[:]=[(lbl,re.compile(rx)) for lbl,rx in cfg.get("func_extra",[])]
    TOPICS.update(cfg.get("topics_extra",{}))
def func(t):
    t=(t or "").lower()
    for lbl,rx in FUNC_EXTRA:
        if rx.search(t): return lbl
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
 "disability":["disability","absence","return to health","idi","ltd claims"],
 "retirement":["retirement","annuit"],
 "group":["group insurance","group benefits","group operations","group life"],
 "ltc":["long-term care","long term care"],
 "reinsurance":["reinsurance"],
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
def topics(t):
    t=" "+(t or "").lower()+" "
    return {k for k,ws in TOPICS.items() if any(w in t for w in ws)}
