# Builds the Nate campaign structure review page (Sep 4 2026)
import html, os
S=os.path.dirname(os.path.abspath(__file__))
LOGO=open(S+'/logo.svg').read()
OUT=os.path.expanduser('~/Desktop/Intradiem Deliverables/Nate_Campaign_Structure_Review_Sep4.html')

P,F,H='pass','fix','hold'
LINES=['Channels','Branching','Testing','Timing','Variables','Replies','Measurement','Deliverability','Gates']

# --- campaign data -------------------------------------------------------
C=[]
def seq(*rows): return list(rows)
# row = (day, channel, text, depth, kind) kind: '', 'branch', 'new', 'skip'
C.append(dict(
 key='res', name='Stars - Resurrection', id='cam_sh3JCJoxtEHyjGrsw', leads=43, status='paused',
 q='Re-approach of the July Stars pool. Pipeline: second-look meetings from plans that ignored wave 1 before the fall scoring peak.',
 costing='The "Opened email" branch can never fire because open tracking is off, so nobody gets the "one more" email that names the re-entry condition. Two stray API-test steps sit in the live tree and create empty tasks for Nate.',
 marks={'Channels':P,'Branching':F,'Testing':H,'Timing':P,'Variables':P,'Replies':P,'Measurement':P,'Deliverability':P,'Gates':P},
 now=seq((0,'LinkedIn','Profile visit',0,''),(1,'LinkedIn','Connect, blank note, Nate approves',0,''),(3,'Condition','Accepted the connect? (within 2 days)',0,''),
   (3,'LinkedIn','Message after connect',1,'branch'),(4,'Call','Call, voicemail if no answer',1,''),(7,'Email','"one more before the window closes"',1,''),(7,'Task','STRAY step from the Aug 31 API test',1,'skip'),
   (3,'Call','Call, then the email goes out',1,'branch2'),(3,'Email','"just tried you" (A/B winner A already picked)',1,''),(6,'Condition','Opened the email? (open tracking is OFF, so never true)',1,'bad'),(7,'Email','"one more" (unreachable)',2,'branch'),(7,'Email','"closing the loop" (everyone lands here)',2,'branch2'),
   (3,'Voice note','STRAY manual voice note, empty, fires for every lead',0,'skip')),
 gaps=['Branching: the open condition is dead with tracking off. Swap the condition to one that is always true so every no-connect lead gets the stronger breakup, and the "closing the loop" step goes quiet.',
       'Two stray steps (root voice note, Yes-branch task) create empty tasks. The API refuses deletion once leads are reviewed. Skip both for all leads in the UI.',
       'Testing: the "just tried you" A/B already has a winner picked (A), which locks A/B for this campaign. No further test possible here.',
       'Voice note where the persona warrants it: quality and ops directors. Manual voice note after the connect message, in the Yes branch. The API refuses voice notes inside branches, so this is a UI add.'],
 then=seq((0,'LinkedIn','Profile visit',0,''),(1,'LinkedIn','Connect, blank note, Nate approves',0,''),(3,'Condition','Accepted the connect? (within 2 days)',0,''),
   (3,'LinkedIn','Message after connect',1,'branch'),(4,'Voice note','Manual voice note, Nate records (UI add)',1,'new'),(5,'Call','Call, voicemail if no answer',1,''),(8,'Email','"one more before the window closes"',1,''),
   (3,'Call','Call, then the email goes out',1,'branch2'),(3,'Email','"just tried you"',1,''),(6,'Condition','Has email address (always true) replaces "opened"',1,'new'),(7,'Email','"one more" for everyone in this branch',2,'branch')),
 api=['update_sequence_step on stp_Xwt4NgD3FFSFTvvbY: conditionKey hasEmailAddress, delayType within, delay 0 (then the "one more" email keeps its +1 day)','Shift the Yes-branch call (stp_kBkdqpRK7voEnbLup) delay from 1 to 2 after the voice note is added'],
 ui=['Skip stp_6eBfPTm3Y92XNT363 (root voice note) and stp_MPXXucbkXwjkiiJSP (Yes-branch task) for all leads','Add a manual Voice message step in the Accepted branch after the LinkedIn message'],
 locked='Every email, LinkedIn message and call script from the Sep 3 rewrite. Variant B of "just tried you" is archived by the winner pick.'))

stars_common_gaps=['Channels: complete. Email, visit, connect, message, manual voice note, two calls in the connect path, voicemail plus two calls in the phone path. Doctrine says these personas answer.',
 'Voice note step has an empty body. Nate\'s task would show no script, even though every lead carries a voice_script variable. Put {{voice_script}} in the step body the way Citizens does.',
 'Branching: no "has LinkedIn URL" branch is needed, every lead carries a URL (Aug 31 sweep). No click branch: click tracking is off on purpose (see Deliverability), so calls fire on the accepted connect and on the phone branch instead.',
 'Testing: Email 1 A/B is live with the doctrine hypothesis (benchmark question against offer note). Needs a read date. With under 30 leads there is no statistical read, so the read is on reply count only, 14 business days after start.',
 'Connect-note A/B waived: the sample is too small to learn from and Nate prefers a blank connect.']
stars_now=lambda subj: seq((0,'Email','Email 1 A/B: '+subj,0,''),(0,'LinkedIn','Profile visit',0,''),(1,'LinkedIn','Connect, blank note, Nate approves',0,''),(3,'Condition','Accepted the connect? (within 2 days)',0,''),
   (3,'LinkedIn','Message after connect',1,'branch'),(4,'Call','Call 1, no voicemail',1,''),(5,'Voice note','Manual voice note (body EMPTY)',1,'bad'),(6,'Call','Call 2, leave voicemail',1,''),(8,'Email','Email 2 in thread',1,''),(10,'Email','Email 3 breakup',1,''),
   (3,'Condition','Has a phone number?',1,'branch2'),(3,'Call','Voicemail',2,'branch'),(4,'Call','Call, day after voicemail',2,''),(6,'Email','Email 2 in thread',2,''),(8,'Call','Final call',2,''),(9,'Email','Email 3 breakup',2,''),
   (4,'LinkedIn','Like last post + follow',2,'branch2'),(5,'Email','Email 2 in thread',2,''),(9,'Email','Email 3 breakup',2,''))
stars_then=lambda subj: seq((0,'Email','Email 1 A/B: '+subj,0,''),(0,'LinkedIn','Profile visit',0,''),(1,'LinkedIn','Connect, blank note, Nate approves',0,''),(3,'Condition','Accepted the connect? (within 2 days)',0,''),
   (3,'LinkedIn','Message after connect',1,'branch'),(4,'Call','Call 1, no voicemail',1,''),(5,'Voice note','Manual voice note, body = {{voice_script}}',1,'new'),(6,'Call','Call 2, leave voicemail',1,''),(8,'Email','Email 2 in thread',1,''),(10,'Email','Email 3 breakup',1,''),
   (3,'Condition','Has a phone number?',1,'branch2'),(3,'Call','Voicemail',2,'branch'),(4,'Call','Call, day after voicemail',2,''),(6,'Email','Email 2 in thread',2,''),(8,'Call','Final call',2,''),(9,'Email','Email 3 breakup',2,''),
   (4,'LinkedIn','Like last post + follow',2,'branch2'),(5,'Email','Email 2 in thread',2,''),(9,'Email','Email 3 breakup',2,''))
C.append(dict(key='qual', name='Stars - Fresh Pool / Quality', id='cam_viEbB6HkYsCPtxKbi', leads=29, status='paused',
 q='Fresh quality and Stars leaders at plans near the 4.0 line. Pipeline: measurement-year conversations before the fall volume.',
 costing='Structure is the strongest of the eleven. The one live defect is the voice note step with no script, and open tracking is on with no tracking domain, which lemlist now blocks at send.',
 marks={'Channels':P,'Branching':P,'Testing':F,'Timing':P,'Variables':P,'Replies':P,'Measurement':P,'Deliverability':F,'Gates':P},
 now=stars_now('"the service measures at {{plan_name}}"'), gaps=stars_common_gaps+['Deliverability: open tracking is ON here (off on Finance). No custom tracking domain exists on the team, and lemlist now blocks sending when tracking is on without one. Turn it off.'],
 then=stars_then('"the service measures at {{plan_name}}"'),
 api=['update_sequence_step stp_LumCYdLyCLbM5ssPX (seq_FKqfv2325wMmz8Dtc): message {{voice_script}}','update_settings campaign: trackOpens false','Record the A/B read date: 14 business days after start, reply count by variant'],
 ui=[], locked='Both Email 1 variants, LinkedIn message, both call scripts, voicemail, both Email 2s, both breakups (Sep 3 rewrite, third pass).'))
C.append(dict(key='fin', name='Stars - Fresh Pool / Finance', id='cam_2gy9hmEvMjYEuPZ8A', leads=13, status='paused',
 q='CFOs and actuarial leaders at plans near the bonus line. Pipeline: quality-bonus economics conversations.',
 costing='Same tree as Quality. The voice note has no script in the task. Everything else holds.',
 marks={'Channels':P,'Branching':P,'Testing':F,'Timing':P,'Variables':P,'Replies':P,'Measurement':P,'Deliverability':P,'Gates':P},
 now=stars_now('"the bonus line at {{plan_name}}"'), gaps=stars_common_gaps+['Only 13 leads. Two calls plus a voice note per accepted connect is the right weight for CFO seats that answer; keep it.'],
 then=stars_then('"the bonus line at {{plan_name}}"'),
 api=['update_sequence_step stp_9YLwdR5Rrt6eAvXns (seq_Mtnqt8s9LKr9bKnpD): message {{voice_script}}','Record the A/B read date: 14 business days after start'],
 ui=[], locked='All copy from the Sep 3 rewrite.'))
blitz_gaps=['Channels: complete, same shape as Stars with the voice note carrying {{voice_script}} in the body (correct).',
 'Testing: Email 1 A/B is live but a one-account campaign of under ten leads cannot read a test. Keep it for consistency with the other lanes; no read date, the Stars lanes carry the read.',
 'Timing: blitz shape, ten to eleven business days. Passive LinkedIn actions (visit, like, follow) share a day with an email in the no-LinkedIn path; messages and calls never do.']
C.append(dict(key='cit', name='Blitz - Citizens', id='cam_yWefPqaDhNNv4RyQK', leads=8, status='paused',
 q='One account, eight buying-committee seats, the deflection thread. Pipeline: one Citizens meeting on the human side of the AI rollout.',
 costing='Auto-review is ON, so any lead added later launches without Nate seeing it. Jeffrey Foss is a held warm play in this account; auto-review is the wrong setting here.',
 marks={'Channels':P,'Branching':P,'Testing':H,'Timing':P,'Variables':P,'Replies':P,'Measurement':P,'Deliverability':P,'Gates':F},
 now=stars_now('"the half that\'s left"'), gaps=blitz_gaps+['Gates: autoReview is true on this campaign only. Turn it off so every added lead waits for Nate\'s review (the held Foss play depends on it).','Verified claims: "one large North American bank measured $6.1M a year" is the RBC story cited blinded, which marketing\'s registry allows. Pass.'],
 then=stars_then('"the half that\'s left"'),
 api=['update_settings campaign: automation.autoReview false'], ui=[], locked='All copy from the Sep 3 rewrite; Citizens Q1 2026 call signal verified Sep 3.'))
C.append(dict(key='hart', name='Blitz - The Hartford', id='cam_fYp7Nh9wB72gfMke6', leads=7, status='paused',
 q='One account, seven seats, the claims side of the AI number. Pipeline: one Hartford meeting on service and claims staffing.',
 costing='A second voice note sits at the ROOT after the condition, auto-send, no recording. It fires for every lead including people who never connected, and an auto voice note with no audio cannot send.',
 marks={'Channels':P,'Branching':P,'Testing':H,'Timing':P,'Variables':P,'Replies':P,'Measurement':P,'Deliverability':P,'Gates':P},
 now=stars_now('"the claims side of the AI number"')+[(4,'Voice note','ROOT voice note, auto-send, no audio, fires for everyone',0,'skip')], gaps=blitz_gaps+['The root-level voice note (stp_6s7955iZXipEEB2Xr) is the Aug 31 API placement lesson left behind. Skip it for all leads in the UI; the in-branch manual voice note already does the job.'],
 then=stars_then('"the claims side of the AI number"'),
 api=[], ui=['Skip stp_6s7955iZXipEEB2Xr (root voice note) for all leads'], locked='All copy from the Sep 3 rewrite; Hartford Q2 2026 call signal verified Sep 3.'))

bo_now=lambda s1,s2: seq((0,'Email','Email 1: '+s1+' (locked)',0,''),(1,'LinkedIn','Profile visit',0,''),(1,'LinkedIn','Connect, blank note, Nate approves',0,''),(3,'Condition','Accepted the connect? BOTH branches are EMPTY',0,'bad'),
   (5,'LinkedIn','Message to everyone, connected or not',0,'skip'),(7,'Email','Email 2: '+s2+' (locked)',0,''),(9,'Call','Call task for every lead, "cleared names only" is a note, not a gate',0,'skip'))
bo_then=lambda s1,s2: seq((0,'Email','Email 1: '+s1+' (locked)',0,''),(1,'LinkedIn','Profile visit',0,''),(2,'LinkedIn','Connect, blank note, Nate approves. A/B: note vs blank',0,'new'),(4,'Condition','Accepted the connect? (within 2 days)',0,''),
   (4,'LinkedIn','Message after connect, Nate approves',1,'new'),(4,'Nothing','Not connected: wait for Email 2',1,'branch2'),(7,'Email','Email 2: '+s2+' (locked)',0,''),(7,'Condition','call_cleared equals yes (lead variable set at AM clearance)',0,'new'),
   (9,'Call','Call task, cleared names only',1,'new'),(12,'Email','Email 3 breakup, names the re-entry condition [draft, Nate reads]',0,'new'))
bo_gaps=['Branching: the accepted-connect condition exists but both branches are empty, so it routes nobody. The LinkedIn message then goes to every lead as a task; LinkedIn refuses messages to people who are not connected, so Nate hits a dead task for most of the list.',
 'The call task fires for every lead. Mary Ann\'s rule (AM clears every name before Nate calls) lives only in the task text. Gate it on a per-lead campaign variable call_cleared, set when the AM clears the name. Never on a shared contact field.',
 'Timing: no breakup. The arc ends on a call at day 9 with no email that names the re-entry condition. Add Email 3 at day 12 (draft below, Nate reads before start).',
 'Testing: Email 1 copy is locked, so the cheap test is the connect note: with a note versus blank. Hypothesis: a note that references the email lifts acceptance. Read at 14 business days on acceptance rate.',
 'Doctrine gaps in the locked copy (no product sentence, "Worth 15 min" close): recorded for Nate\'s next read, not changed.',
 'Deliverability: open and click tracking are ON with no custom tracking domain; lemlist blocks the send. Turn both off. Reply on this campaign only pauses the lead and creates no task; set it to stop and create a task so Nate sees it.']
for key,name,cid,leads,s1,s2,extra,locked in [
 ('hc','BO Expansion - Healthcare Payer','cam_N92Tgg29ncHWnYAD9',67,'"the monday backlog"','"yesterday\'s report"',['Nate cleared copy and contacts Sep 4.'],'Email 1, LinkedIn message, Email 2, call note. Nate: "Healthcare is good."'),
 ('fs','BO Expansion - Financial Services','cam_x8ehMHnWSjBr2CLQe',79,'"between the reports"','"found capacity"',['HOLD: Nate is still thinking the Financial Services copy through. Structure fixes can be staged, nothing starts until his notes land.'],'Nothing locked yet. Copy waits on Nate; do not touch it before his notes.'),
 ('ins','BO Expansion - Insurance','cam_HCu4jiFB8oinz2s3F',33,'"the tat clock"','"the overtime premium"',['Nate: "Would not change that one. Hits the mark."'],'Email 1, LinkedIn message, Email 2, call note. Locked as reviewed.'),
 ('bpo','BO Expansion - BPO','cam_Fy287YF9X5fjPYBSo',25,'"the margin line"','"slas in real time, cost at month end"',['Maximus (5) loaded Sep 4; Frank\'s partner brief covers Maximus, give him the heads-up before this one starts.'],'Email 1, LinkedIn message, Email 2, call note. Thumbs up Sep 4.')]:
    C.append(dict(key=key,name=name,id=cid,leads=leads,status='paused',
      q='Back-office leaders inside a current customer account, cleared by the AM. Pipeline: expansion meetings the AM co-owns, on Mary Ann\'s sponsor-line rules.',
      costing='The accepted-connect branch is empty and the LinkedIn message goes to everyone, so the LinkedIn channel produces dead tasks instead of conversations. No breakup email. Tracking on without a tracking domain blocks the send.',
      marks={'Channels':P,'Branching':F,'Testing':F,'Timing':F,'Variables':P,'Replies':F,'Measurement':P,'Deliverability':F,'Gates':P if key!='fs' else H},
      now=bo_now(s1,s2), gaps=bo_gaps+extra, then=bo_then(s1,s2),
      api=['Shift the connect step (index 2) delay from 0 to 1 so visit and connect sit on different days','add_sequence_step linkedinSend (manual, title "LinkedIn message after accepted connect", priority 1) into the Accepted branch sequence with the locked LinkedIn copy; if the API refuses the branch, fall back to UI','set_ab_variant on the connect step: variant B carries the note (under 300 chars, references the email); if refused (SEQUENCE_AB_CAMPAIGN_RUNNING), fall back to UI','add_sequence_step conditional customLeadInfo call_cleared equal yes (within, delay 0) after Email 2, then a phone step (title "Call {{firstName}}, AM cleared", priority 2) in its Yes branch','add_sequence_step email (thread reply, delay 3) Email 3 breakup at the end, draft copy below','update_settings: trackOpens false, trackClicks false, onReplied stop + createNewTask true','update_lead_variables: call_cleared = no on every lead now; flips to yes per name as the AM clears'],
      ui=['Skip the root LinkedIn message step and the root call step for all leads once the branch versions exist','If the API refuses the branch add or the A/B: add the LinkedIn message inside the Accepted branch and set the connect-note A/B in the editor'],
      locked=locked))

C.append(dict(key='nn', name='BO Net-New - Back Office', id='cam_DNErdZPANvC2sqRCK', leads=130, status='paused',
 q='Nate\'s six net-new prospects, back-office leaders. Pipeline: new-logo meetings the council counts, from the warm intradiemhq.com mailbox.',
 costing='No conditions at all. LinkedIn message and voicemail land on the same day for everyone, connected or not, cleared or not. The call gate is a task note.',
 marks={'Channels':F,'Branching':F,'Testing':F,'Timing':F,'Variables':F,'Replies':F,'Measurement':P,'Deliverability':F,'Gates':P},
 now=seq((0,'Email','Email 1 "two clocks" ({{opener_line}} + {{function}})',0,''),(1,'LinkedIn','Connect, blank note, Nate approves (no visit before it)',0,''),(3,'Call','Voicemail for every lead, "cleared only" is a note',0,'skip'),(3,'LinkedIn','Message to everyone, same day as the voicemail',0,'skip'),(5,'Email','Email 2 "the headcount cutoff"',0,''),(8,'Email','Breakup "closing the loop"',0,'')),
 gaps=['Channels: no profile visit before the connect. Add it at day 1, connect at day 2.',
  'Branching: none. Add accepted-connect (message in the Yes path), has-phone in the No path (voicemail then call), and a call_cleared variable gate before any call.',
  'Timing: voicemail and LinkedIn message on the same day for everyone. In the new tree they sit in different branches on different days. Arc lands at day 9 to 11.',
  'Testing: no A/B. Email 1 subject and body A/B with a stated hypothesis is due here (130 leads, the largest BO pool): variant B = same body, offer-note close. Plus connect note versus blank.',
  'Variables: one contact collision. Steve Hagerman carries companyName JPMorgan and parentAccount JPMorgan on a truist.com address (the Sep 3 DWO push overwrote the shared contact fields). Email 1 still renders "Truist" because it uses opener_line, but the relay and the brief would show JPMorgan. Reset the contact. Two job titles carry notes in the field (Keenan "retiring end of 2026", Librera "Interim President effective Sept 1"); move the notes to lead notes.',
  'Doctrine gaps in the copy (calendar close, no product sentence, breakup signs full name): not Nate-approved yet, so a doctrine pass is a proposal for his read before Sep 21, not a change now.',
  'Deliverability: tracking on without a tracking domain blocks the send. Sender must move to nathan.belfield@intradiemhq.com once lemwarm clears it (Sep 21 earliest). Daily volume in week one: 10 to 15 leads a day.'],
 then=seq((0,'Email','Email 1 A/B: benchmark question vs offer-note close',0,'new'),(1,'LinkedIn','Profile visit',0,'new'),(2,'LinkedIn','Connect. A/B: note vs blank',0,'new'),(4,'Condition','Accepted the connect? (within 2 days)',0,'new'),
   (4,'LinkedIn','Message after connect, Nate approves',1,'branch'),(5,'Voice note','Manual voice note for WFM and planning titles (UI add, optional)',1,'new'),
   (4,'Condition','Has a phone number?',1,'branch2'),(4,'Call','Voicemail, cleared names only',2,'branch'),(5,'Call','Call, day after',2,''),(5,'LinkedIn','Second profile visit',2,'branch2'),
   (7,'Email','Email 2 in thread',0,''),(7,'Condition','call_cleared equals yes',0,'new'),(9,'Call','Final call, cleared names only',1,'new'),(11,'Email','Email 3 breakup, names the re-entry condition',0,'')),
 api=['add_sequence_step linkedinVisit at index 1, delay 1; then set the connect step delay to 1','add_sequence_step conditional linkedinInviteAccepted (within, 2) after the connect; add the LinkedIn message (manual) in Yes; add conditional hasPhoneNumber in Else with voicemail + call phone steps in its Yes','set_ab_variant on Email 1 (offer-note close, subject unchanged) and on the connect step (note vs blank); UI fallback if refused','add_sequence_step conditional customLeadInfo call_cleared equal yes after Email 2, phone step in Yes','update_sequence_step on the breakup: delay so it lands day 11','update_settings: trackOpens false, trackClicks false, onReplied stop + createNewTask true','update_lead on Hagerman: companyName Truist, companyDomain truist.com, parentAccount Truist; move Keenan and Librera title notes to lead notes','update_lead_variables: call_cleared = no on all 130'],
 ui=['Skip the root voicemail and root LinkedIn message steps for all leads once the branch versions exist','Sender switch to nathan.belfield@intradiemhq.com after lemwarm shows clear in the UI (Dallas\'s hands)'],
 locked='Nothing is locked by Nate. Copy stays as loaded until he reads a doctrine pass.'))

C.append(dict(key='dwo', name='DWO Executives - Live Pool', id='cam_SiD4KmWcRuhiF6uhL', leads=803, status='draft',
 q='C-level operations, customer and transformation executives at 346 net-new accounts. Pipeline: John\'s C-suite DWO meetings and the council\'s cost-per-meeting row, with the Lane B holdout.',
 costing='No conditions. The LinkedIn message at day 6 auto-sends to people who never accepted and fails. 36 leads have no LinkedIn URL and would stall on the connect step. LinkedIn allows 20 invites a day, so 803 leads launched at once queue for eight weeks on the connect step and drag Email 2 with them.',
 marks={'Channels':F,'Branching':F,'Testing':F,'Timing':F,'Variables':F,'Replies':F,'Measurement':P,'Deliverability':F,'Gates':P},
 now=seq((0,'Email','Email 1 A/B, per-lead angle variables (locked)',0,''),(1,'LinkedIn','Connect with note (auto), no visit before it',0,''),(3,'Email','Email 2 in thread',0,''),(6,'LinkedIn','Message, auto-send, to everyone connected or not',0,'skip'),(10,'Email','Email 3 breakup ({{peak}})',0,'')),
 gaps=['Channels: C-level, so email plus LinkedIn only, no phone, no voice note. Correct. Missing the profile visit before the connect.',
  'Branching: none. Needs has-LinkedIn-URL first (36 leads go email-only), then accepted-connect (message in Yes, second visit in No). Reply exits are automatic.',
  'Testing: Email 1 A/B is live with the doctrine hypothesis (benchmark question vs offer note), 803 leads, the one test that can produce a real read. Read date: 14 business days after the first send, on reply rate by variant. Connect note vs blank is the second cheap test.',
  'Timing: 20 LinkedIn invites a day and a mailbox in warm-up mean the launch is paced, not flipped: 15 to 20 leads a day in week one, 20 to 30 in week two, test arm and holdout arm interleaved by day so the cohort clock holds. At that pace wave 1 takes about six weeks to enter.',
  'Variables: all three previews render. Four company names read oddly: "eHarmony.com" is tagged Telecom and gets the device-season opener (wrong pool vertical); "wellabe" and "CarParts.com" are the brands\' own styling; fix eHarmony (name, vertical, opener, workTeams) and leave the other two.',
  'Measurement: cohortId and cohortArm sit on every lead, SF campaign "GTM Eng - DWO Executives - Wave 1", stamp plan written. Scorecard read date = T30 after the first send.',
  'Deliverability: sender is still the intradiem.com main mailbox; the warm intradiemhq.com mailbox is 4 days old and its lemwarm status is not readable by API (the API sees lemwarm active on the MAIN mailbox, score 81). Tracking on with no tracking domain blocks the send. Reply creates no task.'],
 then=seq((0,'Email','Email 1 A/B, angle variables (locked)',0,''),(0,'Condition','Has a LinkedIn URL?',0,'new'),
   (1,'LinkedIn','Profile visit',1,'branch'),(2,'LinkedIn','Connect. A/B: note vs blank',1,'new'),(4,'Condition','Accepted the connect? (within 2 days)',1,'new'),(4,'LinkedIn','Message after connect (locked copy)',2,'branch'),(5,'Email','Email 2 in thread',2,''),(11,'Email','Email 3 breakup',2,''),
   (4,'Email','Email 2 in thread',2,'branch2'),(7,'LinkedIn','Second profile visit',2,''),(11,'Email','Email 3 breakup',2,''),
   (4,'Email','Email 2 in thread (no URL, email only)',1,'branch2'),(10,'Email','Email 3 breakup',1,'')),
 api=['This campaign is a DRAFT, so steps can also be deleted and reordered in the UI. Rebuild the tree with propose_sequence (root: E1 A/B existing; hasLinkedinUrl; Yes: visit, invite A/B, linkedinInviteAccepted within 2, Yes: linkedinSend + E2 + E3, Else: E2 + visit + E3; Else: E2 + E3) and apply step by step with add_sequence_step, or build it in the UI from the drawing','set_ab_variant on the connect step: A = current note, B = blank','update_lead_variables on eHarmony (lea_ZyqicBavchF8Ryg6Z): companyName eHarmony, opener from the Retail line, workTeams "customer care teams", peak "holiday peak"','update_settings: trackOpens false, trackClicks false, onReplied stop + createNewTask true','Record the Email 1 A/B read date and the T30 scorecard date next to the cohort manifest'],
 ui=['If the API refuses nested branches: build the tree in the Sequence editor from the drawing (draft, delete allowed)','Sender switch to nathan.belfield@intradiemhq.com after lemwarm shows clear (Dallas\'s hands, Sep 21 to 28)','Confirm Nate\'s daily email limit in Sending settings (not readable with the current API key)'],
 locked='Email 1 bodies for all three families exactly as the Sep 4 doc wrote them (Nate has not read them yet). Email 2, LinkedIn message, Email 3 as written.'))

# --- v2: pressure model overrides (Sep 4 evening, Dallas: steps, not copy) ----
byk={c['key']:c for c in C}

# DWO executives: 16 to 17 touches over 18 business days, three leaves
byk['dwo']['then']=seq(
 (0,'Email','Email 1 A/B, angle variables (locked)',0,''),(0,'LinkedIn','Profile visit (auto), lands the same day as the email',0,'new'),(0,'Condition','Has a LinkedIn URL?',0,'new'),
 (1,'LinkedIn','Connect (auto). A/B: note vs blank',1,'branch'),(2,'Call','Call 1, voicemail: the short version is in your email. Direct line if sourced, else the office of the COO',1,'new'),(3,'Email','Email 2 in thread (12,000 VTO hours, locked)',1,''),(4,'Condition','Accepted the connect? (within 2 days)',1,'new'),
 (4,'LinkedIn','DM 1 (locked LinkedIn message), Nate approves',2,'branch'),(6,'Call','Call 2, leave voicemail',2,'new'),(6,'Email','"just tried you", in thread, same hour as the call',2,'new'),(7,'Voice note','Manual voice note (new-in-role and multi-seat accounts first)',2,'new'),(9,'Email','Email 3, NEW thread, the peak angle',2,'new'),(11,'LinkedIn','DM 2: one number, one question',2,'new'),(13,'Call','Call 3, closing voicemail: this year or next',2,'new'),(14,'Email','Email 4 in thread: the one-question email',2,'new'),(16,'LinkedIn','DM 3: closing note on LinkedIn',2,'new'),(18,'Email','Email 5 breakup ({{peak}}, locked Email 3 copy)',2,''),
 (4,'LinkedIn','Like last post (auto)',2,'branch2'),(6,'Call','Call 2, leave voicemail',2,'new'),(6,'Email','"just tried you", in thread, same hour',2,'new'),(9,'Email','Email 3, NEW thread, the peak angle',2,'new'),(11,'LinkedIn','Second profile visit (auto)',2,'new'),(13,'Call','Call 3, closing voicemail: this year or next',2,'new'),(14,'Email','Email 4 in thread: the one-question email',2,'new'),(18,'Email','Email 5 breakup (locked)',2,''),(20,'LinkedIn','Withdraw the pending invitation (auto)',2,'new'),
 (2,'Call','Call 1, voicemail (no URL: email and phone only)',1,'branch2'),(3,'Email','Email 2 in thread',1,''),(6,'Call','Call 2, voicemail + "just tried you"',1,'new'),(9,'Email','Email 3, NEW thread',1,'new'),(13,'Call','Call 3, closing voicemail',1,'new'),(14,'Email','Email 4 one-question',1,'new'),(18,'Email','Email 5 breakup',1,''))
byk['dwo']['costing']='BUILT Sep 4 evening on your go (33 steps, three leaves, IDs in DWO_Exec_Tree_Built_Sep4.json; the manual voice note after DM 1 is still your UI add). What it replaced: five touches over ten days is a director cadence. A COO\'s inbox is triaged by an EA and a cold email gets one glance; the seat is won by showing up on three channels for four weeks. Today the campaign has no calls, one LinkedIn message that auto-sends to people who never connected, no second thread, and 36 leads with no URL that would stall on the connect step. It also has no phone numbers at all, so a call layer needs sourcing before it can fire.'
byk['dwo']['gaps']=['Channels: email 5, calls 3, LinkedIn 6 (visit, connect, DM x3, like, voice note) on the connected path. Every step is a distinct touch; the only same-day pair is the deliberate call-then-email at day 6, which is what made the Resurrection "just tried you" step honest.',
 'Phones: zero of 803 leads carry a number. The ZoomInfo 500-contact list overlaps the pool by four emails and no accounts. Source direct or mobile numbers through the Clay waterfall in priority order: new-in-role (84), then multi-seat accounts (166 accounts with two or more executives, 624 people), then the rest. [estimate] 5 to 8 credits per found number, 8 of 10 hit rate on the Stars wave 1; a 20-row test first, then your go above the 200-credit line. Until a number lands, Call 1 is the EA route: main line, "the office of {{firstName}} {{lastName}}", ask for the EA by name and leave the one line.',
 'Branching: has LinkedIn URL (36 go email and phone only), accepted connect (DMs and the voice note only on Yes; likes, a second visit and the invite withdrawal on No). Reply exits automatically; meeting booked stops the lead.',
 'Testing: Email 1 A/B (benchmark question vs offer note) stays the headline test, read at 14 business days on reply rate. Connect note vs blank is the second test. One test per step, nothing else varies.',
 'Timing: 18 business days, a touch every one to two days, breakup last, pending invites withdrawn at day 20 so Nate\'s LinkedIn account never carries hundreds of open invites. A separate "Second Look" campaign takes non-responders after 20 quiet days on the peak trigger (Resurrection pattern), built later.',
 'Pacing: LinkedIn allows 20 invites, 30 messages, 30 visits a day and the warm mailbox allows 10 to 15 emails a day in week one. 15 to 20 new leads a day, test and holdout arms interleaved, is the ceiling. At that pace wave 1 enters over eight to eleven weeks, and the Lane B ads run over the test arm for the first four.',
 'Nate\'s load at 20 leads a day, steady state: about 25 dials, 12 to 15 DMs, 4 to 6 voice notes, everything else automated. A two to three hour daily block. The daily brief lists it in priority order (new-in-role and accepted connects first).',
 'Variables: all previews render; fix eHarmony (tagged Telecom, gets the device-season opener) and leave wellabe and CarParts.com, which are the brands\' own styling.',
 'New steps need bodies. Eight short drafts are on this page, all built from the locked one idea and the Humana numbers already in Email 1 and 2. They go to Nate with the rest of his read; none of the locked copy moves.']
byk['dwo']['api']=['Campaign is a DRAFT: propose_sequence with the full tree below, then add_sequence_step step by step (root: existing E1, linkedinVisit d0, conditional hasLinkedinUrl; Yes branch: linkedinInvite d1 with set_ab_variant note vs blank, phone d2, email d3 thread, conditional linkedinInviteAccepted within 2; its Yes: linkedinSend manual d4, phone d6, email d6 thread, linkedinVoiceNote manual d7, email d9 new subject, linkedinSend manual d11, phone d13, email d14 thread, linkedinSend manual d16, email d18 thread; its Else: linkedinLikeLastPost d4, phone d6, email d6, email d9, linkedinVisit d11, phone d13, email d14, email d18, linkedinWithdrawInvitation d20; root Else: phone d2, email d3, phone d6, email d6, email d9, phone d13, email d14, email d18). Voice notes inside a branch are refused by the API, so that one step is a UI add. Stop at the first refusal and tell me which steps I build by hand.',
 'Body of every new step = the draft on this page, marked [draft, Nate reads]; locked steps reuse their existing copy verbatim',
 'update_lead_variables on lea_ZyqicBavchF8Ryg6Z (eHarmony): companyName eHarmony, opener from the Retail line, workTeams "customer care teams", peak "holiday peak"',
 'Phone sourcing plan: write the priority list (new-in-role, multi-seat accounts, rest) as a CSV; 20-row Clay find-phone test with the actual cost logged; hold for your go before the rest',
 'Write the A/B read date, the T30 scorecard date and the 15-to-20-a-day pacing rule into the cohort manifest']
byk['dwo']['ui']=['Add the manual Voice message step in the Accepted branch after DM 1 (the API refuses voice notes inside branches)','If a nested branch is refused: build the leaf lists from the drawing in the Sequence editor (draft, delete and reorder allowed)','Sender switch to nathan.belfield@intradiemhq.com after lemwarm shows clear (Sep 21 to 28); confirm Nate\'s daily email limit on the same screen']
byk['dwo']['marks'].update({'Channels':F,'Branching':F,'Timing':F})

# Net-New: same pressure shape, calls only when cleared, clearance split once at the top
byk['nn']['then']=seq(
 (0,'Email','Email 1 A/B: benchmark question vs offer-note close',0,'new'),(0,'LinkedIn','Profile visit (auto)',0,'new'),(1,'LinkedIn','Connect (Nate approves). A/B: note vs blank',0,'new'),(2,'Condition','call_cleared equals yes? (AE cleared the name)',0,'new'),
 (2,'Call','Call 1, no voicemail',1,'branch'),(3,'Email','Email 2 in thread',1,''),(4,'Condition','Accepted the connect? (within 2 days)',1,'new'),
 (4,'LinkedIn','DM 1 (existing LinkedIn message), Nate approves',2,'branch'),(6,'Call','Call 2, voicemail (existing script) + "just tried you" email same hour',2,'new'),(7,'Voice note','Manual voice note, WFM and planning titles',2,'new'),(9,'Email','Email 3, NEW thread: the headcount cutoff angle',2,'new'),(11,'LinkedIn','DM 2: one number, one question',2,'new'),(13,'Call','Call 3, closing voicemail: this year or next',2,'new'),(14,'Email','Email 4 in thread: one question',2,'new'),(16,'LinkedIn','DM 3: closing note',2,'new'),(18,'Email','Email 5 breakup (existing "closing the loop")',2,''),
 (4,'LinkedIn','Like last post (auto)',2,'branch2'),(6,'Call','Call 2, voicemail + "just tried you"',2,'new'),(9,'Email','Email 3, NEW thread',2,'new'),(11,'LinkedIn','Second visit (auto)',2,'new'),(13,'Call','Call 3, closing voicemail: this year or next',2,'new'),(14,'Email','Email 4 one question',2,'new'),(18,'Email','Email 5 breakup',2,''),(20,'LinkedIn','Withdraw pending invitation',2,'new'),
 (3,'Email','Not cleared: identical path minus the three call steps (Email 2 d3, accepted split d4, DMs or likes, Email 3 d9, Email 4 d14, breakup d18)',1,'branch2'))
byk['nn']['costing']='Linear, no conditions, six touches in eight days, calls and DMs firing on people who never connected or were never cleared. Back-office ops directors answer the phone and read a thread that keeps coming; this list gets one email a week and a dead LinkedIn task.'
byk['nn']['gaps'][0]='Channels: email 5, calls 3 (cleared names only), LinkedIn 6 on the connected path. Profile visit added at day 0 with the email, connect at day 1.'
byk['nn']['gaps'][1]='Branching: clearance split once at the top (call_cleared, a per-lead campaign variable the AE flips), then accepted-connect inside each side. The not-cleared side is the same list minus calls, so no name gets dialled that an AE has not cleared.'
byk['nn']['gaps'][2]='Timing: 18 business days, breakup last, invite withdrawn at day 20. The call-then-email pair at day 6 is the only same-day pairing.'
byk['nn']['api']=['update_lead_variables call_cleared = no on all 130 (flip to yes per name as the AE clears)','update_lead on Hagerman (companyName Truist, companyDomain truist.com, parentAccount Truist); move the Keenan and Librera title notes to lead notes','add_sequence_step linkedinVisit at index 1 delay 0; set the connect delay to 1; set_ab_variant on Email 1 (offer-note close) and on the connect (note vs blank)','add_sequence_step conditional customLeadInfo call_cleared equal yes (within, 0) after the connect, then build both sides from the drawing with add_sequence_step (phone, email thread, conditional linkedinInviteAccepted within 2, linkedinSend manual, linkedinLikeLastPost, linkedinVisit, linkedinWithdrawInvitation); voice note is a UI add','New step bodies from the drafts on this page; existing Email 2 and breakup copy reused verbatim in their new positions','update_settings: trackOpens false, trackClicks false, onReplied stop + createNewTask true']
byk['nn']['ui']=['Skip the root voicemail, root LinkedIn message, root Email 2 and root breakup for all leads once the branch versions exist (the API refuses deletion)','Add the manual voice note in the cleared/accepted branch','Sender switch to nathan.belfield@intradiemhq.com after lemwarm clears']

# BO customer lanes: pressure inside Mary Ann's rule
def bo_then_v2(s1,s2):
    return seq((0,'Email','Email 1: '+s1+' (locked)',0,''),(0,'LinkedIn','Profile visit (auto)',0,''),(1,'LinkedIn','Connect, Nate approves. A/B: note vs blank',0,'new'),(3,'Condition','Accepted the connect? (within 2 days)',0,''),
      (3,'LinkedIn','DM 1 (locked LinkedIn message), Nate approves',1,'branch'),(5,'Voice note','Manual voice note, WFM and planning titles',1,'new'),(9,'LinkedIn','DM 2: one number, one question',1,'new'),(14,'LinkedIn','DM 3: closing note',1,'new'),
      (3,'LinkedIn','Like last post (auto)',1,'branch2'),(8,'LinkedIn','Second visit (auto)',1,'new'),(16,'LinkedIn','Withdraw pending invitation',1,'new'),
      (7,'Email','Email 2: '+s2+' (locked)',0,''),(7,'Condition','call_cleared equals yes? (AM cleared the name)',0,'new'),(8,'Call','Call 1, no voicemail',1,'branch'),(11,'Call','Call 2, voicemail + "just tried you" email same hour',1,'new'),(13,'Call','Call 3, closing voicemail',1,'new'),
      (12,'Email','Email 3 in thread: one question [draft]',0,'new'),(15,'Email','Email 4 breakup, names the re-entry condition [draft]',0,'new'))
bo_gaps_v2=['Channels: email 4, LinkedIn 6 on the connected path, calls 3 for cleared names only. The uncleared name still gets four emails and the LinkedIn arc, which is what Mary Ann\'s rule allows.',
 'Branching: accepted-connect (DMs and voice note on Yes; like, second visit, withdrawal on No), then a clearance split before any call. Both conditions exist as lead-level facts, never shared contact fields.',
 'Timing: 15 business days, the call-then-email pair at day 11 is the only same-day pairing, breakup last. Under the 300-by-all-hands line this arc still finishes inside September for anything started by Sep 10.',
 'Testing: Email 1 is locked, so the test is the connect note (with versus blank). Read at 14 business days on acceptance.',
 'Copy: Email 3 (one question) and Email 4 (breakup) are new drafts for Nate; DM 2 and DM 3 are the two-line LinkedIn drafts. Everything he approved stays verbatim.',
 'Deliverability: tracking off (no tracking domain). Reply on this campaign only pauses the lead and creates no task; set it to stop and create a task.']
for k,s1,s2 in [('hc','"the monday backlog"','"yesterday\'s report"'),('fs','"between the reports"','"found capacity"'),('ins','"the tat clock"','"the overtime premium"'),('bpo','"the margin line"','"slas in real time, cost at month end"')]:
    c=byk[k]; c['then']=bo_then_v2(s1,s2)
    extra=c['gaps'][6:]
    c['gaps']=bo_gaps_v2+extra
    c['costing']='Two emails, one LinkedIn task that fires on people who never connected, one call task on names nobody cleared, and it ends at day 9 with no breakup. An AM-cleared back-office director inside a customer account is the warmest seat we have and this tree gives up on them after two emails.'
    c['api']=['update_lead_variables call_cleared = no on every lead FIRST (flips to yes per name as the AM clears)','Set the connect step delay to 1; set_ab_variant on it (note vs blank); UI fallback if refused','Into the existing Accepted branch: linkedinSend manual d0 (locked LinkedIn copy), linkedinSend manual d6 (DM 2 draft), linkedinSend manual d5 (DM 3 draft); into the existing Else branch: linkedinLikeLastPost d0, linkedinVisit d5, linkedinWithdrawInvitation d8; voice note is a UI add','After Email 2: conditional customLeadInfo call_cleared equal yes (within, 0) with three phone steps in its Yes (d1 no voicemail, d3 voicemail with the "just tried you" email step right after it at d0, d2 no voicemail)','Then email d1 (Email 3 one-question draft, in thread) and email d3 (Email 4 breakup draft, in thread) at the root end','update_settings: trackOpens false, trackClicks false, onReplied stop + createNewTask true']
    c['ui']=['Skip the root LinkedIn message and root call for all leads only after the branch versions exist','Add the manual voice note in the Accepted branch after DM 1','If the API refuses a branch add or the A/B: build that piece in the editor from the drawing']
    c['marks'].update({'Channels':F})

# Stars and Blitz: extend the arc by a third week
def stars_then_v2(subj):
    return seq((0,'Email','Email 1 A/B: '+subj,0,''),(0,'LinkedIn','Profile visit',0,''),(1,'LinkedIn','Connect, blank note, Nate approves',0,''),(3,'Condition','Accepted the connect? (within 2 days)',0,''),
      (3,'LinkedIn','Message after connect',1,'branch'),(4,'Call','Call 1, no voicemail',1,''),(5,'Voice note','Manual voice note, body = {{voice_script}}',1,'new'),(6,'Call','Call 2, leave voicemail',1,''),(8,'Email','Email 2 in thread',1,''),(9,'LinkedIn','Like last post (auto)',1,'new'),(11,'Call','Call 3, no voicemail',1,'new'),(12,'Email','Email 3 in thread: one question [draft]',1,'new'),(14,'LinkedIn','DM 2: closing note [draft]',1,'new'),(16,'Email','Email 4 breakup (existing breakup copy)',1,''),
      (3,'Condition','Has a phone number?',1,'branch2'),(3,'Call','Voicemail',2,'branch'),(4,'Call','Call, day after voicemail',2,''),(6,'Email','Email 2 in thread',2,''),(8,'Call','Final call',2,''),(10,'LinkedIn','Second visit (auto)',2,'new'),(12,'Email','Email 3 in thread: one question [draft]',2,'new'),(16,'Email','Email 4 breakup (existing)',2,''),(18,'LinkedIn','Withdraw pending invitation',2,'new'),
      (4,'LinkedIn','Like last post + follow',2,'branch2'),(5,'Email','Email 2 in thread',2,''),(10,'LinkedIn','Second visit (auto)',2,'new'),(12,'Email','Email 3 in thread: one question [draft]',2,'new'),(16,'Email','Email 4 breakup (existing)',2,''),(18,'LinkedIn','Withdraw pending invitation',2,'new'))
for k,subj in [('qual','"the service measures at {{plan_name}}"'),('fin','"the bonus line at {{plan_name}}"'),('cit','"the half that\'s left"'),('hart','"the claims side of the AI number"')]:
    c=byk[k]; c['then']=stars_then_v2(subj)
    c['gaps'].insert(1,'Pressure: the current arc ends at day 10 after two calls. A third week adds a like, a third call with no voicemail, a one-question Email 3 in thread, a closing DM for connected leads, a second visit for the rest, and moves the existing breakup to day 16. Every step is a distinct touch. Two new email drafts and one DM draft per lane go to Nate; the breakup copy he approved moves, unchanged.')
    c['api']=[x for x in c['api'] if 'read date' not in x]+['Into the Accepted branch after Email 2: linkedinLikeLastPost d1, phone d2 (Call 3, no voicemail), email d1 thread (Email 3 one-question draft), linkedinSend manual d2 (DM 2 draft); then set the existing breakup delay to 2','Into the phone branch after the final call: linkedinVisit d2, email d2 thread (Email 3 draft); breakup delay to 4; linkedinWithdrawInvitation d2 after it','Into the no-phone branch after Email 2: linkedinVisit d5, email d2 (Email 3 draft); breakup delay to 4; linkedinWithdrawInvitation d2','Record the A/B read date: 14 business days after start']
    c['marks'].update({'Timing':F})

# --- render helpers -------------------------------------------------------
def esc(s): return html.escape(s, quote=False)
ICON={'Email':'E','LinkedIn':'in','Call':'C','Voice note':'V','Condition':'?','Task':'T','Nothing':'·'}
def render_seq(rows):
    out=['<ol class="seq">']
    for d,ch,text,depth,kind in rows:
        cls='step'
        if kind=='branch': cls+=' br yes'
        elif kind=='branch2': cls+=' br no'
        if kind=='new': cls+=' new'
        if kind=='skip': cls+=' skip'
        if kind=='bad': cls+=' bad'
        lab={'branch':'YES','branch2':'NO'}.get(kind,'')
        out.append(f'<li class="{cls} d{depth}"><span class="day">d{d}</span><span class="ic ic-{ch.split()[0].lower()}">{ICON.get(ch,ch[:1])}</span><span class="t">{("<b>"+lab+"</b> " if lab else "")}{esc(text)}</span>'+('<span class="flag new">add</span>' if kind=='new' else '')+('<span class="flag skip">skip in UI</span>' if kind=='skip' else '')+('<span class="flag bad">dead</span>' if kind=='bad' else '')+'</li>')
    out.append('</ol>'); return ''.join(out)

def mark(m): return {'pass':'<span class="mk p">pass</span>','fix':'<span class="mk f">fix</span>','hold':'<span class="mk h">n/a</span>'}[m]

def score(c):
    v=list(c['marks'].values()); return sum(1 for x in v if x==P), sum(1 for x in v if x==F)

# --- page ------------------------------------------------------------------
tot_leads=sum(c['leads'] for c in C)
tot_fix=sum(score(c)[1] for c in C)
CSS='''
:root{--green:#2DB56E;--green-600:#228752;--green-300:#7BD3A0;--green-100:#C4ECD4;--forest:#014637;--orange:#F58220;--orange-600:#D96D12;--ink:#202020;--ink-2:#5A5A5A;--ink-3:#9A9A9A;--bg:#FFFFFF;--sidebar:#F5F4F2;--zebra:#FAFAFA;--tint:rgba(45,181,110,.12);--tint-soft:rgba(45,181,110,.08);--otint:rgba(245,130,32,.10);--otint-line:rgba(245,130,32,.28);--line:#E0E0E0;--r:8px;--ff:'Roboto',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;--ff-mono:'Roboto Mono',ui-monospace,SFMono-Regular,Menlo,monospace;color-scheme:light}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--sidebar)}body{font-family:var(--ff);background:var(--sidebar);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased}
.sheet{max-width:1160px;margin:0 auto;background:var(--bg)}.wrap{max-width:1100px;margin:0 auto;padding:0 30px}
.eyebrow{font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.16em;font-size:11px;font-weight:600}
.logo{height:26px;width:auto;display:block;color:#014637}a{color:var(--green-600)}
.hero{background:var(--forest);color:#fff;padding:44px 0 36px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-160px;top:-120px;width:440px;height:440px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.30),transparent 62%)}
.hero .wrap{position:relative;z-index:1}.hero .logo{height:46px;margin-bottom:24px;color:#fff}.hero .eyebrow{color:var(--green-300)}
.hero h1{font-weight:900;font-size:38px;line-height:1.08;margin:14px 0 14px;letter-spacing:-.02em;max-width:26ch}
.hero p.sub{font-size:17px;max-width:70ch;color:#C7DAD1}.hero p.sub b{color:#fff;font-weight:700}
.hstats{display:grid;grid-template-columns:repeat(4,auto);gap:14px 44px;justify-content:start;margin-top:26px}
.hstats div b{display:block;white-space:nowrap;font-weight:900;font-size:34px;color:var(--green-300);letter-spacing:-.02em;line-height:1;font-variant-numeric:tabular-nums}
.hstats div>span{display:block;font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#9DBBAE;font-weight:600;margin-top:7px}
section{padding:36px 0;border-bottom:1px solid var(--line)}section:last-of-type{border-bottom:none}section>.wrap>.eyebrow{color:var(--green-600)}
h2{font-weight:900;font-size:28px;line-height:1.12;margin:10px 0 10px;letter-spacing:-.02em}h2+.lede{font-size:16px;color:var(--ink-2);margin-bottom:18px;max-width:80ch}
h3{font-weight:700;font-size:19px;margin:24px 0 8px;letter-spacing:-.01em}h4{font-size:15px;font-weight:700;margin:16px 0 6px}
p{color:var(--ink-2);max-width:80ch;margin-top:10px;font-size:15px}p b,li b,td b{color:var(--ink);font-weight:700}
.tldr{background:var(--tint-soft);border:1px solid var(--tint);border-left:4px solid var(--green);border-radius:var(--r);padding:22px 28px}
.tldr .k{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--green-600);font-weight:600;margin-bottom:10px}
.tldr ul{list-style:none}.tldr li{padding:7px 0 7px 24px;position:relative;font-size:15px;color:var(--ink-2)}.tldr li::before{content:"";position:absolute;left:0;top:14px;width:7px;height:7px;border-radius:2px;background:var(--green)}
.callout{background:var(--otint);border:1px solid var(--otint-line);border-left:4px solid var(--orange);border-radius:var(--r);padding:18px 24px;margin-top:20px}
.callout h4{font-size:16px;font-weight:700;color:var(--orange-600);margin:0 0 6px}.callout p{font-size:14.5px;margin-top:0;max-width:none}
.gate{background:var(--tint-soft);border:1px solid var(--tint);border-left:4px solid var(--green);border-radius:var(--r);padding:18px 24px;margin-top:20px}
.gate h4{font-size:16px;font-weight:700;color:var(--green-600);margin:0 0 6px}.gate p{font-size:14.5px;margin-top:0;max-width:none}
.tablewrap{overflow-x:auto;margin-top:16px}table{width:100%;border-collapse:collapse;font-size:13.5px}
th{font-family:var(--ff-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);text-align:left;padding:0 10px 10px 0;border-bottom:1px solid var(--line);font-weight:600;white-space:nowrap}
td{padding:9px 10px 9px 0;border-bottom:1px solid var(--line);color:var(--ink-2);vertical-align:top}tbody tr:nth-child(even){background:var(--zebra)}
td.who{white-space:nowrap;color:var(--ink);font-weight:700}td.who small{display:block;font-family:var(--ff-mono);font-weight:500;font-size:10px;color:var(--ink-3);letter-spacing:.04em}
.mk{display:inline-block;font-family:var(--ff-mono);font-size:9.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;padding:2px 7px;border-radius:5px;white-space:nowrap}
.mk.p{background:var(--tint);color:var(--green-600)}.mk.f{background:#FDECD9;color:var(--orange-600)}.mk.h{background:var(--zebra);color:var(--ink-3);border:1px solid var(--line)}
.card{background:var(--bg);border:1px solid var(--line);border-radius:var(--r);padding:22px 26px;box-shadow:0 1px 2px rgba(20,30,25,.04);margin-top:22px}
.card .head{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;flex-wrap:wrap}
.card h3{margin:0;font-size:21px}.card .idl{font-family:var(--ff-mono);font-size:11px;color:var(--ink-3);letter-spacing:.04em;margin-top:4px}
.card .sc{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600;text-align:right}.card .sc b{display:block;font-family:var(--ff);font-size:26px;font-weight:900;color:var(--forest);letter-spacing:-.02em;line-height:1}
.q{margin-top:12px;padding:12px 16px;background:var(--zebra);border-radius:6px;font-size:14.5px;color:var(--ink-2)}.q b{color:var(--ink)}
.cost{margin-top:10px;padding:12px 16px;border-left:4px solid var(--orange);background:var(--otint);border-radius:6px;font-size:14.5px;color:var(--ink-2)}.cost b{color:var(--orange-600)}
.two{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:16px}@media(max-width:820px){.two{grid-template-columns:1fr}}
.two>div>.eyebrow{margin-bottom:8px;color:var(--ink-3)}.two>div:last-child>.eyebrow{color:var(--green-600)}
.seq{list-style:none;border-left:2px solid var(--line);margin-left:10px}
.seq li{position:relative;display:flex;gap:9px;align-items:flex-start;padding:5px 0 5px 16px;font-size:13.5px;color:var(--ink-2);line-height:1.4}
.seq li::before{content:"";position:absolute;left:-6px;top:11px;width:10px;height:10px;border-radius:50%;background:var(--bg);border:2px solid var(--ink-3)}
.seq li.d1{margin-left:22px}.seq li.d2{margin-left:44px}
.seq li.br::before{border-color:var(--forest);background:var(--forest)}
.seq li.new{color:var(--ink)}.seq li.new::before{border-color:var(--green);background:var(--green)}
.seq li.skip{text-decoration:line-through;color:var(--ink-3)}.seq li.skip::before{border-color:var(--orange);background:#fff}
.seq li.bad::before{border-color:var(--orange);background:var(--orange)}
.day{font-family:var(--ff-mono);font-size:10px;font-weight:600;color:var(--green-600);min-width:26px;padding-top:3px}
.ic{font-family:var(--ff-mono);font-size:9.5px;font-weight:700;min-width:20px;height:20px;line-height:20px;text-align:center;border-radius:4px;background:var(--zebra);border:1px solid var(--line);color:var(--ink-2);flex:none}
.ic-email{background:var(--forest);color:#fff;border-color:var(--forest)}.ic-linkedin{background:#E8F0FA;color:#0F4C99;border-color:#C9DBF2}.ic-call{background:#FDECD9;color:var(--orange-600);border-color:var(--otint-line)}.ic-voice{background:#EEE7F8;color:#5B3FA0;border-color:#D9CCF0}.ic-condition{background:#fff;color:var(--forest);border-color:var(--forest)}
.t{flex:1}.t b{font-family:var(--ff-mono);font-size:9.5px;color:var(--forest);letter-spacing:.06em;margin-right:4px}
.flag{font-family:var(--ff-mono);font-size:9px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;padding:2px 6px;border-radius:4px;white-space:nowrap;text-decoration:none}
.flag.new{background:var(--tint);color:var(--green-600)}.flag.skip{background:#FDECD9;color:var(--orange-600)}.flag.bad{background:var(--orange);color:#fff}
.gaps{list-style:none;margin-top:8px}.gaps li{padding:6px 0 6px 20px;position:relative;font-size:14px;color:var(--ink-2)}.gaps li::before{content:"\\2192";position:absolute;left:0;color:var(--green-600);font-weight:700}
.cs{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:14px}@media(max-width:820px){.cs{grid-template-columns:1fr}}
.cs div{background:var(--zebra);border-radius:6px;padding:12px 16px;font-size:13.5px}.cs .eyebrow{margin-bottom:6px}.cs.api .eyebrow{color:var(--green-600)}
.cs ul{list-style:none}.cs li{padding:4px 0 4px 16px;position:relative;color:var(--ink-2)}.cs li::before{content:"";position:absolute;left:0;top:11px;width:6px;height:6px;border-radius:2px;background:var(--green)}
.cs div.u li::before{background:var(--orange)}
.lock{margin-top:12px;font-size:13.5px;color:var(--ink-2);padding:10px 14px;border:1px dashed var(--line);border-radius:6px}.lock b{font-family:var(--ff-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--forest)}
code{font-family:var(--ff-mono);font-size:12.5px;background:var(--zebra);padding:1px 5px;border-radius:4px;color:var(--ink)}
.steps{list-style:none;margin-top:18px;border-top:1px solid var(--line)}
.steps li{display:grid;grid-template-columns:44px 1.1fr 130px 1.8fr;gap:18px;align-items:start;padding:13px 0;border-bottom:1px solid var(--line)}
.steps .n{width:34px;height:34px;border-radius:6px;background:var(--forest);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:16px}
.steps li.hold .n{background:var(--orange)}
.steps .t{font-weight:700;font-size:15px;letter-spacing:-.01em;color:var(--ink)}.steps .o{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);font-weight:600;padding-top:4px}.steps .r{font-size:14px;color:var(--ink-2)}
.ui ol{margin:8px 0 0 20px;font-size:14px;color:var(--ink-2)}.ui li{padding:4px 0}.ui li b{color:var(--ink)}.ui .confirm{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;background:#FDECD9;color:var(--orange-600);padding:2px 6px;border-radius:4px}
.foot{padding:26px 0 46px;text-align:center;color:var(--ink-3);font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;background:var(--bg);text-transform:uppercase}.foot .logo{height:26px;display:inline-block;margin:0 auto 12px;opacity:.85}.foot span{display:block;margin-top:4px}
@media print{.sheet{max-width:none}section{page-break-inside:auto}.card{page-break-inside:avoid}}
'''

def card(c):
    ps,fs=score(c)
    marks=' '.join(f'<span class="mk {m[0]}" title="{ln}">{ln}</span>' for ln,m in c['marks'].items())
    api=''.join(f'<li>{esc(x)}</li>' for x in c['api']) or '<li>Nothing for the API.</li>'
    ui=''.join(f'<li>{esc(x)}</li>' for x in c['ui']) or '<li>Nothing for the UI.</li>'
    return f'''
<div class="card" id="{c['key']}">
 <div class="head"><div><h3>{esc(c['name'])}</h3><div class="idl">{c['id']} · {c['leads']} leads · {c['status']}</div></div><div class="sc"><b>{ps}/9</b>{fs} to fix</div></div>
 <div class="q"><b>What it produces.</b> {esc(c['q'])}</div>
 <div class="cost"><b>What is costing meetings.</b> {esc(c['costing'])}</div>
 <div style="margin-top:12px">{marks}</div>
 <div class="two"><div><div class="eyebrow">As it is today</div>{render_seq(c['now'])}</div><div><div class="eyebrow">As it should run</div>{render_seq(c['then'])}</div></div>
 <h4>Gaps by line</h4><ul class="gaps">{''.join(f'<li>{esc(g)}</li>' for g in c['gaps'])}</ul>
 <div class="cs"><div class="api"><div class="eyebrow">Agent applies on your go (API and MCP)</div><ul>{api}</ul></div><div class="u"><div class="eyebrow">Your hands in the lemlist UI</div><ul>{ui}</ul></div></div>
 <div class="lock"><b>Do not change</b> &nbsp;{esc(c['locked'])}</div>
</div>'''

def scoretable():
    hdr=''.join(f'<th>{l}</th>' for l in LINES)
    rows=[]
    for c in C:
        ps,fs=score(c)
        cells=''.join(f'<td>{mark(c["marks"][l])}</td>' for l in LINES)
        rows.append(f'<tr><td class="who"><a href="#{c["key"]}" style="color:inherit;text-decoration:none">{esc(c["name"])}</a><small>{c["leads"]} leads · {c["status"]}</small></td>{cells}<td class="who">{ps}/9</td></tr>')
    return f'<div class="tablewrap"><table><thead><tr><th>Campaign</th>{hdr}><th>Score</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'.replace('</th>><th>','</th><th>')

BREAKUPS=[('Healthcare Payer','re: the monday backlog','Hi {{firstName}}, I\'ll stop here. If the Monday backlog puts claims capacity back on your desk, this quarter or next, reply to this thread and I\'ll pick it up. Good luck with open enrollment. Nathan'),
('Financial Services (holds for Nate\'s notes)','re: between the reports','Hi {{firstName}}, I\'ll stop here. If year-end volume puts found capacity back on your desk, reply to this thread and I\'ll pick it up. Good luck with the close. Nathan'),
('Insurance','re: the tat clock','Hi {{firstName}}, I\'ll stop here. If the Q4 claims peak puts turnaround time back on your desk, reply to this thread and I\'ll pick it up. Good luck with the renewal season. Nathan'),
('BPO','re: the margin line','Hi {{firstName}}, I\'ll stop here. If a renewal conversation puts margin per seat back on your desk, reply to this thread and I\'ll pick it up. Good luck with the year-end SLAs. Nathan')]

page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Nate campaign structure review, Sep 4 2026</title>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=Roboto+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<svg width="0" height="0" style="position:absolute">{LOGO}</svg>
<div class="sheet">
<div class="hero"><div class="wrap">
<svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
<div class="eyebrow">GTM Engineering · Nate's lemlist campaigns · Fri Sep 4 2026 · dry run, nothing sending</div>
<h1>What each campaign produces, and the step that is costing it meetings</h1>
<p class="sub">Every sequence pulled from lemlist tonight, both A/B variants, every branch, every task title, readiness check run on all eleven. Scored against the nine lines of a multichannel motion, then rebuilt on a <b>sustained pressure model</b>: calls, LinkedIn DMs, voice notes and two email threads over four weeks. Copy Nate approved stays as written. Structure changes are proposals until you say go; the prompts in chat apply them.</p>
<div class="hstats"><div><b>{len(C)}</b><span>campaigns, all Nate's</span></div><div><b>{tot_leads:,}</b><span>leads loaded, none sent</span></div><div><b>7</b><span>would block at send: tracking on, no tracking domain</span></div><div><b>6</b><span>campaigns the reply relay cannot route</span></div></div>
</div></div>

<section><div class="wrap">
<div class="tldr"><div class="k">What matters first</div><ul>
<li><b>Seven campaigns cannot send as configured.</b> Open or click tracking is on (Quality, the four BO customer lanes, Net-New, DWO) and the team has no custom tracking domain. lemlist now blocks sending in that state. The readiness check does not catch it. Turn tracking off on the cold lanes; replies still track.</li>
<li><b>The LinkedIn channel is wired to fail on six campaigns.</b> The four BO customer lanes have an accepted-connect condition with both branches empty, so the LinkedIn message goes to everyone as a task. Net-New and DWO have no condition at all; DWO auto-sends the message. LinkedIn refuses messages to non-connections.</li>
<li><b>Six campaigns are invisible to Nate's Slack channel.</b> The relay routes by campaign id and the map stops at the Blitz pair. BO x4, Net-New and DWO replies would be logged as unroutable. The daily brief config has no BO or DWO block and sits at live=false.</li>
<li><b>The trees are rebuilt on a pressure model, not the five-touch arc.</b> Three channels for four weeks, a touch every one to two business days: five emails across two threads, three calls (no voicemail, voicemail paired with a same-hour email, no voicemail), three LinkedIn DMs for accepted connects, a voice note, likes and visits for the rest, and the pending invite withdrawn at the end. Sixteen to seventeen touches per executive.</li>
<li><b>Calls need phones first.</b> Zero DWO leads carry a number and the ZoomInfo list does not cover the pool. Sourcing runs in priority order (new-in-role, multi-seat accounts, rest), 20-row test then your go; until a number lands the call is the EA route through the main line.</li>
<li><b>DWO launches paced, not flipped.</b> 20 LinkedIn invites a day, 30 messages, a warm-up mailbox at 10 to 15 emails a day in week one, and Nate's own dial time all point to 15 to 20 leads a day, test and holdout arms interleaved so the Lane B clock holds. Wave 1 enters over eight to eleven weeks.</li>
<li><b>Stars and Blitz are structurally sound.</b> Five fixes total: a dead "opened" branch and two stray steps on Resurrection, an empty voice-note body on Quality and Finance, a root voice note on Hartford, auto-review on Citizens.</li>
<li><b>Nothing unverified in the copy.</b> Every Humana figure traces to the VERIFIED 1:many rows; the Blitz "large North American bank, $6.1M" line is the RBC story cited blinded, which marketing's registry allows. All 33 previews render with no empty braces.</li>
</ul></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">Scorecard</div><h2>Eleven campaigns against the nine lines</h2><p class="lede">Pass means the line holds as built. Fix means a specific change is named in the campaign's card. n/a means the line cannot apply (a locked A/B winner, a campaign that waits on Nate). Click a name to jump.</p>
{scoretable()}
<div class="gate"><h4>What holds everywhere</h4><p>Sender is Nate on every campaign. Customer exclusion passed upstream in Clay on every load (the BO customer lanes are customer lanes by design). Opt-out line present on every Stars, Blitz and BO customer Email 1 (US prospect lanes carry none, none required). One Salesforce campaign name per lemlist campaign and Lead Source GTM Engineering in all eleven stamp plans. The relay drafts a reply in Nate's voice with zero stats, and the reply-triage agent handles the objection categories.</p></div>
<div class="callout"><h4>Where the standard and deliverability disagree</h4><p>Line 2 asks for a call task that fires on a click. Click tracking is bot-polluted and requires a tracking domain lemlist will not send without. The proposal keeps click and open tracking off on every cold lane and fires the call from the two honest signals instead: the accepted connect, and the phone branch for people who never connect. If you want the click trigger later, the custom tracking domain is a DNS change on intradiem.com through IT, then the branch is one API call.</p></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">Campaign by campaign</div><h2>The sequence each one should become</h2><p class="lede">Left is the live tree. Right is the proposal. Green dots are additions, struck lines are steps the API cannot delete and you skip for all leads in the UI, orange dots are dead or misplaced steps. Days are business days from the first touch.</p>
{''.join(card(c) for c in C)}
</div></section>

<section><div class="wrap"><div class="eyebrow">The pressure model</div><h2>What it takes to get an executive's attention, and what it costs Nate per day</h2>
<p class="lede">The doctrine's five-touch arc is a director cadence: people who read their own inbox and answer the phone. A COO's inbox is triaged by an EA, LinkedIn is the one channel they touch themselves, and a cold thread earns a reply on the third or fourth honest attempt, not the first. The trees above are rebuilt on six rules.</p>
<ul class="gaps">
<li><b>Three channels, four weeks, a touch every one to two business days.</b> Emails 5, calls 3, LinkedIn 6 on the connected path: 16 to 17 distinct touches over 18 business days, then a withdrawal of the pending invite so Nate's account stays clean. Nothing is "bumping this"; every step carries one new thing (a number, a question, a peak, a call).</li>
<li><b>The call layer runs on two scripts and one route.</b> Every call leaves a voicemail, each one different: Call 1 points at the note already in their inbox, Call 2 carries the overtime number and pairs with a same-hour "just tried you" email in the thread, Call 3 asks the this-year-or-next question and closes the file. No direct number yet means the EA route: main line, the office of the executive, one line left with the assistant by name. That is a real touch, and EAs forward.</li>
<li><b>LinkedIn is where the executive answers.</b> Visit lands the same day as Email 1 so the name is familiar before the connect. DMs only ever go to accepted connects (three of them: the short version, one number plus one question, the close). Non-connects still see a like and a second visit. The voice note goes to accepted connects who are new in role or sit in a multi-seat account, because that is where Nate's recording minutes pay.</li>
<li><b>Two threads, not one.</b> Emails 1, 2, 4 and 5 live in one thread. Email 3 opens a new subject on the vertical peak so the inbox shows a second conversation, which is what survives an EA's triage.</li>
<li><b>Branch on facts, exit on signal.</b> Has URL, accepted connect, has phone or cleared. Reply exits, meeting booked stops, every campaign. Open and click tracking stay off; the call is the read.</li>
<li><b>Second Look is a separate campaign.</b> Twenty quiet days after the breakup, non-responders enter a Resurrection-shaped campaign on the peak trigger (one call, one email, one DM). Built after wave 1 is in; it keeps the council's reporting clean and the cohort id intact.</li>
</ul>
<h3>Phones before calls</h3><p>Zero of the 803 DWO leads carry a number, and the ZoomInfo 500-contact list overlaps the pool by four emails and no accounts. The call layer therefore starts with a sourcing pass in priority order: the 84 new-in-role executives, then the 624 people at the 166 accounts with two or more seats (a call to one COO at an account where a CAO also sits is worth two), then the rest. Clay find-phone waterfall: [estimate] 5 to 8 credits per found number, 8 of 10 hit on the Stars wave 1, so roughly 700 to 1,100 credits over the wave if it runs to the end. A 20-row test with the real cost logged, then your go above the 200-credit line, then batches that stay ahead of the daily launch pace. Until a number lands, Call 1 is the EA route. The ZoomInfo ask through Chris (one ask at a time) is the cheaper path if it comes through, and it can run in parallel.</p>
<h3>Nate's day at full pace</h3>
<div class="tablewrap"><table><thead><tr><th>Lane running</th><th>Leads entering per day</th><th>Dials per day (steady state)</th><th>DMs and voice notes per day</th><th>Nate's block</th></tr></thead><tbody>
<tr><td class="who">DWO executives alone</td><td>15 to 20</td><td>25 to 35 (three calls, phones on about six in ten, EA route on the rest)</td><td>12 to 15 DMs, 4 to 6 voice notes</td><td>2 to 3 hours</td></tr>
<tr><td class="who">BO customer x3 plus Net-New first</td><td>15 (all cleared names)</td><td>15 to 25 (cleared names only)</td><td>8 to 10 DMs, 2 to 4 voice notes</td><td>1.5 to 2 hours</td></tr>
<tr><td class="who">Stars and Blitz restart</td><td>100 in one week</td><td>20 to 30 for two weeks</td><td>10 DMs, 5 voice notes</td><td>1.5 hours for two weeks</td></tr>
</tbody></table></div>
<p>The LinkedIn automation ceiling on the account (20 invites, 30 messages, 30 visits a day) is the hard cap on entering leads; the manual DMs and calls are Nate's cap. Both point to 15 to 20 new DWO leads a day, BO lanes ahead of DWO so the customer meetings land before the all-hands, and the daily brief ordering his list: replies first, accepted connects and new-in-role next, then the rest.</p>
<h3>Drafts for the new steps (Nate reads, nothing locked moves)</h3><p>Every draft carries only the numbers already in the locked Email 1 and 2 (Humana, VERIFIED 1:many), the locked one idea, and the lead's own variables. Under the doctrine word counts, first-name sign-off, no calendar in a first ask.</p>
<div class="tablewrap"><table><thead><tr><th>Step</th><th>DWO executives (Nate's voice)</th></tr></thead><tbody>
<tr><td class="who">Call 1, no voicemail</td><td>"{{firstName}}? Nathan Belfield at Intradiem. I sent you a note on idle minutes at {{companyName}}. Can I take 30 seconds, and you tell me if it's not for you?" Engage: "Your operations pay for capacity twice, idle minutes inside the shift and overtime after it. Intradiem sits on top of the WFM and case systems your {{workTeams}} already run and moves work into the idle windows as they open. Humana has two hours back per agent per month on the record." Hand it over: "Is overtime a line you're being asked to take down this year?" Brush-off: "Fair enough. Is that because it's handled, or not the priority right now?" EA route: "Could you point me to whoever runs {{firstName}}'s calendar? One line for them: idle time and overtime across the {{workTeams}}, and whether it's worth fifteen minutes in October."</td></tr>
<tr><td class="who">Call 2, voicemail (under 25 seconds)</td><td>"{{firstName}}, Nathan Belfield with Intradiem. I've sent a couple of notes on idle minutes and overtime at {{companyName}}. Short version: the capacity is already on the payroll, it arrives at the wrong minute, and Humana gets two hours back per agent per month by moving work into it. I'm at 937-238-3179, or reply to my email. Thanks {{firstName}}."</td></tr>
<tr><td class="who">"just tried you" (in thread, same hour)</td><td>Hi {{firstName}}, just tried your line and missed you, so I'll leave this here. Same question as my notes: how much of {{companyName}}'s overtime is idle time in disguise? If this is the wrong desk, a name is all I need. Nathan</td></tr>
<tr><td class="who">Voice note (30 seconds, accepted connects)</td><td>"Hi {{firstName}}, Nathan Belfield at Intradiem, thanks for connecting. One thought behind my note: most operations pay for capacity twice, idle minutes inside the shift and overtime after it. We move work into those idle windows as they open, on top of what your {{workTeams}} already run. Humana has two hours back per agent per month on the record. Worth a conversation on what that looks like at {{companyName}}? Thanks."</td></tr>
<tr><td class="who">Email 3, new thread. Subject: <code>{{peak}} at {{companyName}}</code></td><td>Hi {{firstName}}, {{peak}} is the stretch where the staffing plan and the day disagree most, and where the overtime line gets set for the year. Intradiem moves work, training and breaks into idle windows as they open, so the {{workTeams}} absorb the peak without the after-hours bill. Humana has it on the record: 12,000 voluntary time-off hours found inside the schedule, counted as overtime avoided. Worth a look at what that does to {{companyName}}'s {{peak}} before it starts? Nathan</td></tr>
<tr><td class="who">DM 2 (LinkedIn)</td><td>{{firstName}}, one number from the Humana story and then I'll leave you be: 12,000 voluntary time-off hours found inside the schedule, counted as overtime avoided. Is overtime a line you're being asked to take down this year, or is it holding steady?</td></tr>
<tr><td class="who">Email 4, in thread (one question)</td><td>Hi {{firstName}}, one question and I'll close the file either way: is intraday capacity a this-year item for {{companyName}}'s operations, or a next-year one? Either answer helps me stop guessing. Nathan</td></tr>
<tr><td class="who">DM 3 (LinkedIn, close)</td><td>Closing this out here too, {{firstName}}. If {{peak}} puts intraday capacity back on your desk, the email thread is the fastest way back to me. Good luck with it. Nathan</td></tr>
</tbody></table></div>
<p>The same eight shapes carry to the other lanes with the lane's own number and question: Stars asks "is the gap to 4.0 a this-cycle question or next year's"; the BO lanes ask about turnaround time, found capacity, the overtime premium or margin per seat and carry no figure (mechanism-only, as loaded); Net-New asks about the headcount cutoff. Those drafts are written the day you say go, in the same table format, before any step is created.</p>
</div></section>

<section><div class="wrap"><div class="eyebrow">Across all eleven</div><h2>Platform fixes that no single campaign can carry</h2>
<h3>Reply handling</h3><ul class="gaps">
<li>Add six ids to campaign_channel_map in automation/config/lemlist_channels.json, all routed to nathan: cam_N92Tgg29ncHWnYAD9, cam_x8ehMHnWSjBr2CLQe, cam_HCu4jiFB8oinz2s3F, cam_Fy287YF9X5fjPYBSo, cam_DNErdZPANvC2sqRCK, cam_SiD4KmWcRuhiF6uhL.</li>
<li>Add two brief blocks to automation/config/action_brief.json under nathan: "backoffice" (the five BO campaigns, playbook source motions/back_office_expansion/BO_Lemlist_Campaign_Copy_Sep2.md, held lead Ilene Baylinson) and "dwo" (cam_SiD4KmWcRuhiF6uhL, source motions/dwo_executives/DWO_Exec_Sequence_Sep4.md, the 36 provider-unit COOs as held names). Stars source list should add motions/star_ratings/Nate_Copy_Rewrite_Sep3.md.</li>
<li>The brief is at live=false since Aug 17 because the trial plan blocked task actions. The plan is now Multichannel. Flipping it live posts to Nate's channel every weekday morning, so that flip is your call, not part of the go.</li>
<li>onReplied on BO x5 and DWO is "pause the lead, no task". Stars and Blitz use "stop, create task". Align the six to stop plus task so a reply shows up in Nate's task list as well as the relay.</li></ul>
<h3>Deliverability and sending</h3><ul class="gaps">
<li>No custom tracking domain on the team (customDomain null). Tracking off on the seven campaigns listed above; keep trackReplies on.</li>
<li>lemwarm reads active on Nate's MAIN mailbox (usm_BuFNcjKBEvKKABRid) since Aug 31, ramp-up 3, max 30 a day, deliverability 81. The intradiemhq.com mailbox is 4 days old; its warm-up status is not exposed to this API key, so the UI check before the sender switch stands (Sep 21 to 28).</li>
<li>LinkedIn limits on the account: 20 invites, 30 messages, 30 visits a day. Every campaign that starts adds to the same queue. Start order therefore matters: BO customer lanes (204 leads) before DWO (803), Stars and Blitz (100) in between, so Nate's daily task list stays under the limit.</li>
<li>Nate's daily email limit is not readable with the current API key (sending settings show no email accounts for the key owner). Confirm it in his Sending settings before the first start.</li></ul>
<h3>Measurement</h3><ul class="gaps">
<li>Lane B applies to DWO wave 1 only: cohort GTMENG-DWO1-2026-09, test 399 / holdout 405 by domain hash, both stamped on every lead. The other ten campaigns are not in a cohort, by design.</li>
<li>Read dates to write into the cohort manifest: Email 1 A/B read 14 business days after the first DWO send; scorecard T30 after the first send; council row = cost per meeting against $3,402 and 19 percent meeting-to-opp, from automation/council_meeting_feed.py.</li>
<li>Stamp plans exist for all eleven campaigns (1,141 rows) but no Salesforce write exists until Sierra's ticket lands. Lead Source GTM Engineering is therefore staged, not applied.</li></ul>
<h3>Voice</h3><ul class="gaps">
<li>Voice profiles available: 26 lemlist defaults (US voices Kévin, Armando, Hope, Lori; UK voices Tal, Shelby, Lucy; plus Greek, Dutch, Portuguese, German, Spanish, French), no cloned team voice. An AI note in Nate's own voice needs his clone recorded in the UI and Jason Jones's exception on the pilot. Until then every voice note is a manual recording task, which is what the Stars and Blitz trees already carry.</li></ul>
<h3>Email 3 breakup drafts for the BO customer lanes</h3><p>Under 40 words each, in-thread reply, names the re-entry condition, first-name sign-off. Drafts for Nate to read before any of the four starts; the structure change (the step) can go in with the draft as the body.</p>
<div class="tablewrap"><table><thead><tr><th>Lane</th><th>Subject</th><th>Body</th></tr></thead><tbody>{''.join(f'<tr><td class="who">{esc(a)}</td><td><code>{esc(b)}</code></td><td>{esc(c)}</td></tr>' for a,b,c in BREAKUPS)}</tbody></table></div>
</div></section>

<section><div class="wrap"><div class="eyebrow">Locked</div><h2>What does not change because Nate approved it</h2>
<ul class="gaps">
<li><b>BO Insurance, Healthcare Payer, BPO:</b> Email 1, LinkedIn message, Email 2, call note, exactly as loaded. Doctrine gaps (no product sentence, calendar close) are recorded for his next read, not applied.</li>
<li><b>BO Financial Services:</b> nothing touched until his notes. Structure fixes stage, campaign does not start.</li>
<li><b>Stars Quality, Finance, Resurrection, Blitz Citizens, Hartford:</b> every email, LinkedIn message, call script and voicemail from the Sep 3 third pass, including the 160-word Email 1s and the two-call rhythm he accepted.</li>
<li><b>DWO Email 1 bodies</b> for all three families as the Sep 4 doc wrote them (median 128 words), Email 2, LinkedIn message and Email 3. Nate has not read them; nothing edits ahead of him.</li>
<li><b>Variant B of Resurrection's "just tried you"</b> is archived by the winner pick; leave it.</li>
<li><b>Blank connect notes</b> on Stars and Blitz stay blank. The connect-note A/B is proposed only where the sample can teach something (BO x5, DWO).</li></ul>
</div></section>

<section><div class="wrap"><div class="eyebrow">Order</div><h2>Do it in this order so nothing regresses</h2>
<ol class="steps">
<li><div class="n">1</div><div class="t">Config first, no lemlist touch</div><div class="o">agent, on go</div><div class="r">Relay map (six ids) and brief blocks. Zero risk, and every later change becomes visible in Nate's channel the moment it matters.</div></li>
<li><div class="n">2</div><div class="t">Settings on all eleven</div><div class="o">agent, on go</div><div class="r">Tracking off on the seven, onReplied stop plus task on the six, autoReview off on Citizens. Settings before structure so no test send can ever hit the tracking block.</div></li>
<li><div class="n">3</div><div class="t">Stars and Blitz surgery</div><div class="o">agent then you</div><div class="r">Voice-note bodies (Quality, Finance), Resurrection condition swap by API. Then your UI pass: skip the three stray steps, add the manual voice note in Resurrection's Yes branch. These lanes are then ready to restart on Nate's word.</div></li>
<li class="hold"><div class="n">H</div><div class="t">Hold: BO Financial Services</div><div class="o">do nothing yet</div><div class="r">Stage nothing on cam_x8ehMHnWSjBr2CLQe until Nate's notes land. His copy read may change Email 2, and a structural edit mid-read is the kind of thing that erases his changes.</div></li>
<li><div class="n">4</div><div class="t">BO customer lanes, three of four</div><div class="o">agent then you</div><div class="r">Order inside each: call_cleared = no on every lead FIRST, then the call-gate condition, then the branch LinkedIn message, then the breakup step with the draft, then the connect-note A/B. Only after all adds succeed: your UI skip of the root LinkedIn message and root call. Skipping before the branch versions exist would leave the campaign with no LinkedIn message at all.</div></li>
<li><div class="n">5</div><div class="t">Net-New surgery, before the mailbox switch</div><div class="o">agent then you</div><div class="r">Same paste-then-skip order. Do it now while it waits on lemwarm; the doctrine copy pass for Nate's read goes to him in the same window so both land before Sep 21.</div></li>
<li><div class="n">6</div><div class="t">Drafts to Nate, phone test in parallel</div><div class="o">agent then Nate</div><div class="r">The eight DWO drafts plus the Stars, BO and Net-New variants go on his read page in one pass. Same day: the phone priority CSV and the 20-row Clay find-phone test with the real cost logged. Neither blocks the other.</div></li>
<li><div class="n">7</div><div class="t">DWO rebuild in draft</div><div class="o">agent, UI fallback</div><div class="r">Draft status means the editor can delete and reorder. Full tree from the drawing, connect-note A/B, eHarmony fix, pacing rule and read dates into the manifest. Nothing here touches Email 1, 2 or the breakup.</div></li>
<li class="hold"><div class="n">H</div><div class="t">Hold: phone sourcing above the test</div><div class="o">your go</div><div class="r">The full pass is [estimate] 700 to 1,100 credits over the wave, well past the 200 line. It runs in batches that stay a week ahead of the launch pace, each on your word, and stops the day the ZoomInfo route comes through.</div></li>
<li class="hold"><div class="n">H</div><div class="t">Hold: sender switch and any start</div><div class="o">your hands only</div><div class="r">lemwarm confirmed in the UI on nathan.belfield@intradiemhq.com, readiness check green again after the structure changes, Nate's daily email limit confirmed, then Net-New and DWO move to the warm mailbox. No campaign starts, no gate moves, without your explicit go.</div></li>
<li><div class="n">8</div><div class="t">Start order when the go comes</div><div class="o">you, one at a time</div><div class="r">Insurance, Healthcare Payer, BPO (after Frank's Maximus heads-up), then Stars and Blitz on Nate's word, then Net-New on the warm mailbox, then DWO paced at 15 to 20 leads a day with phones a week ahead. Readiness check before each start. Second Look campaigns get built once the first breakups have gone out.</div></li>
</ol>
</div></section>

<section><div class="wrap"><div class="eyebrow">UI sheet</div><h2>Click by click for what the API refuses</h2><p class="lede">Grounded in lemlist's help center as of Sep 4 2026 (articles: delete or skip steps, skip a step for all leads, conditions, LinkedIn voice messages, A/B test a step, disable tracking). Labels marked <span class="confirm">confirm</span> are ones the docs describe in prose rather than quote; if your screen differs, stop and send the screen.</p>
<div class="ui">
<h3>A. Skip a step for all leads (Resurrection x2, Hartford x1, BO customer x2 each, Net-New x2)</h3>
<ol><li>Open <b>Campaigns</b> in the left sidebar, open the campaign, click the <b>Sequence</b> tab.</li>
<li>Find the step by its title (the stray steps are titled "STRAY STEP from an API test (Dallas): delete this step, it does nothing"; the BO root steps are "LinkedIn message for {{firstName}} (approve before sending)" and "Call {{firstName}} (CLEARED NAMES ONLY, check owner_cleared first)").</li>
<li>Open the three-dots menu on the step. Because leads have already been reviewed, the Delete action reads <b>Skip this step for all leads</b>. Click it.</li>
<li>A confirmation modal shows how many leads are affected. Click <b>Skip for X leads</b>. Skipping is irreversible; the step greys out with a <b>Skipped</b> badge and stays visible for reporting.</li>
<li>Order trap: on the BO lanes, skip the root LinkedIn message and root call only AFTER the agent has confirmed the branch versions exist.</li></ol>
<h3>B. Add a manual voice note inside the Accepted branch (Resurrection; optional on BO Net-New)</h3>
<ol><li>Sequence tab, find the accepted-connect condition, click into the <b>Yes</b> path after the LinkedIn message step.</li>
<li>Click <b>Add step</b>, choose <b>Voice message</b> (LinkedIn). Not "AI Voice message"; that path needs a cloned voice and Jason's exception.</li>
<li>In the step, choose Nate as the sender. Under the audio area, toggle the step to a manual task <span class="confirm">confirm label: "Mark as manual"</span>, set the title "Voice note {{firstName}}: read voice_script in the body" and priority Medium.</li>
<li>Set the delay to 1 day after the LinkedIn message. Leave the invite-fallback field empty (these leads are already connected).</li>
<li>Nate records per lead in the <b>Launch</b> section when the task comes up.</li></ol>
<h3>C. Connect-note A/B if the API refuses it (BO x5, DWO)</h3>
<ol><li>Sequence tab, open the LinkedIn connect step, click the <b>A/B test</b> icon on the step.</li>
<li>Choose <b>Duplicate Variant A</b>, click <b>Create variant B</b>.</li>
<li>Use the tabs at the top to switch to <b>Sequence B</b>, open the connect step there and paste the note (under 300 characters, references the email): "Hi {{firstName}}, shot you a note by email about [topic], thought this might be quicker. Nathan, Intradiem". On DWO, variant A already carries the note, so variant B is the blank one.</li>
<li>Never click "choose winner" on any campaign until the read date; the winner pick is permanent and ends A/B for that campaign.</li></ol>
<h3>D. Tracking off if the settings tool is refused</h3>
<ol><li>Open the campaign, click the <b>Settings</b> (gear) icon, open <b>Tracking</b> <span class="confirm">confirm tab name</span>.</li>
<li>Turn off <b>Track opens</b> and <b>Track clicks</b>. Leave reply tracking on. Repeat on the seven campaigns.</li></ol>
<h3>E. Before the sender switch (your hands, not part of any go)</h3>
<ol><li>Click your name bottom-left, <b>Settings</b>, <b>Sending settings</b>, expand <b>Email</b>.</li>
<li>On nathan.belfield@intradiemhq.com confirm lemwarm shows active with a deliverability score and at least three weeks of warm-up. Note Nate's daily email limit on the same screen.</li>
<li>Only then, in the Net-New and DWO campaigns, change the sender to the intradiemhq.com mailbox (or let the agent do it with set_campaign_senders on your go) and rerun the readiness check.</li></ol>
</div>
</div></section>

<div class="foot"><svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg><span>Intradiem GTM Engineering · Nate campaign structure review · Sep 4 2026 · Dallas only · nothing sending</span></div>
</div></body></html>'''
os.makedirs(os.path.dirname(OUT),exist_ok=True)
open(OUT,'w').write(page)
print(OUT, len(page))
