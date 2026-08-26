# BOO Launch — Instrumentation Plan (v0)

Measurement before volume: nothing activates until every row entering the motion is countable.

## Source tags (already enforced by the pull spec; verify at launch)

Every contact in the launch motion carries: `source_motion = back_office_boo` for the net-new BOO universe vs `back_office_install_base` for Mandate 3 expansion (do not conflate: the first keeps customer exclusion ON, the second inverts it) · `universe` · `persona_key` · `parent_account` · `sourced_date` · `source` · `owner_cleared` · `fo_risk_flag`. The 59-row sample already carries all of these (added Jul 14).

## Baselines (set before launch week, from engine_state.json + Clay)

- Accounts: Tier-1 count (56), owner-cleared count (0 today — the Scott/AE review is the unlock), suppressed count.
- Contacts: sourced (59 now, ~200 at scale), email-valid rate (81% in sample: 48/59), dup rate vs Contacts (1/59).
- Zero-line: replies, meetings, opps all start at 0 in outcomes.csv; surfaced vs realized never blended.

## What week-2 retro measures

Deliverability (bounce < 2%, no spam flags) · reply rate by persona lane · reply category mix (Reply Engine v1 logs) · owner-clearance velocity (how many of the 56 cleared) · which Touch generates replies · kill list: any lane under X% positive-reply signal after full cadence (X set with Naveen at launch, provisional not defended).

## What week-6 retro measures

Meetings per lane · cost-per-qualified-reply (credits + sends per qualified reply; credit-steward computes) · signal-fired vs base-only conversion (does the intent layer actually predict?) · scale/kill/retool call per lane, appended to this folder and fed to the Friday readout.

## Credit budget (clay-credit-steward pre-check, ledger-logged)

- Persona pull to 200: **~300 credits measured** (59-contact sample ran at 86 credits ≈ 1.46/finished contact; meter-verified Jul 14, favorable >25% drift from the 600-900 estimate, re-estimate logged).
- Monthly back-office signal sweep: est ~11 credits/parent × 56 Tier-1 parents ≈ 620/mo — HELD until launch go; pre-estimate against live provider pricing at run time (meter is the authority).
- All spend appends to `Clay_Credit_Ledger.md` before it fires; workspace budget 5,000/mo, flag at 3,000.

## Fail-closed checklist before first send

- [ ] Instrumentation columns verified on every row entering a campaign
- [ ] Deliverability green (Nathan's mailbox warmup complete — ETA due from Nathan Wed Jul 15)
- [ ] owner_cleared TRUE for every account in the load list
- [ ] Reply Engine v1 SOP live; bdr_claimed gate behavior re-verified
- [ ] Sequences passed copy-sharpener + verified-metrics; approvals logged
