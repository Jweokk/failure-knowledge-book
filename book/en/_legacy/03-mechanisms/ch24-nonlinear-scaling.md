# Chapter 24: Nonlinear Scaling across Thresholds

> What this chapter covers: why the same method fails at larger scale; three criteria, four field sites, the rhythm of "re-validation at each order of magnitude," and putting coordination cost on the books.
> When to return: at the moments when growth accelerates, when a platform forms, when a single point turns into a network, and when self-operation turns into openness.
> Reading time: 50 minutes.

Growing organisations carry an illusion: if it worked with a hundred people, then with a thousand we simply try harder. The illusion's mathematical basis is wrong: coordination cost grows superlinearly with the number of nodes, management bandwidth decays with the number of layers, and validation's sample assumptions were set at the old magnitude. The most dangerous thing about crossing a scale threshold is its failure mode: not collapse, but a quiet change in kind. The same method keeps running, everyone keeps trying hard, and the quality of output silently changes its nature — while every current indicator still looks good, because the deteriorating part grows precisely in the dimensions the indicators cannot see.

## 1 What It Is

Definition: an organisation's capability function is not linear. Coordination cost, information loss, the number of anomaly exposures, the number of interfaces — all grow superlinearly with scale; meanwhile the organisation's governance structure (processes, systems, staffing, validation rhythm) was designed for the previous size. Crossing a scale threshold means: the same method quietly fails at some magnitude, and the failure arrives ahead of any alarm.

Three trigger criteria (if any one appears, the mechanism has already started):

① The same method has already changed in kind at twice the scale: it now survives only on "let's coordinate a bit more";
② A new management layer has been added, or the number of meetings grows out of proportion to headcount;
③ Local optima begin to cancel each other (every department is optimising; the overall indicator stalls or worsens).

## 2 How It Grows

Three generating conditions. Condition one: growth outruns governance's renewal cycle. The governance structure was built for the scale at design time, and growth leaves its boundary of validity behind; the boundary raises no alarm, because the old method's success record at the old magnitude keeps being produced (only the sample behind it already belongs to an earlier scale). Condition two: validation's sample size was never reset with scale. A defect-rate hypothesis validated on a thousand users scales its exposure count proportionally in front of a million users: the probability is unchanged, the absolute count multiplied by a thousand. A rare defect becomes a daily report, and the capacity to process daily reports was not multiplied by a thousand. Condition three: the invisibility of coordination cost. Meeting time does not enter product cost, layer overhead does not enter the financial report, interface staffing does not enter gross margin (a sister of Chapter 29: maintenance is invisible, and coordination is equally invisible). Costs that are invisible default to zero in growth decisions.

The threshold's most insidious property is its after-the-fact nature: a threshold only becomes visible after it has been crossed, and the visible sign is usually the veteran's sentence: "it didn't use to be this way." In an organisational context, that sentence is not nostalgia; it is data.

## 3 The Mechanism in Four Domains

### Case 1 (Manufacturing): One Year on the Market Burned In a Recall of 338,800 Units

mn-003. The DREO DR-HSH015 electric heater. CPSC recall notice (reviewed for this book): approximately 338,800 units recalled (about 36,300 more in Canada), with 17 reports of ignition, 1 hand burn, and 3 reports of property damage — a sweeping recall triggered within one year of the product's launch. With the per-unit defect rate unchanged, channel volume multiplied the exposure count (the summed hours of operation) by several orders of magnitude: the "acceptable low probability" under the validation rhythm entered the zone of inevitability in the first sales season after scale-up. The threshold was not in the factory; it was in the channel.

Stop at the decision point: the moment the first production run and the channel distribution plan were set. On the table: the sample size of the validation batch, the distribution multiple of the channel, and a relation never drawn as an equation between the two: the validation covered the usage intensity of a thousand units, while the channel promised the exposure of a million. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Large-scale recall. Primary source: CPSC, 2026; link in Appendix B, mn-003.

### Case 2 (Public): Eleven Thousand Schedules

po-001. US FAA air traffic control modernisation (BNATCS). GAO report (GAO-26-107992, reviewed for this book): in July 2025 Congress appropriated 12.5 billion dollars for phase one; FAA estimates phase two will need roughly 10.2 billion more; the programme comprises 138 systems, FAA holds 11,389 independent project schedules that have not been integrated, and there is no full life-cycle cost estimate. The programme's engineering scale crossed the threshold of coordination: each schedule is defensible locally, and the whole's schedule and cost are therefore unknowable — it is not that nobody is managing; it is that the management tool's designed capacity (tracking project by project) lost its power of aggregation in front of the system count.

Stop at the decision point: the moment the multi-phase programme's governance structure was set up and the schedule management tools and their metrics were chosen. On the table: the count of subprojects, the existing tools' capacity, and Congress's appropriation rhythm. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕GAO framed it as "cost and planning need improvement," leaving the integration pressure to phase two. Primary source: GAO, GAO-26-107992, 2026; link in Appendix B, po-001.

### Case 3 (Software): The Day of Record Load

sw-005. The GitHub platform, 17 August 2026. Official statement (reviewed for this book): record-breaking load broke through components with insufficient headroom; the outage lasted 7 hours 47 minutes. The core assumptions of capacity planning had been calibrated on historical peaks; a record-setting day zeroed out the historical extrapolability of those assumptions: the scaling coefficient was not wrong — what the coefficient extrapolated from (the previous generation's load shape) was no longer this load. Scale here arrived as the double growth of traffic and task shape: the old peak curve could not measure the new workload.

Stop at the decision point: the most recent moment the capacity model set its parameters on historical peaks and left no unjustified headroom for a "record day." On the table: the growth curves, the architecture of the last peak, and a set of new behaviours that could not be verified. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Nearly eight hours unavailable; recovery completed in phases, with the follow-up work named "the work ahead." Primary source: GitHub, 2026; link in Appendix B, sw-005.

### Case 4 (Finance): Thirty-Eight Shells Registered in Bulk

fi-004. SEC's mass action against 38 fictitious investment adviser entities (Litigation Release No. 26622, reviewed for this book): between 2025 and 2026, the defendants made major false statements in Forms ADV filed with the Commission, presenting themselves as legitimate advisory firms; the cases were consolidated in the US District Court for the District of Colorado. The registration system's designed capacity faced firm-by-firm human review; bulk, automated, template-based fabrication voided the review's scale assumptions wholesale: the threshold never changed — the way of crossing it did. This is the adversary's version of the scale threshold: not an organisation growing, but the scale of attack growing, while the defence's granularity remains one firm at a time.

Stop at the decision point: every day the registration system's structure (bulk submission interfaces, formal review rules) remained unchanged in front of the new automated use. On the table: the anomalous growth of submission volume, and the compliant appearance of each firm's materials. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕38 cases consolidated in one action; systematic registration anti-fraud entered the agenda. Primary source: SEC, Litigation Release No. 26622, 2026; link in Appendix B, fi-004.

## 4 What Shows Earliest

Six weak signals, each with the reason that usually overrides it.

1. A new management layer is added, with the stated purpose of "strengthening coordination." Override: "we have reached that scale."
2. The number and length of meetings grow out of proportion to headcount, and decisions slow down. Override: "people are eager to align."
3. The veterans' catchphrase becomes "it didn't use to be this way." Override: "nostalgia."
4. Every local indicator improves while the overall indicator stalls or worsens. Override: "every department is working hard."
5. Rare events rise in frequency proportionally with scale (absolute counts grow) and get misread as quality deterioration. Override: "a quality problem." (The numerator grows with the denominator; that is not a quality signal.)
6. The staffing share of interfaces, reconciliation, and cross-department scheduling quietly exceeds the staffing share of core output. Override: "big companies are all like this."

## 5 How to Defend

Device one: re-validation at each order of magnitude. Divide organisational scale into orders-of-magnitude steps (ten, a hundred, a thousand, ten thousand); at each step crossing, the core assumptions — coordination method, validation sample size, capacity coefficients, review throughput — are force re-validated. Not linear extrapolation; the problem is reworked from scratch. GitHub's capacity coefficient, DREO's validation sample, and FAA's schedule tool should all re-sit the exam at each step; the exam has one question: does this method still hold at the new magnitude? On what evidence?

Device two: coordination cost on the books. Hours spent in cross-department meetings, reconciliation, and interface maintenance are counted and published quarterly; when the share crosses a threshold (self-set, for example a fifth of core hours), a structural review is triggered. Invisible costs are the ones that need bookkeeping; visible costs will call out on their own. Bookkeeping also gives the expansion of "we hire in order to coordinate" a true unit price.

Device three: unjustified headroom in capacity assumptions. For "record day" class scenarios, the capacity model reserves one tier of headroom that cannot be argued from history (for example, two tenths on top of the peak coefficient), and the document states plainly "the basis of this tier is that we do not know." The basis of headroom may be luck, provided someone remembers it is luck: write it down, and luck can be audited.

Device four: an annual teardown question about structure. Once a year, run the thought experiment: "if we designed from zero today, how would the coordination structure differ from today's?" The difference list does not serve an immediate reorganisation; it serves as early warning: the speed at which the list lengthens is the speed at which the threshold approaches (Chapter 34's path-locking contrast question, used here in reverse).

## 6 Boundaries with Adjacent Mechanisms

Against extrapolation beyond the validated domain (Chapter 23): change of scale is the difference item most often left off the list: Chapter 23 governs "whether the differences got listed," and this chapter governs "how to re-validate once they are listed." Pilot to rollout goes through Chapter 23's declaration form; every crossing of an order-of-magnitude step goes through this chapter's re-validation.

Against cascading failure (Chapter 33): dependency concentration at networked scale is cascading's territory; this chapter governs the nonlinearity of coordination and validation, cascading the propagation of a single point amplified by the network. Growing platforms should read the two chapters together.

Against diffusion of responsibility (Chapter 18): scale expansion's habitual remedy is adding people and adding signatures, and a lengthening signature chain is exactly what manufactures dilution: using Chapter 18's disease to treat Chapter 24's disease is the most common self-injury of growing organisations. Responsibility design during expansion should use a single accountable person, not added signatures.

## 7 Self-Check: Five Questions

1. Which order-of-magnitude step is your organisation on now? At the last step crossing, which core assumptions were re-validated?
2. What is coordination's share of your core hours? Is there a number? Having no number is itself the answer.
3. The most recent reset of a capacity or review-throughput assumption — was it triggered by data or by an incident?
4. What process did the veterans last describe with "it didn't use to be this way"? When did that process last run as originally designed?
5. If scale doubled tomorrow, what is the first thing that would break? Does what you are betting on match the headroom you have set?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

Coordination-cost accounting goes first — it is the gauge; nonlinearity shows up in the numbers before it shows up anywhere else. Cross-threshold re-validation follows (the gate at each doubling), unsupported capacity margins third (the cushion for the crossing season), and the annual demolition question last (a culture device: one meeting a year, interrogating the whole structure). First ninety days: week one, open the coordination accounts — quarterly curves for meeting count, management layers, interface documents, cross-team approval-chain length; four numbers suffice; weeks two to six, locate the last threshold crossings (users, throughput, headcount) and check whether re-validation happened there; month two, register the three most fragile capacity assumptions as unsupported margins (which assumptions were eyeballed, at what number — written down); month three, hold the first demolition session (one agenda: building from zero today, what gets cut — no conclusions required, the list goes on file).

Failure modes. Coordination accounts get cosmetically merged (meetings consolidated, templates unified, the curve dressed flat) — take the numbers by machine from calendar and document systems, never by self-report. Re-validation shrinks to capacity only (systems hold; the sign-off chain doesn't — Chapter 18 at scale) — run twin checklists, technical and organizational, the latter covering approval latency, decision backlog, incident response time. Cushions get raided first in tight budgets (Chapter 25's erosion, applied to air) — wall them: a separate line item, any draw registered with a repayment date. The demolition session turns into a tribute session (proving the present structure wise) — spec the output: three things that would not exist if built from zero; a year that produces no three is an invalid year.

Cost: the accounts are a one-time extraction script plus an hour or two a month; re-validation fires at crossings (one to two weeks each); margin registration is entry cost; the demolition session is half a day a year. Against a record load finding the one never-stressed component, a hospital oxygen system sized to an old bed count, or a $75 million startup dead by its own expansion — scale failures share one signature: yesterday's map over today's territory. All four devices redraw maps.

Toolchain: the locator triggers on "climbing from multi-team toward network" — a happening trigger, table repeated during the climb. Question set 24's item 2 ("is coordination cost measured") audits the accounts. Post-mortems with "designed to the old scale" feed the twin checklists. And in pre-mortems during a climb, scale-class deaths convert to re-validation: the pre-mortem doubts the assumption; re-validation collects on the doubt.

## Quick-Reference Card

**The mechanism in one sentence:** an organisation's capability function is not linear

**The three criteria, compressed:** 

**The devices (Section 5 has the detail):** Device one: re-validation at each order of magnitude; Device two: coordination cost on the books; Device three: unjustified headroom in capacity assumptions; Device four: an annual teardown question about structure.

**The four loudest weak signals (Section 4):** A new management layer is added, with the stated purpose of "strengthening coordination." Override: "we have…; The number and length of meetings grow out of proportion to headcount, and decisions slow down. Override…; The veterans' catchphrase becomes "it didn't use to be this way." Override: "nostalgia."; Every local indicator improves while the overall indicator stalls or worsens. Override: "every department is….

**Cost register and case index:** fi-004: 无公开量化（新起诉）; mn-003: 召回约338,800台（33.8万台；加拿大另约36,300台）；17起点燃、1; po-001: 一期拨款125亿美元；FAA自估二期还需约102亿美元; sw-005: 宕机7小时47分钟.

**Domain cross-reference:** this chapter's cases live on the Finance, Manufacturing, Public Policy, Software domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** Scale is nonlinear: yesterday's map does not cover today's territory.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "the last doubling hurt nothing" belongs here; the check action is the re-validation record.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: see Section 6 (read the boundary discussion in Section 6 first). Question set 24 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(First draft: 3,615 Chinese characters; English edition independently written.)
