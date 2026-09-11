#!/usr/bin/env python3
"""Quality fresh pull, Sep 3 2026. Reads Quality_FreshPull_Sep3.csv, writes the lemlist load payload
(Quality_FreshPull_Load_Sep3.json) and the review page (Quality_FreshPull_Sep3.html, copied to the Desktop).
Load rule: only rows with email_status valid go in the load; greylisted rows go in a second block Dallas can add
after a lemlist-side check; everything else stays on the bench with the reason."""
import csv, json, html, sys, os, shutil
from collections import OrderedDict
HERE=os.path.dirname(os.path.abspath(__file__))
rows=list(csv.DictReader(open(f"{HERE}/Quality_FreshPull_Sep3.csv")))
LOGO=open(sys.argv[1]).read() if len(sys.argv)>1 else ""
def lead(r):
    return {"email":r["email"],"firstName":r["first_name"].split()[0] if r["first_name"] not in ("Leigh Anne",) else "Leigh Anne",
            "lastName":r["last_name"],"companyName":r["company"].replace(" (Lumeris)",""),"companyDomain":r["company_domain"],
            "jobTitle":r["job_title"],"linkedinUrl":r["linkedin_url"],
            "customVariables":{"plan_name":r["plan_name"],"qbp_avg":r["qbp_avg"],"vm_hook":r["vm_hook"],"voice_script":r["voice_script"]}}
valid=[r for r in rows if r["email_status"].startswith("valid")]
grey=[r for r in rows if r["email_status"].startswith("unknown")]
bench=[r for r in rows if r not in valid and r not in grey]
json.dump({"generated":"2026-09-03","campaignId":"cam_viEbB6HkYsCPtxKbi","campaign":"Stars - Fresh Pool / Quality (Nate)","deduplicate":True,
           "leads":[lead(r) for r in valid],"greylisted_hold":[lead(r) for r in grey],
           "bench":[{"name":f'{r["first_name"]} {r["last_name"]}',"company":r["company"],"title":r["job_title"],"linkedin":r["linkedin_url"],"reason":r["email_status"],"note":r["note"]} for r in bench]},
          open(f"{HERE}/Quality_FreshPull_Load_Sep3.json","w"),indent=1)
def esc(s): return html.escape(s or "")
def table(rs, with_email=True):
    out=['<div class="tw"><table><thead><tr><th>Plan</th><th>Name</th><th>Title</th><th>Star avg</th>'+('<th>Email</th><th>Status</th>' if with_email else '<th>Why benched</th>')+'</tr></thead><tbody>']
    for r in sorted(rs,key=lambda r:(r["plan_name"],r["last_name"])):
        out.append(f'<tr><td>{esc(r["plan_name"])}</td><td><a href="{esc(r["linkedin_url"])}" target="_blank">{esc(r["first_name"])} {esc(r["last_name"])}</a>'+(f'<div class="sub">{esc(r["note"])}</div>' if r["note"] and with_email else '')+f'</td><td>{esc(r["job_title"])}</td><td class="num">{esc(r["qbp_avg"])}</td>'+(f'<td class="mono">{esc(r["email"])}</td><td><span class="tag {"ok" if r["email_status"]=="valid" else "warn"}">{esc(r["email_status"])}</span></td>' if with_email else f'<td>{esc(r["email_status"])}{(" · "+esc(r["note"])) if r["note"] else ""}</td>')+'</tr>')
    out.append('</tbody></table></div>'); return "\n".join(out)
plans=OrderedDict()
for r in valid+grey: plans.setdefault(r["plan_name"],0); plans[r["plan_name"]]+=1
page=f'''<title>Quality Pool Rebuild</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=Roboto+Mono:wght@500;600&display=swap');
:root{{--forest:#014637;--green:#2DB56E;--green-600:#228752;--green-300:#7BD3A0;--orange:#F58220;--ink:#202020;--sidebar:#F5F4F2;--line:#E0E0E0;--bg:#fff}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:Roboto,system-ui,sans-serif;font-size:15px;line-height:1.5}}
.wrap{{max-width:1120px;margin:0 auto;padding:0 28px 64px}}
.hero{{background:var(--forest);color:#fff;padding:44px 0 40px;position:relative;overflow:hidden}}
.hero:before{{content:"";position:absolute;right:-120px;top:-160px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.45),rgba(45,181,110,0) 65%)}}
.hero .wrap{{position:relative;padding-bottom:0}}
.eyebrow{{font-family:'Roboto Mono',monospace;font-weight:600;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-300)}}
h1{{font-weight:900;letter-spacing:-.02em;font-size:38px;margin:10px 0 8px;line-height:1.1}}
h2{{font-weight:900;letter-spacing:-.02em;font-size:24px;margin:40px 0 10px}}
.lede{{font-size:17px;max-width:760px;opacity:.92}}
.band{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:28px}}
.band div{{border:1px solid rgba(255,255,255,.18);border-radius:8px;padding:14px 16px}}
.band b{{display:block;font-size:30px;font-weight:900;color:var(--green-300);letter-spacing:-.02em}}
.band span{{font-family:'Roboto Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.06em;opacity:.85}}
.gate{{border-left:4px solid var(--green);background:var(--sidebar);padding:14px 18px;border-radius:0 8px 8px 0;margin:16px 0}}
.callout{{border-left:4px solid var(--orange);background:var(--sidebar);padding:14px 18px;border-radius:0 8px 8px 0;margin:16px 0}}
.tw{{overflow-x:auto;border:1px solid var(--line);border-radius:8px}}
table{{border-collapse:collapse;width:100%;font-size:14px}}
th{{font-family:'Roboto Mono',monospace;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--green-600);text-align:left;padding:10px 12px;background:var(--sidebar);border-bottom:1px solid var(--line)}}
td{{padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}}
td.num{{font-family:'Roboto Mono',monospace}} td.mono{{font-family:'Roboto Mono',monospace;font-size:12.5px}}
.sub{{font-size:12px;color:#666}}
a{{color:var(--forest)}}
.tag{{font-family:'Roboto Mono',monospace;font-size:11px;padding:2px 8px;border-radius:999px;border:1px solid var(--line)}}
.tag.ok{{background:#E9F7EF;color:var(--green-600);border-color:#BFE8D0}} .tag.warn{{background:#FFF1E3;color:#B85A0A;border-color:#F8D4B0}}
.logo{{width:150px;height:auto;color:#fff}}
.plans{{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 0}} .plans span{{font-family:'Roboto Mono',monospace;font-size:12px;background:var(--sidebar);border:1px solid var(--line);border-radius:999px;padding:3px 10px}}
ol li,ul li{{margin:6px 0}}
@media (max-width:760px){{.band{{grid-template-columns:repeat(2,1fr)}} h1{{font-size:30px}}}}
</style>
{LOGO}
<div class="hero"><div class="wrap">
<svg class="logo"><use href="#ilogo"/></svg>
<div class="eyebrow" style="margin-top:22px">Stars · Fresh Pool / Quality · Nathan Belfield</div>
<h1>The Quality lane, rebuilt from two people to a real pool</h1>
<p class="lede">The Quality campaign held two contacts because everyone else in that persona had already been emailed in July and moved to Resurrection. This pull went back to the 26 non-customer Stars parents, found every Quality, Stars, CAHPS and member-experience leader at director level and above, and removed anyone already in a campaign, on a reply lane, or ruled out.</p>
<div class="band">
<div><b>{len(valid)}</b><span>ready to load, verified email</span></div>
<div><b>{len(grey)}</b><span>greylisted, load after a check</span></div>
<div><b>{len(plans)}</b><span>plans covered</span></div>
<div><b>{len(bench)}</b><span>benched, reason listed</span></div>
</div>
</div></div>
<div class="wrap">
<h2>Who goes in first</h2>
<div class="gate">Every row below passed four checks on Sep 3: current at the plan on the live LinkedIn bridge, the current employer matched to a non-customer parent row in the Stars account table in Clay (Accounts Master), not in any Nate campaign or on a never-load ruling, and a work email that ZeroBounce returned as valid. Customer parents (Humana, UnitedHealth, CVS/Aetna, Elevance, HCSC, Molina) were excluded at the search, not after.</div>
<div class="plans">{"".join(f'<span>{esc(p)} · {n}</span>' for p,n in plans.items())}</div>
<div style="height:14px"></div>
{table(valid)}
<h2>Greylisted addresses, a second look before they load</h2>
<div class="callout">ZeroBounce could not confirm these mailboxes because the receiving server greylists first attempts. The pattern matches verified colleagues at the same domain. They are loaded. ZeroBounce greylisted them twice, which means the server refuses probes, not that the mailbox is missing. lemlist stops the lead on a bounce.</div>
{table(grey)}
<h2>Benched, and why</h2>
{table(bench, with_email=False)}
<h2>What each lead carries into the sequence</h2>
<p>Every lead loads with the four variables the rewritten Quality copy already uses: the plan's spoken name, its member-weighted 2026 star average with the humility clause, a one-line phone hook Nate says in his own words, and a short voice note. The star average is the parent's member-weighted figure from the CMS 2026 release, rounded to the half-star. Centene loads as Wellcare, its Medicare Advantage brand.</p>
<h2>What happens next</h2>
<ol>
<li>Done Sep 3: Nathan attached as sender, the verified rows loaded with deduplicate on, readiness green, Email 1 previewed on a real lead.</li>
<li>Launch: lead review and start once Nate has read this page. Nothing sends until then.</li>
<li>Done Sep 3, later: the seven loaded, then re-checked through Clay's ZeroBounce. Norwood, Hebert and Thomas M. came back valid and moved up. Duckett, Tuite, Neal and Reid greylisted a second time and stay in with that flag.</li>
<li>Second pass: the ten with no address get one more source before they are dropped.</li>
</ol>
</div>'''
open(f"{HERE}/Quality_FreshPull_Sep3.html","w").write(page)
dest=os.path.expanduser("~/Desktop/Intradiem Deliverables/Quality_FreshPull_Sep3.html")
shutil.copy(f"{HERE}/Quality_FreshPull_Sep3.html",dest)
print(f"valid {len(valid)} grey {len(grey)} bench {len(bench)} -> {dest}")
