---
name: account-execution-kit
description: Stamps the execution kit on top of a finished account package for any AE, AM or partner rep - the persona and finding one-pager shelf with vertical-matched social proof, the what-to-send-when selector on the account room, the sequence blueprint (waves, the rep's doors, held executives, angle and asset per touch), and the lemlist campaign draft, gate closed. Trigger on - build the execution kit for [rep or account], one-pager shelf, what do we send after a reply, sequence blueprint, wave plan for [account], give [rep] the Keegan treatment, make the kit for the next AE, execution package, sales kit for [account]. Load after an account package (maps, room, brief, one-pager) exists and someone asks how the sales org executes it.
---

# Account execution kit

The plan half tells a rep where to go. This kit is what they carry. First run: Keegan Sanders, Sep 18 2026 (`motions/keegan/accounts/`).

Read `~/Claude/Projects/Intradiem GTM Engineer/motions/shared/Account_Execution_Kit_Runbook_Sep18.md` before doing anything. It holds the pieces, the standing decisions, the ten build steps in dependency order, the gates and the known traps. Follow its order.

## Fastest path for the one-pager shelf
For any rep after Keegan use the shared builder: write `shelf_<rep>.py`, run `motions/shared/execution_kit/build_shelf_generic.py` on it, then `link_shelf.py`. Give a builder agent `SHELF_BUILD_BRIEF.md` plus the department objective (AE net-new, AM expansion, AM save and renew, partners); the runbook lists how each objective changes the pages.

## Non-negotiables
- Prerequisite: the account package exists (live-checked map sheets, plans, research files, contacts). If it doesn't, build that first.
- Every finding on a page is the account's own public fact with a source and date. Proud, not wound. The account's rules in `plans.py` govern what is never named.
- Social proof ships: blinded results from marketing's published-stories registry, in marketing's wording. Named only per marketing's Status column. JPMC, AT&T and Liberty Mutual are never referenced. Greenlight data stays internal.
- The one-pager template file is locked. Slots get filled; the proof tile is injected by `shelf.with_proof`.
- No message bodies and no contact details on any page. Copy lives in lemlist under the sender.
- Read the newest live campaign before cloning copy, and read the whole messaging doctrine including the Sep 4 addendum and the Sep 18 decisions.
- Stage by default. Deploy, load and launch only on Dallas's explicit ask. Never flip a send gate.
- Colleague-facing pages carry no defect ledger; defects go to the log and to Dallas.

## Output
Staged pages under `deploy-save-rooms/<slug>/<rep>/` (one-pagers, sequence, room with selector), PDFs in a Desktop deliverables folder named for the rep, a paused zero-lead lemlist draft with its build record and staged variables, one log with evt anchors, one memory file. Report what is staged, what was decided, and what still needs Dallas's hand, in order.
