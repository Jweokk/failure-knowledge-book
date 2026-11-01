# Chapter 23: Extrapolation beyond the Validated Domain

> What this chapter covers: the mechanism by which "validated at A" gets carried straight to B; three criteria, four field sites, a mandatory format for the difference list, and graded release.
> When to return: when a pilot turns into a rollout, when a method crosses between models or versions, when an old instrument gets a new use, and whenever "this is how we have always done it" is being written into a new scenario.
> Reading time: 50 minutes.

All knowledge has boundaries; the question is never "whether there is a boundary" but "whether the boundary has been declared." A validation report says a method works — strictly speaking, that sentence is incomplete: the complete version is always "works under such-and-such conditions, within such-and-such range, on such-and-such objects." Extrapolation beyond the validated domain names the default act: whoever cites the conclusion silently fills in the omitted part, reading "valid here" as "valid everywhere." This completion is cognition's factory setting; what this chapter does is charge a declaration fee for every extrapolation. Eliminating extrapolation would eliminate all action, and that is not this book's direction.

## 1 What It Is

Definition: extrapolation beyond the validated domain means using a conclusion that holds inside its boundary as a boundary-free law, while the boundary itself is never listed — let alone declared invalid item by item. Machine learning calls the same problem out-of-distribution use; the traditional terms in engineering and medicine are off-label and beyond-limit use.

Three trigger criteria (if any one appears, the mechanism has already started):

① The environment of use differs from the environment of validation, and the items of difference have never been drawn up as a list;
② "We already validated this at A" appears in the argument as a no-inspection-needed reason;
③ The items of difference were once pointed out by individuals, but never entered the decision record.

Extrapolation is not always wrong: an organisation that forbids extrapolation entirely cannot act (the exploratory failure of Chapter 40 in Part Six is extrapolation under control). The judgment of this mechanism falls not on the act of extrapolating but on the absence of the difference list: extrapolating without declaring is the disease. Declare the differences, explain the impact item by item, complete the verification the differences require — that is a rollout. Do none of it and it is cargo, hauled.

## 2 How It Grows

Three generating conditions. Condition one: organisational separation between pilot and rollout. The pilot team knows where the boundary lies (which users, which city, what weather, who was watching); the rollout team receives the conclusion with the boundary stripped off; the knowledge of the boundary is tacit and stays behind with the pilot team. Condition two: the analogical lure of cross-domain transplantation. The similarity is at the surface (all insulin, all jet display flying, all dairy), the difference at depth (concentration scales, aircraft performance, microbial ecology); surface similarity powers the analogy's intuition, deep difference decides whether the conclusion lives, and it is the intuition that speaks at the decision meeting. Condition three: the cost of validation is borne by one side only. The cost of writing the boundary clearly and re-verifying item by item falls on the user, while the benefit of speed accrues to the decision-maker — so naturally nobody writes the list.

## 3 The Mechanism in Four Domains

### Case 1 (Aviation): A Vintage Jet Inside a Display Framework

av-021. Hawker Hunter T7 (G-BXFI), the Shoreham air show, 22 August 2015. AAIB formal report (AAR 1/2017, reviewed for this book): while performing a manoeuvre, the aircraft crashed onto the A27 road; 11 people on the road died, and 13 people including the pilot were injured. The UK air show safety framework — the display line, the crowd exclusion zone, the approval of manoeuvres — had been built for the existing fleet and the existing families of manoeuvres and had run for years; a single-engine jet of 1950s design entered this framework with high-energy manoeuvring, and the boundary of the framework-and-aircraft-performance combination was never re-declared. The existing protection system did not fail; it ran according to its design assumptions. What failed was the declaration of fit between the assumptions and this case's aircraft.

Stop at the decision point: the moment this aircraft's display sequence entered the approval and execution chain. On the table: the framework's existing clauses, the type's performance file and energy-management characteristics, and the relative positions of the road and the flight path. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕11 people on the ground dead; the report drove revision of the air show safety framework. Primary source: AAIB, AAR 1/2017, 2017; link in Appendix B, av-021.

### Case 2 (Pharma and Devices): The Reprocessing Protocol Covered a Model It Should Not Have

ph-007. The Ethicon XCEL trocar (5 mm), circulated after reprocessing by Stryker Sustainability Solutions. FDA device recall record (Z-3183-2026, API record reviewed for this book): the reprocessed device may crack; 2,838 units recalled. Reprocessing and reuse of single-use devices has mature protocols and a regulatory framework; the framework's boundary of applicability to this model's specific structure — the integrity behaviour of the bladeless trocar's seal and hub connections after reprocessing cycles — was covered over by the protocol's generality. The protocol had validated "devices of this class can be processed this way"; it had never validated "this one."

Stop at the decision point: the review moment when the reprocessing protocol admitted the new model to its list and the batch was released. On the table: the protocol's prior safety record, the structural differences between the new model and prior models, and the release schedule. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Recall; batch withdrawn. Primary source: FDA, Enforcement Report Z-3183-2026, 2026; link in Appendix B, ph-007.

### Case 3 (Healthcare): The Boundary of a Syringe Scale

me-002. General medical wards in an English hospital. HSIB report (Administering high-strength insulin from a pen device in hospital, 2022; archived snapshot reviewed for this book): after the dedicated safety needle for U-500 high-strength insulin (500 units per millilitre) disappeared from the supply catalogue following a contract change, nurses switched to drawing the dose with U-100 syringes — a syringe graduated for 100 units per millilitre was used with fluid at 500 units per millilitre, every graduation reading five-fold, and the patient suffered two hypoglycaemic events. The U-100 syringe's validated boundary was the world of U-100 concentration; the instrument never changed, the world changed five-fold, and a qualified tool inside the boundary became an overdose generator outside it.

Stop at the decision point: the moment the safety needle vanished from the catalogue and the nurse chose a substitute instrument before drawing the dose. On the table: the syringe at hand, the concentration label on the fluid, and the seam along which the catalogue-change notice never reached the ward. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Two hypoglycaemic events; the report issued recommendations along the chain from supply to bedside. Primary source: HSIB, 2022; link in Appendix B, me-002 (archived link, grade A−).

### Case 4 (Agriculture): Raw Milk's Safety Assumptions and 171 Cases

ag-001. Commercially distributed raw milk in California, from September 2023. CDC MMWR report (Vol. 74, reviewed for this book): a Salmonella Typhimurium outbreak was confirmed at 171 cases with 22 hospitalisations, of which 120 cases (70%) were minors under 18; the timeline runs from first illness onset on 21 September, county health department report on 18 October, detection in samples on 23 October, production halt and recall on 24 October, and resumption of production on 31 October. Raw milk is unpasteurised; its marketability rests on assumptions of process and testing. The outbreak showed where the assumptions' boundaries lay — batches, microbial ecology, sampling rates, the consuming population — failing at commercial scale.

Stop at the decision point: the approval of resumption on 31 October, with the testing regime carried over unchanged. On the table: the post-recall remediation list, the testing sampling scheme, and the epidemiological fact of children's share in the consuming population. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Further cases continued to appear within the resumption period (MMWR coverage extends to March 2024). Primary source: CDC, MMWR Vol.74, 2025; link in Appendix B, ag-001.

## 4 What Shows Earliest

Six weak signals, each with the reason that usually overrides it.

1. The rollout plan contains no section on "what changed compared with the pilot." Override: "the pilot already proved it."
2. Differences are acknowledged verbally ("the users here are different") but never enter the decision record. Override: "everybody knows."
3. The conclusion sentence of the validation report does not state its scope of validity. Override: "who reads that closely."
4. Reuse across models, populations, or regions triggers no re-validation at all. Override: "same principle."
5. A difference item someone pointed out disappears from the meeting minutes. Override: "meeting time is limited."
6. Boundary events (minor anomalies) are explained as "normal fluctuation outside the pilot's scope." Override: "the sample is still small."

## 5 How to Defend

Device one: an extrapolation declaration form. Every act that carries a conclusion outside its validation environment files one form: the original validation's boundary (sample, operating conditions, duration), the target environment's difference list, and item-by-item statements of "why this difference does not affect the conclusion." The items whose impact cannot be explained are precisely the items needing supplementary verification: the form's value is exposing what cannot be explained. The form itself must be archived: it is the raw voucher of "what was known at the time" for any future postmortem.

Device two: independent supplementation of the difference list. The list is drafted by the user and supplemented by the pilot team; the two sides list separately and are not permitted to merge discussions before writing: only by listing separately does the list come out complete (the differences the pilot team knows are often in the user's blind spots, and vice versa). The union of the two lists is the real difference surface.

Device three: the boundary written into the conclusion sentence. The conclusion sentence of every validation report is required to carry its scope of validity ("holds under conditions X"). Downstream citations that strip the boundary count as citation errors and enter the postmortem ledger. What this changes is really a writing habit: only when the boundary is promoted from footnote to body text does its probability of being cited rise above zero.

Device four: graded release. Extrapolation is graded by the item count of the difference list: zero differences, released directly; with differences, verification intensity and monitoring density rise with the item count; where differences touch safety boundaries, direct extrapolation is barred (the three criteria of Chapter 40's exploratory failure connect here: controlled extrapolation requires a declaration, a budget ceiling, and a stop-loss point). The grading's effect is to turn extrapolation from "do it if you can" into "do it by the price list."

## 6 Boundaries with Adjacent Mechanisms

Against the failure zone of expert intuition (Chapter 14): extrapolation is the transportation of conclusions (the data layer); the failure zone is the transportation of the judge (the human layer). When one scene occupies both, check the person first (his experience's premises), then the conclusion (its validation boundary): fixing the person is cheaper; fixing the conclusion is expensive.

Against narrative before evidence (Chapter 13): narrative-first means the conclusion runs ahead of the evidence; boundary extrapolation means the evidence has run beyond its range of validity. The first lacks evidence; the second lacks a boundary declaration. Sizewell's "replication" narrative (Case 2 of Chapter 13) and this chapter's difference list are two faces of one coin.

Against nonlinear scaling (Chapter 24): change of scale is the difference item most commonly overlooked: from a pilot of ten to a rollout of a hundred thousand, the distributions of users, load, and anomalies all change. A change of scale must appear on the first line of the difference list.

## 7 Self-Check: Five Questions

1. Your organisation's most recent "pilot to rollout" — does a difference list exist? Who drew it up? Has the pilot team read it?
2. Validation conclusions you have cited — did the conclusion sentence carry a scope of validity? If not, what boundary did you fill in yourself?
3. The most recent reuse across models, populations, or regions in your field — who was required to re-validate? Was it nobody, or was it nobody?
4. Which of your product's or process's "always done this way" steps have original validation conditions that can no longer be found?
5. Take one of your old validation reports and rewrite its conclusion sentence with the boundary attached. After rewriting, can it still support the current use?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

The extrapolation declaration goes first — it is the gate; promotion and transplantation that bypass it make everything after it moot. Independent supplementation of the difference list follows (it blocks the declarer from grading their own homework), boundary-in-the-conclusion third (a drafting discipline riding the finalization calendar), tiered release last (flow control through the gate: passage allowed, dosed). First ninety days: week one, inventory every promotion and transplantation under way — new line, new region, new population, new stack — and open a declaration for each; weeks two and three, build each difference list and then hand it to someone who was not on the pilot for a third list (what the declarer missed); month two, put boundary clauses into two documents being finalized ("this conclusion holds for... under... conditions"); month three, tier the fastest-moving promotion (first tranche at a few percent, second-tranche promotion criteria, full-rollout acceptance).

Failure modes. Declarations arrive late — the promotion has been running in two regions while the form is in workflow, and the gate is decorative. Bind declarations to budget release: the finance-side check field pays promotion spend only against a filed declaration. Supplementers assimilate (review the same project repeatedly and they learn the declarer's blind spots as their own) — rotate them, preferring people who have never touched the project. Boundary clauses go universal (one all-purpose sentence stapled to every conclusion) — sample-read them: "which words could you delete from this sentence and still sign it" — the deletable words are the empty boundary. Tiers become leaps (tranche two ships before tranche one's data is read) — make the look-back report a promotion attachment; no report, no promotion.

Cost: half a day per declaration including the difference list; half a day per supplementer; clause cost for boundaries; tiers are pacing, nearly free — what they save is the rework of a full rollout gone wrong. Against a reactor that extrapolated bench-scale data to production, a heater that extrapolated lab duty cycles to living rooms, a trocar reused past its validated count, or raw milk legal in one jurisdiction and lethal in practice — the failure point is always the hop where things were assumed alike; declarations and difference lists are the speed bumps on that hop.

Toolchain: the locator treats this as a happening trigger — repeat the table while promotions run. Question set 23's item 1 ("which page holds 'what changed since the pilot'") audits the declaration. Post-mortems with "rollout," "transplant," or "replicated the pilot" in the conclusion dispose through difference-list gaps. And in the thirty-minute walkthrough, a promotion decision is this chapter's regular customer: the scale parameter's upgrade signal is often the extrapolating move itself.

## Quick-Reference Card

**The mechanism in one sentence:** extrapolation beyond the validated domain means using a conclusion that holds inside its boundary as a boundary-free law, while the boundary itself is never listed — let alone declared invalid item by item

**The three criteria, compressed:** 

**The devices (Section 5 has the detail):** Device one: an extrapolation declaration form; Device two: independent supplementation of the difference list; Device three: the boundary written into the conclusion sentence; Device four: graded release.

**The four loudest weak signals (Section 4):** The rollout plan contains no section on "what changed compared with the pilot." Override: "the pilot already…; Differences are acknowledged verbally ("the users here are different") but never enter the decision record…; The conclusion sentence of the validation report does not state its scope of validity. Override: "who reads…; Reuse across models, populations, or regions triggers no re-validation at all. Override: "same principle.".

**Cost register and case index:** ag-001: 致病171例、住院22例、死亡0; av-021: 机上2人全部死亡；机体烧毁; me-002: 患者2次低血糖；全国2017-2022年11例胰岛素过量Never Event; ph-007: 召回2,838件.

**Domain cross-reference:** this chapter's cases live on the Agriculture, Aviation, Healthcare, Pharma domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** Conclusions carry boundaries: at the step past the boundary you need a speed bump, not faith.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "the pilot went perfectly" belongs here; the check action is completing the difference list.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: see Section 6 (read the boundary discussion in Section 6 first). Question set 23 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(First draft: 3,814 Chinese characters; English edition independently written.)
