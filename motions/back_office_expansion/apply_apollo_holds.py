#!/usr/bin/env python3
"""After load_customer_wave.py's dry-run merge, apply the Apollo verdicts that the merge cannot express:
rows Apollo places outside the US (foreign_location) or at another employer (moved) become holds with the reason in
email_note; rows with no Apollo match and only a Jul 26 address lose the address (no second source) and become needs_email.
Usage: apply_apollo_holds.py <scratch>  (edits customer_lane_staging/wave1/*_remainder.csv in place)"""
import csv,glob,json,os,re,sys
HERE=os.path.dirname(os.path.abspath(__file__)); SP=sys.argv[1]
ap=json.load(open(os.path.join(SP,'remainder_apollo_results.json')))
def slug(u): return re.sub(r'/+$','',(u or '').lower().split('linkedin.com/in/')[-1]).strip('/')
n={'hold':0,'needs_email':0,'valid':0}
for f in glob.glob(os.path.join(HERE,'customer_lane_staging','wave1','*_remainder.csv')):
    rows=list(csv.DictReader(open(f))); changed=False
    for r in rows:
        a=ap.get(slug(r['linkedinUrl']))
        if not a: continue
        if a['status'] in ('foreign_location','moved'):
            r['load_status']='hold'; r['email_note']=(r['email_note']+'; '+a['note']).strip('; '); n['hold']+=1; changed=True
        elif a['status']=='valid': n['valid']+=1
        elif r['email'] and r['load_status']!='hold':
            r['email']=''; r['load_status']='needs_email'; r['email_note']=(r['email_note']+'; jul26 address dropped, no second source (apollo no match)').strip('; '); n['needs_email']+=1; changed=True
    if changed:
        w=csv.DictWriter(open(f,'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('apollo verdicts applied',n)
