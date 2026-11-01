# Chapter 15: Practical Drift (Snook)

> What this chapter covers: how formal procedure and actual practice fork over the long term without anything going wrong; Scott Snook's drift model, three criteria, four scenes on the ground, and the "align both ends" countermeasure.
> When to return: when the training content and the on-site practice do not match; before you write a new "must be followed" rule; after an audit finds "operations inconsistent with the manual."
> Reading time: 50 minutes.

The hardest thing about practical drift to detect is that in ordinary times it produces no victims at all. Every crew works by the methods it has worked out for itself, and the work gets done well; every checklist gets ticked as procedure requires, and the ticks are all there. Scott Snook, studying the 1994 shootdown of two U.S. Army Black Hawk helicopters by their own fighters, found the terrifying property of this structure: every link of the accident had been running the same way on every day before the accident — both units' actual practices diverged from their respective manuals, and in ordinary times the divergences were absorbed by routine coordination between organizations. Only on that one day, along one accidental chain of events, did all the forks connect head to tail. The name he gave the phenomenon is practical drift: the organization is not sliding into chaos; each unit is drifting toward its own convenience.

## 1 What It Is

Definition: practical drift is the gradual departure of actual practice from formal procedure, the departure persisting for a long time with no one correcting it, until members of the organization take the fork for granted. The departure is not an impulse toward accident. It is a local adaptation to real working conditions: the workload changed, the staffing changed, the tools changed, the manual did not — so reality grew a second way of doing things.

Three activating criteria (the mechanism has started if any one of them appears):

1. Formal procedure and actual practice have forked for a long time, and the fork has considerable history;
2. The fork is taken as the mark of competence: departing from the manual is treated as proof of expertise, while following the manual gets you laughed at as a novice;
3. No one feels they are violating anything, because the rule as written cannot actually be followed by anyone.

The third criterion is the dividing line between drift and ordinary violation, and the reason drift's consequences run heavier: a violator knows what risk he is taking; a drifter does not — the bypassed procedure simply is not in his risk model. The practice the manual describes cannot be executed under the real workload, staffing, and tooling; reality grows a substitute, and the text never catches up. From that day on the organization is in fact running without a manual. No one announces it.

## 2 How It Grows

Four generating conditions. Structural: rules are written by people who are not on the front line, and they are written against the design state — designed staffing, designed tooling, designed business volume — not the operating state. The moment the operating state changes, the rule's applicability conditions quietly lapse. Incentive: following the rule has an immediate cost (slow, cumbersome, breaks rhythm), while the cost of departing is delayed and probabilistic. A rational shop floor always drifts toward the low-cost side, and every single drift really does purchase a current-period gain. Time: drift needs time. Every "let's simplify just this once, this case is special" leaves no record; after years of accumulation the departure is the standard practice, and the veterans have become the guardians of the new deviation. Information: there is no comparison mechanism, so the gap between manual and reality is never measured. The gap gets written either into the training ("actually, this is how we do it") or into the accident report — the first moment it is described precisely is usually after the accident.

Drift's arithmetic property is worth memorizing: a single-point deviation is usually harmless (Chapter 9's rule that "one broken layer alone is a fault, not a failure"). Drift's catastrophic form is several fork points stacking in the same direction along one event chain. In the Snook case, every link viewed alone sat within tolerance; joined together, they constituted exactly one complete fratricide chain.

## 3 The Pattern in Four Domains

### Case 1 (Aviation): The Flight Log, En Route

av-020. An air ambulance helicopter, Eurocopter EC135 P2+ (N558MT), March 9, 2023, Franklin, North Carolina. NTSB final report (Aviation Investigation Final Report ERA23LA147; the PDF has been downloaded and verified for this book): during an air-ambulance mission leg, the crew looked down to verify the flight log; when they looked up, the cloud base had already sunk below the helicopter. During the evasive maneuver it struck trees and subsequently made a forced landing on a road; of the four people aboard, three suffered minor injuries and one was uninjured; the aircraft sustained substantial damage. The report reconstructs a remarkably complete behavior chain: verifying records in flight was a habitual action of this operation's system; the cloud base's descent was gradual; and every step was, at the time, inside tolerance.

Stop at the decision point: the few seconds in flight when the decision is made to look down and check the log. On the desk: a night cockpit, the records in hand to verify, a sky ahead still clear enough — and an operating culture in which handling paperwork en route had long been the default, where nobody felt any tension with the rule about "maintaining visual contact." 〔Outcome〕Struck trees, then the forced landing on a road. Primary source: NTSB, ERA23LA147, 2023; link in Appendix B, av-020.

### Case 2 (Maritime): The Watch Alarm Drowned by Music

ma-002. The fishing vessel Silver Cloud II (WK 80), October 14, 2025, near Lochinver, Scotland. MAIB report (Report 17/2026; the page has been verified for this book): the watchkeeper dozed off during a solo watch and the vessel ran onto rocks; it broke up after grounding and was presumed a total loss; three crew members were rescued by the Royal National Lifeboat Institution (RNLI) with no casualties. The report's key sentence: the vessel was fitted with a watch alarm, and the alarm's sound was masked by music playing in the wheelhouse. The technical defense was present and functioning. What failed was the daily practice around the defense: music had become the standard background sound of the watch, and the volume of the alarm and the volume of the music had never been thought about at the same table.

Stop at the decision point: the ordinary configuration moment when wheelhouse music volume and the watch alarm came to coexist. On the desk: long night watches, an alarm tested monthly and working (so the feeling of "having a defense" was true), and no prohibition anywhere against playing music. 〔Outcome〕Grounding, break-up; no casualties. Primary source: MAIB, Report 17/2026, 2026; link in Appendix B, ma-002.

### Case 3 (Healthcare): The Checklist That Changed Shape

me-001. An NHS orthopedic treatment centre in the UK. HSIB investigation report (Administering a wrong site nerve block, 2018; the archived snapshot has been verified for this book): a nerve block intended for a 69-year-old patient's right-ankle surgery was injected into the wrong leg; the patient came to no harm. The "Stop Before You Block" checklist was in use and was being filled in — but its execution had changed shape: the checklist had evolved from "pause at each item and verify aloud in both directions" into "tick the box in passing"; the verification did not happen as designed. The report gives the national figure: roughly 192 wrong-site surgeries of this kind occur each year. Mr Awcock's escape from harm was luck; the checklist's deformation was structure.

Stop at the decision point: some moment when the checklist slid from "pause-and-verify item by item" to "tick in passing" — a moment that was never decided; it was diluted out of busyness. On the desk: the rhythm of back-to-back surgical cases, the checklist's completion rate on paper, and one thing that had never been measured: verification quality. 〔Outcome〕Wrong-site block, no harm; two safety recommendations issued (2018/012, 2018/013). Primary source: HSIB, 2018; link in Appendix B, me-001 (archived link, grade A−).

### Case 4 (Construction): The Safety Space Filled with Cable

ce-003. Ickenham station, London Underground, March 28, 2025. RAIB report (Report 02/2026; the page has been verified for this book): a passenger fell onto the track and was struck and killed by a train. The recess beneath the platform edge exists to give a person who has fallen onto the track a space to shelter in; the investigation found the recess "full of communication cables," leaving insufficient refuge space. Every cable-laying permit was one small occupation, and the occupation was never reviewed under the heading of "safety space": the engineering approval looked at laying feasibility and cost, and no one attended the meeting representing the safety function.

Stop at the decision point: some sign-off moment when cable laying beneath the platform edge was approved. On the desk: the engineering need for the cable route, the observation that the recess "isn't used in normal times," and an institutional setup that had never listed the recess as protected space. 〔Outcome〕One death; the report pointed directly at the loss of the refuge space. Primary source: RAIB, Report 02/2026, 2026; link in Appendix B, ce-003.

What the four scenes share: the defense did not disappear — it was domesticated. The log still gets checked (only at the wrong moment to look down); the alarm still sounds (only at a volume that loses to the music); the checklist still gets filled in (only the verification does not happen); the recess is still there (only full of cable). Drift does not demolish defenses. Drift strips defenses of their working conditions.

## 4 What Can Be Seen Earliest

Eight weak signals, each with the reason it is usually steamrolled by.

1. The practice taught in training differs from the practice on the floor, and both sides know it. The reason it gets waved off: "Training teaches principles; the floor teaches reality."
2. Newcomers are taught by the veterans, not by the manual. Reason: "Learning from the experienced is most effective."
3. Some step of the manual has never once been executed in reality, yet still appears on every compliance checklist. Reason: "Better to have it written than not."
4. The floor's verdict on the manual is "that one was written for the auditors." Reason: "Everyone understands."
5. When workload rises, the first things to be simplified are the pause-type actions in the process (verification, read-back, waiting). Reason: "Efficiency."
6. An audit finds "operations inconsistent with the manual," and the response is to change the floor without changing the manual — or to change the manual without asking the floor. Reason: "One of the two has to give." (The correct action: align both ends first, then decide.)
7. Two demonstration versions of a key action exist — the "plant version" and the "floor version" — and newcomers are told to watch the floor version. Reason: "The manual is out of date; don't learn it wrong."
8. The person who signed off a procedure cannot name the last accident or risk the procedure was written against. Reason: "Compliance requires it."

Items 3 and 8 together are the late-stage indicator of drift: the procedure has lost both its executability and its reason for existing, and retains only its ceremonial status.

## 5 How to Prevent It

Device one: manual-versus-reality comparison. Every six months, write the manual steps of key processes and the actual practices side by side, as a list of differences (the audit-trail regime of Chapter 38 supplies the material). Each difference is either fixed in the manual (conceding that reality does it better) or fixed in the process (giving reality the resources it lacks). Only one action is forbidden: not comparing. The comparison meeting's signatories are the process owner plus one front-line representative; missing either side, the comparison slides into one-sided text editing.

Device two: list-protected pause actions. All "pause-type actions" in a process — verifications, read-backs, visual confirmations, wait-for-acknowledgment steps — are listed in their own register, and any simplification request must pass review item by item, with the default answer being no. Drift eats pause-type actions first, because a pause's output is "the thing that did not happen" (the bookkeeping method of Chapter 20 is reused here: every problem a pause catches gets logged).

Device three: a space-dimension register for occupation approvals. For every physical space in a facility that carries a safety function — refuge recesses, evacuation routes, maintenance clearances, headroom — establish a protected-space ledger; every occupation goes through an independent approval, and the approving party is separate from the using party. The direct countermeasure for the Ickenham case: at every concession of the recess, someone attends representing "the future person on the track."

Device four: resource clauses attached to rules. Every mandatory procedure ships with a statement of its execution cost — time consumed, manpower required, tooling needed — and whenever the procedure changes, the statement is re-checked against the floor's actual workload. Writing a rule nobody can execute is pre-spending one drift. The point of the resource clause is to surface "this cannot be executed" on the signing table, rather than three years later in an accident report.

## 6 Boundaries with Adjacent Mechanisms

Versus normalization of deviance (Chapter 11): drift describes the existence of the fork (how the work is done has changed); normalization describes the fork being re-filed (how it is judged has changed). Drift can exist without normalization: a fork watched by the ledger stays in "remediation by deadline" status. Normalization usually takes drift as raw material but requires the second step — explain, then file. Processing order: align first (this chapter), then guard the archive (Chapter 11).

Versus compliance without safety (Chapter 32): compliance without safety is every check passing while the whole remains at risk (the inspection system and the real risk have come apart); practical drift is the fork between text and practice (the document and the behavior have come apart). The Ickenham recess occupies both banks: the occupation went through engineering approval (compliant), while the safety function was already gone (unsafe). When filing a case, classify by the triggering mechanism and cross-list the residual ones.

Versus automation and skill degradation (Chapter 26): drift is human practice departing from text; degradation is the decay of the human ability to execute the existing actions. Rising automation accelerates both at once: the text updates more slowly than the system (drift), and people leave practice along with the system (degradation). In automated environments, drift takes a special form as well: the system's own configuration forks from the text, and there is no "veteran" left to notice.

## 7 Self-Check: Five Questions

1. Write down three differences between "what the manual says" and "what is actually done" in your process. If you cannot write them — is it that you do not know, or that there are no differences?
2. In your organization's checklists, which item do you know has never genuinely been executed? Is it still on every form?
3. The most recent process simplification: which kind of action did it cut — output-type or pause-type? When the pause-type was cut, was there a ledger entry?
4. Which of your floor's rules are "written so that nobody can follow them"? Take three of them: do you dare initiate a comparison revision?
5. Do protected spaces — physical or procedural — have a ledger in your organization? When was the most recent occupation?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

The manual-versus-practice diff goes first — it is the probe, and every later action aims at what the diff surfaces. Pause-action protection follows (it guards the most expensive class of differences), then spatial caliber and resource clauses by domain (occupied-space organizations install the former first; rule-bloated ones the latter). First ninety days: weeks one to three, diff three key processes (chosen for proximity to irreversible points, or for mutual complaints between training and the floor), producing a difference list; month two, dispose of every difference one of two ways — fix the manual or fix the reality; the only banned outcome is non-disposal, with signatures on the disposal record; month three, build the pause-action register: every verify, read-back, and eyeball-confirm across key processes, listed to become the standing basis for judging future simplification requests.

Failure modes. The diff turns into theater — the floor performs a script for audit day and the output is all green. Counter it with randomized timing and material sampling: draw diff evidence from daily records (ledgers, system logs, shift handovers), never from staged demonstration. Pause protection swells into list bloat (every action claims pause status; simplification approvals bottleneck; the floor routes around them), so hold an admission bar: only pause actions with inspectable outputs enter the register — protect verification strength, not action count. Spatial caliber gets captured (the occupier co-signs every occupancy), so separate the approver's appraisal from the user's and verify the register physically once a year — entries on the drawing but absent on the ground are capture, documented. Resource clauses rot (workloads moved, cost notes didn't), so refresh cost notes with every procedure change, bound like a caliber registration.

Cost: half a day to a day per process per diff; two to three days one-time for the pause register; clause-level costs for space and resources. About forty hours a year at two diffs over four processes. Against Ickenham (a refuge space lost to compliant occupations), the wrong-side nerve block, or the trawler aground with its watch alarm under the music — drift's cost curve is flat at zero in quiet periods and one enormous lump at payoff; the diff is what moves the payoff-date arithmetic into the quiet periods.

Toolchain: the locator triggers on "short time pressure plus rules mismatched to workload"; three diffs are the opening move. Question set 15's item 1 ("when was the last diff") audits Device 1 directly. Post-mortems that surface "practice differed from the manual" dispose through Device 1's two-way choice; and in pre-mortems, drift-class deaths almost always convert to diffs — the pre-mortem finds the fork, the diff measures it. The two form a pair.

## Quick-Reference Card

**The mechanism in one sentence:** practical drift is the gradual departure of actual practice from formal procedure, the departure persisting for a long time with no one correcting it, until members of the organization take the fork for granted

**The three criteria, compressed:** Formal procedure and actual practice have forked for a long time, and the fork has considerable history; / The fork is taken as the mark of competence: departing from the manual is treated as proof of expertise, while following the manual gets you laughed at as a novice; / No one feels they are violating anything, because the rule as written cannot actually be followed by anyone

**The devices (Section 5 has the detail):** Device one: manual-versus-reality comparison; Device two: list-protected pause actions; Device three: a space-dimension register for occupation approvals; Device four: resource clauses attached to rules.

**The four loudest weak signals (Section 4):** The practice taught in training differs from the practice on the floor, and both sides know it; Newcomers are taught by the veterans, not by the manual; Some step of the manual has never once been executed in reality, yet still appears on every compliance…; When workload rises, the first things to be simplified are the pause-type actions in the process….

**Cost register and case index:** av-020: 机上4人中3人轻伤、1人未受伤；机体重大损坏; ce-003: 1人死亡; ma-002: 无人伤亡（3名船员由RNLI救起，原文核实）；船舶推定全损; me-001: 患者本人无伤害；全国年度约192例错部位手术.

**Domain cross-reference:** this chapter's cases live on the Aviation, Construction, Maritime, Healthcare domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** Drift produces no victims in peacetime; guard against it with comparison, never with vigilance.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "everyone actually does it this way" belongs here; the check action is scheduling a manual-versus-practice diff.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: Normalization Of Deviance (Ch. 11), Compliance Without Safety (Ch. 32), Automation And Skill Degradation (Ch. 26) (read the boundary discussion in Section 6 first). Question set 15 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(Chinese source: expanded and synced; English edition: about 3,523 words)
