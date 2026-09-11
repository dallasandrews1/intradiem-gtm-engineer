#!/usr/bin/env python3
"""Nate campaign copy rewrite, Sep 3 2026 (v3: plain spoken, proper paragraph spacing). Source of truth for the lemlist step updates.

Doctrine: motions/shared/Messaging_Doctrine_Sep3.md. Sender: Nathan Belfield, first name only.
Verified claims used (04-value-repository): Humana (cleared, named): AHT down 45 seconds, 2 hours of capacity per agent
per month, 7X ROI five years in. RBC cited BLINDED ("a large North American bank", $6.1M a year). Public CMS math carries
the humility clause. Public signals verified Sep 3: Hartford Q2 2026 call (AI in underwriting), Citizens Q1 2026 call
(25 percent of calls answered by non-humans by end of 2026, 50 percent by fall 2027). No other numbers.
Per-lead variables on every lead: firstName, plan_name, qbp_avg, vm_hook, voice_script.

Formatting: lemlist renders <p> with no margin, so every paragraph break is an explicit blank line (<p><br></p>).
Voice test applied to every line: would Nate say this on the phone? No "in one line", no "the seam I work",
no "which is the only reason", no "the ground between".

Run:  python3 nate_rewrite_sep3.py > Nate_Copy_Rewrite_Sep3.md   |   --json for the step payloads
"""

OPT = "If you'd rather not hear from me, just say so and I'll stop."
NOT_A_CLAIM = "I'm not making a Stars claim. We move the service operation, and the measures follow."

def P(*paras):
    """Paragraphs separated by an explicit blank line, the way lemlist's own editor stores them."""
    blank = '<p><br></p>'
    return blank.join(f"<p>{p}</p>" for p in paras)

U = []
def add(camp, cid, sid, stp, label, subject=None, body=None, vb=None):
    U.append(dict(campaign=camp, campaignId=cid, sequenceId=sid, stepId=stp, label=label,
                  subject=subject, message=body, variantB=vb))

CALL_OPENER = ("OPENER, four beats, then stop talking:\n1) Say their first name. Pause.\n2) \"It's Nathan Belfield at Intradiem.\"\n"
  "3) \"We connected on LinkedIn this week. {{vm_hook}}\"\n4) \"Can I take 30 seconds, and you tell me if it's not for you?\"\n\n")
CALL_TAIL = ("\n\nON A YES: lock the slot on the call, two concrete options.\n\n"
  "IF BUSY: \"Completely get it. Ten seconds so you know what this was: {{vm_hook}} When's better this week?\"\n\n"
  "IF BRUSH-OFF: accept it immediately. \"Fair enough. One thing before I go: is that because it's already handled, or just "
  "not the priority right now?\" Then thank them and stop.")
def call1(insight, floor, ask):
    return ("Call 1 of 2. If no answer, hang up, no voicemail (that comes with call 2).\n\n" + CALL_OPENER +
            f"IF THEY ENGAGE (20 to 30 seconds): \"{insight}\" Then hand them the floor: \"{floor}\"\n\n"
            f"THE ASK: \"Fifteen minutes and I'll walk you through {ask}. If it's already handled, I'll say so and leave you alone.\""
            + CALL_TAIL)
def vm(product_line):
    return ("\"{{firstName}}, this is Nathan Belfield with Intradiem. {{vm_hook}} Quick version: " + product_line +
            " I'm at 937-238-3179, or just reply to my email. Thanks {{firstName}}, Nathan Belfield.\"")
def call2(v, recap):
    return ("Call 2 of 2. If no answer, leave this voicemail, under 30 seconds, warm, unhurried:\n\n" + v +
            "\n\nIF THEY ANSWER, four-beat opener (skip the LinkedIn reference), then the same flow as call 1: " + recap +
            ", hand them the floor, the 15-minute ask with the honest-exit clause.")
def vmstep(v, recap):
    return ("Dial, and if no answer leave this voicemail, under 30 seconds:\n\n" + v +
            "\n\nIF THEY ANSWER: four beats (first name, \"It's Nathan Belfield at Intradiem\", \"I sent you a note this week. "
            "{{vm_hook}}\", \"Can I take 30 seconds?\"), then " + recap + ", and the 15-minute ask. Brush-off: accept it, one "
            "either-or question, release warmly.")
def dayafter(topic, product_line, ask):
    return ("Call, the day after the voicemail. If no answer, hang up, no second voicemail.\n\nIF THEY ANSWER: "
            "\"{{firstName}}, Nathan Belfield at Intradiem, I left you a note yesterday" + topic + ". {{vm_hook}} " + product_line +
            " Worth 15 minutes on " + ask + "?\" If busy, trade up to a real slot this week.")
def final(topic, question, comeback):
    return ("Final call, no voicemail (one already left).\n\nIF THEY ANSWER: \"{{firstName}}, Nathan Belfield at Intradiem, "
            "I'll be quick. I've sent a couple of notes on " + topic + ". Before I close the file: " + question + " Either answer is useful.\""
            "\n\nIf next year, ask permission to come back " + comeback + ". If this cycle, lock 15 minutes on the call with two concrete options.")

# ---------------------------------------------------------------- Stars, Finance lane
C = "Stars - Fresh Pool / Finance (Nate)"; CID = "cam_2gy9hmEvMjYEuPZ8A"
FIN_OPEN = ("On the latest CMS release, {{plan_name}}'s Medicare Advantage book looks to be sitting near {{qbp_avg}}. "
            "You'll know the exact number better than I do. From the finance side, that's a quality bonus question. The bonus "
            "turns on at 4.0, and most of what stands between you and 4.0 is customer service measures. Those are cheaper to "
            "move than the clinical ones, and they're being scored right now.")
FIN_PROD = ("That's what Intradiem does. It sits on top of the WFM and phone system your service centers already run and "
            "keeps adherence and handle time steady during the day, while those calls are being scored. Humana has it on the "
            "record: handle time down 45 seconds and a 7X return five years in.")
FIN_E1 = P("Hi {{firstName}},", FIN_OPEN, FIN_PROD, NOT_A_CLAIM,
           "Worth a conversation on what it costs to close the gap to 4.0 versus what the bonus pays?", OPT, "Nathan")
FIN_E1_B = P("Hi {{firstName}},", FIN_OPEN, FIN_PROD, NOT_A_CLAIM,
             "Would it help if I sent over a short note on how plans near the line weigh that cost against the bonus? "
             "No meeting attached, I'll just send it.", OPT, "Nathan")
FIN_LI = ("Thanks for connecting, {{firstName}}. Short version of my email: {{plan_name}}'s book looks to be near "
          "{{qbp_avg}}, the bonus turns on at 4.0, and the points that can still move this cycle are the customer service "
          "ones. Intradiem keeps those steady during the day on top of the WFM you already run. Worth a conversation on what "
          "closing the gap costs versus what the bonus pays?")
FIN_E2 = P("Hi {{firstName}},",
  "One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's "
  "still open is next year's rating, and that's being scored in the busy weeks between now and December. So the window "
  "to move the service measures at {{plan_name}} is this fall, not next spring.",
  "If the gap to 4.0 is in your model at all, it's cheaper to start before the fall volume hits than after. Intradiem "
  "runs on top of what you already have, so it can start inside that window.",
  "Would twenty minutes on the finance side be useful? What it costs to hold the line versus what the bonus pays.",
  "Nathan")
FIN_E3 = P("Hi {{firstName}},",
  "I'll stop here. If the quality bonus becomes a live question at {{plan_name}}, this cycle or next, reach out. I'd "
  "start with the contracts closest to the line.",
  "Good luck with the fall.", "Nathan")
FIN_INSIGHT = ("The bonus turns on at 4.0, and most of what stands between the book and 4.0 is customer service measures. "
  "Intradiem sits on top of the WFM and phone system your service centers already run and keeps adherence and handle time "
  "steady during the day, while those calls are being scored. Humana has it on the record with handle time down 45 seconds.")
FIN_CALL1 = call1(FIN_INSIGHT, "Is the bonus line in your model this cycle?", "what it costs to close the gap to 4.0 versus what the bonus pays")
FIN_VM = vm("Intradiem sits on top of the WFM your service centers already run and keeps the service measures steady while they're being scored. Humana has handle time down 45 seconds with it.")
FIN_CALL2 = call2(FIN_VM, "the bonus line, what Intradiem does, the Humana number")
FIN_VM_STEP = vmstep(FIN_VM, "the bonus line, what Intradiem does, the Humana number")
FIN_DAYAFTER = dayafter(" on the bonus line at {{plan_name}}", "Intradiem keeps the service measures steady during the day on top of the WFM you already run.", "what closing the gap costs versus what the bonus pays")
FIN_FINAL = final("the quality bonus line at {{plan_name}}", "is the bonus a this-cycle question for your team, or a next-year one?", "in the spring")
add(C,CID,"seq_JgHnp4nwCZ47sqjXo","stp_hmp9Gp7dAZFgkgqPq","Email 1 (A/B)","the bonus line at {{plan_name}}",FIN_E1, dict(subject="the bonus line at {{plan_name}}", message=FIN_E1_B))
add(C,CID,"seq_Mtnqt8s9LKr9bKnpD","stp_y85XidZL3XCecpzAZ","LinkedIn message after connect",None,FIN_LI)
add(C,CID,"seq_Mtnqt8s9LKr9bKnpD","stp_mGX4zdGjW24szwMn2","Call 1 (no voicemail)",None,FIN_CALL1)
add(C,CID,"seq_Mtnqt8s9LKr9bKnpD","stp_79dFBYM92pciNTc4p","Call 2 (voicemail)",None,FIN_CALL2)
add(C,CID,"seq_Mtnqt8s9LKr9bKnpD","stp_WGh7oxAFgKYpWpvxX","Email 2 (connect branch)","re: the bonus line at {{plan_name}}",FIN_E2)
add(C,CID,"seq_Mtnqt8s9LKr9bKnpD","stp_zqvz6RiisyJP7jrEu","Email 3 breakup (connect branch)","re: the bonus line at {{plan_name}}",FIN_E3)
add(C,CID,"seq_dN2LWWFxL8ZcnHe5f","stp_2PEMT5MxZGCvQ4gCc","Voicemail (no connect)",None,FIN_VM_STEP)
add(C,CID,"seq_dN2LWWFxL8ZcnHe5f","stp_bz4CCwLzxstfepkkT","Call day after voicemail",None,FIN_DAYAFTER)
add(C,CID,"seq_dN2LWWFxL8ZcnHe5f","stp_SAQGYwNEDHNYMo7yg","Email 2 (no-connect branch)","re: the bonus line at {{plan_name}}",FIN_E2)
add(C,CID,"seq_dN2LWWFxL8ZcnHe5f","stp_GvbcKTybfkWs3egL4","Final call",None,FIN_FINAL)
add(C,CID,"seq_dN2LWWFxL8ZcnHe5f","stp_WF7nrb9fXE4DJZttE","Email 3 breakup (no-connect branch)","re: the bonus line at {{plan_name}}",FIN_E3)
add(C,CID,"seq_GTqA7GD4zMosMcNqP","stp_5Hce5ibX4ngDWTtsW","Email 2 (no-LinkedIn branch)","re: the bonus line at {{plan_name}}",FIN_E2)
add(C,CID,"seq_GTqA7GD4zMosMcNqP","stp_d586JNgt2ithx2mqa","Email 3 breakup (no-LinkedIn branch)","re: the bonus line at {{plan_name}}",FIN_E3)

# ---------------------------------------------------------------- Stars, Quality lane
C = "Stars - Fresh Pool / Quality (Nate)"; CID = "cam_viEbB6HkYsCPtxKbi"
QUA_OPEN = ("{{plan_name}}'s Medicare Advantage book looks to be sitting near {{qbp_avg}} on the latest CMS release. You'll "
            "know the exact picture better than I do. Between there and 4.0, the points that move fastest are usually the "
            "customer service measures, and those are being scored right now, this measurement year, not on the October release.")
QUA_PROD = ("That's what Intradiem does. It sits on top of the WFM and phone system your service centers already run and "
            "works during the day: it moves breaks and training into the quiet minutes and keeps adherence and handle time "
            "steady while calls are being scored. Humana has it on the record with handle time down 45 seconds.")
QUA_E1 = P("Hi {{firstName}},", QUA_OPEN, QUA_PROD, NOT_A_CLAIM,
           "Worth a conversation on which of your contracts are closest to the line and what can still move this cycle?", OPT, "Nathan")
QUA_E1_B = P("Hi {{firstName}},", QUA_OPEN, QUA_PROD, NOT_A_CLAIM,
             "Would it help if I sent over a short note on which service measures usually decide it for a book near the line? "
             "No meeting attached, I'll just send it.", OPT, "Nathan")
QUA_LI = ("Thanks for connecting, {{firstName}}. Short version of my email: {{plan_name}}'s book looks to be near "
          "{{qbp_avg}}, and the points that can still move this cycle are the customer service ones, scored on live calls "
          "between now and December. Intradiem keeps those steady during the day on top of the WFM you already run. Worth a "
          "conversation on your contracts closest to the line?")
QUA_E2 = P("Hi {{firstName}},",
  "One thing I didn't say clearly in my first note. The rating that comes out in October was set by last year. What's "
  "still open is next year's rating, and the customer service measures are scored in the busy weeks between now and "
  "December, which is also when they tend to slip.",
  "Keeping them steady through those weeks is the whole job. Humana runs Intradiem on top of its WFM for exactly that, "
  "and gets about two hours back per agent per month, most of it going into coaching that used to wait for a quiet day.",
  "Would twenty minutes be useful on which measures usually decide the next half-star for a book near your line?",
  "Nathan")
QUA_E3 = P("Hi {{firstName}},",
  "I'll stop here. If the next half-star at {{plan_name}} becomes a priority, this cycle or next, reach out. I'd start "
  "with the customer service measures on your contracts closest to the line.",
  "Good luck with the fall.", "Nathan")
QUA_INSIGHT = ("Between where the book sits and 4.0, the points that move fastest are usually the customer service measures, "
  "and they're being scored right now. Intradiem sits on top of the WFM and phone system your service centers already run "
  "and keeps adherence and handle time steady during the day, while those calls are being scored. Humana has it on the "
  "record with handle time down 45 seconds.")
QUA_CALL1 = call1(QUA_INSIGHT, "Is that anywhere near how it looks from your seat?", "which of your contracts are closest to the line and what can still move this cycle")
QUA_VM = FIN_VM
QUA_CALL2 = call2(QUA_VM, "the service measures, what Intradiem does, the Humana number")
QUA_VM_STEP = vmstep(QUA_VM, "the service measures, what Intradiem does, the Humana number")
QUA_DAYAFTER = dayafter(" on the customer service measures at {{plan_name}}", "Intradiem keeps the service measures steady during the day on top of the WFM you already run.", "which of your contracts are closest to the line")
QUA_FINAL = final("the next half-star at {{plan_name}}", "is the next half-star a this-cycle question for your team, or a next-year one?", "in the spring")
add(C,CID,"seq_uya6vybEyCKXZbfMg","stp_b9Ns4nuZJSpT8Xr6s","Email 1 (A/B)","the service measures at {{plan_name}}",QUA_E1, dict(subject="the service measures at {{plan_name}}", message=QUA_E1_B))
add(C,CID,"seq_FKqfv2325wMmz8Dtc","stp_BiYawgXJqunKqMKQ6","LinkedIn message after connect",None,QUA_LI)
add(C,CID,"seq_FKqfv2325wMmz8Dtc","stp_g5ovqqDRpZR2wZ9GM","Call 1 (no voicemail)",None,QUA_CALL1)
add(C,CID,"seq_FKqfv2325wMmz8Dtc","stp_QkYs9KGRARYvZzeso","Call 2 (voicemail)",None,QUA_CALL2)
add(C,CID,"seq_FKqfv2325wMmz8Dtc","stp_6Ec35QjTN8wxQTyzh","Email 2 (connect branch)","re: the service measures at {{plan_name}}",QUA_E2)
add(C,CID,"seq_FKqfv2325wMmz8Dtc","stp_SgSrRTk2JmXjFk6h2","Email 3 breakup (connect branch)","re: the service measures at {{plan_name}}",QUA_E3)
add(C,CID,"seq_kLTLpLpFLCyvp6Kcd","stp_6ypPNXP38fcrnDCqk","Voicemail (no connect)",None,QUA_VM_STEP)
add(C,CID,"seq_kLTLpLpFLCyvp6Kcd","stp_WwSBttJmtvcmP9wE7","Call day after voicemail",None,QUA_DAYAFTER)
add(C,CID,"seq_kLTLpLpFLCyvp6Kcd","stp_Su5qdLPGd4uk4KAFZ","Email 2 (no-connect branch)","re: the service measures at {{plan_name}}",QUA_E2)
add(C,CID,"seq_kLTLpLpFLCyvp6Kcd","stp_LABLiwASiNCuHtSHy","Final call",None,QUA_FINAL)
add(C,CID,"seq_kLTLpLpFLCyvp6Kcd","stp_wthvAbfD3vu8iKFFo","Email 3 breakup (no-connect branch)","re: the service measures at {{plan_name}}",QUA_E3)
add(C,CID,"seq_xayDCoQKqqpnEm9YC","stp_REBxnFqwvo4FF9xFk","Email 2 (no-LinkedIn branch)","re: the service measures at {{plan_name}}",QUA_E2)
add(C,CID,"seq_xayDCoQKqqpnEm9YC","stp_CBmQ7XJkTNsyXF5hr","Email 3 breakup (no-LinkedIn branch)","re: the service measures at {{plan_name}}",QUA_E3)

# ---------------------------------------------------------------- Stars, Resurrection
C = "Stars - Resurrection (Nate)"; CID = "cam_sh3JCJoxtEHyjGrsw"
RES_LI = ("Thanks for connecting, {{firstName}}. I emailed a few weeks ago about {{plan_name}}'s Medicare book and the "
          "customer service measures that still move next year's rating. Intradiem sits on top of the WFM you already run "
          "and keeps those measures steady while they're being scored. Worth a fresh look before the fall volume hits?")
def res_vm(tail):
    return ("\"{{firstName}}, this is Nathan Belfield with Intradiem" + tail + ". I emailed a few weeks ago about {{plan_name}}'s "
      "Medicare book and the customer service measures that still move next year's rating. Intradiem keeps those steady during "
      "the day on top of the WFM you already run, and Humana has handle time down 45 seconds with it. Worth a fresh look before "
      "the fall volume hits? I'm at 937-238-3179, or reply to my email. Thanks {{firstName}}, Nathan Belfield.\"")
RES_CALL_CONNECT = "Call after the accepted connect. Leave as voicemail if no answer, under 30 seconds:\n\n" + res_vm(", thanks for the connect")
RES_CALL_NOCONNECT = "Call, then the \"just tried you\" email goes out. Leave as voicemail if no answer, under 30 seconds:\n\n" + res_vm("")
RES_OPEN = ("Just tried your line and missed you, so I'll leave this here. I emailed a few weeks ago about {{plan_name}}'s "
            "Medicare Advantage book and the customer service measures that still move next year's rating. Those measures "
            "are being scored right now, which is why I'm following up.")
RES_PROD = ("Quick version of what Intradiem does: it sits on top of the WFM and phone system your service centers already "
            "run and keeps adherence and handle time steady while calls are being scored. Humana has it on the record with "
            "handle time down 45 seconds.")
RES_TRIED = P("Hi {{firstName}},", RES_OPEN, RES_PROD, NOT_A_CLAIM,
              "Worth a conversation on your contracts closest to the line before the fall volume hits?", "Nathan")
RES_TRIED_B = P("Hi {{firstName}},", RES_OPEN, RES_PROD, NOT_A_CLAIM,
                "Rather than ask for time again, would it help if I sent a short note on which service measures still move "
                "this cycle? No meeting attached, I'll just send it.", "Nathan")
RES_ONEMORE = P("Hi {{firstName}},",
  "One more and then I'll stop. The measures that still move next year's rating are being scored on live calls right "
  "now, and once the fall peak is over, the easy fixes are gone.",
  "If the next half-star at {{plan_name}} makes the list before then, reach out.", "Nathan")
RES_CLOSE = P("Hi {{firstName}},",
  "Closing the loop on my notes about {{plan_name}}. If this belongs on someone else's desk, a name is all I need. "
  "Otherwise I'll leave it until the timing is better.",
  "Good luck with the fall.", "Nathan")
add(C,CID,"seq_WbTtwaYkMggGu9ztX","stp_3P8mtA3juwKYMXjJg","LinkedIn message after connect",None,RES_LI)
add(C,CID,"seq_WbTtwaYkMggGu9ztX","stp_kBkdqpRK7voEnbLup","Call after connect",None,RES_CALL_CONNECT)
add(C,CID,"seq_WbTtwaYkMggGu9ztX","stp_zgdinKdRRCcsTg9qA","Email: one more (connect branch)","one more before the window closes",RES_ONEMORE)
add(C,CID,"seq_3Aj58rf9Yp8kZpdvS","stp_np2nhyGjHiKYZTM26","Call before the just-tried-you email",None,RES_CALL_NOCONNECT)
add(C,CID,"seq_3Aj58rf9Yp8kZpdvS","stp_afdYJbTbPXLZkvxkC","Email: just tried you (A/B)","just tried you",RES_TRIED, dict(subject="just tried you", message=RES_TRIED_B))
add(C,CID,"seq_3FpmiTeBzmnZiTzFy","stp_WqeFKM5M9Rjn7ehvF","Email: one more (no-connect branch)","re: just tried you",RES_ONEMORE)
add(C,CID,"seq_L3XgZazRhgn6WdP3R","stp_JZWJtgNf59zwwWDBB","Email: closing the loop","closing the loop",RES_CLOSE)

# ---------------------------------------------------------------- Blitz, The Hartford
C = "Blitz - The Hartford (Nate)"; CID = "cam_fYp7Nh9wB72gfMke6"
BANK = "One large North American bank measured $6.1M a year in savings with it, mostly from call handling and schedule adherence."
HAR_OPEN = ("The Hartford has been public this year about AI on the underwriting side. From the outside, the claims and "
            "service side doesn't have a number on it yet. That's usually where the gap shows up. Automation takes the "
            "predictable work first, so the calls and claims that still reach a person are the unpredictable ones, and "
            "they're staffed off a schedule that was set before the week started.")
HAR_PROD = ("That's what Intradiem does. It sits on top of the WFM and phone system your service and claims teams already "
            "run and moves people, breaks and training during the day as the week actually plays out, instead of fixing it "
            "the next morning. " + BANK)
HAR_E1 = P("Hi {{firstName}},", HAR_OPEN, HAR_PROD,
           "Worth a conversation on how you keep service steady when the week doesn't match the plan?", OPT, "Nathan")
HAR_E1_B = P("Hi {{firstName}},", HAR_OPEN, HAR_PROD,
             "Would it help if I sent a short note on what separates a cheap bad week from an expensive one on the service "
             "side? No meeting attached, I'll just send it.", OPT, "Nathan")
HAR_LI = ("Thanks for connecting, {{firstName}}. Short version of my email: The Hartford's AI number is on the underwriting "
          "side today, and the claims and service side is where the unpredictable work still lands on a schedule set before "
          "the week started. Intradiem moves people, breaks and training during the day on top of the WFM you already run. "
          "Worth a conversation on how you're closing that gap?")
HAR_E2 = P("Hi {{firstName}},",
  "One thing I didn't say clearly in my first note. On the service side, the AI number usually shows up once work gets "
  "moved while the day is still running, instead of reconciled after it. That's the specific thing Intradiem does. It "
  "reads the WFM and phone system you already have and moves people, breaks and training as the day changes.",
  "Humana runs it that way and gets about two hours back per agent per month, on top of handle time down 45 seconds.",
  "Would twenty minutes be useful on where carriers usually find the first measurable piece?", "Nathan")
HAR_E3 = P("Hi {{firstName}},",
  "I'll stop here. If the service side becomes the number you have to move at The Hartford, this quarter or next, reach "
  "out. I'd start with the weeks where the plan and the volume disagree most.",
  "Good luck with the quarter.", "Nathan")
HAR_INSIGHT = ("Automation takes the predictable work first, so the calls and claims that still reach a person are the "
  "unpredictable ones. Intradiem sits on top of the WFM and phone system your teams already run and moves people, breaks "
  "and training during the day as the week plays out. One large North American bank measured $6.1M a year in savings with it.")
HAR_CALL1 = call1(HAR_INSIGHT, "Is that anywhere near how it plays out at The Hartford?", "where carriers usually find the first measurable piece on the service side")
HAR_VM = vm("Intradiem sits on top of the WFM your service and claims teams already run and moves people, breaks and training during the day as the week plays out.")
HAR_CALL2 = call2(HAR_VM, "the insight, what Intradiem does, the bank number")
HAR_VM_STEP = vmstep(HAR_VM, "the insight, what Intradiem does, the bank number")
HAR_DAYAFTER = dayafter("", "Intradiem moves people, breaks and training during the day on top of the WFM your teams already run.", "where carriers usually find the first measurable piece on the service side")
HAR_FINAL = final("the service side carrying the unpredictable work at The Hartford", "is that a this-year question for your team, or a next-year one?", "then")
add(C,CID,"seq_jG8aiuxE8FCQD564C","stp_MwwcFRGtWS9GY9yoJ","Email 1 (A/B)","the claims side of the AI number",HAR_E1, dict(subject="the claims side of the AI number", message=HAR_E1_B))
add(C,CID,"seq_DrLnaPQw4KjR3tobM","stp_NeBRHt488XSHbLmvB","LinkedIn message after connect",None,HAR_LI)
add(C,CID,"seq_DrLnaPQw4KjR3tobM","stp_6TkpGJRtRv7XLryaQ","Call 1 (no voicemail)",None,HAR_CALL1)
add(C,CID,"seq_DrLnaPQw4KjR3tobM","stp_Exk874hWjGJzWJzPx","Call 2 (voicemail)",None,HAR_CALL2)
add(C,CID,"seq_DrLnaPQw4KjR3tobM","stp_un4Y4stcgJFjSNamu","Email 2 (connect branch)","re: the claims side of the AI number",HAR_E2)
add(C,CID,"seq_DrLnaPQw4KjR3tobM","stp_usGHSFy2jjRRP2LGF","Email 3 breakup (connect branch)","re: the claims side of the AI number",HAR_E3)
add(C,CID,"seq_Pa7JYyP45rAyP5vnk","stp_5sNTrLPNrS7xqfobc","Voicemail (no connect)",None,HAR_VM_STEP)
add(C,CID,"seq_Pa7JYyP45rAyP5vnk","stp_DDWtmpJcGb4sMfvAm","Call day after voicemail",None,HAR_DAYAFTER)
add(C,CID,"seq_Pa7JYyP45rAyP5vnk","stp_2EyhwKb8irsw8MKEq","Email 2 (no-connect branch)","re: the claims side of the AI number",HAR_E2)
add(C,CID,"seq_Pa7JYyP45rAyP5vnk","stp_cxk2ntRzbzNHukCRr","Final call",None,HAR_FINAL)
add(C,CID,"seq_Pa7JYyP45rAyP5vnk","stp_Z2p2cDvkmJwtAPPcX","Email 3 breakup (no-connect branch)","re: the claims side of the AI number",HAR_E3)
add(C,CID,"seq_mZ3DFWrsQHiu623Ai","stp_BCcEf8PwC4Qn6vZb9","Email 2 (no-LinkedIn branch)","re: the claims side of the AI number",HAR_E2)
add(C,CID,"seq_mZ3DFWrsQHiu623Ai","stp_2ek52DPKmHsRbQfbQ","Email 3 breakup (no-LinkedIn branch)","re: the claims side of the AI number",HAR_E3)

# ---------------------------------------------------------------- Blitz, Citizens
C = "Blitz - Citizens (Nate)"; CID = "cam_yWefPqaDhNNv4RyQK"
CIT_OPEN = ("Citizens has said publicly it wants a quarter of calls answered without a person by the end of this year, on "
            "the way to half. Every deflection program hits the same second problem. The calls that still reach a person are "
            "the hard ones, so handle time goes up, and the easy volume that used to give the schedule some slack is gone.")
CIT_PROD = ("That's what Intradiem does. It sits on top of the WFM and phone system your service teams already run and moves "
            "people, breaks and coaching during the day as the mix changes, instead of fixing it the next morning. " + BANK)
CIT_E1 = P("Hi {{firstName}},", CIT_OPEN, CIT_PROD,
           "Worth a conversation on how you're planning the human side of that shift?", OPT, "Nathan")
CIT_E1_B = P("Hi {{firstName}},", CIT_OPEN, CIT_PROD,
             "Would it help if I sent a short note on what teams usually run into on the human side once deflection is live? "
             "No meeting attached, I'll just send it.", OPT, "Nathan")
CIT_LI = ("Thanks for connecting, {{firstName}}. Short version of my email: once AI takes the easy half of the calls, the "
          "half that's left is the hard ones, and the schedule has no slack to absorb the change. Intradiem moves people, "
          "breaks and coaching during the day on top of the WFM you already run. Worth a conversation on how you're planning "
          "that side of it?")
CIT_E2 = P("Hi {{firstName}},",
  "One thing I didn't say clearly in my first note. A quarter of calls by year end puts the change inside the next two "
  "quarters. The part that has to be managed in the moment, not in the next morning's report, is the human queue "
  "underneath it. That's the specific thing Intradiem does. It reads the WFM and phone system you already have and moves "
  "people, breaks and coaching as the mix changes during the day.",
  "Humana runs it that way and gets handle time down 45 seconds and about two hours back per agent per month.",
  "Would twenty minutes be useful on what the human side usually looks like once deflection is running at scale?", "Nathan")
CIT_E3 = P("Hi {{firstName}},",
  "I'll stop here. A deflection program gets judged on the half that goes away and decided by the half that stays. If "
  "that half becomes a live question at Citizens, this quarter or next, reach out.",
  "Good luck with the rollout.", "Nathan")
CIT_INSIGHT = ("Once AI takes the easy half of the calls, the half that's left is the hard ones, so handle time goes up and "
  "the schedule has no slack to absorb it. Intradiem sits on top of the WFM and phone system your teams already run and "
  "moves people, breaks and coaching during the day as the mix changes. One large North American bank measured $6.1M a "
  "year in savings with it.")
CIT_CALL1 = call1(CIT_INSIGHT, "Is that anywhere near how it plays out at Citizens?", "what the human side usually looks like once a deflection program is running at scale")
CIT_VM = vm("Intradiem sits on top of the WFM your service teams already run and moves people, breaks and coaching during the day as the call mix changes.")
CIT_CALL2 = call2(CIT_VM, "the insight, what Intradiem does, the bank number")
CIT_VM_STEP = vmstep(CIT_VM, "the insight, what Intradiem does, the bank number")
CIT_DAYAFTER = dayafter("", "Intradiem moves people, breaks and coaching during the day on top of the WFM your teams already run.", "what the human side looks like once a deflection program is running at scale")
CIT_FINAL = final("what happens to the calls that are left at Citizens once AI answers the easy ones", "is that a this-year question for your team, or a next-year one?", "then")
add(C,CID,"seq_vWS3ceMs5oh8YB6E5","stp_scn8zBoQtoAuP9AgE","Email 1 (A/B)","the half that's left",CIT_E1, dict(subject="the half that's left", message=CIT_E1_B))
add(C,CID,"seq_d8BtwftFedbCAdGvY","stp_4oFHeJmAEYrh6bXHD","LinkedIn message after connect",None,CIT_LI)
add(C,CID,"seq_d8BtwftFedbCAdGvY","stp_n6TyMNxkjuvkZrPqm","Call 1 (no voicemail)",None,CIT_CALL1)
add(C,CID,"seq_d8BtwftFedbCAdGvY","stp_usi9YgduCawPoMniK","Call 2 (voicemail)",None,CIT_CALL2)
add(C,CID,"seq_d8BtwftFedbCAdGvY","stp_t4YyNH3bvLP7dZWgM","Email 2 (connect branch)","re: the half that's left",CIT_E2)
add(C,CID,"seq_d8BtwftFedbCAdGvY","stp_jdBdpZdERe7eSTobo","Email 3 breakup (connect branch)","re: the half that's left",CIT_E3)
add(C,CID,"seq_rButuj6uT9QfZJunq","stp_oewTS8bXHTpAgwavt","Voicemail (no connect)",None,CIT_VM_STEP)
add(C,CID,"seq_rButuj6uT9QfZJunq","stp_T8KzCY7Fq7q66BvnQ","Call day after voicemail",None,CIT_DAYAFTER)
add(C,CID,"seq_rButuj6uT9QfZJunq","stp_5a4AbeFcXpjRTAmcR","Email 2 (no-connect branch)","re: the half that's left",CIT_E2)
add(C,CID,"seq_rButuj6uT9QfZJunq","stp_kEt8LTw26BYBezMZc","Final call",None,CIT_FINAL)
add(C,CID,"seq_rButuj6uT9QfZJunq","stp_MmRkH4eX4LAQuQ2hC","Email 3 breakup (no-connect branch)","re: the half that's left",CIT_E3)
add(C,CID,"seq_vTyQc2EYYDgHSY8vp","stp_ZNej6Ez543J6P5vmu","Email 2 (no-LinkedIn branch)","re: the half that's left",CIT_E2)
add(C,CID,"seq_vTyQc2EYYDgHSY8vp","stp_QQRXiaQzdQYekGZ4H","Email 3 breakup (no-LinkedIn branch)","re: the half that's left",CIT_E3)


if __name__ == "__main__":
    import json, re, sys
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print(json.dumps(U, indent=1)); sys.exit()
    def txt(h):
        h = (h or "").replace("<p><br></p>", "\n"); h = re.sub(r"</p>", "\n", h); h = re.sub(r"<[^>]+>", "", h)
        return re.sub(r"\n{3,}", "\n\n", h).strip()
    def wc(h): return len(re.findall(r"[A-Za-z0-9'{}$.,%]+", txt(h)))
    print("# Nate campaign copy rewrite (Sep 3 2026)\n")
    print("> Every email, LinkedIn message and call script on the four paused campaigns plus the Quality draft, rewritten under the Sep 3 doctrine in plain spoken language. Each Email 1 opens on the plan's own CMS number or the account's public signal, says who Intradiem is and what it does by the second paragraph, carries one verified proof, and ends on one question with no calendar in it. Paragraphs are separated by real blank lines in lemlist. Campaigns stay paused until Nate has read this.\n")
    cur = None
    for u in U:
        if u["campaign"] != cur:
            cur = u["campaign"]; print(f"\n## {cur}\n")
        print(f"### {u['label']}")
        if u["subject"]: print(f"**Subject:** `{u['subject']}`\n")
        body = txt(u["message"]); words = wc(u["message"]) if u["subject"] else None
        print("\n".join("> " + l for l in body.split("\n")))
        if words: print(f"\n*{words} words*")
        if u.get("variantB"):
            print(f"\n**Variant B (offer note close):**\n")
            print("\n".join("> " + l for l in txt(u["variantB"]["message"]).split("\n")))
        print()
