# Clay MessageGen retired, Sep 5 2026

**Status Sep 5, late:** Dallas deleted the table-side surfaces (MessageGen, Msg1 outputs, Sync Leads, audits, critic status, send_ready, human_approved) from the Stars table. Live workflows validated clean afterwards. Remaining on the list, deletable at any time: the six gate/critic Functions and the seven Alpha/Pilot workflows. `Invoke Workflow`, `customer_exclude` and the two `Lookup Single Row` columns are still on the table; hidden in the demo view.

> Decision, Dallas Andrews, Sep 5 2026: the Clay drafting layer is obsolete. Prospect-facing copy is written once, Claude-side, per contact, through the first-draft engine and the copy sharpener, and loaded into lemlist as per-lead variables by the bridge. Clay does research, enrichment and storage. Clay does not write messaging and Clay does not gate sends; the gates run Claude-side on the way into lemlist. Having Clay draft what Claude already drafts is double work and burns credits per row.

## What this retires

| Surface | Status now | Action |
|---|---|---|
| `MessageGen Email` AI columns and their `Msg1Subject` / `Msg1Body` outputs on the motion tables (Stars `Contacts (Buying Committee)` t_0thtm73HHxyiupTuepK, WFM-Adjacency, Cost-Mandate) | Retired. Never run again. | Hide from every view now; delete in the UI after the all-hands recording is in the can (table-hygiene agent produces the safe-delete plan with dependents) |
| Per-touch Claygent clones (Stars/WFM MessageGen, Voice Audit, Voice Fix, Figure Critic E1-E5; 25 of the 37 live Claygents per the registry) | Retired. | Delete in the Claygents page after the recording |
| Companion critic and draft-clean Functions used only by the Clay drafts (`fn_draft_critic`, `fn_draft_clean`) | Retired as Clay columns. The rules they encode live on in the Claude-side gate (`intradiem-copy-sharpener`, `intradiem-verified-metrics`). | Leave the Functions in place until the columns that call them are gone, then delete |
| `Sync Leads` columns and `Invoke Workflow` on the motion tables (Clay to lemlist push) | Retired. The lemlist bridge (`build_lemlist_bridge.py`, workflows wf_0tksuthtP8TEFF2WxHF and wf_0tksukwf5aTgJAeDNYp) is the only path into lemlist. | Hide now, delete after the recording |
| `Clay_MessageGen_SystemPrompt_v2.md` and the Stars/BackOffice/CostMandate prompt files | Historical. The living prompt is `motions/shared/Messaging_Doctrine_Sep3.md` plus the first-draft engine. | Keep as history; never transcribe into Clay again |
| motion-stamp skill step 4 (inject MessageGen prompts into workflow agent nodes) | Retired. | Skill updated to build research and gates only; copy comes from the Claude layer |
| Golden Standard layer L4 "Message Gen + companion critic" | Re-scoped: L4 is research assembly (persona key, product angle, why-now, platforms, posts). Copy is not a Clay layer. | Noted in the standard |

| The Clay gate Functions (`fn_eligible`, `fn_tokens_ready`, `fn_email_verified`, `fn_send_ready`) and the send-ready / human-approved / customer_exclude columns on the motion tables | Retired. Nothing on the live path calls them (verified Sep 5: no script, workflow or bridge node references them; the Jul 27 audit already found no live table wired to `fn_send_ready`). The gates that actually run are Claude-side: the customer-exclusion union (Salesforce exclusion segment + install-base table + denylist) in `motions/lemlist_contacts/build_us_lists.py` and `push_us_lists.py`, the denylist re-check in the lemlist bridge code node, ZeroBounce status read from the enrichment, the verified-claims and copy gates in the skills, and Dallas's approval before a load. | Leave the Functions until the columns that call them are gone, then delete |
| The July "Alpha" workflows: Star Ratings 5-Touch Send-Readiness, WFM-Adjacency 5-Touch Send-Readiness, WFM-Adjacency Send-Readiness, Cost-Mandate Send-Readiness, Reply Triage + Draft, Stars Post-Approval Apollo Push (Pilot), ACD Detection Validation Test | Retired. All built on the Clay-drafts-and-gates model. | Delete after the recording |

## What stays in Clay

- Data: Audiences (Salesforce-synced people, companies, deals), its segments including the Cold-Outbound Exclusion segment the Claude scripts read, and the new company fields (platforms, rep-confirmed).
- Enrichment: email validation and the work-email waterfall, LinkedIn posts, the contact center platforms read, Enrich Person, `fn_persona_key` (still called by the webinar routing workflow).
- Workflows that move data, not copy: the lemlist bridge pair, Heat Lane A and Heat Stamp, LI Post Engagement A and B, Webinar Registrant Enrich + Route, Net-new contact find + verify work email, Profile URL Repair, Profile Photo Fetch, Tech stack read, Stamp rep-confirmed platform.

The dividing line: Clay finds, enriches and stores. Claude decides, writes and gates. lemlist sends.

## Why it matters for the demo

The act 2 enrichment clip shows research only: email verified, what they've posted, which platforms their company runs, persona, angle, why-now. The drafting is shown where it happens, in act 1 (the strike plan writes the sequence per person) and act 3 (each lead's lines in lemlist). Narration never says a Clay column wrote the copy.

## Credits

Every Clay draft was one or more AI-column credits per row on top of the Claude generation that actually shipped. Retiring the layer removes that cost from every future motion. Related: `Clay_Credit_Ledger.md`, `coordinator/memory/lemlist-variable-generation-is-claude-side.md`.
