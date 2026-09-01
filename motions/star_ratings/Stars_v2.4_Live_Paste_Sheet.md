# Stars v2.4.0 — Live Clay Paste Sheet (Dallas's hands)

**Table:** Contacts (Buying Committee) · `t_0thtm73HHxyiupTuepK`
**Source of the copy to paste:** `Stars_MessageGen_v2.4_NateFeedback_Rewrite.md` (same folder).
**Verify labels before clicking.** Clay's column-edit UI: click the column header, the field config panel opens, the AI/action prompt sits in the prompt box. If a label below reads differently in your live UI, trust the live label and tell me so I fix this sheet.

**STATUS after the Naveen 1:1 (Jul 22): campaigns PAUSED; HOLD the live paste until tonight's assembly.** Dallas paused the Stars campaigns Jul 22 so we can regenerate against the new prompt before resuming. Three things fold in first so you paste ONCE, not twice: (1) Naveen's confirm on naming Queue Optimizer pre-GA (or the platform-level fallback), (2) your 5-6 layman points + final product one-liner wording, (3) Nate's ~20 golden emails appended to the §2 EXAMPLES anchor. Once those land, this sheet executes as written.

**Scope on resume (revised Jul 22): regenerate ALL 46 leads, not a 7-company wave.** Because the campaign is paused there is no in-flight cohort to protect. Regenerate every lead's MessageGen: Email 1 for anyone not yet sent, and Email 2-5 for everyone. The 23 who already received Email 1 keep that send (can't unsend), but their NEXT scheduled touch reads the freshly recomputed column, so they pick up v2.4 automatically. Then resume. (Naveen's separate "next 7 companies" is an additive new wave on top of this, same v2.4 copy.) Dallas to loop Nate in on the pause per Naveen.

**Ordering traps (read first):**
- Campaign is PAUSED, so a full recompute is now the goal, not a hazard. These drafts are all AI-generated (no manual overrides to protect), so recomputing overwrites cleanly, which is exactly what we want. Keep the campaign paused until every column has finished recomputing, THEN resume.
- **Email 2-5 must be regenerated too, not just Email 1.** The 23 already-sent leads' next touch is Email 2, so if only Email 1 is updated they'd resume on stale E2 copy. Before resuming, confirm the live E2-5 generation surface (the Stars 5-touch workflow `wf_0tiegzuo3PzJ4UtUGFA` nodes, or E2-5 table columns) is on v2.4 too. The stage-sheet specs are already patched; the live nodes are the piece to update. (I'll locate and spec these as part of tonight's assembly.)
- Paste MessageGen FIRST, then the two critics. If you flip a critic before the copy is updated, good drafts can trip a rule the new copy hasn't caught up to yet.
- Don't edit a column while its run is in progress; let each recompute finish before touching the next.

---

## STEP 1 (required) — MessageGen Email 1 (v2.2) · `f_0ti6c7jcHFffy94Qmqv`

1. Open the table, click the **MessageGen Email 1 (v2.2)** column header, open its config.
2. In the system-prompt box, select all and replace with the full **§2 prompt** from `Stars_MessageGen_v2.4_NateFeedback_Rewrite.md`. (Paste it whole; it's the complete v2.4.0 prompt, not a patch.)
3. Leave the token bindings / inputs as they are. `account_row` still carries contract_id as an available field; the new prompt forbids printing it, which is correct. No input change needed.
4. Save. Do NOT run yet if the in-flight cohort shares this column. Run only on the un-sent pool (filter to un-sent, then run the column on that view).
5. Update the SENTENCE FLOW gold-standard exemplar inside the prompt to the **§3** Nate-voice version (swaps again tonight when the real sends land).

---

## STEP 2 (backstop) — Voice Audit · `f_0tiaks8wH5dHsbkvjcz`

Add the **§7** block to the FAIL conditions and the PASS requirement in the Voice Audit prompt (keep everything already there). This makes the cadence critic also catch: stock openers ("let me make this concrete"), cold/vendor tone, overclaiming a Stars result from an operational proof, and any printed contract ID. Save.

---

## STEP 3 (backstop) — Draft Audit · `f_0ti6ehbktFZ6uMkz8dT`

The figure critic currently only fails contract IDs that aren't in the source. Under the new no-contract-ID rule, ANY contract ID in the copy should fail. Three precise edits to its prompt (paste the replacement clause over the existing one; leave the rest of the critic intact):

**Rule 2 — replace:**
> `2. Any contract ID appears that is not in the source data.`

**with:**
> `2. Any contract ID (an H-number or any single-contract identifier) appears anywhere in the draft subject or body. Contract IDs are banned from copy entirely now; payer-level plan/brand names are fine, CMS contract numbers are not.`

**Rule 5 — add these to the banned list:**
> `, "let me make this concrete", "let's make it concrete", "to make this concrete", "here's the concrete version"`

**Rule 9 — replace the artifact wording** so it's payer-level, not contract-level:
> replace every "the contract-level artifact" / "their contract's numbers" / "their contract" with "the payer-level service-measure breakdown" / "the service measures on their book". The PASS behavior is unchanged (a close that offers the breakdown and a specific low-friction 15-minute ask); only the wording drops the single-contract framing.

Save.

---

## AFTER PASTE

- Tell me it's in and I'll re-sync `Clay_MessageGen_SystemPrompt_v2.md` to v2.4.0 verbatim (the canonical mirror).
- E2-E5: the stage sheets are already patched (concrete line killed, payer-level, gracious close). Those apply when the 5-touch workflow's MessageGen nodes are updated or when the manual E2/E3 drafts are regenerated. Not part of this paste; flag when you want the E2-E5 workflow-node paste sheet.
- Tonight: send Nate's real emails and I retrain the Nate skill + swap the §3 gold standard.
