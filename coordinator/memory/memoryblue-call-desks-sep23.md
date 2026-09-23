---
name: memoryblue-call-desks-sep23
description: "Sep 23 2026: memoryBlue call desks SHELL staged (Tyler front office, Aiden back office); link in the clear, contacts and cards sealed by passphrase; fills only on Nate's go after Kevin's sign-off"
metadata:
  type: project
---

**What:** `motions/memoryblue/` builds one link-style desk per memoryBlue caller (Tyler Walden, front office; Aiden Thall, back office) plus a root page for Nate, in the rep-page look. Staged to `~/Desktop/Intradiem Deliverables/deploy-call-desk/`, NOT deployed; Pages project `intradiem-call-desk` not created yet. Deploy target `automation/deploy_rep_pages.sh desk` added. Log: `automation/logs/memoryblue-desk-2026-09-23.md` (evt `memoryblue-2026-09-23#desk-shell-staged`).

**Nate's rules (DM Sep 23 09:21 CT):** Tyler front office, Aiden back office; "send everyone", no lemlist exclusion (the card marks a note in the inbox instead). memoryBlue dials from its own Salesforce, not ours, so a folder per desk plus a list id per person (FO-W1-001, BO-W1-001) is the reporting contract Nate takes to pipeline council. Nate needs Kevin's sign-off (one-on-one Sep 23) before any contact loads.

**Design decision:** the Sep 22 rule (method pages are links, contact detail is a file) is kept on one link: rules, card shape and reporting are plain; contacts and per-person cards are sealed (PBKDF2 250k + AES-256-GCM via `encrypt.js`, WebCrypto in the browser); the CSV for their Salesforce is built in the browser. Passphrases in `automation/config/memoryblue_desk.json`, one per desk, `handed_to` null; link and passphrase travel in separate messages. Builder gate fails on any surname, domain, email, number or LinkedIn URL in the clear.

**Fill order on the go:** contacts in Clay (exclusion union, domain match, sourced numbers) to `people/<desk>.json`; cards with `intradiem-cold-call-playbook` then `gtm-copy-reviewer` to `cards/<desk>.json`; build, then project create from an EMPTY folder with `--force` and deploy from Dallas's terminal; register URLs in the manifest. Confirm with Nate first: how memoryBlue introduces itself, folder names, CSV or page. Related: [[stars-call-cards-sep22]], [[strike-room-guide-deployed-sep22]], [[wrangler-pages-force-delegation-trap]], [[claude-code-auto-mode-blocks-deploys]].
