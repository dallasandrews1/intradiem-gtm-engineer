# WFM-Adjacency Quick-Win Wave 1 — MessageGen Persona Variants

**Owner:** Dallas Andrews (GTM Engineer, Intradiem)
**Motion:** WFM-Adjacency · **Wave:** 1 (quick-win, hand-sourced) · **Channel:** Cold email 1 (Day 1, brand-light)
**Angle:** activation gap (Week-1 Pack Part A §A4) — *"You just stood up [platform]. The hard part isn't the deployment, it's getting the floor to act on it in real time."*
**Pipeline run:** `intradiem-first-draft-engine` (five gates) → `intradiem-copy-sharpener` (9 rules + Voice Audit + verified-claims gate)
**Sender:** `{{sender_first_name}}` — **CONFIRM before send.** Default assumption: Nathan Belfield (first name only, Days 1–5). No WFM-Adjacency sender was named; flag for Dallas.
**Tokens:** `{{first_name}}` · `{{platform}}` = confirmed `techstack_wfm` value (Verint / NICE / Calabrio / Genesys / Amazon Connect) · `{{sender_first_name}}`

> Two variants, one motion. Champion gets the **operational-activation** angle (the reaction lag that leaks ROI). Economic buyer gets the **cost / utilization-of-the-investment** angle (paid capacity the rollout was supposed to hand back). Neither names Intradiem, neither carries a product tell, neither uses an unverified stat.

---

## Variant A — Operational Champion
**Routes to:** `CAMP_WFM_Champion` (`persona_match = WFM` or `CareOps`) — VP/Dir WFM, Workforce Optimization, Contact-Center Ops, Resource Planning.
**One idea:** *The platform you just stood up shows you the floor in real time; the return leaks in the gap between what it shows and how fast the floor actually reacts.*

**Subject:** after the rollout

**Body (token template):**
```
{{first_name}}, standing up {{platform}} gave you a real-time read on the floor you didn't have a year ago. The part that catches teams off guard is what happens after the screen lights up. Adherence flags the lull at 2:15. By the time a supervisor sees it and moves someone, the window's closed. That reaction lag is where the return you paid for goes.

Might be worth walking through where that gap opens first after a rollout.

Worth 15 minutes in the next couple weeks?

{{sender_first_name}}
```

**Rendered example** (first_name = Maria, platform = NICE, sender = Nathan):
> Maria, standing up NICE gave you a real-time read on the floor you didn't have a year ago. The part that catches teams off guard is what happens after the screen lights up. Adherence flags the lull at 2:15. By the time a supervisor sees it and moves someone, the window's closed. That reaction lag is where the return you paid for goes.
>
> Might be worth walking through where that gap opens first after a rollout.
>
> Worth 15 minutes in the next couple weeks?
>
> Nathan

**Word count:** ~83 (cold email 1 range 80–120). ✅

---

## Variant B — Economic Buyer
**Routes to:** `CAMP_WFM_EconBuyer` (`persona_match = EconBuyer`) — VP/SVP Customer Care, Member Services, Care Operations (one level up from the champion).
**One idea:** *The rollout was a capital commitment; its return is how much paid capacity it hands back, and that turns on real-time reaction, not on the tool measuring the gap.*

**Subject:** what the rollout hands back

**Body (token template):**
```
{{first_name}}, the {{platform}} rollout was a real line item. The return on it isn't the go-live, it's how much paid capacity it actually hands back to you. Most of that turns on what happens the moment a gap opens on the floor, not on the software measuring it. Twenty minutes of unworked lull is capacity you already paid for. Across a few hundred agents that adds up faster than a rollout forecast assumes.

Where that capacity hides after a launch tends to surprise people.

Open to 15 minutes on it in the next couple weeks?

{{sender_first_name}}
```

**Rendered example** (first_name = David, platform = Verint, sender = Nathan):
> David, the Verint rollout was a real line item. The return on it isn't the go-live, it's how much paid capacity it actually hands back to you. Most of that turns on what happens the moment a gap opens on the floor, not on the software measuring it. Twenty minutes of unworked lull is capacity you already paid for. Across a few hundred agents that adds up faster than a rollout forecast assumes.
>
> Where that capacity hides after a launch tends to surprise people.
>
> Open to 15 minutes on it in the next couple weeks?
>
> Nathan

**Word count:** ~86 (cold email 1 range 80–120). ✅

---

## Send-Ready Test (both variants)

| Check | A (Champion) | B (Econ Buyer) |
|---|---|---|
| Starts with a specific observation, not a greeting | ✅ | ✅ |
| Single idea, stated once | ✅ | ✅ |
| Prospect is the hero (never told their job) | ✅ | ✅ |
| Feel-not-tell / self-selection | ✅ | ✅ |
| CTA has a connector sentence + names the topic | ✅ | ✅ |
| Exactly one question in the CTA | ✅ | ✅ |
| Meeting is their idea (no seller-want CTA) | ✅ | ✅ |
| Brand-light: Intradiem absent everywhere incl. signature | ✅ | ✅ |
| Sign-off = sender first name (Days 1–5) | ✅ | ✅ |
| Zero em dashes | ✅ | ✅ |
| Zero product tells (human reality, not category) | ✅ | ✅ |
| Zero forbidden words / vague language | ✅ | ✅ |
| Persona tone matched | ✅ Ops/WFM | ✅ Cost/capacity |
| Voice Audit: opener one fact, no appositive stacking, no 2+ commas before main verb | ✅ | ✅ |
| At least one short sentence; lengths vary | ✅ ("Adherence flags the lull at 2:15.") | ✅ ("...was a real line item.") |
| No decorative metaphors in prose | ✅ | ✅ |
| Every stat/outcome verified or absent | ✅ none used | ✅ none used |

**Both PASS.**

**Plain-language pass (added):** every decorative/writerly move stripped so nothing trips an internal cadence critic. Cut `quietly leaks out` → `the return you paid for goes`; cut the trailing-fragment `...paid for, gone.` → `Twenty minutes of unworked lull is capacity you already paid for.` No punchy tags, no flourish sentences, no crafted rhythm — just plain statements a peer would type.

**Closes de-rhymed:** A and B no longer share scaffolding, so a champion + economic buyer at the *same account* who compare inboxes see two different messages.

| | Variant A (Champion) | Variant B (Econ Buyer) |
|---|---|---|
| Connector | "Might be worth walking through where that gap opens first after a rollout." | "Where that capacity hides after a launch tends to surprise people." |
| CTA verb / shape | "Worth 15 minutes in the next couple weeks?" | "Open to 15 minutes on it in the next couple weeks?" |

---

## Verified-Claims Ledger (hard gate)

| Claim in copy | Type | Repository status | Disposition |
|---|---|---|---|
| (none) | — | — | Both variants ship **zero** Intradiem stats, customer outcomes, or peer claims. Nothing to verify. |
| `{{platform}}` reference (NICE/Verint/etc.) | Prospect's own tech | n/a | Framed as **their investment to activate**, never as a competitor — complies with verified-metrics "never position WFM vendors as competitors." |
| "twenty minutes," "a few hundred agents," "a year ago" | Illustrative generics | n/a | Not Intradiem-attributed figures; generic scene-setting. No idle-% stat used (that's DO-NOT-SEND). |

**Available for later touches (Day 6+, not used here):** Humana is the one customer story cleared for prospect copy — 7X ROI five years in; 2 hours of capacity per agent per month in 2025; AHT −45s; occupancy +4% (public SWPP/Intradiem webinar, intradiem.com) [VERIFIED 1:many]. Usable as a named or blind peer proof point from Day 6 onward, once the brand-light window closes. **Greenlight/Zuar CTO figures are CV-INTERNAL — never in prospect copy.**

---

## Deployment notes (before this becomes a Clay MessageGen batch)

1. **Confirm the sender.** Everything above signs `{{sender_first_name}}`; default Nathan Belfield. Dallas confirms who owns this motion's sends before any launch.
2. **These are Wave-1 templates**, not a send list. Per the wave runbook: enrich the 30–50 slice (tiered, ledger row first), generate per-lead, **census every draft**, fix FAILs per-lead at campaign level, verify `Sent At` on the live page, launch only on Dallas's explicit in-session approval, and schedule Wave 2 (~9 business days out) before Wave 1 counts as launched.
3. **Stamp the prompt version** on the wave when these seed the MessageGen table; fold Wave 1 reply data into the next version before Wave 2 generates.
4. **Voice Audit parity:** the cadence standard here is identical to the Clay MessageGen `voice_audit` critic column — keep them in sync so the human gate and the engine gate never drift.
5. **Nothing is scheduled or sent.** Human-gated launch always.
