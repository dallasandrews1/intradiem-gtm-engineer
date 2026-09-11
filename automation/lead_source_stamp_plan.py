#!/usr/bin/env python3
"""Salesforce stamp plan: every contact GTM Engineering created, with the values Sales Ops applies when the record lands in
Salesforce (Lead Source = GTM Engineering, Lead Origin = GTM Engineering, Primary Campaign Source = one SF campaign per
lemlist campaign). Reads live lemlist campaign leads (read-only) plus the DWO load plan CSV. Writes one CSV per campaign
and a summary. No Salesforce write exists in this repo; the plan is the handoff to Sierra/Genna until the picklist value ships.
Usage: lead_source_stamp_plan.py [--out <dir>]"""
import csv,json,os,sys,subprocess,time,collections
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=sys.argv[sys.argv.index('--out')+1] if '--out' in sys.argv else os.path.join(ROOT,'motions','pipeline_council','stamp_plans')
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
def g(p):
    for i in range(3):
        out=subprocess.run(['curl','-s','-u',f':{KEY}','https://api.lemlist.com'+p],capture_output=True,text=True).stdout
        try: return json.loads(out)
        except Exception: time.sleep(2)
    return []
CAMPS={'cam_sh3JCJoxtEHyjGrsw':'GTM Eng - Star Ratings - Resurrection','cam_viEbB6HkYsCPtxKbi':'GTM Eng - Star Ratings - Quality','cam_2gy9hmEvMjYEuPZ8A':'GTM Eng - Star Ratings - Finance',
 'cam_yWefPqaDhNNv4RyQK':'GTM Eng - Blitz - Citizens','cam_fYp7Nh9wB72gfMke6':'GTM Eng - Blitz - The Hartford',
 'cam_N92Tgg29ncHWnYAD9':'GTM Eng - Back Office Expansion - Healthcare Payer','cam_x8ehMHnWSjBr2CLQe':'GTM Eng - Back Office Expansion - Financial Services','cam_HCu4jiFB8oinz2s3F':'GTM Eng - Back Office Expansion - Insurance','cam_Fy287YF9X5fjPYBSo':'GTM Eng - Back Office Expansion - BPO',
 'cam_DNErdZPANvC2sqRCK':'GTM Eng - Back Office - Net New','cam_SiD4KmWcRuhiF6uhL':'GTM Eng - DWO Executives - Wave 1'}
COLS=['Email','First Name','Last Name','Title','Company','Company Domain','LinkedIn URL','Lead Source','Lead Origin','Primary Campaign Source','Lemlist Campaign','Cohort','Cohort Arm']
os.makedirs(OUT,exist_ok=True); summary=[]
for cid,sf in CAMPS.items():
    leads=g(f'/api/campaigns/{cid}/export/leads?state=all&format=json'); leads=leads if isinstance(leads,list) else []
    rows=[{'Email':l.get('email') or '','First Name':l.get('firstName') or '','Last Name':l.get('lastName') or '','Title':l.get('jobTitle') or '','Company':l.get('companyName') or '','Company Domain':l.get('companyDomain') or '','LinkedIn URL':l.get('linkedinUrl') or '','Lead Source':'GTM Engineering','Lead Origin':'GTM Engineering','Primary Campaign Source':sf,'Lemlist Campaign':cid,'Cohort':l.get('cohortId') or '','Cohort Arm':l.get('cohortArm') or ''} for l in leads]
    if cid=='cam_SiD4KmWcRuhiF6uhL' and not rows:
        pp=os.path.join(ROOT,'motions','dwo_executives','DWO_Shell_Load_Plan_Sep4.csv')
        if os.path.exists(pp):
            rows=[{'Email':r['email'],'First Name':r['firstName'],'Last Name':r['lastName'],'Title':r['title'],'Company':r['companyName'],'Company Domain':r['domain'],'LinkedIn URL':r['linkedinUrl'],'Lead Source':'GTM Engineering','Lead Origin':'GTM Engineering','Primary Campaign Source':sf,'Lemlist Campaign':cid+' (load plan, not yet loaded)','Cohort':r.get('cohortId',''),'Cohort Arm':r.get('cohortArm','')} for r in csv.DictReader(open(pp))]
    fn=os.path.join(OUT,sf.replace(' ','_').replace('/','-')+'.csv')
    w=csv.DictWriter(open(fn,'w',newline=''),fieldnames=COLS); w.writeheader(); w.writerows(rows); summary.append((sf,cid,len(rows)))
tot=0
for sf,cid,n in summary: print(f'{n:5}  {sf}  ({cid})'); tot+=n
print('total',tot,'->',OUT)
