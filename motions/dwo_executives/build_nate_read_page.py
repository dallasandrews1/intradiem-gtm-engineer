#!/usr/bin/env python3
"""Build the DWO executives Nate-read page (branded, Intradiem page system) from the load plan and the live lemlist sequence.
Usage: build_nate_read_page.py <scratch>  -> writes DWO_Executives_Nate_Read_Sep4.html here and on the Desktop."""
import json,os,sys,re,html,collections
SP=sys.argv[1]; HERE=os.path.dirname(os.path.abspath(__file__))
TPL=os.path.expanduser('~/Desktop/Intradiem Deliverables/Nate_Copy_Rewrite_Sep3.html')
css=re.search(r'<style>(.*?)</style>',open(TPL).read(),re.S).group(1)
logo=open(f'{SP}/ilogo.svg').read()
P=json.load(open(f'{SP}/dwo_shell_plan.json')); plan=P['plan']; skipped=P['skipped']
seq=json.load(open(f'{SP}/dwo_sequence_live.json'))['seq_XiYpoRMDksmH7c93u']['steps']
E=html.escape
def txt(h): return html.unescape(re.sub(r'<div>|<p>','',re.sub(r'</div>|</p>|<br>','\n',h or ''))).strip()
def paras(t): return ''.join(f'<p>{E(x)}</p>' for x in [x for x in t.split('\n') if x.strip()])
n=len(plan); accts=len({r['account'] for r in plan}); ruleA=sum(1 for r in plan if r['opener_rule']=='A')
arms=collections.Counter(r['cohortArm'] for r in plan); armacc={a:len({r['domain'] for r in plan if r['cohortArm']==a}) for a in ('test','holdout')}
vert=collections.Counter(r['vertical'] for r in plan); fam=collections.Counter(r['e1_variant'] for r in plan)
flag=[r for r in plan if r.get('flag')]
skc=collections.Counter(s['reason'].split(':')[0] for s in skipped)
# rendered examples
def render(r,variant='A'):
    a={'core':0,'customer':1,'transformation':2}
    body=[f"Hi {r['firstName']},",r['opener'],r['angleIdea'],r['angleProof'],(r['angleAsk'] if variant=='A' else "Would it help if I sent a short note on how operations leaders size that number for their own teams? No meeting attached, I'll just send it."),"Nathan"]
    return f"<div class='mail'><div class='subj'>Subject: idle minutes at {E(r['companyName'])}</div>"+''.join(f'<p>{E(x)}</p>' for x in body)+"</div>"
exA=[r for r in plan if r['opener_rule']=='A' and r['e1_variant']=='core'][0]
exB=[r for r in plan if r['opener_rule']=='B' and r['e1_variant']=='customer' and r['family']=='COO/ops'][0]
exC=[r for r in plan if r['family']=='CAO' and r['e1_variant']=='core'][0]
exT=[r for r in plan if r['e1_variant']=='transformation'][0]
def meta(r): return f"<div class='who'>{E(r['name'])}, {E(r['title'])}, {E(r['account'])} ({E(r['vertical'])}). Opener rule {r['opener_rule']}, angle: {r['e1_variant']}, cohort arm: {r['cohortArm']}.</div>"
steps_html=''
labels={0:'Email 1, day 1 (A/B: benchmark question vs offer note)',1:'LinkedIn connect, day 2',2:'Email 2 in thread, day 4',3:'LinkedIn message, day 7',4:'Email 3, breakup, day 11'}
for s in seq:
    i=s['sequenceStep']; body=txt(s.get('message'))
    if i==0:
        body=body.replace("There's a cost in there you pay twice: idle minutes inside the shift, and overtime after it to clear what didn't get done.","{{angleIdea}}").replace("That's what Intradiem does. It sits on top of the WFM and case systems your {{workTeams}} already run and moves work, training and breaks into the idle windows as they open, contact center and back office. Humana has it on the record: two hours back per agent per month, and 7X five years in.","{{angleProof}}").replace("Worth a conversation on how much of {{companyName}}'s overtime is idle time in disguise?","{{angleAsk}}")
    steps_html+=f"<div class='card'><span class='tag go'>{E(labels[i])}</span>"+(f"<p><b>Subject:</b> {E(s.get('subject') or '(in thread)')}</p>" if s.get('type')=='email' else '')+paras(body)+"</div>"
angles=[('core','COO, operations and CAO seats (450 people)',"There's a cost in there you pay twice: idle minutes inside the shift, and overtime after it to clear what didn't get done.","...moves work, training and breaks into the idle windows as they open, contact center and back office. Humana has it on the record: two hours back per agent per month, and 7X five years in.","Worth a conversation on how much of {{companyName}}'s overtime is idle time in disguise?"),
 ('customer','Customer, experience and service seats, and the second person at an account (160)',"In service operations the trade usually gets framed as cost or experience. The idle minutes inside the shift are the one lever that moves both: coaching and training happen in the quiet windows instead of never, and the busy windows get the people back.","...spots idle windows as they open, and moves work, coaching and breaks into them, contact center and back office. Humana has it on the record: two hours of capacity back per agent per month, and handle time down 45 seconds.","Worth a conversation on where {{companyName}}'s coaching hours actually come from today?"),
 ('transformation','Transformation seats, and the third person at an account (90)',"Most of a change portfolio is modelled benefit. Intraday capacity is the known number: it's already on the payroll, and it runs as rules on top of the systems you already govern, nothing new to stand up.","...spots idle windows as they open, and moves work, training and breaks into them, contact center and back office. Humana has it on the record: the return landed inside the first year, and 7X five years in.","Worth a conversation on whether that belongs in {{companyName}}'s roadmap as the certain line?")]
angle_html=''.join(f"<div class='card'><span class='tag now'>{E(k)}</span><h4>{E(who)}</h4><p><b>angleIdea</b> {E(a)}</p><p><b>angleProof</b> That's what Intradiem does. It sits on top of the WFM and case systems your {{{{workTeams}}}} already run and {E(b[3:])}</p><p><b>angleAsk</b> {E(c)}</p></div>" for k,who,a,b,c in angles)
flag_rows=''.join(f"<tr><td class='who'>{E(r['name'])}</td><td>{E(r['title'])}</td><td>{E(r['account'])}</td></tr>" for r in flag)
inbo=[s for s in skipped if s['reason'].startswith('already')]
inbo_rows=''.join(f"<tr><td class='who'>{E(s['name'])}</td><td>{E(s['title'])}</td><td>{E(s['account'])}</td><td class='st'>{E(s['reason'].split(': ',1)[1])}</td></tr>" for s in inbo)
skip_rows=''.join(f"<tr><td class='who'>{E(k)}</td><td>{v}</td><td>{E({'no verified email (LinkedIn-first variant later)':'Stays on the lemlist list as needs_email. A LinkedIn-first variant of this sequence picks them up once the email backlog runs.','title filter':'Chief of staff, deputy, associate, assistant, chief nursing, chief medical, specialist, analyst, office of. Kept on the list, not loaded.','held (moved company)':'The free LinkedIn bridge found them at another company. Held.','already a lead in':'Loaded in BO Net-New on Sep 2. One motion per person; they stay there.','disputed email':'mm@fidelity.com was staged under two names. Needs re-resolving before anyone sends to it.','account/company disagree':'Search matched the person to an account whose name does not match their current employer. Held.'}.get(k,''))}</td></tr>" for k,v in skc.most_common())
vert_rows=''.join(f"<tr><td class='who'>{E(v)}</td><td>{c}</td><td>{len({r['account'] for r in plan if r['vertical']==v})}</td><td>{E({'Healthcare':'open enrollment','Insurance':'the Q4 claims and renewal peak','Financial Services':'year-end close','Utilities':'the winter season','Retail':'holiday peak','Telecom':'device season'}[v])}</td></tr>" for v,c in vert.most_common())
top=sorted(collections.Counter(r['account'] for r in plan).items(),key=lambda kv:-kv[1])[:8]
top_rows=''.join(f"<tr><td class='who'>{E(a)}</td><td>{c}</td><td>{E(', '.join(sorted({r['e1_variant'] for r in plan if r['account']==a})))}</td></tr>" for a,c in top)
prompt=E("""Load the DWO shell. Run, in this order, nothing else:
1. In lemlist campaign cam_SiD4KmWcRuhiF6uhL (draft, 0 leads), sequence seq_XiYpoRMDksmH7c93u, step stp_vQd7kTCL3DpDgkryR: replace the three fixed paragraphs of Email 1 (variant A and variant B) with {{angleIdea}}, {{angleProof}}, {{angleAsk}}; keep the greeting, {{opener}}, the A/B closings and the sign-off exactly as they are. Preview the diff first, then apply.
2. python3 motions/dwo_executives/load_dwo_shell.py <scratch> --go   (700 leads, cohort GTMENG-DWO1-2026-09 with test/holdout arm on every lead, motionStatus loaded). Read the loaded count back from lemlist.
3. Run the lemlist-lead-integrity check on cam_SiD4KmWcRuhiF6uhL and preview Email 1 for three leads (one rule A, one customer angle, one CAO).
Do not launch, do not change the sender, do not touch any other campaign.""")
page=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>DWO executives, wave 1: Nate's read (Sep 4 2026)</title>
<style>{css}
.mail{{background:var(--zebra);border:1px solid var(--line);border-radius:var(--r);padding:18px 22px;margin-top:10px}}
.mail .subj{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600);font-weight:600;margin-bottom:8px}}
.mail p{{margin-top:8px;font-size:15px;color:var(--ink)}}
.who{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.04em;color:var(--ink-3);margin-top:18px}}
pre.prompt{{background:var(--forest);color:#E9F3EE;border-radius:var(--r);padding:20px 24px;font-family:var(--ff-mono);font-size:12.5px;line-height:1.55;white-space:pre-wrap;margin-top:14px}}
.card p{{margin-top:8px}}
</style></head><body><div class="sheet">
<svg width="0" height="0" style="position:absolute">{logo}</svg>
<div class="hero on"><div class="wrap">
<svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">GTM Engineering · DWO executives · wave 1 · Nate's read · Sep 4 2026</div>
<h1 data-h="2">{n} operating executives at {accts} accounts, <span class="spark">ready for your read.</span></h1>
<p class="sub" data-h="3">Every one sourced live this week, current in role, verified email, no current customer or partner. The five-touch sequence sits in lemlist as a draft with zero leads. <b>Nothing loads and nothing sends until you and Dallas say so.</b></p>
<div class="hstats" data-h="4"><div><b>{n}</b><span>leads ready to load</span></div><div><b>{accts}</b><span>accounts, cap 10 each</span></div><div><b>{ruleA}</b><span>new in role, six months or less</span></div><div><b>0</b><span>sends</span></div></div>
</div></div>

<section><div class="wrap"><div class="tldr"><div class="k">The read in five lines</div><ul>
<li><b>Who:</b> COOs, CAOs, customer and service chiefs, transformation chiefs at six-vertical US prospects. C-level only in wave 1; EVP, SVP and Head titles are wave 2.</li>
<li><b>One idea, three angles:</b> the operation pays for capacity twice, idle minutes inside the shift and overtime after it. No two people at one account get the same angle.</li>
<li><b>Numbers in the copy:</b> only the Humana on-the-record set (two hours per agent per month, 7X five years in, 12,000 VTO hours, handle time down 45 seconds, first-year return). Nothing else.</li>
<li><b>Your calls on this page:</b> {len(flag)} provider-system unit COOs to keep or drop, the opt-out line, and the sending mailbox.</li>
<li><b>Lane B pilot rides on this wave:</b> half the accounts also get LinkedIn ads three days before Email 1, half get the sequence only, so the council row gets its own cost per meeting.</li>
</ul></div></div></section>

<section><div class="wrap"><div class="eyebrow">Where the pool went</div><h2>1,135 sourced, {n} loadable, the rest held with a reason</h2>
<p class="lede">Wave 1 was the 1,135 C-level operating executives found by live Clay search this week. Verified email is the load gate; the rest stay on the lemlist list with a status, never in a campaign.</p>
<div class="tablewrap"><table><thead><tr><th>Held or skipped</th><th>People</th><th>What it means</th></tr></thead><tbody>{skip_rows}</tbody></table></div>
<div class="grid" style="margin-top:22px"><div class="card"><h4>By vertical</h4><div class="tablewrap"><table><thead><tr><th>Vertical</th><th>People</th><th>Accounts</th><th>Peak in Email 3</th></tr></thead><tbody>{vert_rows}</tbody></table></div></div>
<div class="card"><h4>Largest accounts</h4><div class="tablewrap"><table><thead><tr><th>Account</th><th>People</th><th>Angles used</th></tr></thead><tbody>{top_rows}</tbody></table></div></div></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">The sequence, as it sits in lemlist</div><h2>Five touches over eleven days, no phone step</h2>
<p class="lede">C-level seats get email and LinkedIn only. Email 1 splits A/B: a benchmark question against an offer note. The three paragraphs in the middle of Email 1 become per-lead variables at load so the angle can change by person; everything else on this page is verbatim from the draft.</p>
<div class="grid">{steps_html}</div>
<h3>The three angles that fill Email 1</h3>
<div class="grid c3">{angle_html}</div>
<div class="gate"><h4>Claims gate</h4><p>Every number above is Humana, on the record at a public SWPP webinar, cleared for one-to-many use. No value-deck figures, no ranges, no other customers. If a reply asks for more, that is the conversation, not the email.</p></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">Rendered</div><h2>What four real people would receive</h2>
{meta(exA)}{render(exA)}
{meta(exB)}{render(exB,'B')}
{meta(exC)}{render(exC)}
{meta(exT)}{render(exT)}
<p style="margin-top:16px">Openers: people six months or less into the seat get the new-in-role line ({ruleA} of {n}). Everyone else gets the dated vertical peak line, which a per-account war-room signal replaces wherever one exists (none of the 285 accounts has one staged today).</p>
</div></section>

<section><div class="wrap"><div class="eyebrow">Your calls</div><h2>Three decisions before the load, all yours</h2>
<div class="grid">
<div class="card"><span class="tag now">1 · provider-system unit COOs</span><h4>{len(flag)} hospital and medical-group COOs</h4><p>Health-system COOs run patient access, billing and revenue cycle, which is the back-office story. Unit-level ones (a hospital, a medical group, a market) are weaker seats for it. They are in the load plan and flagged; say drop and they hold.</p></div>
<div class="card"><span class="tag now">2 · opt-out line</span><h4>Dropped from Email 1 to keep it at the ceiling</h4><p>US market, C-level, no obligation. If you want it back in your voice, it goes on the last line of Email 1 and Email 3. Say the words and it lands before load.</p></div>
<div class="card"><span class="tag now">3 · mailbox</span><h4>Sends go from nathan.belfield@intradiemhq.com, not the main</h4><p>The warm mailbox is active in lemlist, DNS scores 100 of 100, four days old. The campaign is still on the main mailbox and gets switched the day lemwarm clears it (Sep 21 to 28). Loading does not change this.</p></div>
<div class="card"><span class="tag hold">already elsewhere</span><h4>{len(inbo)} people stay in BO Net-New</h4><div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Account</th><th>Where</th></tr></thead><tbody>{inbo_rows}</tbody></table></div></div>
</div>
<h3>The {len(flag)} flagged seats</h3>
<div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Account</th></tr></thead><tbody>{flag_rows}</tbody></table></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">Lane B pilot</div><h2>Half the accounts get ads on the same clock, so the row gets a number</h2>
<div class="statband"><div><div class="n">{arms['test']}</div><div class="l">test arm, {armacc['test']} accounts: LinkedIn ads plus the sequence</div></div><div><div class="n">{arms['holdout']}</div><div class="l">holdout, {armacc['holdout']} accounts: sequence only</div></div><div><div class="n">T-3</div><div class="l">ads live three business days before Email 1, off at day 25</div></div><div><div class="n">1</div><div class="l">Salesforce campaign: GTM Eng - DWO Executives - Wave 1</div></div></div>
<p>Split is by account, the same rule the cohort cutter uses, so an account is never in both arms. Each lead carries the cohort id and its arm as lead fields, and the stamp plan for Sales Ops carries them too. The ads list (test arm, LinkedIn list-upload columns) is written and goes to Melissa and Sierra the day the launch date is set, not before.</p>
<div class="callout"><h4>What the ads need from marketing</h4><p>A LinkedIn Matched Audience from the CSV (LinkedIn's floor is 300 matched; the test arm has {arms['test']} rows with email and name plus company), one creative on the idle-minutes idea, and a landing page that is the same idea, not a product page. Spend is theirs; the meetings land on our row either way.</p></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">Order of operations</div><h2>What happens on go, in the order that cannot bite</h2>
<ol class="steps">
<li><div class="n">1</div><div class="t">Nate's read</div><div class="o">Nate</div><div class="r">This page. Three calls above, plus any line you would not say on the phone.</div></li>
<li><div class="n">2</div><div class="t">Email 1 gets the angle variables</div><div class="o">Claude, on Dallas's go</div><div class="r">Draft campaign, zero leads, so the template edit is safe. Done before any lead exists, never after.</div></li>
<li><div class="n">3</div><div class="t">Load {n} leads</div><div class="o">Claude, same go</div><div class="r">Dedupe on, variables filled per lead, cohort arm stamped, motionStatus loaded. Campaign stays draft.</div></li>
<li><div class="n">4</div><div class="t">Integrity sweep and three previews</div><div class="o">Claude</div><div class="r">Unrendered variables, wrong-company emails, test rows. Report back, fix, re-check.</div></li>
<li><div class="n">5</div><div class="t">Confirm lemwarm, switch the sender</div><div class="o">Dallas, lemlist UI</div><div class="r">When the warm mailbox clears (Sep 21 to 28): campaign sender to nathan.belfield@intradiemhq.com, then readiness check.</div></li>
<li><div class="n">6</div><div class="t">Ads list to marketing, launch date set</div><div class="o">Dallas</div><div class="r">Ads live T-3, Email 1 on T0. Launch is Nate's hand in lemlist after the readiness check.</div></li>
</ol>
<h3>Copy-paste for step 2 to 4</h3>
<pre class="prompt">{prompt}</pre>
<div class="gate"><h4>What this does not do</h4><p>No launch, no sender change, no send gate, no credits. The 289 people on the list without a verified email and the 78 without a LinkedIn URL are the enrichment backlog, on its own page.</p></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">Files</div><h2>Where everything lives</h2>
<ul class="threads"><li><b>Load plan</b> motions/dwo_executives/DWO_Shell_Load_Plan_Sep4.csv ({n} rows, every variable filled)</li><li><b>Held and skipped</b> motions/dwo_executives/DWO_Shell_Skipped_Sep4.csv</li><li><b>Ads list, test arm</b> motions/dwo_executives/GTMENG-DWO1-2026-09_ads_linkedin.csv</li><li><b>Loader</b> motions/dwo_executives/load_dwo_shell.py (dry run by default, --go loads, never launches)</li><li><b>Copy source</b> motions/dwo_executives/DWO_Exec_Sequence_Sep4.md</li><li><b>Stamp plan for Sales Ops</b> motions/pipeline_council/stamp_plans/GTM_Eng_-_DWO_Executives_-_Wave_1.csv</li></ul>
</div></section>
</div></body></html>"""
out=os.path.join(HERE,'DWO_Executives_Nate_Read_Sep4.html'); open(out,'w').write(page)
dt=os.path.expanduser('~/Desktop/Intradiem Deliverables/DWO_Executives_Nate_Read_Sep4.html'); open(dt,'w').write(page); print('wrote',out,'and',dt,len(page))
