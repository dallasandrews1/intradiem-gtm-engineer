#!/usr/bin/env python3
"""Title rules shared by build_inger_roster.py and build_am_roster.py (lifted verbatim Sep 11 2026)."""
import re
def norm(s):
    """first+last token key, credentials and middle initials stripped, so 'John L. Bertrand' == 'John Bertrand'"""
    n = re.sub(r"[,(].*$", "", s or "")
    n = re.sub(r"\b(mba|cpa|jr|sr|ii|iii|phd|clms|rmc|cep|arm|msf|rhia|dnp|rn|ne-bc|faan|lssbb|pmp|pspo|cma|cpcu|cris|ccla)\b\.?", "", n, flags=re.I)
    t = [x for x in re.sub(r"[^a-z ]", "", n.lower()).split() if len(x) > 1]
    return (t[0] + t[-1]) if len(t) >= 2 else (t[0] if t else "")

# ---- band + function inference from title text -------------------------------------------------
BAND_RULES = [
    ("EVP", r"\b(evp|executive vice president)\b"),
    ("SVP", r"\b(svp|senior vice president|sr\.? vice president|sr\.? vp)\b"),
    ("Director", r"\b(avp|assistant vice president|director|dir\.?|directora)\b"),   # AVP sits at Director level in practice
    ("VP", r"\b(vp|vice president|head of|global head|managing director|md)\b"),
    ("C", r"\b(chief|ceo|coo|cfo|cao|cio|cto|chro|president|chairman|chairwoman)\b"),
    ("Manager", r"\b(manager|mgr|lead|supervisor|specialist|analyst|engineer|coordinator|associate|representative|agent|expert)\b"),
]
BACK_OFFICE = r"(shared services|claims|fraud|payment|payments|disputes|billing|collections|underwriting|appeals|procurement|accounts payable|accounts receivable|treasury|finance operations|financial operations|back office|back-office|administration|administrative|operations|document|processing|enrollment|servicing|settlement|reconciliation)"
CONTACT_CENTER = r"(contact center|call center|customer care|customer service|customer experience|cx|workforce management|wfm|workforce planning|voice services|service delivery|omnichannel|support center)"
TECH = r"(technology|engineer|software|it\b|information|data|digital|architect|network|systems|infrastructure|analytics|learning|training|enablement|hr\b|human resources|talent|real estate|facilit|marketing|sales|legal|counsel|risk|compliance|audit)"

def infer_band(title):
    t = (title or "").lower()
    for band, rx in BAND_RULES:
        if re.search(rx, t):
            return band
    return "Unknown"

def infer_function(title):
    t = (title or "").lower()
    if re.search(CONTACT_CENTER, t):
        return "contact_center"
    if re.search(BACK_OFFICE, t):
        return "back_office"
    if re.search(TECH, t):
        return "tech_or_other"
    return "unknown"

def in_band(band):
    return band in ("SVP", "VP", "Director")

