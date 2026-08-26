# Stars Wave 1 — Reset Unlaunched Campaigns to the VoiceFix (approved two-pass) Output
Date: 2026-07-20 · Table: Contacts (Buying Committee) `t_0thtm73HHxyiupTuepK` · Workbook: Star Ratings `wb_0thtlocqNeb46szQtAf` · workspace 1180800

## What this fixes (read first)
The approved workflow is the two-pass engine: `MessageGen Email 1 (v2.2)` (`f_0ti6c7jcHFffy94Qmqv`)
-> `Voice Fix` (`f_0tigozgsBq5RYTww6et`, outputs `revised_subject` / `revised_body`) -> gated by
`Draft Audit` + `Voice Audit` -> `send_ready` (`f_0thtsyrabg7qGSqe5gf`).

Verified live on 2026-07-20: the gate reads Voice Fix, but the sync columns ship
`Msg1Body` (`f_0tiaar2jh3zvx8iwTGw` = `{{MessageGen Email 1 (v2.2)}}?.["msg1_body"]`) and
`Msg1Subject` (`f_0tiaaxrMWFddyKBDstY` = MessageGen msg1_subject) — the PRE-Voice-Fix draft.
So the campaigns receive Pass 1 even when the gate passed Pass 2. The fix is to add the two
missing VoiceFix extractor columns and repoint the unlaunched sync columns' body/subject values
to them.

Do NOT edit `Msg1Body`/`Msg1Subject` themselves — `Voice Fix` READS them as its input, so pointing
them at Voice Fix would create a circular reference. Add NEW columns instead.

Campaigns in scope (not launched): Persona 2 sync `f_0ti5hg5NMbD7o5ZB8gh` -> "Stars QBP Wave 1 -
Persona 2 (Finance)"; Longer-Horizon sync `f_0ti7czq3gB56KQRZWKE` -> "Stars QBP Wave 1B -
Longer-Horizon". Leave Persona 1 sync `f_0ti5fzpC6KQ6NjVadCZ` alone (already sent; see Step 6 note).

ORDER MATTERS. Do Step 1 before Step 2 (the sync edit references columns that must exist first).
Do Step 3 (regenerate) before Step 4 (re-sync), or you push stale text.

---

## Step 1 — Create the two VoiceFix extractor columns (additive, safe)
On table `t_0thtm73HHxyiupTuepK`, add two new columns of type **Formula / Text** (the same column
type as the existing `Msg1Body`). Use the "+ Add column" control at the right edge of the grid,
choose the plain formula/text option (confirm the exact label in your UI).

1. Name exactly: `VoiceFix Body`
   Formula: `{{Voice Fix}}?.["revised_body"]`
2. Name exactly: `VoiceFix Subject`
   Formula: `{{Voice Fix}}?.["revised_subject"]`

After each saves, spot-check one Wave-2 row that already has a Voice Fix value: the new columns
should show the polished text, not empty. If empty, the row hasn't had Voice Fix run yet (fine —
Step 3 handles that for the Wave 1 rows).

## Step 2 — Repoint the two unlaunched sync columns to VoiceFix (value swap, keep the keys)
For EACH of the two sync columns below: open the column header -> Edit / Configure -> the
**Row Data** JSON. Change ONLY the two VALUES; keep the KEY names `"Msg1Body"` and `"Msg1Subject"`
exactly (the destination campaign table expects those keys).

- `"Msg1Body"`: change `{{f_0tiaar2jh3zvx8iwTGw}}` to a reference to your new **VoiceFix Body** column.
- `"Msg1Subject"`: change `{{f_0tiaaxrMWFddyKBDstY}}` to a reference to your new **VoiceFix Subject** column.

Insert the new column reference with Clay's variable picker (type `/` or click the column-insert
control and pick "VoiceFix Body" / "VoiceFix Subject") so the correct token drops in — don't hand-type
an ID. Change nothing else in the Row Data. Save.

Columns to edit:
1. `Sync leads to campaign (3)` (`f_0ti5hg5NMbD7o5ZB8gh`) -> Persona 2 (Finance)
2. `Sync leads to campaign` (`f_0ti7czq3gB56KQRZWKE`) -> Wave 1B Longer-Horizon
   NOTE: this column currently pushes the MAIN v2.2 body, not the "MessageGen Email 1 - Longer
   Horizon" (`f_0ti7aa1XuAP4jZaQkqi`) variant. If Longer-Horizon is supposed to send the LH variant,
   that's a separate decision — see "Calls that are yours" at the bottom. For now this swap just
   makes it ship the Voice-Fixed version of whatever body it already carries.

## Step 3 — Regenerate the pipeline on the unlaunched rows (so send_ready = READY)
`send_ready` now requires `critic_email_valid==PASS` AND `msg1_critic Status==PASS` AND
`voice_status==PASS` (human_approved was already dropped). So the row won't be READY until Voice Fix
+ both audits have run. For the Persona 2 and Longer-Horizon rows:

1. Filter the grid to the rows for that campaign (Persona 2: `Persona Key` = `coo_finance`;
   Longer-Horizon: `parent_key` in caloptima, lacare, iehp, myzinghealth, chpw, atriohp, baystatehealth).
2. If `MessageGen Email 1 (v2.2)` is stale/empty on those rows, run it first on the selected rows.
3. Run `Voice Fix` on the selected rows.
4. Run `Draft Audit` and `Voice Audit` on the selected rows.
5. Confirm `send_ready` shows `READY` for the rows you intend to send. Any `HOLD` = a failed audit;
   read `msg1_critic Reason` / `Voice Audit` reason and fix or drop that row (do not force it).

## Step 4 — Clear stale rows in the destination table, then re-sync
1. Open the destination campaign table ("Stars QBP Wave 1 - Persona 2 (Finance)" /
   "Stars QBP Wave 1B - Longer-Horizon"). If it already holds rows from an earlier sync (they'll
   carry the old MessageGen text), delete those rows first so you don't duplicate or leave stale copy.
2. Back on `t_0thtm73HHxyiupTuepK`, run the sync column on the qualified selected rows:
   - Persona 2: `Sync leads to campaign (3)` is a manual button (no run condition) — select only the
     READY Persona 2 rows in the view, then run the column, so nothing off-persona or HOLD gets pushed.
   - Longer-Horizon: `Sync leads to campaign` runs on its parent_key condition; run/refresh it on the
     READY rows.

## Step 5 — Confirm the campaign now carries VoiceFix text, keep it Draft
In each destination table, open a couple of freshly synced rows and confirm `Msg1Body` / `Msg1Subject`
now read the polished Voice-Fixed copy (compare against the row's `VoiceFix Body` on the source table —
they should match). The campaign stays in Draft. NOTHING sends here.

## Step 6 — Final gate-semantics check on REAL rows before any launch (non-negotiable)
Before you ever launch, on real rows (never synthetic): confirm `customer_exclude != "true"` is
actually excluding current customers from these campaigns, and that only the intended
persona/wave/batch rows are present. `customer_exclude` is stored as TEXT — a synthetic pass can hide
a real-row gate miss. This is the one validation that must run on live rows.

NOTE on Persona 1 (`f_0ti5fzpC6KQ6NjVadCZ`, already launched, 23 sent): the 23 already went out on
Pass 1 text; nothing changes them. If you want future Persona 1 re-syncs to also ship VoiceFix, apply
the same Step 2 value swap to that column too — but do not re-run its sync button unless you intend to
push more rows into that live campaign.

---

## Calls that are yours (I flagged, did not change)
1. **Longer-Horizon variant.** The Wave 1B sync ships the main v2.2 body Voice-Fixed, not the dedicated
   `MessageGen Email 1 - Longer Horizon` variant (which has its own `LH Draft Audit`). Decide whether
   Wave 1B should send the LH variant; if so, that's a different rewire (point Voice Fix / the extractors
   at the LH pipeline), not this sheet.
2. **Global vs unlaunched-only.** This sheet repoints only the two unlaunched syncs. Repointing Persona 1
   and Wave 2 P1 too makes the whole table ship VoiceFix consistently going forward. Recommended, but it
   touches a live-launched campaign's future syncs, so it's your call.
