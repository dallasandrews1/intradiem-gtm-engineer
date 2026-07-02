# Message-Variant Starter Pack (Pilot Wk 3–4)
Three variants per segment — the "three message variants per segment" the Section 05 pilot calls for. Modeled on the **approved sample** (Kristen Dowd / Point32): short, one insight, a specific signal/number, humble framing, soft 15-min ask. `{{merge_fields}}` = personalization at scale from the Golden List.

**Rules baked in:** no fabricated stats — any Intradiem metric must come from the verified-metrics repository before sending. Human approval before anything leaves the building. Vary opener/angle so these read as different messages, not a template with swapped variables.

---

## SEGMENT 1 — Star Ratings · Stars/Quality leader (VP Medicare Stars, Dir Quality)

**Variant 1A — the cliff number (mirrors the approved sample):**
> Subject: {{plan_name}} + the 4.0 line
> Hi {{first_name}}, your weighted average looks to be right around {{qbp_avg}}, just under 4.0 — though you'll know the exact picture far better than I do. For plans sitting this close, the call center measures are often where the last few points come from.
> If useful, I'd value 15 minutes on how you're approaching your cliff-edge contracts.

**Variant 1B — the measurement-window angle:**
> Subject: the 2028 window
> Hi {{first_name}}, the Call Center measures (Foreign Language Interpreter, TTY) drop first but still count toward 2028 Stars across the 2026–27 measurement years — the cleanest attribution window left. For a plan near the line, that's the part still movable right now.
> Worth 15 minutes to compare notes on how you're playing it?

**Variant 1C — the new-leader / signal angle (fires on Tier-2 leadership signal):**
> Subject: congrats — and one thought
> Hi {{first_name}}, saw you {{recent_signal e.g. "stepped into the Stars program"}}. When the contract's sitting around {{qbp_avg}}, the fastest-moving points this cycle tend to be in the call center measures rather than the clinical ones.
> If it's useful early on, I'd value 15 minutes on where you're focusing first.

---

## SEGMENT 2 — Star Ratings · Finance leader (CFO, VP Finance)

**Variant 2A — bonus-dollars framing:**
> Subject: the bonus at {{qbp_avg}}
> Hi {{first_name}}, from the finance seat the 4.0 line is really a quality-bonus question — and {{plan_name}} looks to be sitting right under it at about {{qbp_avg}}. The measures still movable this cycle are mostly operational, not clinical.
> Open to 15 minutes on how you're modeling the cliff?

**Variant 2B — cost-of-inaction angle:**
> Subject: one cycle of margin
> Hi {{first_name}}, missing 4.0 by a fraction is the same financial outcome as missing it by a lot — one cycle of bonus either way. For contracts this close, the last few points usually come from the call center measures.
> Worth 15 minutes to pressure-test the numbers together?

**Variant 2C — SEC/earnings signal angle (fires on Tier-1):**
> Subject: re: your {{filing_or_call}} note on Stars
> Hi {{first_name}}, noticed Stars came up in {{filing_or_call}}. With {{plan_name}} near {{qbp_avg}}, the bonus exposure is real but the movable measures this cycle are operational.
> If useful, I'd value 15 minutes on how finance is framing it internally.

---

## SEGMENT 3 — Back office · Ops/WFM leader (install base — confirm ICP w/ Scott Kemme first)

**Variant 3A — install-base / off-the-phones angle:**
> Subject: the work off the phones
> Hi {{first_name}}, we already work with {{company}} on the front office — what we don't see yet is how the back office ({{function e.g. claims, enrollment}}) is handling its volume. Most teams have real-time orchestration on the phones and almost none of it behind them.
> Worth 15 minutes to hear how you're running it today?

**Variant 3B — backlog/SLA angle:**
> Subject: backlog vs. capacity
> Hi {{first_name}}, in most back-office operations the constraint isn't headcount, it's that idle and peak time aren't visible the way they are on the phone queues. Curious whether that's the picture in {{function}} at {{company}}.
> Open to 15 minutes to compare notes?

**Variant 3C — automation-initiative signal angle (fires on back-office signal):**
> Subject: re: your {{signal e.g. automation push}}
> Hi {{first_name}}, saw {{company}} is {{recent_signal}}. The piece that usually gets missed in those efforts is real-time orchestration of the people doing the work, not just the RPA on the tasks.
> If it's relevant, I'd value 15 minutes on where you're starting.

---

### Variant test design (Wk 3–4 → 5–6)
Launch all three per segment to matched samples, track to **qualified reply** (not open). Wk 5–6: kill the lowest, scale the winner, fold the winning angle into the follow-up agent. Log results to the dashboard by `source_motion`.
