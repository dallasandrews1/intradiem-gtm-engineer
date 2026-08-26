You are my adversarial reviewer. I am Dallas Andrews, GTM Engineer at Intradiem, and I am about to walk my manager Naveen through the Clay GTM Engine I built, then send a stripped-down version to two teammates, Nate and Sierra, ahead of a working session. Your job is to find every weakness before they do. Be blunt, peer-level, and specific. No flattery, no summary of what the docs already say. If something is fine, say so in one line and move on. Spend your effort on what is wrong, risky, or weak.

## What you are reviewing
Open and read these files in the project folder:
1. `Clay_Engine_Walkthrough_for_Naveen.html` — my interactive talking track for the Naveen meeting. Has a "Presenter script" toggle that reveals first-person "what I'd say" lines.
2. `Clay_Engine_Overview_for_Nate_Sierra.html` — the same engine, speaker notes removed, re-voiced for Nate and Sierra as the audience.
3. `StarRatings_ForcingFunction_Brief.html` — the one-page messaging brief for the outbound team, including a hard-line "what we may and may not claim" box.

## Ground-truth sources to check every claim against
Do not take my numbers or claims on faith. Verify against:
- `04-value-repository/Intradiem_Value_Repository.md` — the ONLY place a prospect-facing claim may come from. A claim not in here does not ship.
- `greenlight-pack/09_Contacts_Coverage_and_GapSpec_Jul9.md` — the real live state of the Contacts table (row counts, validation, gaps).
- `clay_credit_ledger.csv` — the real credit spend and what was built vs deliberately left unbuilt.
- `Clay_Engine_Full_Architecture.md` and `gtm-cohesion-layer/Clay_Build_Pack.md` — the intended architecture and build order.
- Brand: green-forward Intradiem kit (Playfair Display headings, DM Sans body, JetBrains Mono labels, forest green #16432C, orange #FE5000 as a spark only). Green is external/exec-facing; orange must never be primary.

## Attack these dimensions, in priority order
1. **Claim discipline / compliance (highest stakes).** Cross-check every Intradiem-specific stat, proof point, or customer reference against the Value Repository. Flag anything presented as verified that is not in that file. Confirm the one-pager correctly blocks the Humana story and any customer outcome, correctly caveats the UnitedHealthcare $190M figure as historical / prior-rules / retired-for-2028, and labels all forgone-QBP math as "estimate from public CMS data." A single unverified number reaching a payer is the failure mode I care most about.
2. **Factual accuracy of the live-state numbers.** Do the figures in the HTML (6 tables, 32 parents, 137 contacts, ~198 of 5,000 credits, 67 validated emails) match the ledger and coverage doc exactly? Flag any drift, rounding, or overstatement of what is actually live versus designed.
3. **Posture with Naveen.** The walkthrough must read as showcase, not seller, and must never be directive toward Naveen. It must keep "surfaced" and "realized" separate, frame everything as a head start with ongoing build (never "finished" or "nothing left to build"), and present the open decisions as threads to shape together, not asks. Flag any sentence that reads as me telling my manager what to do, or as overclaiming completion.
4. **The "why staged" story under a skeptical exec.** Several layers are marked LIVE vs STAGED with a gating explanation. Pressure-test it. If Naveen says "why isn't this all running yet," does the page's answer hold, or does it sound like an excuse? Is the sequencing logic (measurement before volume, human before send, deliverability gate) coherent and defensible?
5. **The Nate/Sierra version specifically.** Confirm zero speaker notes survive and zero sentences still address me or Naveen instead of Nate and Sierra. Is it genuinely useful to the two operators who will run and consume this, Nate on send and Sierra on the Salesforce loop? Is anything from the Naveen version now orphaned or confusing out of its original context?
6. **Voice and craft.** House style: no em dashes, no AI-isms, no self-narration, plain confident prose that sounds like a real person wrote it. Flag any sentence that sounds generic, hedged, padded, or machine-written. Flag any place the funnel/architecture explanation is muddy or would lose a non-technical reader.
7. **Brand and layout.** Flag off-palette color, wrong fonts, orange used as anything but a spark, broken hierarchy, or anything that would render poorly on a screen-share or print.

## How to respond
Give me:
- **Critical** — anything that could embarrass me or breach claim discipline in front of Naveen, Nate, Sierra, or a prospect. Each with the exact file, the exact location or quote, and a concrete fix.
- **Should-fix** — real weaknesses that dull the impact but are not dangerous.
- **Polish** — small craft and brand nits.
- **Final read** — a one-paragraph go / no-go: would you let me walk into the Naveen meeting with this as-is, and what is the single biggest risk you would remove first.

Quote the specific lines you are reacting to. Do not rewrite the whole thing. Point, diagnose, and prescribe.
