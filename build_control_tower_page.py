#!/usr/bin/env python3
"""Render the control tower as a page Dallas can open (Sep 14 2026).

Reads control_tower_state.json (written by build_control_tower.py) plus the live Clay balance from
automation/logs/credit_reconciliation.log, inlines the state into one branded HTML page, and writes it to
~/Desktop/Intradiem Deliverables/deploy-gtm-control-tower/index.html (plus a repo copy). With --deploy it
also pushes the folder to the gtm-control-tower Cloudflare Pages project (noindex). Deterministic, no
network except the optional deploy, never DMs. Chained after build_control_tower.py in run_daily_rundown.sh.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(ROOT, "control_tower_state.json")
RECON = os.path.join(ROOT, "automation", "logs", "credit_reconciliation.log")
DEPLOY_DIR = os.path.expanduser("~/Desktop/Intradiem Deliverables/deploy-gtm-control-tower")
REPO_COPY = os.path.join(ROOT, "gtm-cohesion-layer", "control_tower_live.html")
LOGO_SRC = os.path.join(ROOT, "dwo-html-deck", "DWO_Deck_Update_Guide.html")
CSS_SRC = os.path.join(ROOT, "motions", "shared", "Polar_In_The_Stack_Sep13.html")
TOTAL_AVAILABLE = 83836.0  # 72,000 proof budget + 11,836 Jul 31 top-up (credit-check anchor)
PROJECT = "gtm-control-tower"
ACCOUNT_ID = "37eeacfb7a4767c44ee8f40243b62c96"

HEADERS = "/*\n  X-Robots-Tag: noindex, nofollow, noarchive\n  Referrer-Policy: no-referrer\n  X-Content-Type-Options: nosniff\n"
NOT_FOUND = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow">'
             '<title>Not here</title><style>body{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;'
             'background:#014637;color:#fff;font-family:Roboto,Helvetica,Arial,sans-serif;padding:32px}a{color:#7BD3A0}</style></head>'
             '<body><div><h1>Nothing at this address</h1><p><a href="/">Go to the tower</a></p></div></body></html>')


def live_balance():
    if not os.path.exists(RECON):
        return None, None
    text = open(RECON).read()
    blocks = re.findall(r"===== (20\d\d-\d\d-\d\d) =====.*?\"balance\":\s*([\d.]+)", text, re.S)
    if not blocks:
        return None, None
    date, bal = blocks[-1]
    return float(bal), date


def extract(pattern, text, flags=re.S):
    m = re.search(pattern, text, flags)
    return m.group(0) if m else ""


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>GTM Control Tower</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=Roboto+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>
__CSS__
.stat{grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.tbwrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;margin-top:16px}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th{font-family:"Roboto Mono",ui-monospace,monospace;font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--mono-dim);text-align:left;padding:11px 13px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.03);white-space:nowrap}
td{padding:10px 13px;border-bottom:1px solid var(--line-2);color:var(--dim);vertical-align:top;line-height:1.45;font-variant-numeric:tabular-nums}
td b{color:var(--cream);font-weight:500} tr:last-child td{border-bottom:0}
.g{font-family:"Roboto Mono",ui-monospace,monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;padding:3px 8px;border-radius:5px;display:inline-block;white-space:nowrap}
.g.run{color:#0b2f24;background:var(--green-300)} .g.pau{color:#3a1e04;background:#F7C48A} .g.dr{color:var(--dim);background:rgba(255,255,255,.1)} .g.st{color:var(--cream);background:rgba(245,130,32,.6)}
.list{margin-top:14px} .list>div{padding:12px 0;border-top:1px solid var(--line-2);font-size:14px;line-height:1.55;color:var(--dim)} .list>div:first-child{border-top:0} .list b{color:var(--cream);font-weight:500}
.list .o{color:var(--orange);font-family:"Roboto Mono",ui-monospace,monospace;font-size:10px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;margin-right:8px}
.small{font-size:12.5px;color:var(--dim-2);margin-top:12px;line-height:1.55}
footer{padding:36px 0 44px;border-top:1px solid var(--line-2);margin-top:56px;color:var(--dim-2);font-size:12.5px;line-height:1.6}
@media (max-width:640px){.wrap{padding:0 18px}}
</style></head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">__LOGO__</svg>
<div class="wrap">
<header>
  <div class="brandrow">
    <svg class="lg" role="img" aria-label="Intradiem"><use href="#ilogo"/></svg>
    <div class="stamp">GTM Engineering<br><b>Control tower</b><br><span id="gen"></span></div>
  </div>
  <div class="hero">
    <div class="eyebrow">One screen, the state the rundown reads</div>
    <h1>Where every sequence stands <span class="spark">this morning.</span></h1>
    <p class="lede">Built from the same state file the daily rundown reads, refreshed with it each weekday at 7:50. Campaign numbers come from the hourly scorecard read of lemlist. Nothing here is a customer or company claim.</p>
  </div>
</header>
<nav><div class="navin"><a href="#s1">Funnel</a><a href="#s2">Stalled</a><a href="#s3">Capacity</a><a href="#s4">Motions</a><a href="#s5">Campaigns</a><a href="#s6">Blockers</a><a href="#s7">Signals</a><a href="#s8">Sources</a></div></nav>

<section id="s1"><div class="snum">01</div><h2>The engine funnel, lifetime</h2><div class="blk"><div class="stat" id="stat"></div></div><p class="small" id="credline"></p></section>
<section id="s2"><div class="snum">02</div><h2>Stalled sequences</h2><p class="sdek">A running campaign with leads in flight and open rep tasks that has not moved for three days.</p><div class="list" id="stalled"></div></section>
<section id="s3"><div class="snum">03</div><h2>Send capacity</h2><p class="sdek">Waiting leads against each mailbox's daily cap. Wave sizing comes from these lines.</p><div class="list" id="capacity"></div></section>
<section id="s4"><div class="snum">04</div><h2>By motion</h2><div class="tbwrap"><table id="motions"></table></div></section>
<section id="s5"><div class="snum">05</div><h2>Every mapped campaign</h2><div class="tbwrap"><table id="campaigns"></table></div></section>
<section id="s6"><div class="snum">06</div><h2>Open blockers</h2><div class="list" id="blockers"></div></section>
<section id="s7"><div class="snum">07</div><h2>Hot accounts from the TAM engine</h2><div class="tbwrap"><table id="signals"></table></div><p class="small">ROI labels are the engine's labelled estimates, never verified Intradiem figures.</p></section>
<section id="s8"><div class="snum">08</div><h2>Source freshness</h2><div class="list" id="sources"></div></section>
<footer>GTM Engineering, Dallas Andrews. Internal. Rendered by build_control_tower_page.py from control_tower_state.json.</footer>
</div>
<script id="state" type="application/json">__STATE__</script>
<script>
const S=JSON.parse(document.getElementById('state').textContent);
const $=id=>document.getElementById(id); const n=v=>(v==null?'':Number(v).toLocaleString());
$('gen').textContent='state '+(S.generated_at||'').replace('T',' ').slice(0,16)+' UTC';
const lc=S.live_campaigns||{}; const pm=lc.per_motion||{}; const eng=Object.entries(pm).filter(([k])=>k!=='Rep-built');
const sum=k=>eng.reduce((a,[,v])=>a+(v[k]||0),0);
const camps=(lc.campaigns||[]).filter(c=>c.motion!=='Rep-built');
const tiles=[[camps.length,'sequences built',camps.filter(c=>c.status==='running').length+' sending, '+camps.filter(c=>c.status==='paused').length+' paused'],
 [sum('leads'),'leads loaded',sum('launched')+' launched'],[sum('waiting'),'waiting, never launched','first-touch capacity is the constraint'],
 [sum('replies'),'replies',sum('interested')+' interested','o'],[sum('meetings'),'meetings booked','counted only in Salesforce','o'],
 [sum('open_tasks'),'open rep tasks','sequences stall until worked','o'],[(lc.stalled||[]).length,'stalled sequences','3+ days, no movement','o'],
 [S.credits_live&&S.credits_live.pct!=null?S.credits_live.pct+'%':'n/a','proof credits consumed',S.credits_live&&S.credits_live.balance?n(S.credits_live.balance)+' left, read '+S.credits_live.date:'no reconciliation read']];
$('stat').innerHTML=tiles.map(([v,l,s,o])=>`<div><div class="n ${o||''}">${v}</div><div class="l">${l}</div><div class="s">${s}</div></div>`).join('');
$('credline').textContent='Scorecard trust: '+(lc.trust||'MISSING')+(lc.as_of?' as of '+lc.as_of:'')+'. Credits: live balance from the weekly reconciliation against the 83,836 total ever made available.';
$('stalled').innerHTML=(lc.stalled||[]).length?lc.stalled.map(s=>`<div><span class="o">stalled</span>${s.replace(/^STALLED /,'')}</div>`).join(''):'<div>none</div>';
$('capacity').innerHTML=(lc.capacity||[]).length?lc.capacity.map(s=>`<div>${s}</div>`).join(''):'<div>no capacity lines</div>';
$('motions').innerHTML='<tr><th>Motion</th><th>Campaigns</th><th>Running</th><th>Leads</th><th>Launched</th><th>Waiting</th><th>Replies</th><th>Interested</th><th>Meetings</th><th>Open tasks</th></tr>'+Object.entries(pm).sort((a,b)=>(a[0]==='Rep-built')-(b[0]==='Rep-built')||a[0].localeCompare(b[0])).map(([k,v])=>`<tr><td><b>${k}</b></td><td>${v.campaigns}</td><td>${v.running}</td><td>${n(v.leads)}</td><td>${n(v.launched)}</td><td>${n(v.waiting)}</td><td>${v.replies}</td><td>${v.interested}</td><td>${v.meetings}</td><td>${v.open_tasks}</td></tr>`).join('');
const cls=s=>s==='running'?'run':s==='paused'?'pau':'dr';
$('campaigns').innerHTML='<tr><th>Campaign</th><th>Motion</th><th>Rep</th><th>Status</th><th>Leads</th><th>Launched</th><th>Replies</th><th>Meetings</th><th>Open tasks</th><th>Mailbox</th></tr>'+(lc.campaigns||[]).sort((a,b)=>(a.motion==='Rep-built')-(b.motion==='Rep-built')||a.motion.localeCompare(b.motion)||a.name.localeCompare(b.name)).map(c=>`<tr><td><b>${c.name}</b></td><td>${c.motion}</td><td>${c.rep}</td><td><span class="g ${cls(c.status)}">${c.status}</span></td><td>${n(c.leads)}</td><td>${n(c.launched)}</td><td>${c.replies}</td><td>${c.meetings}</td><td>${c.open_tasks}</td><td>${c.mailbox||''}</td></tr>`).join('');
$('blockers').innerHTML=(S.blockers_and_asks||[]).filter(b=>b.open).map(b=>`<div><span class="o">${b.type}</span><b>${b.source}</b>: ${b.text}</div>`).join('')||'<div>none open</div>';
$('signals').innerHTML='<tr><th>Account</th><th>Tier</th><th>Why now</th><th>Top play</th><th>Fresh</th></tr>'+(S.signals||[]).map(s=>`<tr><td><b>${s.company}</b></td><td>${s.tier}</td><td>${s.why_now}</td><td>${s.top_play}</td><td>${s.fresh?'yes':'no'}</td></tr>`).join('');
$('sources').innerHTML=(S.sources||[]).map(s=>`<div><b>${s.name}</b>: ${s.status||''}${s.last_updated?' · '+String(s.last_updated).slice(0,10):''}${s.stale?' <span class="o">stale</span>':''}</div>`).join('');
</script>
</body></html>
"""


def main(argv):
    state = json.load(open(STATE))
    bal, date = live_balance()
    state["credits_live"] = {"balance": bal, "date": date,
                             "pct": round((TOTAL_AVAILABLE - bal) / TOTAL_AVAILABLE * 100, 1) if bal else None}
    logo = extract(r'<symbol id="ilogo".*?</symbol>', open(LOGO_SRC).read())
    css = re.search(r"<style>(.*?)</style>", open(CSS_SRC).read(), re.S).group(1)
    payload = json.dumps(state).replace("</", "<\\/")
    html = PAGE.replace("__CSS__", css).replace("__LOGO__", logo).replace("__STATE__", payload)
    assert "—" not in html
    os.makedirs(DEPLOY_DIR, exist_ok=True)
    open(os.path.join(DEPLOY_DIR, "index.html"), "w").write(html)
    open(os.path.join(DEPLOY_DIR, "_headers"), "w").write(HEADERS)
    open(os.path.join(DEPLOY_DIR, "404.html"), "w").write(NOT_FOUND)
    open(REPO_COPY, "w").write(html)
    print(f"wrote {DEPLOY_DIR}/index.html ({len(html)} bytes)")
    if "--deploy" in argv:
        env = dict(os.environ, CLOUDFLARE_ACCOUNT_ID=ACCOUNT_ID)
        r = subprocess.run(["npx", "--no-install", "wrangler", "pages", "deploy", ".", f"--project-name={PROJECT}",
                            "--branch=main", "--commit-dirty=true"], cwd=DEPLOY_DIR, env=env, capture_output=True, text=True, timeout=240)
        tail = (r.stdout + r.stderr).strip().splitlines()[-1:] or [""]
        print("deploy:", tail[0])
        return r.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
