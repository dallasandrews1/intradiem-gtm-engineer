---
name: gtm-cadence-sep8-next-steps
description: "Sep 8 2026 GTM cadence (Naveen, Genna, Sierra, Carter) outcomes and the follow-on Sep 9 DMs; 6sense fields verified populated in Clay Audiences; Tom cleared new sending domains Sep 9"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1100345b-bc86-4d17-919c-c44c462cffa7
  modified: 2026-09-09T19:40:22.904Z
---

**Sep 8 2026 GTM cadence call** (Otter SAEBLuEq0LX1XfNXxRQk3LbrqhY, 31 min; Naveen, Genna, Sierra, Carter, Dallas):
- Pipeline Council Thu Sep 10: Genna's advice is no hard numbers yet; present build-out, learnings, spend decisions. Naveen agreed.
- Credits: Dallas said ~14 percent consumed. Verified Sep 9: live balance 62,468.8; ledger's first read Jul 12 was 72,670.3, so GTM Engineering consumption is ~10,200 credits, 14.0 percent of the 72K pool, ~$710 at the ~$5K proof-budget rate (~$235/month over Jul 12 to Sep 9). The rundown's "21,178 consumed" counts pre-July use against the 83,836 ever made available; the council line is the 10.2K.
- Naveen: current lemlist campaigns are inbox warm-up and deliverability tests, not legitimate campaigns until messaging is fixed from marketing's guidance. Sierra to consolidate messaging guidance into one doc pointing at the customer-story spreadsheet; DWO exec messaging must combine front and back office; vertical guidance for BO (healthcare, FS, general/BPO, insurance under FS).
- Sierra: Optum can be name-dropped in email (not on the website); wants Optum and subsidiaries suppressed. CONFLICT: Value Repository (Sep 3) says only Humana and Virgin Media are "Cleared to use" by name; Optum is blinded. Needs reconciling before copy ships. Customer exclusion already holds Optum at parent level (Sep 5 load).
- 6sense: three predictive areas (profile fit, intent from 25 Bombora topics + keywords, reach). Keyword intent is company-level, scored nightly, never person-level unless cookied. Carter: fields already mapped to Clay. Sierra: technology-used field NOT mapped yet (she confirms). Sierra's proposed trigger path: 6sense audience segment per keyword group pushes to SF and fires a campaign.
- Naveen's ask to Dallas + Carter: an actionable mechanism where keyword intent (e.g. researching NICE DAA / Verint WFM) invokes a campaign within ~24h and shapes timing; what intent may and may not feed the message.
- Carter never logged into Clay (invite to resend).
- Genna: Eric (lemlist) connecting lemlist to SF ~Sep 9; she then maps fields. Genna asked Sep 9 13:42 "are you using SMS in lemlist?"

**Verified Sep 9 (0 credits):** Clay Audiences companies carry 6sense fields: Buying Stage 137/150 sampled, 6QA 150/150, Temperature 147/150, Intent Score 137/150, Profile Fit 137/150, "6sense Segments (2)" 96/150 with values like "6s - Top of Funnel". "6sense Segments" (first field) is empty. People carry Lead/Contact grade and intent scores. Field ids in the Audiences fields list (audf_0tkdv...). No saved audience uses them yet.

**Sep 9 DMs from Naveen:** start updating BO lemlist messaging from Sierra's doc (11:07); all-hands video: add a data-flow view (Clay, lemlist, ZoomInfo, 6sense into the sequencer) with motion graphics, drop "Nine campaigns, one engine", lean into AI; intro Jean Ann and Mike Regan at the all-hands; Naveen talking to Tom about a LinkedIn Ads seat; Tom cleared buying new sending domains (13:54), Dallas explained the 20-30/day mailbox mechanics.

**Why:** these are the live commitments from the cadence; the Sep 10 council and John meeting, the domain warm-up clock, and the messaging rewrite all key off them.
**How to apply:** order work as domain purchase first (longest lead time), Sierra's doc into the repo before any copy rewrite, Lead Source ticket raised while Genna maps lemlist to SF, 6sense trigger built as a Heat List family off the Segments (2) field. See [[signal-marketing-loop-strategy-aug25]], [[pipeline-council-context-aug24]], [[bo-lemlist-shells-built-sep2]].
