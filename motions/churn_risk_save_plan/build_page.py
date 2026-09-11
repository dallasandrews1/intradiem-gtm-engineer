#!/usr/bin/env python3
"""Builds Churn_Risk_Save_Plan_Sep10.html on the Intradiem GTM Engineering page system."""
import pathlib, shutil
HERE = pathlib.Path(__file__).parent
BO = HERE.parent / "back_office_expansion"
fonts = (BO / "_fonts_embed.css").read_text()
logo = (BO / "_logo_symbol.svg").read_text()

CSS = """
:root{--green:#2DB56E;--green-600:#228752;--green-300:#7BD3A0;--green-100:#C4ECD4;--forest:#014637;--orange:#F58220;--orange-600:#D96D12;--ink:#202020;--ink-2:#5A5A5A;--ink-3:#9A9A9A;--bg:#FFFFFF;--sidebar:#F5F4F2;--zebra:#FAFAFA;--tint:rgba(45,181,110,.12);--tint-soft:rgba(45,181,110,.08);--otint:rgba(245,130,32,.10);--otint-line:rgba(245,130,32,.28);--line:#E0E0E0;--r:8px;--ff:'Roboto',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;--ff-mono:'Roboto Mono',ui-monospace,SFMono-Regular,Menlo,monospace;--shadow:0 1px 2px rgba(20,30,25,.04);color-scheme:light}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--sidebar)}
body{font-family:var(--ff);background:var(--sidebar);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased}
.sheet{max-width:1120px;margin:0 auto;background:var(--bg)}
.wrap{max-width:1060px;margin:0 auto;padding:0 30px}
.eyebrow{font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.16em;font-size:11px;font-weight:600}
.logo{height:26px;width:auto;display:block;color:#014637}
a{color:var(--green-600)}
.hero{background:var(--forest);color:#fff;padding:44px 0 36px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-160px;top:-120px;width:440px;height:440px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.30),transparent 62%)}
.hero .wrap{position:relative;z-index:1}
.hero .logo{height:46px;margin-bottom:24px;color:#fff}
.hero .eyebrow{color:var(--green-300)}
.hero h1{font-weight:900;font-size:40px;line-height:1.06;margin:14px 0 14px;letter-spacing:-.02em;max-width:24ch}
.hero h1 .spark{color:var(--green-300)}
.hero p.sub{font-size:17px;max-width:66ch;color:#C7DAD1}
.hero p.sub b{color:#fff;font-weight:700}
.hero .meta{margin-top:26px;display:grid;grid-template-columns:repeat(4,auto);gap:14px 44px;justify-content:start}
.hero .meta div{color:#fff;font-size:14.5px;font-weight:500}
.hero .meta div span{display:block;font-family:var(--ff-mono);color:var(--green-300);font-size:10px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin-bottom:5px}
.hstats{display:grid;grid-template-columns:repeat(4,auto);gap:14px 44px;justify-content:start;margin-top:26px}
.hstats div b{display:block;white-space:nowrap;font-weight:900;font-size:34px;color:var(--green-300);letter-spacing:-.02em;line-height:1;font-variant-numeric:tabular-nums}
.hstats div>span{display:block;font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#9DBBAE;font-weight:600;margin-top:7px}
.hero [data-h]{opacity:0;transform:translateY(14px);transition:opacity .7s ease,transform .7s ease}
.hero [data-h="1"]{transition-delay:.05s}.hero [data-h="2"]{transition-delay:.2s}.hero [data-h="3"]{transition-delay:.4s}.hero [data-h="4"]{transition-delay:.6s}
.hero.on [data-h]{opacity:1;transform:none}
section{padding:36px 0;border-bottom:1px solid var(--line)}
section:last-of-type{border-bottom:none}
section>.wrap>.eyebrow{color:var(--green-600)}
h2{font-weight:900;font-size:28px;line-height:1.12;margin:10px 0 10px;letter-spacing:-.02em}
h3{font-weight:700;font-size:19px;margin:24px 0 8px;letter-spacing:-.01em}
p{color:var(--ink-2);max-width:78ch;margin-top:10px;font-size:15.5px}
p b,li b,td b{color:var(--ink);font-weight:700}
.tldr{background:var(--tint-soft);border:1px solid var(--tint);border-left:4px solid var(--green);border-radius:var(--r);padding:22px 28px}
.tldr .k{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--green-600);font-weight:600;margin-bottom:10px}
.tldr ul{list-style:none}
.tldr li{padding:7px 0 7px 24px;position:relative;font-size:15.5px;color:var(--ink-2)}
.tldr li::before{content:"";position:absolute;left:0;top:14px;width:7px;height:7px;border-radius:2px;background:var(--green)}
.tldr li b{color:var(--ink)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:20px}
.grid.c3{grid-template-columns:repeat(3,1fr)}
.card{background:var(--bg);border:1px solid var(--line);border-radius:var(--r);padding:20px 22px;box-shadow:var(--shadow)}
.card h4{font-size:17px;font-weight:700;margin-bottom:6px;letter-spacing:-.01em}
.card p{font-size:14.5px;margin-top:0;max-width:none}
.card ul{list-style:none;margin-top:6px}
.card li{padding:4px 0 4px 20px;position:relative;font-size:14.5px;color:var(--ink-2)}
.card li::before{content:"\\2192";position:absolute;left:0;color:var(--green-600);font-weight:700}
.tag{display:inline-block;font-family:var(--ff-mono);font-size:10px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;padding:4px 10px;border-radius:6px;margin-bottom:12px}
.tag.go{background:var(--tint);color:var(--green-600)}
.tag.now{background:#FDECD9;color:var(--orange-600)}
.tag.hold{background:var(--zebra);color:var(--ink-3);border:1px solid var(--line)}
.statband{display:grid;grid-template-columns:repeat(5,1fr);gap:22px;background:var(--forest);border-radius:var(--r);padding:24px 32px;margin-top:22px;position:relative;overflow:hidden}
.statband::after{content:"";position:absolute;right:-130px;top:-150px;width:360px;height:360px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.22),transparent 62%)}
.statband>div{position:relative;z-index:1}
.statband .n{font-weight:900;font-size:26px;color:var(--green-300);letter-spacing:-.01em;line-height:1.1;white-space:nowrap}
.statband .l{font-family:var(--ff-mono);font-size:10px;letter-spacing:.1em;color:#9DBBAE;text-transform:uppercase;margin-top:9px;line-height:1.6}
.callout{background:var(--otint);border:1px solid var(--otint-line);border-left:4px solid var(--orange);border-radius:var(--r);padding:18px 24px;margin-top:20px}
.callout h4{font-size:17px;font-weight:700;color:var(--orange-600);margin-bottom:6px}
.callout p{font-size:14.5px;margin-top:0;max-width:none}
.gate{background:var(--tint-soft);border:1px solid var(--tint);border-left:4px solid var(--green);border-radius:var(--r);padding:18px 24px;margin-top:20px}
.gate h4{font-size:17px;font-weight:700;color:var(--green-600);margin-bottom:6px}
.gate p{font-size:14.5px;margin-top:0;max-width:none}
.tablewrap{overflow-x:auto;margin-top:16px}
table{width:100%;border-collapse:collapse;font-size:14px}
th{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);text-align:left;padding:0 14px 10px 0;border-bottom:1px solid var(--line);font-weight:600}
td{padding:10px 14px 10px 0;border-bottom:1px solid var(--line);color:var(--ink-2);vertical-align:top}
tr:last-child td{border-bottom:none}
tbody tr:nth-child(even){background:var(--zebra)}
td.who{white-space:nowrap;color:var(--ink);font-weight:700}
td.st{font-family:var(--ff-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);white-space:nowrap}
.steps{list-style:none;margin-top:18px;border-top:1px solid var(--line)}
.steps li{display:grid;grid-template-columns:44px 1.1fr 150px 1.6fr;gap:18px;align-items:center;padding:13px 0;border-bottom:1px solid var(--line)}
.steps .n{width:34px;height:34px;border-radius:6px;background:var(--forest);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:16px}
.steps .t{font-weight:700;font-size:16px;letter-spacing:-.01em;color:var(--ink)}
.steps .o{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.steps .r{font-size:14.5px;color:var(--ink-2)}
.cal{list-style:none;margin-top:16px;border-top:1px solid var(--line)}
.cal li{display:grid;grid-template-columns:150px 1fr 1.4fr;gap:18px;padding:11px 0;border-bottom:1px solid var(--line);font-size:14.5px;align-items:baseline}
.cal .d{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600);font-weight:600}
.cal .e{font-weight:700;color:var(--ink)}
.cal .r{color:var(--ink-2)}
.threads{list-style:none;margin-top:16px;max-width:820px}
.threads li{padding:12px 0 12px 30px;position:relative;font-size:15px;color:var(--ink-2);border-bottom:1px solid var(--line)}
.threads li:last-child{border-bottom:none}
.threads li::before{content:"";position:absolute;left:6px;top:19px;width:8px;height:8px;border-radius:2px;background:var(--green)}
.threads li b{color:var(--ink)}
.pill{display:inline-block;font-family:var(--ff-mono);font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;padding:3px 9px;border-radius:6px;white-space:nowrap}
.pill.go{background:var(--tint);color:var(--green-600)}
.pill.now{background:#FDECD9;color:var(--orange-600)}
.pill.hold{background:var(--zebra);color:var(--ink-3);border:1px solid var(--line)}
.pill.red{background:#FDE3E3;color:#B42318}
.foot{padding:26px 0 46px;text-align:center;color:var(--ink-3);font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;background:var(--bg);text-transform:uppercase}
.foot .logo{height:26px;display:inline-block;margin:0 auto 12px;opacity:.85}
.foot span{display:block;margin-top:4px}
.rv{opacity:0;transform:translateY(14px);transition:opacity .6s ease,transform .6s ease;transition-delay:calc(var(--i,0)*.07s)}
tr.rv{transform:none}
.rv.on{opacity:1;transform:none}
@media(max-width:760px){.hero h1{font-size:30px}.hero .meta,.hstats{grid-template-columns:1fr 1fr}.grid,.grid.c3{grid-template-columns:1fr}.statband{grid-template-columns:1fr 1fr}.steps li{grid-template-columns:44px 1fr}.steps .o,.steps .r{grid-column:2}.cal li{grid-template-columns:1fr}}
@media print{html,body{background:#fff}.hero [data-h],.rv{opacity:1!important;transform:none!important}section{break-inside:avoid}}
"""

BODY = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true">%(logo)s</svg>
<div class="sheet">
<header class="hero" id="hero"><div class="wrap">
<svg class="logo" data-h="1"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">Customer retention &middot; churn-risk accounts</div>
<h1 data-h="2">One save plan per at-risk account, <span class="spark">owned and on a clock.</span></h1>
<p class="sub" data-h="3">Built from Salesforce, the Success Plan, Sales Navigator and meeting notes. Each owner gets their items weekly. Mary Ann gets one line per account. The PMO list stays the record.</p>
<div class="hstats" data-h="4">
<div><b data-n="3">0</b><span>accounts at risk</span></div>
<div><b data-n="89">0</b><span>Cleveland Clinic contacts in Salesforce</span></div>
<div><b data-n="16">0</b><span>names Inger found</span></div>
<div><b data-n="20">0</b><span>back-office leaders mapped</span></div>
</div>
<div class="meta" data-h="4">
<div><span>Prepared for</span>Dallas, internal read</div>
<div><span>By</span>GTM Engineering</div>
<div><span>Date</span>Sep 10 2026</div>
<div><span>Source</span>Inger call, her plan, the PMO list</div>
</div>
</div></header>

<section><div class="wrap">
<div class="tldr rv"><div class="k">The read</div><ul>
<li><b>Inger asked for three things:</b> new people at the table in accounts where the sponsor blocks, one place that shows who is doing what inside each account, and next steps that reach people without a spreadsheet or a Slack channel. Her constraint: no new noise.</li>
<li><b>The problem is not a missing tracker.</b> Actions have no owner, no date and no visibility, so a brainstorm six weeks ago produced work from one person. The Progress tracker list she and Nicole started in the PMO hub is the right record. What is missing is the plan being generated into it and the nudge going to the owner.</li>
<li><b>Recommendation:</b> keep the PMO list as the record. Add a generated Save Room page per account, a weekly health watcher with reason codes, an owner digest that rolls overdue items up to Mary Ann, and two lemlist tracks.</li>
<li><b>Cleveland Clinic first.</b> The clock is the CCaaS RFP plus the January renewal, and the savings dispute from last November has to be settled before anyone widens to executives.</li>
</ul></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Cleveland Clinic</div>
<h2>What the account data already says</h2>
<div class="statband rv">
<div><div class="n">13 of 17</div><div class="l">contracted use cases live</div></div>
<div><div class="n">17.8%%</div><div class="l">dynamic session accept, goal 75%%</div></div>
<div><div class="n">7%%</div><div class="l">agents coached, goal 80%%</div></div>
<div><div class="n">Jun 12</div><div class="l">Leave Early and End of Shift rules paused</div></div>
<div><div class="n">$719K</div><div class="l">YTD savings, 1.9x, disputed by the customer</div></div>
</div>
<div class="grid">
<div class="card rv"><span class="tag now">Where trust broke</span><h4>Nov 6 2025 success review</h4><p>Five slides in, the customer challenged savings accuracy, unmet feature commitments and open cases, and said they added staff to run Intradiem. Amy, Matt and Mary Ann committed to a line-by-line ROI review. The Success Plan still carries that item as open. Weekly meetings since have been cancelled by Shantel more often than held.</p></div>
<div class="card rv"><span class="tag now">The real clock</span><h4>RFP, Harmonic, January</h4><p>An RFP is out for the CCaaS stack. Harmonic migration conversations are starting. Two renewal options are on the table for January. Inger's read: a one-year renewal, a migration, then an exit. The RFP evaluators are the people she found, and the verified line for them is that Intradiem sits on top of whatever platform they pick.</p></div>
</div>
<div class="callout rv"><h4>Sequence matters</h4><p>Widening to the CFO and COO with a savings number the customer already disputes is the one move that speeds the exit. Settle the number with Shantel and Rena first, get the supervisors who use Coach Now on record (83%% acceptance is the bright spot), then widen with the RFP-continuity message.</p></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">The system</div>
<h2>Five parts around the list they already have</h2>
<ul class="steps">
<li class="rv"><div class="n">1</div><div><div class="t">Record: PMO Progress tracker list</div><div class="o">Inger, Nicole, Clint</div></div><div class="o">SharePoint</div><div class="r">One row per action: account, owner, due date, status, evidence link. Clint's format stays. Nothing else becomes a second list.</div></li>
<li class="rv"><div class="n">2</div><div><div class="t">Save Room page per account</div><div class="o">Dallas builds, AM edits status</div></div><div class="o">generated page</div><div class="r">Contacts in three layers (in Salesforce, AM research, net-new map), health with the reason and its evidence, the 30/60/90 with owners, open items mirrored from the list. Same pattern as the back-office maps.</div></li>
<li class="rv"><div class="n">3</div><div><div class="t">Health watcher, weekly</div><div class="o">scheduled job, log only</div></div><div class="o">automation</div><div class="r">Reads the Success Plan notes, the monthly adoption deck, Sales Navigator alerts, Otter meetings and Salesforce activity. Sets red, yellow or green with a reason code and the line of evidence. Writes a log the daily rundown reads.</div></li>
<li class="rv"><div class="n">4</div><div><div class="t">Owner digest, Monday</div><div class="o">scheduled job</div></div><div class="o">Outlook or Teams</div><div class="r">Each owner gets one message with only their open items, due dates and the room link. Overdue items roll up into Mary Ann's one line per account. Nobody has to open the list to know what is theirs.</div></li>
<li class="rv"><div class="n">5</div><div><div class="t">Two lemlist tracks</div><div class="o">Dallas builds, AM clears, marketing supplies content</div></div><div class="o">lemlist</div><div class="r">Nurture: monthly one-pager to known contacts, set once. Stakeholder: a short sequence to net-new names after the AM clears them, with the account's own language, not a template.</div></li>
</ul>
<h3>Reason codes the watcher can set</h3>
<div class="tablewrap"><table>
<thead><tr><th>Code</th><th>Trigger</th><th>Source</th></tr></thead><tbody>
<tr class="rv"><td class="who">Sponsor silence</td><td>Two or more cancelled or no-show meetings in four weeks</td><td>Success Plan notes, Outlook calendar</td></tr>
<tr class="rv"><td class="who">Adoption decline</td><td>Accept rate under goal two months running, or a rule paused</td><td>Monthly adoption deck</td></tr>
<tr class="rv"><td class="who">Open case aging</td><td>Support case open past 30 days</td><td>Success Plan notes, Salesforce cases</td></tr>
<tr class="rv"><td class="who">Executive change</td><td>Sponsor, blocker or evaluator changes role</td><td>Sales Navigator alert emails (already read weekly)</td></tr>
<tr class="rv"><td class="who">Competitive event</td><td>RFP, vendor evaluation, platform migration</td><td>Meeting notes, AM input, web</td></tr>
<tr class="rv"><td class="who">Renewal clock</td><td>Inside 120 days with no option signed</td><td>Salesforce</td></tr>
</tbody></table></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Inger's question</div>
<h2>Where her sixteen names fit</h2>
<p>Two are in Salesforce. Two are already on the back-office map. Twelve are new to every list we hold. None has a validated email yet.</p>
<div class="tablewrap"><table>
<thead><tr><th>Name</th><th>Title</th><th>Layer</th><th>Role in the save</th><th>Track</th></tr></thead><tbody>
<tr class="rv"><td class="who">Rena Thompson</td><td>Director, Enterprise Contact Center Operations</td><td class="st">in Salesforce, Inger's map</td><td>Sponsor. Owns the savings conversation.</td><td><span class="pill hold">Inger</span></td></tr>
<tr class="rv"><td class="who">Scott Faini</td><td>IT Product Director, Unified Communications</td><td class="st">in Salesforce, Inger's map</td><td>RFP voice. Platform continuity.</td><td><span class="pill go">Stakeholder</span></td></tr>
<tr class="rv"><td class="who">Katherine Neal</td><td>IT Director, Access Innovations</td><td class="st">new</td><td>RFP evaluator, peer to Faini</td><td><span class="pill go">Stakeholder</span></td></tr>
<tr class="rv"><td class="who">Bob Ganem</td><td>ITD Director and Product Owner</td><td class="st">new</td><td>RFP evaluator</td><td><span class="pill go">Stakeholder</span></td></tr>
<tr class="rv"><td class="who">Leslie Chom</td><td>Director, Patient and Caregiver Computing</td><td class="st">new</td><td>RFP evaluator</td><td><span class="pill go">Stakeholder</span></td></tr>
<tr class="rv"><td class="who">Terri Horan</td><td>Product Owner, Patient Journey</td><td class="st">new</td><td>Patient-experience angle on agent time</td><td><span class="pill go">Stakeholder</span></td></tr>
<tr class="rv"><td class="who">Dennis Laraway</td><td>EVP and CFO</td><td class="st">new</td><td>Economic buyer. Only after the number holds.</td><td><span class="pill now">Hold, then exec</span></td></tr>
<tr class="rv"><td class="who">Bill Peacock</td><td>EVP, Chief of Operations</td><td class="st">new</td><td>Top of operations. Mary Ann's touch, same gate.</td><td><span class="pill now">Hold, then exec</span></td></tr>
<tr class="rv"><td class="who">Kelly Hancock</td><td>EVP, Chief Caregiver and Chief Administrative Officer</td><td class="st">on back-office map</td><td>Distinct line from the sponsor. Expansion, not the save.</td><td><span class="pill go">Back office</span></td></tr>
<tr class="rv"><td class="who">Emily Monteleone</td><td>Director, Strategic Workforce Planning</td><td class="st">on back-office map</td><td>Workforce planning lane</td><td><span class="pill go">Back office</span></td></tr>
<tr class="rv"><td class="who">Rebecca Vance</td><td>Senior HR Director, Connected Care, Nursing, Pharmacy</td><td class="st">new</td><td>Caregiver office, consulted on workforce</td><td><span class="pill hold">Nurture</span></td></tr>
<tr class="rv"><td class="who">Meredith Foxx</td><td>SVP, Enterprise Chief Nursing Officer</td><td class="st">new</td><td>Triage lines, burnout. Low fit for the save.</td><td><span class="pill hold">Nurture</span></td></tr>
<tr class="rv"><td class="who">Sonya Pease</td><td>Chief of Quality, Safety, Patient Experience, Florida</td><td class="st">new</td><td>Regional, clinical</td><td><span class="pill hold">Bench</span></td></tr>
<tr class="rv"><td class="who">F. Scott Ross, Richard Rothman, David (Florida)</td><td>Regional hospital operations</td><td class="st">new</td><td>Outside the contact center decision</td><td><span class="pill hold">Bench</span></td></tr>
</tbody></table></div>
<div class="gate rv"><h4>Verified line for the RFP evaluators</h4><p>Intradiem sits on top of the existing WFM and integrates with Genesys Cloud, NICE and others without replacing them. This is in the Value Repository and is the message for Faini, Neal, Ganem and Chom while the RFP runs. Any savings figure used with the CFO or COO must be the reviewed one, not the disputed deck number.</p></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Cleveland Clinic</div>
<h2>Ninety days to the renewal decision</h2>
<ul class="cal">
<li class="rv"><div class="d">To Oct 10</div><div class="e">Settle the number, staff the room</div><div class="r">ROI line-by-line with Shantel closes (Amy, Matt). Case closure dates in writing. Coach Now supervisors on record. Save Room live, owners assigned in Inger's brainstorm, digest starts the Monday after.</div></li>
<li class="rv"><div class="d">To Nov 9</div><div class="e">Continuity with the RFP evaluators</div><div class="r">Faini and the three IT product owners hear platform continuity from Inger and one technical voice. Harmonic presented as continuity, not a project. Executive review with Yerian. CFO note only if the reviewed number holds.</div></li>
<li class="rv"><div class="d">To Dec 9</div><div class="e">Option chosen, expansion separated</div><div class="r">Renewal option selected. Hancock line approached as back-office expansion, on its own track, after the renewal conversation is stable.</div></li>
</ul>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Inger's plan</div>
<h2>What to keep, what to change</h2>
<div class="grid">
<div class="card rv"><span class="tag go">Keep</span><h4>Bottom-up proof and peer backchannels</h4><p>The adoption numbers are weak, so user testimony is the strongest evidence available. The supervisors accepting coaching and the teams self-curing AUX alerts at 94%% are the voices to collect. Peer-to-peer introductions from those teams are the cleanest route around a blocker.</p></div>
<div class="card rv"><span class="tag now">Change</span><h4>The risk-frame email</h4><p>"What you lose in January if the system shuts down" reads as a threat to a customer who is already frustrated, and it invites the reply that they can live without it. Replace with continuity: the reviewed savings, the RFP-agnostic integration, and the migration plan. Templates need Cleveland Clinic's own language, drawn from the Success Plan notes.</p></div>
</div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Open</div>
<h2>Decisions and dependencies</h2>
<ul class="threads">
<li class="rv"><b>The PMO list itself.</b> The Microsoft connector reads SharePoint files, not lists, so the Progress tracker could not be opened here. Reading it needs an export, and writing to it needs a Graph list permission or a Power Automate flow. Until then the Save Room mirrors the list from an export.</li>
<li class="rv"><b>Digest channel.</b> AMs and Success live in Outlook and Teams, GTM lives in Slack. One message per owner in the tool they already open.</li>
<li class="rv"><b>Which job runs the watcher.</b> The Sales Navigator alert reader and the meeting capture already run weekly and daily. The watcher extends them rather than adding a third reader of the same sources.</li>
<li class="rv"><b>Rogers and the third account.</b> Same pattern, names and renewal dates needed from Inger.</li>
</ul>
</div></section>

<footer class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; churn-risk save plan &middot; Sep 10 2026</span><span>Internal. Figures from the Cleveland Clinic Success Plan and the September 2026 adoption review.</span></footer>
</div>
<script>
(function(){
  var h=document.getElementById('hero');setTimeout(function(){h.classList.add('on')},60);
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.08});
  document.querySelectorAll('.rv').forEach(function(el,i){el.style.setProperty('--i',i%%8);io.observe(el)});
  setTimeout(function(){document.querySelectorAll('.rv').forEach(function(el){el.classList.add('on')})},1400);
  document.querySelectorAll('[data-n]').forEach(function(el){var t=+el.getAttribute('data-n'),s=0,st=Date.now();var iv=setInterval(function(){var p=Math.min(1,(Date.now()-st)/900);el.textContent=Math.round(t*(1-Math.pow(1-p,3)));if(p>=1)clearInterval(iv)},30)});
})();
</script>
"""

html = ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<meta name=\"robots\" content=\"noindex,nofollow\"><title>Churn-Risk Save Plan</title><style>" + fonts + CSS + "</style></head><body>"
        + BODY % {"logo": logo} + "</body></html>")
out = HERE / "Churn_Risk_Save_Plan_Sep10.html"
out.write_text(html)
dest = pathlib.Path.home() / "Desktop" / "Intradiem Deliverables" / "Churn-Risk Save Plan - Sep 10.html"
shutil.copy(out, dest)
print(out, len(html)); print(dest)
