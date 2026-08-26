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

## BRAND CONVENTION
A (brand-light Days 1-5) or B (product at most once from Day 1). WFM = B.

## SENDER / SIGNATURE
Who sends (per motion) and the sign-off flip (first name D1-5, full name D6+), applied in the signature layer, not the MessageGen output.

## GOLD STANDARD (E1)
One fully-written Email 1 in this motion's voice that hits the whole arc with no fabricated number, as the cadence anchor for E2-E5.
