# Chapter 32: Compliance without Safety; Safety-I and Safety-II (Hollnagel)

> What this chapter covers: why a system that passes every single check can still be lethal; Hollnagel's Safety-I/Safety-II distinction, three field sites, and "scenario-based inspection."
> When to return: after every check has passed and the accident happens anyway; and whenever someone proposes "adding one more compliance requirement."
> Reading time: 50 minutes.

The compliance system carries a promise it never states aloud: meet every clause and you are safe. Erik Hollnagel calls this find-failure-and-assign-blame mode of inspection Safety-I, and names its blind spot: it can prove the absence of violations, but it cannot prove safety — safety was never the sum of the clauses; it is the system's performance as a whole in real scenarios. The seams between clauses, the new scenarios the clauses do not reach, the way clauses are executed on false premises — all of it falls outside Safety-I's field of view. This chapter's three field sites display three prices of that blind spot: a physical gap that could be computed, one wrong classification, and a consent mechanism still in violation after remediation.

## 1 What It Is

Definition: compliance without safety is the structure in which the inspection system passes every item and the safety accident happens anyway: rules are written clause by clause, inspections are executed clause by clause, every clause's compliance is genuine — but the seams between the rules belong to no one, and compliance gradually replaces safety judgement as the proof of safety (Hollnagel, Safety-I and Safety-II: Safety Thinking in Action, Ashgate, 2014; the Crossref citation has been verified).

Three trigger criteria (if any one appears, the mechanism has already started):

① Every check is compliant and the accident still occurs;
② The seams between compliant items belong to no one: no post signs for "whether the whole is safe";
③ Compliance records begin to be used as proof of safety ("we meet every standard" becomes the final answer to challenges about risk).

## 2 How It Grows

Three generating conditions. Condition one: the historical path of clause-by-clause rule writing. Laws and standards grow naturally in the form of clauses; the clause is the inspectable unit, and the inspection can only see clauses. Condition two: the cost structure of inspection. Clause-by-clause inspection can be standardised, outsourced, and evidenced; whole-system assessment cannot be standardised, and so loses ground after ground in resource allocation. Condition three: the self-protective choice on responsibility. For the inspector, "every clause passed" is the safest conclusion; for the inspected, "every clause met" is the cheapest defence. Supply and demand together push the inspection system toward clause-ification, and the destination of that push is criterion ③: the compliance certificate replaces safety judgement across the board.

## 3 Field Sites

### Case 1 (Aviation): The Qualified Certification and Flammable Tank Vapour

av-036. Trans World Airlines Flight 800, Boeing 747-131 (N93119), 17 July 1996. NTSB final report (AAR-00/03; the official 341-page PDF was downloaded and reviewed for this book): the centre wing tank's fuel-air vapour exploded and the aircraft broke up in flight; all 230 aboard died (the report's own words confirm: "230 people on board were killed"). The certification-philosophy gap the report identified is this chapter's specimen: the certification framework accepted the presence of flammable fuel-air vapour in the tank, treating safety as achieved so long as every ignition source was eliminated — every certification requirement was duly executed, and the fact "flammable vapour is flammable" sat in no requirement's inspection scope. The compliance system asked the tank one question only — "is there an ignition source" — and never asked "is there flammable vapour"; the answer to the second was yes, and it was a physical fact.

Stop at the decision point: the moment the certification framework converged on "eliminate the ignition sources and we are done" and wrote it into the rules and the training. On the table: the ignition-source list and its reliability data, the physics of fuel vapour flammability, and the framework's disposition of "residual flammable vapour": accepted by default. 〔Outcome〕230 people died; the certification system introduced fuel tank inerting step by step afterwards — one more line on Safety-I's checklist, and a local correction to the philosophy of the seam. Primary source: NTSB, AAR-00/03, 2000; link in Appendix B, av-036.

### Case 2 (Chemical): The Dust Workshop Correctly Inspected Under the Wrong Class

ch-008. The polishing workshop of Kunshan Zhongrong Metal Products Co., Ltd., 2 August 2014. State Council accident investigation team report (published on the website of the Ministry of Emergency Management; the full report has been reviewed for this book): an aluminium dust explosion killed 97 people, injured 163, and caused direct economic losses of 351 million yuan. Among the key facts the report established: the collection bucket of dust collector No. 1 was rusted through, and damp aluminium dust inside oxidised exothermically and ignited (original verified); and the workshop's hazard class had been wrongly assessed as Class E. After the mis-classification, every check executed to Class E standards passed: Class E (production using non-combustible substances at ambient temperature) requires none of the explosion-proof provisions an aluminium dust workshop should have, and the dust collection system's maintenance arrears had no corresponding inspection item anywhere in the compliance system. Compliance ran here in full working order — running, on a wrong classification.

Stop at the decision point: the entry into force of the hazard-class assessment, and the first inspection cycle thereafter executed under that class. On the table: the assessment paperwork, the workshop's actual process and dust properties, and the distance between the paperwork and the actual. 〔Outcome〕97 dead, 163 injured; the criminal and disciplinary dispositions of those responsible are in the report. Primary source: State Council "8·2" accident investigation team, 2014; link in Appendix B, ch-008.

### Case 3 (Software): Still in Violation After the Remediation

sw-007. Google LLC and Google Ireland. CNIL decision (reviewed for this book): in September 2025, for inserting advertisements into Gmail without consent and for cookies set at account creation without valid free and informed consent, fines totalling 325 million euros were imposed (200 million on Google LLC, 125 million on Google Ireland). The decision records a more noteworthy chronology: remediation had already been conducted in two earlier rounds, and the regulator found the violations still persisting. The compliance process ran in full working order — remediate, re-check, remediate again — while the whole question "are users actually consenting in knowledge and freedom" was unchanged by the item-by-item fixes. The remediation changed how the clauses were implemented; what violated was the overall design of the consent mechanism.

Stop at the decision point: the moment the second remediation plan was finalised and the team confirmed "we now meet the requirements." On the table: the item-by-item closure of the remediation checklist, the real consent rates in the user research, and the compliance credentials of each of the two bodies of information. 〔Outcome〕A 325-million-euro fine; the overall design of the consent mechanism was named. Primary source: CNIL, 2025; link in Appendix B, sw-007.

### Evidence Gap Note

This chapter's fourth case slot is reserved for the same pattern in agriculture and food (systemic outbreaks under compliance systems such as HACCP; the compliance histories of selected outbreak cases already collected in CDC MMWR require retrospective verification), to be added once collected. The three existing cases cover aviation, chemicals, and data compliance.

## 4 What Shows Earliest

Six weak signals, each with the reason that usually overrides it.

1. The safety meeting's agenda is entirely "was there a violation," never "where could it happen." Override: "compliance is the floor."
2. Every finding is a single-clause finding; no cross-clause, systemic finding ever appears. Override: "inspections are designed clause by clause."
3. "We meet every standard" is deployed to answer challenges unrelated to any clause. Override: "let the data speak."
4. The approval flow for exceptions and waivers runs more smoothly than the remediation flow. Override: "waivers have a dedicated channel."
5. Risks reported by the front line have no corresponding inspection item, and so never enter inspection results. Override: "without a clause there is nothing to inspect."
6. Check items added after accidents accumulate year on year; inspection hours double while the accident rate stands still. Override: "keep strengthening."

## 5 How to Defend

Device one: the plus-one question after every compliance check. The conclusion page of every compliance inspection carries one fixed additional question: "Taken together, are these compliant items safe?" The answer must come from a person who signs for the whole (Chapter 18's single accountable owner), and must cite at least one cross-clause whole-system analysis (scenario walk-through, joint failure analysis). One question does not close the seam; one question puts the seam into writing.

Device two: scenario-based inspection. Once each year, switch the inspection system from clause mode to scenario mode: pick three real accident scenarios (from your own library or the industry's), walk the full chain of relevant clauses and field conditions along each scenario, and record the stretches no clause covers. The uncovered stretches are the map's edge: the mis-assessed class at Kunshan, the flammable vapour of TWA 800, the overall consent design at CNIL are all locations on that edge.

Device three: Safety-II sampling. Periodically collect "how is it that things go well": not hunting violations, but recording the differences between actual everyday practice and the rules (an operationalisation of Hollnagel's method). Most of the differences are harmless; a few are exactly where the seams lie — and they can only be seen in success, because failure exposes only the failure point, while success exposes the entire way of working.

Device four: a prohibition on the compliance certificate. It is forbidden to answer a safety challenge with "we meet every standard"; the answer must point to scenario-based whole-system analysis. What this prohibition changes is a habit of language — and until the habit of language changes, criterion ③ is already running in every organisation.

## 6 Boundaries with Adjacent Mechanisms

Against regulatory lag and capture (Chapter 31): lag and capture supply the compliance system's stale rules (the climate); this chapter runs inside the stale rules (the weather). The longer the old rules run, the louder Chapter 32's "we meet every standard."

Against the illusion of redundancy (Chapter 22): the illusion counts defences by number and not by kind; compliance without safety counts inspection by clause and not by scenario. Both share the same auditing habit: count what can be counted, ignore what cannot.

Against normalisation of deviance (Chapter 11): normalisation's form inside the inspection system is criterion ③ — answering challenges about risk with compliance records. Chapter 11 watches the ledger; this chapter watches the meeting language.

## 7 Self-Check: Five Questions

1. Your domain's most recent accident — had every prior compliance check passed? What fraction of the causal chain did those checks cover?
2. How many lines in your inspection checklist were added ten or more years ago? When did each last intercept anything?
3. Where was the most recent occasion your organisation's compliance certificate was used to answer a safety challenge — and who pressed on the whole scenario?
4. If next year you halved the compliance-inspection budget and doubled the scenario-walk-through budget, would your organisation's visibility of risk rise or fall?
5. Pick one scenario you are responsible for (fire, outage, contamination) and walk your entire rulebook along the accident chain: how long is the stretch the clauses cannot reach, written out?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

The one-more-question goes first — it costs nothing: one sentence appended to every inspection report. Scenario-based inspection follows (it re-organizes checking from line items to scenes), Safety-II sampling third (a new observing habit: how the right runs went right), and the compliance-proof usage ban last (a legal and communications discipline riding the outbound-document templates). First ninety days: week one, write the question into the inspection template ("taken together, are these compliant items safe today — and who signs that judgment?"); weeks two to four, design the first scenario inspection (one real cross-item scene — night shift, single staffing, degraded equipment — and walk the relevant clauses through it); month two, start Safety-II sampling (one normally completed high-risk operation a week; record what went right, especially the informal moves that caught the slack); month three, draft the usage ban (any outbound document citing compliance proof must carry a whole-system judgment field; the ban goes into legal's template set).

Failure modes. The question becomes liturgy ("safe" appended by an unhesitating hand) — require differentiation: the answer must name the period's weakest item and its handling; five reports answering in one sentence count as unanswered. Scenario inspections get staged (the scene designed, the crew rehearsed) — add randomness, Chapter 20's live-testing rule: degraded mode, time, and personnel drawn by lot. Safety-II sampling turns into a laurel (the standard gets the credit; the informal backstops stay hidden) — anonymize and guarantee: backstop records enter no appraisal and trigger no retrospective discipline — promise that in writing before sampling starts, or nobody writes anything down. Usage bans get PR exceptions for big occasions — an equal clause: every exception citing compliance proof carries a same-page risk disclosure.

Cost: the question is free; a scenario inspection is half a day to a day per quarter; sampling is half an hour a week; the ban is template work. Against a dust workshop that passed every check on its way to detonation, problem cheese sold through legal channels, paper compliance over live risk, or sterile barriers with batch-to-batch holes — the compliance-safety gap lives entirely in the seams between lines, and the four devices are one seam-scanner.

Toolchain: the locator triggers on "dense oversight plus safety meetings that only discuss violations." Question set 32's item 2 ("has anyone asked whether they're safe together") audits the one-more-question. Chapter 38's success-post-mortem variant and Safety-II sampling share a method: the run that went right carries more information than the one that went wrong. And in pre-mortems, seam-class deaths convert to scenario inspections: the pre-mortem names the scene; the inspection walks into it.

## Quick-Reference Card

**The mechanism in one sentence:** compliance without safety is the structure in which the inspection system passes every item and the safety accident happens anyway: rules are written clause by clause, inspections are executed clause by clause, every clause's compliance is genuine — but the seams between the rules belong to no one, 

**The three criteria, compressed:** 

**The devices (Section 5 has the detail):** Device one: the plus-one question after every compliance check; Device two: scenario-based inspection; Device three: Safety-II sampling; Device four: a prohibition on the compliance certificate.

**The four loudest weak signals (Section 4):** The safety meeting's agenda is entirely "was there a violation," never "where could it happen." Override…; Every finding is a single-clause finding; no cross-clause, systemic finding ever appears. Override…; "We meet every standard" is deployed to answer challenges unrelated to any clause. Override: "let the data…; The approval flow for exceptions and waivers runs more smoothly than the remediation flow. Override: "waivers….

**Cost register and case index:** av-036: 机上230人全部死亡; ch-008: 97人死亡、163人受伤；直接经济损失3.51亿元; sw-007: 罚款3.25亿欧元（2亿+1.25亿）.

**Domain cross-reference:** this chapter's cases live on the Aviation, Chemical, Software domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** Every line can pass and the whole can still kill: the gaps need a scanner.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "every check passes and things still fail" belongs here; the check action is one scenario-based inspection.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: see Section 6 (read the boundary discussion in Section 6 first). Question set 32 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(First draft: 3,546 Chinese characters; English edition independently written.)
