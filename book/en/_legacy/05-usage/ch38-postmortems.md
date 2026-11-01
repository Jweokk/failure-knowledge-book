# Chapter 38: How to Write a Postmortem That Still Works Three Years Later

> What this chapter covers: how to turn the case card into a postmortem template; a paragraph-by-paragraph rewrite of a "strengthen management"-style postmortem; and the record-keeping system that keeps a postmortem citable three years later.
> When to return: when you are about to write or review a postmortem, or when you discover that nobody can make sense of the one you wrote three years ago.
> Reading time: 35 minutes.

## 1 The Two Fates of a Postmortem

For a postmortem to die as soon as it is finished is the norm: submitted, filed, never opened again. The postmortems that can still be cited three years later are a minority, and they share three features: the information environment at decision time can be reconstructed (timestamped materials exist), the conclusions trace back to one concrete action (the minimal counterfactual exists), and someone owns the follow-up (a verifier and a date exist). This chapter turns those three features into a template and a system.

Read the other way, the causes of early death are just as clear: the fact layer has no timestamps (nothing can be verified), the conclusion layer is all adjectives (nothing can be executed), and the output layer has no responsible person (nothing can land). The three deaths correspond to the chapter's three sections.

Three publics, three registers. A postmortem serves three audiences whose needs differ, and writing begins by choosing for whom.

Public one, the team itself: they need the decision point replayed and the next actions named; the register is concrete — work-order numbers, dates, names. Public two, the people who will run similar projects: absent from the scene, strangers to the cast, they need the mechanism in transferable form; the register is structural — under which conditions, which mechanism starts. Public three, the investigator or successor three years out: they need the chain of evidence; the register is the index — numbers, sources, the material list. Most postmortems serve only public one, which is why three years later only public one remembers them — and public one has usually rotated out.

The three publics map onto the template's three parts: write the factual part for public one (two columns, sources cited), the mechanism part for public two (a paragraph of field-form description, in the manner of the mechanism chapters' Section 3), the evidence part for public three (material list and grades, per Chapter 5). The template's design already carries all three — the twelve fields are simultaneously an event record, a teaching text, and an evidence file.

One more layer: the knowledge a postmortem produces comes in two kinds — about this event (this project's pothole) and about the mechanism (the general structure of this class of failure). The first goes to the project ledger; the second goes to the organization's case library. The mechanism field is the conversion point between them: once the event is written, abstract its mechanism into one transferable sentence; what enters the library may be de-identified in its particulars but keeps its mechanism intact. Library entries use the Chapter 5 card format, so internal postmortems and this book's external cases speak one language and interchange without loss.

## 2bis Filling the twelve fields: discipline per field

Each field's guidance, written to the question "who will use this line, how, in three years."

Field 1 (ID): issue a number never reused — year, sequence, entity code. The common failure is renumbering after a system migration, which breaks every old citation. An ID is a birth certificate, not a file name.

Field 2 (one-sentence statement): one sentence, mechanism-neutral, no cause words. "Methyl mercaptan accumulated in the building during a transfer, four workers died" — yes. "Accident caused by inadequate management" — no; causes belong in the mechanism field, and the sentence pins facts only.

Field 3 (subject): identifiable organizational units and roles, not nicknames. Three years out, nobody knows who "the old platform team" were; "platform infrastructure, storage group" survives.

Field 4 (time and place): to the minute where the record supports it; state the precision where it does not. Ban "recently" and "in the period before." Write the shift; night-shift failures and day-shift failures are different mechanisms wearing one date.

Field 5 (domain and mechanism): the book's mechanism name plus chapter number; two suspects allowed at first draft with a deadline for settling. The common failure is hanging a result-label ("operator error") — that is a conclusion; the field wants a process (which two of Chapter 9's three layers broke, and how).

Field 6 (visible at the time): every line with a source and timestamp, left column only. The standard failure is leakage from hindsight: the writer knows the ending, and the pen drifts toward "they should have seen." Test: cover the right column and read the left. If it reads as "knowingly reckless," the left column is contaminated.

Field 7 (options excluded): at least one, with the reason and the moment of exclusion. The failure is writing "should have chosen" for options whose merits only the ending revealed — evaluate the exclusion against the then-visible information (Chapter 6).

Field 8 (decision point): at the grain of "what was on the table." The failure is writing a calendar day ("the decision of Sept. 12") — a decision point is where materials met options, not a square on a calendar.

Field 9 (irreversible point): the triggering act and the moment of effect. The failure is merging it with the decision point: in most events the two sit hours to months apart, and the gap between them is exactly the working window of every defense.

Field 10 (toll): numbers plus口径 — plus, in English, a stated basis. Direct losses at minimum; delay, trust, and opportunity costs where estimable; where not estimable, say so. Never "significant losses."

Field 11 (minimal counterfactual): one action, before the decision point, with its conditions noted. The failure is writing three actions — that is an improvement list, not a counterfactual.

Field 12 (evidence grades): grades on every load-bearing fact, per Chapter 5's A to E. Internal reviews hold natural A material (system logs, original ledgers) — the surplus over an external investigation; grading makes the surplus visible.

The header carries one line of metadata: postmortem date, author, and the material list — a dated list of files. Group the list by evidence grade, A first, and give each file two timestamps: content date and export date. The export date proves you reviewed the version as it stood, not as later updated. The list ends with a gap section, and the honesty of the gap section is the litmus of the whole document's honesty.

## 2 The Twelve-Field Postmortem Template

The twelve fields of the case card from Chapter 5 are directly a postmortem template, organized into three sections when a postmortem is written:

Opening section (fields 1–5): ID, one-line summary, subject, time and place, domain and mechanism. This section pins the event down and prevents drift in the agreed account. The mechanism field may not be fillable with confidence at postmortem time; a first draft is allowed to carry a "suspected" tag, to be finalized at the monthly revision.

Process section (fields 6–9): what was visible at the time, the options excluded, the decision point, the irreversibility point. This is the body of the postmortem, written in two columns (Chapter 6): the left column for what was visible at the time, the right for post hoc reconstruction. Here lies the difference between an internal postmortem and an external case card: you hold the internal materials and can write the meeting and signature records in finer detail than any investigation report. That is the only advantage — do not waste it on adjectives.

Output section (fields 10–12): magnitude of consequences, the minimal counterfactual, evidence grade and sources. The output section of a postmortem adds three more items, making fifteen fields: the corrective action (one per mode of death, written the way Chapter 36's conclusion page specifies), a verifier and a date, and a ledger number (entered into the anomaly ledger, Chapter 8, Device One).

The file header carries one fixed line of metadata: postmortem date, author, and the materials list (a dated list of documents). The materials list is the collateral for the postmortem's credibility: it is how readers judge what you actually had in hand.

## 3 A Rewrite, Paragraph by Paragraph

The passages below are teaching composites; their sentence patterns are drawn from the common forms of real postmortems (no specific organization). Each is rewritten paragraph by paragraph, with a note after each rewrite on what changed and why.

Original one: "At approximately 14:00 on September 12, 2025, a quality problem occurred on our company's Project X, causing a certain amount of economic loss."

The problem: vague time (the "approximately 14:00" is a fact and acceptable; "a certain amount of economic loss" carries zero information). Rewrite: "2025-09-12 14:07 (time recorded on work order X-3312): hollow and cracked masonry walls found on floor 5 of Building 3, Project X, affecting 42 walls (quality inspection record Q-258, 2025-09-12). Economic loss to be stated separately under the method described below." What changed: a vague quantifier replaced by a number with a source; where the loss figure could not yet be computed under a stated method, that is said outright — no "certain amount" standing in as a placeholder.

Original two: "Analysis found that the main causes were insufficient safety and quality awareness among construction personnel, compounded by schedule pressure in the earlier phase and weak links in management."

The problem: four judgments (insufficient awareness, schedule pressure, weak links, "main") and zero actions. The rewrite has two columns. Visible at the time: the crew meeting minutes of August 28 record that masonry work on Building 3 was assigned to a newly transferred crew, with no model demonstration section arranged; item 3 of the September 3 weekly inspection report had already flagged mortar-joint fill below standard. Reconstructed after the fact: teardown inspection confirmed insufficient mortar strength (laboratory report L-77). What changed: judgments replaced by dated evidence; "schedule pressure" pinned to a specific crew-assignment change; what was visible at the time separated from what was learned after.

Original three: "The project department attached great importance to the matter and organized rectification immediately."

The problem: no action, no subject, no date. Rewrite: "16:30 on September 12, the project manager issued rectification order R-91; on September 15, rework of 31 of the 42 walls was completed (supervision log, September 15); the remaining 11, held pending replacement of delivered materials, are scheduled for September 22 (responsible person: [name], calendar milestone 9-22)." What changed: the whole action sequence landed on work orders, logs, signatures, and dates.

Original four: "Going forward, we will strengthen training, improve our systems, intensify oversight, draw broader lessons, and ensure that similar problems never happen again."

The problem: four all-purpose counterfactuals (Chapter 10, Section 3), which amount to zero. Rewrite: the minimal counterfactual is that after item 3 of the September 3 weekly inspection report, a re-inspection within five working days as the procedure requires (the clause reads "re-inspection shall be performed"; no re-inspection record was found) would have caught the defect before it spread across the walls. Two matching corrective actions: (1) a re-inspection deadline for flagged weekly-report items is added to the supervisor's weekly checklist (verifier: the chief supervisor's representative, at every weekly inspection); (2) the model demonstration section for newly arriving crews is written into the conditions for starting work (verifier: the project manager, at every start of work). What changed: one minimal counterfactual (changing one action only); two verification actions that can be marked on a calendar; "never happen again" deleted and replaced by ledger tracking.

The common property of the four rewrites: none adds a fact the original did not contain. It only swaps adjectives for sources, judgments for actions, and four directions for one counterfactual. Nearly all of a postmortem's information already sits in the raw materials; writing is just the act of putting it into a shape that can be checked.

## 3bis Two more rewrites

A fifth pair (an IT incident). Original: "In the early hours the system experienced jitter; delayed alerting allowed the impact to widen; service has been restored." Rewrite: "2025-11-08 02:14 (gateway log, NTP-synced), payment-gateway connection pool exhausted; order-failure rate 63% from 02:14 to 02:41 (sampled from gateway access logs; sampling basis in Annex A). The first automatic alert fired at 02:29 on the failure-rate threshold, ahead of human engagement (duty log, 02:33); in the four alert-to-engagement minutes, the escalation path on the roster pointed to a person who had rotated off (roster v3, signed 11-07)." What changed: "jitter" became a rate with a sampling basis; "delayed alerting" dissolved into a timeline that exposed the real break — an escalation path pointing at an empty chair (Chapter 30's territory).

A sixth pair (a near miss). Original: "A near-injury occurred in the workshop; no one was hurt; personnel were educated on site." Rewrite: "2025-10-21 10:52 (CCTV timestamp), line 3 packing station: the palletizer started without awaiting the confirm signal and emergency-stopped 0.8 meters from the operator (PLC log). Two prior unconfirmed starts of the same model are on record (maintenance ledger 9-30, 10-07), both closed as sensor false alarms, neither triggering an interlock check." What changed: "no one was hurt" became a distance and a stop record; "educated" became a ledger sweep that surfaced the third occurrence of the same deviation (Chapter 11's criterion: twice already, and counting). A near miss's value lives almost entirely in the sweep: a near miss is the mechanism's free sample, and skipping the sweep voids the sample.

Both pairs make the same point: every fact in the rewrite already existed in a system the organization was already paying for. What the postmortem lacked was never data; it was the act of putting data on a timeline.

## 4bis Embedding the four standards: templates, not resolutions

The four minimum traceability standards land not as policy but as fields in documents that already exist. Standard one (three-line decision record) becomes a required section on the approval form — "irreversibility declaration," three lines, blank blocks the flow. Standard two (objection column) becomes two fixed lines on the minutes template — "Objections:" and "No objections, confirmed by:"; a team whose objection column is permanently empty should be watched more closely than one with content. Standard three (the anomaly ledger) becomes one line on the shift and QC handover sheet — "anomaly entry No. this shift" (or "none"). Standard four (caliber registration) becomes a forced link in every reporting change: any change to a metric's caliber must reference a registration entry. Four embeds, all on existing paperwork — no new permissions, no new systems, no new headcount; a week to roll out. After rollout, the postmortem's raw material has a supply line, and the quality ceiling of every future review was fixed, for better or worse, by these four fields.

The evidence-grade table doubles as an X-ray of the record culture. If a review's A-grade share (system logs, original ledgers) is low and its C-grade share (after-the-fact accounts) high, that finding belongs in the header metadata: the decision moment left too little behind, and the postmortem stands on recollection. Several consecutive reviews with that shape upgrade the finding: the traceability standards themselves are the patient. The grade table, in organizational use, is a health check on the record system — Chapter 5's table, turned inward.

## 4 The Record System: The Postmortem Begins at the Moment of Decision

Whether a postmortem is usable three years later depends on what was left behind at the moment of decision. Four minimum record-keeping standards:

Standard one: the three-line decision record (Chapter 7). The irreversibility point, the second-to-last confirmation position, and the information visible at the time. The three lines go into a fixed field of the decision document or the meeting minutes.

Standard two: the minimum standard for meeting minutes. Date, attendance, order of agenda items, the conclusion and the dissents for each item, and the time of adjournment. Minutes without a dissent column cannot produce "options excluded"; the postmortem must then reconstruct them from memory, and memory is grade-D evidence.

Standard three: the anomaly ledger, registered and attributed as events occur (Chapter 8, Device One). The ledger is the primitive accumulation of the postmortem: half the material of a postmortem three years later comes from the ledger, not from anyone's memory.

Standard four: registration of changes in measurement definitions (Chapter 8, Device Two). Every adjustment to a metric definition, a baseline, or a standard leaves its own record. The operating condition a postmortem fears most is "why was it calculated this way at the time" with nobody able to answer; the definitions register is the answer bank.

None of the four standards is expensive: each is a fixed field in documents that already exist. In the terms of Chapter 4, this is the path by which an organization installs its own devices without waiting for legislation.

## 4ter Running the meeting

Writing is afterwards; a badly run meeting poisons the material before any writing. Five rules.

Rule one: lock the materials before the meeting. Circulate the material list two days ahead (logs, minutes, ledger extracts); no oral fact enters the record unless it was on the list. This chokes off the memory contest in which the loudest voice's version becomes the record.

Rule two: project the two columns. The screen shows the left column — visible-at-the-time, sorted by timestamp — with the right column empty. Every contribution answers one question first: left column or right? Left needs a source; right is tagged "after the fact." Chapter 6's writing discipline, moved forward into the meeting, at the cost of one repeated question.

Rule three: replay the decision point. Advance the material to the moment before the decision and stop. Those who were present answer, under 36.1's rules and on the left column alone: what would you have done? Only then is the ending revealed. This is the meeting's single licensed "if only," and its cheapest classroom.

Rule four: no-blame, implemented procedurally. The chair holds two iron rules: questions address structures; questions addressed to persons transfer, in the room, to a separate channel — the minutes carry four words, "handled on the personnel line." The rules stand on the system separation described at this chapter's opening: two systems, two permission groups. Procedural backing, not the chair's personal authority, is what makes the rules survive a hard case.

Rule five: leave with three artifacts. The mechanism field's first draft (suspicions allowed), a minimal-counterfactual candidate (two allowed, one to be settled within the week), and an owner for every improvement action. A meeting that ends with none of the three was a memorial service.

## 4quinq The boundary of blamelessness

No-blame does not mean no responsibility, and the boundary must be drawn precisely or the first ugly case will overturn the institution. The line runs on intent and capacity. Negligence, process gaps, knowledge gaps, incentive distortions: all go into the postmortem, and the accounting targets structure. Deliberate violation, falsified records, working impaired: these go down the personnel line, and the postmortem records the factual chain only, without evaluating the person. The line is not drawn by the meeting; existing instruments draw it (safety rules, professional codes), and the meeting's duty is to write the factual chain to the precision their adjudication requires. Announce the boundary when the institution launches, with the negative list posted on the postmortem system's front page — protecting "honest error" in general terms protects nothing. The posted list defends in both directions at once: against the postmortem becoming a tribunal, and against anyone sheltering behind no-blame to disclaim everything.

One sequencing rule completes the design: freeze before judging. The factual section is frozen — hashed or signed on paper, either serves — before the personnel process draws on it, so that adjudication pressure can never revise the facts. The freeze protects both ways: the investigated party against a slowly rewritten record, and the writer against inheriting blame for the verdict. Boundary plus sequencing plus the freeze is what lets no-blame survive contact with a real case: it is a procedural promise, and a procedural promise's credibility is exactly its record of being kept — one breach resets it to zero.

## 4quater A banned-words list for postmortems

The decay of a postmortem culture begins in its vocabulary, so the vocabulary gets a list: seven bans, with replacements.

One: "insufficient awareness" / "not enough attention" — inner states cannot be verified; name the missing act instead ("no pilot piece was scheduled for the new crew"). Two: "further strengthen" / "continuously improve" — verbs without artifacts; replace with action plus verifier plus date. Three: "serious" / "major,"修饰 losses without a basis — a number with an estimation method, or "basis to be stated separately." Four: "immediately" / "at once" — time adjectives; write the timestamp to the minute. Five: "similar incidents" — vague scope; write the ledger search ("unconfirmed starts, same model, line 3"). Six: "deep reflection" / "draw inferences widely" — emotion verbs; write the concrete sweep they supposedly trigger ("all interlocks of the model inspected; list appended"). Seven: "never again" — an unverifiable promise; replace with a ledgered closure condition ("two consecutive inspection cycles with no new entries closes the item").

Enforcement is mechanical: run the seven phrases through full-text search before the ten-question check, and rewrite every hit. The list will miss variants ("effectively enhance"), so after the machine, one human pass with a single instruction: stop at any sentence of inner state, emotion, or promise, and demand evidence. The list and the ten questions together are the postmortem's language discipline — the ground floor on which templates and protocols stand. Revise the list annually with the governance cycle: each year's new bans come from the year's evasions, and the list's growth history is the history of the organization's honesty.

## 5 The Postmortem's Quality Check

Before a postmortem is delivered it passes ten questions, one line each:

1. Does every statement in the fact section carry a source? 2. Are there separate columns for "visible at the time" and "reconstructed after"? 3. Is the subject of the conclusion section a structure or a person? (Chapter 9: if the subject is a person, send it back.) 4. Is at least one excluded option written down? 5. Is the minimal counterfactual a single action? 6. Do the corrective actions map one-to-one onto the modes of death? 7. Does every action have a verifier? 8. Does the verifier know? (It counts only if they have been asked.) 9. Is the mechanism field tagged with the right name from the vocabulary? 10. Is the metadata's materials list complete?

Pass all ten and the postmortem enters the ledger; fail any and it goes back for rewriting. This is the same list as Acceptance Gate 3, put to a second use.

## 5bis The ten questions, four of them in detail

Four of the ten questions let the most through, so each gets a reading rule.

Question 3 (is the conclusion's subject a structure or a person): read the grammatical subject. "The crew's safety awareness was insufficient" — a person, reject. "No pilot piece was scheduled for the new crew" — an institutional act, pass. The gray zone ("the duty manager did not confirm against the roster") resolves on one test: would a competent substitute, in that seat, have done the same? Same answer, keep the sentence; different answer, it is a shot at a person.

Question 6 (do actions map one-to-one onto the deaths): play connect-the-dots. Draw a line from each death to its action. Two deaths sharing one action (usually "more training") or a death with no line at all (found, but nothing will be done) — either way, reject. Five minutes of dots catches the commonest half-breed: actions disconnected from conclusions.

Question 8 (does the verifier know): read the evidence format. The evidence is the verifier's own confirmation — a message reply, an accepted calendar entry, a signature. The author's "they should know" is not evidence. This question exists for the polite nod: agreement in the meeting, amnesia after.

Question 10 (is the material list complete): judge the honesty of the gap section, not the list's length. A short list is fine; a hidden gap is not — logs not exported, minutes lost, all stated in the gap section. The gap section lets a three-years-later reader distinguish the silences of missing material from the silences of missing writing.

The book's cases have one further use at the meeting: calibration. When the discussion reaches the mechanism section, pull one card of the same mechanism (Appendix B indexes by mechanism) and lay it beside your case — compare the material composition of the two decision points, check whether your excluded-options column contains the option theirs contained, set your toll beside theirs. The purpose is to keep the mechanism section from sliding into local exceptionalism ("we are different"): laid side by side, two decision tables look alarmingly alike, and the differences are usually only vocabulary. Rotate the calibration case monthly; within six months the room has face-recognition for the mechanisms — the second internalization path, alongside the question pass.

## 6 Converting to case cards: the second life

Writing the postmortem is the first step; the second life decides its shelf life. The main channel is conversion: compress the fifteen-field review into a twelve-field case card on the Chapter 5 format, for the organization's case library. Three conversion rules.

Rule one: de-identify the particulars, keep the structure. Names become roles ("the duty engineer"); units may survive to department level; commercially sensitive magnitudes become bands ("losses in the millions"). The de-identification floor is structural fidelity: the timeline's intervals, the material composition of the decision point, and the excluded options are the three things most often smoothed in redaction — smoothed, the case is dead. Keep a restoration key (an ID cross-table) in a permission group separate from the library, for internal investigators only.

Rule two: re-grade the evidence. A-grade material in the review stays A on the card; oral accounts drop to D. Conversion is re-grading, and the pass fixes sloppy grades from the review along the way.

Rule three: settle the mechanism field. The review's first-draft suspects settle here against each chapter's Section 1 criteria, checked one by one; criteria without evidence stay flagged as suspicion, with the missing criterion named. A library's search quality lives and dies on the mechanism field — a mis-filed case is a lost case.

The library's rhythm: quarterly intake (three to five cards from the quarter's reviews — those with second-life value), an annual compilation (aggregated by mechanism: the organization's own mechanism distribution), and one reflux line — the cards feed the Chapter 35 mapping table's calibration and the Chapter 37 library's additions every six months. Postmortem, case card, question bank, mapping table: four tools on one data flow, and the postmortem is the source. The flow's test is brutal and quick: pull any card at random — can you reach, in ten minutes, its review of origin, its evidence grades, and the improvements it spawned? Yes: the chain is alive.

## 7 Governing the archive: four duties

Once reviews accumulate, four duties govern them.

A registry: every review enters one master ledger (ID, subject, mechanism, date, action-verification status). The registry prevents duplicate labor — reviews of similar events cite each other instead of rewriting the background.

Aggregation: once a year, aggregate by mechanism — which mechanism draws the most reviews, which has the lowest action-verification rate, which gets cited most often three years on. One page of output: the organization's failure portrait, feeding Chapter 39's topic list directly.

The three-year test: each quarter, draw three reviews that have passed their third birthday and hand them to someone who was never involved, with the opening three questions (what happened, why, what would you have done differently). The share fully answerable is the archive's survival rate; track it by year. This is the opening standard, institutionalized, at the cost of one afternoon a quarter.

Retirement: reviews whose actions are all verified and whose mechanism has entered the library move to read-only archive — which is not a grave; the three-year test draws exactly from there.

Registry, aggregation, test, retirement: about a day's work a quarter, under the same housekeeper as the question library. One governance rule above all: review outputs enter no one's appraisal denominator, and review counts are never ranked. The only publishable KPI is the survival rate — the one measure that reflects quality without pressing the writers, because the pressure lands three years later, on people no longer in the seat, which is what keeps blamelessness from seeping back in.

## 8 The writing budget

"I had no time to write" is a common death; here is a realistic budget. Small events (no injury, losses in the low five figures): four hours. Medium (one review meeting, draft within a week): two working days. Large (cross-department, formally investigated): follow the investigation's rhythm, with the postmortem due two weeks after the investigation report settles. Staffing: one writer (preferably someone present at the decision but not its primary owner), one materials clerk (pulling logs and ledger extracts), one chair (who runs the meeting and executes the ten questions). Three writers do not work: a review with three voices reads like three documents stapled together. The last discipline is honesty's: where you cannot proceed — material missing, memories in conflict, mechanism unsettled — write "missing: X" and stop. No fluent speculation filling holes. A reader three years out forgives a gap; no reader forgives a gap disguised as prose.

## 9 Defending the review against its own narrative

A postmortem can catch Chapter 13's disease: the first review establishes a narrative, the second cites the first, and in three years the narrative is load-bearing fact. Three defenses.

Defense one: a rival-mechanism paragraph is mandatory. Beside the settled mechanism, list the alternatives considered and the reasons for exclusion — in the spirit of Chapter 13's comparison hypotheses: not balance-rhetoric, but a record of the exclusion so a later reader can re-open it when new evidence arrives.

Defense two: citations of other reviews grade down to D. When review A cites review B's conclusion, the cited content is first-party self-report, whatever grade B's facts carried — grade belongs to the material form, and retelling never upgrades it. Most public-events narrative errors work exactly this way: the first report's phrasing, fossilized by every retelling.

Defense three: a two-year reopening clause. The keeper sweeps, every second year, the entries flagged as suspicion, downgraded citations, and material gaps; new evidence — logs unsealed, external reports published, a participant willing to talk after moving on — triggers a partial reopening whose output is an errata page, never a silent rewrite. The errata preserve the review's historicity: the reader always sees both the judgment of the time and the correction that followed, and both are knowledge.

The three share one principle: a postmortem is writing about the past, and writing collapses toward narrative of its own weight. Evidence chains, rival paragraphs, and errata pages resist the collapse on the writing's behalf; the writer's private vigilance is not a mechanism.

## 10 Two variants: the near miss and the success

The template stretches to two special objects.

The near-miss review: isomorphic to the incident review, with two relaxations and one tightening. Relaxation one: the decision-point materials may be incomplete — near misses generate thinner records, and gaps honestly stated are acceptable. Relaxation two: the mechanism may stay suspect longer — near-miss signals are weak, and forcing a settlement mis-files. The tightening: the ledger sweep is mandatory — the sixth rewrite's rule; prior same-class signals must be swept, because a near miss's value lies mostly in what it confirms about its siblings. Keep the intake bar deliberately low: incident reviews pass the ten questions; near misses pass three (facts sourced, mechanism flagged, sweep done). Low bars give volume, and volume is what turns scattered near misses into a pattern.

The success review: after a project's conspicuous victory, review which defenses actually fired. The format mirrors the incident review — decision-point replay unchanged, the conclusion section naming "which device stopped which path" (the deviation ledger's entry that caught it; the true switchover that saved it). The dearest output is the counterfactual's other half: nothing went wrong — was that luck, or was it one specific device working? Only the review can tell, and an organization that cannot tell luck from defense will copy the luck and cut the defense (Chapter 20's slack begins exactly there). The twelve fields carry over with the mechanism field reading "mechanism intercepted" and field eleven rewritten as "the minimum defense, verified." Two or three a year gives the defense system a win record — which, at budget season, is the written evidence for Chapter 20's question four: does no-incident count as output?

## 11 The mirror at Chapter 39

Postmortem and pre-mortem are one tool facing two ways; the comparison sharpens both. Time: review after the event, rehearsal before the irreversible point — one processes tuition already paid, the other tries to waive it. Information: the review has an ending to anchor on and dense material; the rehearsal has none, runs on inference, and ships rougher goods. Psychology: the review defends against hindsight (knowing the ending distorts the replay), the rehearsal borrows it (pretending the ending is known raises criticality) — one coin, and Chapter 6's discipline is armor in one hand and weapon in the other. Outputs: case cards and improvement actions versus a hazard list and owners; in the ledger, the two must cross-reference — if a pre-mortem hazard comes true, the postmortem must cite that hazard list and ask whether the defense failed or the list was never executed. Cadence: reviews are event-driven, rehearsals calendar-driven (quarterly); calendar-driven tools decay slower, which is one reason to keep both. Maturity, for the pair, has a single observable: a postmortem that cites a two-year-old rehearsal's hazard line, and a rehearsal sheet whose disposition column records why that line was not acted on. At that point the tuition loop is closed: what the rehearsal could not prevent, the review collects; what the review cannot prevent, the next rehearsal plays out in advance.

## Self-Check: Five Questions

1. Take your organization's most recent postmortem and check it section by section against the four rewrites of Section 3. Which sections are written like Original One?
2. Of the materials list in your postmortem, how many documents carry timestamps? If the answer is none, the problem started on the day of the decision.
3. Where is the dissent record from your most recent postmortem? Minutes without a dissent column — how much do you trust them?
4. Of the four record-keeping standards in Section 4, which could your organization implement immediately? Who is the point of blockage for the one it cannot?
5. Can the postmortem you wrote three years ago still answer "why was it decided this way at the time"? For the one that cannot, which record-keeping standard was missing?

(First draft: 2,599 Chinese characters; English edition: about 1,700 words)
