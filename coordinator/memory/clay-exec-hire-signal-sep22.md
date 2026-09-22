---
name: clay-exec-hire-signal-sep22
description: Clay workflow wf_0tlsaeuxF4TykJKs2Tv, executive-hire signal (domain in, recent leader hires out), published Sep 22 2026; plus the four CLI gotchas the build cost a cycle each
metadata:
  type: project
---

Built and published Sep 22 2026 after Dallas rejected an Apollo version ([[feedback-use-the-paid-stack]]). Workflow `wf_0tlsaeuxF4TykJKs2Tv`, three nodes: manual trigger taking `company_domain`, Icypeas `find-people-at-company` filtered to the title taxonomy in `october-flywheel/config/exec_signal.json` plus United States, then a Python code node keeping only leaders whose current role started inside the window. Signal file `october-flywheel/signals/exec_hires.csv`, read by `score_accounts.py` as the `new_exec` moderate signal.

**Icypeas `find-people-at-company` already returns `lastJobStartDate`**, so no separate profile-read step is needed. The two pre-existing LinkedIn profile-check workflows (`wf_0tlqmjdJhZeKuj6gYzs`, `wf_0tlqmxpbyV8UYBPe6mN`) stay useful for a single known URL but are not in this path.

Result across all 72 scored Tier 1 and Tier 2 accounts: **9 carry a recent leader hire, 13 hires total**, from roughly 300 leaders. Strongest is Blue Shield of California, 4 recent of 9 leaders including a COO who started Aug 2026. About 2.4 data credits per account.

**Four Clay CLI facts, each of which cost a build cycle:**
1. `inputMappingConfig` type discriminators are `static | reference | coalesce | item | skip | map`. NOT `literal`.
2. Edges are set with `incomingEdges: [{"sourceNode": "wfn_..."}]` on the node itself. There is no edge command, and CLI-created nodes arrive unconnected, including from the trigger.
3. Code nodes run **Python**, not JavaScript, and the contract is `def handler(context)` with `context.get_input()`. A bare `return` at module level is a syntax error.
4. The code sandbox has **no `datetime` and no `calendar`**. `time` works, so use `time.gmtime().tm_year` / `.tm_mon`.

**The failure worth remembering:** 32 of 72 runs failed on `path "$.result.leads" resolved to undefined`. When an account has no matching people, the finder OMITS the `leads` key rather than returning an empty list, so the reference breaks. Reference the parent object (`$.result`) and dig for the optional collection inside the handler. Applies to any Clay reference into something that may be absent.

Test out of band before wiring: `clay workflows code test --file handler.py --inputs inputs.json`. Related: [[signal-scoring-model-sep22]], [[enrichment-doctrine-clay-not-lemlist]].

**SUPERSEDED the same day by Clay's native New hire signal, which is roughly seven times better.**
Signal table `t_0tlsexb7wv6dCvdpqX9` in workbook `wb_0tlsckobh5jFUyecchR`, daily, 3-month window, seniority exactly Director/VP/C-suite/Head, 26 title filters, no enrichments, 432 credits a month. First run: **24 hires across 17 of the 72 companies in a THREE month window.** My Icypeas workflow found 13 across 9 in a TWELVE month window. About 8 a month against 1.1.

That kills the argument I gave Dallas for keeping the batch, which was that a signal cannot backfill because it only sees forward from switch-on. The native signal's three-month lookback already beat my twelve-month batch. **Retire `wf_0tlsaeuxF4TykJKs2Tv` as the exec-hire source and point `score_accounts.py` at the signal table.**

The general lesson: before hand-building a detector on a generic people-search action, check whether the platform has a purpose-built one. Icypeas find-people-at-company returns whoever it holds for a title match with a `lastJobStartDate`, so detection depends on the record existing and being dated. A native job-change feed watches transitions directly and sees far more.
