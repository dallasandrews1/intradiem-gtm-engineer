#!/usr/bin/env python3
"""Directory pulls that work over plain HTTP (no browser). Run from motions/partner_channel.

  python3 landscape/tools/directory_pulls.py genesys   -> landscape/research/emea/genesys_finder.json (595 records, Zift API)
  python3 landscape/tools/directory_pulls.py verint    -> landscape/research/emea/verint_emea.json (FacetWP refresh endpoint)
  python3 landscape/tools/directory_pulls.py aspect    -> prints every directory entry (Webflow pagination)

Five9 (Salesforce Lightning Out, shadow DOM) and the AWS Partner Finder (SPA) need the puppeteer-core
scripts next to this file: `npm i puppeteer-core` in a scratch folder, then `node five9_locator.js > tiles.json`
and `node aws_partner_finder.js > cards.json`. Both drive the installed Google Chrome.
"""
import json, re, sys, html, urllib.request, pathlib

HERE = pathlib.Path(__file__).resolve().parents[1] / "research" / "emea"
UA = {"User-Agent": "Mozilla/5.0"}


def genesys():
    H = {**UA, "X-ZIFT-PARTNER-LOCATOR": "8a99836c82cdb3970182d1169fef4b2c", "Referer": "https://www.genesys.com/partners/partner-finder"}
    get = lambda u: json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=60).read())
    base = "https://rest.ziftmarcom.com/locator/partners?size=100&includeFields=true&includeTiers=true&types=PARTNER&language=en_US&page="
    r = get(base + "0"); allp = list(r["content"])
    for p in range(1, r["totalPages"]):
        allp += get(base + str(p))["content"]
    (HERE / "genesys_finder_raw.json").write_text(json.dumps(allp))
    print("genesys records", len(allp))


def verint():
    def refresh(paged, ptype):
        body = {"action": "facetwp_refresh", "data": {"facets": {"partner_regions": ["emea"], "partner_type": [ptype], "partner_solutions": [], "partners_search": "", "partners_pagination": []},
                "frozen_facets": {}, "http_params": {"get": {}, "uri": "partners", "url_vars": {}}, "template": "partners", "extras": {"counts": True}, "soft_refresh": 0, "is_bfcache": 0, "first_load": 0, "paged": paged}}
        req = urllib.request.Request("https://www.verint.com/wp-json/facetwp/v1/refresh", data=json.dumps(body).encode(), headers={**UA, "Content-Type": "application/json", "Referer": "https://www.verint.com/partners/"})
        return json.loads(urllib.request.urlopen(req, timeout=60).read())
    out = {}
    for ptype in ["channel-partner", "consultancy-partner", "global-alliance", "technology-partner"]:
        names = []
        for paged in range(1, 12):
            cards = re.findall(r'<h2 class="visually-hidden">\s*(.*?)</h2>.*?href="([^"]*)"', refresh(paged, ptype).get("template", ""), re.S)
            new = [(html.unescape(n.strip()), u) for n, u in cards if html.unescape(n.strip()) not in [x[0] for x in names]]
            if not new:
                break
            names += new
        out[ptype] = names
        print(ptype, len(names))
    (HERE / "verint_emea.json").write_text(json.dumps(out, indent=1))


def aspect():
    for n in range(1, 8):
        t = urllib.request.urlopen(urllib.request.Request(f"https://www.aspect.com/company/partners?7f3d30a2_page={n}", headers=UA), timeout=60).read().decode()
        parts = t.split('class="partner-grid_item w-dyn-item"')[1:]
        if not parts:
            break
        for blk in parts:
            txt = html.unescape(re.sub(r"<[^>]+>", " | ", blk[:6000])); txt = re.sub(r"(\s*\|\s*)+", " | ", txt); txt = re.sub(r"\s+", " ", txt).split("Visit partner site")[0].strip(" |")
            print(f"p{n} | {txt[:180]}")


if __name__ == "__main__":
    {"genesys": genesys, "verint": verint, "aspect": aspect}[sys.argv[1]]()
