# Lemlist Per-Lead Variable Stage (Jul 31 2026)

Personalization variables for the 17 fresh-pool contacts (15 Finance, 2 Quality), written per lead from the locked load lists in Lemlist_Trial_Build_Review_Jul31.md section 9. These load as lemlist `customVariables` at lead-load time; the sequence steps reference them as {{opener_line}}, {{contract_line}}, {{vm_hook}}, {{voice_script}}.

Rules honored (re-swept Jul 31 night against the full copy-sharpener guardrails after Dallas's corrections; spoken-register re-sweep Aug 2 against the say-it-out-loud bar in automation/config/action_brief_format.md SPOKEN VOICE, with the 8 loaded Finance leads updated in Lemlist to match): zero Intradiem stats (trial claims discipline), no fabricated plan facts (only qbp_avg from the locked list plus soft, public plan characterizations), no em dashes, contractions throughout, house CTA form ("thought it might be worth [topic]" / "worth [topic]?"), BANNED: "comparing notes" in any form, "leverage"/"lever" family, voice notes naming the company (voice notes open "it's Nathan Belfield", first and last name only), notes on connection requests (invites always go blank). Every voice script ends on a soft question. Voice scripts contain no {{firstName}} tokens on purpose: lemlist does not resolve variables nested inside variable values. Aug 6 2026 seam pass (seam-v1.0, motions/shared/Variable_Seam_Contract_Aug6.md): all 16 live vm_hooks rewritten to stop restating the email (17/17 previously opened "I sent you a note about...") and to fit the voicemail budget (Finance 28 words, Quality 22); 7 contract_lines rewritten so the next fixed sentence's demonstrative resolves (Finance "those measures", Quality "that experience") and to stop pre-empting the template's own "keeping/holding steady" verb; 9 opener_lines de-echoed against their lane's fixed follow-on. Lead 12 (Miyasato) left untouched: removed from the campaign Aug 2, do not reload.

MERGE AT LOAD: first_name, email, job_title, linkedin_url come from the Clay Contacts export (same export that unblocks the Wave 1 de-dupe). Two contacts already have full records on file: Miyasato (heather_miyasato@hmsa.com, VP Health Finance) and Lynch (mlynch@solishealthplans.com, CFO). plan_name = the parent name used below unless the export shows a sharper plan-level name.

How each variable lands in the copy:
- opener_line completes "Hi {{firstName}}, {{opener_line}}" in E1 (starts lowercase, ends as a full sentence).
- contract_line is its own sentence inside E2's first paragraph.
- vm_hook is the reason-for-call sentence inside the voicemail and call scripts.
- voice_script is the full accepted-branch voice note (~20 seconds read aloud).

---

## FINANCE LANE (cam_2gy9hmEvMjYEuPZ8A)

### 1. Goldberg, Point32Health, qbp_avg 3.5
- opener_line: from the finance seat the 4.0 line is really a quality-bonus question, and Point32's book looks to be sitting at about 3.5, one half-star from the bonus turning on.
- contract_line: For a combined book like Harvard Pilgrim and Tufts sitting at 3.5, the half-star between here and 4.0 is revenue the plan still controls, and what decides it is a handful of customer-service measures.
- vm_hook: What I didn't put in writing is that the half-star is priced twice, once in the bonus and again in the rebate that funds next year's benefits.
- voice_script: Hey, it's Nathan Belfield, thanks for connecting. Short version of my note: Point32 looks to be about a half-star from the 4.0 bonus line, and the measures that still move this cycle are the service ones, decided in day-to-day service operations during peak weeks. If modeling that cliff is on your desk, worth fifteen minutes on it whenever it suits? Thanks.

### 2. Marrone, Point32Health, qbp_avg 3.5
- opener_line: one number kept my attention this week: 3.5. That's about where Point32's combined book sits on the weighted average, which puts the whole quality-bonus question inside a single half-star.
- contract_line: At 3.5, Point32 sits in the narrow band where this year still decides which side of the bonus line the book lands on, and the deciding weight sits in the service measures.
- vm_hook: The part worth a conversation is that a combined book moves as one, so the same half-star decision applies across Harvard Pilgrim and Tufts at once.
- voice_script: Hey, Nathan Belfield here, appreciate the connect. The reason I emailed: at roughly 3.5, Point32's combined book moves together once the service measures move, and that's happening in the live weeks, not in October. If that model crosses your desk, worth a short call sometime? Thanks.

### 3. Ingram, L.A. Care, qbp_avg 3.0
- opener_line: for a safety-net book the size of L.A. Care's, sitting near 3.0, every half-star on the way back to 4.0 carries real bonus and rebate money.
- contract_line: For L.A. Care, holding the service measures steady through the fall peak is what keeps the next half-star in reach before the window closes.
- vm_hook: For a safety-net book at 3.0 the first half-star doesn't pay by itself, it's what makes the second one reachable while the service measures are still live.
- voice_script: Hey, it's Nathan Belfield, thanks for connecting. My note in one line: for a book like L.A. Care's, around 3.0, the quickest star points sit in the service measures, and they're scored on what happens in service operations between now and December. Worth a short walk through the finance view sometime? Thanks.

### 4. Martin, Baystate Health, qbp_avg 3.0
- opener_line: a provider-owned book like Baystate's near 3.0 is the classic case where the bonus math turns on how service runs during the busiest weeks of the year.
- contract_line: For a provider-owned plan, the service measures are also the ones the health system side feels first, which makes them the natural place to start the model.
- vm_hook: For a provider-owned plan the service side shows up on the health system's numbers too, which usually changes who ends up funding the work.
- voice_script: Hey, it's Nathan Belfield, thanks for the connect. Quick context: for a provider-owned book near 3.0, the fastest star points are the service measures, and they're decided in live weeks during peak volume, not on the October release. If the cliff model is on your plate this quarter, worth a short call? Thanks.

### 5. Rains, Cambia, qbp_avg 3.0 (both contracts exactly 3.0)
- opener_line: what stood out on Cambia's book is that both contracts sit at 3.0 exactly, so the average isn't hiding anything, and the whole book would move together on a single push.
- contract_line: With both Cambia contracts at 3.0, one improvement in the service measures moves the entire book at once, and it's rare for one initiative to carry that much.
- vm_hook: Two contracts sitting on the same number is unusual, and it means one initiative carries the whole book rather than half of it.
- voice_script: Hey, it's Nathan Belfield, appreciate you connecting. The thing that caught my eye: both of Cambia's contracts sit at exactly 3.0, so one push in the service measures moves the whole book together. That's a rare setup. If the star model is in your world, worth fifteen minutes sometime? Thanks.

### 6. Qin, Blue Shield of California, qbp_avg 3.5
- opener_line: at about 3.5, Blue Shield of California is inside the band where one half-star decides whether the quality bonus turns on at all.
- contract_line: For a book Blue Shield's size the dollars on that half-star are large enough to make it a finance decision rather than a quality one, and they turn on the service measures.
- vm_hook: At Blue Shield's enrollment the half-star is large enough that it stops being a quality budget question and starts being a finance one.
- voice_script: Hey, Nathan Belfield here, thanks for connecting. My note in short: Blue Shield sits about a half-star from the 4.0 bonus line, and that half-star lives in the service measures being scored right now, in the live weeks. If you're modeling that exposure, worth fifteen minutes on it? Thanks.

### 7. Hoenstine, Zing Health, qbp_avg 2.5
- opener_line: at about 2.5, Zing's star position reads less like a bonus question and more like a trajectory question, and the fastest points on the board are the ones scored week to week.
- contract_line: For a book at 2.5, every half-star recovered this cycle compounds into the next one, and the service measures are where recovery shows up first.
- vm_hook: From 2.5 the question is trajectory rather than one cycle, and the service side is the only part that compounds inside a single measurement year.
- voice_script: Hey, it's Nathan Belfield, thanks for the connect. Straight version: from 2.5, the fastest recovery is in the service measures, the ones scored in the live weeks. Clinical measures usually take years to shift, and these move inside one cycle. If the climb-back plan is yours to model, worth a short call? Thanks.

### 8. Thornton, Clover Health, qbp_avg 3.5
- opener_line: at roughly 3.5, Clover sits one half-star from the bonus line, and for an MA-focused book that bonus is a bigger share of the economics than it is for a diversified payer.
- contract_line: For a book this concentrated in Medicare Advantage the half-star decides the bonus, and the bonus is a large enough share of the economics to justify working the service measures directly.
- vm_hook: The awkward part for an MA-focused book is that the bonus and the rebate fund the benefits you compete on, so a missed cycle shows up in enrollment.
- voice_script: Hey, it's Nathan Belfield, appreciate the connect. Short version: Clover's about a half-star off the bonus line, and for a book as MA-focused as Clover's that half-star is real money. The measures that still move it this cycle are service measures, decided in the live weeks. If it's on your desk, worth a few minutes on it sometime? Thanks.

### 9. Chio, IEHP, qbp_avg 3.0
- opener_line: for a safety-net book like IEHP's near 3.0, the star question and the member-experience question turn out to be the same question.
- contract_line: For IEHP specifically, the service measures move both the rating and the member experience the mission is built on, which usually makes them the easiest initiative to fund.
- vm_hook: What's different about a public plan is that the rating and the rate-setting conversation tend to land on the same desk in the same year.
- voice_script: Hey, it's Nathan Belfield, thanks for connecting. The note I sent boils down to this: near 3.0, IEHP's fastest star points are the service measures, and they're scored on day-to-day service performance between now and December. Worth a short call whenever it's useful? Thanks.

### 10. Battersby, Community Health Plan of Washington, qbp_avg 3.0
- opener_line: Community Health Plan of Washington's book near 3.0 is right in the range where the next rating is still genuinely undecided.
- contract_line: For CHPW, the service measures are the points that can still move before the window closes, and they're the first to slip when fall volume hits.
- vm_hook: For CHPW the constraint is how many peak weeks are left in the measurement year, and that count only goes one way from here.
- voice_script: Hey, it's Nathan Belfield, thanks for the connect. One-line version of my note: CHPW's nearest star points are operational, scored in the live weeks between now and December, and they're the first thing to slip under fall volume. If that model's on your plate, worth a short call? Thanks.

### 11. Faulring, Community Health Plan of Washington, qbp_avg 3.0
- opener_line: the number that got my attention on Community Health Plan of Washington was 3.0, close enough that this measurement year still decides which direction the rating moves.
- contract_line: At 3.0, CHPW doesn't need a multi-year clinical program to move; it needs the service measures held steady through the exact weeks when they usually slip.
- vm_hook: At 3.0 the honest framing is trajectory, because the first half-star doesn't pay, it just decides whether the second one is reachable next cycle.
- voice_script: Hey, it's Nathan Belfield, appreciate you connecting. Why I emailed: at 3.0, CHPW's rating direction is still live this cycle, and the deciding measures are the service ones, scored week by week under peak-season volume. If that's your model to build, worth a fifteen-minute walk through it? Thanks.

### 12. Miyasato, HMSA, qbp_avg 3.5 — REMOVED Aug 2 2026 (left HMSA; CFO at Kupu since June 2026 per LinkedIn; lead deleted from the Finance campaign, do not reload)
- opener_line: at about 3.5, HMSA sits one half-star from the 4.0 bonus line, and the measures still movable this measurement year are the operational ones, not the clinical ones.
- contract_line: For HMSA, holding service steady through the fall peak is what decides which side of the bonus line the book lands on before the number ever publishes.
- vm_hook: I sent you a note about HMSA sitting near 3.5, half a star from the quality bonus. The points that can still move this cycle are mostly operational ones, and that's the part I wanted to talk through with you.
- voice_script: Hey, it's Nathan Belfield, thanks for connecting. The short version: HMSA's about a half-star from the bonus line, that half-star lives in the service measures, and those are decided in the live weeks between now and December. Worth fifteen minutes on the finance view whenever it suits? Thanks.

### 13. Yang, NYC Health + Hospitals, qbp_avg 3.5
- opener_line: at roughly 3.5, the Health + Hospitals book sits one half-star from the bonus line, and for a safety-net plan, bonus dollars carry more weight in the budget than they do almost anywhere else.
- contract_line: For a public-system book, that half-star is one of the few revenue paths that doesn't require new membership or new rates, just execution in the service measures.
- vm_hook: On safety-net books the bonus usually carries more weight in the budget than it does at a commercial payer, so a missed cycle gets felt sooner.
- voice_script: Hey, it's Nathan Belfield, thanks for the connect. Short version: the book sits about a half-star from the 4.0 bonus line, and for a safety-net plan that bonus is one of the cleanest paths to new revenue there is. The deciding measures are operational, scored in the live weeks. Worth a short call sometime? Thanks.

### 14. Lynch, Solis Health Plans, qbp_avg 3.5 (record on file: mlynch@solishealthplans.com, CFO)
- opener_line: at about 3.5, Solis is one half-star from the 4.0 bonus line, and for an MA plan Solis's size, clearing that line changes how much rebate flows into next year's benefits.
- contract_line: For a book Solis's size, clearing 4.0 this cycle changes next year's benefit economics, and the part still in play between now and December is the service measures.
- vm_hook: For a plan competing on benefits, the rebate side of the bonus matters more than the bonus itself, and it's decided on the same measures.
- voice_script: Hey, it's Nathan Belfield, appreciate the connect. The reason I emailed: Solis is about a half-star from the bonus line, and clearing it feeds straight into next year's benefits and enrollment. The deciding measures are the service ones, scored in live weeks. Worth fifteen minutes whenever it works? Thanks.

### 15. Huang, CalOptima, qbp_avg 3.0
- opener_line: for a county-organized book like CalOptima's near 3.0, the next half-star is mostly an execution question in the service measures, and it's being decided in this measurement year.
- contract_line: For CalOptima, the service measures carry double weight: they move the rating and they're the member experience a public plan answers for.
- vm_hook: CalOptima's size means each half-star is a budget-scale number rather than a rounding one, and from 3.0 the climb needs its own workstream to happen at all.
- voice_script: Hey, it's Nathan Belfield, thanks for connecting. One line: near 3.0, CalOptima's quickest star points are the service measures, decided in day-to-day operations between now and December, not on the October release. Worth a quick walk through it sometime? Thanks.

---

## QUALITY LANE (cam_viEbB6HkYsCPtxKbi)

### 16. Pedro Rivera, NYC Health + Hospitals, qbp_avg 3.5
- opener_line: your weighted average looks to be right around 3.5, and for a safety-net book that's close enough that the last half-star to 4.0 is genuinely in play this cycle.
- contract_line: On a book near 3.5 those are the measures that carry the member's actual experience of the plan, and they're settled in the busiest weeks of the year.
- vm_hook: The part I'd want your read on is which CAHPS items your own data says sit closest to a cut point.
- voice_script: Hey, it's Nathan Belfield, thanks for connecting. My note in one line: at about 3.5, the last half-star to 4.0 sits in the CAHPS and service measures, and those are being scored right now, in the live weeks. Thought it might be worth walking through which measures usually decide it for a book like yours. Fifteen minutes sometime? Thanks.

### 17. Andrew Breuckman, Community Health Plan of Washington, qbp_avg 3.0
- opener_line: Community Health Plan of Washington's weighted average looks to be right around 3.0, which is close enough that the next half-star is still genuinely winnable.
- contract_line: At 3.0 CHPW's rating direction is still live, and what moves it is the everyday experience members have when they need something from the plan, which is the first thing to give under load.
- vm_hook: What I'd ask is whether your service measures hold through the fall peak or quietly give back what the spring earned.
- voice_script: Hey, it's Nathan Belfield, appreciate the connect. Quick context: at about 3.0, CHPW's next half-star is decided in the customer-service measures, and they're scored on day-to-day service performance between now and December. Worth fifteen minutes to walk through which measures usually move first? Thanks.

---

## Load notes (premortem fixes baked in, Jul 31 night)

- Resurrection (cam_sh3JCJoxtEHyjGrsw) needs none of these: its copy uses only {{firstName}} and {{plan_name}}.
- Load call shape per lead: `add_leads_to_campaign` with `customVariables: {opener_line, contract_line, vm_hook, voice_script, plan_name, qbp_avg}`. Lemlist fails closed on a missing variable (lead flags for review instead of sending a blank).
- **Phone coverage (premortem failure #2 fix):** load fresh-pool leads with `findPhone: true` (credits per successful find, ~17 leads, budget the spend against the 200 trial credits before voice notes). Resurrection: merge Connor's ~50 ZoomInfo cells FIRST, findPhone only the gaps. Report phone-coverage % in the pre-load counts; under ~50% the multichannel story is thin and Dallas should see the number before Start.
- **LinkedIn safety (premortem failure #3 fix):** comment-last-post steps are OUT of the standard (auto-only in lemlist, cannot be manual-approved; replaced with a second profile visit in Finance no-phone). At the moment Nate's LinkedIn connects, set conservative daily LinkedIn action caps in his sender settings BEFORE Start; that setting does not exist until the account is connected. Nate's explicit consent to the voice clone is required before any AI voice note step is armed.
- **Voice note swap procedure:** update_sequence_step cannot change recordMode; the swap to Nate's AI clone = delete the manual voice-note step and re-add with recordMode "ai" + voiceId + message "{{voice_script}}" + manual true, same index and delay. Finance: stp_9YLwdR5Rrt6eAvXns (seq_Mtnqt8s9LKr9bKnpD, index 2, d1). Quality: stp_LumCYdLyCLbM5ssPX (seq_FKqfv2325wMmz8Dtc, index 2, d1).
- **Runway rule (premortem failure #1 fix):** the 10-business-day sequence needs Start no later than Aug 3-4 to finish inside the trial (ends ~Aug 13). Standing fallback: if Nate's channels aren't connected by Mon Aug 3, activate Nate's untouched free trial as the workspace that day.
- Nothing loads until: Nate's channels connect, the Wave 1 export lands (de-dupe + name/email merge), and Dallas eyeballs rendered emails in the Leads tab. Launch stays Dallas's hand.
