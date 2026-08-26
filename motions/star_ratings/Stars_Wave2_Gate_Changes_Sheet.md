# Stars Wave 2 — Gate Changes Sheet
Date: 2026-07-20 · Table: Contacts (Buying Committee) `t_0thtm73HHxyiupTuepK` · workspace 1180800

Goal: remove the per-row `human_approved` checkoff, and add a `wave_number` gate so only the
wave you intend can enter the campaign. Net effect: clean + non-customer + right-persona +
current-wave rows flow into the campaign on their own; your only gate is launch. Nothing sends
until you launch the campaign (it stays Draft).

ORDER MATTERS — do Step 1 before Step 3, or the sync gate will reference a column that doesn't
exist yet.

## Step 1 — Create the wave column
Add a new **Number** column named exactly `wave_number`.
Tag your intended wave-2 slice with `2` (keep it to ~30-50 rows, not all 60). Leave every other
row blank. Wave-1's already-sent rows can stay blank (they've shipped; the ==2 gate won't touch them).

## Step 2 — Drop human_approved (removes the checkoff)
Open the `send_ready` column (`f_0thtsyrabg7qGSqe5gf`) → edit its formula.
- BEFORE: `{{critic_email_valid}}=="PASS" && {{human_approved}} && !{{bdr_claimed}} ? "READY" : "HOLD"`
- AFTER:  `{{critic_email_valid}}=="PASS" && !{{bdr_claimed}} ? "READY" : "HOLD"`
(Just delete ` && {{human_approved}}`. Everything else stays byte-identical.)

## Step 3 — Add the wave gate to BOTH sync columns
The two persona sync columns each have a run condition (Configure → Run condition / conditional run).
Append ` && {{wave_number}} == 2` to the very end of each. Do not change anything else in them.

`Sync leads to campaign (2)` — Persona 1 / stars_quality (`f_0ti5fzpC6KQ6NjVadCZ`):
- AFTER: `send_ready == "ready" && not bdr_claimed && customer_exclude != "true" && Account Forgone QBP ($M, 2026-cycle) > 0 && Persona Key == "stars_quality" && msg1_critic Status == "PASS" && Voice Audit.voice_verdict == "PASS" && {{wave_number}} == 2`

`Sync leads to campaign (3)` — Persona 2 / coo_finance (`f_0ti5hg5NMbD7o5ZB8gh`):
- AFTER: `send_ready == "ready" && not bdr_claimed && customer_exclude != "true" && Account Forgone QBP ($M, 2026-cycle) > 0 && Persona Key == "coo_finance" && msg1_critic Status == "PASS" && Voice Audit.voice_verdict == "PASS" && {{wave_number}} == 2`

(The clauses above are the plain-language version of what's already in each condition; you're only
adding the final `&& {{wave_number}} == 2`.)

## What stays (the safety that costs zero clicks)
- `customer_exclude != "true"` — keeps current customers out of a cold campaign. NEVER remove.
- `msg1_critic Status == "PASS"` — keeps wrong-number drafts out.
- `Voice Audit.voice_verdict == "PASS"` — keeps AI-sounding drafts out.
- persona match + forgone > 0 — routing + real dollar basis.

## For the next wave
To run wave 3 later, change `== 2` to `== 3` in both sync conditions and tag that slice `3`.

## Reminder
Once these are live, qualified wave-2 rows auto-sync into the (Draft) campaign. They only start
emailing when YOU launch the campaign. Review the campaign, then launch.
