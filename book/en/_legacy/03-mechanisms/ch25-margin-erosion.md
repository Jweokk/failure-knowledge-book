# Chapter 25: Margin Erosion; Drift into Failure (Dekker)

> What this chapter covers: how margins are eaten bite by bite with nobody seeing the whole; Dekker's drift perspective, three criteria, four field sites, the margin ledger and cumulative-view review.
> When to return: at every cut review, every "just this once" exception request, and the day the system crosses the boundary with no warning at all.
> Reading time: 50 minutes.

No system that comes to grief was pushed over the cliff by a single decision. Dekker (Sidney Dekker) calls its real mode of motion drift into failure: the system drifts into failure — every deviation was lawful under the rules of its moment, every cut passed its review, every "let's manage for now" did in fact hold. The margin is not decided away; it is forgotten away: it has no ledger, no guardian, and has never been looked at as a whole in any meeting. When boundary day arrives, everyone in the room faces a thing that "has never happened before."

## 1 What It Is

Definition: margin erosion means the system's design margins — time, strength, distance, redundancy, room to manoeuvre — are eaten away piece by piece by a sequence of cuts each of which looks harmless alone, while no one holds the cumulative total.

Three trigger criteria (if any one appears, the mechanism has already started):

① Each cut alone is insufficient to cause an incident (the cut's defence speech is usually true);
② Nobody holds the cumulative total: there is no ledger, only each round's instance-level assessment;
③ "Still enough" becomes the basis of decision, and the baseline of "enough" is the state after the previous cut.

Criterion ③ is the mechanism's self-locking structure and deserves to be spelled out: each cut resets the baseline, and the reset baseline becomes the starting point of the next cut. Before the first cut, the margin is the design value; after the tenth cut, the reference frame of the margin has slid to the position of the sixth, and nobody remembers the origin. That is the difference between "margin cut" and "margin eaten": a cut is an action; being eaten is the loss of memory.

## 2 How It Grows

Three generating conditions. Condition one: cost pressure persists. Not one big cut in one crisis, but small and medium cuts in every budget cycle; once pressure becomes normal, cutting becomes normal too, and normalisation dissolves each individual cut's signal value. Condition two: the invisibility of margin. Design margin enters no financial report and earns no revenue; its existence becomes visible only after the fact (when the incident happens). What is invisible has a determined fate under cost pressure; Chapter 29's invisibility of maintenance is this mechanism's asset-side form. Condition three: the regime of instance-level assessment. Every change is assessed only for "this time"; no post, no form, no standing meeting is responsible for stacking history. Each instance-level conclusion may be honest; summed, they are systemic self-deception.

## 3 The Mechanism in Four Domains

### Case 1 (Maritime): Scuppers Narrowed One Change at a Time

ma-009. The twin-rig stern trawler Ocean Way, November 2014, west coast of Scotland. MAIB report (Report 23/2015, reviewed for this book): the fishing vessel capsized and sank; 3 people died and 2 survived. The investigation points to the weight of water trapped on deck: water penned up on the deck pressed the boat over (the report's original text uses entrapped water to describe the role of the deck water); earlier step-by-step modifications to the scuppers made entrapment easier. The liferaft's cradle was jammed and failed to release, and the EPIRB emergency beacon, carrying no GNSS positioning, revealed the vessel's position to searchers only after 47 minutes 〔details of the modifications and the liferaft are in the report body; this review covered the capsizing mechanism and the casualties〕. Each change to the drainage had its own justification; taken together they ate the reserve of stability the whole ship depended on in bad seas — precisely the margin promised to the fishing vessel at design time.

Stop at the decision point: the approval moment of one particular change to the drainage openings. On the table: the functional reason for this change, the fact that daily operations ran normally after it, and a deck-drainage drawing with no cumulative record attached. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Capsized and sunk; 3 people dead. Primary source: MAIB, Report 23/2015, 2015; link in Appendix B, ma-009.

### Case 2 (Chemical): An Undersized Relief and an Absent System

ch-006. Reactor 6 at the Givaudan Sense Colour plant (Louisville, Kentucky), 12 November 2024. CSB final report (released 27 May 2026, reviewed for this book): the reactor underwent a runaway decomposition explosion; vessel fragments flew beyond the plant; 2 people died and 2 were seriously injured. The report's recommendation list marks out three margins that had been eaten away: no reactive testing data (the margin of process safety information — nobody knew how close this chemistry ran to runaway), an undersized emergency relief system (the physical margin — relief capacity mismatched to the runaway's rate), and no process safety management system anywhere in the plant (the organisational margin — no institutional line of defence existed at all). With all three layers of margin absent, nothing caught the runaway when it came.

Stop at the decision point: the two reviews at which the process was established without reactive testing and the relief system was designed to existing parameters. On the table: the historical experience of similar processes, the cost of testing, and the record of "the plant has run for years." 〔Stop point: reader judges first, then turns the page〕〔Outcome〕2 dead, 2 seriously injured; the recommendations point to completing the testing, redesigning the relief, and establishing PSM. Primary source: CSB, Final Report, 2026; link in Appendix B, ch-006.

### Case 3 (Software): Three Security-Control Debts

sw-011. France Travail (the French employment agency). CNIL closing decision (reviewed for this book): fined 5 million euros for inadequate protection of job-seekers' data; the found deficiencies included adviser accounts without multi-factor authentication (MFA), data access rights exceeding what duties required, and a lack of proactive monitoring of tool activity logs — the case closed in September 2026 after remediation. All three are margins: the margin of authentication (a single factor sufficed to log in — the extra factor was skipped), the margin of access (broad rights granted in passing — least privilege was skipped), the margin of logging (records kept but unread — proactive monitoring was skipped). Before the incident, each ran "normally," and each omission had a legitimate reason at the time.

Stop at the decision point: the configuration decision, at the build of the account system, that listed MFA as optional rather than default. On the table: the demand for ease of use, the deployment cost, and the tiering assumption that "only high-risk roles need it." 〔Stop point: reader judges first, then turns the page〕〔Outcome〕A 5-million-euro fine; case closed after remediation. Primary source: CNIL, 2026; link in Appendix B, sw-011.

### Case 4 (Aviation): Margins Whose Disposition Could Not Be Reconstructed

av-015. Reims/Cessna FA150L (I-FFSQ), 1 November 2019, Santa Severa, Italy. ANSV investigation report (Relazione d'inchiesta; PDF reviewed for this book): on approach for a sightseeing flight the aircraft struck power lines, fell to the ground, and burned; the 2 people aboard (pilot and passenger) died (original text: "Le due persone a bordo (pilota e passeggero) perdevano la vita"). The report's honesty lies in its admission: it could not establish why the aircraft was below the height it should have flown on approach. The mechanism of margins being eaten happened in full: altitude margin, track margin, and visibility margin failed one by one, yet the disposition of each step cannot be reconstructed from the evidence left afterwards.

Stop at the decision point: each stretch of the approach in which altitude margin was consumed step by step. On the table: the visual references of the moment, the judgment process of the two people aboard — precisely the part the evidence cannot fully restore. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕2 people dead. This case is the reductio ad absurdum proving the necessity of a margin ledger: if even the investigators cannot reconstruct where the margins went afterwards, the ledger kept beforehand is the only memory there is. Primary source: ANSV, Relazione d'inchiesta I-FFSQ, 2023; link in Appendix B, av-015.

## 4 What Shows Earliest

Six weak signals, each with the reason that usually overrides it.

1. Design margin has no book record; it lives only in the original designer's memory. Override: "it is all on the drawings."
2. Every assessment looks only at the change of the moment; nobody builds the cumulative view. Override: "each one was assessed."
3. "Still enough" has no quantitative basis, or its basis is the state after the last cut. Override: "proven in practice."
4. The list of exceptions and waivers keeps lengthening, and waivers start citing other waivers. Override: "just a special case."
5. The system recovers from disturbances more slowly (the same small faults take longer to clear). Override: "a coincidence."
6. Reports of near misses (almost-an-incident) decline while operating intensity stays unchanged. Override: "safety is improving." (A cognate signal of Chapter 11's criterion.)

## 5 How to Defend

Device one: a margin ledger. Write the system's key margins as cumulative numbers: structural margin, time margin, staffing margin, financial margin — each recording the original design value, the current value, and every change. The ledger's keeper is separated from the cut's applicant (Chapter 17's conflict-of-interest check principle). The I-FFSQ case proves it: without a ledger, reconstruction is impossible even afterwards.

Device two: cumulative-view review. When any cut proposal enters a meeting, the pre-read must contain the margin's historical cut curve: the object of review shifts from "this time" to "this line." The standard of judgment shifts from "is there still enough after this cut" to "how many more cuts does this line allow." The curve's mere existence is a deterrent: whoever cuts on the curve signs a cut with a name attached.

Device three: a minimum water line for margins. For irreversible margins (structure, relief capacity, emergency capacity) set a water line that cannot be crossed and write it into the institution: cuts below the line require the signature of an external independent party (Chapter 7's second-confirmation seat for irreversible points). The water line's design basis is the original design value, not the value from the last review: that is exactly what distinguishes it from "still enough."

Device four: recovery-time monitoring. Take "the system's recovery time from an identical disturbance" as a living indicator of margin: slowing recovery is the early reading of margins being eaten. It needs no knowledge of which cut did the damage; it needs only to know the ship sits lower in the water. Recovery time's baseline must be re-measured and archived on a schedule, or even "it got slower" becomes unstatable.

## 6 Boundaries with Adjacent Mechanisms

Against the invisibility of maintenance (Chapter 29): maintenance debt is "the work that should have been done, not done" (the asset form); eating margin is "the quantity that should have been kept, not kept" (the design form). The two often share cause and effect (Surfside is claimed by both chapters); the criterion is the object: time and actions go to Chapter 29; margin and strength stay in this chapter.

Against procedural drift (Chapter 15): drift moves the distance between practice and text; eating margin moves the distance between the system and its boundary. Drift usually precedes margin eating: practice loosens first, margins get cut after. The two ledgers are best read side by side; the line that loosened first is usually the line cut next.

Against normalisation of deviance (Chapter 11): normalisation supplies margin eating's psychological permit ("nothing happened last time"); this chapter supplies the physical result ("this time there really is not enough"). Chapter 11's criterion ③, "the standard has been quietly lowered," lands in engineering contexts as this chapter's ledger.

## 7 Self-Check: Five Questions

1. Your system's three key margins — is each one's current value and original design value recorded? What is the ratio?
2. At the most recent cut review, did you see "the impact of this one" or "the history of this line"?
3. How long has your exception list grown? How many entries were added last year? Has any ever been deleted?
4. Your system's recovery time from identical small faults — is it lengthening? Is there data?
5. If tomorrow you had to explain to a new successor "how much safety margin this system has left," how many pages could you hand them?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

The margin ledger goes first — uncumulated erosion is rumor; accumulated erosion is risk. The cumulative-view review follows (it makes somebody look at the whole ledger), the minimum-waterline third (a red line drawn on the ledger), recovery-time monitoring last (it governs the world after a breach: how slow, who is stalling). First ninety days: weeks one and two, build the first ledger (design margins line by line — structural, schedule, staffing, financial, buffer — two columns: design value, current value); weeks three to six, hold the first cumulative review (project the erosion curves for governance; most organizations see, in that meeting for the first time, how much a decade ate); month two, draw waterlines for the three thinnest margins (a breach forces a review whose output is a recovery plan or a signed risk acceptance); month three, open recovery monitoring for breached entries (milestones, owners, monthly progress).

Failure modes. The ledger's caliber thins (current values estimated generously — Chapter 12 reborn inside a ledger) — give every update an evidence field: measurement or calculation, or process at the worst-case value. Review cadence collapses (quarterly, to annual, to "not this year") — bind the review to budget season as a standing agenda, sharing the table with Chapter 20's defensive account. Waterlines get redrawn instead of honored (the line blocks, so the line moves) — route any revision up a level: governance signature, stated reason, public record. Recovery drifts forever (milestones rolling month after month into a diary) — attach escalation: two slipped milestones auto-escalate one level, to governance.

Cost: the first ledger runs one to two weeks by system count with hours of quarterly upkeep; half a day per quarter for the review; clause and tracking costs for waterlines and recovery. Against Surfside (a repair gap nobody cumulated, ninety-eight lives), a broken drag chain on a deck, or a cleanup task pushing a main database over a line nobody watched — erosion is harmless every single day, and the ledger's whole purpose is to make a thousand harmlessnesses into one visible number.

Toolchain: the locator triggers on "medium-or-long time pressure plus two or more consecutive cuts"; the first ledger is the opening move. Question set 25's item 3 ("the quantitative basis for 'still enough'") audits the evidence field. Post-mortems with insufficient margin in the chain backfill the erosion curves. And Chapter 40's exploration budget shares this chapter's waterline logic: what can be calculated can be spent calmly — the two ledgers sit side by side at the same budget review.

## Quick-Reference Card

**The mechanism in one sentence:** margin erosion means the system's design margins — time, strength, distance, redundancy, room to manoeuvre — are eaten away piece by piece by a sequence of cuts each of which looks harmless alone, while no one holds the cumulative total

**The three criteria, compressed:** 

**The devices (Section 5 has the detail):** Device one: a margin ledger; Device two: cumulative-view review; Device three: a minimum water line for margins; Device four: recovery-time monitoring.

**The four loudest weak signals (Section 4):** Design margin has no book record; it lives only in the original designer's memory. Override: "it is all on…; Every assessment looks only at the change of the moment; nobody builds the cumulative view. Override: "each…; "Still enough" has no quantitative basis, or its basis is the state after the last cut. Override: "proven in…; The list of exceptions and waivers keeps lengthening, and waivers start citing other waivers. Override: "just….

**Cost register and case index:** av-015: 2人死亡（飞行员与乘客）; ch-006: 死亡2人；2人重伤; ma-009: 3人死亡（1人遗体寻获、2人未寻获；2人生还）.

**Domain cross-reference:** this chapter's cases live on the Aviation, Chemical, Maritime, Software domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** Margins die by thin slices: keep a running total, not a per-meal view.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "there's still margin" belongs here; the check action is the cumulative ledger.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: see Section 6 (read the boundary discussion in Section 6 first). Question set 25 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(First draft: 3,821 Chinese characters; English edition independently written.)
