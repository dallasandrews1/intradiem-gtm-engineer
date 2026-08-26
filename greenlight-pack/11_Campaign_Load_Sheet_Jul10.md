# Campaign Load Sheet: Stars QBP Wave 1 (Jul 10 2026)

Paste-ready copy for the existing campaign (Campaign Group + 3 Message Groups, input: Rows from Contacts (Buying Committee)). Each Message Group = one touch in the sequence. Nothing here launches anything; this stages copy so the campaign renders real emails for review.

## Before pasting anything (order matters)

1. Runbook 10 steps 1 and 2 first (purge the 10 pre-gate leads, provisional customer_exclude). Otherwise the wrong rows are what render.
2. **Repoint the sync field mapping.** The Sync-leads enrichment still maps off an aux column (`New Column (2)`), flagged in doc 09. Open the sync column settings and remap every field to the real display columns (First Name, Company, email_final, and the three QBP columns). If this isn't fixed, merge fields resolve blank or wrong.
3. **Add a sync condition for cliff parents only:** `Cliff-Edge Contracts` present / `Account Forgone QBP` > 0, on top of the existing `send_ready == "READY" && bdr_claimed != true`. Nine eligible parents sit at 3.0 stars with no cliff contract this cycle (CalOptima, L.A. Care, Lumeris, IEHP, Presbyterian, Zing, CHPW, ATRIO, Baystate); this copy leads with the cliff dollar and would render wrong for them. They get their own later wave with longer-horizon copy.
4. **Verify the two QBP cells render as expected.** Open the Centene row and read `Cliff-Edge Contracts` and `Account Forgone QBP`. The copy below assumes a contract reference and a dollar figure. If the cell holds longer analysis text, trim the phrasing in Preview before saving.

## Persona structure

This campaign carries **Persona 1 (Stars/Quality)** copy. Finance contacts get a **cloned campaign** with the Persona 2 copy below (duplicate the campaign, swap the three messages, filter each campaign's sync by persona). There's no persona column yet; the free fix is the `persona_key` formula column already spec'd in doc 03 (route from Job Title: Stars/Quality/CAHPS/Member Experience → stars_quality; CFO/Finance/Actuary → coo_finance). Add it before syncing so each campaign's condition can filter on it.

Signal variants (1C, 2C) stay out of the sequencer: their tokens (recent_signal, filing_or_call) have no live column. They're the 1:1 strike-room lane.

## How to paste (per Message Group)

Open the Message Group, paste the body text, then replace each `[VAR: ...]` marker by typing `/`, choosing **Clean variable**, picking the named column from Rows from Contacts, and setting the fallback shown. Keep **plaintext** (no HTML), per deliverability SOP. Toggle **Preview** against a Centene row, then **Send test email** to yourself.

---

## CAMPAIGN 1: Persona 1, Stars/Quality (this campaign)

### Message Group 1 (Day 0)

Subject: `the last stretch to 4.0`

> Hi [VAR: First Name, fallback "there"], I've been doing contract-level math on the public CMS release, and [VAR: Company, fallback "your plan"]'s picture caught my eye: [VAR: Cliff-Edge Contracts, fallback "your largest MA contract"] sitting a half-star under the bonus line, an est. [VAR: Account Forgone QBP, fallback "real bonus money"] from public CMS enrollment and ratings data. You'll know the exact picture far better than I do. What stands out is where the remaining gap tends to live for books that close: the customer-service measures, CAHPS experience, complaints, appeals, and they're being set right now, in this measurement year, not on the October release.
>
> Thought it might be worth talking through which contracts sit closest to the line and which measures still move them this cycle. Have 15 minutes in the next few weeks?

### Message Group 2 (Day 4, same thread)

> Hi [VAR: First Name, fallback "there"], one thing I didn't say last week: the customer-service measures that count for 2028 Stars are scored only through this December. After that, the same gap gets harder to reach and concentrates into CAHPS. I've got the measure-level view for [VAR: Company, fallback "your plan"]'s contracts as a one-pager; want it?

### Message Group 3 (Day 9, same thread)

> Hi [VAR: First Name, fallback "there"], closing the thread. If Stars sits with someone else on your team, point me at them and I'll keep it short. Either way, the contract-level math is a one-pager built from public CMS data; it's yours whenever it's useful.

---

## CAMPAIGN 2: Persona 2, Finance (clone this campaign, swap messages)

### Message Group 1 (Day 0)

Subject: `the bonus question`

> Hi [VAR: First Name, fallback "there"], from the finance seat the 4.0 line is really a quality-bonus question, and [VAR: Company, fallback "your plan"] looks to be sitting right under it: an est. [VAR: Account Forgone QBP, fallback "a full cycle of bonus"] a year, from public CMS enrollment and ratings data. The measures still movable this cycle are mostly operational, not clinical, so it's the slice operations can close without touching HEDIS. I'll concede the clinical side; that's what makes the math hold up.
>
> Thought it might be worth 15 minutes on how you're modeling the cliff. Open to it?

### Message Group 2 (Day 4, same thread)

> Hi [VAR: First Name, fallback "there"], the timing detail that matters for the model: the service measures behind that bonus are scored only through December for 2028 Stars. Missing 4.0 by a fraction costs the same as missing it by a lot, one cycle of bonus either way. The contract-level math is one page; want it?

### Message Group 3 (Day 9, same thread)

> Hi [VAR: First Name, fallback "there"], last note from me. If Stars exposure is modeled by someone else on your team, point me at them and I'll keep it short. The one-pager stands either way: public CMS data, contract level.

**Sharpener catch resolved (Jul 10):** the planted banned construction "happy to be pointed there" was replaced with "point me at them and I'll keep it short." Confirms the v2.2 sharpener pass ran on Touch 2 and 3.

---

## Schedule settings (per campaign, from the SOP)

- Plaintext, HTML off (also disables open/click tracking, which is correct for cold).
- Minimum time between sends: 20 minutes.
- Maximum new leads per day: start at 10.
- Days: Tue to Thu to start. Timezone: recipient-market Eastern.
- Sequences auto-stop on reply (Clay detects and skips OOO). The pause-same-company action per the SOP rides on top.
- Campaign start date: leave unset. Launch is a separate, deliberate act after warmup is green and the walkthrough meeting happens.

## Provenance and gates

- Touch 1 copy adapts approved pack variants 1A/2A to the columns that actually exist (the pack's `{{qbp_avg}}` token has no live column; the cliff-dollar framing replaces it). Touch 2 and 3 are new copy written to v2.2 rules; **the v2.2 copy-sharpener pass ran Jul 10** (verified-claims gate clean, zero forbidden words, zero em dashes, one question per CTA, Finance/Stars persona tone matched, planted banned construction fixed). One open item before launch: confirm the campaign signature block, so per-touch sign-off convention is right (sender first name Days 1-5 = Nathan; full name Day 6+ = Nathan Belfield on the Day 9 closers). If the campaign auto-appends a signature, leave the bodies unsigned to avoid doubling.
- No Intradiem metric or customer claim appears anywhere; all figures are the prospect's own, labeled as public CMS estimates. Verified-claims gate intact.
- Week 3-4 variant test: check whether a Message Group accepts multiple messages inside it (variant slots). If yes, add 1B/2B there; if no, clone campaigns per variant and split leads.

## The 10-minute check when done

Preview 3 leads (one Centene, one small parent, one edge row), send both test emails to yourself, read them as the prospect. If the QBP cells render as analysis text instead of clean figures, trim phrasing in the message, not the column.
