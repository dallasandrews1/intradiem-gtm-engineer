# Back Office Optimizer Messaging Framework (Marketing, Cheryl Eckel, Jun 26 2026)

Source: `Back-Office-Optimizer_Messaging-Framework.docx`, Cheryl Eckel's OneDrive, last modified Jun 26 2026. Transcribed Sep 3 2026 for the messaging engine. This is marketing's own language and outranks anything the engine invented. The proof-point section is explicitly unpopulated: the only figure is an illustrative model, not a customer result.

## Value proposition
Know if your back office can keep up, before you miss an SLA.

## ICP
Primary buyer is a COO, VP of Operations, or Head of Back-Office Operations at a regulated mid-to-large enterprise (financial services, insurance, healthcare, utilities, government) running 500 to 5,000+ back-office agents. Accountable for SLA compliance, headcount cost, and regulatory risk. Limited-to-no visibility into intraday back-office productivity, or relying on lagging backlog-aging data, so they cannot act before SLAs are missed or headcount is added just to keep up. They own the commercial decision and need a CFO-ready ROI story anchored to reduced penalty exposure and unlocked capacity.

## Personas

**1. The WFM Champion (WFM / Resource Planning Manager).** Technical evaluator and day-to-day champion. Spends an estimated 30 percent of the day manually re-skilling queues, no real-time intraday visibility, a WFM platform blind to back-office case demand. Skill mismatches discovered only after breaches. Evaluated on intraday re-skilling decisions, analyst time on tactical tasks, skill coverage gaps detected. Wants a tool that does the hard intraday work and earns credit for preventing breaches rather than explaining them.

**2. The Economic Buyer (COO / VP Operations).** Budget owner. Board-level exposure: SLA misses reaching regulators, overstaffing eroding margin, no confidence the operation holds under peak. Measured on SLA attainment rate, penalty exposure in dollars, overstaffing buffer percent, overtime cost. Closes on board-level confidence in operational resilience and ROI in dollars avoided.

**3. The Technical Buyer (IT / CTO).** Gatekeeper. Concerns: platform sprawl, integration complexity, security, data residency. Has heard "seamless integration" before. Evaluated on integration effort in days, data residency compliance, SOC 2 / ISO 27001. Needs minimal integration footprint, confirmation no PII is stored, standard API connectors, not a platform migration.

**4. The End User (Head of Operations / Ops Director).** Operational champion who feels the daily pain. Managers firefighting, cherry-picking endemic, escalations reaching senior leadership. Measured on breach rate, escalations per week, agent utilization, queue backlog age. Motivated by calmer operations, a proactive team, and a story about how they fixed it. Get Next Work Item removes cognitive load from agents and managers.

## Elevator pitch
Back-office operations lose money on SLA breaches and overstaffing when managers lack real-time visibility into team capacity against fluctuating workload demand. Back Office Optimizer gives operations leaders the supply-and-demand intelligence to drive efficiency, automatically routing the right work to the right resource so teams hit SLA targets consistently and proactively, without the cost of excess headcount.

## Long description
Unlike live inbound operations, which have ACDs and real-time infrastructure built in, back offices have historically had no way to see whether their current staff can handle the volume of work piling up across their queues. Managers discover SLA breaches after the fact, overstaff as a safety net, and watch workers cherry-pick the cases they'd rather handle.

Back Office Optimizer solves both sides. Managers get granular, real-time visibility into supply (accounting for planned and unplanned shrinkage most back-office tools ignore) and demand, across every queue and process. "What if" scenario modeling tests staffing configurations before committing. On the worker side, it surfaces the next best item for each agent based on SLA priority and skill match, eliminating cherry-picking. For organizations without a workload distribution system it takes that role entirely; for those that have one, it integrates.

Result: regulated enterprises hit SLA targets without overstaffing and unlock fixed capacity that can be redeployed to revenue-generating work.

## Tone of voice
Confident. Direct. Credible. Commercially sharp.

Before: "Our solution helps teams manage their back-office workloads more efficiently and can improve SLA outcomes over time."

After: "Back Office Optimizer shows you exactly how much work is piling up, whether your staff can handle it, and which case each worker should tackle next, before you miss an SLA or pay a penalty."

## Outcomes
- Hit SLA targets consistently across all back-office processes without overstaffing as a safety net
- Reduce regulatory penalty payments by catching capacity-demand imbalances before they become breaches
- Reduce worker cherry-picking; every agent works the highest-priority item they're qualified for, automatically
- Free WFM analysts from manual triage; reclaim 25 to 30 percent of analyst capacity for strategic work
- Model "what if" staffing scenarios before committing, including shrinkage factors most tools ignore
- Identify pockets of excess capacity and redeploy fixed-cost headcount to revenue-generating work
- Move from reactive firefighting to proactive, board-reportable SLA governance
- Provide regulators and auditors with a digital audit trail of every proactive intervention

## Customer requirements by persona
- COO / VP Ops: proof the operation won't fail under board or regulatory scrutiny; ROI in dollars avoided; SLA confidence at peak without buffer overstaffing.
- WFM / Resource Planning Manager: real-time intraday visibility into case demand vs staff availability; automated skill-based allocation; integrates alongside existing WFM (NICE, Verint, Calabrio) without replacing it.
- Head of Operations / Ops Director: proactive intraday allocation control that ends cherry-picking and firefighting; fewer escalations and less burnout; Get Next removes cognitive load.
- IT / CTO: standard API connectors, metadata only, no PII stored; minimal footprint, an API layer approval not a platform migration; SOC 2 / ISO 27001; data residency met.

## Pain points (marketing's wording, condensed)
1. No real-time view of supply and demand, so breaches are discovered too late. Reporting lags 24 to 48 hours; the organization lives in permanent firefighting mode.
2. Work prioritization left to individual preference. Homegrown "next item" tools have the same blind spot.
3. Forecasting built for front-office intervals, not back-office complexity (shrinkage through the day, interval-level modeling, handle time via a digital twin).
4. Overstaffing as the only safety net.
5. Trapped capacity that can't be redeployed (fixed full-time supply).

## How it works
1. Queue and SLA configuration. 2. Supply ingestion with shrinkage from WFM platforms, net staffing line continuously updated. 3. "What if" scenario modeling at FTE level. 4. Real-time supply vs demand monitoring across every queue. 5. Next best work item delivery per worker, enforced by operations leadership. 6. Automated re-skilling (roadmap), reassigning human and AI workers to queues.

## Feature details
Supply and demand visibility engine; "what if" scenario modeling; WFM Lite for teams with no back-office scheduling or forecasting; next best work item engine; Skill Tagging API and re-skilling (roadmap).

## Proof points (status as written)
- Illustrative model, not an actual customer result: a typical 2,000-agent deployment with $1M/year in SLA penalties: $250K penalty reduction + $262K overstaffing saving + $236K analyst capacity freed = ~$748K annual benefit, payback under 6 months.
- Named customer case studies: to be populated from the Beta program (target one FS, one insurance or healthcare, one government).

## Beta program (from the BOO Sales Enablement deck, Jul 7 2026 draft)
90 days free access. Plus 50 percent discount on Year 1 of a multi-year deal, or plus 10 percent on a single year, Early Adopter rate locked for the Beta window. Eligibility: existing customers or new logos on Harmoniq, case-based back-office workflows with measurable goals, complex skill mix preferred, no existing WFM required (WFM Light included). Participants provide an executive sponsor, one or two lighthouse workflows, monthly value reviews, and a reference or case study. Signed letter of intent required. Goal: three beta customers for soft launch, six lighthouse enterprise wins post-launch. Pricing: value-aligned (workflows, case volume, workforce complexity, not seats). Target ACV $250K to $750K mid-market, $750K to $2M+ enterprise; confirm ranges with Sales leadership before quoting.
