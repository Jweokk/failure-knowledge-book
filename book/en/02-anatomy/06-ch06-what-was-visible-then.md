# Chapter 6 Visible at the Time

> What this chapter covers: how to drive the hindsight perspective out of your postmortems and out of your reading. Three operating disciplines, one test, three worked examples.
> When to turn back: when writing a postmortem, reading one, reviewing a design, or catching yourself saying "they should have seen it".
> Estimated reading time: 45 minutes.

The main enemy of the postmortem is a fact about memory: a person who knows how something ended can no longer think the way they thought before they knew.

The fact applies to the case card as well. Every card is written after the outcome is known, and no card can eliminate hindsight; the discipline has to be forced into the fields. Field 6, what was visible at the time, stands alone in the left column while the analytic fields are held back during composition. One rule follows: fill Field 6 first, and read the outcome section only after it is complete. An ordering discipline is imperfect and better than nothing. It rests on the writer's self-control, and self-control fails, so every card library needs a fallibility statement and an errata channel alongside it.

What follows compresses the contamination to a minimum, and states its ceiling in the same breath: these disciplines cannot return a postmortem to zero bias. Bias can be compressed, never zeroed. Memory and the narrative instinct reintroduce the outcome perspective at every layer of writing. Chapter 2 made that claim. This chapter is the compression manual.

Teach the three disciplines to your team. One person compressing their own bias still leaves a team postmortem with bias in it. Only when the whole team carries the disciplines does an organization's postmortem turn collectively. The teaching material is this chapter: forty minutes to read, an afternoon to practise.

The three rules: use only timestamped material; use only information the actors could obtain; list separately everything learned later. Executed together, they hold hindsight outside the door.

Whether the door is actually shut can be tested. The exchange test hands your left column to someone who does not know the outcome and asks them to infer what happened. The distance between their inference and the real ending is the purity of your column. A short distance means the column leaves the right blanks and leaks nothing from the future. The tester should if possible be a new colleague, who carries none of the organization's existing narrative and so measures more accurately. The test returns a purity score and a recording of the tester's reasoning, which shows what path your column led the reader down. Run it on a sample of postmortems once a quarter. Half a day of a newcomer buys an objective third-party reading of postmortem quality.

## 6.1 Why the Rearview Mirror Cannot Be Shut Off

Psychological experiments in the 1970s gave the phenomenon its name. Baruch Fischhoff's classic study had two groups read the same historical situation, one told how it turned out and one not told. The group that knew judged the outcome to have been systematically more likely all along, and did not realize that knowing the ending was why (Fischhoff, "Hindsight Foresight: The Effect of Outcome Knowledge on Judgment under Uncertainty", 1975; full citation: Fischhoff, 'Hindsight-foresight', Journal of Experimental Psychology: Human Perception and Performance 1(3): 288–299, 1975, bibliographic record verified via Crossref).

One laboratory detail carries a sharper implication for organizations. People who know the outcome do not merely raise their estimate for the outcome that happened. They lower their estimates for the others. The whole probability distribution is dragged toward the ending, and a distribution dragged that way is useless for risk work. The historical risk list written inside a postmortem has already been reshaped by the outcome, so using it to identify future risks is measuring new events with a bent ruler.

The correction is to write intervals instead of points. A risk retrospective records the several outcomes that seemed possible at the time, each with the basis it rested on. That spreads the bent distribution back out. The difficulty is evidential: probability judgments made at the time were almost never written down. That is the gap the decision record of Chapter 7 fills. Write the distribution at the moment of decision, and a future postmortem inherits a draft the ending has not touched.

The draft does not need to be elaborate. Line 2.5 of the three-line decision record covers it: the main alternative outcomes then believed, and roughly how much confidence each carried, in words rather than numbers. "About seventy percent confident" is enough for a later comparison. Verbal probability is unintimidating, since numerical probability demands calibration training while anyone can write down how confident they felt. Vagueness beats absence, because a postmortem with no draft can only be reshaped by the ending. File it in the same repository as the decision record. Half a line added to the Chapter 7 system saves a chapter's worth of archaeology later.

Later research gave the effect a plainer name: creeping determinism. Once the ending is known, memory rewrites the process into a single road running to that ending.

Inside an organization the consequences are worse than in a laboratory, because postmortems are written by people who know the ending, for readers who will know it too. Three layers of contamination stack up: the author knows, the reader knows, and both find it obvious that anyone at the time would have known.

Each layer has one counter. The author's is a writing-order discipline: left column first. The reader's is a reading-order discipline: left column alone, form a judgment, then read the right column and compare. The editor's is a layout discipline: columns physically separated, the entry point to the right column at the end of the left column, behind an explicit button. All three cost layout work and process discipline, and none is technically difficult. The difficulty is persistence, which comes from template fixation, Chapter 38's subject. The template hard-codes where the columns sit, so an editor who wants to interleave them has to fight the tooling.

Layout discipline sounds like housekeeping. It is the only one of the three that keeps working after the author leaves. Institutionalized layout outlives personal conscientiousness. Without it, postmortems train no judgment at all. Every fork in the road looks like open highway on paper, the reader concludes he would have seen it too, and back at his own desk he finds information arriving mixed with noise.

Accident investigation bodies maintain a whole procedural defence against this, and five of their devices can be lifted directly. Facts and analysis are published as separate parts, and the boundary between them is the boundary between the columns. Evidence is numbered item by item, so the analysis cites numbers and the citation chain can be checked. Competing hypotheses are worked through before any conclusion, and the report lists the hypotheses it excluded with the grounds. Conclusions are graded, each annotated with the strength of the evidence behind it, reusing the grade table in Chapter 10. Dissent is recorded: disagreements inside the team go into the report, because the presence of dissent is a mark of honesty.

All five have been verified as transferable, since they recur across industries in the better investigations. Resistance is measured in working hours. Together they add roughly thirty percent to the time a postmortem takes, and what that thirty percent buys is a generation of difference in credibility. Put a postmortem with all five beside one missing three, read both, and the gap needs no argument.

The anti-forgery principle deserves one more step. A structured document's verification path closes because every number it carries walks down to a physical object in the file. The report cites an investigation number, the number resolves to an interview record number, and the interview record carries a signature page. Three levels down, and forgery would have to be committed at one of the three.

The organizational version of that landing is an evidence chain of numbers. Each fact number maps to a number in the source record, which can be a work order number, a log ID, a page number in meeting minutes, anything that lands on a physical object. A postmortem whose numbering chain closes gains anti-forgery and anti-forgetting at once, because retrieval runs on the numbers. Three years later, the factual basis of a conclusion takes about five minutes to reach.

Reports of the NTSB type split facts and analysis into two parts. The facts part admits only material that carries a source and a phase. The analysis part annotates each statement with the fact it rests on. The structure's deeper function is chronological sorting: for any statement, the first question is whether it happened before the accident or after.

For readers who work in investigation, that question has an upgraded form. Tag each statement with three moments: when the event occurred, when the information about it was recorded, when the author used it. Three-phase tagging makes recording delay visible, and recording delay is itself an object of postmortem. A record system with long delays produces a left column that is incomplete by construction. One more column than two-phase tagging buys an evaluation dimension for the record system, and gives improvement a precise target under Chapter 38's trace-keeping requirements: the link with the longest delay gets rebuilt first.

This chapter's discipline is that whole procedure compressed into three rules a person or a team can execute on Monday.

The scope has to be drawn before the rules are applied. They constrain the writing and reading of postmortems, whose purpose is to preserve the training value of judgment. They do not constrain the conduct of an accident investigation, which should exhaust every piece of evidence available after the fact. An investigation establishes what happened; a postmortem re-enacts a decision. The two document types face different directions, so their disciplines differ.

The two meet at the reading of an investigation report: facts part under this chapter's discipline, analysis part as conclusions, the switch between the two readings being the section heading. With the scope drawn this way, no reader need fear that the discipline turns a postmortem into a crippled version of the truth. The right column, the post-hoc reconstruction, is where the truth is kept. The discipline asks only that the two worlds be labelled.

## 6.2 Discipline One: Timestamped Material Only

The operational definition: every item admitted to the visible-at-the-time set must answer when it entered whose field of view. Only items that can answer it may stand as inputs to the decision.

Timestamped material includes meeting minutes, with date, attendees and the order of the agenda; work orders and checklists, with completion time and signatory; the publication times of weather and market data; the timelines of recordings and chat logs; the sequence of steps in an approval flow.

One digital-age caution belongs on that list. System timestamps are not automatically trustworthy. Server clocks can be reset, clocks across machines drift out of sync, log time zones can be a mess. Judgment about sequence across systems needs clock alignment first. Record the clock source and the time zone for each class of log, in the system configuration, so that at postmortem time the clocks are checked before the timeline is ordered. Cross-system accidents are where this trap bites hardest: two systems five minutes apart in their logs will invert the order of events, and an inverted order drives the analysis in a completely different direction. Synchronize the watches, then read the cards.

Material without timestamps includes the recollections of participants, summary reports, retellings in the press, and undated statements like "hidden dangers had been found repeatedly before this".

An aviation case shows how hard the discipline bites. In the fact chain of Alaska Airlines 261 (NTSB AAR-02/01), the items that can carry timestamps include the application documents for extending the lubrication and end-play check intervals, with the dates on which the FAA approved them; the accident crew's reports to the ground about abnormal jackscrew position on the horizontal stabilizer, with call times; and cabin reports of unusual noise, with times. The thread wear morphology of the nut found in the teardown after the accident, and the laboratory metallurgical analysis, have no moment at which they entered anyone's field of view. They go to the hindsight column whole.

Once the columns are separated, the reader sees what the decision-makers held: the interval had been extended by their own organization, and the aircraft had begun reporting abnormal position. What they were not holding was any card showing the condition of the nut.

The method asks something cruel of the writer. Every clever insight has to pass four questions, and most fail, because they are thoughts available only after the ending is known. The cruelty pays. The thinner the left column, the more real the reader's immersion, and fewer cards on the table means the judgment being trained is closer to the judgment the field demanded.

The method extends outside postmortems. Split a history book's account into what was visible then and what was learned later, and you will see at once how much of what gets called foresight was assembled afterward. The demystification of historical reading comes free with this discipline.

The frequent error in practice is to treat the existence of information somewhere inside the organization as visibility to the actor. Between existing and visible lie four gaps: channel, format, timing, language. A test report buried on the ninth directory level of a shared drive does not exist for the engineer making a release decision at two in the morning.

Judging visibility takes four questions. Did the item enter the channel the actor actually uses? The duty room reads the duty system, not the shared drive. Can the format be read on the spot? An original English report handed to a night-shift assembler may not be. Did it arrive before the action or after it? And can the magnitude be grasped on the spot, when the one number that matters sits inside a hundred pages?

Institutionalized, those questions become an information accessibility audit: an annual sample of key decision points, drawn from every major decision the organization made that year, audited by postmortem-style walkthrough. It produces an annual accessibility report that lists the decision points where accessibility failed and classifies the causes, channel missing, format wrong, timing late, magnitude hidden, with counts for each. The report goes to the annual budget for information infrastructure, Chapter 39's line item, where accessibility spending and its returns are reconciled. The audit costs about two working days a year, sampling plus walkthrough. An individual discipline governs the pen; an annual audit governs the system.

The four questions also compress into a pocket card, taped to the monitor while a postmortem is written: channel, format, timing, magnitude. Read the four words in order. If any word fails, the item moves to the right column.

From the pocket card the next step is organizational: an information accessibility matrix, key decision points as rows, the four questions as columns, the actual situation at the time in the cells, maintained annually by Chapter 33's intelligence function. Its output is an accessibility terrain map. The depressions on it, information that should have been visible at a key decision point and was not, form the construction list for information infrastructure. That list's budget line exists in Chapter 39. From terrain map to budget, the chain is complete except for a first move.

## 6.3 Discipline Two: Only What the Actors Could Obtain

The direct corollary: any "data at the time" cited in a postmortem must state whose hands it was in.

Where the same information sits in an organization determines what it is worth. Risk control knew that customer concentration had passed its limit, but the lending decision belonged to a branch manager whose system displayed only a ranking of customer contribution. A postmortem that writes "the bank knew concentration was over the limit and lent anyway" has placed the risk department's knowledge inside the branch manager's field of view. The accurate version reads: "the branch's lending system interface carries no customer-concentration field; that field appears only in the head office risk monthly report, dated the fifteenth of each month." Both sentences describe the same organization. The first invents a decision-maker who never existed.

A companion field belongs beside the distribution note: the people who should have known. Record which positions, by design, were supposed to have this information, then record who actually knew. The designed side comes from process documents, job descriptions and flow charts that specify the intended scope of knowledge. The actual side comes from systems and records, which show who could really see. Put the two columns side by side and the difference is a symptom of the information system.

A distribution table built this way serves two later chapters at once: information attenuation up the hierarchy (Chapter 16) and lateral information gaps (Chapter 21). Draw it once and both analyses have ground under them.

The Challenger case shows why the discipline is necessary, and shows it most completely. On the teleconference of the evening of January 27, 1986, the engineers' hand held this: O-rings recovered from booster joints on earlier flights had shown erosion and blow-by, with flight numbers and photographs on record; those signs correlated statistically with low temperature; the joint had performed worst at the lowest launch temperature reached so far. Their hand did not hold the on-site high-speed imagery, which came into existence only after the accident; nor the precise order in which the joint failed, reconstructed afterward; nor data on how the second seal behaved dynamically at low temperature, supplied by later experiments. The decision in that meeting was made with the first hand only. The Rogers Commission report can support attribution at the organizational layer precisely because its evidence chain keeps the two hands strictly apart. (Each item checked: the flight-numbered records of erosion and blow-through, and the Morton Thiokol engineer's memorandum of July 31, 1985 warning of "a catastrophe of the highest order", both appear in Volume 1, Chapter 6, "An Accident Rooted in History"; the conduct of the meeting, with the engineers' photographs and diagrams entered as evidence, appears in Volume 1, Chapter 5. Official full text at nasa.gov/history/rogersrep/, read and verified for this book on 2026-11-01.)

The material leaves an advanced note for postmortem writers. Split the actors' hands by person. The engineers and the managers in that night's meeting held different cards: the engineers held cards leaning on data, the managers held cards about schedule and precedent. Only when the hands are split does the source of the disagreement become readable.

The technique is a seat-by-seat card chart, one column per attendee, recording what he brought into the room, what he received there, and who received what he sent out. The cost is a few more columns per person. The return is that a meeting postmortem stops being a blur and becomes a card game analyzable seat by seat: whose card was suppressed and never played, whose was played at the wrong moment. Chapter 19's price list for speaking and Chapter 16's attenuation analysis both run on that chart.

## 6.4 Discipline Three: What Was Learned Later Goes in Its Own Column

On the page, Discipline Three is two columns. The left column is visible at the time. The right column is reconstructed afterward, and every right-column entry states how it became known: teardown, interview, experiment, data analysis.

The right column carries a source discipline of its own. The means by which post-hoc information was obtained must be named as a tool: which instrument performed the teardown, whom the interview spoke to, what parameters the experiment ran. Tool information is what makes the right column's evidential strength assessable. Spoken post-hoc information and measured post-hoc information differ by an order of magnitude.

The execution standard is one line of source per entry, abbreviations acceptable: teardown report number, the interviewee's position, the experiment's parameter table number. The benefit is that the right column becomes checkable in its own right. A postmortem with both columns checkable is the highest definition of a postmortem this book offers.

The columns may not be interleaved. Any sentence that borrows from the right column to support reasoning in the left gets rewritten or deleted.

| Visible at the time (left column) | Reconstructed afterward (right column) |
|---|---|
| Around 20:00 on January 27, contractor engineers on the teleconference recommended against launching below 12 degrees Celsius | Launch imagery shows gas leakage at the joint beginning around the 58th second after liftoff [pending: page number awaits the official Rogers report text] |
| Erosion records from O-rings recovered on earlier flights, flight numbers checkable | Laboratory low-temperature elasticity test data, run after the accident |
| Contractor management reversed its position after a recess of roughly 30 minutes and agreed to launch | Vaughan's 1996 quantitative reconstruction of the successive lowering of launch temperature thresholds |

The value of the two columns lies in the existence of the right one. It admits on paper which content is post-hoc knowledge, and in doing so exposes an illusion the author and the reader share. A postmortem with interleaved columns never writes the word "afterward" and depends on hindsight in every sentence. The two-column version drives those sentences into the annotation column, where anyone can see them.

One maintenance rule: keep the growth history of the right column. An early draft's right column is thin and thickens as the investigation goes deeper. Keeping the two versions side by side leaves a live record of how the postmortem's understanding evolved. That record has teaching value. Where the draft judgment and the final judgment differ is the trace of an author's cognition being corrected by evidence, and such a trace is unusually good material for training judgment.

The organizational application is a postmortem of the postmortems. Once a year, sample the differences between first draft and final version across everything the organization produced, and look for the pattern. Which class of problem is always misread in the first draft is the organization's systematic blind spot in judgment. That list is the target paper for the next training cycle, and Chapter 39's rehearsal meetings should pick their topics from it first.

## 6.5 The Test: Three Signal Classes and One Dissection

A quick test for readers. When a piece of narration contains any of the following three classes of signal words, the hindsight perspective is doing the talking.

The first class is the counterfactual inside a process account: "if only, at the time, they had". A counterfactual appearing there means the author is filtering the process through the outcome.

The list has to keep growing as the genre's style evolves. Three phrases have come into fashion and belong on it: "essentially", "in the final analysis", "when it comes down to it". They almost always land where attribution is converging, and they work as rhetorical tools for compressing a complex failure, which is the flattening disease of Chapter 2, section 2.3. The mechanism for growing the list is a team blacklist of signal words, kept in a shared document and extended after each month's postmortem meeting. The longer the list, the stronger the team's immunity. The blacklist is for marking, not banning: writing does not have to avoid these words, but where one appears the author checks the perspective. Marking trains self-awareness. It does not censor vocabulary.

The second class is the vocabulary of surprise and retrospection: "had they known", "to everyone's surprise", "unexpectedly", "nobody imagined", "and yet". The subject of these words is a person who knows the ending, not an actor in the event.

The third class is "in fact, by then it had already". Behind every "in fact" sits a piece of information with no timestamp. Interrogate it: who saw it, when, through which channel.

For a deeper check, dissect. Break the narration into event cards, each card carrying two lines: the moment the event happened, and the moment the information reached the decision-maker's field of view. The difference between the two lines is the post-hoc content.

The tool version is a dissection table with three columns, event, event time, information arrival time, and a fourth that computes the difference. Every row gets filled. Where arrival time cannot be established, the row is marked N/A with a note. The N/A rows become a list of record gaps, which is also a map of where the trace-keeping system is missing pieces.

The payoff usually arrives about thirty minutes in, when the person filling the table first sees, physically, how many rows carry a large gap. Those rows are where hindsight is concentrated, and they get rewritten or moved to the right column. The template belongs in the postmortem toolkit of Chapter 38, alongside the two-column template and the signal word list. Those three pieces are the complete set of implements for this chapter's discipline.

Do it once and you will find that in most of your own cards the two lines carry the same moment. As you wrote, you promoted the ending into the information environment of the time.

More phrases are worth collecting, and the acknowledgements and closing paragraphs are where they cluster: "if only it had been a little earlier", "thankfully", "a blessing in misfortune", "fortunately". Words of that kind in a closing paragraph mean the author's perspective was suspended over the outcome from beginning to end.

The correction for a closing paragraph is to return to the beginning. What the ending should answer is this: if we did it again, which items on the list of decision points would change? That question forces the author from the endpoint back to the start, and the round trip is itself a full self-check of the three disciplines across the document. An alternative honest ending states the limits of the judgment: "this postmortem's reconstruction of what was visible then is limited by missing records; the following three points cannot be restored." A limitation statement tells the reader where the thin ice is. Thin ice is not off limits; it has to be crossed with the uncertainty in view.

## 6.6 Three Walkthroughs

Walkthrough one: rewriting an Alaska Airlines 261 postmortem.

The hindsight version reads: "the threads of the jackscrew nut were already severely worn, the safety margin exhausted, and ditching was only a matter of time." Three post-hoc components sit in that sentence. The degree of wear was known only from the teardown. "The safety margin exhausted" is an analytic conclusion. "Only a matter of time" is an inference running backward from the ending.

The visible-at-the-time version reads: "the crew of the accident flight reported abnormal stabilizer position and motor overload in succession, with call records of repeated attempts and exchanges over roughly ten-plus minutes; the component's lubrication and check intervals had earlier been extended following the company's application and FAA approval (AAR-02/01 executive summary p.4, verified)."

Both versions describe one event. The first teaches the reader to watch out for wear. The second teaches the reader to watch the decision chain that extended the interval, and the procedure for handling abnormal signals. The first cannot be acted on. The second can.

There is an extreme form of actionable writing, the decision-point re-enactment. The left column becomes a drill. The reader reaches the decision point, closes the material, writes down a judgment, then opens it again to compare. Re-enactment is the name of this book's stop-point design, and it converts a postmortem from something read into something practised.

The organizational use is a rebuilt postmortem meeting, with the agenda changed from reading the report aloud to walking the decision points. At each point the meeting stops, everyone writes a judgment, and then the discussion starts. The meeting takes twice as long and trains ten times as much. Resistance comes from the time cost, and the honest comparison is that one rebuilt meeting is worth three accidents. The account is worked out in Chapter 39's budget.

An actionable left column has a check standard: the density of executable instruction. Can the reader, after each sentence, list an action? Sentences that allow it are information. Sentences that do not are atmosphere. The strict form is one action per paragraph: every paragraph contains at least one item convertible into an action check, and paragraphs that fall short get cut or supplemented.

The organizational version is quantitative quality control. Count the executable instructions in each postmortem and send anything below threshold back for rewriting, with the threshold starting at three per page. This control and the Chapter 38 template requirements are two halves of one gate: the template governs structure, the count governs density.

Walkthrough two: the 737-9 door plug (av-030, NTSB AIR-25-04).

Among the safety issues listed in the report's executive summary is the state of work on the door area during final assembly at Boeing's Renton factory. Sorted under the two-column discipline, the visible side holds the operational fact that this door had been opened for riveting rework within the assembly flow, together with the states of the work-order records along the release chain. The hindsight side holds the laboratory confirmation made after the accident that four positioning bolts were missing and no reinstallation was recorded (AIR-25-04 PDF pp. 10, 22, 26, verified).

Standing at the release node, what the actors could see was that the records were incomplete. What they could not see was that the bolts were missing. A postmortem that writes "they knew the bolts were not installed and released the aircraft anyway" has pushed the right column's physical evidence into the left column's heads.

The accurate question sits in the left column: how did work on a critical area, with no record of reinstallation, pass down the release chain without any additional confirmation being required? That question points at structure, specifically at the rule that incomplete records for critical-area work should by themselves trigger manual review. The remedies are in Chapter 29 (the invisibility of maintenance) and Chapter 15 (practical drift). The attribution of knowing violation points at nothing.

Structure-pointing questions come in a set of five patterns, all running backward from the conclusion. How was it allowed, meaning who did the structure authorize? How was it not stopped, meaning which gate was missing? How was it not seen, meaning which information chain was broken? How was it not written down, meaning which record requirement was absent? How did nobody own it, meaning which seat was empty?

The output is a list of five structural questions, each pointing at an object that can be modified. That list is the translation layer between postmortem and remediation, and the layer is what lets a postmortem end in a work order instead of a sigh. A sigh-style postmortem leaves the reader with a feeling. A postmortem built from the sentence patterns leaves a work order.

Attribution by knowing violation deserves a specific prohibition, because it is the most harmful pattern in the genre. It disguises a structural problem as a problem of character, and writes a repairable organizational defect as an unrepairable human one.

Enforcement takes a substitution drill. Whenever the pen produces "knowingly" or "deliberately", stop and ask why a rational person inside that structure would have done this. The answers that come back are almost always structural: the appraisal system, the process, the information available, the workload.

The psychological resistance is that the drill looks like excusing the actors. Chapter 2 covered the difference. Attribution places a behaviour inside its conditions in order to understand it. Excusing wipes responsibility off the conditions. This chapter trains attribution. When it is done, responsibility is still distributed through the structure, each piece where it belongs. Fixing the structure is more useful than cursing the people.

Walkthrough three: the R44 that took off at night in fog (av-021, NTSB CEN23FA125).

Visible at the time: the pilot's night qualification and instrument experience status, checkable in person and in the records; his own visual reading of the weather at the departure point; the night visual conditions before departure and in the direction of the destination. Reconstructed afterward: the flight path rebuilt from ADS-B data, which shows ground impact within a very short distance after liftoff.

A postmortem that writes "he did not know he had entered dense fog" breaks Discipline Two. Whether he knew cannot be established from the materials. What can be established is the climb and the turn he performed at that moment. Write actions, leave the psychology out: rule 2 of the case-writing method in Chapter 5, applied here.

The rule has a companion. Gaps between actions are left blank, honestly. If forty minutes pass between two calls with nothing recorded, write that nothing was recorded. A blank is honesty toward the recording system; filling it is a deception of the reader. Mark the blank with a gap row in the timeline: forty minutes with no record, no calls inbound or outbound and no system event log. The gap row reminds the reader that every judgment in that interval is a blind spot.

Gap density is diagnostic data in itself. Many gaps along the key decision chain mean the trace-keeping system is in poor condition, and Chapter 38's trace requirements exist to treat exactly that. The psychological threshold for leaving blanks is higher than it appears. A writer's instinct is to fill the gaps with reasonable inference so the narrative runs smoothly. Smoothness is a virtue in narrative and a poison in postmortem.

## 6.7 The Limits of the Discipline

The three disciplines have an honest boundary. In most organizations, timestamped material does not cover every key decision. Meetings without minutes, decisions reached in a corridor, verbal instructions that left no trace: the organization's own recording gaps thin the visible-at-the-time column itself.

That is a diagnosis rather than a failure of the discipline. A key decision point in some failure carrying no timestamped record at all is itself a failure report on the organization's trace-keeping system. Chapter 38 lists the trace requirement as a standing clause of the postmortem system.

This chapter can supply a design standard for that system. The minimum requirement is three moments: when the decision was made, when it was recorded, when it was communicated. With all three present, a future postmortem has something to restore. The registration cost is tiny, since the three-line decision record already carries it under the Chapter 7 system. The maximum requirement is the probability draft described earlier: the alternative outcomes then believed, with confidence attached, in words. Between the minimum and the maximum, each organization sets its level by the risk grade of the decision. Low-risk decisions take the minimum. High-risk decisions, the ones before an irreversible point, take the maximum. Grading the requirement is what keeps a trace-keeping system from being resented, because a blanket requirement for full tracing dies in its first week.

Where the record is blank, the blank is marked as blank. Memory is not permitted to fill it.

Blank marking carries a second value. The distribution of blanks is a disease map of the organization's record system: which classes of decision carry the most blanks. Levels where verbal command dominates, cross-department coordination points, and night shifts are the three high-incidence zones.

Drawing the map takes a blank count across every postmortem of the past three years, classifying and counting the blank points in each left column. The output is a heat map, and its three hot zones correspond exactly to the handover failure of Chapter 28, the coordination problem of Chapter 18, and the night shift of Chapter 26. The remedies in those three chapters are the heat map's prescription. After the prescription comes a retest: the same blank count run again next year, against this year's. The speed at which blank density falls is the speed at which the record system improves.

The heat map is where this chapter's discipline scales. An individual's honesty, aggregated, becomes an organization's diagnosis.

## Five Self-Checks

1. Take your most recent postmortem and scan it with the three signal classes from section 6.5. How many hits?
2. In your organization, what key information exists somewhere in a system but cannot be seen on the interface of the person who decides? Name the system and the field.
3. For your last important decision, can you reconstruct the timestamped sequence of information arrival? Where you cannot, is the record missing or is your memory?
4. Does your team's postmortem template have columns for visible at the time and reconstructed afterward? If not, whose resistance will adding them meet?
5. Rewrite one paragraph of your industry's most recent public postmortem in two columns, three items in each.

Beyond the five, the graduation exercise for this chapter: run the whole sequence on your organization's last major postmortem, all four steps, the signal scan, the two-column rewrite, the dissection table, and the exchange test. It takes about one working day. Its four products, the scan list, the two-column version, the dissection table, and the purity score, are the first physical examination report on your organization's postmortem capability.

The report's value shows over time, in the annual comparison. Run the same sequence next year, and the improvement across the four products is a growth curve for organizational postmortem capability. What that curve means gets said again in Chapter 38, where postmortem capability is treated as the cardiopulmonary function of organizational learning.
