# MessageGen Deployment Sheet (v2.2 prompt to the live GTM Engine workbook)
**Status:** GATED. The AI column does not get built until the Value Repository is connected. This sheet makes the build a 15-minute paste-in on that day. The canonical prompt is Clay_MessageGen_SystemPrompt_v2.md (v2.2, patched Jul 9 with the natural-CTA banned-words standard; base rules verified Jul 1); nothing here changes it.

## Live wiring map (v2.2 token to the actual workbook, as built Jul 7)
| Prompt token | Live source | Note |
|---|---|---|
| first_name, job_title, company | Contacts (Buying Committee): First Name, Job Title, Company | direct |
| seniority_tier | Contacts: Seniority Tier | direct |
| cs_star, clin_star, gross/addressable_forgone_qbp_musd | Accounts (Master), after the 98-row import | lookup by contract; interim fallback = CMS Star Ratings Import |
| addr_2028_musd, addr_2029plus_musd | Accounts (Master) | Persona 2 lead dollar; present in the 98-row pack |
| members_sub4 | Accounts (Master): members | rename on lookup |
| cliff_edge_contracts | Accounts (Master): contract_id | max two, prefer largest |
| why_now | DO NOT wire from the current Contacts "Why Now" column until the 2026-cycle refresh (greenlight-pack CSV) is applied; the live text still carries 2025-cycle numbers | hard rule |
| earnings_angle_line | StarRatings_Earnings_Signals_2026.csv lookup by parent | blank for unswept long-tail |
| product_angle | **Value Repository VERIFIED-tier rows ONLY. Leave unmapped until connected.** | see collision below |
| source_motion | Contacts: Source Motion | prompt errors if not star_ratings family |

## The collision to not walk into
The live Contacts column named "Product Angle" holds product ROUTING values (Queue Optimizer, Back Office Optimizer). The prompt token `product_angle` means "an approved Intradiem claim from the Value Repository." These are different things with the same name. If the column is mapped to the token, the prompt will treat routing labels as approved claims. On build day: map the prompt token to a NEW column fed only from Verified Metrics / Claims rows tiered VERIFIED; the existing "Product Angle" column stays routing-only (optionally rename it product_routing during wiring).

## Guardrail tier wiring (the workbook enforces what the prompt assumes)
- VERIFIED tier rows: the only permissible source for product_angle content.
- DRY-RUN tier: never enters MessageGen input; those numbers exist to demo the instrument, not to reach prospects.
- DO-NOT-SEND tier: the idle-time stat, peer outcomes, and unverified ROI never map to any token. The prompt's own NUMBER DISCIPLINE block is the second lock; this mapping is the first.
- Generated drafts land upstream of the existing L5 gate untouched: critic_email_valid and human_approved still decide send_ready. MessageGen never bypasses the HOLD column.

## Build-day checklist (in order, ~15 min)
1. Confirm Value Repository connected and Verified Metrics / Claims reflects it.
2. Apply Contacts_QBP_2026Cycle_Refresh.csv so Why Now is current-cycle.
3. Add persona_key column if routing logs are wanted (stars_quality / medicare_finance); keep Product Angle clean.
4. Create the AI column on Contacts; paste the v2.2 system prompt verbatim; map tokens per the table above.
5. Run on 3 rows only (one Persona 1, one Persona 2, one empty-token edge case). Check against the two worked examples in the v2 doc.
6. Read all 3 as the prospect (Gate 4). Only then enable for the table, still behind human_approved.
7. Ledger entry: AI column runs consume credits; estimate rows x 1-2 credits and log before the full run.
