# WFM Adjacency Clone Pack — CORRECTION (2026-07-17)

**Read this alongside `WFM_Adjacency_Clone_Pack_v1.md`. Where they disagree, this wins.**

Source: live verification of the `Golden New-Logo Scaffold` (wb_0tib7v5msZ2qYbGc4AC) in Clay on 2026-07-17.

## The correction: re-populate ALL THREE AI columns per stamp, not two
Clay's **Duplicate table does NOT carry over "Write with AI" column prompts.** Verified live: all three AI columns on the golden L3 — `MessageGen Email 1` (Sonnet), `Draft Audit` (GPT-4o), and `Email Voice Audit` — came through the duplicate with **empty prompt boxes** (only model + structure survived; Clay suggests re-applying the saved Claygent).

The original Clone Pack Part A lists only MessageGen + Draft Audit. **That is incomplete.** Every stamp must also re-populate `Email Voice Audit`. If it's left blank, the stamped motion ships with:
- **no voice gate** → the exact "sounds like AI" failure Tom (CMO) flagged, re-introduced structurally, and
- (if Draft Audit is also skipped) **no figure-integrity critic** → unsourced numbers can pass.

## Corrected AI-column step for every stamp
| Column | Model | What to paste per stamp | Motion-specific? |
|---|---|---|---|
| `MessageGen Email 1` | Sonnet | The motion's §2 MessageGen system prompt | YES — always per-motion |
| `Draft Audit` | GPT-4o | The motion's §4 critic (shared base + motion FAILs) | Mostly — shared base, motion-specific FAILs |
| `Email Voice Audit` | (as built) | The **universal** voice-audit prompt — identical every motion | NO — reusable verbatim |

## Recommended fix so this stops costing time: save-as-Claygent
Because the two motion-AGNOSTIC pieces (`Email Voice Audit`, and the shared base of `Draft Audit`) are identical across motions, save them as **Claygents** once, then **apply** them to the column in one click per stamp instead of pasting long prompts. Clay already surfaces this ("Use a saved Claygent"), and the MessageGen Claygent ("Cost-Mandate MessageGen Email1") shows you started down this path. Target end-state per stamp:
- `Email Voice Audit` → apply the saved **Voice Audit (universal)** Claygent — zero editing.
- `Draft Audit` → apply a saved **Draft Critic (base)** Claygent, then add the motion FAILs.
- `MessageGen` → paste the motion §2 (this one is always bespoke).

## Also confirmed on the golden (so you don't re-check)
- `Universe Lookup` already targets the golden's own L1 — after you duplicate to a motion, RE-POINT it to the NEW workbook's own L1 (this is the recurring silent breakage; verify the workbook id).
- `Source Motion` = `<<motion>>` on the golden → set to the motion key per stamp.
- L1 = clean firmographic structure, 0 rows, no bound universe source.

## Pre-first-stamp STEP-4 checks still owed on the golden (read-only, ~2 min)
Confirm on the golden L3 before trusting the stamp: optional inputs (`li_recent_post_hook`, `disclosed_figure`, `disclosed_figure_source`) have **Required-to-run = OFF**; no AI column shows a stray "Agent template being used" banner with auto-run; sender webhook/sync = OFF. (These are the settings that blocked node 4/6 in the CM workflow build.)
