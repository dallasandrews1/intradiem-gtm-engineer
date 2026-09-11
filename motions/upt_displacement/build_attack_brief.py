#!/usr/bin/env python3
"""UPT displacement brief for Naveen's Thursday Sep 10 2026 meeting with John: the Verint estate and NICE estate lists,
the people already on file, the Verint-first call, the Verint attack in John's ten rows, the NICE delta, Email 1 rendered.
Reads lists/summary.json, lists/*_estate.csv and UPT_Attack_Sequences_Sep9.md so the page always carries current numbers and copy.
Usage: build_attack_brief.py [scratch dir holding ilogo.svg]"""
import json, os, sys, re, html, csv, pathlib
HERE = pathlib.Path(__file__).resolve().parent; E = html.escape
SP = sys.argv[1] if len(sys.argv) > 1 else str(HERE)
TPL = os.path.expanduser('~/Desktop/Intradiem Deliverables/Nate_Copy_Rewrite_Sep3.html')
css = re.search(r'<style>(.*?)</style>', open(TPL).read(), re.S).group(1)
logo = open(f'{SP}/ilogo.svg').read()
S = json.load(open(HERE / 'lists/summary.json')); V = S['verint']; N = S['nice']; C = S['segment_counts']
_est = [r for fn in ('verint_estate.csv','nice_estate.csv') for r in csv.DictReader(open(HERE / 'lists' / fn))]
_vd = {r['domain']: int(r['vito_in_dwo_pool']) for r in _est if int(r['vito_in_dwo_pool'])}
vito_accts = len(_vd); vito_people = sum(_vd.values())
seq = open(HERE / 'UPT_Attack_Sequences_Sep9.md').read()
def email1(section):
    m = re.search(r'## ' + re.escape(section) + r'.*?\*\*Email 1\*\* · subject: `([^`]+)`\n\n(.*?)\n\nNathan', seq, re.S)
    return m.group(1), m.group(2)
def render_mail(subject, body, label):
    body = body.replace('{{signal}}', '[dated signal per lead: a posting for a Desktop and Process Analytics analyst, a profile at the account listing the product, or the Oct 15 open-enrollment line]')
    paras = ''.join(f'<p>{E(p)}</p>' for p in body.split('\n\n'))
    return f"<div class='mail'><div class='mlabel'>{E(label)}</div><div class='msubj'>subject: {E(subject)}</div>{paras}<p>Nathan</p></div>"
def top(fn, k=10):
    rows = [r for r in csv.DictReader(open(HERE / 'lists' / fn)) if r['icp_fit'] == 'yes'][:k]
    return ', '.join(E(r['company']) for r in rows)
rows = [('Target market', f"US prospects running Verint: {V['icp_accounts']} in the six verticals plus BPO first, {V['outside_icp']} held. {V['employees_20k_plus']} above 20,000 employees. No customers or partners."),
 ('Roles and titles', f"Head of WFM or Real-Time, Director or VP Contact Center Operations, Director Operational Excellence, VP or Director Claims Operations or Shared Services. Three or four seats per account. The COO or CAO at {V['accounts_with_vito']} of these accounts is already in the DWO Executives campaign."),
 ('Data collected', "Verified work email, LinkedIn URL, phone, Salesforce account ID, the stack read with its date, the desktop-analytics evidence tier and source, rep confirmation, and the angle each person carries."),
 ('Key signals', "The desktop-analytics signal first, then a war-room trigger, then the vertical peak (open enrollment Oct 15, Q4 claims, year-end close, winter season). A known Verint renewal date goes in the breakup."),
 ('Tooling', "Lists live in Audiences as six saved segments. Sequence sends from lemlist as Verint Attack, sender Nate, warm mailbox. Email finding 1.6 credits a row; wave 1 about 240 credits."),
 ('Marketing support', "One page on intradiem.com on what User Productivity Tracking does next to a desktop-analytics report, carrying the Humana line. Ads on the test arm, same design as DWO."),
 ('Execution', "Sixteen touches over eighteen business days: five emails in two threads, three calls with voicemails, six LinkedIn touches, one breakup. All seats at an account start the same day. Waves of 30 to 50 accounts, each back here with a read."),
 ('Gates', "Customers out. Humana on the record and two blinded back-office stories only. Module confirmed per account by the AE or Nate before it loads. Verified email is the load gate. Nate reads every wave."),
 ('Tracking', "Lead Source GTM Engineering, campaign GTM Eng - Verint Attack - Wave 1, cohort id per lead. Cost per meeting and meeting-to-opp against Cold ($3,402, 19 percent). Incumbent named on every opportunity."),
 ('Owner and next read', "Dallas builds, Nate sends, the AE confirms the module. Wave 1 loads the week of Sep 21. First read Oct 1.")]
rows_html = ''.join(f"<li><div class='n'>{i+1}</div><div class='t'>{E(k)}</div><div class='o'>{'agenda' if i<7 else 'countable'}</div><div class='r'>{E(v)}</div></li>" for i,(k,v) in enumerate(rows))
_all = {r['domain']: r for fn in ('verint_estate.csv','nice_estate.csv') for r in csv.DictReader(open(HERE / 'lists' / fn))}
tierA_rows = [r for r in _all.values() if r['evidence_tier'].startswith('A')]; tierB_rows = [r for r in _all.values() if r['evidence_tier'] == 'B']
tierA = len(tierA_rows); tierB = len(tierB_rows); tierAB = tierA + tierB; tierD = sum(1 for r in _all.values() if r['evidence_tier'] == 'D')
tierA_names = ', '.join(E(r['company'].split(' (')[0]) for r in sorted(tierA_rows, key=lambda r: r['company']))
nice_used = N['nice_tags'].get('bundled and used', 0); nice_conf = N['nice_tags'].get('vendor confirmed, desktop module not named', 0); nice_none = N['nice_tags'].get('bundled, no evidence of use', 0)
s1, b1 = email1('Verint attack, FO estate owner')
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>UPT displacement: Verint and NICE estates for Thursday with John</title><style>{css}
.steps li{{grid-template-columns:44px 1fr 110px 3fr}}
table.est td:first-child{{font-weight:700}} table.est td,table.est th{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;font-size:14.5px}} table.est th{{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--green-600);font-weight:600}}
.mail{{background:var(--bg);border:1px solid var(--line);border-radius:var(--r);padding:18px 20px;font-size:14.5px;line-height:1.55;box-shadow:var(--shadow)}} .mail p{{margin:0 0 10px}} .mail p:last-child{{margin:0}} .mlabel{{font-family:var(--ff-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--green-600);font-weight:600;margin-bottom:6px}} .msubj{{font-family:var(--ff-mono);font-size:12px;color:var(--ink-2);margin-bottom:12px;padding-bottom:10px;border-bottom:1px solid var(--line)}}
.grid.mails.one{{grid-template-columns:minmax(0,640px)}} .names{{font-size:14px;color:var(--ink-2);margin-top:8px}} .names b{{color:var(--ink)}}
@media(max-width:900px){{.steps li{{grid-template-columns:44px 1fr}} .steps .o,.hstats{{display:none}}}}</style></head><body><div class="sheet">
<svg width="0" height="0" style="position:absolute">{logo}</svg>
<div class="hero on"><div class="wrap"><svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">GTM Engineering · UPT displacement · Thu Sep 10 2026</div>
<h1 data-h="2">Verint and NICE desktop analytics: <span class="spark">the accounts, the people, the sequence.</span></h1>
<p class="sub" data-h="3">Two prospect lists from the stack read, the executives already sequenced, and the Verint attack written to the Sep 4 standard. The desktop-analytics module is the wedge; the WFM and the ACD stay the layer we act on.</p>
<div class="hstats" data-h="4"><div><b>{V['accounts']}</b><span>Verint estate accounts</span></div><div><b>{N['accounts']}</b><span>NICE estate accounts</span></div><div><b>{vito_people}</b><span>executives already in the DWO campaign, {vito_accts} accounts</span></div><div><b>{tierA}</b><span>accounts with the desktop module confirmed</span></div></div></div></div>

<section><div class="wrap"><div class="eyebrow">The lists</div><h2>Two tiers: the vendor estate is in hand, the module is confirmed account by account</h2>
<div class="gate"><h4>Vendor estate, in hand</h4><p>Verint: {V['accounts']} prospects, 50 on Verint Workforce Management. NICE: {N['accounts']}, 97 on CXone, 67 on inContact, 15 on NICE WFM. {S['both_estates']} in both. {S['customers_excluded']} held out as customers, subsidiaries or merged entities.</p></div>
<div class="callout"><h4>Desktop-analytics module, swept Sep 9</h4><p>No stack read sees the module. Confirmed at {tierA} accounts ({tierA_names}) from vendor case studies, current-role profiles that name the product, and the rep's read. Vendor confirmed at {tierB} more. Stack read alone at {tierD}. The rep-confirmed field qualifies every other account before it loads.</p></div></div></section>

<section><div class="wrap"><div class="eyebrow">On file</div><h2>Both estates already hold the people the sequence needs</h2>
<div class="tablewrap"><table class="est"><thead><tr><th>Estate</th><th>Accounts (six verticals + BPO / outside)</th><th>Front office, Director+, email on file</th><th>Back office, Director+, email on file</th><th>Executives in the DWO campaign</th></tr></thead><tbody>
<tr><td>Verint</td><td>{V['accounts']} ({V['icp_accounts']} / {V['outside_icp']})</td><td>{C['Verint_people_fo']:,}</td><td>{C['Verint_people_bo']}</td><td>{V['vito_people']} at {V['accounts_with_vito']}</td></tr>
<tr><td>NICE</td><td>{N['accounts']} ({N['icp_accounts']} / {N['outside_icp']})</td><td>{C['NICE_people_fo']:,}</td><td>{C['NICE_people_bo']}</td><td>{N['vito_people']} at {N['accounts_with_vito']}</td></tr></tbody></table></div>
<p class="names"><b>Verint, largest in the six verticals:</b> {top('verint_estate.csv', 10)}.</p>
<p class="names"><b>NICE, largest in the six verticals:</b> {top('nice_estate.csv', 10)}.</p>
<p>A wave is 30 to 50 accounts, three or four seats each: 120 to 200 people.</p></div></section>

<section><div class="wrap"><div class="eyebrow">The order</div><h2>Verint first, NICE second</h2>
<div class="grid"><div class="card"><span class="tag go">Wave 1 · Verint</span><h4>Findable buyer, underserved incumbent</h4><p>50 of {V['accounts']} run Verint WFM, so the Head of WFM who reads the desktop report owns the renewal. Nate's field read, Aug 18 and Sep 4: Verint back-office users are underserved, Maximus among them.</p></div>
<div class="card"><span class="tag hold">Wave 2 · NICE</span><h4>Larger, bundled, measured against Verint first</h4><p>NICE desktop analytics usually arrives bundled with the front office, so the displacement is against "free." It scales to {N['icp_accounts']} accounts only against a Verint cost-per-meeting read.</p></div></div>
<div class="gate"><h4>The rule</h4><p>The module, never the layer. Intradiem integrates with Verint WFM and NICE. The copy says "on top of Verint" and "alongside CXone."</p></div></div></section>

<section><div class="wrap"><div class="eyebrow">Brief 3 · Verint attack</div><h2>The Verint attack in the ten rows</h2>
<ol class="steps">{rows_html}</ol></div></section>

<section><div class="wrap"><div class="eyebrow">Brief 4 · NICE attack</div><h2>The NICE attack changes three rows</h2>
<div class="grid c3"><div class="card"><span class="tag hold">Target market</span><h4>{N['accounts']} accounts, {N['icp_accounts']} in the six verticals plus BPO</h4><p>Second wave, after the Verint read.</p></div>
<div class="card"><span class="tag hold">Key signal</span><h4>Module in use at {nice_used}, vendor confirmed at {nice_conf}, no evidence at {nice_none}</h4><p>A bundled module never turned on is a greenfield UPT account, not a displacement. The tag rides on every row.</p></div>
<div class="card"><span class="tag hold">Execution</span><h4>Same arc, one angle swapped</h4><p>"The number CXone already has." Never "replace NICE."</p></div></div></div></section>

<section><div class="wrap"><div class="eyebrow">The sequence</div><h2>One arc, four angles, Email 1</h2>
<p>Sixteen touches, eighteen business days. Four angles so no two people at an account read the same idea. Full arc, calls and LinkedIn in the sequence file.</p>
<div class="grid mails one">{render_mail(s1, b1, "Verint attack · Head of WFM · Email 1 shell; product sentence swaps for Naveen's wording")}</div>
<p class="names">Every Intradiem number is a verified row: Humana on the record, plus two blinded back-office stories.</p></div></section>

<section><div class="wrap"><div class="eyebrow">Decisions</div><h2>Three decisions, three owners</h2>
<ul class="threads"><li><b>Verint first, NICE second.</b> Naveen and John.</li><li><b>Module confirmed per account before it loads.</b> Kevin and Nate.</li><li><b>One UPT page for the sequence link; ads on the test arm.</b> Melissa and Sierra.</li></ul></div></section>

<section><div class="wrap"><div class="eyebrow">Next</div><h2>What happens next</h2>
<div class="grid c3"><div class="card"><span class="tag now">This week</span><p>Rep confirmation on wave-1 accounts. Phones on wave-1 seats. Naveen's messaging document swaps the product sentence.</p></div><div class="card"><span class="tag go">Week of Sep 21</span><p>Wave 1 loads: Verint estate, six verticals plus BPO, 30 to 50 accounts.</p></div><div class="card"><span class="tag hold">Oct 1</span><p>First read at the alignment meeting.</p></div></div></div></section>
<div class="foot">GTM Engineering · Sep 9 2026</div>
</div></body></html>"""
assert '—' not in page, 'em dash on the page'
for p in (HERE / 'UPT_Attack_Brief_Sep10.html', pathlib.Path(os.path.expanduser('~/Desktop/Intradiem Deliverables/UPT_Attack_Brief_Sep10.html'))):
    p.write_text(page)
print('ok', len(page), 'bytes;', V['accounts'], N['accounts'], vito_people, vito_accts, 'tierA', tierA)
