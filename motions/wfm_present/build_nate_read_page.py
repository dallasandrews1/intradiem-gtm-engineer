#!/usr/bin/env python3
"""Build the WFM Present wave-1 Nate-read page (Intradiem page system) from the load file and the live lemlist copy.
Usage: build_nate_read_page.py <scratch>  (scratch holds ilogo.svg) -> writes WFM_Present_Nate_Read_Sep5.html here and on the Desktop."""
import csv, os, sys, re, html, collections
SP = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.expanduser('~/Desktop/Intradiem Deliverables/Nate_Copy_Rewrite_Sep3.html')
css = re.search(r'<style>(.*?)</style>', open(TPL).read(), re.S).group(1)
logo = open(f'{SP}/ilogo.svg').read()
rows = list(csv.DictReader(open(os.path.join(HERE, 'WFM_Present_Full_Load_Sep5.csv'))))
held = list(csv.DictReader(open(os.path.join(HERE, 'WFM_Present_Held_Sep5.csv'))))
held_reasons = collections.Counter(h['reason'].split(':')[0] for h in held)
E = html.escape
def paras(t): return ''.join(f'<p>{E(x)}</p>' for x in t.split('\n') if x.strip())
n = len(rows); accts = sorted({r['companyName'] for r in rows})
wfm = collections.Counter(r['wfmPlatform'] for r in rows); acd = collections.Counter(r['acdPlatform'] for r in rows)
withurl = sum(1 for r in rows if r['linkedinUrl']); withcol = sum(1 for r in rows if r['colleagueLine']); handn = sum(1 for r in rows if r.get('source') == 'hand'); vpn = sum(1 for r in rows if r.get('tier') == '0')
def e1(r):
    body = [f"Hi {r['firstName']},", r['opener'], r['angleIdea'], r['angleProof'], r['angleAsk'], "Nathan"]
    words = sum(len(x.split()) for x in body[1:5]) + 3
    return (f"<div class='mail'><div class='subj'>Subject: the intraday layer on top of {E(r['wfmPlatform'])} &middot; {words} words</div>"
            + ''.join(f'<p>{E(x)}</p>' for x in body) + "</div>")
def who(r): return (f"<div class='who'>{E(r['firstName'])} {E(r['lastName'])}, {E(r['jobTitle'])}, {E(r['companyName'])}. "
                    f"WFM {E(r['wfmPlatform'])}, ACD {E(r['acdPlatform'])}, read {E(r['acdLastSeen'])}. "
                    f"{'LinkedIn on file' if r['linkedinUrl'] else 'No LinkedIn on file, email and phone branch'}.</div>")
# three examples, one per WFM platform, freshest read first
def pick(p):
    c = sorted([r for r in rows if r['wfmPlatform'] == p], key=lambda r: r['acdLastSeen'], reverse=True); return c[0]
examples = [pick('Verint'), pick('Calabrio'), pick('Aspect')]
# accounts table
acc_rows = ''
for a in accts:
    rs = [r for r in rows if r['companyName'] == a]
    acc_rows += (f"<tr><td class='who'>{E(a)}</td><td>{E(rs[0]['wfmPlatform'])}</td><td>{E(rs[0]['acdPlatform'])}</td>"
                 f"<td>{E(max(r['acdLastSeen'] for r in rs))}</td><td>{len(rs)}</td><td>{E(rs[0]['peak'])}</td></tr>")
plat_rows = ''.join(f"<tr><td class='who'>{E(k)}</td><td>{v}</td><td>{len({r['companyName'] for r in rows if r['wfmPlatform']==k})}</td></tr>" for k, v in wfm.most_common())
acd_rows = ''.join(f"<tr><td class='who'>{E(k)}</td><td>{v}</td><td>{len({r['companyName'] for r in rows if r['acdPlatform']==k})}</td></tr>" for k, v in acd.most_common())
# sequence copy after Email 1 (verbatim from the live draft, variables left as written)
steps = [
 ('LinkedIn connect note, day 2 (leads with a profile on file)', None, "Hi {{firstName}}, shot you a note by email on the intraday layer on top of {{wfmPlatform}} at {{companyName}}, thought this might be quicker. Nathan, Intradiem"),
 ('Call 1, day 3, voicemail if no answer', None, "{{firstName}}, Nathan Belfield at Intradiem. I sent you a note on the intraday layer on top of {{wfmPlatform}} at {{companyName}}; the short version is in your email. The plan is right at eight and wrong by ten, and your team absorbs the drift by hand. Humana runs the fix on top of the WFM it already had and gets about two hours back per agent per month. I'm at 937-238-3179. Thanks {{firstName}}."),
 ('Email 2 in thread, day 4', '(in thread)', "Hi {{firstName}},\nOne number I left out. Humana's agents took 12,000 hours of voluntary time off that Intradiem found inside the schedule, which Humana counts directly as overtime avoided.\nThat's the shape of it on top of {{wfmPlatform}}: the capacity is already in the plan, it just arrives at the wrong minute.\nIs intraday exception work a line your team is being asked to take down this year, or is it holding steady?\nNathan"),
 ('LinkedIn message 1, on accept (you approve before it goes)', None, "Thanks for connecting, {{firstName}}. Short version of my email: the plan {{wfmPlatform}} builds is right at eight and wrong by ten, and your team absorbs the drift by hand. Intradiem sits on top of {{wfmPlatform}} and acts on your rules automatically as the day moves. Humana has about two hours back per agent per month on the record. Worth a conversation on what that looks like across your teams?"),
 ('Call 2, day 6, then the just-tried-you email the same hour', '(in thread)', "Hi {{firstName}},\nJust tried your line and left a short message. The question in my notes stands: how much of your team's day is intraday correction on top of {{wfmPlatform}} rather than planning? Humana's answer was about two hours per agent per month, found and used automatically.\nWorth twenty minutes to find out what {{companyName}}'s is?\nNathan"),
 ('Email 3, the peak, day 8', '{{peak}} at {{companyName}}', "Hi {{firstName}},\nAt {{companyName}}, {{peak}} is the stretch where the {{wfmPlatform}} plan and the day disagree most, and where the overtime line gets set for the year.\nIntradiem sits on top of {{wfmPlatform}} and moves work, training and breaks into idle windows as they open, so the {{workTeams}} absorb the peak without the after-hours bill. Humana has it on the record: 12,000 voluntary time-off hours found inside the schedule, counted as overtime avoided.\nWorth a look at what that does to {{peak}} at {{companyName}} before it starts?\nNathan"),
 ('LinkedIn message 2, day 10 (connected leads)', None, "{{firstName}}, one number from the Humana story: 12,000 voluntary time-off hours found inside the schedule on top of the WFM they already had. Is intraday exception work a line your team is being asked to take down this year, or holding steady?"),
 ('Call 3, day 12, voicemail if no answer', None, "Hi {{firstName}}, Nathan at Intradiem again. Third and last call from me. [If a colleague is in the wave:] {{colleagueFirst}} has the same note, so you two can decide who it belongs to. The question is only whether intraday capacity on top of {{wfmPlatform}} is on the list this year or next. A reply to my email with one word is enough. Thanks {{firstName}}."),
 ('Email 4, day 13', 'before {{peak}}', "Hi {{firstName}},\nOne thing worth knowing before {{peak}}: Intradiem runs inside the {{wfmPlatform}} plan you've already set, so it can start before the peak rather than after it. [If a colleague is in the wave, one line names them here.]\nIs intraday capacity on the list for this year, or next?\nNathan"),
 ('LinkedIn message 3, day 15 (connected leads)', None, "{{firstName}}, [if a colleague is in the wave:] you and {{colleagueFirst}} both carry a piece of the intraday layer at {{companyName}}, so you've both got the same note from me. Twenty minutes before {{peak}} on where the drift sits on top of {{wfmPlatform}}. Which week works?"),
 ('Email 5, the close, day 17', 'leaving this here', "Hi {{firstName}},\nI'll leave this here. If {{peak}} or the exception load puts the intraday layer back on your desk, reply to this thread and I'll pick it up.\nGood luck with {{peak}}. May it treat {{companyName}}'s teams better than last year's did.\nNathan"),
]
steps_html = ''.join(f"<div class='card'><span class='tag go'>{E(t)}</span>" + (f"<p><b>Subject:</b> {E(s)}</p>" if s else '') + paras(b) + "</div>" for t, s, b in steps)
# every lead, grouped by account
lead_html = ''
for a in accts:
    rs = [r for r in rows if r['companyName'] == a]
    lead_html += f"<h3>{E(a)}</h3>" + ''.join(who(r) + e1(r) for r in rs)
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>WFM Present: Nate's read (Sep 5 2026)</title>
<style>{css}
.mail{{background:var(--zebra);border:1px solid var(--line);border-radius:var(--r);padding:18px 22px;margin-top:10px}}
.mail .subj{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600);font-weight:600;margin-bottom:8px}}
.mail p{{margin-top:8px;font-size:15px;color:var(--ink)}}
.who{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.04em;color:var(--ink-3);margin-top:18px}}
.card p{{margin-top:8px}}
h3{{margin-top:34px;font-size:18px;letter-spacing:-.01em}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}
@media(max-width:760px){{.two{{grid-template-columns:1fr}}}}
</style></head><body><div class="sheet">
<svg width="0" height="0" style="position:absolute">{logo}</svg>
<div class="hero on"><div class="wrap">
<svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">GTM Engineering · WFM Present · Nate's read · Sep 5 2026</div>
<h1 data-h="2">{n} workforce and service leaders at {len(accts)} accounts, each with the WFM platform on the record, <span class="spark">loaded and waiting on your read.</span></h1>
<p class="sub" data-h="3">Every account carries a dated read of the WFM and contact center platform it runs, none older than ten months. The copy names that platform in the first line and sells Intradiem as the intraday layer on top of it. The full list is loaded into the lemlist draft, every variable filled, ten people per account at most. <b>Nothing sends until you and Dallas say so.</b></p>
<div class="hstats" data-h="4"><div><b>{n}</b><span>leads loaded</span></div><div><b>{len(accts)}</b><span>accounts, ten people max</span></div><div><b>{len(wfm)}</b><span>WFM platforms named</span></div><div><b>0</b><span>sends</span></div></div>
</div></div>

<section><div class="wrap"><div class="tldr"><div class="k">The read in five lines</div><ul>
<li><b>Who:</b> WFM directors, workforce planning heads and contact center operations leaders at US prospects in the six verticals. Every one has a verified email already in Clay Audiences; {withurl} have a LinkedIn profile on file and get the connect branch, the rest run on email and phone.</li>
<li><b>The idea:</b> the plan their WFM builds is right at eight and wrong by ten, and the team absorbs the drift by hand. Intradiem sits on top of the WFM they already run and acts on their own rules as the day moves. No rip-and-replace, nothing new to stand up.</li>
<li><b>Numbers in the copy:</b> only the Humana on-the-record set (2.7 million automated actions last year, about two hours back per agent per month, 12,000 voluntary time-off hours counted as overtime avoided). Nothing else.</li>
<li><b>Who is not in:</b> {held_reasons.get('over the per-account cap', 0)} more people at the same accounts sit behind the ten-per-account cap (the next names on each account when the first reply lands), {held_reasons.get('outside the US', 0)} are outside the US, and {held_reasons.get('customer gate', 0)} sit at accounts the customer gate held (Optum, Aetna, Assurant, TTEC, Maximus, the AT&T U-verse unit).</li>
<li><b>Your calls on this page:</b> the platform line in the opener (it reads as informed, not as surveillance, when it points at a public job posting), the peak named per account, and the sending mailbox. {handn} of the notes were written by hand one at a time; the rest follow the same frame from each account's read.</li>
</ul></div></div></section>

<section><div class="wrap"><div class="eyebrow">What the read says</div><h2>Four WFM platforms, and the ACD next to each</h2>
<div class="two"><div><table><thead><tr><th>WFM platform</th><th>People</th><th>Accounts</th></tr></thead><tbody>{plat_rows}</tbody></table></div>
<div><table><thead><tr><th>Contact center platform</th><th>People</th><th>Accounts</th></tr></thead><tbody>{acd_rows}</tbody></table></div></div>
<p>The read comes from public job postings and vendor pages, dated to the last time the platform was seen. Verint and Calabrio accounts get the "layer Verint never finished" framing; Aspect accounts get the "plan is set, the day moves" framing; NICE accounts hear about the gap between the schedule and the floor. A rep's own confirmation always overrides the read.</p>
</div></section>

<section><div class="wrap"><div class="eyebrow">The accounts</div><h2>{len(accts)} accounts, the platform pair, and the peak each note points at</h2>
<table><thead><tr><th>Account</th><th>WFM</th><th>ACD</th><th>Read</th><th>People</th><th>Peak in the copy</th></tr></thead><tbody>{acc_rows}</tbody></table>
</div></section>

<section><div class="wrap"><div class="eyebrow">Email 1, three examples</div><h2>One per platform, the freshest read first</h2>
{''.join(who(r) + e1(r) for r in examples)}
</div></section>

<section><div class="wrap"><div class="eyebrow">After Email 1</div><h2>Seventeen business days, five emails, three calls, three LinkedIn notes</h2>
<p>The tree branches on whether a profile is on file and whether the connect is accepted. Calls are tasks in your queue with the voicemail written out; LinkedIn messages wait for your approval before they go. Every colleague line drops out on its own when nobody else at the account is in the wave.</p>
{steps_html}
</div></section>

<section><div class="wrap"><div class="eyebrow">Every Email 1</div><h2>All {n}, grouped by account, with the read that produced each opener ({vpn} VP and above)</h2>
{lead_html}
</div></section>

<section><div class="wrap"><div class="eyebrow">What Dallas does next</div><h2>On your word</h2>
<ul class="threads"><li><b>Sender and labels</b> go on in lemlist, then the integrity check runs and three previews come to you.</li><li><b>The cap</b> lifts per account on your word; the held names are in the file below.</li><li><b>Genesys Present</b> is the sister campaign for the accounts whose floor runs Genesys with no WFM read on file (354 people at 52 accounts), same tree, same proof.</li><li><b>Files</b> motions/wfm_present/WFM_Present_Full_Load_Sep5.csv (the {n} rows) · WFM_Present_Held_Sep5.csv (held names with reasons) · WFM_Present_Lemlist_Campaign_Sep5.json (campaign and step ids) · the customer-side platform reads for the back-office lane at backoffice-maps.pages.dev/platforms/</li></ul>
</div></section>
</div></body></html>"""
out = os.path.join(HERE, 'WFM_Present_Nate_Read_Sep5.html'); open(out, 'w').write(page)
dt = os.path.expanduser('~/Desktop/Intradiem Deliverables/WFM_Present_Nate_Read_Sep5.html'); open(dt, 'w').write(page)
assert '—' not in page, 'em dash in page'
print('wrote', out, 'and', dt, len(page))
