# Exec decisions, FS wave 1 and open loops (Aug 3 2026)

Dallas delegated these calls ("make all the exec decisions you would make if you were me"). Each is decided, applied to the assets, and reversible. Anything Dallas wants flipped, flip the tag in `UK_FS_Committee_Contacts_v1.csv` and tell the engine.

## Roster (applied to the CSV as `wave_status`)

1. **Wave 1 = 62 contacts**: UK-resident, operational seats, all 12 firms. Quality over quantity holds; nobody embarrassing is in the send list.
2. **Group ExCo held out of the volume campaign** (Barclays Craig Bright + Mark Ashton-Rigby, HSBC Suzy White): tagged WAVE2-EXCO-STRIKE. A Group COO earns a bespoke strike sequence like BMO/TELUS got, not step 14 of a 22-step tree. Nothing sends to them until that's built.
3. **EU/Ireland contacts held from wave 1** (Mulligan/Monzo, Edward M./Revolut, Erixon/Aviva, Condon/Barclays): tagged WAVE2-EU-HOLD. Wave 1 is UK-resident; the FOS wedge is UK-jurisdiction and the sends read cleanest that way. Their EU-preview copy is already written and keeps.
4. **Four division-ambiguous contacts go verify-first** (HSBC Sault, Britain, Khan; Barclays Feindel): tagged VERIFY-DIVISION-FIRST. Jack confirms consumer-side on LinkedIn in about five minutes; CIB or marketing means flip to OUT. Better to lose four sends than have one CIB exec forward a complaints email around.
5. **Kept in wave 1, decided**: the financial-crime/economic-crime COOs (fraud casework is a top FOS driver, the angle is genuinely theirs), James Oakes (CFO seat, finance-first copy already written, the fee is his cost base), Jamel Oulidi (Coutts is consumer banking), Kirsty-Marie Turner (IC-level, but complaints practitioners reply and forward; cheap to include).

## Sequencing and money

6. **Lloyds stays out of wave 1.** Jack's priority is acknowledged, but their complaints fell 20.1% and the rising-number wedge would misfire. Lloyds gets touched only after its own falling-number angle is written.
7. **Enrichment pre-approved**: wave-1 roster, ~62 x ~4.7 = roughly 290 credits against ~72.8K live balance. Executes the moment Jack's DNC-scope confirm lands, not before. No spend today.
8. **Schedule gate verified closed**: both Jack campaigns already run Europe/London, 09:00-18:00, Mon-Fri, 20-minute spacing (answers Matt's timezone point). Remaining settings are two UI toggles per campaign on load day: click tracking OFF, reply-stops at lead AND company level. They don't block anything earlier.
9. **Nate first-email A/B stands** as mounted. Winner judged on replies plus note-requests, read directionally, not statistically, given wave sizes.
10. **Offer-note SLA decided**: a "yes, send it over" gets the matching note from `Offer_Notes_Aug3.md` the same day; reply engine drafts, the sender sends.
11. **Airlines Start stays late August. Netherlands stays queued** behind the Rabo ranking conversation and its own natively written copy.

## Background work queued (agent-buildable, not blocking wave 1)

12. Domain re-pull for Admiral, Direct Line, Zopa, Revolut (thin committees from domain failures), zero-credit Clay native search, then fs-v1.0 variables for the new contacts.
13. Named-firm FOS pass on Jack's rep-priority accounts not in the universe (Ageas, Saga, LV=, L&G, D&G, Esure), admitted as a rep-priority tier regardless of rank.

## The launch chain as it now stands

**Amended later Aug 3, two changes:**
- **Standing rule from Dallas: whatever Jack or Nate sends is the final full version.** The Aug 3 customer list IS the complete DNC scope; the confirm ask is dead and enrichment is unblocked now. (Fuzzy Clay titles still get the division check; that's our data being ambiguous, not Jack's.)
- **Per today's Jack DMs: fs-v1.0 copy is the engine's draft entering the working session, not final.** Jack leads with his own messaging (old Lemlist campaigns + context folder incoming); the engine iterates off the back of it. Roster, cuts, and enrichment are copy-independent and proceed regardless.

1. Engine: enrich wave 1 (pre-approved, now unblocked) → load 62 → real-row exclusion check → delete the two TEST leads → two UI toggles per campaign.
2. **Jack**: four division checks (message drafted, Dallas sends); copy session (his messaging leads); connected channels/seat when the money lands.
3. **Dallas**: explicit Start. Unchanged, last, his alone.
