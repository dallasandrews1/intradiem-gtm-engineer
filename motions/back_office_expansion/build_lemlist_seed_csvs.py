#!/usr/bin/env python3
"""Rebuild the two BO seed CSVs that seed_lemlist_lists.py stamps onto lemlist Contacts, from the live state:
motion_status = in_sequence (lead is in the motion's campaign), held (load_status hold), needs_email, or staged.
Sources: BO_NetNew_Leads_Staged_Sep2.csv + the net-new campaign export; the four customer staged CSVs +
customer_lane_staging/wave1/*.csv + the four vertical campaign exports. Run this, then `seed_lemlist_lists.py`."""
import csv,json,os,re,glob,subprocess,collections
HERE=os.path.dirname(os.path.abspath(__file__))
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json')))
def curl(path):
    out=subprocess.run(['curl','-s','-u',f':{KEY}','https://api.lemlist.com'+path],capture_output=True,text=True).stdout
    try: return json.loads(out)
    except Exception: return []
def slug(u): return re.sub(r'/+$','',(u or '').lower().split('linkedin.com/in/')[-1]).strip('/')
def in_campaign(cids):
    keys=set()
    for c in cids:
        for l in curl(f'/api/campaigns/{c}/export/leads?state=all&format=json'):
            if l.get('email'): keys.add(l['email'].lower())
            if l.get('linkedinUrl'): keys.add(slug(l['linkedinUrl']))
    return keys
cols=['email','linkedinUrl','firstName','lastName','jobTitle','companyName','companyDomain','motion','motion_status','parent_account','wave']
# net-new
live=in_campaign(['cam_DNErdZPANvC2sqRCK']); out=[]; st=collections.Counter()
for r in csv.DictReader(open(os.path.join(HERE,'BO_NetNew_Leads_Staged_Sep2.csv'))):
    s='in_sequence' if (r['email'].lower() in live or slug(r['linkedinUrl']) in live) else {'hold':'held','needs_email':'needs_email'}.get(r['load_status'],'staged')
    st[s]+=1
    out.append({'email':r['email'],'linkedinUrl':r['linkedinUrl'],'firstName':r['firstName'],'lastName':r['lastName'],'jobTitle':r['jobTitle'],'companyName':r['companyName'],'companyDomain':r['companyDomain'],'motion':'bo_netnew','motion_status':s,'parent_account':r['parent_account'],'wave':r['wave']})
w=csv.DictWriter(open(os.path.join(HERE,'lemlist_seed_bo_netnew.csv'),'w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(out)
print('bo_netnew',len(out),dict(st))
# customer lane: wave1 files carry the checked state; the staged CSVs carry the rest
live=in_campaign(list(cfg['campaign_ids'].values())); out=[]; st=collections.Counter(); seen=set()
for f in sorted(glob.glob(os.path.join(HERE,'customer_lane_staging','wave1','*.csv'))):
    for r in csv.DictReader(open(f)):
        k=slug(r['linkedinUrl']) or (r['firstName']+' '+r['lastName']).lower(); seen.add(k)
        s='in_sequence' if (r['email'].lower() in live or slug(r['linkedinUrl']) in live) else {'hold':'held','needs_email':'needs_email'}.get(r['load_status'],'staged')
        st[s]+=1
        out.append({'email':r['email'],'linkedinUrl':r['linkedinUrl'],'firstName':r['firstName'],'lastName':r['lastName'],'jobTitle':r['jobTitle'],'companyName':r['companyName'],'companyDomain':r['companyDomain'],'motion':'bo_customer','motion_status':s,'parent_account':r['parent_account'],'wave':'1'})
for v in ['hc','fs','ins','bpo','no_campaign']:
    for r in csv.DictReader(open(os.path.join(HERE,'customer_lane_staging',f'BO_Customer_{v}_Staged_Sep2.csv'))):
        k=slug(r['linkedinUrl']) or r['full_name'].lower()
        if k in seen: continue
        seen.add(k); s='in_sequence' if (r['email'].lower() in live or slug(r['linkedinUrl']) in live) else 'staged'; st[s]+=1
        out.append({'email':r['email'],'linkedinUrl':r['linkedinUrl'],'firstName':r['firstName'],'lastName':' '.join(re.sub(r',.*$','',r['full_name']).split()[1:]),'jobTitle':r['title'],'companyName':r['account'],'companyDomain':'','motion':'bo_customer','motion_status':s,'parent_account':cfg['parent_account'].get(r['account'],r['account']),'wave':''})
w=csv.DictWriter(open(os.path.join(HERE,'customer_lane_staging','lemlist_seed_bo_customer.csv'),'w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(out)
print('bo_customer',len(out),dict(st))
