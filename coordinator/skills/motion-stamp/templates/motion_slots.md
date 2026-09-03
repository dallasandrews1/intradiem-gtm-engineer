# Motion Slots (fill one per motion)

Copy this file to a new motion's build folder and fill every slot. The filled slots + voice_core + stage_ladder assemble the 5 stage prompts. WFM-Adjacency is the worked reference (see WFM_Email2to5_Stage_Prompt_Build_Sheet.md and the live P2P Outreach Email prompt).

## MOTION_KEY
(snake_case, e.g. `wfm_adjacency`, `star_ratings`, `back_office`) — used in the Source Motion check.

## SOURCE_MOTION_CHECK
> Verify Source Motion equals "<MOTION_KEY>". If NOT, return exactly: {"subject": "ERROR wrong motion", "body": "ERROR wrong motion"}

## WHO YOU ARE
The peer the email sounds like (role + fluency). WFM example: "A GTM engineer who knows what a WFM platform does and what it doesn't. Fluent in occupancy, shrinkage, adherence, intraday, service level."

## THE CORE POSITION (never violate)
The product wedge in one paragraph: what the prospect already runs, the specific gap, what our product does about it, and the additive framing (never rip-and-replace, never trash the incumbent). WFM example: "Intradiem is an execution layer on top of the WFM platform they already run; WFM schedules the day but doesn't act in the idle gaps; Intradiem fills those minutes in real time without changing the stack. Never frame their WFM as failed."

## THE ONE IDEA (constant across all 5 touches)
One sentence. WFM example: "WFM schedules the day but can't act in the idle minutes between scheduled activities; that idle capacity is recoverable in real time on top of the stack they already run."

## PERSONA ROUTING (the persona_key rubric for this motion)
For each persona_key value, one line on how to lead. WFM example: wfm → lead with the mechanism in their language; cc_ops → lead with the floor outcome; coo_finance → lead with operational leverage, bookable this period.

## SIGNAL SEMANTICS
What a valid signal means for this motion and how to reference it qualitatively when unsourced. WFM example: the operational moment (idle gap after an early wrap, coaching pull-offs, back-office queue uncovered).

## MOTION-SPECIFIC BANS
Framings this motion must never use. WFM example: never characterize their WFM/CCaaS platform (Verint, NICE, Calabrio, Genesys, Amazon Connect) as unable, slow, or lacking; never cite a competitor or customer number by hand.

## PRODUCT SENTENCE (replaces the old brand convention, Sep 3 2026)
The one concrete sentence E1 uses to say what Intradiem does in this motion, on top of what the prospect already runs. Intradiem named once. Concrete actions, never a category label. Rewrite it from Naveen's messaging document when it lands. Back-office example: "Intradiem sits on top of the case system and the WFM you already run and moves the work inside the day: it spots idle windows as they open, routes aging cases into them, and pushes training and admin into the quiet hours instead of the busy ones."

## E1 CLOSE SHAPE
Benchmark question ("Worth a conversation on how other [persona] teams run this?") or offer note (name the note in motions/shared/Offer_Notes_Aug3.md). Never a calendar ask in E1.

## SENDER / SIGNATURE
Who sends (per motion). First name only, applied in the signature layer, not the MessageGen output; the mailbox signature block carries the rest.

## GOLD STANDARD (E1)
One fully-written Email 1 in this motion's voice that hits the whole arc with no fabricated number, as the cadence anchor for E2-E5.
