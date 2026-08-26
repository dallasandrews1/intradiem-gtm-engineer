# Enrichment Doctrine (Aug 6 2026)

Standing rule for every lemlist wave load, every motion, both reps. Written the day lemlist enrichment put a real deliverable address at a Nevada college onto a Citizens VP's lead row.

## The rule

**Clay enriches. lemlist executes. The two are never confused.**

lemlist is the send engine and the task queue. It is not the data source. Every contact entering a lemlist campaign gets its email and phone from Clay, at load time, attended, before the lead is loaded or immediately after.

Canonical routine: `Enrich Person and Find Contact Details`, `function:t_0thx4ojyQd6uNhDf44G`. Input is the LinkedIn URL. Returns `Work Email` and `Mobile Phone`. 12.8 credits per contact.

```
clay routines runs start function:t_0thx4ojyQd6uNhDf44G --input <file>
```
where the file is `{"items":[{"id":"<slug>","inputs":{"Social Profile URL":"<linkedin url>"}}]}`.

Poll with `clay routines runs get <runId>` until status is `complete`, then write results onto the lemlist leads with `update_lead`.

## Why, in one paragraph

This is not vendor preference. On a sample of eight Citizens contacts, lemlist returned one hard error: it resolved Patrick Savage to `patrick.savage@csn.edu`, a different person at an unrelated organization. That address is deliverable. It would never have bounced, never appeared in a bounce report, and never been noticed. Clay resolved the correct `@citizensbank.com` address for the same person. Clay also returned `stacy.stanton@thehartford.com` and `tayton.guio@thehartford.com` for two contacts whose surnames had changed, which any firstname.lastname pattern guess gets wrong. Clay is reading directory entries; the cheaper path is guessing patterns and occasionally matching the wrong human.

## The three checks that are not optional

**1. Count populated fields after every run. Never trust the response shape.**
lemlist's enrichment failure is SILENT. An out-of-funds batch returns empty email and phone fields with a success response, which is indistinguishable from "these people have no data on file." The failure was only found by an explicit retry that returned `MISSING_FUNDS`. After any enrichment run, count how many rows actually came back populated. A uniform zero is a funding or provider failure, not a fact about the contacts.

**2. Compare the resolved email domain against the account's domain.**
This is the check that catches the Savage class of defect, and the only one that does. Bounce monitoring cannot see it. If the domains differ, stop and resolve it by hand. Legitimate exceptions exist (`citizensbank.com` for "Citizens Financial Group") but they get stated, not assumed.

**3. Preview a real loaded lead per email step before the wave goes.**
An unmapped variable renders as a literal `{{opener_line}}`. There is no other point in the pipeline where that gets caught.

## Where sources disagree

Emails: when two independent sources return the same address character-for-character, treat it as verified. On the Aug 6 Citizens set, 5 of 6 matched exactly between lemlist and Clay.

Phones: they will not agree, and neither is authoritative. On the same 6 contacts, 3 returned different numbers. Clay's field is explicitly "Mobile Phone"; lemlist's is often a desk or switchboard line. Load Clay's as primary and **record the alternate as a fallback rather than discarding it**, so a missed dial has a second number to try. Do not silently overwrite a working number with an unverified different one.

## What is NOT automated, and why

There is deliberately no unattended enrichment agent. Enrichment happens once per wave, at load, with a human present. Three reasons:

1. The dangerous defect is a wrong-but-deliverable address. Automation would write it onto the lead with nobody looking at the domain, which is precisely how it reaches a prospect.
2. Enrichment is not a recurring event. A scheduled job would wake up with nothing to do almost every run.
3. It spends credits. The standing rule is to estimate before any run, per `clay-credit-steward`.

The recurring, unattended job that DOES exist is the `lemlist-lead-integrity` agent: read-only, spends nothing, sweeps loaded campaigns for wrong-domain emails, misrouted leads, unrendered variables, silently-failed enrichment batches, and leftover TEST rows. It finds; a human fixes. That split is the point.

## Ledger

Every enrichment run gets a line in `Clay_Credit_Ledger.md` with the run id, item count, and estimated credits. The Aug 6 Citizens and Hartford entry is the reference format.
