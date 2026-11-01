# Chapter 12: Goal Displacement; Goodhart's Law

> What this chapter covers: how a metric quietly displaces the goal it stands for; three activating criteria, the on-the-ground pattern in four domains, eight weak signals, and four lines of defense for whoever sets a metric.
> When to return: when you are about to set a new KPI, when a beautifully polished metrics report lands on your desk, or when you notice that something "looks great in the numbers but feels wrong."
> Reading time: 50 minutes.

## 1 What It Is

Definition: every metric is a proxy for a goal. The real goals — safety, health, learning, trust, the true condition of assets — mostly cannot be measured directly, so the organization measures some measurable quantity in their place. Goal displacement is what happens once the proxy becomes the center of management gravity: the organization begins to optimize the proxy itself, and the optimizing actions no longer improve the thing the proxy stands for. Goodhart's law, in its familiar formulation: when a measure becomes a target, it ceases to be a good measure (Charles Goodhart raised the point in 1975; the familiar wording is Marilyn Strathern's, 1997 — Goodhart proposed it in 1975 reserve-bank lectures; the popular phrasing comes from Strathern, 'Improving ratings', European Review 5(3): 305–321, 1997; the Crossref record has been verified). Getting the causal arrow right is what matters here: the metric has not gone bad — the organization's behavior has changed.

Three activating criteria (the mechanism has started if any one of them appears):

1. The measured quantity begins to attract dedicated optimization work, and the cost of that work goes into the number rather than into the thing itself;
2. The optimizing actions do not improve the goal being represented — they leave it flat, or they consume it;
3. Someone pays a price, in evaluations or in meetings, for pointing any of this out.

The essence of the mechanism is the proxy gap. The distance between a measurement and its goal is a permanent seam: loan-loss provisions are a proxy for asset quality, risk ratings are a proxy for risk, replica lag is a proxy for database health, failure records are a proxy for equipment condition. The seam is narrowest when the metric is new; from there, two kinds of action widen it — the unintentional (definition drift, sample aging) and the intentional (making the number look good instead of making the thing good). On paper, the two kinds cannot be told apart. This is also the boundary with the fifth step on the escalation ladder of Chapter 8: widening during ordinary times is gradual and looks reasonable; the crisis-time change of yardsticks is abrupt and has meetings on the record.

## 2 How It Grows

Four generating conditions.

Condition one: the goal cannot be measured directly. A goal that can be measured directly needs no proxy, and therefore leaves no seam. Wherever a proxy is required — "this portfolio's risk is under control," "this machine is in good condition," "this student has learned" — this chapter's mechanism has an entrance.

Condition two: superiors read only the number. Management's physical bandwidth is limited, and cross-level reporting compresses naturally into figures (Chapter 16's attenuation acquires its quantitative form here: each added layer of hierarchy keeps one more share of the narrative and one more share of the number). Once decision inputs converge on a single number, optimizing that number becomes the rational choice for every role in the organization: nobody breaks a rule, and every layer completes exactly what it is measured on (this is the technical implementation of Chapter 17's misaligned incentives).

Condition three: the evaluation cycle is shorter than the real cycle. Loan quality runs on a scale of years; the statements run on a scale of quarters. Student growth runs on years; examinations run on semesters. Wherever the gap between the two cycles sits, that is where the metric decouples from the goal.

Condition four: a single metric, no external check. There is no paired counterweight (volume without quality, output without rework rate), and no sampling from outside the system (the measured party self-reports, self-assesses, self-audits). The seam widens with no observer present.

## 3 The Pattern in Four Domains

### Case 1 (Finance): The Delinquent Loans That Moved Out of Frame

fi-001. Travel + Leisure Company, timeshare business. In a September 2026 enforcement action (Litigation Release No. 26657 / AAER-4603; the page has been verified for this book), the U.S. Securities and Exchange Commission found that from October 2019 to February 2021 the company removed thousands of severely delinquent or already-defaulted timeshare loans through a "rescission" program without making corresponding disclosure, materially flattering performance metrics such as the loan-loss provision; the company paid a civil penalty of $975,000 in settlement.

Stop at the decision point: the moment the removal of delinquent loans from the reporting frame is designed or approved. On the desk: the scale of the defaulted loan pool, the provision pressure and its effect on the financial statements, the contractual feasibility of the rescission program — and the question that gets bypassed: once the loans are moved, does the "loan-loss metric" that investors see still represent asset quality? 〔Outcome〕The SEC found the disclosure misleading; the company settled the case (without admitting or denying the findings). Primary source: SEC, Litigation Release No. 26657, 2026; link in Appendix B, fi-001.

### Case 2 (Public Sector): Ratings That Drifted from Actual Risk

po-003. The U.S. federal IT dashboard. Agency chief information officers (CIOs) assign risk ratings to major IT investment projects; the ratings go up to Congress and are public. A U.S. Government Accountability Office (GAO) report of October 2026 (GAO-27-108416; the page has been verified for this book) provides the comparison: of 53 major investments, GAO's independent assessment agreed with the CIO rating on 27; GAO judged the risk higher on 24 and lower on 2; 21 ratings had not been updated in a timely way; all 17 of GAO's historical recommendations were unimplemented; and the Office of Management and Budget plans to replace the dashboard with a new system.

Stop at the decision point: the quarter in which a CIO assigns a low risk rating to a project whose execution problems are already known. On the desk: the project's true execution state (GAO would later confirm the higher risk) and what a rating means for the public image of the project and the agency. The rating's original purpose was to let Congress see risk. Once the rating itself became the object under scrutiny — "why are all our projects red?" — optimizing the rating became a shorter path than eliminating the risk. 〔Outcome〕GAO's comparison went public, and the dashboard's credibility went to zero. Primary source: GAO, GAO-27-108416, 2026; link in Appendix B, po-003.

### Case 3 (Software): The Gatekeeper That Watched Only the Replica

sw-006. The GitHub platform. In September 2026, a background data-cleanup task crushed the primary database; for roughly an hour and a half, 96% of web requests to create issues failed. GitHub's official monthly availability report (verified for this book) states the root cause plainly: the cleanup task's protection mechanism monitored only the replication lag of database replicas and never brought the primary's own load into scope; with every replica metric reading healthy, the task pushed the primary over the line.

Stop at the decision point: the design or review of that protection mechanism. On the desk: replica lag is measurable, plottable, and threshold-able; the primary's load is equally measurable, but it is not on the list of "things that have caused incidents here before." The protection's metric chose the proxy that happened to have historical data. 〔Outcome〕Primary connections ran out; issue creation and account registration failed at scale. The fix: suspend the task, add primary-load metrics and call timeouts. Primary source: GitHub, Availability report September 2026, 2026; link in Appendix B, sw-006.

### Case 4 (Construction): The Broken Bolts That Never Entered the Ledger

ce-002. Audenshaw, Manchester — a railway bridge whose track sits on longitudinal timbers. A 2025 report by the UK Rail Accident Investigation Branch (RAIB, Report 10/2025; the page has been verified for this book) concluded that the derailment originated in fatigue fracture of baseplate fixing bolts, and that earlier bolt failures had been neither recorded by the maintenance team nor reported upward — Network Rail's safety assurance system failed to notice for years. The derailment occurred in September 2024; nine wagons ran off the track, and the line remained closed for roughly eight weeks.

Stop at the decision point: the moment a maintainer finds a fractured bolt and decides to swap it out and be done with it. On the desk: the failed part in hand, no matching record category anywhere in the work-order system, and no immediate benefit to reporting it upward. The equipment's true state speaks the language of "failure counts"; where failures go unrecorded, the system reads zero. The metric sits at zero while the goal worsens. 〔Outcome〕Fatigue cracks accumulated in the uncounted dark until the derailment wrote the data into the news, all at once. Primary source: RAIB, Report 10/2025, 2025; link in Appendix B, ce-002.

## 4 What Can Be Seen Earliest

Eight weak signals, each with the reason it is usually steamrolled by.

1. The footnotes to a metric's definition keep growing longer, until they require a dedicated explainer. The reason it gets waved off: "Refining definitions is a sign of management maturity."
2. The same metric means different things in different departments. Reason: "The businesses differ."
3. A dedicated "data governance" role appears in the organization, while the list of problems does not get shorter. Reason: "Data quality needs professional owners."
4. The metric improves while front-line felt experience diverges from it, and the divergence persists for more than two evaluation cycles. Reason: "The front line only sees its own corner."
5. Optimization actions on the measured quantity are visible in plain sight — month-end sprints, concentrated back-filling of records, selective reporting — and nobody asks how the actions connect to the goal. Reason: "Hitting the number requires flexibility."
6. A person who points out that a metric has gone bad loses points in the evaluation cycle or is rotated to another post. Reason: "Consider the big picture."
7. External comparison data — customer complaints, regulatory sampling, third-party assessments — diverges from internal metrics over the long run. Reason: "Different definitions; not comparable."
8. The metric's historical baseline is retroactively adjusted. Reason: "For comparability."

Item 7 is criterion 2 in its everyday form: external comparison is a free, independent check, and giving it up amounts to disconnecting this chapter's alarm.

## 5 How to Prevent It

Four lines of defense, stationed across the metric's whole life from birth to death.

Defense one (when setting a metric): rehearse the gaming. At the creation of every new metric, force a written answer to the question "how will this be gamed" — at least three optimization scenarios, each with its probe attached (what data would reveal it). Goodhart effects cannot be eliminated, only observed; a metric launched without a gaming rehearsal is a launch without monitoring.

Defense two (paired counterweights): every output metric must be paired with a quality metric, volume must be paired with rework rate, speed must be paired with incident rate. The paired metrics are collected by a different department (Diffusion of Responsibility, Chapter 18, applied in reverse): the measured party does not control the counterweight metric's definition or its sample.

Defense three (keep a channel that is not measured): maintain one information channel whose output is no metric at all — front-line interviews, sampling of raw complaint files, managers' direct observation on site. It feeds decisions and never evaluations, and it must have a named reader (the bypass-the-hierarchy channel of Chapter 16). When its output diverges from the metrics, the divergence itself is the most expensive signal the organization owns.

Defense four (register every definition change): each adjustment to a metric's definition, sample, or baseline is logged separately and reviewed by an independent party (an extension of Device 2 in Chapter 8). The audit definition in the Travel + Leisure case, the monitoring definition at GitHub, the record categories at Audenshaw — all three failures happened in the unregistered definitional zone.

## 6 Boundaries with Adjacent Mechanisms

Versus normalization of deviance (Chapter 11): normalization re-files a deviation (it moves the archive); goal displacement redefines a goal (it moves the ruler). In actual cases the two often share a bed: the optimized metric conceals deviations, and the deviations' unbroken success reinforces the metric's credibility. Distinguish them by the object of the action: archiving actions go to Chapter 11; measuring actions stay in this chapter.

Versus misaligned incentives (Chapter 17): misalignment is the disease at the structure layer (the interests of the different layers point in different directions); goal displacement is its most common technical implementation. The division of labor between the criteria: if what needs changing is the interest structure (who bears the consequence), go to Chapter 17; if the interest structure is sound but the measurement is crooked, stay in this chapter.

Versus the fifth step of escalation (Chapter 8): the yardstick change on step five is a crisis-time emergency action (it has meetings and decisions on record); this chapter's definition drift is steady-state gradualism (there is no single futable moment to point to). The two defenses share the definition registry, but the triggering scenarios differ.

## 7 Self-Check: Five Questions

1. Write down your team's three most important evaluation metrics, and for each one state the real goal it proxies. Any metric whose proxy relationship you cannot state should not yet be discussed as an optimization target.
2. In your organization, when did someone last point out that a metric had gone bad? What happened to that person afterward?
3. Pick a metric that has improved for three consecutive cycles and find one external comparison data point (complaints, sampling, felt experience) to check it against. How large is the divergence?
4. Which metric in your system has definition changes with no registration record? How much of that metric do you still believe?
5. If your core KPI were abolished tomorrow, what is the first number you would want to look at? Why is that number not inside the metric today?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

Gaming rehearsal goes first — it is the only device that acts before a metric goes live, and retrofitting it onto a metric that is already being gamed is an autopsy. Paired checks and caliber registration follow; the non-metric channel comes last, because it is the hardest to install and the easiest to cut, and standing at the end protects it as an established asset. First ninety days: week one, rehearse every metric in the coming cycle (three plays each, two to three days of meetings); weeks two through six, pair the core metrics and settle which departments own the counter-metrics; weeks seven through ten, put caliber registration on a system — even a shared sheet will do; week twelve, open the first non-metric channel in its smallest form (front-line interviews, a named reader, one trial round).

How each device gets gamed. Rehearsal turns theatrical: three plays written to be progressively harmless, with nobody reading the output. Require play-and-probe pairing (each play must name a probe — what data, what threshold, triggers what review; a play without a probe counts as unrehearsed). Paired checks get captured: rework rates self-reported by the team being measured. The pairing's whole point was organizational separation of collectors from the measured — lock it in writing and spot-check the counter-metrics' raw sources quarterly. The non-metric channel dies quietly of heartbreak (interviews held, reader reads, nothing happens), so require a written receipt for every channel output ("read; action: none / yes, action No. X" — three consecutive no-actions escalates). Caliber registration simply stops being filled in; bind it to report publication — an unregistered caliber change blocks the release, which is half a form field of engineering.

Cost: half a day per metric for the rehearsal; one-time setup for the pairings plus one or two hours a month per metric for independent collection; near-zero for registration; about half a day a month for the channel. A twenty-metric team carries eighty to a hundred hours a year. Against Travel + Leisure's $975,000 penalty or the GAO's 24 divergent risk ratings, the first averted caliber change pays for everything.

Toolchain: Chapter 35 lists this chapter as the measurement face of the incentive cluster (systemic misalignment lights rows 12, 17, 19, 27). Question set 12 audits the devices; post-mortems whose conclusions read "metric fine, target worse" install Device 2; and in the thirty-minute walkthrough, this chapter's criterion — dedicated optimization actions on the measured quantity — is among the easiest to confirm with data inside fifteen minutes.

## Quick-Reference Card

**The mechanism in one sentence:** every metric is a proxy for a goal

**The three criteria, compressed:** The measured quantity begins to attract dedicated optimization work, and the cost of that work goes into the number rather than into the thing itself; / The optimizing actions do not improve the goal being represented — they leave it flat, or they consume it; / Someone pays a price, in evaluations or in meetings, for pointing any of this out

**The devices (Section 5 has the detail):** see Section 5.

**The four loudest weak signals (Section 4):** The footnotes to a metric's definition keep growing longer, until they require a dedicated explainer; The same metric means different things in different departments; A dedicated "data governance" role appears in the organization, while the list of problems does not get…; The metric improves while front-line felt experience diverges from it, and the divergence persists for more….

**Cost register and case index:** ce-002: 无人伤亡；9节货车脱轨，线路封闭约8周; fi-001: 民事罚款97.5万美元；涉及约7700万美元贷款余额; po-003: 53项重大投资中GAO评估风险更高者24项；21项评级未及时更新; sw-006: 事件约1.5小时；期间约96%网页建单请求受影响.

**Domain cross-reference:** this chapter's cases live on the Construction, Finance, Public Policy, Software domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** The metric did not go bad; the organization's behavior did. Watch the behavior, not the number's mood.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "the metric will look great" belongs here; the check action is the gaming rehearsal.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: Normalization Of Deviance (Ch. 11), Misaligned Incentives (Ch. 17), The Fifth Step Of Escalation (Ch. 8) (read the boundary discussion in Section 6 first). Question set 12 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(Chinese source: expanded and synced; English edition: about 3,214 words)
