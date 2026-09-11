#!/usr/bin/env python3
"""Source the DWO executive universe LIVE from Clay search (0 credits): current C-suite / EVP / SVP / head-of operating
executives at every US six-vertical Salesforce PROSPECT account (accounts file from build_us_lists' companies dump).
Search is free and current; it returns clay_profile_id, name, location and the matched current experience, no URL and
no email. URLs come later from the free MCP bridge (find-and-enrich-list-of-contacts); emails from the Work Email routine
(paid, waved, Dallas's go). Usage: source_dwo_live.py <scratch> [--accounts <json>] [--batch 25]
Writes <scratch>/dwo_live_universe.json and prints yield per vertical and tier."""
import json,subprocess,sys,time,re,collections,os
SP=sys.argv[1]; BATCH=int(sys.argv[sys.argv.index('--batch')+1]) if '--batch' in sys.argv else 25
ACC=sys.argv[sys.argv.index('--accounts')+1] if '--accounts' in sys.argv else os.path.join(SP,'six_vertical_prospect_accounts.json')
TITLES=["Chief Operating Officer","Chief Administrative Officer","Chief Customer Officer","Chief Claims Officer","Chief Experience Officer","Chief Service Officer","Chief Transformation Officer","SVP Operations","EVP Operations","Head of Shared Services","Head of Operations","Chief Financial Officer"]
def cli(*a):
    for i in range(4):
        r=subprocess.run(['clay',*a],capture_output=True,text=True)
        try:
            d=json.loads(r.stdout)
            if isinstance(d,dict) and d.get('error'):
                code=d['error'].get('code');
                if code=='rate_limited': time.sleep(float((d['error'].get('details') or {}).get('retryAfter',20))+1); continue
                return d
            return d
        except Exception: time.sleep(5*(i+1))
    return {'error':{'code':'cli_failed'}}
accts=json.load(open(ACC)); by_dom={a['domain']:a for a in accts}
out_path=os.path.join(SP,'dwo_live_universe.json')
uni=json.load(open(out_path)) if os.path.exists(out_path) else {'people':[],'done_batches':[]}
doms=[a['domain'] for a in accts]; batches=[doms[i:i+BATCH] for i in range(0,len(doms),BATCH)]
for bi,b in enumerate(batches):
    if bi in uni['done_batches']: continue
    q='select from people where location_country = "United States" and experiences.any(is_current = true and company.domain in ('+','.join(f'"{d}"' for d in b)+') and seniority in ("C-suite","VP","Head") and job_title is_similar_to ('+','.join(f'"{t}"' for t in TITLES)+'))'
    c=cli('search','query-mode','create','--query',q); sid=c.get('searchId')
    if not sid: print('batch',bi,'create failed',str(c)[:200]);
    if not sid and (c.get('error') or {}).get('code')=='quota_exceeded': break
    if not sid: continue
    n=0
    while True:
        d=cli('search','query-mode','run',sid,'--limit','100')
        if 'data' not in d: print('batch',bi,'run stopped',str(d)[:200]); break
        for p in d['data']:
            e=(p.get('matched_experiences') or [{}])[0]
            uni['people'].append({'clay_profile_id':p.get('clay_profile_id'),'name':p.get('name'),'firstName':p.get('first_name'),'lastName':p.get('last_name'),'location':(p.get('location') or {}).get('name'),'company':e.get('company'),'title':e.get('title'),'start_date':e.get('start_date'),'batch':bi,'search_id':sid})
        n+=len(d['data'])
        if not d.get('hasMore'): break
    uni['done_batches'].append(bi); json.dump(uni,open(out_path,'w'))
    print(f'batch {bi+1}/{len(batches)}: {n} people (total {len(uni["people"])})',flush=True)
# summarize
def tier(t): return 'C-level' if re.search(r'chief|\bc[oafe]o\b|\bcxo\b|\bcco\b',t or '',re.I) else 'EVP/SVP/Head' if re.search(r'evp|svp|executive vice|senior vice|head of',t or '',re.I) else 'VP/other'
print('TOTAL people',len(uni['people']),'| companies',len({p['company'] for p in uni['people']}),'| tier',dict(collections.Counter(tier(p['title']) for p in uni['people'])))
