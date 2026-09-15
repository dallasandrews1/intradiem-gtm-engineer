---
name: sixsense-kw-segments-absent-sep15
description: "Sep 15 2026 Clay read: no '6s - KW -' keyword segments exist on any company; 6sense syncs only funnel-stage, G2 and 'Back Office Intent - FS & HC' (107 companies, Clay audience audseg_0tlesobkMWeuqsmbwZX); Sierra's Sep 11 email shared keyword groups (xlsx), not segments; trigger families stay staged, scorer untouched"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1cc96141-e5aa-4bc9-8ae4-2f2c4b818224
  modified: 2026-09-15T14:32:36.884Z
---

**Verified Sep 15 2026 (0 credits, Clay Audiences companies, field "6sense Segments (2)" audf_0tkdvbt5xi8uZgVuErt):** filter Contain "6s - KW" returns 0 companies. Values that do sync: "6s - Top of Funnel", "6s - Middle of Funnel", "6s - Bottom of Funnel", "G2 - TOF/BOF", "Back Office Intent - FS & HC" (107 companies), "TAM UK", "3. Multiple Unique Website Visitors", "Assigned-CAM-OR-Partner-PrePipeline-Accts". Two Clay company audiences already exist for the 6sense side: `audseg_0tlesobkMWeuqsmbwZX` "6sense: Back Office Intent - FS & HC" and `audseg_0tlesof2jkhrEDkeiez` "6sense: G2 research".

Sierra's Sep 11 email "Back Office Keyword Tracking" (to Naveen, Dallas, Carter) shared `intradiem_keyword-groups_6sense_2026-09-11.xlsx` on the Marketing SharePoint and asked for sources to expand the groups. The Sep 11 ads touch base (Otter CaWR8S5LmfcXl7oXhmq0El7q4VM) never mentioned 6sense segments; only Sierra's aside that 6sense audience workflows might route to LinkedIn ads.

**Decision:** per Dallas's Sep 15 rule (segments absent means draft and hold), `staged/sixsense_families.json` stays unmerged, `heat_list_scorer.py` and `heat_loop.json` untouched, `live_stamp` and `live_lane_a` untouched. Slack draft to Sierra in `motions/back_office_expansion/BO_Drafts_Sep15.md`, not sent.

**How to apply:** the "Back Office Intent - FS & HC" segment is the one real 6sense back-office signal today; if Sierra builds no per-keyword segments, the design can run on it as a single `sixsense_kw_backoffice` family with the segment id above. Re-run the Contain "6s - KW" read before merging anything. Related: [[signal-marketing-loop-strategy-aug25]], [[gtm-cadence-sep8-next-steps]], [[bo-copy-c-autopilot-sep15]].
