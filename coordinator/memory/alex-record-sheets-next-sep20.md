---
name: alex-record-sheets-next-sep20
description: "Sep 20 2026 decision: next build for Alex Bauer is a record sheet per account (his first dated move on all six plans); the account-plan-fields version waits on the Mary Ann huddle; briefs only when a door opens"
metadata:
  type: project
---

**Decided with Dallas, Sep 20 2026:** Alex was fully part of the Sep 20 upgrade (six rooms, six shelves, index, roadmap fit, all live on three hosts). What helps him next, in order:
1. **Record sheet per account, BUILD NOW.** "Confirm the record" is the first dated move on all six plans (Sep 21 on five, Sep 15 on Elevance) and gates everything after it. One page per account from the install-base table, Salesforce via Clay and Alex's own account plan: seats, live modules, customer since, renewal date, admin of record, contracted entity. It must LEAD WITH CONFLICTS AND BLANKS (Synchrony 5,700 seats vs 6,347 agents and two admin names; Citi has no Customer record; AT&T back office reads Prospect; Elevance has no parent record), because the no-fluff rule forbids showing a rep his own CRM back to him. A field that agrees everywhere earns one line at most.
2. **Account-plan-fields copy-paste version: DO NOT BUILD YET.** Dallas promised it to Alex on Sep 15 2026 pending a huddle with Mary Ann Chandler on her format. The huddle has not happened. The only action is getting it booked; a finished record sheet is the sample to bring.
3. **Sourced briefs: only when a door replies**, for that one account, ahead of the working session (Oct 26 on his plans). Not all six up front.

**STATE Sep 20 2026, later session: six record sheets LIVE on all three hosts** (save-rooms 6346a3d8, intradiem-accounts 37d30e55, maps 9389f774 unchanged; read back whole-site, zero files differ; gate 109 of 109; Jen Lee 21 of 21 newest). Mary Ann note is an UNSENT Slack draft in her DM with the Synchrony sheet as sample; when sent, move that URL under her name in the registry. The 12 record URLs are registered under a Nobody-yet entry. Data `rooms/alex_accounts/records.py`, builder `build_record_sheets.py` (re-reads the Jul 10 export workbook and fails on drift), staged at `deploy-save-rooms/<account>/alex/record/`, linked from each room header as "The record to confirm". Shaped by [[feedback-rep-word-is-the-truth]]: rows read "your word stands, Salesforce to correct", then "two values, one needed", blanks, one-source, agrees. Only TWO account plans from Alex exist (Synchrony Aug 31, Elevance Sep 11). Key finding: the export holds Customer records owned by Alex (Citicorp Credit Services, AT&T Enterprise Group, Elevance Health) that the Clay sync never surfaces, so the Sep 14 "Citi is a Prospect" read described the sync, not the account. Deploys stay Dallas's (the classifier blocks the script in auto mode despite the allow rules). OPEN: Citi and Elevance room wording contradicts the rep-truth rule.

**Why:** an AM already knows the account; depth pays at the working session, not before. The record is what blocks him this week.

**How to apply:** new pages ship through `automation/deploy_rep_pages.sh maps`, `rooms`, `plans` run by Dallas (this kind of session cannot deploy, see [[claude-code-auto-mode-blocks-deploys]]); gate before and after ([[shared-links-gate-sep20]]); standard in [[feedback-seller-pages-no-fluff]].

Related: [[rep-index-pages-sep20]], [[department-shelves-sep18]].
