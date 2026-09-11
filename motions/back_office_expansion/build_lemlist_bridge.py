#!/usr/bin/env python3
"""Build (or rebuild) the Clay 'Lemlist bridge' workflow nodes from lemlist_bridge_config.json.
Usage: python3 build_lemlist_bridge.py <scratch_dir>. Deletes existing non-trigger nodes first."""
import json,subprocess,sys,base64,os,tempfile
SP=sys.argv[1]; HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
CLAY='/Users/dallasandrews/.claude/plugins/cache/clay-plugins/clay/2.13.0/bin/clay'
cfg=json.load(open(os.path.join(HERE,'lemlist_bridge_config.json'))); WF=cfg['workflow_id']; F=cfg['fields']
KEY=[l.split('=',1)[1].strip() for l in open('/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env') if l.startswith('LEMLIST_API_KEY=')][0]
AUTH='Basic '+base64.b64encode((':'+KEY).encode()).decode()
dl=json.load(open(os.path.join(ROOT,cfg['denylist_domains_source'])))
def clay(*a,inp=None):
    cmd=[CLAY,*a]
    if inp is not None:
        p=tempfile.NamedTemporaryFile('w',suffix='.json',delete=False,dir=SP); json.dump(inp,p); p.close(); cmd+=['--input',p.name]
    r=subprocess.run(cmd,capture_output=True,text=True); out=r.stdout or r.stderr
    try: return json.loads(out)
    except Exception: return {'raw':out}
g=clay('workflows','graph','get',WF); s=g.get('data',g).get('summary',g)
trig=[n for n in s['nodes'] if n['nodeType']=='trigger'][0]['id']
for n in s['nodes']:
    if n['nodeType']!='trigger': clay('workflows','nodes','delete',WF,n['id'])
print('trigger node',trig)
def create(spec):
    r=clay('workflows','nodes','create',WF,inp=spec); nid=r.get('nodeId')
    bad=[u for u in r.get('appliedUpdates',[]) if not u.get('success')]
    print(f"{spec['name']:34} -> {nid} {bad or ''} {r.get('error','') or (r.get('raw','')[:200] if not nid else '')}")
    return nid
ref=lambda node,path,desc='x': {"type":"string","description":desc,"sourceNodeId":node,"sourcePath":path}
lists=json.dumps(cfg['lists']); deny=json.dumps(sorted(set(dl.get('domains',[]))))
BASE=f'https://:{KEY}@api.lemlist.com'
code1=f'''import json
BASE = '{BASE}'
LISTS = json.loads('{lists}')
DENY = set(json.loads('{deny}'))
def handler(context):
    g = lambda k: (context.get_input(k) or "").strip()
    email = g("email").lower(); li = g("linkedin_url"); motion = g("motion").lower()
    dom = g("company_domain").lower() or (email.split("@")[1] if "@" in email else "")
    dom = dom.replace("https://","").replace("http://","").replace("www.","").split("/")[0]
    list_id = LISTS.get(motion, "")
    skip, reason = False, ""
    if not email and not li: skip, reason = True, "no_identifier"
    elif not list_id: skip, reason = True, "unknown_motion:" + motion
    elif dom and dom in DENY: skip, reason = True, "denylist_domain:" + dom
    elif dom == "intradiem.com": skip, reason = True, "internal"
    body = {{"firstName": g("first_name"), "lastName": g("last_name"), "jobTitle": g("title"), "motion": motion, "motionStatus": "staged"}}
    if email: body["email"] = email
    if li: body["linkedinUrl"] = li
    if dom: body["companyDomain"] = dom
    return {{"skip": skip, "reason": reason, "email": email, "linkedin_url": li, "motion": motion, "list_id": list_id, "list_url": BASE + "/api/contacts/lists/" + list_id + "/entities", "contacts_url": BASE + "/api/contacts", "contact_body": json.dumps(body), "company_domain": dom, "excluded_status": ("excluded:" + reason) if skip else ""}}
'''
outs=["skip","reason","email","linkedin_url","motion","list_id","list_url","contacts_url","contact_body","company_domain","excluded_status"]
n1=create({"nodeType":"code","name":"1. Normalize + exclusion check","description":"Builds the lemlist contact body, maps motion to a list id, re-checks the customer denylist domains and internal addresses. The queue segment already excludes SF Customer/Partner accounts. Motion-to-list map and denylist are baked from lemlist_bridge_config.json; rebuild with build_lemlist_bridge.py.","code":code1,
  "inputSchema":{"email":ref(trig,"$.fields.Email","email"),"first_name":ref(trig,"$.fields['First name']","first name"),"last_name":ref(trig,"$.fields['Last name']","last name"),"title":ref(trig,"$.fields.Title","title"),"linkedin_url":ref(trig,"$.fields['LinkedIn URL']","linkedin"),"motion":ref(trig,"$.fields['Lemlist Push Motion']","motion key")},
  "outputSchema":{k:{"type":"boolean" if k=="skip" else "string","description":k} for k in outs},"incomingEdges":[{"sourceNode":trig}]})
_sch=clay('workflows','nodes','get',WF,n1)['node']['inputSchema']; _sch['required']=['email','motion']; clay('workflows','nodes','update',WF,n1,inp={"inputSchema":_sch})
n2=create({"nodeType":"conditional","name":"1g. Excluded?","conditionalMode":"rules","rulesConditionalConfig":{"rules":[{"id":"skip","name":"skip","condition":{"type":"GroupOp","combinationMode":"And","items":[{"type":"BinOp","value":True,"dataPath":["skip"],"operator":"Equal"}]}}]},
  "inputSchema":{"skip":{"type":"boolean","description":"true when excluded","sourceNodeId":n1,"sourcePath":"$.skip"}},"incomingEdges":[{"sourceNode":n1}]})
def http(name,desc,url_ref,body_ref,inc):
    return create({"nodeType":"tool","name":name,"description":desc,"retryConfig":{"maxToolCallFailures":0},
      "tools":[{"toolType":"clay_action","actionKey":"http-api-v2","actionPackageId":"4299091f-3cd3-4d68-b198-0143575f471d","description":"HTTP API",
        "inputMappingConfig":{"method":{"type":"static","value":"POST"},"url":{"type":"reference","expression":"{{url}}"},"body":{"type":"reference","expression":"{{body}}"},"removeNull":{"type":"static","value":True},"returnResponseMetadata":{"type":"static","value":False}},
        "inputParameters":[{"name":"method","type":"string","required":False,"description":"HTTP method"},{"name":"url","type":"string","required":True,"description":"Endpoint"},{"name":"body","type":"string","required":False,"description":"JSON body"},{"name":"removeNull","type":"boolean","required":False,"description":"Remove empty values"},{"name":"returnResponseMetadata","type":"boolean","required":False,"description":"metadata"}]}],
      "inputSchema":{"url":url_ref,"body":body_ref},"incomingEdges":inc})
n3=http("2. Upsert lemlist contact","POST /api/contacts: lemlist upserts on email or LinkedIn URL, so a person already in the CRM is updated, never duplicated.",ref(n1,"$.contacts_url","contacts endpoint"),ref(n1,"$.contact_body","contact JSON"),[{"sourceNode":n2,"isDefaultRoute":True}])
n4=create({"nodeType":"code","name":"2b. Contact id","code":'''import json
def handler(context):
    r = context.get_input("result")
    if isinstance(r, str):
        try: r = json.loads(r)
        except Exception: r = {}
    d = (r or {}).get("data") or r or {}
    cid = d.get("_id") or ""
    return {"contact_id": cid, "ok": bool(cid), "status": "pushed" if cid else "error:no_contact_id", "list_body": json.dumps({"action": "add", "contactIds": [cid]}) if cid else ""}
''',"inputSchema":{"result":{"type":"string","description":"lemlist response","sourceNodeId":n3,"sourcePath":"$.result"}},
  "outputSchema":{"contact_id":{"type":"string","description":"ctc id"},"ok":{"type":"boolean","description":"had id"},"status":{"type":"string","description":"pushed or error"},"list_body":{"type":"string","description":"add body"}},"incomingEdges":[{"sourceNode":n3}]})
n5=http("3. Add to the motion's list","POST /api/contacts/lists/{listId}/entities with action add; contacts already in the list are skipped by lemlist.",ref(n1,"$.list_url","list entities endpoint"),ref(n4,"$.list_body","add body"),[{"sourceNode":n4}])
def wb(name,desc,status_ref,inc,extra):
    fields=[F['status']]+([F['contact_id']] if extra else [])
    m={"entityType":{"type":"static","value":"CONTACT"},"lookupFields|email":{"type":"reference","expression":"{{email}}"},"lookupFields|selectedLookupFields":{"type":"static","value":["email"]},"recordFields|removeNullValues":{"type":"static","value":True},"recordFields|selectedRecordFields":{"type":"static","value":fields},"recordFields|"+F['status']:{"type":"reference","expression":"{{status}}"}}
    props={"email":ref(n1,"$.email","email"),"status":status_ref}
    if extra:
        m["recordFields|"+F['contact_id']]={"type":"reference","expression":"{{contact_id}}"}
        props["contact_id"]=ref(n4,"$.contact_id","lemlist contact id")
    return create({"nodeType":"tool","name":name,"description":desc,"retryConfig":{"maxToolCallFailures":0},"tools":[{"toolType":"clay_action","actionKey":"upsert-audiences-record","actionPackageId":"b1ab3d5d-b0db-4b30-9251-3f32d8b103c1","description":"Upsert Audiences Record","inputMappingConfig":m,"inputParameters":[{"name":"entityType","type":"string","required":True,"description":"entity"},{"name":"lookupFields","type":"string","required":False,"description":" "},{"name":"recordFields","type":"string","required":False,"description":" "}]}],
        "inputSchema":props,"incomingEdges":inc})
n6=wb("4. Write back: pushed","Stamps Lemlist Status, the lemlist contact id and the push time on the Audiences person, which removes them from the queue segment.",ref(n4,"$.status","status"),[{"sourceNode":n5}],True)
n7=wb("EXIT: excluded","Stamps Lemlist Status = excluded:<reason> so the person leaves the queue and the reason is visible in Audiences.",ref(n1,"$.excluded_status","excluded status"),[{"sourceNode":n2,"ruleId":"skip","ruleName":"skip"}],False)
json.dump({"trigger_node":trig,"n1":n1,"n2":n2,"n3":n3,"n4":n4,"n5":n5,"n6":n6,"n7":n7},open(os.path.join(SP,'bridge_nodes.json'),'w'))
v=clay('workflows','graph','validate',WF); print('VALIDATE',json.dumps(v)[:1500])
