#!/usr/bin/env python3
"""Build the candidate rows for the US lemlist Contacts lists (us_lists_config.json), one list per motion.

Pulls every source fresh (Clay tables and Audiences segments by CLI, lemlist campaign leads by API), applies the
customer-exclusion union (SF Customer/Partner segment + install-base table + denylist + the customer-lane domain map),
keeps US people only (country, else email TLD), dedupes on email and LinkedIn URL, and stamps motion / parentAccount.
Company names for Audiences people come from the SF Account ID -> Audiences company map (the person-level Company
field is lead-only). Usage: build_us_lists.py <scratch_dir> [--cache] ; writes <scratch>/us_lists_candidates.json,
<scratch>/has_motion_keys.json and prints the count per list. Zero credits: reads only."""
import csv,json,os,re,sys,subprocess,collections
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
SP=sys.argv[1]; CACHE='--cache' in sys.argv
CFG=json.load(open(os.path.join(HERE,'us_lists_config.json')))
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
def cli(*a): return json.loads(subprocess.run(['clay',*a],capture_output=True,text=True).stdout)
def cached(name,fn):
    p=os.path.join(SP,name)
    if CACHE and os.path.exists(p): return json.load(open(p))
    v=fn(); json.dump(v,open(p,'w')); return v
def table(tid):
    rows=[]; cur=None
    while True:
        d=cli(*(['tables','rows','list',tid,'--limit','100']+(['--cursor',cur] if cur else []))); rows+=d['data']; cur=d.get('cursor')
        if not cur: break
    return [{'id':r['id'],**{k:(v.get('value') if v.get('status')=='success' else None) for k,v in r['cells'].items()}} for r in rows]
def segment(seg,etype):
    ids=[]; cur=None
    while True:
        d=cli(*(['audiences','records','search-ids','--entity-type',etype]+(['--audience-id',seg] if seg else [])+['--limit','1000']+(['--cursor',cur] if cur else []))); ids+=d['data']; cur=d.get('cursor')
        if not cur: break
    recs=[]
    for i in range(0,len(ids),100): recs+=cli('audiences','records','get','--entity-type',etype,'--ids',','.join(map(str,ids[i:i+100])))['data']
    return recs
def leads(cid):
    out=subprocess.run(['curl','-s','-u',f':{KEY}',f'https://api.lemlist.com/api/campaigns/{cid}/export/leads?state=all&format=json'],capture_output=True,text=True).stdout
    try: return json.loads(out)
    except Exception: return []
def norm(s): return re.sub(r'[^a-z0-9 ]','',(s or '').lower()).replace(' inc','').replace(' corporation','').replace(' company','').strip()
# exclusion union
sf=cached('sf_exclusion_companies.json',lambda: segment(CFG['exclusion']['sf_segment_companies'],'companies'))
ib=cached('install_base.json',lambda: table(CFG['exclusion']['install_base_table']))
dl=json.load(open(os.path.join(ROOT,CFG['exclusion']['denylist'])))
src=open(os.path.join(ROOT,'motions/back_office_expansion/build_customer_wave1.py')).read(); DOM=eval(src.split("DOM=")[1].split("\nPA=")[0])
ex_domains={(r['fields'].get('normalized_domain') or '').lower() for r in sf}|set(dl['domains'])|{d for v in DOM.values() for d in v}
ex_domains|=set(json.load(open(os.path.join(HERE,'exclusion_extra_domains.json'))))
ex_domains.discard('')
ex_names=[n for n in ([norm(r['fields'].get('org_name')) for r in sf]+[norm(r.get('f_0ti4jj2wiPhYXNvZZxA')) for r in ib]+dl['name_aliases']) if n and len(n)>3]
def excluded(name,domain,email):
    d=(domain or '').lower().replace('www.',''); e=(email or '').lower().split('@')[-1] if email else ''
    for x in ex_domains:
        if d==x or d.endswith('.'+x) or (e and (e==x or e.endswith('.'+x))): return 'domain:'+x
    n=norm(name)
    for x in ex_names:
        if re.search(r'\b'+re.escape(x)+r'\b',n): return 'name:'+x
    return ''
tlds='|'.join(CFG['non_us_email_tlds'])
def is_us(country,email):
    c=(country or '').strip().lower(); e=(email or '').lower()
    if c in ('united states','united states of america','us','usa'): return True
    if c: return False
    return not re.search(r'\.('+tlds+r')$',e)
companies=cached('companies_all.json',lambda: {str(r['recordId']):{'name':r['fields'].get('org_name'),'domain':(r['fields'].get('normalized_domain') or '').lower(),'sf_account':next((aid for org in (json.loads(r['fields'].get('external_source_sync_status_v3') or '{}').get('SALESFORCE',{}) or {}).values() for aid in (org.get('account') or {}).keys()),None),'type':r['fields'].get('audf_0timw0xX6CfUdJXJznM'),'country':r['fields'].get('location_country')} for r in segment(None,'companies')})
by_sf={v['sf_account']:v for v in companies.values() if v.get('sf_account')}
def row(first,last,email,li,co,dom,title,motion,parent,src):
    return {'firstName':first or '','lastName':last or '','email':(email or '').strip(),'linkedinUrl':(li or '').strip(),'companyName':co or '','companyDomain':dom or '','jobTitle':title or '','motion':motion,'parentAccount':parent or co or '','src':src}
out={}
# Stars: table + the three Stars campaigns
s=cached('stars_committee.json',lambda: table('t_0thtm73HHxyiupTuepK')); rows=[]
for r in s:
    fn=(r.get('f_0thtm74dzuASRCbAExz') or '').split(' ')
    rows.append(row(fn[0],' '.join(fn[1:]),r.get('f_0thx699qdHjGY5zW7fH') or r.get('f_0thtm75SRgJxZBohRZm'),r.get('f_0thtm75CBvmFqsy4WC9'),r.get('f_0thtm74JvDBs8jimWYf'),r.get('f_0thtm75xyuXYN6UMwTS'),r.get('f_0thtm74WsoQtAf6vg6m'),'stars',None,'table'))
for cid in ['cam_sh3JCJoxtEHyjGrsw','cam_viEbB6HkYsCPtxKbi','cam_2gy9hmEvMjYEuPZ8A']:
    for l in cached(f'leads_{cid}.json',lambda c=cid: leads(c)): rows.append(row(l.get('firstName'),l.get('lastName'),l.get('email'),l.get('linkedinUrl'),l.get('companyName'),l.get('companyDomain'),l.get('jobTitle'),'stars',l.get('parent_account'),cid))
out['stars']=rows
rows=[]
for cid in ['cam_yWefPqaDhNNv4RyQK','cam_fYp7Nh9wB72gfMke6']:
    for l in cached(f'leads_{cid}.json',lambda c=cid: leads(c)): rows.append(row(l.get('firstName'),l.get('lastName'),l.get('email'),l.get('linkedinUrl'),l.get('companyName'),l.get('companyDomain'),l.get('jobTitle'),'blitz',None,cid))
out['blitz']=rows
w=cached('wfm_l3.json',lambda: table('t_0tic8arWbZp8bSx87Ad')); cnt=collections.Counter(r.get('f_0ti8tdqbxQo5dNucJjc') for r in w); rows=[]; noise=0
for r in w:
    co=r.get('f_0ti8tdqbxQo5dNucJjc') or ''
    if cnt[co]<CFG['wfm_min_rows_per_company']: noise+=1; continue
    rows.append(row(r.get('f_0ti8tdqKabRw8T5JFpv'),r.get('f_0ti8tdqTvG5rzPcjy83'),r.get('f_0ti9f743tZjXdBgDApr'),r.get('f_0ti8tdr2u6KpEcpakcQ'),co,r.get('f_0ti8tdrnCsHVcUNjmh8'),r.get('f_0ti8tdqMAWD2Nmo2ErE'),'wfm_adjacency',None,'table'))
out['wfm_adjacency']=rows; print('wfm search-noise rows dropped',noise)
c=cached('cost_mandate.json',lambda: table('t_0ti8tdqQAXiWMkx76Jj'))
out['cost_mandate']=[row(r.get('f_0ti8tdqKabRw8T5JFpv'),r.get('f_0ti8tdqTvG5rzPcjy83'),r.get('f_0ti9f743tZjXdBgDApr'),r.get('f_0ti8tdr2u6KpEcpakcQ'),r.get('f_0ti8tdqbxQo5dNucJjc'),r.get('f_0ti8tdrnCsHVcUNjmh8'),r.get('f_0ti8tdqMAWD2Nmo2ErE'),'cost_mandate',None,'table') for r in c]
def aud(seg,name,motion):
    rows=[]; nonus=0
    for r in cached(name,lambda: segment(seg,'people')):
        f=r['fields']
        if not is_us(f.get('location_country'),f.get('email')): nonus+=1; continue
        co=by_sf.get(f.get('audf_0timw68Jf4dTsQQqq38')) or {}
        dom=co.get('domain') or ((f.get('email') or '').split('@')[-1] if f.get('email') else '')
        rows.append(row(f.get('first_name'),f.get('last_name'),f.get('email'),f.get('linkedin_url'),co.get('name') or f.get('audf_0tkdvkhYzHJGF3NrfqG') or dom,dom,f.get('title'),motion,None,'audiences:'+seg))
    print(motion,seg,'non-US dropped',nonus); return rows
out['bo_leaders_prospects']=aud('audseg_0tk324ghMPTbzvR8pGK','bo_leaders_prospects.json','bo_leaders')
out['webinar_t1_dirplus']=aud('audseg_0tk4ivq7cX4pEjivYgy','webinar_t1_dirplus_prospects.json','webinar_sep2')
if '--with-t2' in sys.argv: out['webinar_t2_dirplus']=aud('audseg_0tk4ivr8riXSR3RA4Vh','webinar_t2_dirplus_prospects.json','webinar_sep2')
final={}; report={}
for k,rows in out.items():
    keep=[]; exc=collections.Counter(); seen=set(); dup=0; noid=0
    for r in rows:
        if not r['email'] and not r['linkedinUrl']: noid+=1; continue
        why=excluded(r['companyName'],r['companyDomain'],r['email'])
        if why: exc[r['companyName'] or why]+=1; continue
        key=(r['email'].lower() or None, r['linkedinUrl'].lower().rstrip('/') or None)
        if (key[0] and key[0] in seen) or (key[1] and key[1] in seen): dup+=1; continue
        seen|={x for x in key if x}; keep.append(r)
    final[k]=keep; report[k]={'candidates':len(rows),'keep':len(keep),'excluded':sum(exc.values()),'excluded_by':dict(exc.most_common(10)),'dup':dup,'no_email_or_li':noid,'with_email':sum(1 for r in keep if r['email']),'with_li':sum(1 for r in keep if r['linkedinUrl']),'accounts':len({r['parentAccount'] for r in keep})}
    print(f"{k}: candidates {len(rows)} -> keep {len(keep)} | excluded {sum(exc.values())} {dict(exc.most_common(6))} | dup {dup} | no email/li {noid} | with email {report[k]['with_email']} | accounts {report[k]['accounts']}")
json.dump(final,open(os.path.join(SP,'us_lists_candidates.json'),'w')); json.dump(report,open(os.path.join(HERE,'us_lists_report.json'),'w'),indent=1)
# contacts that already carry a motion (the two BO lists): first motion wins on push
keys=set()
for lid in CFG['existing_lists'].values():
    out_=subprocess.run(['curl','-s','-u',f':{KEY}',f'https://api.lemlist.com/api/contacts?listId={lid}&limit=500'],capture_output=True,text=True).stdout
    d_=json.loads(out_); d_=d_.get('data',d_) if isinstance(d_,dict) else d_
    for ct in d_:
        if ct.get('email'): keys.add(ct['email'].lower())
        if ct.get('linkedinUrl'): keys.add(ct['linkedinUrl'].lower().rstrip('/'))
json.dump(sorted(keys),open(os.path.join(SP,'has_motion_keys.json'),'w')); print('contacts already carrying a motion',len(keys))
