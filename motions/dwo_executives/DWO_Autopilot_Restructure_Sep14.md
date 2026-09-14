# DWO Executives autopilot lane, restructure record (Sep 14 2026)

Campaign cam_SiD4KmWcRuhiF6uhL, 803 leads, paused, sender still nathan.belfield@intradiem.com (switch to the intradiemhq.com mailbox is Dallas's hand, earliest Sep 21, planned Sep 25). Nothing sent, nothing launched, no live post.

## The first three touches now
| Day | Step | Type | Who acts |
|---|---|---|---|
| 0 | Email 1 (A/B, unchanged) | auto | nobody |
| 1 | Call 1, leave the voicemail (script below) | task | Nate |
| 3 | Email 2, same thread, verbatim Sep 4 body | auto | nobody |
| 4 | LinkedIn visit | auto | nobody |
| 5 | LinkedIn invite (leads with a URL), then the accepted / else branches as built Sep 4 | task | Nate |

The Sep 4 tree put a LinkedIn visit and the invite before the call and email 2, so every lead waited on Nate's task queue after one email. Now a lead gets three touches before any manual LinkedIn step, and the rep's first task is the call.

## Preview, Keith Farley (Aflac), variant A lead
**Email 1, day 0.** Subject: Quick idea to cut agent idle minutes at Aflac

Hi Keith,

Two months into the Chief Customer Officer seat at Aflac, the listening tour is over and the operating agenda is getting written.

In service operations the trade usually gets framed as cost or experience. The idle minutes inside the shift are the one lever that moves both: coaching and training happen in the quiet windows instead of never, and the busy windows get the people back.

That's what Intradiem does. It sits on top of the WFM and case systems your claims and service teams already run, spots idle windows as they open, and moves work, coaching and breaks into them, contact center and back office. Humana has it on the record: two hours of capacity back per agent per month, and handle time down 45 seconds.

Worth a conversation on where Aflac's coaching hours actually come from today?

Nathan

**Call 1, day 1 (task title: Call 1 Keith (Aflac): leave the voicemail. No number? Main line, office of the COO)**

[draft, Nate reads] Call 1 of 3, the day after email 1. If no answer, leave this voicemail, about 20 seconds, warm, unhurried:

"Keith, Nathan Belfield at Intradiem. I sent you a note on idle minutes at Aflac; the short version is in your email. Your operations pay for capacity twice, idle minutes inside the shift and overtime after it, and Humana gets two hours back per agent per month by moving work into those minutes. I'm at 937-238-3179. Thanks Keith."

IF THEY ANSWER, four beats, then stop talking: "Keith?" (pause) "Nathan Belfield at Intradiem." "I sent you a note on idle minutes at Aflac." "Can I take 30 seconds, and you tell me if it's not for you?" Then: capacity paid for twice, what Intradiem does on top of the WFM and case systems your claims and service teams already run, the Humana number, and hand it over: "Is overtime a line you're being asked to take down this year?" On a yes, lock 15 minutes with two concrete options. Brush-off: "Fair enough. Is that because it's handled, or not the priority right now?" Thank them and stop.

NO DIRECT NUMBER (EA route): main line, ask for the office of Keith Farley, get the EA's name, leave the one line: "Idle time and overtime across the claims and service teams, and whether it's worth fifteen minutes in October. The note is in Keith's email."

**Email 2, day 3, same thread**

Hi Keith,

One number I left out. Humana's agents took 12,000 hours of voluntary time off that Intradiem found inside the schedule, which Humana counts directly as overtime avoided.

That's the shape of it in most operations: the capacity is already on the payroll, it just arrives at the wrong minute.

Is overtime a line you're being asked to take down this year, or is it holding steady?

Nathan

## What changed in lemlist (all via the connector, campaign paused)
- Added root step stp_aJGLWhmk73ajWjYcx (phone, delay 1) at index 1 and stp_xXqcnL3No78zYfHsG (email thread, delay 2) at index 2.
- LinkedIn visit stp_NZxCJfcS4nFWiqwk5 delay 0 to 1.
- Deleted the four duplicates the inserts made redundant: Call 1 and Email 2 in both hasLinkedinUrl branches (stp_RkQGWsp35dP4GjiAD, stp_J4fiJT3SfkNQpoJ6k, stp_7Xn7F6LZSGes3oeqJ, stp_b5Pdy5yq2gwQdJzeF).
- Everything after the invite (accepted and else branches, calls 2 and 3, the just-tried-you, peak, colleague and breakup emails) is untouched.

## Daily Action Brief
- config/action_brief.json: live stays false; new dry_run_lanes (nathan: dwo only, jack: none); the dwo brief carries autopilot_lane true. Wrapper honours BRIEF_REPS for an on-demand scoped run and the dry-run lane filter.
- First dry-run render: automation/logs/action-brief-2026-09-14.md.

## Still Dallas's hands
- Sender switch to the warm mailbox, then launch (never by the agent).
- Phone coverage: 41 of 803 leads carry a phone; the EA route covers the rest, or run the phone sourcing test from motions/dwo_executives/phones/ first.
- Nate reads the call script and email 2 placement before launch.
