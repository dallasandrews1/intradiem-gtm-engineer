---
name: work-email-by-url-beats-workflow-sep4
description: Sep 4 2026 measured, the managed Work Email routine fed a LinkedIn URL (function:t_0thx4ovuPGp8sjH2hPP) found 110 of 125 at 1.07-1.42 credits a row, versus 1.6-3.0 a row and lower hit rates for the name-and-domain workflow wf_0tk4jo5z7RjGKo3rvR8; banks still go to Apollo
metadata:
  type: project
---
On the 162 wave-1 rows the two stuck runs never returned: Work Email routine with Social Profile URL + Full Name + Company Domain + Company Name = 110 found of 125 (88%), 139.4 credits, 1.27 per address. The workflow on the 17 rows with no URL = 14 valid at 0.98/row; the same workflow on a 15-row mixed test earlier that day billed 3.04/row because no-find rows bill every provider. Apollo people match on 20 bank-domain rows = 10 verified current for 17 Apollo credits. Enrich Person by email on 64 ZeroBounce-valid addresses with no URL = 40 profiles for 20 credits, 5 of them movers.

**Why:** the URL pins the person, so the cascade stops at the first provider; name-and-domain runs pay for every miss.

**How to apply:** order for any email backlog: free bridge for the URL, then Work Email routine by URL, then the workflow only for rows with no URL, banks to Apollo. The routine returns an address without a ZeroBounce status; loaded as routine_found. See [[enrichment-backlog-sep4]] and [[dwo-shell-load-plan-sep4]].
