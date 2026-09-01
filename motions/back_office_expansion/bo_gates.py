#!/usr/bin/env python3
"""Title gates for net-new back-office sourcing: which titles never reach a map, and why. One definition used by
filter_sweep.py (at sourcing time) and by apply_bridge.py / verify_live.py (re-gating refreshed titles)."""
import re
from bo_titles import band, topics, is_root
LEVEL_RX = re.compile(r"\b(chief|ceo|coo|cfo|cao|cio|president|evp|executive vice president|svp|senior vice president|sr\.? vice president|vice president|vp|avp|associate vice president|assistant vice president|2nd vice president|second vice president|managing director|executive director|director|head of|global head|head,)\b", re.I)
# front line and non-back-office gates, in the order they are reported
GATES = [
 ("ceo_out_of_scope", re.compile(r"chief executive|\bceo\b", re.I)),
 ("title_excluded_gate_individual_contributor", re.compile(r"analyst|team lead|\blead\b|specialist|coordinator|supervisor|\bassociate\b(?! vice)|consultant|administrator\b|^(?!.*chief).*\bofficer\b", re.I)),
 ("title_excluded_gate_front_line", re.compile(r"contact cent|call cent|customer care|care cent|customer support|customer experience|\bcx\b|branch|retail|teller|\bstore\b|\bivr\b|interactive voice|customer engagement|customer success|client experience|member experience|patient experience|voice of", re.I)),
 ("title_excluded_gate_sales", re.compile(r"\bsales\b|business development|account executive|account manage|relationship manag|relationship banker|private bank|private wealth|wealth|advisor|adviser|financial consultant|financial planner|commercial bank|\bbanker\b|portfolio manag|investment(?! operations)|trader|trading(?! operations)|treasury management(?! operations)|treasury solutions|\bmarketing\b|capital markets|area director|hr solutions(?! service)|product group|general manager|marketplace|\bbrand\b|chief commercial|communications|public relations|go.to.market|\bgtm\b|revenue operations|sales operations|distribution|growth|partnerships|channel|dealer|broker(?!age operations)|producer|insurance agency|underwriter(?! operations)|origination|lending officer|loan officer|capital markets|corporate development|m&a|mergers", re.I)),
 ("title_excluded_gate_legal", re.compile(r"\blegal\b|counsel|attorney|compliance|regulatory|\baudit|privacy|ethics|government|public policy|corporate secretary|litigation(?! operations)|operational risk|risk management|risk officer|controls testing|internal control|\brisk\b(?! operations)", re.I)),
 ("title_excluded_gate_it_engineering", re.compile(r"software|engineer|developer|data scien|data analytics|analytics|architect|cyber|security|network|infrastructure|cloud|devops|information technology|\bit\b|technology|\bcio\b|\bcto\b|chief information|chief technology|application delivery|application rationalization|application configuration|application support|product design|product\b(?! operations| owner)|digital(?! operations)|product manag|product development|innovation|agile|\bplatform\b|\bai\b|machine learning|data management|data governance|enterprise data|application development|solutions delivery|test(ing)? manager|automation engineer|\bqa\b", re.I)),
 ("title_excluded_gate_hr", re.compile(r"talent|recruit|learning|training|workforce development|leadership development|diversity|inclusion|compensation|total rewards|employee relations|hr business partner|hrbp|people partner|people business|human resources(?! operations| shared)|organizational development|culture|employee experience|benefits(?! administration| operations)", re.I)),
 ("title_excluded_gate_field_ops", re.compile(r"facilit|real estate|construction|\bfield\b|\bgas\b|electric|transmission|substation|pipeline|environmental|safety|fleet|generation|energy|grid operations|control room|control center|system operations|gas operations|electric operations|storm|emergency|maintenance|plant|meter reading|linemen|lineman|line worker|dispatch|engineering", re.I)),
 ("title_excluded_gate_clinical", re.compile(r"clinical(?! operations)|\bnurse|\brn\b|pharmac|medical director|physician|behavioral|care management(?! operations)|case management(?! operations)|population health|quality improvement|\bhedis\b|star ratings|medicare sales", re.I)),
 ("title_excluded_gate_other", re.compile(r"social impact|community|sustainability|chief of staff|executive assistant|assistant to|\bintern\b|consultant|contractor|retired|former|student|program manager|project manager|\bpmo\b|strategy(?! operations)|strategic planning|transformation office|corporate strategy|investor relations|treasurer\b|tax(?! service| operations| filing| pay)|actuar|underwriting|reinsurance|insurance operations$", re.I)),
]
CRED_CLIN = re.compile(r",\s*(MD|DO|RN|DNP|NP|PharmD|BSN|MSN)\b|\b(MD|RN|DNP|PharmD)\b", re.I)
CRED_ACT = re.compile(r"\b(FSA|MAAA|ASA|ACAS|FCAS)\b")
GENERIC = {"operations","transformation","process","business_ops"}
KEEP_TECH = re.compile(r"chief.*operations officer|chief divisional technology|operations technology|business systems|business technology|claims systems|systems implementation|operations systems|workforce management technology", re.I)
NON_US = re.compile(r"united kingdom|england|london|scotland|wales|ireland|\buk\b|india|philippines|canada|mexico|poland", re.I)


def gate_reason(title, full_name="", spec=None, location=""):
    """Return the excluded_reason for a title (blank = passes every gate)."""
    spec = spec or {}
    t = re.sub(r"\s+", " ", (title or "")).strip()
    if spec.get("us_only") and NON_US.search(location or ""): return "non_us_location"
    if not LEVEL_RX.search(t): return "title_excluded_gate_below_director"
    if CRED_CLIN.search(full_name or ""): return "title_excluded_gate_clinical"
    if CRED_ACT.search(full_name or ""): return "title_excluded_gate_other"
    if len(re.sub(r"[^a-z]", "", t.lower())) < 8 or '"' in t: return "title_excluded_gate_other"
    if re.search(r"chief.*operations officer|chief divisional technology", t, re.I) and not re.search(r"assistant to|chief of staff", t, re.I): pass   # the operations executive at banks carries Technology in the title; keep the officer, not the org
    elif re.search(r"\b(cio|cto)\b|chief information|chief technology", t, re.I): return "title_excluded_gate_it_engineering"
    if not spec.get("lob_cfo_ok") and re.search(r"\bcfo\b|chief financial officer\s*[,(\-/]|chief financial officer (of|for|at)\b", t, re.I): return "title_excluded_gate_lob_finance"
    for name, rx in GATES:
        if name == "title_excluded_gate_front_line" and spec.get("front_line_ok_with_ops") and re.search(r"operations|service", t, re.I): continue   # at service-business accounts, "customer success/experience" IS the operations org
        if name == "title_excluded_gate_it_engineering" and KEEP_TECH.search(t): continue
        if name == "title_excluded_gate_legal" and re.search(r"fraud|financial crimes|bsa|aml", t, re.I) and not re.search(r"counsel|attorney|compliance officer|audit", t, re.I): continue
        if rx.search(t): return name
    if band(t) not in ("C", "EVP", "SVP", "VP", "AVP", "Director"): return "title_excluded_gate_below_director"
    if not topics(t) and not is_root(t): return "no_back_office_function_in_title"
    if spec.get("require_specific_topic") and not is_root(t) and topics(t) <= GENERIC: return "generic_operations_title"
    return ""
