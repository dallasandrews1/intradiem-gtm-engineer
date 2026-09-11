#!/usr/bin/env python3
"""Full-motion load plan for the platform-keyed motions (Sep 5 2026). No waves: every qualified person in the
motion's Audiences people segment is planned, with a per-account cap and the standing exclusions.

usage: build_full_load.py <wfm|genesys> <scratch> [--cap N] [--go]
  scratch holds: <m>_people (raw records), <m>_cos_records.json, <m>_map.json (company -> people ids),
                 lemlist_lead_index.json, inmotion_domains.txt
Dry run writes <Motion>_Full_Load_Sep5.csv + <Motion>_Held_Sep5.csv next to this script (or motions/genesys_present).
--go loads the plan into the motion's DRAFT campaign with deduplicate=true. Never launches, never sets a sender."""
import csv, json, os, re, sys, hashlib, subprocess, collections, datetime
M = sys.argv[1]; SP = sys.argv[2]; GO = '--go' in sys.argv
CAP = int(sys.argv[sys.argv.index('--cap') + 1]) if '--cap' in sys.argv else 10
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = HERE if M == 'wfm' else os.path.join(ROOT, 'motions', 'genesys_present'); os.makedirs(OUT, exist_ok=True)
CAMP = {'wfm': 'cam_K6dGjBt6WukSo3jvB', 'genesys': 'cam_b7TS4fCDCnt2f8S84'}[M]
MOTION = {'wfm': 'wfm_present', 'genesys': 'genesys_present'}[M]
PEOPLE = {'wfm': 'wfm_people_raw.json', 'genesys': 'gen_people_records.json'}[M]
COS = {'wfm': 'wfm_cos_records.json', 'genesys': 'gen_cos_records.json'}[M]
MAP = {'wfm': 'wfm_map.json', 'genesys': 'gen_map.json'}[M]
F_ACD, F_ACD_SEEN, F_WFM, F_ALL, F_REP = 'audf_0tkv9tyqFQ6H2g2ESvx', 'audf_0tkv9ty3of7Ng2tHFev', 'audf_0tkv9tzQXmR5ZVaK4Mc', 'audf_0tkv9tzfu29933xgTW5', 'audf_0tkveafmZS5BQqgqYuQ'
ENV = '/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
PROOF = "Humana runs it on top of the WFM it already had: 2.7 million automated actions last year, and about two hours back per agent per month."

people = json.load(open(f'{SP}/{PEOPLE}')); people = people if isinstance(people, list) else people['records']
cos = {str(c['recordId']): c for c in json.load(open(f'{SP}/{COS}'))}
mp = json.load(open(f'{SP}/{MAP}'))
idx = json.load(open(f'{SP}/lemlist_lead_index.json')); lead_index = idx['lead_index']
inmotion = {l.strip().lower() for l in open(f'{SP}/inmotion_domains.txt') if l.strip()}
wfm_cos_domains = {c['fields'].get('normalized_domain', '').lower() for c in json.load(open(f'{SP}/wfm_cos_records.json'))} if M == 'genesys' else set()
exd = {(c['fields'].get('normalized_domain') or c['fields'].get('domain') or '').lower() for c in json.load(open(f'{SP}/sf_exclusion_cos.json'))}
GATE_HOLD = {'assurant.com': 'Assurant is a customer account (Inger), subsidiary record tagged Prospect', 'maximus.com': 'Maximus sits in the BO Expansion customer lane; status to confirm with Nate',
             'ttec.com': 'TTEC Digital is on the exclusion list (partner); parent held', 'att.com/uverse': 'AT&T Entertainment Group is on the exclusion list; U-verse unit held',
             'optum.com': 'Optum is on the exclusion list', 'aetna.com': 'Aetna is on the exclusion list'}
hand = {}
if M == 'wfm':
    hand = {r['email'].lower(): r for r in csv.DictReader(open(os.path.join(HERE, 'WFM_Present_Wave1_Load_Sep5.csv')))}
person_co = {}
for cid, v in mp.items():
    for pid in v['people']: person_co.setdefault(pid, cid)

NAME_MAP = {'American International Group (AIG)': 'AIG', 'AT&T U-Verse': 'AT&T', 'AT&T Services - Backoffice': 'AT&T', 'Aetna Claims': 'Aetna', 'Aetna Clinical': 'Aetna',
 'BlueCross BlueShield South Carolina (BCBS SC)': 'BlueCross BlueShield of South Carolina', 'Centene Corporation': 'Centene', 'Cigna Corporation': 'Cigna', 'Concentrix - CRM - GM - CARS': 'Concentrix',
 'First Citizens BancShares, Inc.': 'First Citizens', 'General Motors Financial Company': 'GM Financial', 'IBM GBS (Global Business Services)': 'IBM', 'IBM TFL': 'IBM', 'Kemper Corporation': 'Kemper',
 'Lumen Technologies (formerly CenturyLink)': 'Lumen', 'M&T Bank Corporation': 'M&T Bank', 'Manulife Financial Corporation': 'Manulife', 'McKesson Inc': 'McKesson', 'Modivcare (formerly Logisticare)': 'Modivcare',
 'NRG Energy, Inc.': 'NRG Energy', 'Nationwide Mutual Insurance Company': 'Nationwide', 'Nv Energy': 'NV Energy', 'OGE Energy Corp.': 'OGE Energy', 'Petco Animal Supplies, Inc.': 'Petco',
 'Premera Blue Cross Washington (BCBS WA)': 'Premera Blue Cross', 'Principal Financial Group': 'Principal', 'Progressive Insurance': 'Progressive', 'Southwest Business Corporation (SWBC)': 'SWBC',
 'Sutherland Global Services': 'Sutherland', 'Tech Mahindra Limited': 'Tech Mahindra', 'The Dayton Power and Light Company': 'Dayton Power and Light', 'The Hartford Financial Services Group': 'The Hartford',
 'W.W. Grainger (aka Grainger)': 'Grainger', 'eHealth , Inc.': 'eHealth', 'loanDepot.com LLC': 'loanDepot', 'Target Corporation': 'Target', 'Safelite Auto Glass': 'Safelite', 'Interstate Gas Supply, Inc': 'IGS Energy',
 'Independent Health Corporation': 'Independent Health', 'Huntington National Bank': 'Huntington', 'American Bankers Life Assurance Company of Florida': 'Assurant', 'Optum360': 'Optum', 'Ascension Health': 'Ascension',
 'Duluth Trading Co.': 'Duluth Trading', 'Tampa Electric Company': 'Tampa Electric', 'VyStar Credit Union': 'VyStar', 'Blue Shield of California (BSCA)': 'Blue Shield of California', 'Republic Services': 'Republic Services', 'WAL-MART STORES (U K) LTD': 'Walmart', 'Canada Life Assurance Company': 'Canada Life'}
def short_co(name):
    if name in NAME_MAP: return NAME_MAP[name]
    n = re.sub(r'\s*\([^)]*\)\s*', ' ', name or '').strip()
    n = re.sub(r'(?:,|\s)\s*(inc\.?|corporation|corp\.?|company|co\.?|llc|group|holdings|ltd\.?|plc|incorporated|n\.a\.)\s*$', '', n, flags=re.I).strip()
    return n or name
def poss(co): return co + ("'" if co.endswith('s') else "'s")
def when(d):
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})', d or '')
    if not m: return None
    y, mo, dd = map(int, m.groups()); mon = datetime.date(y, mo, 1).strftime('%B')
    part = 'early' if dd <= 10 else 'mid' if dd <= 20 else 'late'
    return f"{part}-{mon}" if part == 'mid' else f"{part} {mon}"
def wfm_date(allp, wfm):
    m = re.search(re.escape(wfm) + r'[^()]*\((\d{4}-\d{2}-\d{2})\)', allp or '')
    return m.group(1) if m else None
def seat(title):
    t = (title or '').lower()
    return 'wfm' if re.search(r'workforce|wfm|real[- ]time|scheduling|forecast|capacity plan|command center', t) else 'ops'
def tier(title):
    t = (title or '').lower()
    return 0 if re.search(r'\b(svp|evp|vp|vice president|chief|head of|president)\b', t) else 1
def industry_bucket(ind):
    i = (ind or '').lower()
    if 'payer' in i or 'managed' in i or 'health plan' in i: return 'payer'
    if 'provider' in i or 'hospital' in i: return 'provider'
    if 'health' in i: return 'payer'
    if 'auto' in i or 'p&c' in i or 'property' in i: return 'pc'
    if 'insurance' in i or 'life' in i or 'annuit' in i: return 'life'
    if 'bank' in i: return 'bank'
    if 'financial' in i or 'fs' in i or 'lend' in i or 'mortgage' in i or 'card' in i: return 'fs'
    if 'utilit' in i or 'energy' in i: return 'utility'
    if 'retail' in i or 'consumer' in i or 'e-comm' in i: return 'retail'
    if 'telco' in i or 'cable' in i or 'telecom' in i or 'wireless' in i: return 'telco'
    if 'business services' in i or 'bpo' in i or 'outsourc' in i: return 'bpo'
    return 'other'
PEAK = {'payer': 'open enrollment', 'provider': 'flu season', 'pc': 'catastrophe season', 'life': 'the Q4 claims and renewal peak', 'bank': 'the January statement and tax surge', 'fs': 'year-end', 'utility': 'storm season', 'retail': 'the holiday peak', 'telco': 'the fall device launches', 'bpo': 'client Q4 ramps', 'other': 'year-end'}
TEAMS = {'payer': 'member services teams', 'provider': 'patient access teams', 'pc': 'claims and service teams', 'life': 'claims and service teams', 'bank': 'servicing teams', 'fs': 'servicing teams', 'utility': 'customer care teams', 'retail': 'customer service teams', 'telco': 'customer care teams', 'bpo': 'client programs', 'other': 'service teams'}
ASK = {'wfm': "How much of your team's day is intraday exception work rather than planning?", 'ops': "How much of the plan survives past ten on a heavy day?", 'bpo': "Which client programs carry the most intraday exception work for your team today?"}
IDEA_WFM = {
 ('Verint', 'wfm'): "Intradiem is the intraday layer Verint never finished: it watches real-time conditions against the plan and acts on the rules your team already applies by hand, offline windows, adherence nudges, breaks moved, training pushed into the slack.",
 ('Verint', 'ops'): "Intradiem is the intraday layer on top of Verint: it reads real-time conditions against the schedule and acts on the rules your team applies by hand, so adherence, breaks and training move themselves as the day drifts.",
 ('Calabrio', 'wfm'): "Intradiem is the intraday layer on top of Calabrio: it reads real-time conditions against the schedule and acts on the rules your team applies by hand, so adherence, breaks and training move themselves as the day drifts.",
 ('Calabrio', 'ops'): "Intradiem sits on top of Calabrio and acts inside the plan as the day moves, so the exception work your team chases by hand happens automatically, and the recovered minutes show up as capacity rather than overtime.",
 ('Aspect', 'wfm'): "Intradiem sits on top of Aspect and acts inside the plan as the day moves, so the exception work your team chases by hand happens automatically, and the recovered minutes show up as capacity rather than overtime.",
 ('Aspect', 'ops'): "Intradiem is the intraday layer on top of Aspect: it reads real-time conditions against the schedule and acts on the rules your team applies by hand, so adherence, breaks and training move themselves as the day drifts.",
 ('NICE', 'wfm'): "Intradiem is the intraday layer on top of NICE: it reads real-time conditions against the schedule and acts on the rules your team applies by hand, so adherence, breaks and training move themselves as the day drifts.",
 ('NICE', 'ops'): "Intradiem sits on top of NICE and acts inside the plan as the day moves, so the exception work your team chases by hand happens automatically, and the recovered minutes show up as capacity rather than overtime.",
}
def idea(acd, wfm, st, allp):
    if M == 'wfm':
        return IDEA_WFM.get((wfm, st)) or IDEA_WFM.get((wfm, 'wfm')) or IDEA_WFM[('Calabrio', st)].replace('Calabrio', wfm)
    native = 'Genesys Cloud' in (allp or '')
    lead = "Intradiem integrates natively with Genesys Cloud as the intraday layer" if native else f"Intradiem sits on top of {acd} as the intraday layer"
    if st == 'wfm':
        return f"{lead}: it reads real-time conditions against the plan and acts on the rules your team applies by hand, offline windows, adherence nudges, breaks moved, training pushed into the slack."
    return f"{lead}: it reads real-time conditions against the schedule and acts on your rules by itself, so adherence, breaks and training move as the day drifts."
def opener(co, acd, acd_when, wfm, wfm_when, dom):
    v = int(hashlib.md5(dom.encode()).hexdigest(), 16) % 3
    w = acd_when or wfm_when
    if M == 'wfm':
        if acd and w:
            return [f"{wfm} under the schedule and {acd} on the floor, both in {poss(co)} own postings as of {w}, which usually means the plan is right at eight and wrong by ten.",
                    f"{poss(co)} postings named {wfm} for the schedule and {acd} on the floor as recently as {w}. The plan those two produce is right at eight and wrong by ten.",
                    f"As of {w}, {co} was hiring against {wfm} for workforce management with {acd} on the floor. That pairing sets a plan the day starts moving against by mid-morning."][v]
        return f"{wfm} under the schedule at {co}, in its own postings as of {w or 'this year'}, which usually means the plan is right at eight and wrong by ten."
    return [f"{acd} on the floor at {co}, in its own postings as of {w}, which usually means the schedule is right at eight and the floor has moved by ten.",
            f"{poss(co)} postings named {acd} on the floor as recently as {w}. The schedule set the night before is right at eight and wrong by ten, and someone absorbs the drift by hand.",
            f"As of {w}, {co} was hiring against {acd} on the floor. The plan the day starts against is right at eight and moving by ten."][v]

plan, held = [], []; reasons = collections.Counter()
by_acct = collections.defaultdict(list)
for p in people:
    f = p['fields']; pid = str(p['recordId']); e = (f.get('email') or '').lower(); u = (f.get('linkedin_url') or '').lower().rstrip('/')
    cid = person_co.get(pid); c = cos.get(cid) if cid else None
    r = None
    if not c: r = 'no account match in the motion segment'
    elif (f.get('location_country') or 'United States') not in ('United States', 'US'): r = 'outside the US: ' + f.get('location_country')
    elif e in lead_index or (u and u in lead_index): r = 'already a lead in: ' + ', '.join(sorted(set(lead_index.get(e, []) + lead_index.get(u, []))))
    elif M == 'genesys' and c['fields'].get('normalized_domain', '').lower() in wfm_cos_domains: r = 'account belongs to WFM Present'
    elif not e: r = 'no email'
    elif c['fields'].get('normalized_domain', '').lower() in exd: r = 'customer gate: account on the Salesforce exclusion segment'
    elif c['fields'].get('normalized_domain', '').lower() in GATE_HOLD: r = 'customer gate: ' + GATE_HOLD[c['fields'].get('normalized_domain', '').lower()]
    if r:
        reasons[r.split(':')[0]] += 1; held.append({'name': f.get('name'), 'title': f.get('title'), 'account': (c or {}).get('fields', {}).get('org_name'), 'email': e, 'reason': r}); continue
    by_acct[cid].append(p)
for cid, ps in by_acct.items():
    c = cos[cid]['fields']; co = short_co(c.get('org_name')); dom = c.get('normalized_domain', '').lower(); ib = industry_bucket(c.get('industry'))
    acd = c.get(F_ACD) or ''; wfm = c.get(F_WFM) or ''; allp = c.get(F_ALL) or ''; rep = c.get(F_REP) or ''
    if rep:
        mm = re.match(r'\s*([A-Za-z0-9 ]+?)\s*\((WFM|ACD)', rep)
        if mm and mm.group(2) == 'WFM': wfm = mm.group(1).strip()
        elif mm: acd = mm.group(1).strip()
    ps.sort(key=lambda p: (0 if (p['fields'].get('email') or '').lower() in hand else 1, tier(p['fields'].get('title')), 0 if seat(p['fields'].get('title')) == 'wfm' else 1, 0 if p['fields'].get('linkedin_url') else 1, p['fields'].get('name') or ''))
    for i, p in enumerate(ps):
        f = p['fields']; e = f['email'].lower(); st = seat(f.get('title'))
        if i >= CAP:
            reasons['over the per-account cap'] += 1; held.append({'name': f.get('name'), 'title': f.get('title'), 'account': co, 'email': e, 'reason': f'over the per-account cap of {CAP}'}); continue
        h = hand.get(e)
        row = {'email': e, 'firstName': f.get('first_name') or '', 'lastName': f.get('last_name') or '', 'companyName': co, 'jobTitle': f.get('title') or '',
               'linkedinUrl': f.get('linkedin_url') or '', 'domain': dom, 'industry': c.get('industry') or '', 'seat': st, 'tier': tier(f.get('title')),
               'acdPlatform': acd, 'acdLastSeen': c.get(F_ACD_SEEN) or '', 'wfmPlatform': wfm, 'wfmLastSeen': wfm_date(allp, wfm) or '',
               'motion': MOTION, 'motionStatus': 'loaded', 'source': 'hand' if h else 'generated'}
        if h:
            for k in ('opener', 'angleIdea', 'angleProof', 'angleAsk', 'peak', 'workTeams', 'colleagueFirst', 'colleagueLine'): row[k] = h[k]
        else:
            row['opener'] = opener(co, acd, when(row['acdLastSeen']), wfm, when(row['wfmLastSeen']), dom)
            row['angleIdea'] = idea(acd, wfm, st, allp); row['angleProof'] = PROOF
            row['angleAsk'] = ASK['bpo'] if ib == 'bpo' else ASK[st]
            row['peak'] = PEAK[ib]; row['workTeams'] = TEAMS[ib]; row['colleagueFirst'] = ''; row['colleagueLine'] = ''
            words = sum(len(row[k].split()) for k in ('opener', 'angleIdea', 'angleProof', 'angleAsk')) + 3
            if words > 110:
                w_ = when(row['acdLastSeen']) or when(row['wfmLastSeen']) or 'this year'
                row['opener'] = (f"{wfm} under the schedule and {acd} on the floor at {co}, in its own postings as of {w_}. The plan is right at eight and wrong by ten." if M == 'wfm' and acd
                                 else f"{wfm} under the schedule at {co}, in its own postings as of {w_}. The plan is right at eight and wrong by ten." if M == 'wfm'
                                 else f"{acd} on the floor at {co}, in its own postings as of {w_}. The schedule is right at eight and the floor has moved by ten.")
                words = sum(len(row[k].split()) for k in ('opener', 'angleIdea', 'angleProof', 'angleAsk')) + 3
                if words > 110:
                    base = (wfm if M == 'wfm' else acd)
                    row['angleIdea'] = f"Intradiem is the intraday layer on top of {base}: it reads real-time conditions against the schedule and acts on your rules by itself, so adherence, breaks and training move as the day drifts."
                    words = sum(len(row[k].split()) for k in ('opener', 'angleIdea', 'angleProof', 'angleAsk')) + 3
            row['e1Words'] = words
        plan.append(row)
plan.sort(key=lambda r: (r['companyName'], r['tier'], r['lastName']))
if '--reconcile' in sys.argv:
    # after a --go: anything planned that lemlist did not accept (its own cross-campaign dedupe) moves to held
    KEY_ = [l.split('=', 1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
    out_ = subprocess.run(['curl', '-s', '-u', f':{KEY_}', f'https://api.lemlist.com/api/campaigns/{CAMP}/export/leads?state=all&format=json'], capture_output=True, text=True).stdout
    live_ = {(l.get('email') or '').lower() for l in json.loads(out_) if isinstance(l, dict)}
    keep_ = []
    for r in plan:
        if r['email'] in live_: keep_.append(r)
        else:
            reasons['rejected by lemlist dedupe'] += 1
            held.append({'name': f"{r['firstName']} {r['lastName']}", 'title': r['jobTitle'], 'account': r['companyName'], 'email': r['email'], 'reason': 'rejected by lemlist dedupe: already a lead in another campaign'})
    plan = keep_
name = {'wfm': 'WFM_Present', 'genesys': 'Genesys_Present'}[M]
cols = ['email', 'firstName', 'lastName', 'companyName', 'jobTitle', 'linkedinUrl', 'opener', 'angleIdea', 'angleProof', 'angleAsk', 'peak', 'workTeams', 'wfmPlatform', 'acdPlatform', 'colleagueFirst', 'colleagueLine', 'motion', 'motionStatus', 'domain', 'industry', 'seat', 'tier', 'acdLastSeen', 'wfmLastSeen', 'source', 'e1Words']
w = csv.DictWriter(open(os.path.join(OUT, f'{name}_Full_Load_Sep5.csv'), 'w', newline=''), fieldnames=cols, extrasaction='ignore'); w.writeheader(); w.writerows(plan)
w = csv.DictWriter(open(os.path.join(OUT, f'{name}_Held_Sep5.csv'), 'w', newline=''), fieldnames=['name', 'title', 'account', 'email', 'reason']); w.writeheader(); w.writerows(held)
accts = len({r['domain'] for r in plan}); over = [r for r in plan if r.get('e1Words', 0) > 110]
bad = [r['email'] for r in plan if '—' in (r['opener'] + r['angleIdea'] + r['angleAsk']) or r['angleAsk'].count('?') != 1]
print(f"{MOTION}: planned {len(plan)} at {accts} accounts (cap {CAP}); hand-written {sum(1 for r in plan if r['source']=='hand')}; held {len(held)} -> {dict(reasons)}; over 110 words {len(over)}; QC issues {bad or 'none'}")
print('platforms', collections.Counter(r['wfmPlatform' if M == 'wfm' else 'acdPlatform'] for r in plan).most_common(), '| seats', collections.Counter(r['seat'] for r in plan), '| with URL', sum(1 for r in plan if r['linkedinUrl']))
if not GO: print('DRY RUN, nothing loaded'); sys.exit(0)
KEY = [l.split('=', 1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
def curl(m, p, b=None):
    a = ['curl', '-s', '-u', f':{KEY}', '-X', m, 'https://api.lemlist.com' + p, '-H', 'Content-Type: application/json']
    if b is not None: a += ['-d', json.dumps(b)]
    out = subprocess.run(a, capture_output=True, text=True).stdout
    try: return json.loads(out)
    except Exception: return {'raw': out[:200]}
have = {(l.get('email') or '').lower() for l in (curl('GET', f'/api/campaigns/{CAMP}/export/leads?state=all&format=json') or []) if isinstance(l, dict)}
ok = err = 0
for r in plan:
    if r['email'] in have: continue
    body = {k: r[k] for k in ('firstName', 'lastName', 'companyName', 'jobTitle', 'linkedinUrl', 'opener', 'angleIdea', 'angleProof', 'angleAsk', 'peak', 'workTeams', 'wfmPlatform', 'acdPlatform', 'colleagueFirst', 'colleagueLine', 'motion', 'motionStatus')}
    body['companyDomain'] = r['domain']; body['parentAccount'] = r['companyName']; body['acdLastSeen'] = r['acdLastSeen']
    res = curl('POST', f'/api/campaigns/{CAMP}/leads/{r["email"]}?deduplicate=true', body)
    if res.get('_id'): ok += 1
    else: err += 1; print('ERR', r['email'], str(res)[:160])
print('loaded', ok, 'errors', err, 'already there', len(have))
