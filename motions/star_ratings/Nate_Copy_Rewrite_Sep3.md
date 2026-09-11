# Nate campaign copy rewrite (Sep 3 2026)

> Every email, LinkedIn message and call script on the four paused campaigns plus the Quality draft, rewritten under the Sep 3 doctrine in plain spoken language. Each Email 1 opens on the plan's own CMS number or the account's public signal, says who Intradiem is and what it does by the second paragraph, carries one verified proof, and ends on one question with no calendar in it. Paragraphs are separated by real blank lines in lemlist. Campaigns stay paused until Nate has read this.


## Status after the lemlist apply (Sep 3 2026, third pass)

- Third pass: every email rewritten in plain spoken language after Dallas's read. Gone: "in one line, in case the first note didn't land", "the scoring window has kept closing since, which is the only reason I'm back", "the ground between", "the seam I work", "I'm easy to find". Every paragraph now sits on its own line with a blank line between, the way lemlist's editor stores it, so nothing bunches.
- Every email, LinkedIn message and call script on this page is live in the lemlist steps, both A/B variants on the Finance, Quality, Hartford and Citizens Email 1s. All four running campaigns stay paused. Quality was already a draft.
- Both public signals verified Sep 3 against the source: The Hartford's Q2 2026 earnings call (AI completing underwriting work in a fraction of the time, no KPIs disclosed for claims and service) and Citizens' Q1 2026 call (25 percent of calls answered by non-humans by end of 2026, on the way to 50 percent by fall 2027).
- One exception: lemlist refused the variant B rewrite on the Resurrection "just tried you" step on every attempt (SEQUENCE_AB_CAMPAIGN_RUNNING despite the pause). Variant A carries the new copy; variant B still carries the old body. Before restarting Resurrection, open that step in the lemlist UI and pick variant A as the winner, or paste the variant B text from this page.
- The pre-rewrite copy of every step is saved next to this file as `Lemlist_Sequences_Backup_PreRewrite_Sep3.json`.
- Nothing restarts until Nate has read this page and Dallas presses Start.

## Stars - Fresh Pool / Finance (Nate)

### Email 1 (A/B)
**Subject:** `the bonus line at {{plan_name}}`

> Hi {{firstName}},
> 
> On the latest CMS release, {{plan_name}}'s Medicare Advantage book looks to be sitting near {{qbp_avg}}. You'll know the exact number better than I do. From the finance side, that's a quality bonus question. The bonus turns on at 4.0, and most of what stands between you and 4.0 is customer service measures. Those are cheaper to move than the clinical ones, and they're being scored right now.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service centers already run and keeps adherence and handle time steady during the day, while those calls are being scored. Humana has it on the record: handle time down 45 seconds and a 7X return five years in.
> 
> I'm not making a Stars claim. We move the service operation, and the measures follow.
> 
> Worth a conversation on what it costs to close the gap to 4.0 versus what the bonus pays?
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

*171 words*

**Variant B (offer note close):**

> Hi {{firstName}},
> 
> On the latest CMS release, {{plan_name}}'s Medicare Advantage book looks to be sitting near {{qbp_avg}}. You'll know the exact number better than I do. From the finance side, that's a quality bonus question. The bonus turns on at 4.0, and most of what stands between you and 4.0 is customer service measures. Those are cheaper to move than the clinical ones, and they're being scored right now.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service centers already run and keeps adherence and handle time steady during the day, while those calls are being scored. Humana has it on the record: handle time down 45 seconds and a 7X return five years in.
> 
> I'm not making a Stars claim. We move the service operation, and the measures follow.
> 
> Would it help if I sent over a short note on how plans near the line weigh that cost against the bonus? No meeting attached, I'll just send it.
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

### LinkedIn message after connect
> Thanks for connecting, {{firstName}}. Short version of my email: {{plan_name}}'s book looks to be near {{qbp_avg}}, the bonus turns on at 4.0, and the points that can still move this cycle are the customer service ones. Intradiem keeps those steady during the day on top of the WFM you already run. Worth a conversation on what closing the gap costs versus what the bonus pays?

### Call 1 (no voicemail)
> Call 1 of 2. If no answer, hang up, no voicemail (that comes with call 2).
> 
> OPENER, four beats, then stop talking:
> 1) Say their first name. Pause.
> 2) "It's Nathan Belfield at Intradiem."
> 3) "We connected on LinkedIn this week. {{vm_hook}}"
> 4) "Can I take 30 seconds, and you tell me if it's not for you?"
> 
> IF THEY ENGAGE (20 to 30 seconds): "The bonus turns on at 4.0, and most of what stands between the book and 4.0 is customer service measures. Intradiem sits on top of the WFM and phone system your service centers already run and keeps adherence and handle time steady during the day, while those calls are being scored. Humana has it on the record with handle time down 45 seconds." Then hand them the floor: "Is the bonus line in your model this cycle?"
> 
> THE ASK: "Fifteen minutes and I'll walk you through what it costs to close the gap to 4.0 versus what the bonus pays. If it's already handled, I'll say so and leave you alone."
> 
> ON A YES: lock the slot on the call, two concrete options.
> 
> IF BUSY: "Completely get it. Ten seconds so you know what this was: {{vm_hook}} When's better this week?"
> 
> IF BRUSH-OFF: accept it immediately. "Fair enough. One thing before I go: is that because it's already handled, or just not the priority right now?" Then thank them and stop.

### Call 2 (voicemail)
> Call 2 of 2. If no answer, leave this voicemail, under 30 seconds, warm, unhurried:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service centers already run and keeps the service measures steady while they're being scored. Humana has handle time down 45 seconds with it. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER, four-beat opener (skip the LinkedIn reference), then the same flow as call 1: the bonus line, what Intradiem does, the Humana number, hand them the floor, the 15-minute ask with the honest-exit clause.

### Email 2 (connect branch)
**Subject:** `re: the bonus line at {{plan_name}}`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's still open is next year's rating, and that's being scored in the busy weeks between now and December. So the window to move the service measures at {{plan_name}} is this fall, not next spring.
> 
> If the gap to 4.0 is in your model at all, it's cheaper to start before the fall volume hits than after. Intradiem runs on top of what you already have, so it can start inside that window.
> 
> Would twenty minutes on the finance side be useful? What it costs to hold the line versus what the bonus pays.
> 
> Nathan

*120 words*

### Email 3 breakup (connect branch)
**Subject:** `re: the bonus line at {{plan_name}}`

> Hi {{firstName}},
> 
> I'll stop here. If the quality bonus becomes a live question at {{plan_name}}, this cycle or next, reach out. I'd start with the contracts closest to the line.
> 
> Good luck with the fall.
> 
> Nathan

*37 words*

### Voicemail (no connect)
> Dial, and if no answer leave this voicemail, under 30 seconds:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service centers already run and keeps the service measures steady while they're being scored. Humana has handle time down 45 seconds with it. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER: four beats (first name, "It's Nathan Belfield at Intradiem", "I sent you a note this week. {{vm_hook}}", "Can I take 30 seconds?"), then the bonus line, what Intradiem does, the Humana number, and the 15-minute ask. Brush-off: accept it, one either-or question, release warmly.

### Call day after voicemail
> Call, the day after the voicemail. If no answer, hang up, no second voicemail.
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I left you a note yesterday on the bonus line at {{plan_name}}. {{vm_hook}} Intradiem keeps the service measures steady during the day on top of the WFM you already run. Worth 15 minutes on what closing the gap costs versus what the bonus pays?" If busy, trade up to a real slot this week.

### Email 2 (no-connect branch)
**Subject:** `re: the bonus line at {{plan_name}}`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's still open is next year's rating, and that's being scored in the busy weeks between now and December. So the window to move the service measures at {{plan_name}} is this fall, not next spring.
> 
> If the gap to 4.0 is in your model at all, it's cheaper to start before the fall volume hits than after. Intradiem runs on top of what you already have, so it can start inside that window.
> 
> Would twenty minutes on the finance side be useful? What it costs to hold the line versus what the bonus pays.
> 
> Nathan

*120 words*

### Final call
> Final call, no voicemail (one already left).
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I'll be quick. I've sent a couple of notes on the quality bonus line at {{plan_name}}. Before I close the file: is the bonus a this-cycle question for your team, or a next-year one? Either answer is useful."
> 
> If next year, ask permission to come back in the spring. If this cycle, lock 15 minutes on the call with two concrete options.

### Email 3 breakup (no-connect branch)
**Subject:** `re: the bonus line at {{plan_name}}`

> Hi {{firstName}},
> 
> I'll stop here. If the quality bonus becomes a live question at {{plan_name}}, this cycle or next, reach out. I'd start with the contracts closest to the line.
> 
> Good luck with the fall.
> 
> Nathan

*37 words*

### Email 2 (no-LinkedIn branch)
**Subject:** `re: the bonus line at {{plan_name}}`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's still open is next year's rating, and that's being scored in the busy weeks between now and December. So the window to move the service measures at {{plan_name}} is this fall, not next spring.
> 
> If the gap to 4.0 is in your model at all, it's cheaper to start before the fall volume hits than after. Intradiem runs on top of what you already have, so it can start inside that window.
> 
> Would twenty minutes on the finance side be useful? What it costs to hold the line versus what the bonus pays.
> 
> Nathan

*120 words*

### Email 3 breakup (no-LinkedIn branch)
**Subject:** `re: the bonus line at {{plan_name}}`

> Hi {{firstName}},
> 
> I'll stop here. If the quality bonus becomes a live question at {{plan_name}}, this cycle or next, reach out. I'd start with the contracts closest to the line.
> 
> Good luck with the fall.
> 
> Nathan

*37 words*


## Stars - Fresh Pool / Quality (Nate)

### Email 1 (A/B)
**Subject:** `the service measures at {{plan_name}}`

> Hi {{firstName}},
> 
> {{plan_name}}'s Medicare Advantage book looks to be sitting near {{qbp_avg}} on the latest CMS release. You'll know the exact picture better than I do. Between there and 4.0, the points that move fastest are usually the customer service measures, and those are being scored right now, this measurement year, not on the October release.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service centers already run and works during the day: it moves breaks and training into the quiet minutes and keeps adherence and handle time steady while calls are being scored. Humana has it on the record with handle time down 45 seconds.
> 
> I'm not making a Stars claim. We move the service operation, and the measures follow.
> 
> Worth a conversation on which of your contracts are closest to the line and what can still move this cycle?
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

*164 words*

**Variant B (offer note close):**

> Hi {{firstName}},
> 
> {{plan_name}}'s Medicare Advantage book looks to be sitting near {{qbp_avg}} on the latest CMS release. You'll know the exact picture better than I do. Between there and 4.0, the points that move fastest are usually the customer service measures, and those are being scored right now, this measurement year, not on the October release.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service centers already run and works during the day: it moves breaks and training into the quiet minutes and keeps adherence and handle time steady while calls are being scored. Humana has it on the record with handle time down 45 seconds.
> 
> I'm not making a Stars claim. We move the service operation, and the measures follow.
> 
> Would it help if I sent over a short note on which service measures usually decide it for a book near the line? No meeting attached, I'll just send it.
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

### LinkedIn message after connect
> Thanks for connecting, {{firstName}}. Short version of my email: {{plan_name}}'s book looks to be near {{qbp_avg}}, and the points that can still move this cycle are the customer service ones, scored on live calls between now and December. Intradiem keeps those steady during the day on top of the WFM you already run. Worth a conversation on your contracts closest to the line?

### Call 1 (no voicemail)
> Call 1 of 2. If no answer, hang up, no voicemail (that comes with call 2).
> 
> OPENER, four beats, then stop talking:
> 1) Say their first name. Pause.
> 2) "It's Nathan Belfield at Intradiem."
> 3) "We connected on LinkedIn this week. {{vm_hook}}"
> 4) "Can I take 30 seconds, and you tell me if it's not for you?"
> 
> IF THEY ENGAGE (20 to 30 seconds): "Between where the book sits and 4.0, the points that move fastest are usually the customer service measures, and they're being scored right now. Intradiem sits on top of the WFM and phone system your service centers already run and keeps adherence and handle time steady during the day, while those calls are being scored. Humana has it on the record with handle time down 45 seconds." Then hand them the floor: "Is that anywhere near how it looks from your seat?"
> 
> THE ASK: "Fifteen minutes and I'll walk you through which of your contracts are closest to the line and what can still move this cycle. If it's already handled, I'll say so and leave you alone."
> 
> ON A YES: lock the slot on the call, two concrete options.
> 
> IF BUSY: "Completely get it. Ten seconds so you know what this was: {{vm_hook}} When's better this week?"
> 
> IF BRUSH-OFF: accept it immediately. "Fair enough. One thing before I go: is that because it's already handled, or just not the priority right now?" Then thank them and stop.

### Call 2 (voicemail)
> Call 2 of 2. If no answer, leave this voicemail, under 30 seconds, warm, unhurried:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service centers already run and keeps the service measures steady while they're being scored. Humana has handle time down 45 seconds with it. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER, four-beat opener (skip the LinkedIn reference), then the same flow as call 1: the service measures, what Intradiem does, the Humana number, hand them the floor, the 15-minute ask with the honest-exit clause.

### Email 2 (connect branch)
**Subject:** `re: the service measures at {{plan_name}}`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's still open is next year's rating, and the customer service measures are scored in the busy weeks between now and December, which is also when they tend to slip.
> 
> Keeping them steady through those weeks is the whole job. Humana runs Intradiem on top of its WFM for exactly that, and gets about two hours back per agent per month, most of it going into coaching that used to wait for a quiet day.
> 
> Would twenty minutes be useful on which measures usually decide the next half-star for a book near your line?
> 
> Nathan

*120 words*

### Email 3 breakup (connect branch)
**Subject:** `re: the service measures at {{plan_name}}`

> Hi {{firstName}},
> 
> I'll stop here. If the next half-star at {{plan_name}} becomes a priority, this cycle or next, reach out. I'd start with the customer service measures on your contracts closest to the line.
> 
> Good luck with the fall.
> 
> Nathan

*42 words*

### Voicemail (no connect)
> Dial, and if no answer leave this voicemail, under 30 seconds:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service centers already run and keeps the service measures steady while they're being scored. Humana has handle time down 45 seconds with it. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER: four beats (first name, "It's Nathan Belfield at Intradiem", "I sent you a note this week. {{vm_hook}}", "Can I take 30 seconds?"), then the service measures, what Intradiem does, the Humana number, and the 15-minute ask. Brush-off: accept it, one either-or question, release warmly.

### Call day after voicemail
> Call, the day after the voicemail. If no answer, hang up, no second voicemail.
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I left you a note yesterday on the customer service measures at {{plan_name}}. {{vm_hook}} Intradiem keeps the service measures steady during the day on top of the WFM you already run. Worth 15 minutes on which of your contracts are closest to the line?" If busy, trade up to a real slot this week.

### Email 2 (no-connect branch)
**Subject:** `re: the service measures at {{plan_name}}`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's still open is next year's rating, and the customer service measures are scored in the busy weeks between now and December, which is also when they tend to slip.
> 
> Keeping them steady through those weeks is the whole job. Humana runs Intradiem on top of its WFM for exactly that, and gets about two hours back per agent per month, most of it going into coaching that used to wait for a quiet day.
> 
> Would twenty minutes be useful on which measures usually decide the next half-star for a book near your line?
> 
> Nathan

*120 words*

### Final call
> Final call, no voicemail (one already left).
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I'll be quick. I've sent a couple of notes on the next half-star at {{plan_name}}. Before I close the file: is the next half-star a this-cycle question for your team, or a next-year one? Either answer is useful."
> 
> If next year, ask permission to come back in the spring. If this cycle, lock 15 minutes on the call with two concrete options.

### Email 3 breakup (no-connect branch)
**Subject:** `re: the service measures at {{plan_name}}`

> Hi {{firstName}},
> 
> I'll stop here. If the next half-star at {{plan_name}} becomes a priority, this cycle or next, reach out. I'd start with the customer service measures on your contracts closest to the line.
> 
> Good luck with the fall.
> 
> Nathan

*42 words*

### Email 2 (no-LinkedIn branch)
**Subject:** `re: the service measures at {{plan_name}}`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's still open is next year's rating, and the customer service measures are scored in the busy weeks between now and December, which is also when they tend to slip.
> 
> Keeping them steady through those weeks is the whole job. Humana runs Intradiem on top of its WFM for exactly that, and gets about two hours back per agent per month, most of it going into coaching that used to wait for a quiet day.
> 
> Would twenty minutes be useful on which measures usually decide the next half-star for a book near your line?
> 
> Nathan

*120 words*

### Email 3 breakup (no-LinkedIn branch)
**Subject:** `re: the service measures at {{plan_name}}`

> Hi {{firstName}},
> 
> I'll stop here. If the next half-star at {{plan_name}} becomes a priority, this cycle or next, reach out. I'd start with the customer service measures on your contracts closest to the line.
> 
> Good luck with the fall.
> 
> Nathan

*42 words*


## Stars - Resurrection (Nate)

### LinkedIn message after connect
> Thanks for connecting, {{firstName}}. I emailed a few weeks ago about {{plan_name}}'s Medicare book and the customer service measures that still move next year's rating. Intradiem sits on top of the WFM you already run and keeps those measures steady while they're being scored. Worth a fresh look before the fall volume hits?

### Call after connect
> Call after the accepted connect. Leave as voicemail if no answer, under 30 seconds:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem, thanks for the connect. I emailed a few weeks ago about {{plan_name}}'s Medicare book and the customer service measures that still move next year's rating. Intradiem keeps those steady during the day on top of the WFM you already run, and Humana has handle time down 45 seconds with it. Worth a fresh look before the fall volume hits? I'm at 937-238-3179, or reply to my email. Thanks {{firstName}}, Nathan Belfield."

### Email: one more (connect branch)
**Subject:** `one more before the window closes`

> Hi {{firstName}},
> 
> One more and then I'll stop. The measures that still move next year's rating are being scored on live calls right now, and once the fall peak is over, the easy fixes are gone.
> 
> If the next half-star at {{plan_name}} makes the list before then, reach out.
> 
> Nathan

*52 words*

### Call before the just-tried-you email
> Call, then the "just tried you" email goes out. Leave as voicemail if no answer, under 30 seconds:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. I emailed a few weeks ago about {{plan_name}}'s Medicare book and the customer service measures that still move next year's rating. Intradiem keeps those steady during the day on top of the WFM you already run, and Humana has handle time down 45 seconds with it. Worth a fresh look before the fall volume hits? I'm at 937-238-3179, or reply to my email. Thanks {{firstName}}, Nathan Belfield."

### Email: just tried you (A/B)
**Subject:** `just tried you`

> Hi {{firstName}},
> 
> Just tried your line and missed you, so I'll leave this here. I emailed a few weeks ago about {{plan_name}}'s Medicare Advantage book and the customer service measures that still move next year's rating. Those measures are being scored right now, which is why I'm following up.
> 
> Quick version of what Intradiem does: it sits on top of the WFM and phone system your service centers already run and keeps adherence and handle time steady while calls are being scored. Humana has it on the record with handle time down 45 seconds.
> 
> I'm not making a Stars claim. We move the service operation, and the measures follow.
> 
> Worth a conversation on your contracts closest to the line before the fall volume hits?
> 
> Nathan

*126 words*

**Variant B (offer note close):**

> Hi {{firstName}},
> 
> Just tried your line and missed you, so I'll leave this here. I emailed a few weeks ago about {{plan_name}}'s Medicare Advantage book and the customer service measures that still move next year's rating. Those measures are being scored right now, which is why I'm following up.
> 
> Quick version of what Intradiem does: it sits on top of the WFM and phone system your service centers already run and keeps adherence and handle time steady while calls are being scored. Humana has it on the record with handle time down 45 seconds.
> 
> I'm not making a Stars claim. We move the service operation, and the measures follow.
> 
> Rather than ask for time again, would it help if I sent a short note on which service measures still move this cycle? No meeting attached, I'll just send it.
> 
> Nathan

### Email: one more (no-connect branch)
**Subject:** `re: just tried you`

> Hi {{firstName}},
> 
> One more and then I'll stop. The measures that still move next year's rating are being scored on live calls right now, and once the fall peak is over, the easy fixes are gone.
> 
> If the next half-star at {{plan_name}} makes the list before then, reach out.
> 
> Nathan

*52 words*

### Email: closing the loop
**Subject:** `closing the loop`

> Hi {{firstName}},
> 
> Closing the loop on my notes about {{plan_name}}. If this belongs on someone else's desk, a name is all I need. Otherwise I'll leave it until the timing is better.
> 
> Good luck with the fall.
> 
> Nathan

*39 words*


## Blitz - The Hartford (Nate)

### Email 1 (A/B)
**Subject:** `the claims side of the AI number`

> Hi {{firstName}},
> 
> The Hartford has been public this year about AI on the underwriting side. From the outside, the claims and service side doesn't have a number on it yet. That's usually where the gap shows up. Automation takes the predictable work first, so the calls and claims that still reach a person are the unpredictable ones, and they're staffed off a schedule that was set before the week started.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service and claims teams already run and moves people, breaks and training during the day as the week actually plays out, instead of fixing it the next morning. One large North American bank measured $6.1M a year in savings with it, mostly from call handling and schedule adherence.
> 
> Worth a conversation on how you keep service steady when the week doesn't match the plan?
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

*163 words*

**Variant B (offer note close):**

> Hi {{firstName}},
> 
> The Hartford has been public this year about AI on the underwriting side. From the outside, the claims and service side doesn't have a number on it yet. That's usually where the gap shows up. Automation takes the predictable work first, so the calls and claims that still reach a person are the unpredictable ones, and they're staffed off a schedule that was set before the week started.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service and claims teams already run and moves people, breaks and training during the day as the week actually plays out, instead of fixing it the next morning. One large North American bank measured $6.1M a year in savings with it, mostly from call handling and schedule adherence.
> 
> Would it help if I sent a short note on what separates a cheap bad week from an expensive one on the service side? No meeting attached, I'll just send it.
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

### LinkedIn message after connect
> Thanks for connecting, {{firstName}}. Short version of my email: The Hartford's AI number is on the underwriting side today, and the claims and service side is where the unpredictable work still lands on a schedule set before the week started. Intradiem moves people, breaks and training during the day on top of the WFM you already run. Worth a conversation on how you're closing that gap?

### Call 1 (no voicemail)
> Call 1 of 2. If no answer, hang up, no voicemail (that comes with call 2).
> 
> OPENER, four beats, then stop talking:
> 1) Say their first name. Pause.
> 2) "It's Nathan Belfield at Intradiem."
> 3) "We connected on LinkedIn this week. {{vm_hook}}"
> 4) "Can I take 30 seconds, and you tell me if it's not for you?"
> 
> IF THEY ENGAGE (20 to 30 seconds): "Automation takes the predictable work first, so the calls and claims that still reach a person are the unpredictable ones. Intradiem sits on top of the WFM and phone system your teams already run and moves people, breaks and training during the day as the week plays out. One large North American bank measured $6.1M a year in savings with it." Then hand them the floor: "Is that anywhere near how it plays out at The Hartford?"
> 
> THE ASK: "Fifteen minutes and I'll walk you through where carriers usually find the first measurable piece on the service side. If it's already handled, I'll say so and leave you alone."
> 
> ON A YES: lock the slot on the call, two concrete options.
> 
> IF BUSY: "Completely get it. Ten seconds so you know what this was: {{vm_hook}} When's better this week?"
> 
> IF BRUSH-OFF: accept it immediately. "Fair enough. One thing before I go: is that because it's already handled, or just not the priority right now?" Then thank them and stop.

### Call 2 (voicemail)
> Call 2 of 2. If no answer, leave this voicemail, under 30 seconds, warm, unhurried:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service and claims teams already run and moves people, breaks and training during the day as the week plays out. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER, four-beat opener (skip the LinkedIn reference), then the same flow as call 1: the insight, what Intradiem does, the bank number, hand them the floor, the 15-minute ask with the honest-exit clause.

### Email 2 (connect branch)
**Subject:** `re: the claims side of the AI number`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. On the service side, the AI number usually shows up once work gets moved while the day is still running, instead of reconciled after it. That's the specific thing Intradiem does. It reads the WFM and phone system you already have and moves people, breaks and training as the day changes.
> 
> Humana runs it that way and gets about two hours back per agent per month, on top of handle time down 45 seconds.
> 
> Would twenty minutes be useful on where carriers usually find the first measurable piece?
> 
> Nathan

*101 words*

### Email 3 breakup (connect branch)
**Subject:** `re: the claims side of the AI number`

> Hi {{firstName}},
> 
> I'll stop here. If the service side becomes the number you have to move at The Hartford, this quarter or next, reach out. I'd start with the weeks where the plan and the volume disagree most.
> 
> Good luck with the quarter.
> 
> Nathan

*44 words*

### Voicemail (no connect)
> Dial, and if no answer leave this voicemail, under 30 seconds:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service and claims teams already run and moves people, breaks and training during the day as the week plays out. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER: four beats (first name, "It's Nathan Belfield at Intradiem", "I sent you a note this week. {{vm_hook}}", "Can I take 30 seconds?"), then the insight, what Intradiem does, the bank number, and the 15-minute ask. Brush-off: accept it, one either-or question, release warmly.

### Call day after voicemail
> Call, the day after the voicemail. If no answer, hang up, no second voicemail.
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I left you a note yesterday. {{vm_hook}} Intradiem moves people, breaks and training during the day on top of the WFM your teams already run. Worth 15 minutes on where carriers usually find the first measurable piece on the service side?" If busy, trade up to a real slot this week.

### Email 2 (no-connect branch)
**Subject:** `re: the claims side of the AI number`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. On the service side, the AI number usually shows up once work gets moved while the day is still running, instead of reconciled after it. That's the specific thing Intradiem does. It reads the WFM and phone system you already have and moves people, breaks and training as the day changes.
> 
> Humana runs it that way and gets about two hours back per agent per month, on top of handle time down 45 seconds.
> 
> Would twenty minutes be useful on where carriers usually find the first measurable piece?
> 
> Nathan

*101 words*

### Final call
> Final call, no voicemail (one already left).
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I'll be quick. I've sent a couple of notes on the service side carrying the unpredictable work at The Hartford. Before I close the file: is that a this-year question for your team, or a next-year one? Either answer is useful."
> 
> If next year, ask permission to come back then. If this cycle, lock 15 minutes on the call with two concrete options.

### Email 3 breakup (no-connect branch)
**Subject:** `re: the claims side of the AI number`

> Hi {{firstName}},
> 
> I'll stop here. If the service side becomes the number you have to move at The Hartford, this quarter or next, reach out. I'd start with the weeks where the plan and the volume disagree most.
> 
> Good luck with the quarter.
> 
> Nathan

*44 words*

### Email 2 (no-LinkedIn branch)
**Subject:** `re: the claims side of the AI number`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. On the service side, the AI number usually shows up once work gets moved while the day is still running, instead of reconciled after it. That's the specific thing Intradiem does. It reads the WFM and phone system you already have and moves people, breaks and training as the day changes.
> 
> Humana runs it that way and gets about two hours back per agent per month, on top of handle time down 45 seconds.
> 
> Would twenty minutes be useful on where carriers usually find the first measurable piece?
> 
> Nathan

*101 words*

### Email 3 breakup (no-LinkedIn branch)
**Subject:** `re: the claims side of the AI number`

> Hi {{firstName}},
> 
> I'll stop here. If the service side becomes the number you have to move at The Hartford, this quarter or next, reach out. I'd start with the weeks where the plan and the volume disagree most.
> 
> Good luck with the quarter.
> 
> Nathan

*44 words*


## Blitz - Citizens (Nate)

### Email 1 (A/B)
**Subject:** `the half that's left`

> Hi {{firstName}},
> 
> Citizens has said publicly it wants a quarter of calls answered without a person by the end of this year, on the way to half. Every deflection program hits the same second problem. The calls that still reach a person are the hard ones, so handle time goes up, and the easy volume that used to give the schedule some slack is gone.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service teams already run and moves people, breaks and coaching during the day as the mix changes, instead of fixing it the next morning. One large North American bank measured $6.1M a year in savings with it, mostly from call handling and schedule adherence.
> 
> Worth a conversation on how you're planning the human side of that shift?
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

*151 words*

**Variant B (offer note close):**

> Hi {{firstName}},
> 
> Citizens has said publicly it wants a quarter of calls answered without a person by the end of this year, on the way to half. Every deflection program hits the same second problem. The calls that still reach a person are the hard ones, so handle time goes up, and the easy volume that used to give the schedule some slack is gone.
> 
> That's what Intradiem does. It sits on top of the WFM and phone system your service teams already run and moves people, breaks and coaching during the day as the mix changes, instead of fixing it the next morning. One large North American bank measured $6.1M a year in savings with it, mostly from call handling and schedule adherence.
> 
> Would it help if I sent a short note on what teams usually run into on the human side once deflection is live? No meeting attached, I'll just send it.
> 
> If you'd rather not hear from me, just say so and I'll stop.
> 
> Nathan

### LinkedIn message after connect
> Thanks for connecting, {{firstName}}. Short version of my email: once AI takes the easy half of the calls, the half that's left is the hard ones, and the schedule has no slack to absorb the change. Intradiem moves people, breaks and coaching during the day on top of the WFM you already run. Worth a conversation on how you're planning that side of it?

### Call 1 (no voicemail)
> Call 1 of 2. If no answer, hang up, no voicemail (that comes with call 2).
> 
> OPENER, four beats, then stop talking:
> 1) Say their first name. Pause.
> 2) "It's Nathan Belfield at Intradiem."
> 3) "We connected on LinkedIn this week. {{vm_hook}}"
> 4) "Can I take 30 seconds, and you tell me if it's not for you?"
> 
> IF THEY ENGAGE (20 to 30 seconds): "Once AI takes the easy half of the calls, the half that's left is the hard ones, so handle time goes up and the schedule has no slack to absorb it. Intradiem sits on top of the WFM and phone system your teams already run and moves people, breaks and coaching during the day as the mix changes. One large North American bank measured $6.1M a year in savings with it." Then hand them the floor: "Is that anywhere near how it plays out at Citizens?"
> 
> THE ASK: "Fifteen minutes and I'll walk you through what the human side usually looks like once a deflection program is running at scale. If it's already handled, I'll say so and leave you alone."
> 
> ON A YES: lock the slot on the call, two concrete options.
> 
> IF BUSY: "Completely get it. Ten seconds so you know what this was: {{vm_hook}} When's better this week?"
> 
> IF BRUSH-OFF: accept it immediately. "Fair enough. One thing before I go: is that because it's already handled, or just not the priority right now?" Then thank them and stop.

### Call 2 (voicemail)
> Call 2 of 2. If no answer, leave this voicemail, under 30 seconds, warm, unhurried:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service teams already run and moves people, breaks and coaching during the day as the call mix changes. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER, four-beat opener (skip the LinkedIn reference), then the same flow as call 1: the insight, what Intradiem does, the bank number, hand them the floor, the 15-minute ask with the honest-exit clause.

### Email 2 (connect branch)
**Subject:** `re: the half that's left`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. A quarter of calls by year end puts the change inside the next two quarters. The part that has to be managed in the moment, not in the next morning's report, is the human queue underneath it. That's the specific thing Intradiem does. It reads the WFM and phone system you already have and moves people, breaks and coaching as the mix changes during the day.
> 
> Humana runs it that way and gets handle time down 45 seconds and about two hours back per agent per month.
> 
> Would twenty minutes be useful on what the human side usually looks like once deflection is running at scale?
> 
> Nathan

*119 words*

### Email 3 breakup (connect branch)
**Subject:** `re: the half that's left`

> Hi {{firstName}},
> 
> I'll stop here. A deflection program gets judged on the half that goes away and decided by the half that stays. If that half becomes a live question at Citizens, this quarter or next, reach out.
> 
> Good luck with the rollout.
> 
> Nathan

*44 words*

### Voicemail (no connect)
> Dial, and if no answer leave this voicemail, under 30 seconds:
> 
> "{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: Intradiem sits on top of the WFM your service teams already run and moves people, breaks and coaching during the day as the call mix changes. I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield."
> 
> IF THEY ANSWER: four beats (first name, "It's Nathan Belfield at Intradiem", "I sent you a note this week. {{vm_hook}}", "Can I take 30 seconds?"), then the insight, what Intradiem does, the bank number, and the 15-minute ask. Brush-off: accept it, one either-or question, release warmly.

### Call day after voicemail
> Call, the day after the voicemail. If no answer, hang up, no second voicemail.
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I left you a note yesterday. {{vm_hook}} Intradiem moves people, breaks and coaching during the day on top of the WFM your teams already run. Worth 15 minutes on what the human side looks like once a deflection program is running at scale?" If busy, trade up to a real slot this week.

### Email 2 (no-connect branch)
**Subject:** `re: the half that's left`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. A quarter of calls by year end puts the change inside the next two quarters. The part that has to be managed in the moment, not in the next morning's report, is the human queue underneath it. That's the specific thing Intradiem does. It reads the WFM and phone system you already have and moves people, breaks and coaching as the mix changes during the day.
> 
> Humana runs it that way and gets handle time down 45 seconds and about two hours back per agent per month.
> 
> Would twenty minutes be useful on what the human side usually looks like once deflection is running at scale?
> 
> Nathan

*119 words*

### Final call
> Final call, no voicemail (one already left).
> 
> IF THEY ANSWER: "{{firstName}}, Nathan Belfield at Intradiem, I'll be quick. I've sent a couple of notes on what happens to the calls that are left at Citizens once AI answers the easy ones. Before I close the file: is that a this-year question for your team, or a next-year one? Either answer is useful."
> 
> If next year, ask permission to come back then. If this cycle, lock 15 minutes on the call with two concrete options.

### Email 3 breakup (no-connect branch)
**Subject:** `re: the half that's left`

> Hi {{firstName}},
> 
> I'll stop here. A deflection program gets judged on the half that goes away and decided by the half that stays. If that half becomes a live question at Citizens, this quarter or next, reach out.
> 
> Good luck with the rollout.
> 
> Nathan

*44 words*

### Email 2 (no-LinkedIn branch)
**Subject:** `re: the half that's left`

> Hi {{firstName}},
> 
> One thing I didn't say clearly in my first note. A quarter of calls by year end puts the change inside the next two quarters. The part that has to be managed in the moment, not in the next morning's report, is the human queue underneath it. That's the specific thing Intradiem does. It reads the WFM and phone system you already have and moves people, breaks and coaching as the mix changes during the day.
> 
> Humana runs it that way and gets handle time down 45 seconds and about two hours back per agent per month.
> 
> Would twenty minutes be useful on what the human side usually looks like once deflection is running at scale?
> 
> Nathan

*119 words*

### Email 3 breakup (no-LinkedIn branch)
**Subject:** `re: the half that's left`

> Hi {{firstName}},
> 
> I'll stop here. A deflection program gets judged on the half that goes away and decided by the half that stays. If that half becomes a live question at Citizens, this quarter or next, reach out.
> 
> Good luck with the rollout.
> 
> Nathan

*44 words*

