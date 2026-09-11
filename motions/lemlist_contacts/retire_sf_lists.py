#!/usr/bin/env python3
"""Retire the Salesforce-mirror `(SF)` contact lists in lemlist (Dallas, Sep 4 2026: suppression lives in Clay
Audiences, lemlist holds only rows a rep could sequence; the (SF) lists only cause confusion).

Rules
- A contact is DELETED only when every list it sits on is an (SF) list AND it is in no campaign.
- A contact that also sits on any non-SF list (the live DWO pool, Stars, Blitz, BO Net-New, etc.) or that is a lead in
  any campaign is KEPT as a contact and only REMOVED from the (SF) lists (membership only).
- lemlist has no API to delete a list; once empty, Dallas deletes the three shells in the Contacts UI.

Usage: retire_sf_lists.py [--go]        (dry run by default; writes a plan JSON next to this file)
"""
import json, os, sys, subprocess, time, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = '/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY = next(l.split('=', 1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY='))
GO = '--go' in sys.argv
SF_LISTS = {
    'clt_wgDkc4GbiL929XthY': 'BO Leaders Prospects Dir+ (SF)',
    'clt_ddYJ2PYTPGTfJXw7D': 'Sep 2 Webinar Prospects, WFM Dir+ (SF)',
    'clt_FKm6KuNcgeghas73o': 'DWO Executives, Prospects (SF)',
}


def curl(m, p, b=None):
    a = ['curl', '-s', '-u', f':{KEY}', '-X', m, 'https://api.lemlist.com' + p, '-H', 'Content-Type: application/json']
    if b is not None:
        a += ['-d', json.dumps(b)]
    for _ in range(3):
        out = subprocess.run(a, capture_output=True, text=True).stdout
        try:
            return json.loads(out) if out.strip() else {}
        except Exception:
            time.sleep(2)
    return {'raw': out[:200]}


def list_members(lid):
    rows, off = [], 0
    while True:
        r = curl('GET', f'/api/contacts?listId={lid}&limit=500&offset={off}')
        data = r.get('data') if isinstance(r, dict) else None
        if data is None:
            print('  read error', lid, str(r)[:160]); break
        rows += data; off += len(data)
        if not data or off >= r.get('total', 0):
            break
    return rows


# 1. every list in the workspace
lists = curl('GET', '/api/contacts/lists')
lists = lists if isinstance(lists, list) else lists.get('data', [])
lists = [l for l in lists if l.get('entity', 'contact') == 'contact']
print(f'{len(lists)} contact lists')
member_of = collections.defaultdict(set)   # contact id -> set(list ids)
contact = {}                                # id -> record
for l in lists:
    lid = l['_id']; rows = list_members(lid)
    tag = 'SF' if lid in SF_LISTS else 'keep'
    print(f'  {tag:4} {l["name"][:45]:45} {lid} {len(rows)}')
    for c in rows:
        member_of[c['_id']].add(lid); contact[c['_id']] = c

# 2. classify
sf_ids = {cid for cid, ls in member_of.items() if ls & set(SF_LISTS)}
delete, unlist_only, reasons = [], [], collections.Counter()
for cid in sf_ids:
    c = contact[cid]; ls = member_of[cid]
    if ls - set(SF_LISTS):
        unlist_only.append(cid); reasons['also on a live list'] += 1
    elif c.get('campaigns'):
        unlist_only.append(cid); reasons['lead in a campaign'] += 1
    else:
        delete.append(cid)
print(f'\nSF-list contacts {len(sf_ids)} | DELETE {len(delete)} | keep contact, remove from SF lists only {len(unlist_only)} {dict(reasons)}')
plan = {'sf_lists': SF_LISTS, 'delete': delete, 'unlist_only': unlist_only, 'reasons': dict(reasons),
        'sample_delete': [{k: contact[i].get(k) for k in ('_id', 'fullName', 'email')} for i in delete[:5]]}
json.dump(plan, open(os.path.join(HERE, 'retire_sf_lists_plan.json'), 'w'), indent=1)
if not GO:
    print('DRY RUN, plan written to retire_sf_lists_plan.json'); sys.exit(0)

# 3. delete contacts whose only home was an SF list
ok = collections.Counter()
for i, cid in enumerate(delete, 1):
    r = curl('DELETE', f'/api/contacts/{cid}')
    ok['deleted' if isinstance(r, dict) and not r.get('error') and 'raw' not in r else 'error'] += 1
    if ok['error'] and ok['error'] <= 3 and 'error' in str(r).lower():
        print('  delete error', cid, str(r)[:160])
    if i % 200 == 0:
        print(f'  {i}/{len(delete)} {dict(ok)}', flush=True)
print('deletes', dict(ok))

# 4. strip remaining members from the SF lists (membership only), leaving empty shells
for lid, name in SF_LISTS.items():
    ids = [cid for cid in unlist_only if lid in member_of[cid]]
    removed = 0
    for j in range(0, len(ids), 1000):
        r = curl('POST', f'/api/contacts/lists/{lid}/entities?action=remove', {'contactIds': ids[j:j + 1000]})
        removed += r.get('removedCount', 0) if isinstance(r, dict) else 0
    left = len(list_members(lid))
    print(f'  {name}: removed {removed} memberships, {left} left on list')
print('\nDone. Delete the three empty (SF) lists in lemlist > Contacts > Lists (no API for list deletion).')
