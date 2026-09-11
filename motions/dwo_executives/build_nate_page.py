import json,subprocess,re,html,os,collections,sys
SP=sys.argv[1]
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
seq=json.loads(subprocess.run(['curl','-s','-u',f':{KEY}','https://api.lemlist.com/api/campaigns/cam_SiD4KmWcRuhiF6uhL/sequences'],capture_output=True,text=True).stdout); json.dump(seq,open(f'{SP}/dwo_sequence_live.json','w'),indent=1)
steps=seq['seq_XiYpoRMDksmH7c93u']['steps']; leads=json.load(open(f'{SP}/dwo_campaign_leads.json'))
E=html.escape
def txt(h): return html.unescape(re.sub(r'<div>|<p>','',re.sub(r'</div>|</p>|<br>','\n',h or ''))).strip()
def paras(t): return ''.join(f'<p>{E(x)}</p>' for x in t.split('\n') if x.strip())
TPL=os.path.expanduser('~/Desktop/Intradiem Deliverables/Nate_Copy_Rewrite_Sep3.html'); css=re.search(r'<style>(.*?)</style>',open(TPL).read(),re.S).group(1); logo=open(f'{SP}/ilogo.svg').read()
n=len(leads); acc=len({l['companyDomain'] for l in leads}); vert=collections.Counter(l['peak'] for l in leads)
PEAKV={'open enrollment':'Healthcare','the Q4 claims and renewal peak':'Insurance','year-end close':'Financial Services','the winter season':'Utilities','holiday peak':'Retail','device season':'Telecom'}
def render(l,variant='A'):
    closing=l['angleAsk'] if variant=='A' else "Would it help if I sent a short note on how operations leaders size that number for their own teams? No meeting attached, I'll just send it."
    body=[f"Hi {l['firstName']},",l['opener'],l['angleIdea'],l['angleProof'],closing,"Nathan"]
    return f"<div class='mail'><div class='subj'>Subject: idle minutes at {E(l['companyName'])}</div>"+''.join(f'<p>{E(x)}</p>' for x in body)+"</div>"
def meta(l): return f"<div class='who'>{E(l['firstName'])} {E(l['lastName'])}, {E(l.get('jobTitle') or '')}, {E(l['companyName'])}. Variant {E(str(l.get('e1Variant')))}.</div>"
exA=next(l for l in leads if 'into the' in l['opener'] and l['angleIdea'].startswith("There's"))
exB=next((l for l in leads if l['angleIdea'].startswith('In service') and l['companyDomain']==exA['companyDomain']),next(l for l in leads if l['angleIdea'].startswith('In service')))
exC=next(l for l in leads if 'shared services' in l['workTeams']); exT=next(l for l in leads if l['angleIdea'].startswith('Most of'))
labels={0:'Email 1, day 1 (A/B: benchmark question vs offer note)',1:'LinkedIn connect, day 2',2:'Email 2 in thread, day 4',3:'LinkedIn message, day 7',4:'Email 3, breakup, day 11'}
steps_html=''.join(f"<div class='card'><span class='tag go'>{E(labels[s['sequenceStep']])}</span>"+(f"<p><b>Subject:</b> {E(s.get('subject') or '(in thread)')}</p>" if s.get('type')=='email' else '')+paras(txt(s.get('message')))+"</div>" for s in steps)
core=next(l for l in leads if l['angleIdea'].startswith("There's")); cust=next(l for l in leads if l['angleIdea'].startswith('In service')); tr=next(l for l in leads if l['angleIdea'].startswith('Most of'))
def ang(l,who): return f"<div class='card'><span class='tag now'>{E(who)}</span><p>{E(l['angleIdea'])}</p><p>{E(l['angleProof'])}</p><p>{E(l['angleAsk'])}</p></div>"
angle_html=ang(core,f"COO, operations and CAO seats ({sum(1 for l in leads if l['angleIdea'].startswith(chr(84)+'here'))})")+ang(cust,f"Customer, experience and service seats, and the second person at an account ({sum(1 for l in leads if l['angleIdea'].startswith('In service'))})")+ang(tr,f"Transformation seats, and the third person ({sum(1 for l in leads if l['angleIdea'].startswith('Most of'))})")
P=json.load(open(f'{SP}/dwo_shell_plan.json'))['plan']; live={(l.get('email') or '').lower() for l in leads}; flag=[r for r in P if r.get('flag') and r['email'].lower() in live]
flag_rows=''.join(f"<tr><td class='who'>{E(r['name'])}</td><td>{E(r['title'])}</td><td>{E(r['account'])}</td></tr>" for r in flag)
vert_rows=''.join(f"<tr><td class='who'>{E(PEAKV.get(k,k))}</td><td>{c}</td><td>{len({l['companyDomain'] for l in leads if l['peak']==k})}</td><td>{E(k)}</td></tr>" for k,c in vert.most_common())
newrole=sum(1 for l in leads if 'into the' in l['opener'])
page=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>DWO executives, wave 1: Nate's read</title><style>{css}
.mail{{background:var(--zebra);border:1px solid var(--line);border-radius:var(--r);padding:18px 22px;margin-top:10px}} .mail .subj{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600);font-weight:600;margin-bottom:8px}} .mail p{{margin-top:8px;font-size:15px;color:var(--ink)}} .who{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.04em;color:var(--ink-3);margin-top:18px}} .card p{{margin-top:8px}}</style></head><body><div class="sheet">
<svg width="0" height="0" style="position:absolute">{logo}</svg>
<div class="hero on"><div class="wrap"><svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">DWO executives · wave 1 · your read · Sep 4 2026</div>
<h1 data-h="2">{n} operating executives at {acc} accounts, <span class="spark">loaded and paused for your read.</span></h1>
<p class="sub" data-h="3">Sourced live this week, current in role, verified email, no current customer or partner. The five-touch sequence is in lemlist as a draft under your name. <b>Nothing sends until you say so.</b></p>
<div class="hstats" data-h="4"><div><b>{n}</b><span>leads, paused</span></div><div><b>{acc}</b><span>accounts, at most 10 each</span></div><div><b>{newrole}</b><span>new in role, six months or less</span></div><div><b>0</b><span>sent</span></div></div></div></div>
<section><div class="wrap"><div class="tldr"><div class="k">The read in four lines</div><ul>
<li><b>Who:</b> COOs, CAOs, customer and service chiefs, transformation chiefs at US prospects in the six verticals. C-level only in this wave.</li>
<li><b>One idea, three angles:</b> the operation pays for capacity twice, idle minutes inside the shift and overtime after it. No two people at one account get the same angle where three angles allow it.</li>
<li><b>Numbers:</b> only the Humana on-the-record set. Two hours per agent per month, 7X five years in, 12,000 VTO hours, handle time down 45 seconds, return inside the first year.</li>
<li><b>Your calls:</b> the {len(flag)} hospital and medical-group COOs below, the opt-out line, and anything you would not say on the phone.</li>
</ul></div></div></section>
<section><div class="wrap"><div class="eyebrow">The sequence, as it sits in lemlist</div><h2>Five touches over eleven days, no phone step</h2>
<p class="lede">C-level seats get email and LinkedIn only. Email 1 splits A/B: a benchmark question against an offer note. The three middle paragraphs of Email 1 change by person (the three angles below); everything else is verbatim from the draft.</p>
<div class="grid">{steps_html}</div>
<h3>The three angles that fill Email 1</h3><div class="grid c3">{angle_html}</div></div></section>
<section><div class="wrap"><div class="eyebrow">Rendered</div><h2>What four real people would receive</h2>
{meta(exA)}{render(exA)}{meta(exB)}{render(exB,'B')}{meta(exC)}{render(exC)}{meta(exT)}{render(exT)}
<p style="margin-top:16px">People six months or less into the seat get the new-in-role opener. Everyone else gets the dated vertical peak line.</p>
<div class="tablewrap"><table><thead><tr><th>Vertical</th><th>People</th><th>Accounts</th><th>Peak named in Email 3</th></tr></thead><tbody>{vert_rows}</tbody></table></div></div></section>
<section><div class="wrap"><div class="eyebrow">Your calls</div><h2>Three decisions, all yours</h2>
<div class="grid"><div class="card"><span class="tag now">1 · hospital and medical-group COOs</span><h4>{len(flag)} unit-level seats in health systems</h4><p>Health-system COOs run patient access, billing and revenue cycle. Unit-level ones (a hospital, a medical group, a market) are weaker seats for it. They are loaded and listed below; say drop and they come out.</p></div>
<div class="card"><span class="tag now">2 · opt-out line</span><h4>Not in Email 1 today</h4><p>US market, C-level, no obligation. If you want it back in your words, it goes on the last line of Email 1 and Email 3.</p></div>
<div class="card"><span class="tag now">3 · anything that does not sound like you</span><h4>Say the line and it changes before anything sends</h4><p>Every email, note and message on this page is editable per lead or per step. The numbers stay; the words are yours.</p></div>
<div class="card"><span class="tag hold">mailbox</span><h4>Sends go from nathan.belfield@intradiemhq.com</h4><p>The warm mailbox, not the main one. The campaign moves to it the day lemwarm clears it, then the readiness check, then your start.</p></div></div>
<h3>The {len(flag)} flagged seats</h3><div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Account</th></tr></thead><tbody>{flag_rows}</tbody></table></div></div></section>
<section><div class="wrap"><div class="eyebrow">What happens next</div><h2>Your read, then the mailbox, then your start</h2>
<ol class="steps"><li><div class="n">1</div><div class="t">Your read</div><div class="o">Nate</div><div class="r">This page. Three calls above.</div></li><li><div class="n">2</div><div class="t">Warm mailbox clears</div><div class="o">Dallas</div><div class="r">Campaign sender switched to intradiemhq.com, readiness check run.</div></li><li><div class="n">3</div><div class="t">Start</div><div class="o">Nate</div><div class="r">Your hand in lemlist. Replies land in your Slack channel the same hour with a drafted answer.</div></li></ol></div></section>
</div></body></html>"""
d=os.path.expanduser('~/Desktop/Intradiem Deliverables/deploy-dwo-exec-read'); os.makedirs(d,exist_ok=True); open(d+'/index.html','w').write(page); open(d+'/_headers','w').write('/*\n  X-Robots-Tag: noindex\n')
open('motions/dwo_executives/DWO_Exec_Nate_Page_Sep4.html','w').write(page); print('nate page built',n,acc,len(flag),'newrole',newrole)
