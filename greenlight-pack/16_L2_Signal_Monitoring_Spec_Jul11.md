# L2 Signal / Intent Layer — build spec + reference implementation

Created Jul 11 2026. Updated Jul 12 2026 after the end-to-end red-team audit (`17_Clay_Build_Audit_2026-07-12.md`): customer-exclusion gate added to the live formulas, leadership weight and tier corrected, hiring threshold corrected, `claims_backlog` moved to the back-office motion, `measure_slippage` added, decay reframed as reference-only. Where this spec and the live Clay build ever disagree, the live build is ground truth.

## What L2 is

The intent layer of the Star Ratings cliff-edge motion. It lives as **enrichment and formula columns on the Accounts (Master) table in Clay**. External market signals fire point values into an account's `intent_score`, which layers on top of the L1 cliff-edge fit and can lift an account's grade or push it into outreach. The defining behavior is **self-cleaning**: an account that reaches 4.0, or that is an existing customer, no longer belongs in the new-logo motion, so its intent zeroes and it drops out. The list stays honest without manual pruning.

L2 is a Clay table layer, refreshed by Clay's own native column auto-update schedule. It is **not** a Claude scheduled task. What this repo holds is the exact build spec for those columns, a runnable reference implementation that proves the logic, and the credit governance around the refresh.

## The signal set (columns on Accounts (Master))

| Signal | Points | Tier | Velocity | Est. credits/acct | Source |
|---|---|---|---|---|---|
| `sig_sec_filing` | 30 | 1 fires | slow | ~3 | SEC full-text search, Stars/QBP language (public parents only) |
| `sig_earnings` | 25 | 1 fires | event | ~3 | earnings-call transcript scan (public parents only) |
| `measure_slippage` | 20 | 1 fires | slow | **0 (first-party)** | owned tiered CMS file, YoY movement on the call-center / CAHPS / complaints measures QO touches |
| `Use AI result` (leadership) | 10 | 2 raises | slow | ~2 | Clay "Use AI" (Claygent) web research, dated last-12-months quality/Stars/CAHPS/member-experience appointment |
| `Job Openings` (hiring) | 15 | 2 raises | fast | ~2 | job-postings enrichment, keyword-filtered, **>= 3** relevant reqs |
| `new_faller` (base) | 20 | 1 base | n/a | 0 | contract fell out of 4.0 this cycle; free base intent |

`claims_backlog` (10, Tier 2) was **moved to the back-office motion** on Jul 12. It is a back-office buying signal, not a Stars-cliff signal, so it no longer scores in the Star Ratings motion. It scores only when the config's `active_motion` is `back_office`.

**Tier 1** fires an account into outreach. **Tier 2** raises priority within the already-fired set. Leadership was demoted 20→10 points and Tier 1→Tier 2 on Jul 11-12: it is directional AI research that over-calls recency (the tightened Claygent prompt still returned "yes" on a plan-president role), so it nudges and is treated as a lead to verify, not an auto-fire.

## The rollup + self-clean (the two live formula columns)

`intent_score` (verified live Jul 12):

```
(Number({{overall_star_2026}}) >= 4 || {{customer_flag}} == "TRUE") ? 0 :
Math.min(100, ({{new_faller}} == "TRUE" ? 20 : 0)
  + ({{sig_sec_filing}} ? 30 : 0)
  + ({{sig_earnings}} ? 25 : 0)
  + (({{Use AI result}} && String({{Use AI result}}).toLowerCase().indexOf("yes") == 0) ? 10 : 0)
  + (Number({{Job Openings}}) >= 3 ? 15 : 0))
```

`intent_status` (verified live Jul 12):

```
{{customer_flag}} == "TRUE" ? "excluded"
 : (Number({{overall_star_2026}}) >= 4 ? "graduated"
 : (Number({{intent_score}}) >= 40 ? "grade_lift"
 : (Number({{intent_score}}) > 0 ? "in_motion" : "dormant")))
```

The kill switch is now two conditions: graduated (>=4.0) OR customer. This makes customer exclusion a property of the score, not a downstream convention, so a customer cannot leak into any intent-driven path. Four distinct states result: `excluded` (customer), `graduated` (>=4.0), `in_motion` (eligible with intent), `dormant` (eligible, no signal). Every paid enrichment column also carries a run condition `new_logo_eligible == "TRUE"` so credits never fire on a customer row.

Exact definitions, points, tiers, thresholds, and the `active_motion` switch: `intradiem-signal-engine/config/l2_intent_signals.json`. Edit values there, never in code or in the Clay formula text.

## Decay: reference-only, refresh-expiry live

The linear-decay model (full weight inside 30 days, down to a 0.4 floor by 120 days) lives in the **reference scorer**, not the live Clay formula. The live layer has no in-formula decay; it approximates staleness via **refresh-expiry** (a signal stays hot only while the monthly re-run still returns it). Do not claim in-formula decay in the live build. Add a per-signal date column later if true decay is needed on the live table.

## Refresh cadence (corrected Jul 12 to parent grain)

| Cadence | Columns refreshed | Scope | Est. credits |
|---|---|---|---|
| Monthly full | sec, earnings, measure_slippage (free), leadership, hiring | 26 eligible non-customer **parents** | ~260 |
| Weekly delta | hiring (fast mover) | top-tier parents | ~60 / wk |
| Event-triggered | full star set | around earnings weeks + October CMS release | ~260 / event |

**Steady state ≈ 520 credits/month**, well inside 5,000. The live table is contract grain (98 rows across 26 parents); running paid signals per contract would cost ~3x, so the go-forward model runs the paid signals once on a 26-row parent helper table and looks the result back onto contracts (Clay-internal lookups are free). Every run is pre-estimated and logged in `Clay_Credit_Ledger.md` before it fires.

## The reference implementation

The paid Clay columns are gated; the mechanic is mirrored in a runnable scorer so it can be demoed and validated:

- `intradiem-signal-engine/l2_intent_scorer.py` — reads the config + `data/l2_signals.csv` + `data/l2_accounts_stars.csv`, outputs per-account `intent_score` with the customer gate, new_faller base, motion filter, decay, and self-cleaning. Run: `python3 l2_intent_scorer.py`.
- `intradiem-signal-engine/test_l2_intent_scorer.py` — **37 checks** (up from 17): per-signal point contribution, customer exclusion, new_faller base, motion filter, decay, cap, rollup, config integrity. Green as of Jul 12.
- Live demo read (today): CareFirst at 4.0 auto-drops (graduated, 0); Humana at 3.5 with a faller and two signals worth 65 points is forced to 0 / excluded (customer gate beats everything); Clover at 58 and Devoted at 40 cross the grade-lift line; Point32's March hiring signal has decayed from 15 to 6; Medica's claims-backlog signal no longer scores (back-office motion). That is the self-cleaning list, visible, without the paid Clay columns being live.

## Build status in Clay (as of Jul 12 2026)

Live on Accounts (Master) (`t_0thuumoUcu6wAAhovti`), 98 contracts, auto-run Manual (zero credits):

- **`intent_score`** and **`intent_status`** — corrected live per the formulas above. Verified: all customer rows (Humana, UHC, CVS) now read intent 0 / `excluded`; eligible fallers stay `in_motion`; eligible-no-signal rows read `dormant`.
- **Hiring** term corrected to `>= 3` on the keyword-filtered count.
- **Vestigial checkbox columns hidden** — `sig_leadership`, `sig_hiring` (the formula reads the enrichment columns directly, not these), and `sig_backlog` (retired from the star motion).
- **Run condition** `new_logo_eligible == "TRUE"` added to the Job Openings enrichment so paid runs can never touch a customer row. (Leadership Claygent run-condition is a noted follow-up; the intent_score customer gate already makes its output inert on customers.)
- **Three signals now wired live:** keyword-filtered Company Job Openings (paid), the Claygent leadership web-research column (paid), and **`measure_slippage` (FREE, first-party CMS)** — built Jul 12 from the uploaded 2025 Star Ratings Data Tables (HD5 Customer Service / HD3 Member Experience domain stars + Summary Overall) joined to the 2026 universe by contract_id via `CMS_Star_Movement_25v26` + a Lookup Single Row + `sig_measure_slippage` formula; 22/98 fire, +20 in intent_score. Verified live: Clover 20->40 (grade_lift), Centene 15->35; customers stay 0/excluded. `sig_sec_filing` and `sig_earnings` stay as gated manual inputs until their native enrichments are wired.

The intent engine is correct, safe, and demoable now. Head start, ongoing build. What remains (paid, gated, held for explicit go): build the parent helper table, wire `measure_slippage` + `sig_sec_filing` + `sig_earnings`, run the first parent-grain sweep (~260), then turn auto-run back on.

## Guardrails

- **Customer exclusion is now in the score itself** (customer_flag in both formulas) AND in the enrichment run conditions — belt and suspenders. Never surface an `excluded` account in outreach.
- **No autonomous paid spend** — every refresh is pre-estimated and logged; the first paid run waits on an explicit go.
- **Config over code / formula** — all points, tiers, thresholds, motions live in `l2_intent_signals.json`.
- **Placeholder discipline** — credit figures are planning assumptions until confirmed against Clay's live per-provider pricing. No Intradiem-verified numbers live anywhere in this layer.
