# Star Ratings Wave 1 — First Batch, Send Guardrails, and the Proof Gap

Written Jul 13 2026, in response to the pre-mortem. This closes the two controllable failure modes (deliverability, addressability) and operationalizes the adaptation for the one that isn't controllable (no Stars proof). Read this before Nathan approves a single contact.

## 1. Addressability cut — who actually belongs in Wave 1

The core claim of the sequences is that the last half-star lives in the customer-service and CAHPS measures. That is true only for plans whose gap sits in those measures. Sending it to a plan whose gap is clinical burns the one cold open you get with a Stars leader who lives in her measure math. So the 26 eligible parents split three ways, from the `CMS_Star_Movement_25v26` first-party data (2025 HD5 Customer Service, HD3 Member Experience, and Complaints measures against the 2026 overall).

**Batch 1 — Priority (send first). measure_slippage fired: overall declined 2025 to 2026 AND a service measure at or below 3.0. The gap is fresh and it is in our lever.**

Centene, Devoted, Clover, Cambia, Zing, Baystate, ATRIO, Excellus (Lifetime Healthcare). 8 parents. Centene alone carries 13 sub-4.0 contracts with a service-measure weakness, so it is the anchor account.

Send-ready buyer contacts in Batch 1 are roughly 20, across seven of the eight parents. Two caveats to hold: **Excellus** buyer contacts are still email-dark, so hold Excellus until email is recovered; **ATRIO** finance (Kirkpatrick) email is still pending, so ATRIO leads with the verified Stars contact (Stone) until the CFO email lands. **Baystate** has a Finance contact but no clean Stars/Quality contact yet, so it runs the Finance lane only for now.

**Batch 2 — Addressable (second wave). Sub-4.0 with a service-measure weakness, but no fresh decline signal.**

CalOptima, L.A. Care, Medica, Clever Care, IEHP, VNS, Presbyterian, NYC Health + Hospitals, Community Health Plan of Washington, Blue Shield of California, Imperial, Point32Health, HMSA. 13 parents. These get the same sequences, one wave behind Batch 1.

**Hold / do not send the service-measure sequence. Their sub-4.0 gap is not in the customer-service measures, so the pitch does not fit.**

CareFirst, Lumeris, Mass General Brigham, GuideWell. 4 parents. Their service measures are already strong; whatever is holding them under 4.0 is on the clinical or HEDIS side, which Queue Optimizer does not move. Do not run them through Wave 1. Either drop them or hold for a different angle. Sending them the service-measure story is the fastest way to look like a vendor who did not do the homework.

**Verify before sending: Solis Health Plans.** Not present in the CMS movement file (too small or newer to the set). Confirm its measure profile before it goes in either batch.

## 2. Deliverability guardrail — the number that was missing

The single biggest silent failure is one warming mailbox pushed past what it can carry, so the tool reports "delivered" while the messages sit in spam. Hard rules for Nathan:

- **Daily send ceiling, one mailbox:** start the first live week at ~20 cold sends per day, ramp to a ceiling of ~40 per day only if bounce and complaint rates stay clean. Never exceed ~40 on a single mailbox. To go past that volume, add mailboxes and domains, do not push one mailbox harder.
- **Size the batch to the ceiling, not the list.** Batch 1 is ~20 send-ready contacts. Enter two to three accounts per day, staggered (Stars/Quality contact first, Finance one to two days behind), so daily sends stay under the ceiling and the committee still hears a coherent story inside a week. Do not flip all of Batch 1 to READY at once.
- **Tripwires, checked in week 2 of live send:**
  - Daily send count over ~40 on one mailbox: stop adding accounts.
  - Bounce rate over 2 to 3 percent: pause, the list or the mailbox needs a look before more sends.
  - Any spam-complaint signal: pause immediately, reputation damage compounds and is hard to reverse.
- **Do not read a low reply rate as a copy or targeting failure until deliverability is ruled out.** Check inbox placement first. A near-zero reply rate on a young domain is almost always placement, not message.

## 3. The proof gap — what to do about the thing you cannot control

There is no verified Intradiem Stars-movement reference. The value repository has a blinded efficiency proof (4.5X annualized ROI in the first quarter, roughly 1,700 agent hours freed) but nothing that says "we moved a plan's Star Rating by X." That is a product-marketing and customer-success reality, not something GTM can manufacture. Three moves:

- **Set the goal of the motion at the discovery meeting, not a Stars guarantee.** The sequences ask for a fifteen-minute conversation about the prospect's own cliff. That is the right ask and it is deliverable. Do not let the copy or Nathan drift into implying a Stars outcome we cannot prove.
- **Answer the proof question honestly when it comes,** and it will come from any serious buyer. The handle is in the sequences doc: we do not claim a Stars number we have not verified; here is the efficiency proof and the mechanism; the meeting is to pressure-test whether that mechanism fits your specific measure gap. Honesty here is a feature to a regulated buyer, not a weakness.
- **Escalate the missing asset.** A Stars-specific reference is the one thing that unlocks conversion past interest. That is Tom Russell and Chris Busbee and customer success to produce, and it should be named as the gating asset now, not discovered at the first stalled deal. Draft flag below.

## 4. Internal flag to Naveen / Tom (draft)

> Quick flag on the Star Ratings motion as we get Nathan live. The outbound is built and the list is scoped to the plans whose gap is actually in the service measures QO moves, so the targeting is honest. The one asset the motion is missing is a Stars-specific outcome reference: a plan where we can say we helped move the rating, and by how much. Right now the strongest proof we can put in front of a Stars or Finance buyer is the efficiency story (4.5X ROI in a quarter, agent hours freed), which opens the conversation but does not answer the question every serious buyer asks: which plan's Stars did you move. We can generate interest and meetings without it. Converting past the proof gate needs it. Flagging now so it is a known gap we are working, not a surprise at the first stalled deal. Happy to help shape what that reference would need to say.

## What this changes in the launch

Nathan's first approved cohort is Batch 1, the eight priority parents (hold Excellus on email, Baystate is Finance-only), roughly 20 contacts, entered two to three accounts a day under a ~40-a-day mailbox ceiling. Batch 2 follows a wave behind. The four clinical-gap parents stay out of Wave 1. Solis gets verified first. The proof gap is named to Tom and Naveen, and the motion is measured on discovery meetings, not on a Stars promise it cannot yet back.
