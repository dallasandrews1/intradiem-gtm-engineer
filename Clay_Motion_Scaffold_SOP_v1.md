# Clay Motion Scaffold SOP — "Stamp a Motion, Don't Rebuild It" v1
**Owner: Dallas Andrews. Companion to `New_Motion_Build_Runbook.md` and `Clay_Golden_Standard.md`. Open this the moment you've decided a new motion.**

## Why this exists
The hours-per-motion cost is in re-creating the same L0–L4 structure by hand in the Clay UI (or worse, an agent clicking through Chrome). Clay has **no create-table API** — not via MCP, CLI, or the agent-plugin (verified against developers.clay.com, Jul 2026). So an agent physically cannot build the tables reliably; browser automation is the only path and it's slow and limit-bound. The fix is not a better agent. It's to stop building structure from scratch: **duplicate a golden scaffold, then re-point the five things that actually change per motion.**

This splits the build into the two layers Clay treats differently:
- **Structure (tables/columns/enrichments)** → `Duplicate table` from a golden scaffold. Manual, seconds, deterministic. This SOP.
- **Logic (the per-motion send-readiness brain)** → agent-built Clay Workflow via local Claude Code. Separate deliverable: `Motion_Workflow_Build_Prompt_TEMPLATE_v1.md`.

## What Clay's `Duplicate table` actually does (verified, and its limits)
- **Where:** click the table title (top-left) → **Duplicate table**.
- **Carries:** the table's column/source structure. It copies the *sources*, not the *data rows* — you get an empty, fully-columned scaffold. That is what we want.
- **Does NOT carry:** the data rows (correct — a scaffold should be empty).
- **UNVERIFIED in Clay's docs:** whether every enrichment column, formula, run-condition, and cross-table Lookup survives a duplicate byte-for-byte. Clay's doc only says "copies the sources." So the **first** time you duplicate the golden scaffold, you verify column-by-column in the UI (checklist below). After that first proof it's a known-good, repeatable stamp.
- **Public "Share as Template" is NOT this.** That path strips down to structure + one sample row and is explicitly vague on enrichment/formula carry. Use in-workspace `Duplicate table`, never the public template link, for your own motions.

## Scope: what gets stamped vs what stays shared
Per the structure law (Golden Standard §2), a new motion builds **L0–L4** and reuses **L5–L8 + reference tables** by tagging rows `source_motion`. So:

**The golden scaffold = L0–L4 only:**
- L1 Accounts/Universe table (identity → fit → grade columns, empty)
- L2 Signals columns (Tier 1/2 point-scorers, wired to write back to Accounts)
- L3 Contacts segment (persona_match, email waterfall, attribution tags)
- L4 MessageGen + companion critic columns

**NOT in the scaffold (already exist once, joined by tag/Lookup):**
- L5 Send Queue, L6 Outreach Sync, L7 Reply/Attribution, L8 AE Worklist
- Reference tables: Verified Metrics, Product-Angle Map, ICP Rubric, Variant Library

> Honest nuance flag: Golden Standard §2 says L5–L8 are *shared tables reused by tag*; §1 says "one motion = one workbook" and calls the critic/gate/campaign wiring a *copy-paste pattern*. Those two readings differ on whether L5–L8 physically live once or are re-stamped per workbook. This SOP does **not** resolve that for you — it stamps L0–L4 (unambiguously motion-specific and the real time sink) and leaves L5–L8 to whatever your live workspace already does. Confirm which reading your live workspace follows before extending the scaffold downstream.

## One-time setup: designate the golden, don't build a new one
You already have motions built to house standard. Designate, don't rebuild (same principle as designating the persona key in the runbook).

1. Pick the cleanest house-standard motion as the source. **Back Office Motion** is the ratified precedent; the hardened **Cost-Mandate Motion** L0–L4 is the other candidate.
2. Create a workbook `__GOLDEN Motion Scaffold`.
3. For each L0–L4 table in the source motion: `Duplicate table` → move the copy into `__GOLDEN Motion Scaffold` (table Actions → **Move table** / "Send Table Data" — verify the current UI label first, per Golden Standard §15; it has moved before).
4. In the golden copy, strip anything motion-specific to a neutral default: clear the universe rows, blank the MessageGen prompt node to a `<<MOTION PROMPT GOES HERE>>` placeholder, set `source_motion` to `<<motion>>`, leave every column/enrichment/run-condition intact.
5. Run the **First-Duplicate Verification** below once against this golden. Fix any column that didn't carry. From then on the golden is trusted.

## The per-motion loop (this replaces "build L0–L4 from scratch")
After you decide the motion and answer the runbook's two decisions (universe source, persona key):

1. `Duplicate table` each L0–L4 table from `__GOLDEN Motion Scaffold`.
2. Move the copies into a new `<Motion> Motion` workbook (create it first — one motion = one workbook).
3. Re-point the **five things that change per motion** (nothing else):
   - **`source_motion` tag** → the motion's key (e.g. `wfm_adjacency`). Set at creation, read-only after (Golden Standard §5).
   - **Universe source** → the motion's L0 (list, signal-first search, or inverted customer file per the runbook).
   - **Persona routing** → the canonical rubric key(s) for this motion (`coo_finance`, `cc_ops`, `wfm`, `cx`, `bo_claims`, `bo_shared`).
   - **MessageGen prompt (L4 node)** → paste the motion's prompt built to the v2.2.3 contract; brand-light, block-on-empty numbers.
   - **The number rule** → the H1 source-window logic for what number (if any) this motion is allowed to cite.
4. Re-point Lookups to the shared reference + L5–L8 tables (duplicated columns may still reference the golden's internal table IDs — this is the #1 thing that silently breaks).
5. Hand off to the workflow build (deliverable B) for the send-readiness logic, then run the runbook's gates: prove on a 10-row slice, credit estimate + ledger row, everything Draft + critic PASS + your approval, sender webhook OFF, nothing sends.

## First-Duplicate Verification (run once per golden change; abbreviated per stamp)
Keyed to your live gotchas (Golden Standard §15). After a duplicate, before loading any universe:
- [ ] Every enrichment column present and its config intact (not reverted to a blank/agent template).
- [ ] **No Claygent binding** — no "Agent template being used" banner on any AI column. If present, click the x to detach.
- [ ] **No stray campaign column** — duplication or a stray click can leave a sync column with Auto-run ON and no run-condition. Delete it.
- [ ] Every **run-condition** carried (the eligibility/`customer_flag`/only-run-if-empty gates). A dropped run-condition = credits firing on excluded rows.
- [ ] **Optional inputs' "Required to run" = OFF** (esp. `li_recent_post_hook`) — else rows missing that input hard-fail and wipe drafts.
- [ ] **Lookups resolve** to the shared reference and L5–L8 tables, not to the golden's copies. Spot-check one value returns.
- [ ] **Sender webhook / sync = OFF.** Dry-run is the default state of the world.
- [ ] `source_motion` set and correct on the Contacts table.

## The law this preserves
Nothing about this SOP sends, launches, or flips a gate. Duplicating a scaffold is structure only. Loading the universe, enriching, drafting, and launching remain the runbook's gated, waved, human-approved steps. Source once, process in waves. Measurement before volume.
