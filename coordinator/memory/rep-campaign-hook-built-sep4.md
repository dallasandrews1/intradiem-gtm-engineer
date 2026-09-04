---
name: rep-campaign-hook-built-sep4
description: "Sep 4 2026: rep-campaign-hook built and loaded (hourly :25) to close the rep-built-campaign gap behind the ST Water bounces; discovers unmapped lemlist campaigns, maps them by sender, checks every lead for a Clay record, dry-run estimates verification"
metadata: 
  node_type: memory
  type: project
  originSessionId: a6d03946-e33b-42bc-beba-7939d9b83bcc
  modified: 2026-09-04T17:24:06.870Z
---

Built Sep 4 2026 on Dallas's ask, immediately after the ST Water fix. Closes the gap in [[st-water-bounces-rep-loaded-gap-sep4]]: a campaign a rep builds by hand in the lemlist UI never passes the Clay verify path, and the relay only reports its bounces after they happen.

**Shape (two steps, mirrors the relay wrapper pattern):** `automation/run_rep_campaign_hook.sh`, launchd `com.dallasandrews.gtm.repcampaignhook` hourly at :25, fifteen minutes after the relay at :10.
- Step 1 `automation/rep_campaign_hook.py`, deterministic, no Claude: lists campaigns over REST, diffs against `campaign_channel_map` plus its own `config/rep_campaign_hook.json` seen list, resolves the rep (campaign sender, then creator, then a "(Jack)" name hint) and ADDS the id to the relay map. That map write is its only write outside logs and staging. Then it pulls each lead and looks for a Clay Audiences record by email, falling back to LinkedIn URL slug, runs the address-pattern checks, and writes a DRY-RUN credit estimate for `wf_0tk4jo5z7RjGKo3rvR8` against the 200 line with per-row inputs staged as JSONL.
- Step 2 Claude, launched only when step 1 found something: `lemlist-lead-integrity` scoped to the new campaigns plus the free Clay bridge (0 credits) on no-record leads, appended to the same dated log.

**Address-pattern checks (the ST Water defect class, pure string work, no credits):** reversed name order (`cawley.stephanie`), local part not matching the first name or surname, hyphenated surname loaded collapsed (flagged as ambiguous rather than wrong, because both forms are plausible and only verification decides), domain drift inside one campaign (a lone `.com` among `.co.uk`), and one person carrying two addresses. Name matching is on TOKENS, not substrings, or `phil.hunter` passes for surname Hunt; first names carry nickname tolerance in both directions (Philip/phil, Daniel/dan) while surnames get none. Apostrophe surnames are excluded on purpose, since O'Sullivan collapses to osullivan by convention. Regression suite `automation/test_rep_campaign_hook.py` (11/11) is fixtured on the real ST Water rows before and after the fix, so it fails if the hook stops catching the bounce it was built for.

**Three bugs caught while building, each worth remembering:**
1. An f-string with escaped quotes inside the wrapper's inline python is a SyntaxError, and the surrounding `except Exception: print("")` swallowed it into a silent "nothing new", so step 2 would never have run. Python now writes a pipe-delimited `staging/rep_hook/_handoff.txt` and the shell parses no JSON at all. Any wrapper deciding whether to launch Claude from inline-python output has this failure mode.
2. `--no-map-write` originally still saved the seen list, so a dry test suppressed the next real run. Look-but-do-not-touch modes must skip every write, state included.
3. Skipping any campaign already in the relay map meant a draft mapped while empty was never re-checked, so a rep loading leads into it later would go unseen. Mapping is routing, not verification: the skip now keys on the hook's own seen state, and a campaign swept while empty carries `recheck_when_loaded` and is silently re-checked every run until leads arrive.

**First live run** mapped three unmapped Jack campaigns (UK Named Accounts / Prospect Clinic, BA Test, BA BOO) and flagged BA Test: 34 leads, 30 with no Clay record, a misspelled local part (`johnathan.foster@ba.com` for Jonathan Foster) and Steven Ellis loaded twice on two addresses. Registered as rundown source 14 in both SKILL.md copies and in `~/coordinator/AGENT_REGISTRY.md`. Related: [[feedback-enrich-in-clay-never-lemlist]], [[lemlist-relay-campaign-map-gap-aug7]].
