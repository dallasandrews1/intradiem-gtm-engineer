#!/usr/bin/env python3
"""Enrichment backlog page: every pool contact ends with a verified email AND a LinkedIn URL. Reads the lemlist contact details
pulled Sep 4 (scratch) and writes the branded page plus the per-pool gap CSVs. Usage: build_backlog_page.py <scratch>"""
import json,os,sys,re,html,csv,collections
SP=sys.argv[1]; HERE=os.path.dirname(os.path.abspath(__file__)); E=html.escape
TPL=os.path.expanduser('~/Desktop/Intradiem Deliverables/Nate_Copy_Rewrite_Sep3.html'); css=re.search(r'<style>(.*?)</style>',open(TPL).read(),re.S).group(1); logo=open(f'{SP}/ilogo.svg').read()
D=json.load(open(f'{SP}/dwo_list_contact_details.json')); O=json.load(open(f'{SP}/other_list_contact_details.json'))
def em(d):
    f=d.get('fields') or {}; return d.get('email') or f.get('email') or ''
pools={'DWO Executives, Live (Clay)':list(D.values())}
for k,lab in (('bo_customer','BO Customer Lane (Nate)'),('bo_netnew','BO Net-New (Nate)'),('stars','Stars Buying Committee (Nate)'),('blitz','Blitz - Citizens + Hartford (Nate)'),('cost_mandate','Cost-Mandate Contacts'),('wfm_adjacency','WFM-Adjacency Prospects')):
    pools[lab]=[d for d in O.values() if d.get('_list')==k]
rows=[]; gap_rows=[]
for lab,items in pools.items():
    e=[d for d in items if em(d)]; u=[d for d in items if d.get('linkedinUrl')]; both=[d for d in items if em(d) and d.get('linkedinUrl')]
    eo=[d for d in items if em(d) and not d.get('linkedinUrl')]; uo=[d for d in items if d.get('linkedinUrl') and not em(d)]
    rows.append((lab,len(items),len(both),len(eo),len(uo)))
    for d in eo: gap_rows.append({'pool':lab,'name':d.get('fullName'),'title':(d.get('fields') or {}).get('jobTitle',''),'account':(d.get('fields') or {}).get('parentAccount',''),'email':em(d),'linkedinUrl':'','gap':'needs LinkedIn URL','path':'free LinkedIn bridge (0 cr), then Enrich Person by email (0.5 on hit)','status':(d.get('fields') or {}).get('motionStatus','')})
    for d in uo: gap_rows.append({'pool':lab,'name':d.get('fullName'),'title':(d.get('fields') or {}).get('jobTitle',''),'account':(d.get('fields') or {}).get('parentAccount',''),'email':'','linkedinUrl':d.get('linkedinUrl'),'gap':'needs verified email','path':'Work Email + ZeroBounce by LinkedIn URL (~1.6 on find) only if confirmed current','status':(d.get('fields') or {}).get('motionStatus','')})
w=csv.DictWriter(open(os.path.join(HERE,'Enrichment_Backlog_Sep4.csv'),'w',newline=''),fieldnames=['pool','name','title','account','email','linkedinUrl','gap','path','status']); w.writeheader(); w.writerows(gap_rows)
tot=sum(r[1] for r in rows); totboth=sum(r[2] for r in rows); toteo=sum(r[3] for r in rows); totuo=sum(r[4] for r in rows)
W=json.load(open(f'{SP}/dwo_live_waves.json')); em1=json.load(open(f'{SP}/dwo_wave1_email_results.json')); w1=[p for p in W['wave1'] if p['domain']!='unive.nl']
stuck=[p for p in w1 if str(p['clay_profile_id']) not in em1]
st_v=collections.Counter(p['vertical'] for p in stuck)
table=''.join(f"<tr><td class='who'>{E(l)}</td><td>{n}</td><td>{b}</td><td>{eo}</td><td>{uo}</td><td class='st'>{E('parked, no spend' if l.startswith('WFM') else ('complete' if eo+uo==0 else 'open'))}</td></tr>" for l,n,b,eo,uo in rows)
runs=[('A','Free LinkedIn bridge on the email-only rows',f'{toteo} people (DWO {rows[0][3]}, BO customer 2)','0 credits','Claude runs it now. Name plus company to the free Clay match; a URL lands on the lemlist contact. Misses go to run B.'),
 ('B','Enrich Person by email on the bridge misses',f'up to {toteo} people','0.5 per hit, ceiling '+str(round(toteo*0.5))+'; bills on hits only','Under the 200 line. Returns the LinkedIn URL and current employer, so it also proves the person is still there.'),
 ('C','Re-run the two stuck Work Email runs',f'{len(stuck)} wave 1 rows never returned (' + ', '.join(f'{v} {c}' for v,c in st_v.most_common()) + ')','about '+str(round(len(stuck)*1.6))+' credits at 1.6 a row','Over the 200 line: 15-row test first, then your go. The alternative is to cancel them and count these rows as needs_email; the cost of doing nothing is '+str(len(stuck))+' C-level seats that never enter a sequence.'),
 ('D','Work Email + ZeroBounce by LinkedIn URL on the rest of the DWO url-only rows',f'{rows[0][4]-len(stuck)} people already tried once by name (no_email, invalid, unknown)','about '+str(round((rows[0][4]-len(stuck))*0.8))+' credits, bills on find only','Under the 200 line. Runs only on rows the bridge confirmed current; the URL input measured about 0.8 a run on Aug 31.'),
 ('E','Stars and BO url-only rows',f'Stars 21, BO Net-New 15, BO customer 56, Cost-Mandate 1','Stars about 34 credits; BO rows are holds (leavers, foreign locations, JPMorgan-class domains), no spend','Stars 21 already failed the Sep 3 pass once; run only the ones a fresh bridge shows current. BO holds stay held.')]
runs_html=''.join(f"<li><div class='n'>{k}</div><div class='t'>{E(t)}</div><div class='o'>{E(c)}</div><div class='r'><b>{E(who)}</b> {E(note)}</div></li>" for k,t,who,c,note in runs)
prompt=E(f"""Enrichment backlog, run A only (0 credits): free LinkedIn bridge on the {toteo} email-only rows in motions/enrichment/Enrichment_Backlog_Sep4.csv (gap = needs LinkedIn URL). Match by name plus company through the free Clay contact match, write found URLs back to the lemlist contact by email, and give me the hit count and the miss list. No paid step.""")
prompt2=E(f"""Enrichment backlog, run C test: re-run 15 of the {len(stuck)} wave 1 rows that never returned (mixed verticals, no bank domains) through Work Email + ZeroBounce workflow wf_0tk4jo5z7RjGKo3rvR8, measure credits per row and valid rate, then stop and report. Ceiling 30 credits.""")
page=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Enrichment backlog across every pool (Sep 4 2026)</title><style>{css}
pre.prompt{{background:var(--forest);color:#E9F3EE;border-radius:var(--r);padding:20px 24px;font-family:var(--ff-mono);font-size:12.5px;line-height:1.55;white-space:pre-wrap;margin-top:14px}}</style></head><body><div class="sheet">
<svg width="0" height="0" style="position:absolute">{logo}</svg>
<div class="hero on"><div class="wrap"><svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">GTM Engineering · enrichment backlog · every pool · Sep 4 2026</div>
<h1 data-h="2">{tot:,} people in the pools. {totboth:,} carry both keys. <span class="spark">{toteo+totuo} to close.</span></h1>
<p class="sub" data-h="3">The rule: every contact a rep could sequence ends with a verified email <b>and</b> a LinkedIn URL. Free paths first, paid only on people confirmed current, nothing over 200 credits without a test and your go.</p>
<div class="hstats" data-h="4"><div><b>{toteo}</b><span>have an email, need a URL (free path)</span></div><div><b>{totuo}</b><span>have a URL, need an email (paid path)</span></div><div><b>{len(stuck)}</b><span>rows stuck in two Clay runs</span></div><div><b>0</b><span>credits spent today</span></div></div></div></div>
<section><div class="wrap"><div class="eyebrow">Pool by pool</div><h2>Where the gaps are</h2>
<p class="lede">Read from lemlist this morning, contact by contact. Campaign leads are complete by construction (every loaded lead has both keys except two BO Insurance leads with no URL); the gaps sit on the lists, in people not yet in a campaign.</p>
<div class="tablewrap"><table><thead><tr><th>Pool</th><th>People</th><th>Email and URL</th><th>Email only</th><th>URL only</th><th>State</th></tr></thead><tbody>{table}</tbody></table></div>
<div class="callout"><h4>WFM-Adjacency is parked</h4><p>206 people with URLs and no email. The motion has no campaign and no sender, so it gets no spend until it is re-opened. Listed so the count is honest, not as a run.</p></div></div></section>
<section><div class="wrap"><div class="eyebrow">The runs, cheapest first</div><h2>Five runs, one free, one over the line</h2>
<ol class="steps">{runs_html}</ol>
<div class="gate"><h4>Credit rule applied</h4><p>Balance this morning 64,997. Run A is free. Runs B, D and E each sit under the 200-credit warn line and still get logged with a stated estimate and the measured actual. Run C is over the line: a 15-row test, then your go, or cancel the two runs and carry the rows as needs_email.</p></div>
<h3>Copy-paste: run A now</h3><pre class="prompt">{prompt}</pre>
<h3>Copy-paste: run C, test only</h3><pre class="prompt">{prompt2}</pre></div></section>
<section><div class="wrap"><div class="eyebrow">Your call</div><h2>The 172 stuck rows: re-run or cancel</h2>
<div class="grid"><div class="card"><span class="tag go">re-run</span><h4>About {round(len(stuck)*1.6)} credits, {len(stuck)} C-level seats back in play</h4><p>Runs run_0tktg67B6g9g3PcGcmh (98 of 100 done) and run_0tktgpqEnKpc4jMdnjN (71 of 72 done) still show in progress and return nothing. A fresh run on the same rows at the measured 1.6 a row, after the 15-row test proves the rate. Expected valid rate about 66 percent, so roughly 115 more verified executives.</p></div>
<div class="card"><span class="tag hold">cancel</span><h4>0 credits, rows stay needs_email</h4><p>They keep their LinkedIn URLs and enter the LinkedIn-first variant of the DWO sequence later. Nothing is lost except email as the first touch.</p></div></div>
<p style="margin-top:16px">Backlog list with the path per person: motions/enrichment/Enrichment_Backlog_Sep4.csv ({len(gap_rows)} rows).</p></div></section>
</div></body></html>"""
for p in (os.path.join(HERE,'Enrichment_Backlog_Sep4.html'),os.path.expanduser('~/Desktop/Intradiem Deliverables/Enrichment_Backlog_Sep4.html')): open(p,'w').write(page)
print('rows',rows,'stuck',len(stuck),'gap rows',len(gap_rows))
