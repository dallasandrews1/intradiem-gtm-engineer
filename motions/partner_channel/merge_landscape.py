#!/usr/bin/env python3
"""Normalise the channel-landscape research fan-out into one data file.

Inputs:  landscape/research/<region>/<vendor_slug>.md   (one per platform pass; each holds a
         "Vendor context" paragraph, a PARTNERS JSON array, a SHARE JSON object, a Gaps list)
         landscape/research/<region>/share_multi.md      (SHARE_POINTS + MULTI_VENDOR JSON arrays)
         landscape/data/<region>_meta.json               (hand-written page copy: tldr, h2s, start,
         confidence, gaps, vendor context/program/share lines, aliases)
Output:  landscape/data/<region>.json  read by build_landscape.py

Run: python3 merge_landscape.py [emea]
"""
import json, pathlib, re, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
region = sys.argv[1] if len(sys.argv) > 1 else "emea"
RES = HERE / "landscape/research" / region
meta = json.loads((HERE / "landscape/data" / f"{region}_meta.json").read_text())
VENDORS = [v["slug"] for v in meta["vendors"]]
ALIASES = {k.lower(): v for k, v in meta.get("aliases", {}).items()}
DROP = {x.lower() for x in meta.get("drop", [])}
DROP_LINKS = {k: set(v) for k, v in meta.get("drop_links", {}).items()}


def conf(c):
    c = str(c or "").upper()
    for lvl in ("HIGH", "MEDIUM", "LOW"):
        if c.startswith(lvl):
            return lvl
    return "LOW" if c else ""

STRIP = re.compile(r"\b(group|holdings?|plc|ltd|limited|inc|llc|gmbh|ag|sa|s\.a\.|nv|bv|b\.v\.|srl|spa|s\.p\.a\.|oy|ab|as|a/s|se|co|corp|corporation|company|international|technologies|technology|solutions|business|services)\b\.?", re.I)


FIRST_SEEN = {}


def canon(name):
    n = unicodedata.normalize("NFKD", name.strip()).encode("ascii", "ignore").decode()
    if n.lower() in ALIASES:
        return ALIASES[n.lower()]
    clean = re.sub(r"\s*\(.*?\)\s*", " ", n).strip()
    base = STRIP.sub("", clean)
    base = re.sub(r"[^A-Za-z0-9&+ ]", " ", base)
    base = re.sub(r"\s+", " ", base).strip().lower()
    if base in ALIASES:
        return ALIASES[base]
    return FIRST_SEEN.setdefault(base, clean)


def extract_json(text, label, kind):
    """First JSON array/object that follows `label` in the text, tolerant of code fences."""
    i = text.find(label)
    if i < 0:
        return None
    open_ch, close_ch = ("[", "]") if kind == "array" else ("{", "}")
    j = text.find(open_ch, i)
    depth, k, in_str, esc = 0, j, False, False
    while k < len(text):
        ch = text[k]
        if in_str:
            if esc: esc = False
            elif ch == "\\": esc = True
            elif ch == '"': in_str = False
        else:
            if ch == '"': in_str = True
            elif ch == open_ch: depth += 1
            elif ch == close_ch:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[j:k + 1])
                    except json.JSONDecodeError as e:
                        raise SystemExit(f"{label}: bad JSON in {text[:40]!r}: {e}")
        k += 1
    raise SystemExit(f"{label}: unterminated JSON")


def norm_sources(srcs):
    out = []
    for s in srcs or []:
        if isinstance(s, str):
            out.append({"url": s, "date": "", "note": ""})
        elif isinstance(s, dict) and s.get("url"):
            out.append({"url": s["url"], "date": str(s.get("date", "") or ""), "note": s.get("note", "")})
    return out


partners = {}   # canon name -> record


def rec(name):
    c = canon(name)
    if c not in partners:
        partners[c] = {"name": c, "hq_country": "", "emea_coverage": [], "partner_type": "", "carries": {},
                       "also_carries": [], "scale_signal": "", "share_statement": "", "sources": [], "_names": set()}
    partners[c]["_names"].add(name)
    return partners[c]


COV_MAP = {"united kingdom": "UK", "uk and ireland": "UK, Ireland", "united arab emirates": "UAE", "uae": "UAE"}


def merge_cov(r, cov):
    for c in cov or []:
        c = str(c).strip()
        c = COV_MAP.get(c.lower(), c)
        for part in ([c] if "," not in c or len(c) > 40 else [x.strip() for x in c.split(",")]):
            if part and part.lower() not in {x.lower() for x in r["emea_coverage"]}:
                r["emea_coverage"].append(part)


share_points = []
for slug in VENDORS:
    f = RES / f"{slug}.md"
    if not f.exists():
        print(f"missing research: {f.name}")
        continue
    t = f.read_text()
    arr = extract_json(t, "PARTNERS", "array") or []
    rel_key = next((k for k in (arr[0].keys() if arr else []) if k.endswith("_relationship")), None)
    for p in arr:
        if p["name"].lower() in DROP:
            continue
        r = rec(p["name"])
        r["hq_country"] = r["hq_country"] or p.get("hq_country", "")
        r["partner_type"] = r["partner_type"] or p.get("partner_type", "")
        merge_cov(r, p.get("emea_coverage"))
        ss = p.get("scale_signal", "")
        if ss and ss.lower() not in ("none found", "none") and len(ss) > len(r["scale_signal"]):
            r["scale_signal"] = ss
        r["carries"][slug] = {"relationship": p.get(rel_key, "listed partner") if rel_key else "listed partner",
                              "evidence": p.get("evidence", ""), "confidence": conf(p.get("confidence")),
                              "sources": norm_sources(p.get("sources"))}
        for ac in p.get("also_carries") or []:
            label = ac if isinstance(ac, str) else (ac.get("vendor") or ac.get("name") or "")
            if label and label not in r["also_carries"]:
                r["also_carries"].append(label)
        r["sources"] += norm_sources(p.get("sources"))
    sh = extract_json(t, "SHARE", "object")
    if sh:
        meta_v = next(v for v in meta["vendors"] if v["slug"] == slug)
        meta_v.setdefault("_share_raw", sh)

sm = RES / "share_multi.md"
if sm.exists():
    t = sm.read_text()
    for sp in extract_json(t, "SHARE_POINTS", "array") or []:
        share_points.append({k: str(sp.get(k, "")) for k in ("metric", "region", "vendor", "value", "measured_as", "source_url", "source_date", "note")})
    for p in extract_json(t, "MULTI_VENDOR", "array") or []:
        if p["name"].lower() in DROP:
            continue
        r = rec(p["name"])
        r["hq_country"] = r["hq_country"] or p.get("hq_country", "")
        r["partner_type"] = r["partner_type"] or p.get("partner_type", "")
        merge_cov(r, p.get("emea_coverage"))
        if p.get("scale_signal") and len(p["scale_signal"]) > len(r["scale_signal"]) and p["scale_signal"].lower() not in ("none", "none found"):
            r["scale_signal"] = p["scale_signal"]
        if p.get("share_statement") and p["share_statement"].lower() not in ("none", "none found"):
            r["share_statement"] = p["share_statement"]
        for vname, c in (p.get("carries") or {}).items():
            slug = meta["vendor_slugs"].get(vname.lower())
            if not slug:
                print(f"  unknown vendor key in MULTI_VENDOR: {vname!r} ({p['name']})")
                continue
            if not isinstance(c, dict):
                continue
            ev = c.get("evidence", "")
            if not ev or ev.lower().startswith(("no ", "not ", "none")):
                continue
            cur = r["carries"].get(slug)
            new = {"relationship": c.get("relationship", "listed partner"), "evidence": ev,
                   "confidence": conf(c.get("confidence")),
                   "sources": norm_sources([{"url": c.get("source_url", ""), "date": c.get("source_date", "")}])}
            if new["confidence"] == "LOW":
                continue
            if not cur:
                r["carries"][slug] = new
            elif cur["confidence"] in ("", "LOW") and new["confidence"] in ("MEDIUM", "HIGH"):
                new["sources"] += cur["sources"]
                r["carries"][slug] = new
            else:
                cur["sources"] += new["sources"]
        r["sources"] += norm_sources(p.get("sources"))

# tidy
out_partners = []
for r in partners.values():
    for slug in DROP_LINKS.get(r["name"], ()):
        r["carries"].pop(slug, None)
    if not r["carries"]:
        continue
    seen, srcs = set(), []
    for s in r["sources"]:
        if s["url"] not in seen:
            seen.add(s["url"]); srcs.append(s)
    r["sources"] = srcs
    def carried(label):
        l = label.lower()
        for k, slug in meta["vendor_slugs"].items():
            if l == k or l.startswith(k + " ") or l.startswith(k + "(") or l.startswith(k + ","):
                return slug in r["carries"]
        return False
    r["also_carries"] = [a for a in r["also_carries"] if not carried(a)]
    r["_names"] = sorted(r["_names"])
    out_partners.append(r)

data = {k: meta[k] for k in ("title", "angle", "subhead", "tldr", "share_h2", "share_intro", "share_note", "vendors_h2",
                             "map_h2", "map_intro", "start_h2", "start", "confidence", "gaps")}
data["vendor_order"] = VENDORS
data["vendors"] = [{k: v[k] for k in ("slug", "name", "context", "program", "share") if k in v} for v in meta["vendors"]]
data["share_points"] = share_points + meta.get("extra_share_points", [])
data["partners"] = out_partners
(HERE / "landscape/data" / f"{region}.json").write_text(json.dumps(data, indent=1, ensure_ascii=False))
multi = sum(1 for p in out_partners if len(p["carries"]) >= 2)
print(f"{region}.json: {len(out_partners)} partners, {multi} multi-platform, {len(data['share_points'])} share points")
for p in sorted(out_partners, key=lambda p: -len(p["carries"]))[:25]:
    print(f"  {len(p['carries'])}  {p['name']:<32} {', '.join(p['carries'])}   aliases={p['_names'] if len(p['_names'])>1 else ''}")
