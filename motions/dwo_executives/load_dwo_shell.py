#!/usr/bin/env python3
"""Load the DWO Executives shell (cam_SiD4KmWcRuhiF6uhL) from the reconciled wave 1 pool. Dry-run by default; --go loads
leads (never launches, never changes the campaign state). Rules from DWO_Exec_Sequence_Sep4.md, Load rules section:
title filter, account/company agreement, verified email only, skip anyone already a lead in any campaign, skip any contact
whose lemlist motion is not dwo_exec, skip disputed emails, new-in-role (Rule A) opener first, else the vertical Rule B
opener, workTeams and peak per vertical (CAO titles get shared-services teams), one angle per account (family swap so no
two people at one account share an angle). Usage: load_dwo_shell.py <scratch> [--go]
Inputs in <scratch>: dwo_wave1_reconciled.json, lemlist_campaign_leads.json, dwo_list_contact_details.json (optional)."""
import json,os,sys,re,csv,subprocess,time,collections,datetime,hashlib
SP=sys.argv[1]; GO='--go' in sys.argv; HERE=os.path.dirname(os.path.abspath(__file__))
CAMP='cam_SiD4KmWcRuhiF6uhL'; TODAY=datetime.date(2026,9,4)
COHORT='GTMENG-DWO1-2026-09'; SF_CAMPAIGN='GTM Eng - DWO Executives - Wave 1'; HOLDOUT_SHARE=0.5   # Lane B pilot: same holdout rule as automation/cohort_cutter.py (sha1 parity by domain)
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
def curl(m,p,b=None):
    a=['curl','-s','-u',f':{KEY}','-X',m,'https://api.lemlist.com'+p,'-H','Content-Type: application/json']
    if b is not None: a+=['-d',json.dumps(b)]
    for i in range(3):
        out=subprocess.run(a,capture_output=True,text=True).stdout
        try: return json.loads(out)
        except Exception: time.sleep(2)
    return {'raw':out[:200]}
DROP=re.compile(r'chief of staff|deputy|assistant|associate chief|specialist|analyst|office of|interim|former|retired|advisor|adviser|consultant|board member|chief nursing|chief medical',re.I)
UNIT=re.compile(r'hospital|medical group|medical center|physician|clinic|post acute|providers|health system region|market\b',re.I)   # provider-system unit COOs: loaded, flagged for Nate
DISPUTED={'mm@fidelity.com'}
WORK={'Healthcare':'service and claims teams','Insurance':'claims and service teams','Financial Services':'servicing and operations teams','Utilities':'billing, credit and service teams','Retail':'customer care and fulfilment support teams','Telecom':'care and back-office teams'}
CAO_WORK='shared services and back-office teams'
PEAK={'Healthcare':'open enrollment','Insurance':'the Q4 claims and renewal peak','Financial Services':'year-end close','Utilities':'the winter season','Retail':'holiday peak','Telecom':'device season'}
RULEB={'Healthcare':"Open enrollment opens October 15, and the peak lands on {co}'s service and claims teams the way it does every year: over on quiet days, behind on busy ones.",
 'Insurance':"Q4 puts claims, renewals and year-end close on the same operations teams at {co}, and the summer staffing plan meets the fall.",
 'Financial Services':"Year-end close and the January statement cycle put {co}'s servicing teams through the same peak every year, staffed to the average day.",
 'Utilities':"Winter season starts in a few weeks, and {co}'s billing, credit and service teams will staff for the storm days and pay for the quiet ones.",
 'Retail':"Holiday peak staffing at {co} gets locked in September, and then the volume arrives on its own schedule, not the plan's.",
 'Telecom':"Device season and the fall churn push hit {co}'s care and back-office teams at once, staffed for the average hour."}
NAME_MAP={'American International Group (AIG)':'AIG','Bon Secours Mercy Health':'Bon Secours Mercy','Navy Federal Credit Union':'Navy Federal','Henry Ford Health System':'Henry Ford Health','Vanderbilt University Medical System':'Vanderbilt Medical','WAL-MART STORES (U K)':'Walmart','City of Los Angeles - Los Angeles Department of Water and Power':'LADWP','Indiana University Health (Clarian)':'IU Health','Rochester Regional Health':'Rochester Regional','SSM Health Care Corporation':'SSM Health','Blue Cross Blue Shield of Michigan':'BCBS Michigan','Blue Cross and Blue Shield of North Carolina':'Blue Cross NC','Blue Cross Blue Shield of Massachusetts':'BCBS Massachusetts','Highmark Blue Cross Blue Shield':'Highmark','Memorial Hermann Health System':'Memorial Hermann',"St. Jude Children's Research Hospital":'St. Jude','The Penn Mutual Life Insurance':'Penn Mutual','Toyota Motor Sales, U.S.A.':'Toyota','BT Business and Public Sector':'BT','Blue Cross Blue Shield Arizona':'BCBS Arizona','Advocate Aurora Health':'Advocate Aurora','American Electric Power':'AEP','American Water Works':'American Water','Beacon Health Options':'Beacon Health','Carnival Cruise Line':'Carnival','DaVita Kidney Care':'DaVita','State Employees Credit Union':'SECU','BlueCross BlueShield South Carolina':'BlueCross SC','Old Republic International':'Old Republic','Santander Bank (US)':'Santander','Pilot Travel Centers':'Pilot','Plymouth Rock Assurance':'Plymouth Rock','Baylor Scott & White Health':'Baylor Scott & White'}
ANGLE={
 'core':{'idea':"There's a cost in there you pay twice: idle minutes inside the shift, and overtime after it to clear what didn't get done.",
         'proof':"That's what Intradiem does. It sits on top of the WFM and case systems your {wt} already run and moves work, training and breaks into the idle windows as they open, contact center and back office. Humana has it on the record: two hours back per agent per month, and 7X five years in.",
         'ask':"Worth a conversation on how much of {co}'s overtime is idle time in disguise?",
         'askA':"Worth a conversation on how much of {co}'s overtime is idle time in disguise?"},
 'customer':{'idea':"In service operations the trade usually gets framed as cost or experience. The idle minutes inside the shift are the one lever that moves both: coaching and training happen in the quiet windows instead of never, and the busy windows get the people back.",
         'proof':"That's what Intradiem does. It sits on top of the WFM and case systems your {wt} already run, spots idle windows as they open, and moves work, coaching and breaks into them, contact center and back office. Humana has it on the record: two hours of capacity back per agent per month, and handle time down 45 seconds.",
         'ask':"Worth a conversation on where {co}'s coaching hours actually come from today?",
         'askA':"Worth a conversation on where {co}'s coaching hours actually come from today?"},
 'transformation':{'idea':"Most of a change portfolio is modelled benefit. Intraday capacity is the known number: it's already on the payroll, and it runs as rules on top of the systems you already govern, nothing new to stand up.",
         'proof':"That's what Intradiem does. It sits on top of the WFM and case systems your {wt} already run, spots idle windows as they open, and moves work, training and breaks into them, contact center and back office. Humana has it on the record: the return landed inside the first year, and 7X five years in.",
         'ask':"Worth a conversation on whether that belongs in {co}'s roadmap as the certain line?",
         'askA':"Worth a conversation on whether that belongs in {co}'s roadmap as the certain line?"}}
def role_word(title):
    t=(title or '').lower()
    if re.search(r'chief operating|\bcoo\b',t): return 'COO seat'
    if re.search(r'chief administrative|\bcao\b',t): return 'CAO seat'
    if re.search(r'chief customer|\bcco\b',t): return 'Chief Customer Officer seat'
    if re.search(r'chief experience|\bcxo\b',t): return 'Chief Experience Officer seat'
    if re.search(r'chief claims',t): return 'Chief Claims Officer seat'
    if re.search(r'chief service',t): return 'Chief Service Officer seat'
    if re.search(r'chief transformation',t): return 'Chief Transformation Officer seat'
    if re.search(r'chief financial|\bcfo\b',t): return 'CFO seat'
    if re.search(r'operations',t): return 'operations seat'
    return 'seat'
def months_in_role(sd):
    m=re.match(r'(\d{4})-(\d{2})',sd or '')
    if not m: return None
    y,mo=int(m.group(1)),int(m.group(2)); return (TODAY.year-y)*12+(TODAY.month-mo)
def norm(s): return re.sub(r'[^a-z0-9 ]','',(s or '').lower())
STOP={'the','inc','corporation','corp','company','co','llc','group','holdings','ltd','plc','incorporated','of','and','health','financial','services','insurance','bank'}
def toks(s): return {t for t in norm(s).split() if t not in STOP and len(t)>1}
def agree(account,company):
    a,c=toks(account),toks(company)
    if not a or not c: return True
    if a&c: return True
    # abbreviation match (e.g. JPMorgan Chase vs JPMorganChase)
    return norm(account).replace(' ','')[:6] in norm(company).replace(' ','') or norm(company).replace(' ','')[:6] in norm(account).replace(' ','')
def poss(co): return co+("'" if co.endswith('s') else "'s")
def short_co(account):
    if account in NAME_MAP: return NAME_MAP[account]
    account=re.sub(r'\s*\([^)]*\)\s*','',account or '').strip()
    if ' - ' in account and len(account.split())>4: account=account.split(' - ')[0].strip()
    s=re.sub(r',?\s*(inc\.?|corporation|corp\.?|company|co\.?|llc|group|holdings|ltd\.?|plc|incorporated)\s*$','',account or '',flags=re.I).strip()
    return s or account
rec=json.load(open(f'{SP}/dwo_wave1_reconciled.json'))
li=json.load(open(f'{SP}/lemlist_campaign_leads.json')); lead_index=li['lead_index']
dp=f'{SP}/dwo_list_contact_details.json'; details=json.load(open(dp)) if os.path.exists(dp) else {}
by_url={}; by_email={}
for cid,d in details.items():
    f=d.get('fields') or {}; u=(d.get('linkedinUrl') or '').lower().rstrip('/')
    if u: by_url[u]=d
    if f.get('email'): by_email[f['email'].lower()]=d
skips=collections.Counter(); plan=[]; skipped=[]
for r in rec:
    reason=None; e=(r['email'] or '').lower(); u=(r['linkedinUrl'] or '').lower().rstrip('/')
    if r['result']=='held': reason='held (moved company)'
    elif r['result']!='found' or not e: reason='no verified email (LinkedIn-first variant later)'
    elif e in DISPUTED: reason='disputed email'
    elif DROP.search(r['title'] or ''): reason='title filter: '+DROP.search(r['title']).group(0).lower()
    elif not agree(r['account'],r['company']): reason='account/company disagree'
    elif e in lead_index or (u and u in lead_index): reason='already a lead in: '+', '.join(sorted(set(lead_index.get(e,[])+lead_index.get(u,[]))))
    else:
        d=by_email.get(e) or by_url.get(u)
        if details and d:
            f=d.get('fields') or {}
            if f.get('motion') and f['motion']!='dwo_exec': reason='contact motion is '+f['motion']
            elif d.get('campaigns'): reason='contact already in campaign(s) per lemlist record'
    if reason: skips[reason.split(':')[0]]+=1; skipped.append({**{k:r[k] for k in ('name','title','account','vertical','email','linkedinUrl')},'reason':reason}); continue
    plan.append(r)
# per-account angle: family swap so no two people at one account share an angle
FAM_ORDER=['COO/ops','CAO','Customer/experience/service','Transformation','Claims']
def family_variant(fam):
    if fam in ('COO/ops','CAO','Claims'): return 'core'
    if fam=='Customer/experience/service': return 'customer'
    return 'transformation'
by_acct=collections.defaultdict(list)
for r in plan: by_acct[r['account']].append(r)
swaps=0
for acct,rows in by_acct.items():
    rows.sort(key=lambda x:(months_in_role(x.get('start_date')) if months_in_role(x.get('start_date')) is not None else 999, x['name']))
    used=set()
    for r in rows:
        v=family_variant(r['family'])
        if v in used:
            for alt in ('customer','transformation','core'):
                if alt not in used: v=alt; swaps+=1; break
        used.add(v); r['e1_variant']=v
for r in plan:
    co=short_co(r['account']); mir=months_in_role(r.get('start_date')); isCAO=bool(re.search(r'chief administrative|\bcao\b',r['title'] or '',re.I))
    if mir is not None and 0<=mir<=6:
        n={0:'A few weeks',1:'One month',2:'Two months',3:'Three months',4:'Four months',5:'Five months',6:'Six months'}[mir]
        r['opener']=f"{n} into the {role_word(r['title'])} at {co}, the listening tour is over and the operating agenda is getting written."; r['opener_rule']='A'
    else:
        r['opener']=RULEB[r['vertical']].format(co=co).replace(co+"'s",poss(co)); r['opener_rule']='B'
    r['workTeams']=CAO_WORK if isCAO else WORK[r['vertical']]; r['peak']=PEAK[r['vertical']]; r['companyName']=co
    a=ANGLE[r['e1_variant']]; r['angleIdea']=a['idea']; r['angleProof']=a['proof'].format(wt=r['workTeams']); r['angleAsk']=(a['askA'] if r['opener_rule']=='A' else a['ask']).format(co=co).replace(co+"'s",poss(co))
for r in plan:
    r['cohortId']=COHORT; r['cohortArm']='test' if int(hashlib.sha1(r['domain'].encode()).hexdigest(),16)%100<HOLDOUT_SHARE*100 else 'holdout'
n=len(plan); acc=len(by_acct)
arms=collections.Counter(r['cohortArm'] for r in plan); arm_acc={a:len({r['domain'] for r in plan if r['cohortArm']==a}) for a in ('test','holdout')}
print('Lane B arms: test (ads + sequence)',arms['test'],'people at',arm_acc['test'],'accounts | holdout (sequence only)',arms['holdout'],'people at',arm_acc['holdout'],'accounts')
ads=[{'email':r['email'],'first_name':r['firstName'],'last_name':r['lastName'],'company':r['companyName'],'title':r['title'],'country':'United States'} for r in plan if r['cohortArm']=='test']
w=csv.DictWriter(open(os.path.join(HERE,f'{COHORT}_ads_linkedin.csv'),'w',newline=''),fieldnames=['email','first_name','last_name','company','title','country']); w.writeheader(); w.writerows(ads)
print(f'wave 1 reconciled {len(rec)} | load plan {n} at {acc} accounts | skipped {len(rec)-n}')
for k,v in skips.most_common(): print(f'  skip {v:4}  {k}')
print('opener rule',dict(collections.Counter(r['opener_rule'] for r in plan)))
print('E1 variant',dict(collections.Counter(r['e1_variant'] for r in plan)),'| swaps',swaps)
print('vertical',dict(collections.Counter(r['vertical'] for r in plan)))
print('family',dict(collections.Counter(r['family'] for r in plan)))
print('per-account max',max(len(v) for v in by_acct.values()),'| accounts with 2+',sum(1 for v in by_acct.values() if len(v)>1))
print('with LinkedIn URL',sum(1 for r in plan if r['linkedinUrl']),'| without',sum(1 for r in plan if not r['linkedinUrl']))
for r in plan: r['flag']='provider unit COO' if (r['vertical']=='Healthcare' and UNIT.search(r['title'] or '')) else ''
print('flagged provider-unit titles (loaded, Nate decides)',sum(1 for r in plan if r['flag']))
cols=['name','firstName','lastName','title','account','companyName','domain','vertical','family','tier','start_date','opener_rule','e1_variant','email','linkedinUrl','opener','workTeams','peak','angleIdea','angleProof','angleAsk','cohortId','cohortArm','flag']
w=csv.DictWriter(open(os.path.join(HERE,'DWO_Shell_Load_Plan_Sep4.csv'),'w',newline=''),fieldnames=cols,extrasaction='ignore'); w.writeheader(); w.writerows(plan)
w=csv.DictWriter(open(os.path.join(HERE,'DWO_Shell_Skipped_Sep4.csv'),'w',newline=''),fieldnames=['name','title','account','vertical','email','linkedinUrl','reason']); w.writeheader(); w.writerows(skipped)
json.dump({'plan':plan,'skipped':skipped,'skips':dict(skips),'swaps':swaps,'details_loaded':bool(details)},open(f'{SP}/dwo_shell_plan.json','w'),indent=0)
if not GO: print('DRY RUN, nothing loaded'); sys.exit(0)
have={(l.get('email') or '').lower() for l in (curl('GET',f'/api/campaigns/{CAMP}/export/leads?state=all&format=json') or []) if isinstance(l,dict)}
ok=0; err=0
for r in plan:
    if r['email'].lower() in have: continue
    body={'firstName':r['firstName'] or '','lastName':r['lastName'] or '','companyName':r['companyName'],'companyDomain':r['domain'],'jobTitle':r['title'] or '','linkedinUrl':r['linkedinUrl'] or '','opener':r['opener'],'workTeams':r['workTeams'],'peak':r['peak'],'angleIdea':r['angleIdea'],'angleProof':r['angleProof'],'angleAsk':r['angleAsk'],'cohortId':r['cohortId'],'cohortArm':r['cohortArm'],'sfCampaign':SF_CAMPAIGN,'e1Variant':r['e1_variant'],'motion':'dwo_exec','motionStatus':'loaded','parentAccount':r['account']}
    res=curl('POST',f'/api/campaigns/{CAMP}/leads/{r["email"]}?deduplicate=true',body)
    if res.get('_id'): ok+=1
    else: err+=1; print('ERR',r['email'],str(res)[:150])
print('loaded',ok,'errors',err,'already there',len(have))
