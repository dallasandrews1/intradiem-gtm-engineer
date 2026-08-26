# BOO Sequence Set — Skeleton (v0, not send-ready)

Persona-mapped outreach for the launch universe. **Nothing here is send-ready:** at compile time each lane's copy is generated through intradiem-first-draft-engine → intradiem-copy-sharpener → intradiem-verified-metrics, in that order, with brand-light rules (Intradiem out of Touch 1-3 bodies) and the humility clause on any modeled number. This file fixes the architecture so the copy compile is mechanical.

## Universe

Tier 1 of `BackOffice_Target_Universe_v1.csv` (56 accounts), contacts from the persona pull (59 sampled, ~200 at scale), only rows with `owner_cleared = TRUE` ever enter a campaign. Sender: Nathan (pending mailbox warmup + owner sign-off). Same five-touch multi-channel spine as Stars Wave 1: Email 1 (D1) → LinkedIn connect (D2) → Voicemail + LinkedIn msg (D4) → Email 2 (D6) → Breakup (D9).

## Lane 1 — `bo_claims` (payer/insurance claims, appeals, UM)

**The one idea:** the backlog that regrows every Monday is not a staffing problem, it is a timing problem: the capacity to clear it exists inside the week's idle windows, but nothing acts on them while they're open.

- T1 angle options: (A) the Monday-regrow pattern; (B) SLA/TAT clock vs yesterday's report; (C) surge-season staffing by guesswork.
- T4 (window email): overtime spend as the receipt for acting late.
- Merge fields: `{{first_name}}`, `{{function}}`, `{{parent_account}}`, optional `{{public_signal}}` (fired bo_* signal, cited from public source).

## Lane 2 — `bo_shared` (payment ops, disputes, doc processing, shared services, enrollment, RCM)

**The one idea:** cost-per-transaction is decided in the minutes between reports; real-time visibility without real-time action just documents the loss faster.

- T1 angle options: (A) cost-per-transaction scrutiny; (B) multi-function queues nobody can rebalance mid-day; (C) utilization they can't prove to finance.
- T4: the found-capacity frame (idle minutes already on payroll).

## Lane 3 — `coo_finance` (economic buyer; NEVER the first touch)

Enters at Day 6+ only after a Lane 1/2 thread exists at the account, or on a fired Tier-1 signal (`bo_cost_mandate`, `sla_penalty_backlog`). **The one idea:** the back office has no equivalent of the contact center's real-time discipline, and the gap is a line their own front office already crossed.

- Single two-touch arc: the mandate email (their stated cost language quoted back, if public) → breakup.

## Gates (all inherited, none new)

Verified-claims (mechanism-only for BOO) · current-customer exclusion INVERTED but `owner_cleared` + `fo_risk_flag` enforced · human approval before any send · deliverability green · Reply Engine v1 SOP on every reply (claim the row, log the outcome).
