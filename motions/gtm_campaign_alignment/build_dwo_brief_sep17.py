#!/usr/bin/env python3
"""DWO executives one-page brief in John's ten rows for the Sep 17 alignment meeting, plus the Stars adjustments slot.
Usage: build_dwo_brief_sep17.py <scratch>"""
import json,os,sys,re,html,collections
SP=sys.argv[1]; HERE=os.path.dirname(os.path.abspath(__file__)); E=html.escape
TPL=os.path.expanduser('~/Desktop/Intradiem Deliverables/Nate_Copy_Rewrite_Sep3.html'); css=re.search(r'<style>(.*?)</style>',open(TPL).read(),re.S).group(1); logo=open(f'{SP}/ilogo.svg').read()
P=json.load(open(f'{SP}/dwo_shell_plan.json')); plan=P['plan']; n=len(plan); accts=len({r['account'] for r in plan})
W=json.load(open(f'{SP}/dwo_live_waves.json')); w2=W['wave2']
def tier(t): return 'EVP' if re.search(r'\bevp\b|executive vice',t or '',re.I) else 'SVP' if re.search(r'\bsvp\b|senior vice',t or '',re.I) else 'Head'
t2=collections.Counter(tier(p['title']) for p in w2); arms=collections.Counter(r['cohortArm'] for r in plan)
rows=[('Target market','US prospects in the six verticals (healthcare, financial services, insurance, retail, telecom, utilities) with a contact center and a back office. 564 accounts hold a current operating executive; 285 are in wave 1. No current customer or partner, checked in Clay Audiences before anything reached lemlist.'),
 ('Roles and titles',f'The VITO first: COO, Chief Administrative Officer, Chief Customer or Experience or Service Officer, Chief Transformation Officer. Wave 1 is C-level only ({n} people). Wave 2 is EVP, SVP and Head of Operations or Shared Services ({len(w2):,} people, {t2["EVP"]+t2["SVP"]} at EVP or SVP). The AE confirms the VITO per account before the second wave at that account.'),
 ('Data collected','Name, title, start date in role, account, vertical, verified work email (ZeroBounce valid), LinkedIn URL, Salesforce account ID where one exists (4 percent do). Per person: which of three angles they get, so no two people at one account read the same note.'),
 ('Key signals',f'New in role, six months or less ({sum(1 for r in plan if r["opener_rule"]=="A")} of {n} in wave 1) leads every note. Otherwise the dated vertical peak (open enrollment, Q4 claims, year-end close, winter season, holiday peak, device season). A war-room signal at the account replaces the peak line the day it exists.'),
 ('Tooling','Sourced live in Clay this week (search is free; email finding 1.6 credits a row, 1,666 credits for wave 1). lemlist campaign DWO Executives - Live Pool, sender Nathan Belfield from the warm intradiemhq.com mailbox. Suppression stays in Clay; lemlist holds only people a rep could sequence.'),
 ('Marketing support',f'LinkedIn Matched Audience on half the accounts ({arms["test"]} people, test arm), live three business days before Email 1, off at day 25, one creative on the idle-minutes idea and a landing page that says the same thing. The other half ({arms["holdout"]} people) gets the sequence only, so the row shows what the ads added.'),
 ('Execution','Five touches over eleven days: Email 1 (A/B: benchmark question against an offer note), LinkedIn connect day 2, Email 2 in thread day 4, LinkedIn message day 7, breakup day 11. No phone step at C-level. Nate sees replies in lemlist and Slack the same hour; a reply gets the objection handler draft in his voice. Waves of 30 to 50 accounts, each back here with a read.'),
 ('Gates','Customers out (Clay Audiences union, checked before load). Only Humana on-the-record figures in the copy, one-to-many cleared. Verified email is the load gate. Nate reads every wave before it starts; Dallas presses nothing that sends.'),
 ('Tracking','Lead Source GTM Engineering, Lead Origin GTM Engineering, Primary Campaign Source GTM Eng - DWO Executives - Wave 1. Cohort id and arm on every lead. Cost per meeting and meeting-to-opp reported on the council row against Cold ($3,402 and 19 percent), test and holdout side by side.'),
 ('Owner and next read',f'Dallas builds, Nate sends. Wave 1 ({n}) loads the day Nate clears the copy; Email 1 goes on the warm mailbox the week of Sep 21. First read at the Oct 1 meeting: replies, meetings, and the ads delta.')]
rows_html=''.join(f"<li><div class='n'>{i+1}</div><div class='t'>{E(k)}</div><div class='o'>{'agenda' if i<7 else 'countable'}</div><div class='r'>{E(v)}</div></li>" for i,(k,v) in enumerate(rows))
page=f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>DWO executives brief for Sep 17 (John's ten rows)</title><style>{css}
.steps li{{grid-template-columns:44px 1fr 110px 3fr}}</style></head><body><div class="sheet">
<svg width="0" height="0" style="position:absolute">{logo}</svg>
<div class="hero on"><div class="wrap"><svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">GTM Engineering · campaign alignment · Thu Sep 17 2026, 11:00 CT</div>
<h1 data-h="2">DWO to the operating executive, <span class="spark">one page in the agenda's rows.</span></h1>
<p class="sub" data-h="3">The campaign John described in July: the VITO first, the DWO story in their words, three or four touches, one row on the council dashboard. Built this week from a live pull, not the Salesforce list.</p>
<div class="hstats" data-h="4"><div><b>{n}</b><span>C-level executives, wave 1</span></div><div><b>{accts}</b><span>accounts</span></div><div><b>{len(w2):,}</b><span>EVP, SVP and Head titles, wave 2</span></div><div><b>96%</b><span>not in Salesforce today</span></div></div></div></div>
<section><div class="wrap"><div class="eyebrow">Brief 2 · DWO executives</div><h2>Ten rows. Seven are the agenda, three make it countable.</h2>
<ol class="steps">{rows_html}</ol></div></section>
<section><div class="wrap"><div class="eyebrow">Wave 2, sized</div><h2>The EVP and SVP layer is the next 785; Heads are the long tail</h2>
<div class="statband"><div><div class="n">{t2['EVP']}</div><div class="l">EVP</div></div><div><div class="n">{t2['SVP']}</div><div class="l">SVP</div></div><div><div class="n">{t2['Head']:,}</div><div class="l">Head of</div></div><div><div class="n">~1,260</div><div class="l">credits for EVP and SVP at 1.6 a row (all 2,669 would be ~4,270)</div></div></div>
<p>Sizing waits for the first DWO replies: the C-level read tells us which vertical and which angle earns the second wave. The AE confirms the VITO at any account before wave 2 goes there.</p></div></section>
<section><div class="wrap"><div class="eyebrow">Brief 1 · Star Ratings, adjustments</div><h2>Two changes after the VITO note, both built</h2>
<div class="grid"><div class="card"><span class="tag go">1 · VITO thread</span><h4>A CFO or COO at every parent in wave 1</h4><p>The Stars sequences reach the VP Stars and Director of Quality. The quality bonus sits with the CFO or COO; they get one note with the number already on the table, and the champion thread continues underneath. Sourced the same way as DWO: live Clay pull, verified email, one-to-many claims only.</p></div>
<div class="card"><span class="tag go">2 · Own row</span><h4>A Salesforce campaign per Stars lane</h4><p>GTM Eng - Star Ratings - Resurrection, Quality and Finance. Every lead carries Lead Source GTM Engineering, so the council sees Stars as its own line instead of rolling into Cold or Digital. Stamp plans are written for all three.</p></div></div>
<div class="callout"><h4>October</h4><p>CMS publishes the 2027 ratings in early October. Plans that drop below 4.0 that day are wave 2; the refresh watcher stages the list, Nate decides the send.</p></div></div></section>
<section><div class="wrap"><div class="eyebrow">Decisions for the room</div><h2>Three lines, three owners</h2>
<ul class="threads"><li><b>Lead Source and Lead Origin value</b> GTM Engineering, one value, motion carried by the campaign name. Genna and Naveen; Sierra files the ticket.</li><li><b>VITO confirmation</b> per account by the AE before wave 2 at that account. Kevin and the AEs.</li><li><b>Ads on the DWO test arm</b> LinkedIn Matched Audience from our list, three days ahead of Email 1. Melissa and Sierra.</li></ul></div></section>
</div></body></html>"""
for p in (os.path.join(HERE,'DWO_Exec_Brief_Sep17.html'),os.path.expanduser('~/Desktop/Intradiem Deliverables/DWO_Exec_Brief_Sep17.html')): open(p,'w').write(page)
print('ok',n,accts,dict(t2))
