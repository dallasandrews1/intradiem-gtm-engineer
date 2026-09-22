---
name: lemlist-sending-domains-sep22
description: lemlist external-domain connection requires full nameserver delegation to Scaleway; intradiem.ai is an active CloudFront redirect on Route 53, so it is the wrong domain to hand over
metadata:
  type: project
---

Sep 22 2026 lemlist workspace domains: intradiemhq.com (ACTIVE, 4 mailboxes,
added Aug 31, M365), intradiem.net (pending, 2 mailboxes, M365), intradiem.ai
(pending, 0 mailboxes, added Sep 22, Google).

Dallas bought the lemlist domains with approval from product leadership and
finance/security. IT was never involved, so the intradiem.ai ticket is the first
time IT sees any of the three.

lemlist's external-domain flow (help article 13916068) requires pointing
nameservers at ns0.dom.scw.cloud and ns1.dom.scw.cloud so lemlist owns the whole
DNS zone. There is no "IT keeps the zone and publishes records" option. The
`_scaleway-challenge` TXT is only step 1. The flow is Google Workspace only, so
an external domain gets a different mail provider than the M365 domains. Two
7-day clocks: TXT verification, then the NS switch, or lemlist drops the domain.

intradiem.ai is live infrastructure, not a parked domain: Route 53 nameservers
(awsdns), root and www A records at 18.161.156.x, CloudFront with an ACM cert
and a CloudFront Function serving a 301 to intradiem.com. No MX and no TXT at
all today. Delegating to lemlist breaks the redirect unless every record is
mirrored first, and the ACM validation CNAME has to be mirrored too or the cert
fails renewal later.

**Why:** The ask as originally written ("transfer hosting, all you need is one
TXT record") is wrong on both halves and would break a working brand redirect.

**How to apply:** Prefer a fresh non-brand domain bought inside lemlist, which
needs no IT ticket and reuses the approval path that already worked. If
intradiem.ai is still wanted, the ticket asks for an NS delegation, discloses
the other two domains up front, and names the redirect as the thing to preserve.
Related: [[lemlist-open-tracking-domain-pending-it]].
