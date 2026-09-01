# Stars - Resurrection (Nate): AI voice step, setup sheet (your hands)

Written Aug 31 2026. Campaign `cam_sh3JCJoxtEHyjGrsw`, 43 leads, status Draft/paused, sender Nathan Belfield (voice already cloned in lemlist). Grounded in lemlist's help articles read Aug 31 (Send AI voice messages on LinkedIn, Add LinkedIn steps, Reorder steps, Conditions) and the API reference. Labels quoted from those docs; anything marked (confirm) is a label I could not verify and you should read off the screen. Everything below is in order; do not skip ahead.

Why this is a sheet and not done already: the lemlist API accepts `linkedinVoiceNote` steps only on a campaign's root sequence, not inside a condition branch, and the voice note has to live in the "Accepted invite" branch (LinkedIn voice messages only reach 1st-degree connections). Two probe steps I created while testing could not be deleted through the API ("you already reviewed some leads"); they are labeled STRAY and Part 1 removes them.

Flags, status Aug 31 evening:
- Jason Jones (AI security) kept AI voice out of the initial lemlist pilot on Aug 13. An exception ask with the guardrails (Nathan's own cloned voice, fixed script, preview and approval per send, 1st-degree connections only) is sitting as a Slack draft in your DM with Jason; send it as is or edit first. Treat his reply as the launch gate for this step.
- MetroPlus lead: `plan_name` already set to "MetroPlus" by API. Done.
- AI voice cost: 5 lemlist credits per send, ceiling 215 for 43 leads, realistic far lower. Nothing to do.

Alternative to Parts 1 and 2 that I can run by API on your explicit go: pull the 43 leads out of the campaign (their full records are snapshotted), which lifts lemlist's "reviewed leads" lock, delete the two strays, add the voice step, then reload the 43 with all variables. Leads come back un-reviewed, so you would review them again before launch. The permission classifier blocked that bulk removal today; to take this route, paste: "Go ahead with the pull-out and reload on Stars - Resurrection to place the voice step by API."


## What is already in place (done by API, Aug 31)

- Every lead has a LinkedIn URL; four departed or out-of-motion contacts removed (47 to 43).
- The MetroPlus lead's `plan_name` set to "MetroPlus" so the voice reads it correctly (was "Health + Hospitals").
- The day 1 LinkedIn message still carries its ORIGINAL copy. The rewritten version that references the voice note is in Part 3 and goes in only after the voice step exists.

Current accepted-invite branch ("Yes path" under "Accepted invite"), top to bottom:
1. LinkedIn message after accepted connect (approve before sending), Wait 0
2. Call {{firstName}} ({{plan_name}}), they accepted the connect, Wait 1
3. Email "eating my words", Wait 3
4. STRAY STEP from an API test (Dallas): delete this step, it does nothing (manual task)

Root sequence, after the "Accepted invite" condition:
- STRAY STEP from an API test (Dallas): delete this step, it does nothing (Voice message, manual record mode)


## Part 1: delete the two stray steps (about 1 minute)

lemlist's rule: steps can be deleted only while the campaign is in Draft. This campaign shows Draft in the campaign list, so the UI should allow it even though the API refused.

1. Campaigns, open `Stars - Resurrection (Nate)`, open the Sequence tab (confirm tab name).
2. In the Yes path under "Accepted invite", find the last step titled `STRAY STEP from an API test (Dallas): delete this step, it does nothing`. Open the step's menu (three dots or trash icon, confirm) and delete it. If lemlist warns about leads already in the campaign, confirm; the step has never fired.
3. Scroll to the root of the sequence, below the "Accepted invite" condition block. Delete the second step with the same STRAY title (it shows as a Voice message step).
4. If either delete is refused, stop here and tell me the exact message on screen. Fallback is a duplicate of the campaign in Draft, which I would rather not do while leads are loaded.


## Part 2: add the AI voice step at the top of the Yes path (about 3 minutes)

Prerequisites already met per the help article: Multichannel Expert or Enterprise plan, Nathan's LinkedIn connected to lemlist, Nathan's voice cloned.

1. In the Yes path under "Accepted invite", use the add control ABOVE the first step `LinkedIn message after accepted connect` (the "+" between the condition and that step, confirm). If the "+" only appears below existing steps, add the step at the bottom and drag it to the top using the drag handle on the left of the step (lemlist supports drag reorder in Draft).
2. Choose `AI Voice message` (help article label; the plain `Voice message` is the manual-recording step, not this one).
3. Paste the script from Part 4 into the script field. Variables `{{firstName}}` and `{{plan_name}}` are populated on all 43 leads; no URL variables are used (lemlist does not support them in voice scripts).
4. `Sender assignment` (help article label): set Nathan as the LinkedIn sender for this step so his cloned voice is used.
5. Set the wait to 0 days (`Wait for…`, confirm): the note lands the same day the connection is accepted, while they are on LinkedIn looking at Nathan.
6. Preview one lead (the article allows up to 15 free previews a day). Listen for: the pause after the first name, "MetroPlus", "CalOptima", and "Point32" read cleanly, and total length around 28 to 30 seconds. If a plan name reads badly, tell me the lead and I will adjust its `plan_name` by API.
7. Keep the step on the same approve-before-sending posture as the other LinkedIn steps in this campaign (confirm the toggle name on screen).
8. After adding, read the `Wait for…` value on every step in the Yes path. lemlist recalculates waits when steps move. Target: voice 0, LinkedIn message 1, call 1, email 3.

Cost: the help article states AI voice sends at 5 lemlist credits per message. Only leads that accept the connect reach this step, so the ceiling is 43 x 5 = 215 lemlist credits and the realistic number is far lower. This is lemlist credit, not Clay.


## Part 3: after the voice step exists (mine, on your go)

Do nothing here until Part 2 is done. Paste this back to me and I will apply the day 1 copy by API and re-read the branch to confirm order and waits:

> Voice step is in the Yes path of Stars - Resurrection. Apply the day 1 LinkedIn DM copy and set its wait to 1, then verify the branch.

The DM copy that will go in (passed the copy review Aug 31):

> Left you a quick voice note yesterday, {{firstName}}, so here's the short version in writing. The measures that still move the last half-star at {{plan_name}} this cycle are being scored in live interactions right now, and the cheap fixes close when the window does. Have 15 minutes this week or next to see which contracts sit closest to the line?


## Part 4: the voice script (Nathan's voice, about 28 seconds)

Passed the verified-claims gate (no figures, no customer outcomes) and the copy review Aug 31. One idea: the measures that still move this cycle are being scored in live interactions right now, and the cheap fixes disappear when the window closes.

> {{firstName}}, thanks for connecting, it's Nathan. I emailed a few weeks back about the last half-star at {{plan_name}}. The measures still movable this cycle are being scored in live interactions right now, and the cheap fixes close when that window does. You'll know each contract better than I do, but give me fifteen minutes and I'll show you which ones sit closest to the line. If it's already handled, just say so. Thanks {{firstName}}.

Why here and not elsewhere: acceptance is the one moment in this sequence where the lead is guaranteed to be on LinkedIn with Nathan's name in front of them, and a voice note in a fresh connection is heard where a text DM is skimmed. The text DM a day later is the written short version, so the ask exists in text for anyone who never plays audio. The no-accept path cannot carry a voice note (not connected), so it stays call, email, condition.


## Ordering traps

- Part 1 before Part 2: two stray steps in the same branch make the drag-to-top step easy to misplace.
- Part 2 before Part 3: the day 1 DM copy says "left you a voice note yesterday"; it is a lie until the voice step exists, which is why it was reverted.
- Do not launch between Part 2 and Part 3; the current DM copy at wait 0 would fire on the same day as the voice note with overlapping words.
- After any drag, re-read every `Wait for…` in the branch (step 8). lemlist changes them silently.
