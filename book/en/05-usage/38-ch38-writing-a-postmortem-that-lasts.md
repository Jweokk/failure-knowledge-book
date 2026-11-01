# Chapter 38 Writing a Postmortem That Lasts

> What this chapter covers: how to turn the case card into a postmortem template; six rewrites set against their originals, paragraph by paragraph; and the record-keeping regime that keeps a postmortem citable three years later.
> When to turn back: when you have to write a postmortem, review someone else's, or discover that nobody can follow the one you wrote three years ago.
> Estimated reading time: 35 minutes.

A postmortem has one test of usability, and the test is a matter of time. Can a new colleague, three years from now, answer three questions from this document alone: what happened, why it happened, what to do if it happens again. A document that answers all three is a live postmortem. One that cannot is a dead file, and dead files outnumber live postmortems in most organizations by a wide margin. The cause is fixed at the moment of writing. They were not designed for the reader three years out. The template and the discipline in this chapter serve that single target.

A postmortem passes through three stages, each with its own reader and its own use. Stage one, the first week after it is written: the reader is the team itself, the use is immediate learning, and the critical item is the replay of the decision point (Chapter 6's two-column discipline). Stage two, three months to a year out: the reader is someone running a similar project, the use is prevention, and the critical item is whether the minimum counterfactual can be executed (Chapter 10's five-step method). Stage three, more than a year out: the reader is the person who inherits the work and the investigator who arrives later, the use is historical truth, and the critical item is the integrity of the numbered evidence chain (Chapter 6's procedural defense). One document, three different requirements. A good postmortem meets all three at once, which means the template has to carry all three by design.

The twelve fields of the case card in Chapter 5 become the section structure of a postmortem directly: ID, one-line summary, subject, when and where, domain and mechanism, what was visible then, options ruled out, decision point, point of no return, scale of consequences, minimum counterfactual, evidence grade and sources. An organization may add or drop fields to suit its own work. The twelve-field skeleton is better left uncut. Cut into it and its postmortems stop being comparable with those of other organizations, and comparability is the precondition for knowledge moving at industry level (Chapter 1).

The other common way to kill a postmortem is to convert it into a blame document. Once a postmortem becomes the basis for punishment, the next one carries no truth (Chapter 19's alarm logic). Chapter 4 has a working model for the institutional design that prevents this, taken from the software case: a blameless principle plus data separation between the review system and the personnel system. What the separation changes is the IT boundary, two systems with two permission groups; it does not delete personnel records. Technical isolation holds where a cultural promise does not (Chapter 19).

A postmortem serves three publics, and the three do not read the same language. Decide who is reading before the first sentence.

Public one is the team. They want the decision point replayed and the next actions named, and the language is concrete: work order numbers, dates, names. Public two is the people who do similar work elsewhere. They were not in the room, they do not know the cast, and what they need is the mechanism in transferable form, in structural language: under which conditions, which mechanism starts. Public three is the investigator or successor three years out. They want the evidence chain, indexed by number, source and material list. Most postmortems serve public one alone, which is why three years later only public one remembers the document, and public one has usually been reassigned.

Each public has a matching writing discipline. For public one, the factual section: two columns, a source on every line. For public two, the mechanism section: the mechanism field plus a paragraph describing the form the mechanism took on site, written the way Section 3 of a mechanism chapter is written. For public three, the evidence section: material list and grade labels, per Chapter 5. The three-part structure of the template in Section 38.2 gives each public one part, which is not a coincidence. The twelve fields were always an event record, a teaching text and an evidence file at the same time.

One more layer of purpose. The knowledge a postmortem produces comes in two kinds: about this event (this project's pothole) and about the mechanism (the general structure under these conditions). The first goes into the project ledger, the second into the organization's case library. The mechanism field is the interface where one turns into the other. Write the event, then abstract its mechanism into one transferable sentence; when the entry moves into the library the particulars can be de-identified and the mechanism kept. Library entries use the Chapter 5 card format, so an internal postmortem and this book's external cases speak one language and exchange without loss.

## 38.1 The Two Fates of a Postmortem

A postmortem that dies the moment it is filed is the normal case: submitted, archived, never opened again. The ones still cited three years later are a minority, and they share three features. The information environment at decision time can be rebuilt, because timestamped material survives. The conclusion traces to one concrete action, because a minimum counterfactual exists. Someone owns the follow-up, because a verifier and a date are written down. This chapter turns the three features into a template and a regime.

The causes of early death are just as clear. The fact layer carries no timestamps, so nothing can be checked. The conclusion layer is made of adjectives, so nothing can be executed. The output layer has no owner, so nothing lands. Three ways to die, three sections of this chapter.

## 38.2 The Twelve-Field Postmortem Template

The twelve fields of the Chapter 5 case card are the postmortem template. Write them in three parts.

Opening section, fields 1 to 5: ID, one-line summary, subject, when and where, domain and mechanism. The section pins the event down and prevents drift in the agreed account. The mechanism field may not be fillable with confidence at postmortem time; a first draft may carry a "suspected" tag and be settled at the monthly revision.

Process section, fields 6 to 9: what was visible then, options ruled out, the decision point, the point of no return. This is the body of the document, written in two columns (Chapter 6), the left column holding what was visible then and the right column holding what was reconstructed afterward. Here sits the one advantage an internal postmortem has over an external case card: you hold the internal material, so you can write the meetings and the signatures in finer grain than any investigation report. That is the whole advantage. Do not spend it on adjectives.

Output section, fields 10 to 12: scale of consequences, minimum counterfactual, evidence grade and sources. The output section of a postmortem adds three items, which makes fifteen fields: the improvement action (one per mode of death, written the way the conclusion page of Chapter 36 specifies), the verifier and the date, and the ledger number (entered into the anomaly ledger, Chapter 8, Device 1).

The file header carries one fixed line of metadata: postmortem date, writer, and the material list, a dated list of files. The material list is the collateral behind the document's credibility, since it is how a reader judges what you actually had in hand. Group the list by evidence grade, A group first, and give each file its export date. Export date and content date are two different timestamps and both are kept: the export date proves that what you reviewed was the version as it stood, not a version updated afterward. The list ends with a gap section, and the honesty of the gap section is the litmus test of the whole document's honesty.

Then the twelve fields one at a time, with the filling rule and the common error for each. The rules are written to the question of who will use this line, and how, three years from now.

Field one, the ID. Issue a number that is never reused; year plus sequence plus subject code is a workable format. The common error is renumbering, where a ledger migration changes the numbers and breaks every old citation. An ID is the document's identity card. Once issued it stays.

Field two, the one-line summary. One sentence, confined to the mechanism, cause words forbidden. "Methyl mercaptan vapour accumulated during tank drainage; four people died" passes. "Accident caused by inadequate management" does not. Cause words belong in the mechanism field. The one sentence pins facts only.

Field three, the subject. Name an organizational unit and a role that can be pointed at, not a department nickname. A reader three years out does not know who "the old platform crew" were. They know "Platform Infrastructure Department, Storage Group".

Field four, when and where. Minutes where the record supports minutes, and a plain statement of the precision where it does not. Ban "recently" and "in the earlier period". Write the time zone and the shift: a night-shift event and a day-shift event are often different mechanisms.

Field five, domain and mechanism. The mechanism name from this book's vocabulary plus the chapter number. Where two mechanisms are plausible, hang both as suspected and note the deadline for settling. The common error is a result label such as "operator error". That is a conclusion. The field wants a process: which two of Chapter 9's three layers broke, and how.

Field six, what was visible then. Every line with a source and a timestamp, left column only. The common error is hindsight leaking in: the writer knows the ending, and the pen slides toward "they should have seen it". Test: cover the right column and read the left. If it reads as wilful disregard, hindsight has entered the text.

Field seven, options ruled out. At least one option, with the reason for exclusion and the moment of exclusion. The common error is writing up the option that only the ending proved best as "what should have been chosen". Judge the exclusion on the information visible then (Chapter 6).

Field eight, the decision point. Write it at the grain of "what was on the table". The common error is writing a calendar day, as in "the decision of 12 September". A decision point is where materials met options, not a square on a calendar.

Field nine, the point of no return. The triggering act and the moment it took effect. The common error is merging it with the decision point. In most events the two sit hours to months apart, and the interval between them is exactly the working window of the defenses.

Field ten, scale of consequences. Numbers plus basis, with the estimation method footnoted. The common error is direct loss alone. Delay cost, trust cost and opportunity cost go in as far as they can be estimated; where they cannot, say that they cannot.

Field eleven, the minimum counterfactual. One action, placed before the decision point, with the conditions it depends on noted. The common error is three actions. Three actions is an improvement list, not a counterfactual.

Field twelve, evidence grade and sources. Grade every load-bearing fact, A to E on the Chapter 5 scale. An internal postmortem holds A-grade material as a matter of course, the original records, which is the surplus it has over an external investigation. Grading makes the surplus visible.

## 38.3 Before and After: Six Rewrites

The passages below are teaching composites. Their sentence patterns are taken from the common forms of real postmortems (no specific organization). Each is rewritten paragraph by paragraph, with a note after the rewrite on what changed and why.

Original one: "At around 14:00 on 12 September 2025, a quality problem occurred in our company's Project X, causing a certain amount of economic loss."

The problem: the time is vague ("around 14:00" is a fact and acceptable; "a certain amount of economic loss" carries zero information). Rewrite: "2025-09-12 14:07 (time recorded on work order X-3312): hollowing and cracking found in the masonry wall on floor 5 of Building 3, Project X, across 42 walls (quality inspection record Q-258, 2025-09-12). Economic loss stated separately under the basis given below." What changed: the vague quantifier became a number with a source; where the basis has not yet produced a figure, the text says it is stated separately rather than parking "a certain" in the slot.

Original two: "Analysis shows the main cause was insufficient safety and quality awareness among the construction crew, together with schedule pressure in the earlier period and weak links in management."

The problem: four evaluations (insufficient awareness, schedule pressure, weak links, main) and zero actions. The rewrite has two columns. Visible then: the crew meeting minutes of 28 August record that masonry work on Building 3 was assigned to a newly transferred crew, with no mock-up demonstration arranged; item 3 of the weekly quality report of 3 September had already flagged mortar joint fill below standard. Reconstructed afterward: teardown inspection confirmed mortar strength below specification (laboratory report L-77). What changed: evaluations became dated evidence; "schedule pressure" landed on a specific scheduling change; what was visible then is separated from what was learned after.

Original three: "The project department attached great importance to the matter and organised rectification at the first opportunity."

The problem: no action, no subject, no date. Rewrite: "12 September 16:30, the project manager signed rectification order R-91; by 15 September, 31 of the 42 walls had been reworked (supervision log, 15 September); the remaining 11 wait on replacement of delivered material and are scheduled for 22 September (owner: [name], calendar milestone 9-22)." What changed: the whole action sequence landed on work orders, logs, signatures and dates.

Original four: "Next, we will strengthen training, improve procedures, tighten supervision, draw lessons across the board, and make sure similar problems never occur again."

The problem: four all-purpose counterfactuals (Section 10.3), which total zero. Rewrite: the minimum counterfactual is that after the flag in item 3 of the 3 September weekly quality report, a re-inspection within five working days as the procedure required (the clause reads "re-inspection shall be carried out"; no re-inspection record was found) would have caught the defect before it spread across the walls. Two improvement actions follow: (1) the re-inspection deadline for flagged weekly-report items goes into the supervisor's weekly checklist (verifier: the chief supervisor's representative, at every weekly inspection); (2) mock-up demonstration for an incoming crew goes into the conditions for starting work (verifier: the project manager, at every start of work). What changed: one minimum counterfactual, changing one action only; two verification actions that can be marked on a calendar; "never occur again" deleted and replaced by ledger tracking.

The four rewrites share one property. None of them adds a fact the original did not contain. They swap adjectives for sources, evaluations for actions, and four directions for one counterfactual. Almost all of a postmortem's information already sits in the raw material. Writing is the act of putting it into a shape that can be checked.

Two more pairs, covering different kinds of event, on the same principle.

A fifth pair (an IT incident). Original: "In the early hours the system jittered; late monitoring alerts allowed the impact to widen; service has been restored." Rewrite: "2025-11-08 02:14 (gateway log, NTP-synchronised), payment gateway connection pool exhausted; order failure rate 63% between 02:14 and 02:41 (sampled from the gateway access log, sampling basis in Annex A). The first automatic alert fired at 02:29 on the failure-rate threshold, before human engagement (duty log 02:33); in the four minutes from alert to engagement, the escalation path on the duty roster pointed to a person who had already left the shift (roster v3, issued 11-07)." What changed: jitter became a failure rate with a sampling basis; the vague complaint about late alerting was broken into a timeline that exposed the real break, an escalation path pointing at someone off duty (Chapter 30, handover rupture).

A sixth pair (a near miss). Original: "A near-injury in the workshop; fortunately nobody was hurt; education was given on site." Rewrite: "2025-10-21 10:52 (workshop CCTV timestamp), line 3 packing station: the palletising robot started without waiting for the confirmation signal and emergency-stopped 0.8 metres from the operator (PLC log). Two earlier unconfirmed starts of the same model are on record (maintenance ledger 9-30, 10-07), both closed as sensor false alarms, neither triggering an interlock check." What changed: "fortunately nobody was hurt" became a distance and a stop record; "education" became a ledger sweep that surfaced the third occurrence of the same deviation (Chapter 11's criterion: the same deviation twice already). The value of a near-miss review lies almost entirely in the sweep. A near miss is the mechanism's free sample, and skipping the sweep voids the sample.

The last two pairs make one further point. Every fact used in the rewrite already existed in a system the organization was already running. What the postmortem lacked was never data. It was the act of putting data onto a timeline.

## 38.4 The Record System: The Postmortem Starts at the Decision

Whether a postmortem is usable three years later was decided at the moment of decision, by what was left behind. Four minimum record-keeping standards.

Standard one: the three-line decision record (Chapter 7). The point of no return, the second-to-last confirmation position, and the information visible at the time. The three lines go into a fixed field of the decision document or the meeting minutes.

Standard two: the minimum standard for minutes. Date, attendance, the order of agenda items, the conclusion and the dissent for each item, and the time of adjournment. Minutes with no dissent column cannot produce "options ruled out". The postmortem then reconstructs them from memory, and memory is grade D evidence.

Standard three: the anomaly ledger, entered and attributed as events occur (Chapter 8, Device 1). The ledger is the postmortem's primitive accumulation. Half the material in a postmortem written three years later comes from the ledger, and none of it from anyone's memory.

Standard four: the register of basis changes (Chapter 8, Device 2). Every adjustment to a measurement basis, a baseline or a standard leaves its own record. The condition a postmortem fears most is "why was it calculated that way at the time" with nobody able to answer. The register is the answer bank.

None of the four is expensive. Each is a fixed field in a document that already exists. In Chapter 4's terms, this is how an organization installs its own devices without waiting for legislation.

## 38.5bis Running the Review Meeting

Writing happens after the meeting, and a badly run meeting poisons the material before anyone writes. Five rules for the meeting itself.

Rule one: lock the materials before the meeting opens. Circulate the material list two days ahead, logs, minutes and ledger extracts included, and accept no oral fact in the room that is not on the list. This blocks the memory contest, in which the loudest voice's version becomes the record.

Rule two: project the two columns. The room's screen carries two columns throughout, the left one holding what was visible then sorted by timestamp, the right one left empty. Every contribution answers one question first: does this go in the left column or the right. Left requires a source. Right gets tagged "after the fact". Chapter 6's writing discipline moves forward into the meeting, at the cost of one repeated question.

Rule three: the decision-point replay. Advance the material to the moment before the decision and stop there. Ask those who were present to answer aloud, under the rules of Section 36.1 and on the left column alone: what would you do. Only then is the ending revealed. This is the one place in the meeting where "if we had it to do again" is allowed, and it is the cheapest classroom a new member will get.

Rule four: the procedural implementation of no-blame. The chair holds two iron rules. Questions address structures. Questions addressed to persons are handed to a separate channel; where the matter is the handling of a specific individual, it goes down the personnel line after the meeting, and the minutes carry four words, "handled on the personnel line". The technical base of those rules is the system separation described at this chapter's opening: two systems, two permission groups. With that in place the chair's rules have institutional backing and do not depend on the chair's personal authority.

Rule five: collect three things before the room empties. A first draft of the mechanism field (suspicion allowed), candidates for the minimum counterfactual (two allowed, one settled after the meeting), and an owner for every improvement action. With those three, the writer has a skeleton. A meeting that ends with none of them was a memorial service.

## 38.4bis The Boundary of Blame

No-blame does not mean no responsibility, and the boundary has to be drawn precisely or the institution will be overturned after the first serious case. The line runs along two sides, intent and capacity. Negligence, process gaps, knowledge gaps, distorted incentives: all of these go into the postmortem, and the accounting targets structure. Deliberate violation, falsified records, working under the influence of alcohol: these go down the personnel line, and the postmortem records the factual chain only, without judging the person. The line is not drawn by the review meeting. Existing instruments draw it (safety regulations, professional codes), and the meeting's job is to write the factual chain to the precision those instruments need for a finding. The boundary has to be explained publicly when the institution goes live: what the postmortem protects is honest error, and the scope of that protection is written as a negative list and posted on the front page of the review system. The list itself defends in both directions at once, against the postmortem turning into a trial and against anyone hiding behind no-blame to shed all responsibility.

The four standards need an implementation path, and the path is to leave the institution alone and change the template. Standard one, the three-line decision record, embeds as a required field in the approval flow: the approval form gains a section headed "declaration of the point of no return", three lines, and the flow does not proceed while it is blank. Standard two, the dissent column, embeds in the minutes template: two fixed lines at the end, "Objections:" and "No objections, confirmed by:". A team whose objection column is permanently empty deserves more suspicion than a team whose column has content. Standard three, the anomaly ledger, embeds in the shift and quality handover sheet: one line, "anomaly entry number this shift", with "none" written where there is none. Standard four, the register of basis changes, embeds in the change process for reports and dashboards: any submission that changes a basis must link to a register entry. All four sit on paperwork that already exists. No permission changes, no new systems, no change to headcount, and a week to roll out. Once rolled out, the supply of raw material for postmortems has a pipeline, and the quality ceiling of every future postmortem was set three years earlier by those four fields.

The evidence grades have a second use inside an internal postmortem: grading the material also exposes the organization's recording habits. Where a postmortem's A-grade share (system logs, original ledgers) is low and its C-grade share (after-the-fact accounts) is high, that finding belongs in the metadata. It says the decision moment left too little behind, and the postmortem rests on recollection. Several postmortems in a row with that shape move the object of improvement up a level, to the record system itself. The grade table therefore doubles as a health check on the record system, which is how the Chapter 5 table gets used inside an organization.

## 38.5 The Quality Check

A postmortem passes ten questions before it is delivered, one line each.

1. Does every statement in the factual section carry a source?
2. Are there separate columns for "visible then" and "reconstructed afterward"?
3. Is the subject of the conclusion section a structure or a person? (Chapter 9: if the subject is a person, send it back.)
4. Is at least one ruled-out option written down?
5. Is the minimum counterfactual a single action?
6. Do the improvement actions map one to one onto the modes of death?
7. Does every action have a verifier?
8. Does the verifier know? (It counts only if they have been asked.)
9. Is the mechanism field tagged with the right name from the vocabulary?
10. Is the metadata's material list complete?

Pass all ten and the postmortem enters the ledger. Fail any and it goes back for rewriting. This is the same table as the thirty-minute procedure in Chapter 36, put to a second use.

A postmortem can also catch the disease of Chapter 13. The first postmortem establishes a narrative, the second cites the first, and three years later the narrative has become fact. Three defenses.

Defense one: the mechanism section must carry a rival-mechanism paragraph. Beside the settled mechanism, list the alternatives that were considered and the reasons they were dropped, written in the manner of Chapter 13's comparison hypotheses. The point is a record of the reasoning rather than a tone of balance: a later reader can re-examine whether the exclusion still holds and, when new evidence appears, knows which direction to reopen.

Defense two: citations of outside conclusions grade down. When a postmortem cites the conclusion of another postmortem, the cited content counts as grade D, a first-party account, whatever grade the original's factual section carried. This is compatible with the Chapter 5 grade table: grade belongs to the form of the material, and retelling never upgrades it. The narrative errors in public events work exactly this way, the wording of the first report fixed by every retelling that follows.

Defense three: a reopening clause, two years after the postmortem is settled. The keeper sweeps, at the two-year mark, the mechanisms still marked suspected, the key conclusions that were downgraded on citation, and the places marked "material gap". New evidence, a log newly released, a new investigation report, a participant willing to talk after leaving the job, triggers a partial reopening. The output of a reopening is an errata page, never a silent rewrite of the original. The errata regime preserves the document's historical truth: the reader can always see the judgment made at the time and the correction that came later, and both are knowledge.

The three defenses share one principle. A postmortem is writing about the past, and writing collapses toward narrative under its own weight. Evidence chains, rival paragraphs and errata pages hold the collapse back on the writer's behalf. The writer's private vigilance is not a mechanism.

## 38.3bis Two Variants: The Near Miss and the Success

The template covers two special objects with two variants.

The near-miss review. It is built like the incident review, with two relaxations and one tightening. Relaxation one: the decision-point material may be incomplete, provided the gaps are stated, since a near miss naturally leaves a thinner record than an accident. Relaxation two: the mechanism may stay suspected longer, since near-miss signals are weak and a forced settlement files the case wrong. The tightening: the ledger sweep is mandatory, as in the sixth rewrite, where prior occurrences of the same class must be traced back. Most of a near-miss review's value lies outside the event itself, in the third confirmation it supplies for its siblings. The intake bar is deliberately low. An incident review passes the ten questions; a near miss passes three (facts sourced, mechanism tagged as suspected, sweep done). A low bar buys volume, and volume is what turns scattered near misses into a pattern.

The success review. A conspicuous project win also deserves a postmortem, and its object is which defenses actually fired. The method mirrors the incident review: the decision-point replay is unchanged, and the conclusion section names which device stopped which path (the deviation ledger entry that caught something under Chapter 11, the live drill that avoided something under Chapter 22). The most valuable output is the other half of the counterfactual. Nothing went wrong: was that luck, or was one specific device doing its job? Only a review can separate the two. An organization that cannot separate luck from defense will copy the luck and cut the defense, which is exactly how the slack of Chapter 20 begins. The success review keeps the twelve fields, with the mechanism field reading "mechanism intercepted" and field eleven rewritten as "minimum defense, verified". Two or three a year gives the defense system a record of its own wins, and at budget review (Chapter 20's question 4) that record is the written evidence that not having an incident counts as output.

## 38.6 Conversion to Case Cards

Writing the postmortem is the first step. Its second life decides how long the knowledge lasts. Conversion into a case card is the main channel: compress the fifteen-field postmortem into a twelve-field case card on the Chapter 5 format and file it in the organization's case library. Three rules govern the trade-offs.

Rule one: de-identify the particulars, keep the structure true. Names become roles ("the duty engineer"); organizational units may survive down to department level; commercially sensitive magnitudes become bands ("losses in the millions"). The floor for de-identification is that the mechanism structure stays undistorted. The intervals in the timeline, the material composition of the decision point and the ruled-out options are the three things most easily smoothed while redacting, and a smoothed case is a dead case. Keep a restoration key, an ID cross-table, in a permission group separate from the library, for internal investigators to restore the identity.

Rule two: re-grade the evidence. A-grade material in the postmortem stays A on the card; oral accounts drop to D on the card. Conversion is a re-grading process, and the pass also corrects the grades the postmortem got wrong.

Rule three: settle the mechanism field. A mechanism left suspected in the postmortem is settled at conversion against the fixed criteria, checked one by one against the starting criteria in the mechanism chapter. A mechanism whose criteria lack evidence stays marked "suspected", with the missing evidence named. A library's search quality rests entirely on the discipline of this field. A case filed under the wrong mechanism is a lost case.

The library's rhythm: quarterly intake (three to five cards chosen from the quarter's postmortems for their second-life value), an annual compilation (aggregated by mechanism, producing the organization's own mechanism distribution), and one reflux line, where the library's cards feed the calibration of Chapter 35's mapping table and the additions to Chapter 37's question library every six months. Postmortem, case card, question library, mapping table: four tools on one data flow, and the postmortem is the source at the head of it.

## 38.7 Governing the Review Archive

Once postmortems accumulate they need governance, and governance has four duties only.

Duty one: the registry. Every postmortem enters one master ledger (ID, subject, mechanism, date, action-verification status). The registry prevents duplicated labor: postmortems of similar events cite each other instead of each rewriting the background.

Duty two: aggregation. Once a year, aggregate by mechanism: which mechanism draws the most postmortems, which has the lowest action-verification rate, which is cited most often three years on. The output is a one-page portrait of the organization's failure patterns, and it feeds the topic list for Chapter 39's rehearsal directly.

Duty three: the three-year test. Each quarter, draw three postmortems at random that have passed their third anniversary, and ask someone who was not involved at the time to answer the opening three questions from the document alone (what happened, why, what to do differently). The share fully answered is the library's survival rate, tracked year by year. This test is the opening standard of this chapter made into an institution, at a cost of one afternoon a year.

Duty four: retirement. A postmortem whose actions are all verified and whose mechanism has entered the case library moves to read-only archive. Read-only is not a grave: the three-year test draws from exactly there.

Registry, aggregation, testing, retirement: about one day's work a quarter in total, and it belongs under the same keeper as Chapter 37's question library.

One last governance point concerns incentives. Postmortem outputs enter no one's appraisal denominator, and postmortem counts are never ranked. The only KPI in postmortem governance that can be published is the survival rate of the three-year test. It is the one measure that reflects quality without putting pressure on the writer, because the pressure lands three years later, when the writer is no longer in the post. That is what keeps the return of blame-ification at bay.

## 38.8 The Writing Budget

One common cause of death is "no time to write". Here is a realistic budget and a division of labor. Small events (no injury, loss under ten thousand yuan): four hours. Medium events (one review meeting, draft within a week): two working days. Large events (cross-department, formally investigated): follow the investigation's rhythm, with the postmortem due within two weeks of the investigation report being settled. Staffing: one writer, preferably someone who sat at the decision but did not own it; one materials clerk, who pulls logs and ledger extracts out of the systems; one chair, who runs the review meeting and executes the ten questions. Three people writing together does not work: a postmortem with three voices reads, three years later, like three people each wrote a section.

The last writing discipline is about honesty. Where you cannot proceed, because material is missing, memories conflict or the mechanism will not settle, write "missing: X here". Fluent speculation filling a hole is forbidden. A reader three years out can forgive a gap. No reader can forgive a hole patched so well it cannot be seen.

## 38.9 The Mirror at Chapter 39

Postmortem and rehearsal are a pair of mirrored tools, and each is clearer against the other. On the time axis, the postmortem follows the event and the rehearsal precedes it; one processes tuition already paid, the other tries to avoid paying it. On the information axis, the postmortem has an ending to lean on and dense material; the rehearsal has no ending, runs entirely on inference, and its output is rough by nature. On the psychological axis, the postmortem has to defend against hindsight, since someone who knows the ending replays the judgment distorted, while the rehearsal borrows hindsight by pretending the ending is known so that criticism rises. One coin, two faces: Chapter 6's discipline is a defense when used in a postmortem and a weapon when used in a rehearsal. On the output axis, the postmortem produces case cards and improvement actions, the rehearsal produces a hazard list and a division of dispositions, and the two outputs should cite each other in the ledger. Where a hazard listed at a rehearsal later becomes a real accident, the postmortem must cite that list and check whether the defense failed or the list was never executed. On the frequency axis, postmortems are driven by events and rehearsals by the calendar, quarterly; calendar-driven tools decay more slowly, event-driven tools depend on a supply of events, and the two complement each other. The sign that a pair has matured in an organization: a postmortem of an accident cites a hazard line from a rehearsal two years earlier, and that rehearsal's disposition column records why the line was not acted on. At that point the tuition loop closes: what the rehearsal could not recover, the postmortem collects, and what the postmortem cannot prevent, the next rehearsal plays out in advance.

## 38.10 Reading Four of the Ten Questions

Four of the ten questions let the most through, so each gets a reading rule.

Question 3, whether the subject of the conclusion is a structure or a person. Read the grammatical subject. "The construction crew's safety awareness was insufficient" has a person as its subject, and goes back. "Mock-up demonstration was not written into the start-of-work conditions" has an institutional act as its subject, and passes. The gray zone ("the duty manager did not confirm against the roster") is judged on one test: could a competent person in that seat have done the same? If yes, keep the sentence; if no, it is a shot at a person.

Question 6, whether the improvement actions map one to one onto the modes of death. Play connect-the-dots. Draw a line from each mode of death in the conclusion section to an action in the output section. Two modes of death sharing one action (usually an all-purpose action of the "more training" kind), or a mode of death with no line at all (found, but nothing is going to be done about it), sends the document back. The exercise takes five minutes, and it catches the commonest half-finished postmortem on the spot, the one whose actions are disconnected from its conclusions.

Question 8, whether the verifier knows. Read the form of the evidence. What counts is the verifier's own confirmation, a message reply, an accepted calendar entry, a signature. The writer's "they should know" does not count. This question exists to catch the courtesy claim, agreement in the room and no knowledge afterward.

Question 10, whether the material list is complete. Judge the honesty of the gap section, not the length of the list. A short list is not the problem. A hidden gap is: a log that should exist and was not exported, minutes that should exist and were lost. State them in the gap section at the end of the list, and only then is the list complete. The gap section is what lets a reader three years later tell which silences belong to missing material and which belong to missing writing.

## 38.11 Calibration Against the Book's Cases

The cases in this book have one more use in the review room: calibration. When the meeting reaches the mechanism section, pull one case card of the same mechanism (Appendix B indexes them by mechanism) and lay it beside your own. Compare how much material stood at your decision point against how much stood at theirs. Check whether your ruled-out options column contains the option theirs contained. Set your scale of consequences beside theirs and count the orders of magnitude between them. The purpose is to stop the mechanism section from sliding back into local exceptionalism ("our situation is different"). Laid side by side, the tables at two organizations' decision points look alarmingly alike, and what differs is usually only the industry's vocabulary. Rotate the calibration case monthly. After six months the room begins to recognize mechanisms on sight, which is the second path to internalizing them, alongside the question pass.

## 38.12 The Banned-Words List

The decay of postmortem writing starts in the vocabulary, which is why the vocabulary gets a list. Seven banned words or phrases, each with its replacement.

One: "insufficient awareness" or "not enough attention paid". An inner state cannot be checked. Name the specific act that was missing ("no mock-up demonstration was arranged"). Two: "further strengthen" or "continuously improve". A verb with no artifact behind it. Replace with an action, a verifier and a date. Three: "certain", "serious" or "major", modifying a loss with no basis. Replace with a number and an estimation method; where no number can be computed, write "basis stated separately". Four: "at the first opportunity". A time adjective. Replace with a timestamp to the minute. Five: "similar problems". A vague scope. Replace with the ledger search string that defines the class ("unconfirmed starts, same model, line 3"). Six: "deep reflection" or "draw lessons across the board". An emotion verb. Replace with the specific sweep it supposedly triggers ("all interlocks of the same model inspected, list in the annex"). Seven: "eliminate" or "never again". An unverifiable promise. Replace with a ledgered acceptance clause ("closed after two consecutive inspection cycles with no entry of the same kind").

Enforcement can be done by machine. Run the seven phrases through full-text search before the ten questions and rewrite every hit. The list will miss variants ("effectively enhance" among them), so a human read follows the machine, and the human has one instruction only: at any sentence describing an inner state, an emotion or a promise, stop and ask for evidence. The list and the ten questions together make up the document's language discipline, and the language discipline is the ground floor. Template and process stand on top of it. Revise the list once a year with the governance cycle: each year's additions come from that year's black questions and from the evasive phrasings that recurred in that year's rejected postmortems, and the list's growth is the history of the organization's language discipline.

## 38.13 Freeze Before Judging

The boundary of blame has one implementation detail left, the sequencing of the two lines. The personnel finding and the writing of the postmortem may run in parallel, but the factual section must be frozen in one version before the personnel finding is made. When the personnel process needs the factual chain, it cites the frozen version, so that the pressure of the finding cannot work backward onto the facts. A hash or a paper signature will do; the form does not matter, the sequence does. Facts frozen first, findings after, and any correction to the postmortem goes through an errata page. The sequencing protects both directions: the person under investigation against a record slowly rewritten, and the writer against the transfer of blame for a verdict ("the version you wrote is what destroyed him"). Boundary plus sequence is what makes the blameless principle stand. It is a procedural promise, and a procedural promise's credibility comes entirely from the record of the procedure being kept. The first exception resets that record to zero.

## Five Self-Checks

1. Take your organization's most recent postmortem and check it paragraph by paragraph against the four rewrites in Section 38.3. How many of its paragraphs are written the way Original One is written?
2. How many files in your postmortem's material list carry timestamps? If the answer is none, the problem began on the day of the decision.
3. Where is the dissent record from your most recent postmortem? Minutes with no dissent column: how much of them do you believe?
4. Of the four record-keeping standards in Section 38.4, which can your organization put in place immediately? The one it cannot, who is blocking it?
5. Can the postmortem you wrote three years ago still answer "why was it decided this way at the time"? For the one that cannot, which record-keeping standard was missing?

The chapter closes here. The whole of this practice compresses back into the three questions it opened with: what happened (the sources and timestamps of the factual section), why it happened (the three-layer structure and the rival-mechanism paragraph of the mechanism section), and what to do if it happens again (one minimum counterfactual plus two actions with named verifiers). Each question has a reader waiting three years out, and a writer who keeps that reader in mind produces a postmortem that does not die. At the level of the organization only one measure is worth carrying: the survival rate of the three-year test. The demand is narrow: a stranger three years later can understand the document and act on it, which is a low bar. It does ask that the writing give up performance at the moment of writing, because performance does not last three years and evidence does. A reader who has come this far in the book carries twenty-four mechanism chapters, thirty-eight devices and one hundred and thirty questions, and all of it becomes an organizational asset only by landing in one concrete postmortem after another. The postmortem is the book's exchange counter: mechanisms convert into actions here, actions into ledger entries, ledger entries into the starting point of someone else three years later. That word, starting point, is this chapter's whole ambition. A postmortem does not try to make the future's decisions in advance. It tries to set the person who comes later one step higher than you stood.

If the answers to the five questions cluster on the last one, what your organization lacks is record-keeping (Section 38.4), and the embedded fields come before any work on writing. If they cluster on the first three, what it lacks is writing discipline (the rewrites in Section 38.3), and the remedy is to take the most recent postmortem and rewrite it paragraph by paragraph as an exercise. Either gap can be closed within a quarter, which is why this tool has the steepest improvement curve in the book. Money spent this month shows this month, and once it shows, the ledger, the case library, the question library and the mapping table all have a common source feeding them.
