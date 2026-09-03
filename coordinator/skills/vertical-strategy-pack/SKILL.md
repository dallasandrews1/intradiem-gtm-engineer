---
name: vertical-strategy-pack
description: Build a complete meeting-booking strategy pack for a vertical or account list — persona-angled email + LinkedIn messaging doc (.md), account strategy tracker (.xlsx) and interactive HTML strategy map. Use this whenever Jack asks to build a strategy for a new vertical or territory ("build me the utilities pack", "do for telcos what we did for insurance", "account strategy for [sector]"), asks to add named-contact messaging to an existing strategy pack ("add messaging for [company], contacts are..."), or asks for outreach sequences, cold email + LinkedIn messaging, account tiering, or a strategy map/tracker for Intradiem prospecting. Also use when updating an existing pack with new intel (bounces, prior no's, new contacts, M&A news).
---

# Vertical Strategy Pack

Reproduce the UKI-insurance strategy workflow for any vertical: research accounts → tier them by timing signals → produce three deliverables that stay consistent with each other:

1. `<Vertical>_Email_LinkedIn_Messaging.md` — persona-angled sequences per named contact
2. `<Vertical>_Meeting_Strategy.xlsx` — tracker + playbook + parked list
3. `<Vertical>_Strategy_Map.html` — interactive tiered card map

The seller is Jack (SDR for Intradiem, real-time intraday automation for contact centres, sold UK&I). Product facts are fixed — read them in `references/messaging-guide.md` §1 before writing a single message, and never invent numbers beyond them.

## Two modes — detect which one you're in

**Mode A — full pack for a new vertical** ("build me the pack for UK utilities"): run all phases below.

**Mode B — update an existing pack** ("add messaging for Domestic & General, contacts are...", "Alan said no", "emails bounced"): ask for / locate the existing files, edit them in place, keep every existing convention (numbering, header style, coordination notes). For new named contacts: assign each a role tag (primary / evaluator / sponsor / new-exec / exec-air-cover / quarantine), write full sequences per the messaging guide, replace any placeholder sequences the named people supersede, and rewrite the routing + coordination note. For intel updates (prior no, gateway block, leadership change): encode the intel as RULES in the account section header so it can't be forgotten — see messaging-guide.md §5.

## Phase 0 — Scope (Mode A)

Ask Jack only what can't be inferred: which vertical/region, any accounts already in pipeline to exclude, any known warm threads or prior no's, and any accounts he already knows he wants in. Default assumptions: UK&I, 200+ agent floor, Intradiem front-office product.

## Phase 1 — Research (before touching any deliverable)

For each candidate account, hunt for **dated timing signals** — these decide tiers and write the hooks:

- M&A: acquisitions closing, integrations starting, brand consolidations
- Sites: new contact centre / hub openings or closures, consolidation into hubs
- Platforms: CCaaS/WFM migrations (post-migration = classic entry window), competitor tools whose contracts may lapse
- Leadership: new ops/customer/transformation execs ≤6 months in role (agenda-setting window), departures (decision vacuums, incoming reviewers)
- Results & regulation: cost-control statements, growth that becomes contact volume, regulator pressure specific to the vertical
- Scale: estimate agent counts (use the agent-count-estimator skill if available); park anything under 200 agents

Web-search each account. Note every signal WITH ITS DATE. A signal without a date can't support a "why now" email.

## Phase 2 — Tier and structure

Build `strategy.json` per `references/strategy-json-spec.md` (read it now). Tier 1 = live timing event, strike this month. Tier 2 = fit + signals, no deadline. Parked = pipeline overlap, too small, build-in-house. Write the REFRAME first — the one belief to flip (e.g. "merger ≠ budget freeze; integration is when tooling decisions get made") — it sets the tone for everything.

## Phase 3 — Build the xlsx + html (scripted, don't hand-build)

```bash
pip install openpyxl --break-system-packages   # once
python3 <this-skill>/scripts/build_pack.py strategy.json <output_dir>
```

Then open the HTML and spot-check: every card needs a non-empty signal, hook and play. Fix the JSON and re-run rather than editing outputs.

## Phase 4 — Write the messaging doc

Read `references/messaging-guide.md` IN FULL first — it contains the voice rules, the five-asset sequence template, the persona→angle library, situational plays (new exec, win-back, prior no, prickly gatekeeper, exec air cover, do-not-sequence, blocked gateway), intel hygiene and gold examples. The doc structure is in strategy-json-spec.md ("Messaging .md structure").

Non-negotiables, because these are what made the originals book meetings:

- Every email opens with the prospect's world, cites a dated signal, stays under ~110 words, and asks for a **benchmark conversation, never a demo**.
- Every persona gets a different angle from the library; every message in an account uses **identical numbers** (the team compares notes).
- Every account ends with a coordination note (who first, who says what about whom, who pulls whom in).
- Private intel never appears in writing; LinkedIn connect notes are genuinely ≤300 characters — count them.

## Phase 5 — QC before delivering

Walk this checklist; fix failures rather than shipping them:

1. Word-count 3 random emails (≤ ~110 words) and character-count 3 connect notes (≤300).
2. Grep the messaging doc for numbers: only the approved stats from messaging-guide.md §1 appear, identically everywhere.
3. Every Tier 1/2 account in strategy.json has a section in the messaging doc, and vice versa.
4. Every account section has: signals with dates, routing, coordination note.
5. No email proposes a specific meeting time, mentions a demo, or opens with "I hope".
6. xlsx opens (3 sheets), HTML renders (open it), cards expand.

Deliver all three files together and offer next steps: find missing contact names (Lusha), set up the sequences (Lemlist), or pre-meeting briefs when meetings land.
