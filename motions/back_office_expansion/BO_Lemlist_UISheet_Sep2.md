# UI sheet: finish the back-office lemlist campaign shells (Sep 2 2026)

Written Sep 2 2026 after the API build. Five campaigns exist as DRAFTS with full
sequences, created by API, zero leads, nothing activated. This sheet covers only what the
API cannot do. Steps are in dependency order; do them top to bottom. Anything marked
(confirm) is a label I could not verify on lemlist's current screens; read it off the
screen and tell me if it differs rather than hunting for my wording.

## The five campaigns

| Campaign | ID | Sequence |
|---|---|---|
| BO Expansion - Healthcare Payer (Nate) | cam_N92Tgg29ncHWnYAD9 | E1 > LI visit > LI connect > LI msg > E2 > call task |
| BO Expansion - Financial Services (Nate) | cam_x8ehMHnWSjBr2CLQe | same spine |
| BO Expansion - Insurance (Nate) | cam_HCu4jiFB8oinz2s3F | same spine |
| BO Expansion - BPO (Nate) | cam_Fy287YF9X5fjPYBSo | same spine |
| BO Net-New - Back Office (Nate) | cam_DNErdZPANvC2sqRCK | E1 > LI connect > voicemail > LI msg > E2 > breakup |

Copy source of truth: `BO_Lemlist_Campaign_Copy_Sep2.md` (this folder). IDs also in
`BO_Lemlist_Campaign_IDs_Sep2.json`.

## Part 1: assign Nathan as sender (do this FIRST)

The API cannot set senders; all five show no sender. Assign the sender before reviewing
the sequences, because the LinkedIn steps may display as unavailable until a
LinkedIn-connected sender is on the campaign.

For each of the five campaigns:
1. Open the campaign, go to its settings or Options area (confirm where sender settings
   live on the current screen).
2. Set the sender to Nathan Belfield (nathan.belfield@intradiem.com), the same identity
   the Stars and Blitz campaigns use. His mailbox and LinkedIn are already connected in
   his seat (the running Stars campaigns prove it).
3. If the screen asks which channels to enable for him, match a running Nate campaign
   (email + LinkedIn + phone).

## Part 2: label all five `gtm-engineering-bo`

The API accepted the label on create but did not persist it; all five read no label.
Apply the label `gtm-engineering-bo` to each campaign from the campaign list or campaign
settings (confirm where labels are managed on the current screen). This label is the
tracking key the strategy doc fixes for the pipeline council receipts, so do not skip it.

## Part 3: review each sequence, in the Sequence tab

What to check per campaign, reading against `BO_Lemlist_Campaign_Copy_Sep2.md`:
1. Step order and delays match the table above.
2. The LinkedIn connect and LinkedIn message steps are set to require manual approval
   before sending (the API set this; confirm the toggle on screen reads that way).
3. The connect step carries NO note (blank invites are the house rule).
4. The call and voicemail steps show their instructions; both say cleared names only.
5. Do NOT edit step copy in this pass and do NOT delete or reorder steps after any lead
   is ever loaded (the Aug 31 Stars lesson: the API cannot undo step edits once leads are
   reviewed; while there are zero leads I can still fix anything by API, so ask me
   instead of hand-editing).

One known design point, not a defect: the customer-lane sequences are linear, so the
LinkedIn message step fires without an accepted-invite condition. If you want the
conditional branch structure the Stars campaigns use (message only after the invite is
accepted), that is a UI edit; decide it now while the campaigns hold zero leads, and if
you want it, do it in the UI for one campaign and tell me which so I can read the
structure back and confirm the other four match.

## Part 4: schedule check

The API created a default schedule for each campaign. Open one campaign's schedule
(confirm tab name) and check window and timezone against a running Nate campaign; fix all
five if the default looks wrong.

## Part 5: what NOT to do yet

- Do not load any leads. Loading is the gated wave process: owner_cleared rows only,
  after gate-integrity-auditor and lemlist-lead-integrity pass on real rows, human
  sign-off, warmup green.
- Do not press launch or review on any of the five.
- Do not add A/B variants; the B slots stay empty for marketing's vertical copy
  (early Sep).

## Variable contract for the eventual load (for the Clay side, not the UI)

Every lead in the four customer campaigns must carry: `function`, `parent_account`, and
`enterprise_line` ALWAYS populated (the AM-cleared enterprise sentence when brand_safe,
otherwise the neutral vertical line from the copy doc; never empty, or lemlist holds the
lead). Net-new leads carry `function` and `parent_account`. `{{firstName}}` is native.
