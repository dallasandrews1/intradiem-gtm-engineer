---
name: intradiemai-domain-route53-not-registrar-sep22
description: "intradiem.ai DNS lives on AWS Route 53, not the registrar (Network Solutions/Key-Systems); Dallas is moving it to lemlist for deliverability protection"
metadata: 
  node_type: memory
  type: project
  originSessionId: 40043602-0e20-4f25-9020-78b5cba6ebca
  modified: 2026-09-23T12:27:56.889Z
---

Dallas messaged the coordinator 2026-09-22 wanting to transfer intradiem.ai domain hosting to lemlist (the sales sequencer) to protect the main domain's deliverability score, using alternate domains for cold outreach. He was given a TXT record to add (`_scaleway-challenge`, value `4887cb0a-5180-40ab-a677-f4b6b96a5e89`) "at the current registrar."

Checked via whois/dig 2026-09-22: registrar of record is Network Solutions (via Key-Systems GmbH), but the actual DNS is delegated to AWS Route 53 (ns-*.awsdns-* nameservers). No TXT records existed on the apex at check time.

**Why:** the registrar's own DNS panel is a dead end here — the nameservers point to Route 53, so any record has to be added in the Route 53 hosted zone for intradiem.ai instead. This is exactly the kind of mistake that would silently fail a domain verification step.

**How to apply:** any future intradiem.ai DNS/domain-verification task (lemlist alt-domains, SPF/DKIM, subdomain delegation, etc.) goes through AWS Route 53, not Network Solutions. No AWS access exists from this coordinator session — confirm with Dallas whether he holds Route 53 console access himself or whether it routes through IT/DevOps before assuming either path. See [[feedback-admin-request-notes-terse]] if it turns into an IT ticket.
