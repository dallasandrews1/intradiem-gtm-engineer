#!/usr/bin/env python3
"""Nate's back-office net-new package page (one page, Intradiem kit). Reads the staged
lead CSV, the audit CSV, netnew_page_signals.json and the campaign copy; writes
Nate_NetNew_Package_Sep2.html. Regenerate after every wave rebuild."""
import csv, json, os, html, collections
HERE=os.path.dirname(os.path.abspath(__file__))
rows=list(csv.DictReader(open(os.path.join(HERE,'BO_NetNew_Leads_Staged_Sep2.csv'))))
sig=json.load(open(os.path.join(HERE,'netnew_page_signals.json')))
opener=json.load(open(os.path.join(HERE,'netnew_package_config.json')))['opener_line']
logo=open(os.path.join(HERE,'_logo_symbol.svg')).read()
E=html.escape
ORDER=['Centene','Fidelity','National Grid','Truist','Paychex','Regions']
LEGAL={'Centene':'Centene Corporation','Fidelity':'Fidelity Investments','National Grid':'National Grid US','Truist':'Truist Financial','Paychex':'Paychex','Regions':'Regions Financial'}
LOADED=('1','2')
w1=[r for r in rows if r['wave'] in LOADED]
ready=[r for r in w1 if r['load_status']=='ready']
holds=[r for r in rows if r['load_status']=='hold']
later=[r for r in rows if r['wave'] not in ('1',)]
strong=sum(1 for a in sig.values() for s in a['signals'] if s['s']=='STRONG')
def pill(st):
    return {'ready':'<span class="pill go">Ready</span>','hold':'<span class="pill hold">Hold</span>','needs_email':'<span class="pill wait">No email yet</span>'}.get(st,st)
def li_name(r):
    n=E((r['firstName']+' '+r['lastName']).strip())
    return f'<a href="{E(r["linkedinUrl"])}" target="_blank" rel="noopener">{n}</a>'
sections=[]
for a in ORDER:
    A=sig[a]; rs=[r for r in w1 if r['parent_account']==a]
    nready=sum(1 for r in rs if r['load_status']=='ready')
    later_n=sum(1 for r in rows if r['parent_account']==a and r['wave'] not in LOADED+('9',))
    sigs=''.join(f'<li><span class="d">{E(s["d"])}</span><span class="t">{E(s["t"])} <a href="{E(s["u"])}" target="_blank" rel="noopener">source</a></span><span class="chip {s["s"].lower()}">{E(s["s"])}</span></li>' for s in A['signals'])
    def hr(r): return '<div class="hr">'+E(r['hold_reason'])+'</div>' if r['hold_reason'] else ''
    trs=''.join(f'<tr><td>{li_name(r)}<div class="tt">{E(r["jobTitle"])}</div></td><td class="fn">{E(r["function"])}</td><td>{pill(r["load_status"])}{hr(r)}</td></tr>' for r in rs)
    sections.append(f'''
<section class="acct" id="{a.lower().replace(' ','-')}">
 <div class="wrap">
  <div class="head"><div><div class="mapname">{E(LEGAL[a])} <b>Back Office map, waves one and two</b></div><h2>{E(a)}</h2></div>
   <div class="stats"><div><b>{nready}</b>ready now</div><div><b>{len(rs)-nready}</b>held or no email</div><div><b>{later_n}</b>in later waves</div></div></div>
  <p class="why">{E(A['why'])}</p>
  <p class="opener"><span class="eyebrow">Email 1 opens with</span> Hi {{{{firstName}}}}, {E(opener.get(a,''))}</p>
  <div class="cols">
   <div><div class="eyebrow">Fresh signals</div><ul class="sigs">{sigs}</ul><p class="who"><b>Who we are reaching.</b> {E(A['call'])}</p></div>
   <div><div class="eyebrow">Loaded in lemlist</div><div class="tw"><table><thead><tr><th>Name</th><th>Reads in the email as</th><th>Status</th></tr></thead><tbody>{trs}</tbody></table></div></div>
  </div>
 </div>
</section>''')
steps=[('Day 0','Email 1','two clocks','Sends once the wave is loaded and you press start.'),('Day 1','LinkedIn connect','blank invite','Waits for your approval in lemlist before it goes.'),('Day 3','Voicemail','under 25 seconds','Only for names on the ready list; skip anyone held.'),('Day 3','LinkedIn message','after the voicemail','Waits for your approval before it goes.'),('Day 5','Email 2','the headcount cutoff','Automatic.'),('Day 8','Breakup','closing the loop','Automatic, signed with your full name.')]
stepshtml=''.join(f'<li><span class="k">{E(k)}</span><b>{E(t)}</b><span class="s">{E(s)}</span><span class="n">{E(n)}</span></li>' for k,t,s,n in steps)
holdshtml=''.join(f'<li><b>{E((r["firstName"]+" "+r["lastName"]).strip())}</b>, {E(r["parent_account"])}: {E(r["hold_reason"])}</li>' for r in holds)
page=f'''<title>Nate's Six, Wave One</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=Roboto+Mono:wght@500;600&display=swap">
<style>
:root{{--green:#2DB56E;--green-600:#228752;--green-300:#7BD3A0;--forest:#014637;--orange:#F58220;--ink:#202020;--ink-2:#5A5A5A;--ink-3:#8A8F8C;--bg:#FFFFFF;--surface:#F5F4F2;--zebra:#FAFAFA;--tint:rgba(45,181,110,.12);--tint-soft:rgba(45,181,110,.07);--otint:rgba(245,130,32,.10);--line:#E0E0E0;--line-strong:#BDBDBD;--r:8px;--eyebrow:#228752;--hero-sub:#C7DAD1;--ff:'Roboto',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;--ff-mono:'Roboto Mono',ui-monospace,SFMono-Regular,Menlo,monospace}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--ink:#EDF2EF;--ink-2:#B9C4BE;--ink-3:#8FA097;--bg:#0F1A16;--surface:#16241F;--zebra:#132019;--line:#2A3B34;--line-strong:#3C5247;--tint:rgba(45,181,110,.18);--tint-soft:rgba(45,181,110,.10);--otint:rgba(245,130,32,.16);--eyebrow:#7BD3A0}}}}
:root[data-theme="dark"]{{--ink:#EDF2EF;--ink-2:#B9C4BE;--ink-3:#8FA097;--bg:#0F1A16;--surface:#16241F;--zebra:#132019;--line:#2A3B34;--line-strong:#3C5247;--tint:rgba(45,181,110,.18);--tint-soft:rgba(45,181,110,.10);--otint:rgba(245,130,32,.16);--eyebrow:#7BD3A0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:var(--ff);background:var(--bg);color:var(--ink);line-height:1.55;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 32px}}
a{{color:var(--green-600)}} :root[data-theme="dark"] a{{color:var(--green-300)}} @media (prefers-color-scheme: dark){{:root:not([data-theme="light"]) a{{color:var(--green-300)}}}}
.eyebrow{{font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.16em;font-size:11px;font-weight:600;color:var(--eyebrow)}}
.hero{{background:var(--forest);color:#fff;padding:40px 0 34px;position:relative;overflow:hidden}}
.hero::after{{content:"";position:absolute;right:-160px;top:-120px;width:460px;height:460px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.32),transparent 62%)}}
.hero .wrap{{position:relative;z-index:1}}
.hero .logo{{height:40px;width:auto;display:block;color:#fff;margin-bottom:22px}}
.hero .eyebrow{{color:var(--green-300)}}
.hero h1{{font-weight:900;font-size:40px;line-height:1.06;margin:12px 0 12px;letter-spacing:-.02em;max-width:22ch;text-wrap:balance}}
.hero h1 .spark{{color:var(--green-300)}}
.hero p.sub{{font-size:16px;max-width:66ch;color:var(--hero-sub)}}
.hstats{{display:grid;grid-template-columns:repeat(4,auto);gap:14px 44px;justify-content:start;margin-top:24px}}
.hstats div b{{display:block;font-weight:900;font-size:32px;color:var(--green-300);letter-spacing:-.02em;line-height:1;font-variant-numeric:tabular-nums}}
.hstats div span{{display:block;font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#9DBBAE;font-weight:600;margin-top:7px}}
.nav{{margin-top:22px;display:flex;flex-wrap:wrap;gap:8px}}
.nav a{{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:#DDE9E3;text-decoration:none;border:1px solid rgba(255,255,255,.22);border-radius:100px;padding:6px 12px}}
.next{{padding:28px 0;border-bottom:1px solid var(--line);background:var(--surface)}}
.next .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:12px}}
.next .card{{background:var(--bg);border-left:4px solid var(--orange);border-radius:var(--r);padding:16px 18px}}
.next .card b{{display:block;font-weight:700;font-size:15px;margin-bottom:6px}}
.next .card p{{font-size:14px;color:var(--ink-2)}}
.seq{{padding:28px 0;border-bottom:1px solid var(--line)}}
.seq ol{{list-style:none;display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-top:12px}}
.seq li{{border:1px solid var(--line);border-radius:var(--r);padding:12px 12px 10px;background:var(--bg)}}
.seq li .k{{display:block;font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--eyebrow);font-weight:600}}
.seq li b{{display:block;font-weight:700;font-size:14px;margin-top:4px}}
.seq li .s{{display:block;font-size:12.5px;color:var(--ink-3);font-style:italic}}
.seq li .n{{display:block;font-size:12.5px;color:var(--ink-2);margin-top:6px;line-height:1.4}}
.gate{{border-left:4px solid var(--green);background:var(--tint-soft);border-radius:var(--r);padding:12px 16px;margin-top:14px;font-size:14px;color:var(--ink-2)}}
section.acct{{padding:36px 0 30px;border-bottom:1px solid var(--line)}}
.acct .head{{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}}
.acct h2{{font-weight:900;font-size:30px;line-height:1.1;letter-spacing:-.02em;margin:0}}
.acct .mapname{{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600;margin-bottom:4px}}
.acct .mapname b{{color:var(--eyebrow)}}
.stats{{display:flex;gap:26px;font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600}}
.stats b{{display:block;font-family:var(--ff);font-size:24px;font-weight:900;color:var(--ink);letter-spacing:-.01em;line-height:1.1;margin-bottom:4px;font-variant-numeric:tabular-nums}}
.why{{margin-top:14px;font-size:15.5px;max-width:78ch;color:var(--ink)}}
.cols{{display:grid;grid-template-columns:1fr 1.2fr;gap:28px;margin-top:20px;align-items:start}}
.sigs{{list-style:none;margin-top:10px;display:flex;flex-direction:column;gap:8px}}
.sigs li{{display:grid;grid-template-columns:52px 1fr auto;gap:10px;align-items:start;font-size:13.5px;padding:8px 0;border-top:1px solid var(--line)}}
.sigs li .d{{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;color:var(--ink-3);font-weight:600;padding-top:3px}}
.sigs li .t{{color:var(--ink);line-height:1.4}}
.chip{{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;padding:3px 8px;border-radius:6px;white-space:nowrap}}
.chip.strong{{background:var(--tint);color:var(--eyebrow)}} .chip.medium{{background:var(--surface);color:var(--ink-2);border:1px solid var(--line)}} .chip.weak{{color:var(--ink-3);border:1px solid var(--line)}} .chip.hold{{background:var(--otint);color:var(--orange)}}
.who{{margin-top:14px;font-size:13.5px;color:var(--ink-2)}}
.opener{{margin-top:12px;font-size:14px;color:var(--ink-2);max-width:78ch;border-left:3px solid var(--green);padding-left:12px;font-style:italic}} .opener .eyebrow{{display:block;font-style:normal;margin-bottom:3px}}
.tw{{overflow-x:auto;margin-top:10px}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}
th{{text-align:left;font-family:var(--ff-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:600;padding:6px 8px;border-bottom:1px solid var(--line-strong)}}
td{{padding:9px 8px;border-bottom:1px solid var(--line);vertical-align:top}}
tbody tr:nth-child(even) td{{background:var(--zebra)}}
td a{{font-weight:700;text-decoration:none;color:var(--ink)}} td a:hover{{text-decoration:underline}}
.tt{{font-size:12px;color:var(--ink-2);line-height:1.3;margin-top:2px}}
.fn{{font-family:var(--ff-mono);font-size:11.5px;color:var(--eyebrow);white-space:nowrap}}
.pill{{display:inline-block;font-family:var(--ff-mono);font-size:9.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;padding:3px 9px;border-radius:6px;white-space:nowrap}}
.pill.go{{background:var(--tint);color:var(--eyebrow)}} .pill.hold{{background:var(--otint);color:var(--orange)}} .pill.wait{{background:var(--surface);color:var(--ink-3);border:1px solid var(--line)}}
.hr{{font-size:11.5px;color:var(--ink-2);margin-top:5px;max-width:36ch;line-height:1.35}}
th:last-child,td:last-child{{min-width:170px}}
.holds{{padding:26px 0;border-bottom:1px solid var(--line)}}
.holds ul{{margin-top:10px;padding-left:18px;font-size:14px;color:var(--ink-2)}} .holds li{{margin-bottom:6px}}
.foot{{padding:26px 0 40px;font-size:13px;color:var(--ink-2)}}
.foot p{{max-width:80ch;margin-bottom:6px}}
h3{{font-weight:900;font-size:20px;letter-spacing:-.01em;margin-top:4px}}
@media (max-width:860px){{.cols{{grid-template-columns:1fr}}.seq ol{{grid-template-columns:repeat(2,1fr)}}.next .grid{{grid-template-columns:1fr}}.hstats{{grid-template-columns:repeat(2,auto)}}.hero h1{{font-size:32px}}}}
@media (prefers-reduced-motion: no-preference){{.hero h1,.hero p.sub,.hstats{{animation:rise .6s ease both}}.hero p.sub{{animation-delay:.12s}}.hstats{{animation-delay:.24s}}}}
@keyframes rise{{from{{opacity:.001;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
a:focus-visible{{outline:2px solid var(--orange);outline-offset:2px}}
</style>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<header class="hero"><div class="wrap">
 <svg class="logo" viewBox="0 0 187 46" role="img" aria-label="Intradiem"><use href="#ilogo"/></svg>
 <div class="eyebrow">Back office, net-new · prepared for Nathan Belfield · September 2, 2026</div>
 <h1>Six accounts, one sequence, <span class="spark">{len(ready)} names</span> loaded and waiting on you.</h1>
 <p class="sub">The back-office operations leaders at Centene, Fidelity, National Grid, Truist, Paychex and Regions, checked against Salesforce, the customer list, and the live sequences, with a verified work email on every loaded row and this month's signals behind each account. The campaign sits in draft in lemlist until you are set as sender and press start.</p>
 <div class="hstats"><div><b>6</b><span>accounts</span></div><div><b>{len(ready)}</b><span>loaded, waves one and two</span></div><div><b>{len(rows)}</b><span>on the maps</span></div><div><b>{strong}</b><span>strong signals</span></div></div>
 <nav class="nav">{''.join(f'<a href="#{a.lower().replace(" ","-")}">{E(a)}</a>' for a in ORDER)}</nav>
</div></header>
<section class="next"><div class="wrap">
 <div class="eyebrow">What you do</div>
 <div class="grid">
  <div class="card"><b>Approve each LinkedIn step</b><p>The connect (blank invite) and the message wait for you in lemlist. Approve them the day they queue; the sequence holds until you do.</p></div>
  <div class="card"><b>Call only names marked Ready</b><p>The voicemail step fires against ready rows only. Anyone marked Hold or No email stays off the phone until Dallas clears them.</p></div>
  <div class="card"><b>Reply fast, forward the rest</b><p>Replies route to you in lemlist. Anything that needs a reframe or a data fix goes back to Dallas the same day; nothing gets re-enriched in lemlist.</p></div>
 </div>
</div></section>
<section class="seq"><div class="wrap">
 <div class="eyebrow">The sequence you are running · BO Net-New, Back Office</div>
 <ol>{stepshtml}</ol>
 <div class="gate">Every email opens on the two-clocks idea and reads the person's own function into the copy (the phrase in the table). Email 1 opens on the account's own situation this month (the line at the top of each section below), then the two-clocks idea. Nothing names Intradiem, quotes a number, or says "customer."</div>
</div></section>
{''.join(sections)}
<section class="holds"><div class="wrap"><div class="eyebrow">Held this wave</div><h3>{len(holds)} names stay off the list until confirmed</h3><ul>{holdshtml}</ul></div></section>
<footer class="foot"><div class="wrap">
 <div class="eyebrow">How this list was built</div>
 <p>Rosters come from the six back-office maps built Aug 31 (150 people, every one live-verified against their LinkedIn profile). Waves one and two are the most senior operations leaders per account, about ten each; the rest follow once replies come back. Every row was swept against the Salesforce customer segment, the install base and the denylist (no hits), and against all 21 live lemlist campaigns (no overlaps).</p>
 <p>Emails come from Salesforce where the record sits at the account's own domain, otherwise from Clay's work-email waterfall with ZeroBounce validation; every address on this page is at the account's domain. The three holds were re-checked today. Signals are from public filings, releases and trade press dated in the last thirty days, linked at source.</p>
</div></footer>
'''
open(os.path.join(HERE,'Nate_NetNew_Package_Sep2.html'),'w').write(page)
print('written',len(page),'bytes; ready',len(ready),'holds',len(holds),'strong',strong)
