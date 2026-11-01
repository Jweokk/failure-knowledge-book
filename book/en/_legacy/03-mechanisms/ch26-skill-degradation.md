# Chapter 26: Automation-Induced Skill Degradation; Out-of-the-Loop

> What this chapter covers: after automation moves the human out of the control loop, how skill and the capacity to take over decay; the criteria, two field sites, and an honest account of the evidence gap.
> When to return: when an automation project is launched, when simulator and hands-on training are cut, or when "the system will handle it anyway" becomes the reason not to practise.
> Reading time: 50 minutes.

Automation and skill degradation form a self-closing loop: the higher the degree of automation, the more the human needs to keep skill sharp for rare takeover moments — and it is automation itself that supplies the reason to cut training: "the system will handle it anyway." With every turn of the loop, whoever happens to be present when the takeover moment arrives is more out of practice, and the takeover moment has precisely been designed by automation to become harder and harder: the system takes over every routine and leaves the entire residue of exceptions to that one person. The case library of this book has an honest shortcoming on this mechanism: the A-grade cases that directly document "takeover failure caused by skill degradation" are concentrated in aviation — and the cause of the shortcoming is itself part of the mechanism (the history of automation in other domains is not yet long enough; takeover failures have not yet entered their investigation regimes). This chapter marks the gap honestly rather than filling it with two or three thin cases.

## 1 What It Is

Definition: once automation has taken over most of the system's running time and most of its routine actions, the human's understanding of the system and manual execution capability decay in step — and the moments automation leaves the human in the loop are precisely the hardest ones. The operator degrades into a monitor; the monitor, after a long stretch of nothing, becomes the person who must take over; and taking over turns out to be the manoeuvre with the fewest lifetime repetitions.

Three trigger criteria (if any one appears, the mechanism has already started):

① The person has not performed a given action for a long time (months to years), yet that action remains essential at the moment of an accident;
② The takeover moment happens to be the hardest moment: automation covers the routine and leaves all of the non-routine residue to the human;
③ The manual and the training assume "the person can do it," but no mechanism ever verifies that they can.

## 2 How It Grows

Three generating conditions. Condition one: automation coverage increases. This is not the disease; it is a choice, and usually the right one. The disease lives in condition two. Condition two: training hours get compressed, and the stated reason for the compression is precisely "the system handles it automatically." Automation both creates the training need (takeover skill) and supplies the justification for cutting the training: the loop closes here, and every turn saves money. Condition three: rare scenarios. Takeover scenarios arrive in real operations on a scale of years; without institutionalised practice, proficiency in them only falls. And every system upgrade changes the interfaces and sequences of takeover, depreciating once more whatever stock the last practice session built.

## 3 Field Sites

### Case 1 (Aviation): The Autothrottle in a Visual Approach

av-031. Asiana Airlines Flight 214, Boeing 777-200ER (HL7742), 6 July 2013, San Francisco. NTSB final report (AAR-14/01; the PDF was downloaded and reviewed for this book): during a visual approach the autothrottle was inadvertently disconnected without the crew noticing, speed and energy management slipped out of hand, and the aircraft sank below the glide path and struck the seawall; 3 of the 291 passengers died, 40 passengers, 8 flight attendants and 1 pilot were seriously injured, and the aircraft was destroyed. The report's core findings run along the automation-and-skill axis: the crew's erroneous mode awareness of the autothrottle state, the low-time first officer's manual handling in a visual approach, and the training system's failure to assure manual flying skills under automation dependence. The report's casualty sentence deserves quotation in full, because it displays the distribution of consequences with precision: "Three of the 291 passengers were fatally injured; 40 passengers, 8 of the 12 flight attendants, and 1 of the 4 flight crewmembers received serious injuries."

Stop at the decision point: the window for noticing the autothrottle's state change during the approach — roughly a minute or more from the change to the seawall. On the table: the mode display on the FMA (flight mode annunciator), the trends in descent rate and speed, the default division of labour between captain and first officer, and the manual flying hours a training system once gave — and never gave. 〔Outcome〕3 dead, 49 seriously injured; the report's safety recommendations pointed to revisions of approach procedures, training, and automation human-machine interfaces, and global regulators subsequently tightened visual-approach and manual-flying training requirements. Primary source: NTSB, AAR-14/01, 2014; link in Appendix B, av-031.

This case demonstrates criterion ③ of this chapter in its most complete form: the manual and the training both assumed "the capacity to take over a visual approach exists," while the stock of that capacity — the first officer's manual approach experience, the captain's grasp of his state — was measured by no mechanism before the day. The test was administered on the seawall of San Francisco airport.

### Case 2 (Software): The Takeover in a Retry Storm

sw-004. The Cloudflare dashboard and API, 12 September 2025. Official deep-dive post-mortem (reviewed for this book): a control-plane fault triggered automatic client retries, the retry storm amplified the fault, and the control plane was unavailable or partially available for about an hour; mitigation was completed by a combination of rate limiting, capacity scaling, and a rollback patch, and the API recovered to 98% availability. This site shows the other face of automation: fault handling itself increasingly depends on a grasp of a set of "hand-feel" judgements — where to set the rate-limit threshold, whom to scale first, how to order the rollbacks. This combination has no simulator; it is practised only in real incidents, and each handler's real incidents arrive on a scale of years. Automation has changed the shape of faults (the retry storm was a compound product of client-side automatic behaviour and a control-plane defect), while the handler's manual craft updates at the slow pace of the human learning curve.

Stop at the decision point: the first few minutes after the storm forms, as the handler picks up the mitigation combination item by item. On the table: several mutually contradictory curves, the rate limit's harm to legitimate users, the new variables a rollback might introduce, and the date of the handler's last comparable combination — possibly years ago. 〔Outcome〕Recovery after about an hour; the post-mortem was distilled into a deep-dive report. Primary source: Cloudflare, 2025; link in Appendix B, sw-004.

### Evidence Gap Note

Validation cases for criterion ① outside aviation (marine autopilots, medical device defaults, operator takeover in industrial control) are for now missing A-grade full texts within this book's collection scope. The cause of the gap is the mechanism itself: in domains where automation has penetrated less deeply, such events have not yet entered investigation regimes in numbers. Supplementary collection directions are listed in Appendix C (regulatory reports and accident databases on automation across domains). The gap is marked honestly and does not affect the generality of the criteria and defences, which derive directly from the long human-factors literature on automation and from the cases above.

## 4 What Shows Earliest

Six weak signals, each with the reason that usually overrides it.

1. Simulator and hands-on training hours decline year by year, in step with automation coverage. Override: "training follows operations."
2. "The system will handle it automatically" appears in the omissions of training materials. Override: "focus on the delta."
3. Minimum manual-execution requirements (such as a pilot's manual take-off and landing quota) exist on paper but have no assessment records. Override: "there is a policy."
4. Post-incident reviews grade the handling of takeover scenarios as "correct but slow." Override: "the result was fine." (The long duration is itself a reading of degradation.)
5. New hires find the system's manual mode unfamiliar, or do not know it exists. Override: "it never gets used."
6. After an automation change (version upgrade, logic adjustment), the takeover plan is not updated in step. Override: "functionally equivalent."

## 5 How to Defend

Device one: a manual quota system. Set minimum-frequency quotas for manual operation of critical systems (the aviation industry's manual flying quota is the mature template), with quota completion as an assessable metric: "can they still do it" is a quantity to be measured, not an assumption to be held. The quota's scenarios must cover the full takeover chain — recognise the anomaly, exit the automation, execute manually, re-engage the automation — with none of the four steps omitted.

Device two: simulator-based takeover scenarios. Rewrite the takeover scenarios from incident post-mortems as simulation exercises (the software industry's game day and chaos engineering are the same species), covering the takeover checklist once each year. The exercises use real post-mortem material, at a cost far below that of real incidents; the exercises' outputs (where people got stuck, who did not know the button) enter the ledger and become the input of the next training round.

Device three: takeover thresholds and cues. The automated system must issue an explicit entry signal for states that "need a human takeover" (mode changes, falling confidence, combinations of multiple alarms), and takeover plans must be bound to and updated with those signals; after every system change, the takeover plan undergoes mandatory re-review (the counter to weak signal 6). The lesson of Asiana 214 takes this form here: a state change must be presented in a way human attention can capture — not as a line of annunciator characters that can be reasonably misread.

Device four: write the automation's knowledge back into the person. Every automation feature ships with a one-pager: what it does, what it does not do, and what you do when it fails; training and recurrent training take this as their standard. The human's understanding of the system is the foundation of takeover capability: without understanding the automation's boundary, takeover begins only after the correct moment has passed; with the boundary understood, takeover can start ahead of time, at the system's limits.

## 6 Boundaries with Adjacent Mechanisms

Against procedural drift (Chapter 15): drift is practice departing from the text (an active fork); degradation is capability departing from the requirement (passive decay). In automated settings the two are each other's cause and effect: the text updates more slowly than the system (drift), and people leave the practice behind along with the system (degradation). After degradation, the distance between field practice and the text exceeds any deliberate deviation.

Against the illusion of redundancy (Chapter 22): automation is often booked as human redundancy ("the system will handle it, no one needs to learn") — and at the moment the human is struck off the defence list, this chapter's mechanism acquires all of its conditions. Whether a person counts as redundant must be answered by Chapter 22's verification standard: was the switchover ever really performed? Was the takeover ever really rehearsed?

Against the failure zone of expert intuition (Chapter 14): degradation is the temporal form of the failure zone: once automation severs feedback, the preconditions of intuition (regularity and feedback) are dismantled systematically. In automated environments, every row of Chapter 14's admission table should fire by default.

## 7 Self-Check: Five Questions

1. When did a compound failure in your system last get taken over by a human? When had the handler last practised before that day?
2. Is your organisation's training-hours curve rising or falling? Which reason is written next to the fall?
3. Does a takeover-scenario checklist exist? When did you last run an exercise built from real post-mortem material?
4. In your automation features' documentation, is "what it does not do" written anywhere? Pick a feature at random and ask a user.
5. If every piece of automation failed tomorrow morning, who on your team could run the machine by hand? How many names are on the list, and what is their average age?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

The manual quota goes first — it is the metering valve that keeps skill alive, simple to rule and quick to show effect. Takeover simulation follows (it trains the most expensive scenario: the moment automation hands the problem back), takeover thresholds and cues third (governing the real takeover's interface and judgment load), and writing automation's logic back into people last (a knowledge device: someone must understand what the system does, and that someone must have a name). First ninety days: weeks one and two, inventory the automation (what is automated, what the old manual skill was, how many hands still hold it) and set quotas per skill by decay speed (monthly for high-risk, quarterly for the rest); weeks three to six, write takeover scenarios into simulation — at least three scripts per system (misbehavior, partial failure, total failure); month two, audit the takeover interface (how the threshold is set, how the cue is given, in what form confirmation comes — three answers, into the operating procedure); month three, run the single-point sweep on automation knowledge (who can explain each system's logic; one name is one risk).

Failure modes. Quotas go through the motions (manual execution transcribed from the automation's own output) — verify truth independently: record manual results separately and discuss every divergence from the machine; the divergence discussion is the whetstone. Simulations age (the system upgraded, the scripts three years old) — trigger script revision on every automation change, Chapter 23's rule. Thresholds swing between jumpy and sluggish (too sensitive and takeovers train wolf-crying; too dull and the window is gone) — keep a tuning log: every adjustment with its data basis, history in the ledger. Documentation drifts (code on v9, manual on v1) — bind versions: deployment version and manual version must match, or the system does not ship.

Cost: quotas cost the manual labor partially given back — typically one to two percent of automation's savings; simulation costs half a day a quarter; the interface is design work; the knowledge sweep, half a day twice a year. Against the takeover failures already in the record and the retry storm that turned a defense into an amplifier — degraded skill bills nothing for years and collects in one moment.

Toolchain: the locator triggers on "high automation plus falling manual practice hours." Question set 26's item 1 ("the mandatory manual frequency, and the last record of it") audits the quota. Post-mortems with "human error under automation" convert to takeover scripts. And in pre-mortems, takeover-class deaths are the hardest to act out — the scripts exist precisely so the pre-mortem does not have to improvise them.

## Quick-Reference Card

**The mechanism in one sentence:** once automation has taken over most of the system's running time and most of its routine actions, the human's understanding of the system and manual execution capability decay in step — and the moments automation leaves the human in the loop are precisely the hardest ones

**The three criteria, compressed:** 

**The devices (Section 5 has the detail):** Device one: a manual quota system; Device two: simulator-based takeover scenarios; Device three: takeover thresholds and cues; Device four: write the automation's knowledge back into the person.

**The four loudest weak signals (Section 4):** Simulator and hands-on training hours decline year by year, in step with automation coverage. Override…; "The system will handle it automatically" appears in the omissions of training materials. Override: "focus on…; Minimum manual-execution requirements (such as a pilot's manual take-off and landing quota) exist on paper…; Post-incident reviews grade the handling of takeover scenarios as "correct but slow." Override: "the result….

**Cost register and case index:** av-031: 机上291名乘客中3人死亡；40名乘客、8名乘务员与1名飞行员重伤; sw-004: 控制面不可用或部分可用约1小时.

**Domain cross-reference:** this chapter's cases live on the Aviation, Software domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** Automation leaves humans the hardest moments: skill needs scheduled reps, like a muscle.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "when it really happens nobody can do it by hand" belongs here; the check action is the manual quota.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: see Section 6 (read the boundary discussion in Section 6 first). Question set 26 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(First draft: 3,554 Chinese characters; English edition independently written.)
