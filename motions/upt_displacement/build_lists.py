#!/usr/bin/env python3
"""UPT displacement motion: the Verint estate and NICE estate lists from Clay Audiences.

Reads the Sep 9 2026 Audiences pull (lists/_audiences_pull_sep9_raw.csv, 208 companies where PredictLeads or a rep
read shows Verint or NICE on the contact center or WFM stack), drops customers, splits by estate and by six-vertical
fit, joins the operating executives already in the DWO wave-1 pool, and writes the two lists plus a summary.

Vendor-level only. No source we hold detects Verint DPA or NICE Desktop Analytics as a SKU; the sku_signal column
is blank until a second signal (job posting, LinkedIn skill, case study, rep confirmation) fills it.

Run: python3 build_lists.py   (0 credits; re-pull the raw file with the Audiences CLI when the stack read refreshes)
"""
import csv, json, re, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent; L = HERE / "lists"
ICP = {"Home & Auto Insurance","Div Financial Services","Banking","Insurance","Healthcare Insurance","Health Insurance",
       "Healthcare Provider","Healthcare_Provider","Retail","Telco/Cable","Telecom","Utilities","Outsourcer"}
def nd(d): return (d or "").lower().replace("https://","").replace("http://","").replace("www.","").strip("/")
raw = list(csv.DictReader(open(L / "_audiences_pull_sep9_raw.csv")))
vito = json.load(open(L / "vito_by_domain.json"))
def stack(r): return " ".join([r["cc_all"] or "", r["cc_latest"] or "", r["wfm_latest"] or ""])
def products(r, vendor):
    out = []
    for part in (r["cc_all"] or "").split("),"):
        s = part.strip().rstrip(")")
        if re.search(vendor, s, re.I): out.append(s + (")" if "(" in s and not s.endswith(")") else ""))
    return "; ".join(out)
cols = ["company","domain","industry","icp_fit","employees","estate","verint_products_dated","nice_products_dated",
        "wfm_latest","cc_latest","vito_in_dwo_pool","vito_names","evidence_tier","sku_signal","sku_signal_source","sku_signal_date","nice_use_tag","rep_confirmed","flag"]
# Held by name: customers or customer subsidiaries that Salesforce still calls Prospect (registry cross-check, Sep 9 2026).
HOLD = {"duke energy": "customer per the Customer Value Registry (Greenlight); Salesforce Account Type says Prospect",
        "optum360": "subsidiary of Optum (customer); domain optum.com",
        "aetna life insurance company inc": "Aetna Inc is a customer; SF record carries the aon.com domain, treat as customer family",
        "express scripts": "Evernorth, which is Cigna, a customer (Cigna's own Verint DPA postings surfaced in the sweep)",
        "american bankers life assurance company of florida": "assurant.com; Assurant is a customer per the value registry",
        "oak street health llc": "CVS Health subsidiary since 2023; CVS is a customer",
        "bt business and public sector": "BT Group; the BT/EE story is in marketing's customer stories registry",
        "first utility": "became Shell Energy (2019) and was sold to Octopus Energy (Dec 2023); entity no longer operates",
        "vivint solar": "acquired by Sunrun (2020); Sunrun is already on the NICE list"}
FLAG = {"american express": "AE to confirm: American Express Global Business Travel is the customer, AmEx proper is not the same company",
        "progressive insurance": "Progressive Leasing (a customer) is an unrelated company; keep",
        "aaa texas": "AAA National HQ is a customer; AAA Texas is Auto Club Enterprises, a separate club. AE to confirm",
        "rsa insurance group (canada)": "RSA Canada is Intact Financial since 2021; the Verint back-office story is the UK parent"}
SIG = json.load(open(L / "sku_signals.json")) if (L / "sku_signals.json").exists() else {}
rows = {"verint": [], "nice": []}; customers = []; other = []
for r in raw:
    if r["account_type"] == "Customer": customers.append(r); continue
    if (r["company"] or "").strip().lower() in HOLD: r["_hold"] = HOLD[r["company"].strip().lower()]; customers.append(r); continue
    if r["account_type"] != "Prospect": other.append(r); continue
    s = stack(r); v = bool(re.search("verint", s, re.I)) or bool((SIG.get(nd(r["domain"])) or {}).get("add_to_verint")); n = bool(re.search("nice", s, re.I))
    d = nd(r["domain"]); vt = vito.get(d, [])
    base = {"company": r["company"], "domain": d, "industry": r["industry"], "icp_fit": "yes" if r["industry"] in ICP else "outside six verticals",
            "employees": r["employees"], "estate": "both" if v and n else ("verint" if v else "nice"),
            "verint_products_dated": products(r, "verint"), "nice_products_dated": products(r, "nice"),
            "wfm_latest": r["wfm_latest"], "cc_latest": r["cc_latest"], "vito_in_dwo_pool": len(vt),
            "vito_names": "; ".join(f"{p['name']} ({p['title']})" for p in vt),
            "evidence_tier": (SIG.get(d) or {}).get("tier", "D"), "sku_signal": (SIG.get(d) or {}).get("signal", ""), "sku_signal_source": (SIG.get(d) or {}).get("source", ""),
            "sku_signal_date": (SIG.get(d) or {}).get("date", ""), "nice_use_tag": ((SIG.get(d) or {}).get("nice_tag") or ("bundled, no evidence of use" if n else "")),
            "rep_confirmed": r["rep_confirmed"] or "", "flag": "; ".join(x for x in [FLAG.get((r["company"] or "").strip().lower(), ""), (SIG.get(d) or {}).get("flag", "")] if x)}
    if v: rows["verint"].append(base)
    if n: rows["nice"].append(base)
for k, fn in (("verint","verint_estate.csv"),("nice","nice_estate.csv")):
    rs = sorted(rows[k], key=lambda x: (x["icp_fit"] != "yes", -(int(float(x["employees"])) if x["employees"] else 0)))
    with open(L / fn, "w", newline="") as fh: w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(rs)
with open(L / "excluded_customers.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["company","domain","wfm_latest","cc_latest","why"])
    for r in customers: w.writerow([r["company"], nd(r["domain"]), r["wfm_latest"], r["cc_latest"], r.get("_hold") or "Account Type = Customer in Salesforce; never in a cold motion"])
    for r in other: w.writerow([r["company"], nd(r["domain"]), r["wfm_latest"], r["cc_latest"], "Account Type blank; held until Salesforce says Prospect"])
def summ(rs):
    icp = [x for x in rs if x["icp_fit"] == "yes"]
    return {"accounts": len(rs), "icp_accounts": len(icp), "outside_icp": len(rs) - len(icp),
            "tiers": collections.Counter(x["evidence_tier"] for x in rs), "tiers_icp": collections.Counter(x["evidence_tier"] for x in icp),
            "nice_tags": collections.Counter(x["nice_use_tag"] for x in rs if x["nice_use_tag"]),
            "tier_a_names": [x["company"] for x in rs if x["evidence_tier"].startswith("A")], "tier_b_names": [x["company"] for x in rs if x["evidence_tier"] == "B"],
            "accounts_with_vito": sum(1 for x in rs if x["vito_in_dwo_pool"]), "vito_people": sum(x["vito_in_dwo_pool"] for x in rs),
            "industries": collections.Counter(x["industry"] or "unknown" for x in rs).most_common(8),
            "employees_20k_plus": sum(1 for x in rs if x["employees"] and float(x["employees"]) >= 20000)}
S = {"pulled": "2026-09-09", "swept": "2026-09-09", "verint": summ(rows["verint"]), "nice": summ(rows["nice"]),
     "both_estates": sum(1 for x in rows["verint"] if x["estate"] == "both"), "customers_excluded": len(customers), "held_blank_type": len(other),
     "segments": json.load(open(L / "segments_made.json")), "segment_counts": json.load(open(L / "segment_counts.json"))}
json.dump(S, open(L / "summary.json", "w"), indent=1)
print(json.dumps(S, indent=1))
