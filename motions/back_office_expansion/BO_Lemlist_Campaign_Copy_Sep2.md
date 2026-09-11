# Back Office lemlist campaigns: copy v1 (Sep 2 2026)

Sender: Nathan Belfield. Compiled per BO_Expansion_Strategy_Aug24.md item B7 through
intradiem-first-draft-engine, intradiem-copy-sharpener, and the verified-claims gate.
Status: DRAFT SHELLS ONLY. No leads loaded, nothing activated. A/B slots reserved for
marketing's vertical copy (early Sep); do not create empty B variants.

## Design decisions

- **Verified-claims posture: mechanism-only.** Zero statistics, zero customer outcomes,
  zero named or blinded peer claims in any template. The launch kit fixes BOO copy as
  mechanism-only, and the one usable 1:many story (Humana) is itself a wave-1 target
  account, so peer-proof beats are rewritten as mechanism observations. Claims ledger: empty
  by design; nothing to verify, nothing [UNVERIFIED].
- **Customer campaigns never say or imply "existing customer."** Default copy reads as
  smart cold outreach on back-office pain. The enterprise-layer connection rides ONLY in
  the `{{enterprise_line}}` variable in Email 2, populated per lead at load time:
  - brand_safe = TRUE (AM cleared the brand name): "There's also a version of this your
    own front office already runs today, which makes the conversation more concrete than
    a cold pitch."
  - brand_safe = FALSE: a neutral second-insight line (per vertical, below), so the
    variable is NEVER empty. lemlist holds leads with missing variables, and an empty
    slot mid-email leaves a visible gap; the always-populated pattern is the same one the
    Stars campaigns use with `{{opener_line}}`.
- **Variables:** `{{firstName}}` (lemlist native; the strategy doc's `first_name`),
  custom `{{function}}`, `{{parent_account}}`, `{{enterprise_line}}`. `brand_safe`
  stays a Clay column that COMPUTES enterprise_line; it is not itself a template token.
  `{{parent_account}}` and `{{function}}` appear in the internal call-task note, and
  `{{function}}` in net-new copy.
- **Customer spine (per strategy sec 4):** Email 1 (D0) > LinkedIn visit (D1) > LinkedIn
  connect, blank note, manual approve (D0 after visit) > LinkedIn message (D2) > Email 2
  (D2) > call task, cleared names only (D2). Linear v1; the accepted-invite conditional
  refinement is a UI decision later (the API cannot build inside condition branches
  reliably, per the Aug 31 Stars lesson).
- **Net-new spine (per launch-kit skeleton):** Email 1 (D0) > LinkedIn connect (D1) >
  voicemail + LinkedIn message (D2 after) > Email 2 (D2) > breakup (D3).
- Brand-light throughout: Intradiem appears nowhere in any template, including
  signatures. Sign-off first name through day 5, full name on the day-9 breakup.
- Opt-out line on customer-lane Email 1s (house pattern from the live Stars template):
  these are sensitive accounts; the exit costs one word.

## Neutral enterprise_line values (brand_safe = FALSE)

- Healthcare payer: "The teams furthest along treat it as a scheduling fact, not a
  reporting gap, which changes who owns the fix."
- Financial services: "The interesting part is that the fix is operational, not another
  reporting layer, which changes the budget conversation."
- Insurance: "The teams getting ahead of it started by measuring the gap for two weeks,
  which made the case internal and concrete."
- BPO: "The operators moving first are using it in renewal conversations, because proving
  it beats promising it."

---

## Campaign 1: BO Expansion - Healthcare Payer (Nate)

Accounts: Elevance, Humana, Aetna, Cigna, Molina, UnitedHealthcare. Personas: VP/Dir
claims ops, appeals, UM, shared services. Lane: bo_claims.
One idea (E1): the backlog that regrows every Monday is a timing problem, not a staffing
problem; the capacity to clear it already exists inside the week's idle windows.

### Email 1 (D0). Subject: `the monday backlog`

Hi {{firstName}}, there's a pattern in claims and appeals operations that rarely makes it
into the staffing conversation: the backlog that gets cleared by Friday grows back by
Monday, while the week's schedules already hold enough idle minutes to absorb it. The two
just never meet, because nobody can see the windows while they're open.

Might be helpful to walk through where those windows usually sit and what it takes to act
on them without adding headcount.

Worth 15 min in the next few weeks?

If you'd rather not hear from me, one word and I'll stop.

Nathan

### LinkedIn visit (D1), then LinkedIn connect (blank note, manual approve)

Task title: LinkedIn connect for {{firstName}}, no note (approve before sending)

### LinkedIn message (D2). Manual approve.

{{firstName}}, sent you a note last week about the Monday regrow pattern in claims
queues. The short version: the capacity to hold service levels through the week usually
already exists inside the schedule, it just isn't pointed at the backlog while the
windows are open. If that matches what you're seeing, worth a quick conversation?

### Email 2 (D2 after). Subject: `yesterday's report`

Hi {{firstName}}, one more thought and then I'll leave it with you. Most claims
operations manage turnaround time off yesterday's report, which means the day's capacity
decisions get made after the day is already gone. The teams that hold TAT through surge
weeks aren't staffed heavier, they've shortened the distance between seeing a queue move
and doing something about it.

{{enterprise_line}}

If turnaround time or overtime is on your radar for this year, I'd like to compare notes
on where that gap costs the most. Have 15 minutes in the next couple weeks?

Nathan

### Call task (D2 after). CLEARED NAMES ONLY.

Task title: Call {{firstName}} ({{function}}, {{parent_account}}). ONLY if the AM has
cleared this name for a call (owner_cleared = TRUE). Reference the Monday-backlog email
thread; no pitch, offer the walk-through.

---

## Campaign 2: BO Expansion - Financial Services (Nate)

Accounts: Goldman, JPMorgan, US Bancorp, Wells Fargo, Synchrony. Personas: payment ops,
disputes, fraud review, doc processing, shared services. Lane: bo_shared.
One idea (E1): cost-per-transaction is reviewed monthly but decided in the minutes
between reports.

### Email 1 (D0). Subject: `between the reports`

Hi {{firstName}}, cost-per-transaction gets reviewed monthly, but it's decided in the
minutes between reports: the dispute queue that sat unworked from ten to eleven, the doc
review team idle while onboarding backed up two floors away. Dashboards made the loss
visible, but most operations still can't act on it until the daily huddle, and by then
the minutes are spent.

Might be helpful to walk through where those minutes usually hide in dispute and payment
operations.

Worth 15 min in the next few weeks?

If you'd rather not hear from me, one word and I'll stop.

Nathan

### LinkedIn visit (D1), then LinkedIn connect (blank note, manual approve)

Task title: LinkedIn connect for {{firstName}}, no note (approve before sending)

### LinkedIn message (D2). Manual approve.

{{firstName}}, I emailed last week about the minutes between reports, the ones that
quietly set cost-per-transaction. The pattern I keep seeing: idle capacity shows up in
end-of-day reporting, long after anyone could have redirected it. If proving utilization
to finance is part of your year, worth a quick conversation?

### Email 2 (D2 after). Subject: `found capacity`

Hi {{firstName}}, last note from me. When volume spikes, the ask is usually overtime or
headcount, and both get harder to defend every budget cycle. The found-capacity
conversation is different: it starts from the idle minutes already on payroll, sitting
between queues that can't rebalance themselves mid-day. Surfacing them isn't a reporting
problem, it's a timing problem, and it's the cheapest capacity an operation has.

{{enterprise_line}}

If utilization is something you have to prove to finance this year, I'd like to compare
notes on how that case gets made. Have 15 minutes in the next couple weeks?

Nathan

### Call task (D2 after). CLEARED NAMES ONLY.

Task title: Call {{firstName}} ({{function}}, {{parent_account}}). ONLY if the AM has
cleared this name for a call (owner_cleared = TRUE). Reference the found-capacity email
thread.

---

## Campaign 3: BO Expansion - Insurance (Nate)

Accounts: Prudential, MetLife. Personas: claims ops, policy admin, underwriting support.
Lane: bo_claims/bo_shared blend.
One idea (E1): the TAT clock runs all day, but capacity gets rebalanced once a day
against yesterday's numbers; aging inventory lives in that gap.

### Email 1 (D0). Subject: `the tat clock`

Hi {{firstName}}, the TAT clock on a claim runs around the clock, but the capacity to
keep it green usually gets rebalanced once a day, against yesterday's numbers. That gap
is where aging inventory comes from: not too few people, but hours of the day where the
right people sit idle in one queue while another one slips.

Might be helpful to walk through where that gap usually shows up across claims and
policy operations.

Worth 15 min in the next few weeks?

If you'd rather not hear from me, one word and I'll stop.

Nathan

### LinkedIn visit (D1), then LinkedIn connect (blank note, manual approve)

Task title: LinkedIn connect for {{firstName}}, no note (approve before sending)

### LinkedIn message (D2). Manual approve.

{{firstName}}, sent a note about aging inventory being a timing problem more than a
staffing one. The queues that slip usually slip at specific hours of the day, and those
same hours hold idle capacity somewhere else in the operation. If that rings true for
your world, worth a quick conversation?

### Email 2 (D2 after). Subject: `the overtime premium`

Hi {{firstName}}, one more from me. Surge weeks expose the pattern: overtime gets
approved after the backlog is visible, which means the operation pays a premium to fix
what it could have absorbed in the moment. The teams getting ahead of it aren't
forecasting better, they're shortening the distance between a queue moving and someone
acting on it, from a day to minutes.

{{enterprise_line}}

If overtime spend in claims or policy ops is a line you're watching this year, I'd like
to compare notes on where it concentrates. Have 15 minutes in the next couple weeks?

Nathan

### Call task (D2 after). CLEARED NAMES ONLY.

Task title: Call {{firstName}} ({{function}}, {{parent_account}}). ONLY if the AM has
cleared this name for a call (owner_cleared = TRUE). Reference the TAT-clock email
thread.

---

## Campaign 4: BO Expansion - BPO (Nate)

Accounts: Foundever, Capita. Personas: ops executives, account/delivery leaders, WFM and
capacity owners. Lane: bo_shared, margin-framed.
One idea (E1): in an outsourced operation idle minutes are the margin line, and most of
them are invisible in the daily numbers.

### Email 1 (D0). Subject: `the margin line`

Hi {{firstName}}, in an outsourced operation idle minutes aren't an efficiency stat,
they're the margin line, and most of them never show up in the daily numbers: short gaps
between volumes, early in shifts, in queues clients never see. Being able to prove
utilization hour by hour, and act on it in the moment rather than explain it a day later,
is becoming the difference at renewal time.

Might be helpful to walk through where those minutes typically sit in a multi-client
operation.

Worth 15 min in the next few weeks?

If you'd rather not hear from me, one word and I'll stop.

Nathan

### LinkedIn visit (D1), then LinkedIn connect (blank note, manual approve)

Task title: LinkedIn connect for {{firstName}}, no note (approve before sending)

### LinkedIn message (D2). Manual approve.

{{firstName}}, I emailed about idle minutes being the margin line in outsourced
operations. The part that stays invisible: capacity trapped between client queues that
can't flex mid-day, on payroll either way. If margin per seat is the number you live in,
worth a quick conversation?

### Email 2 (D2 after). Subject: `slas in real time, cost at month end`

Hi {{firstName}}, last one from me. Client SLAs get managed in real time; the cost side
usually doesn't. So the same operation that never misses a service level still gives
margin back through overtime, shrinkage, and idle time no report catches until month end.
Closing that gap doesn't take new headcount or a new WFM stack, it takes acting inside
the day instead of after it.

{{enterprise_line}}

If margin recovery is part of next year's renewal conversations, I'd like to compare
notes on where the biggest leaks usually are. Have 15 minutes in the next couple weeks?

Nathan

### Call task (D2 after). CLEARED NAMES ONLY.

Task title: Call {{firstName}} ({{function}}, {{parent_account}}). ONLY if the AM has
cleared this name for a call (owner_cleared = TRUE). Reference the margin-line email
thread.

---

## Campaign 5: BO Net-New - Back Office (Nate)

Accounts: Centene, Fidelity, National Grid, Truist, Paychex, Regions (Nate's six, net-new
prospects; separate campaign so council reporting stays new-logo-clean). Personas: back
office ops leaders across verticals; copy is vertical-neutral, personalized by
{{function}}.
One idea (E1): the same company runs its front office minute by minute and its back
office on yesterday's report; the gap between those two clocks is where cost hides.

### Email 1 (D0). Subject: `two clocks`

Hi {{firstName}}, there's a blind spot most back-office operations share: the contact
center gets managed minute by minute, while {{function}} runs on yesterday's report. Same
company, same pressure on cost, two different clocks. The gap shows up as idle windows
nobody can see while they're open, and overtime approved after the fact to clear work
that could have been absorbed in the moment.

Might be helpful to walk through how operations teams are starting to close that gap.

Worth 15 min in the next few weeks?

Nathan

### LinkedIn connect (D1). Blank note, manual approve.

Task title: LinkedIn connect for {{firstName}}, no note (approve before sending)

### Voicemail (D2 after). Under 25 seconds. CLEARED FOR CALL ONLY.

Hi {{firstName}}, Nathan Belfield. I sent you a note last week about the two-clocks
problem, the front office managed in real time while the back office runs on yesterday's
report. I'll try you again another time, but the email has the short version if that's
easier. Thanks.

### LinkedIn message (D0, same day as voicemail). Manual approve.

{{firstName}}, tried you by phone as well. The short version: the idle capacity your
front-office peers manage minute by minute exists in {{function}} too, it's just
invisible until the end-of-day report, when it's too late to use. If cost per transaction
or backlog aging is on your desk, worth a quick conversation?

### Email 2 (D2 after). Subject: `the headcount cutoff`

Hi {{firstName}}, following up once more because the timing side of this is what most
teams miss. Adding headcount to absorb backlog has a cutoff point where it becomes the
expensive option, and most operations are past it before anyone runs the math. The
alternative isn't working harder, it's acting on the capacity already inside the day: the
minutes between queues, the windows after volume drops, the idle time that never makes
the report.

If that's a conversation happening in your planning cycle, I'd like to compare notes on
how others are approaching it. Have 15 minutes in the next couple weeks?

Nathan

### Breakup (D3 after, lands ~day 9). Subject: `closing the loop`

Hi {{firstName}}, I'll close the loop here. The short version of everything I've sent:
back-office cost pressure usually gets treated as a staffing problem, and the operations
getting ahead of it are treating it as a timing problem instead. That reframe is worth a
conversation whenever it lines up with your planning cycle.

This is worth your time. I'm here whenever the timing works.

Nathan Belfield

---

## Verified-claims ledger

Every template scanned. Numbers cited: none. Customer outcomes cited: none. Peer claims
cited: none (soft "how others are approaching it" phrasings carry no outcome or figure).
Gate result: PASS with an empty ledger, by design (mechanism-only posture per the BOO
launch kit).

## Send-ready check (condensed)

All pieces: specific observation first, no greeting filler; one idea per message; one
question per CTA with a connector sentence and a named topic; prospect is the hero; no
forbidden words; no em dashes; no product tells (no "automation," "platform,"
"orchestration," "intraday" anywhere); Intradiem absent everywhere including signatures;
word counts in channel range (E1 85-110, LI 50-80, E2 120-150, voicemail ~55, breakup
~85); openings all different across the five campaigns; senior-contact time anchor ("next
few weeks" / "next couple weeks") throughout; first-name sign-off through day 5, full
name on the day-9 breakup only.
