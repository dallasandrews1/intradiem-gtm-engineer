---
name: hub-verify-drift-discipline
description: Start Here hub is now the living operational surface with interactive checklists + auto War Room tile; hub_verify.py lints its claims against source to catch drift
metadata: 
  node_type: memory
  type: project
  originSessionId: 255fccd7-9187-4515-acdd-bd8ac3b6b4ad
---

Jul 7 2026 build on `Start_Here_Index.html` (the local file:// hub Dallas keeps open in Chrome; not deployed). Triggered by finding a "dead reference" hole: the page named `Day_One_Checklist` as if live but it had no home on the page.

**What was added to the hub:**
- Interactive **Day One** checklist section (7-step signal-engine turn-on order + guardrail + 3 questions), sourced from `Day_One_Checklist.md`. Checkboxes persist via `localStorage` (works on file:// in Chrome).
- Interactive **Weeks 1-2** section (stakeholder meetings + Naveen 1:1 agenda + end-of-two-weeks checkpoint), sourced from `First_Two_Weeks_Meeting_Plan.md` + `Naveen_FirstOneOnOne_Agenda.md`, one shared 22-item progress bar. **Pre-hire correction (Jul 7):** the source doc carried the interview-era cast (CRO "John Norton", "Kevin Wilson" data/eng, Cheryl Eckel as PMM). Per `Arsenal_and_Rollout_Playbook.md` (the authoritative reconciliation), that org chart is NOT confirmed. Hub now corrected: CRO meeting reframed to "the revenue leader — confirm with Naveen (he's the confirmed exec sponsor, maybe no separate CRO)"; Kevin Wilson → "data/eng owner name TBC"; the marketing-governance meeting routed to **Sierra Jones** (confirmed Marketing) not Cheryl; a confirmed-vs-interview-era cast box added. Confirmed cast: Naveen (mgr/sponsor), Nate Belfield, Genna, Sierra Jones, Tom Russell, Scott Kemme, Chris Busbee. Also softened the Day One Q about the "2025 data architecture" to "the platform modernization Busbee/Naveen referenced" (that specificity was interview inference). See [[naveen-email-corpus]].
- **War Room tile** at top of Today, between `<!--WARROOM:START-->`/`<!--WARROOM:END-->` markers, updated in place by `update_war_room_tile.py` (marker-bounded replace; never touches the rest of the page).
- Footer note changed: the HTML is now the **living operational surface** (interactive content lives here, not in `_START_HERE_Index.md`).

**The bug class + the fix (reusable):** the hub makes claims (file refs, hardcoded counts, "twelve skills") that nothing verified against reality. Found one real drift: page said TAM tests "21/21" but the suite passes **25/25** (fixed in html + `_START_HERE_Index.md`). Stars numbers (307 / 98 A+B / 34 A / 32 parents / $2,511M addr_2028) all verified correct — but only after reparsing the tiered CSV with a real csv reader (naive awk split gives $1,742M because `marketing_name`/`primary_sources` contain quoted commas; always use csv module on `StarRatings_Targets_2026_Tiered.csv`).

**`hub_verify.py`** (project root) re-derives every hub claim from source and exits 1 on drift. Wired into `intradiem-signal-engine/run_daily.sh` (non-fatal warn). Run it after ANY edit to the hub's numbers, and before showing the page to Naveen. It's the standing defense against this whole bug class.

**INCIDENT + HARDENING Jul 8 2026:** `update_war_room_tile.py` truncated the hub to 0 bytes when fed malformed JSON (a dict instead of a list of `{priority,text}` items): the old code did `open(HUB,"w").write(pre + build_tile(...))`, so Python truncated the file before build_tile raised. Recovered by replaying the full Write + 49 successful Edits from session transcript JSONLs (`~/Library/Application Support/Claude/local-agent-mode-sessions/**/*.jsonl`; skip tool_uses whose tool_result has is_error). Script now builds the doc first and writes atomically via `.tmp` + `os.replace`; verified a bad-input run leaves the hub intact. Input contract: a LIST of `{"priority","text"}` objects. Session-transcript replay is a general recovery path for any Claude-written file with no other backup. Jul 8 cast confirmation: John Norton IS the CRO (Naveen named him on the strategy call); hub's revenue-leader line updated.

**Scheduled task** `intradiem-morning-war-room` (weekdays 7am) runs the war-room sweep, writes the dated log, calls `update_war_room_tile.py`, then runs `hub_verify.py`. Verified/sourced signals only, never fabricate. See [[three-surface-sync]], [[mission-control-dashboard]], [[no-finished-product-framing]].
