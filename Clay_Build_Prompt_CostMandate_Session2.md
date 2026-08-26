# Cost-Mandate build, session 2 — migration, L3/L4, template stamp

Read project memory notes `cost-mandate-build-jul15` and `motion-structure-law-jul15`, then `Clay_Golden_Standard.md` (Section 1 structure law) and `New_Motion_Build_Runbook.md` at the project root. Sweep live Clay via Chrome before building; verify UI, never instruct from memory. Dry-run law holds: nothing sends, nothing launches, no Stars sync touched.

Execute in this order:

1. **Migrate.** Create the `Cost-Mandate Motion` workbook. Move `Cost-Mandate Universe (x-vert)` into it from the GTM Engine workbook (table menu → Move table). Verify the table, formulas, and run conditions survived the move intact (page-verbatim re-read of intent_score/intent_status on all 10 rows).
2. **Verify cross-workbook Lookup.** Test whether a Lookup in the new workbook can read the reference tables (Verified Metrics, Product-Angle Map, ICP Rubric) and the customer file. If yes, wire customer_flag as a real Lookup against the customer exclusion source. If no, seed small static copies per the structure law.
3. **Finish L1.** Add fit_score + grade formulas (config-driven weights, mirror the Golden Standard). Dedupe the JPMorganChase / J.P. Morgan duplicate (structural_exclude one).
4. **L3 contacts on the 5 eligible slice rows** (J&J, Nike, Citi, Walmart, Abbott): Find People per the ICP rubric (coo_finance + cc_ops lanes, cap 2/account), email waterfall + ZeroBounce (~1.46/contact measured), attribution tags at creation (source_motion=cost_mandate, gtm_engine_sourced, sourced_date), persona_key cost_finance/cost_ops, customer_exclude, bdr_claimed, human_approved, send_ready. This is inside the approved slice envelope (~65-110 credits remaining of Dallas's GO); log the ledger row before firing.
5. **L4 paste.** Paste the MessageGen system prompt and critic from `Clay_MessageGen_SystemPrompt_CostMandate_v1.md` into columns on the contacts table (run-conditioned on source_motion). Run the slice, critic-audit, read every rendered draft. The Claygent rif labels are directional — verify each account's signal evidence before any draft uses it.
6. **L4c campaigns.** Create the two campaigns Draft-only (Cost-Mandate Finance/COO + Ops) from `CostMandate_Persona_Sequences_v1.md`; sync columns carry the full run-condition including msg1_critic PASS. Sender webhook OFF.
7. **Stamp the template.** Once verified, duplicate the workbook (verify workbook-level duplicate exists; fallback = Duplicate table + Move per table), strip motion-specific values to placeholders, name it `Motion Template (do not edit)`. Try "Save as function" for the intent rollup formulas. Add the template step to the Runbook when done.
8. **Close out.** Ledger actuals from the Usage page (drift note if >25%), memory checkpoint, engine-side config sync (triggers.json variants with coo_finance routes, Registry slot 5, proof.json mirror) or flag it as the next task.

Decisions already ratified, do not re-ask: universe = Clay company search signal-first (~150-200 wave, HELD for separate credit go); persona keys coo_finance canonical; one motion = one workbook; slice credit GO given Jul 15.
