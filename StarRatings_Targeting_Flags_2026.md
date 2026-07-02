# Star Ratings targeting flags (verified Jul 1 2026)

Suppression and routing rules that ride on top of the canonical universe. Apply these before sourcing or sending.

## 1. Molina MAPD exit (qualify, do not blanket-drop)
Molina is exiting MAPD / Part D in plan year 2027 (~$1B premiums) to focus on its dual-eligible book, which it keeps. Verified: Fierce Healthcare, Becker's, Molina Q4 2025 release.
- Action: suppress Molina straight-MAPD contracts (no point pitching a book being wound down), but KEEP Molina dual-eligible / MMP contracts (My Choice Wisconsin, Senior Whole Health-type). Confirm each Molina contract's product line before it enters a sequence.
- Molina contracts in the universe to check: H5649 (Central Health Medicare Plan), H3528 (ConnectiCare), H3038 (Molina Healthcare of California), H5209 (My Choice Wisconsin). H2224 (Senior Whole Health) already graduated to 4.0+.
- This is wired into the signal engine: `qbp_earnings_pressure` suppresses for contracts flagged for divestiture/line-exit, so the earnings signal won't fire Molina MAPD into outreach.

## 2. Cigna to HCSC / HealthSpring (routing only, targeting intact)
Cigna sold its Medicare business to HCSC, closed March 19 2025; the plans rebrand HealthSpring for 2026. Verified: PRNewswire, Healthcare Dive, HealthSpring.com.
- The Cigna-branded contracts in the universe are correctly parented to Health Care Service Corporation. Targeting is unaffected.
- Routing change: for the earnings/intent signal, these contracts route to HCSC rules (non-public: press, AM Best, rate filings, integration commentary), NOT Cigna Group earnings calls. Cigna Group calls no longer cover these plans.
- Marketing name may still read "Cigna HealthCare" in the CMS file; expect HealthSpring branding on 2026 member-facing plans.

## 3. Standing CS-addressability proof point (verified, third-party)
UnitedHealthcare told a federal court that a single disputed call-center secret-shopper call (CMS Call Center Monitoring measure) cost it $190M in Star bonus payments; a Texas federal judge ordered CMS to recalculate. Verified: Becker's, Healthcare Finance News, Healthcare Dive.
- Use as a standing proof line in messaging (especially to finance): one CS measure event, $190M, from the largest MA payer, in UHC's own words. It externally validates the entire addressability thesis.
- Not an Intradiem claim, so no approval-tier limit; cite as UHC's stated figure.
- TIME-STAMP REQUIRED (CY2027 final rule): the specific Call Center measure behind the $190M is retired for 2028 Stars. Cite it only as historical proof that a customer-service measure priced real money "under the prior rules." Never imply moving that measure still earns bonus. The live money now sits in Complaints, Appeals, Customer Service, and the CAHPS experience core.

## 4. Long-tail earnings sweep (batch 2, done Jul 1 2026)
Results folded into `StarRatings_Earnings_Signals_2026.csv`.
- FIRES on `qbp_earnings_pressure`: Medica (H8889; reimbursement strain + UCare book absorption = migration-driven CS risk), HMSA (H3832; self-disclosed Medicare operating losses corroborated by audited state filing).
- FIRES on the new `quality_identity_gap` wedge (routes cx): VNS Health (H5549, CS 3.0, 80% addressable, state 5-star brand), Imperial (H5496, CS 2.8, 100% addressable, US News award; media contact is their VP Member Experience = direct cx entry).
- Devoted: growth-strain, not distress ($366M raised, 71% growth). Handle as a whole-parent play, see section 6.
- Hold at zero pending fresher evidence: Cambia and PacificSource (Oregon MA-exit context is Oct 2024, stale >12mo). Natural re-check = their 2026 rate filings land with state DOIs over summer 2026.
- Zing (H4624): sweep empty; stands on QBP math alone. Optional follow-up = state DOI filing pull.

## 5. Two parents exit the motion
- Horizon Mutual Holdings: zero sub-4.0 contracts in the 2026 universe (H0885, H8298 both graduated). Confirmed absent from the canonical file. Remove from any Star Ratings list.
- BCBS Alabama: H0104 is CS 4.6 / Clin 2.8 = 0.00 addressable (gap entirely clinical). H1347 also BCBS AL. Both already in the non-fit bucket; not a fit for the CS motion regardless of financial signal.

## 6. Devoted Health = whole-parent strike-plan candidate
12 Devoted contracts in the universe (Fable's batch-1 said 5, undercount), ~$37M combined addressable, several at 100% CS-addressable (H2923, H8173, H6545, H7199). Devoted's entire brand is the service experience (the personal guide), which its sub-4.0 CS scores directly contradict. Best long-tail whole-parent fit for the CS motion; warrants an account-level strike plan, not sequence-only treatment.

## 7. New signal wired: quality_identity_gap
Added to `tam-outbound-engine/config/triggers.json` (weight 15, routes cx/cc_ops, 21/21 tests still pass). Fires when an account publicly markets on quality/service (state rating, US News award, brand-as-experience) while its CMS CS Star sits below 4.0. Per-account input = the public quality claim from the earnings/intel sweep. First fits: VNS, Imperial, Devoted.
