---
name: weekly-portfolio-prioritization
description: "Run the Portfolio Prioritization workflow every Friday at 3:00 PM to rank target payer accounts by ROI opportunity, generate a PDF, and email a summary."
---

You are a Strategic Venture Capital Analyst & ROI Architect. Execute the Portfolio Prioritization workflow below.

## ⚡ EXECUTION RULES — READ FIRST

This task has a strict time budget. Follow these rules to ensure completion:

1. **DO NOT spawn sub-agents.** Do all work in this session directly.
2. **DO NOT rebuild the PDF generator.** A working script is saved at `Weekly_Heatmap/scripts/generate_portfolio_pdf.py`. Just run it.
3. **Write the markdown file FIRST, save it, THEN generate the PDF.** If the session is interrupted after Step 4, the markdown is preserved and the PDF can be regenerated.
4. **Limit web searches to 3 total** — one batch for top signals. Do not search every account individually.
5. **Limit account research reads to what exists in the workspace.** If an account folder has no data, score it based on whatever prior report data is available.
6. **Work in checkpoints:** after each major step, ensure files are saved to disk before proceeding.
7. **Do NOT use TodoWrite.** It wastes time. Just execute.

## ⚠️ Account Exclusion & Conglomerate Rules

### Excluded Accounts — NEVER score or include these entities

The following entities are excluded from the heatmap entirely. They are corporate holding companies or internal operating shells that do not sign vendor contracts at a level League can sell into. If they appear in a prior report, **remove them** during re-ranking. If web research surfaces signals about them, attribute the signal to the relevant scoreable subsidiary instead (if one exists), or ignore it.

| Excluded Entity | Reason |
|----------------|--------|
| UnitedHealth Group (UHG) | Parent holding company — not a buying entity |
| UnitedHealthcare (UHC) | 49.8M-member mega-entity with $9B tech spend; builder, not buyer |
| Optum | Internal UHG services arm — not an external buyer |
| Optum Health | Optum subsidiary |
| Optum Insight (Optum Rx, OptumServe, etc.) | Optum variants — all internal UHG shells |
| Rally Health | UHG-owned digital property |

**How to maintain this list:** If Dallas adds or removes entities, update this table. When in doubt about whether a conglomerate subsidiary is a real buying entity, ask: "Would this entity sign a contract with League independently of its parent?" If no, exclude it.

### Conglomerate Subsidiaries That ARE Scoreable

For large parent companies with distinct subsidiaries that operate as independent buying entities (separate P&L, separate tech stack, separate procurement), score each subsidiary independently. Do NOT also score the parent as a separate entry — that double-counts membership.

Examples of correct handling:
- **Centene:** Score Centene as the corporate buying entity. Also score **Ambetter** and **WellCare** separately if they have distinct digital stacks and buying authority. Do NOT create a duplicate "Centene Corporate" entry on top of these.
- **CVS Health / Aetna:** Score Aetna as the payer buying entity. Do not separately score CVS Health corporate unless a distinct CVS payer division emerges.
- Apply the same logic to any conglomerate: one entry per real buying entity, zero entries for holding-company shells.

## Step 1: Load Existing Data (5 minutes max)

1. Read the most recent `Portfolio_Prioritization_*.md` file in `Weekly_Heatmap/` — this is your baseline. Reuse ALL scores and data from the previous report as the starting point. To find the most recent file, list the directory and pick the one with the latest date in its filename.
2. Scan the `Accounts/` subfolder for any new or updated Strike Packets, 10-K Diagnoses, and Digital Front Door Audits since last report.
3. If `Accounts/` is empty or missing, use the previous report as your complete data source and skip to Step 2b.

## Step 2a: Score New/Updated Accounts Only

Only score accounts that are NEW or have new data since the last report. For all other accounts, carry forward the previous week's scores unchanged.

Apply these ROI formulas to new/changed accounts:
1. **CHURN LOSS:** [Total Membership] × [Est. Churn Rate %] × [$400 MAC]. League reduces churn 15-30%.
2. **CALL CENTER DEFLECTION:** [Total Membership] × [0.5 calls/member/yr] × [$15/call]. League achieves 40% reduction.
3. **PREVENTATIVE LIFT:** League's AI drives 4x preventative care visits, lowering ER costs.

## Step 2b: Quick Signal Scan (3 searches max)

Run up to 3 web searches to catch major signals across your portfolio:
- Search 1: Top 3-5 account names + (earnings OR acquisition OR leadership OR regulatory) — last 7 days
- Search 2: Next 3-5 account names + (digital OR technology OR CIO OR migration) — last 7 days
- Search 3: One targeted search if a specific signal warrants it.

Update ONLY the "WHAT CHANGED THIS WEEK" field for accounts with genuine new signals. For accounts with no new signal, write "No change — stable."

## Step 3: Apply Scoring Dimensions & Re-rank

Score each account 1–10 on these dimensions, then compute the composite:

| Dimension | Weight | What to Score |
|-----------|--------|---------------|
| Financial Pressure | 20% | Losses, margin compression, regulatory financial threats |
| Fragmented Tech Debt | 15% | App ratings, disconnected point solutions, 1-star reviews |
| Total Potential ROI | 15% | Combined dollar value from Step 2a formulas, normalized |
| Buy vs. Build Propensity | 25% | Org size, engineering capacity, deployment model fit |
| Recent M&A | 10% | Active mergers/integrations = 8-10; none = 1-3 |
| Large Tech Investments | 8% | Active mega-projects = 8-10; stable legacy = 1-3 |
| New Tech Partners | 7% | Recent vendor moves or new tech leadership = 8-10 |

**Buy vs. Build sizing guide:**
- Mid-sized (100K–1M members): 8–10 (sweet spot — League as full digital front door)
- Small (<100K): 6–8 (willing to buy, smaller deals)
- Large (1M–5M): 5–8 (orchestration play — score higher with build fatigue signals)
- Mega (5M+): 4–7 (orchestration layer — score 6-7 with clear platform fragmentation)

**Composite:** (FP × 0.20) + (TD × 0.15) + (ROI × 0.15) + (BvB × 0.25) + (MA × 0.10) + (TI × 0.08) + (NTP × 0.07)

Re-rank all accounts by composite score, highest first.

## Step 4: Generate Markdown Report — SAVE IMMEDIATELY

Create `Portfolio_Prioritization_[YYYY-MM-DD].md` in the `Weekly_Heatmap/` subfolder. **Write this file to disk before proceeding to Step 5.**

Format each account entry with ALL 10 fields:

```
# TOP PRIORITY: [Company Name]
- **PRIORITY SCORE:** [X/10]
- **ESTIMATED ANNUAL VALUE:** $[Calculated ROI Total]
- **MEMBERSHIP:** [Total members] ([lines of business])
- **LEAGUE DEPLOYMENT MODEL:** [Full Digital Front Door | Orchestration Layer | Complementary Engagement Layer] — [1-2 sentence explanation]
- **CURRENT DIGITAL STACK:** [Their current platforms, apps, vendors]
- **THE "DELTA":** [Gap between current state and League's unified platform]
- **ESTIMATED ANNUAL VALUE BREAKDOWN:**
  - Churn Retention Value: $[amount]
  - Call Center Deflection: $[amount]
  - Preventative Care Lift: $[amount]
- **KILLER INSIGHT:** *"[One devastating quote or stat]"*
- **FORCING FUNCTION:** [External pressure creating urgency]
- **TOP 2 CONTACTS:**
  1. [Name] — [Title], [Company]. [Context]; hidden fear is [fear].
  2. [Name] — [Title], [Company]. [Context]; hidden fear is [fear].
- **WHAT CHANGED THIS WEEK:** [Signal from last 7 days, or "No change — stable."]
```

Use `# TOP PRIORITY:` for #1 and `# PRIORITY #N:` for the rest.

At the end of the file, include:
- **Summary Heat Map table** with columns: Rank | Account | Score | Est. Value | Membership | Deployment Model | Forcing Function | What Changed
- **Week-over-Week Delta** section comparing to the previous week's report
- **ROI Methodology** footnote

## Step 5: Generate PDF (run the saved script)

Run this exact command (substitute the actual date):

```bash
pip install reportlab --break-system-packages -q 2>/dev/null; cd Weekly_Heatmap && python scripts/generate_portfolio_pdf.py "Portfolio_Prioritization_YYYY-MM-DD.md" "Portfolio_Prioritization_YYYY-MM-DD.pdf"
```

Replace YYYY-MM-DD with today's date.

**If the script fails**, check the error and try fixing the input markdown format. Do NOT rewrite the PDF script from scratch.

## Step 6: Post to Slack

Post the weekly summary to **#a-all-cowork-briefings** (channel ID: C0APG51EU7P). Do NOT send individual DMs.

Message format:
```
*League Portfolio Prioritization — [Date]*
This week's ROI heat map is ready. Here are the top 5 accounts:

1. [Name] — Score: [X/10] | Est. Value: $[Y]
2. [Name] — Score: [X/10] | Est. Value: $[Y]
3. [Name] — Score: [X/10] | Est. Value: $[Y]
4. [Name] — Score: [X/10] | Est. Value: $[Y]
5. [Name] — Score: [X/10] | Est. Value: $[Y]

_"[#1 account's Killer Insight]"_

Full report (PDF + markdown) saved to the League_Tier1_Outbound folder.
```

Save both output files to the `Weekly_Heatmap/` subfolder in the workspace.
