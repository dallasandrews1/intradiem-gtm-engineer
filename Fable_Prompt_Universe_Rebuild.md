# Fable greenlight: rebuild the Star Ratings universe on the current cycle

Paste into the same Fable thread. This supersedes the earlier QBP rerun; the rebuild IS the QBP recompute on fresh data.

---

Go. Confirmed on my side: my seed was the Oct-2024 vintage (2025 ratings), the 2026 ratings released Oct 9 2025 govern PY2027, and H5216 remaining sub-4.0 checks out against Humana's own disclosure. Build the real current list, not a patch of my 93. Requirements:

**1. Scope: the full current sub-4.0 universe, not a re-rating of my list.**
Pull every MA contract with a 2026 overall rating below 4.0 that is QBP-eligible. Exclude PDPs (S-contracts) and 1876 Cost plans. Flag, do not silently include, contracts that are "too new" or "not enough data" (they fall under separate new-plan QBP rules). Replace my graduated contracts with the contracts that newly fell below 4.0 in this release; treat those as high-priority since their Stars pain is fresh.

**2. Rebuild CS/Clin from the 2026 measure-level file, not the old profile.**
Classify each 2026 Star measure as CS (CAHPS, complaints, call-center/CTM, appeals, access, admin) or Clin (HEDIS, outcomes, adherence). Recompute each contract's CS and Clin composite from its current per-measure stars. Account for the 2026 CAHPS weight change. Then apply my addressability formula unchanged:
```
CS_gap = max(0, 4.0 - CS_star); Clin_gap = max(0, 4.0 - Clin_star)
addressable_pct = CS_gap / (CS_gap + Clin_gap) if (CS_gap+Clin_gap) > 0 else 0
addressable_forgone_qbp_musd = gross_forgone_qbp_musd * addressable_pct
```

**3. Return four things:**

a. The target list as a CSV code block, columns EXACTLY:
`contract_id,parent_org,marketing_name,members,overall_star_2026,cs_star,clin_star,gross_forgone_qbp_musd,addressable_forgone_qbp_musd,addressable_pct,confidence,primary_sources`
Ranked by addressable_forgone_qbp_musd, descending. Round dollars to one decimal, pct to two.

b. The CS/Clin measure-classification rubric as its own table: every 2026 Star measure name, its weight, and whether you tagged it CS or Clin. This is the auditable core of the addressability claim, so it has to be explicit, not implied.

c. A short changelog: which of my 93 graduated to 4.0+ (dropped), which are terminated/consolidated (not in file), and roughly how many contracts newly qualified.

d. The exact CMS source files you used (the 2026 Star Ratings measure data file and the enrollment file, with month), so I can reproduce and re-pull this each October release as the ingest step, rather than hand-maintaining a list.

**4. Enrollment:** use the current CMS Monthly Enrollment by Contract (name the month). Do not reuse my rounded figures where the real file has exact counts.

Keep confidence tags honest: high only where overall rating, per-measure stars, and enrollment are all verified from the CMS files.
