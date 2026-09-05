---
name: messagegen-stale-vs-sep3-doctrine
description: "Sep 4 2026: the Clay MessageGen Email column on the Stars table still runs pre-Sep-3 doctrine (5-touch arc, 75-115 words, 'Worth 15 minutes' CTA) while live campaign copy is now hand-authored outside Clay under Messaging_Doctrine_Sep3"
metadata:
  type: project
---

Checked Sep 4 2026 against the live column settings on `Contacts (Buying Committee)` (t_0thtm73HHxyiupTuepK, column `MessageGen Email`, model claude-sonnet-5, 17,092-char system prompt).

**The column is stale against `motions/shared/Messaging_Doctrine_Sep3.md`**, which explicitly supersedes the copy sharpener, first-draft engine, motion-stamp voice core and stage ladder, and the Aug 3 first-touch doctrine. Three hard conflicts:
1. **Sequence arc.** Prompt says "one email in a 5-touch story" with an E1 to E5 ladder. Doctrine is three emails, two LinkedIn touches, phone between touches.
2. **Word count.** Prompt says 75 to 115 words; doctrine says Email 1 under 110. Live output is worse than both: Krista Dusil 138 words, LaTonya Augustine 140.
3. **The CTA.** Prompt's gold standard and live drafts end "Worth 15 minutes in the next couple weeks?". Doctrine killed exactly this: "One low-friction question that names the topic. No calendar, no minutes, no demo, no time slot in email 1."

The prompt also still carries `[TO BE FILLED TONIGHT]` where Nate's real sends were meant to be appended as the voice anchor.

**Live campaign copy is authored outside Clay.** Nate's four Stars/Blitz campaigns plus the Quality draft were rewritten Sep 3 in `motions/star_ratings/Nate_Copy_Rewrite_Sep3.md` and applied straight to the lemlist steps by API (backup `Lemlist_Sequences_Backup_PreRewrite_Sep3.json`), using lemlist per-lead variables like `{{plan_name}}` and `{{qbp_avg}}`. Same pattern for `BO_Lemlist_Campaign_Copy_Sep2.md` and `DWO_Exec_Sequence_Sep4.md`. So personalization now happens through variables filled at load, not per-row AI generation.

**Why it matters:** two different architectures are live at once, and the all-hands demo was about to show the retired one. Nothing in lemlist reads `Msg1Body` today.

**How to apply:** before the demo shows a MessageGen draft, either update the system prompt to the Sep 3 doctrine (arc, 110-word cap, CTA rule, and stop the 138 to 140 word overshoot) and re-run the five demo rows, or narrate the beat as drafting only and let act 3 carry what reps actually send. Decide which of the two authoring models is the go-forward path before stamping any new motion. Related: [[allhands-ai-session-package-aug31]], [[positioning-automation-first-aug17]].
