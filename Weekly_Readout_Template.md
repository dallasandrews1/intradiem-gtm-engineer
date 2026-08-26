# GTM Engine Weekly Readout — Week of [DATE]

*Prepared by Dallas Andrews · Star Ratings motion · sent every [Friday] · same numbers feed pipeline council*

## Activity (by persona lane)

| Lane | Sends | Bounces | Replies | Reply rate |
|---|---|---|---|---|
| Persona 1 · Stars/Quality | | | | |
| Persona 2 · Finance | | | | |
| **Total** | | | | |

Source: each campaign's **Analytics** tab (campaign = persona lane, so per-persona splits are native). Deliverability = bounces + warmup health from the sender account view.

## Funnel

| Stage | Count | Notes |
|---|---|---|
| Replies | | rows with any reply_status set |
| Qualified conversations | | reply_status = qualified or meeting |
| Meetings booked | | reply_status = meeting |

Source: Contacts (Buying Committee) → filter on **reply_status** (last column). Blank = no reply yet. A row is marked when the reply lands, upgraded when it qualifies, upgraded again when a meeting books — statuses only move forward.

Qualified = a target persona engaging on the problem. Auto-replies, referrals, and polite declines stay at "reply."

## Spend

| Metric | This week | Motion to date |
|---|---|---|
| Credits (GTM Engine workbook line) | | / ≤1,900 projected |
| Cost per qualified reply (credits ÷ qualified) | | |

Source: Settings → Usage → **Workbooks** tab, GTM Engine line only (workspace total includes other workbooks). Cross-log in clay_credit_ledger.

## Against the plan

Full-motion planning ranges: replies 6–11 · qualified 3–7 · meetings 2–4 (floors survive at n=143; don't judge Wave 1 alone).

Rule check this week: **[GREEN / YELLOW / RED]**
- Green: deliverability clean, replies landing in either lane → scale to remaining Tier A/B contacts on winning copy
- Yellow: replies not qualifying or one lane outperforming → kill weak variant, rebalance, re-run
- Red: full-motion reply rate under 3% with deliverability green → stop sends, rework, no volume until the math works

## Notes / decisions needed

-

---

### Runbook (not part of the sent readout)

1. **Opens are not tracked, on purpose.** Both campaigns send plain text (Enable HTML off). Open/click tracking requires HTML, which Clay itself warns hurts cold-outbound deliverability — and open rates are unreliable anyway (Apple Mail privacy inflates them). Report sends, deliverability, and replies; never promise opens.
2. **Marking the funnel:** when a reply lands (campaign Replies tab or Nathan's inbox), find the row in Contacts and set reply_status. This is the one manual step in the loop; do it same-day so Friday pulls are trivial.
3. **Upgrade path once sending starts:** the campaign's "Create events table" button materializes send/reply events as a Clay table — flip that on after launch if you want the activity table auto-filled instead of read from Analytics.
4. **Never open P1's Setup or click Save campaign on P1** (stale source edit floods it). All settings verification happens on P2.
5. Bounce/complaint spike = deliverability gate closed; pause sends regardless of week's plan.
