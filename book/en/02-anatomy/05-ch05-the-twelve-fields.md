# Chapter 5 The Twelve Fields of the Case Card

> What this chapter covers: the twelve fields of the case card, the analytic unit this book uses everywhere, defined one at a time, each with one badly written example and one corrected version.
> When to come back: when you write a postmortem of your own, review someone else's, or need to compress an investigation report onto one page.
> Reading time: about 40 minutes.

A three-hundred-page investigation report holds almost everything and reads badly. A postmortem article reads well and holds fragments. The case card is the layer in between: one page, twelve fields, a hard requirement attached to each field, and no case admitted to the main text until the fields are filled. This chapter defines the fields one at a time and gives each one a bad example. The bad examples come from real postmortem and briefing prose. You will find the same species inside your own organization.

One term of use before the table. The twelve fields are an engineering format, not an academic one. Every field is on the card because something downstream consumes it: the ID feeds citation, what was visible then feeds training, the minimum counterfactual feeds a work order. A field with no downstream consumer has no claim on a line of the page.

Engineering formats are strict, and the strictness is the point. An engineering drawing carries tolerances because a dimension without a tolerance cannot be built to. The field requirements below are tolerances of the same kind, and "maybe good enough" quietly removes the use the field existed for.

Read with a pen in hand. Take your organization's most recent postmortem and fill each field as you reach its definition. By the end you hold one completed card. A reader who only reads ends up with a list of format facts, which is not the same thing as the skill.

The twelve fields at a glance:

| # | Field | Hard requirement |
|---|---|---|
| 1 | Case ID | domain code plus serial, unique across the book |
| 2 | One-line summary | 30 characters or fewer, states only what happened |
| 3 | What and who | organization plus equipment or project, nameable down to model and registration number |
| 4 | When and where | year, month, day plus location |
| 5 | Domain and mechanism | domain code plus main mechanism, 1–3 attached, main mechanism first |
| 6 | What was visible then | information the actors held, with timestamps, at the moment they decided |
| 7 | Options ruled out | options tabled and rejected, and options that never reached the table |
| 8 | The decision point | who did what, in which meeting or on which document |
| 9 | Point of no return | the action after signature, go-live, takeoff, or pour |
| 10 | Scale of consequences | figures from primary material; where none exist, "no public quantification" |
| 11 | Minimum counterfactual | one action changed avoids the event; write one |
| 12 | Evidence grade and sources | grade A–E plus full citation plus link |

## 5.1 Definitions and Examples, Field by Field

### Field 1: Case ID

Definition: `domain code-serial`. Aviation av, chemicals ch, nuclear nu, healthcare me, pharmaceuticals ph, construction ce, maritime ma, software sw, finance fi, startups st, public policy po, military mi, manufacturing mn, agriculture ag.

The scheme travels. An organization building its own library may change the format and draw the prefix from its own industry vocabulary. Three governance rules do not travel, because they are what keeps any citation system alive: append only, keep state separate, reserve ranges. Formats can vary because an ID means something only inside its own system; your av-037 and this book's av-037 may point at different events, and carrying the title when you cite resolves it. The rules cannot be dropped because a broken link or a collided number kills a library outright. Take the three rules and the field definitions and use them as needed. Permission to take them is why this chapter exists.

Bad example: "Accident Case No. 3", or "Compilation of Typical Cases in Our City, Volume XI". The serial hangs off a table of contents. Revise the contents and the serial is void, and every citation into it snaps.

Good example: `av-037`. Three years later, after a contents revision, this ID still points to the Japan Airlines A350 record and its collision with the Japan Coast Guard aircraft. The ID is the anchor between this book and other material, and the primary key of the master case table in Appendix B.

Three engineering rules decide how long a scheme lives. Appending is the only permitted edit: when an ID turns out to sit under the wrong mechanism, add a correction entry and leave the number alone, because citation integrity outranks catalogue tidiness. State is a separate field, so revisions, v1 and v2, and errata never enter the ID. Ranges are reserved, with hand-collected, bulk-imported, and externally exchanged records given their own blocks of serials, so a merge cannot collide. The cost is one line of explanation in the register. The return arrives ten years out, in a system with no broken links, no duplicate numbers, and no silent renumbering, which is the credential a knowledge base needs before it can talk to outside material at all.

### Field 2: One-line summary

Definition: 30 characters or fewer, stating only what happened. The test is negative: no cause, no judgment, no adjective.

Bad example: "Due to inadequate safety management and weak employee safety awareness, an avoidable serious accident occurred." Six information slots, four of them judgments (inadequate, weak, avoidable, serious) and none of them fact.

Good example: "737-9 door plug separates in climb; rapid depressurization; return." Fifteen characters in the Chinese, one action sequence: component, phase, consequence, outcome. The reader knows what happened and does not yet need to know why.

The method is to find the first moment on the timeline when something went wrong physically and write it as subject, verb, object. "Door plug separated." "Ball-nut thread worn to failure." "Oxygen generator caught fire." Evaluation gets its turn later.

The field has a second use as the catalogue index line. A catalogue page carries nothing but IDs and one-line summaries, and one page then scans the whole stock of ways things die. Its standard is the scan test: fifty lines in thirty seconds, after which the reader can say roughly which families of death the library holds. A summary that fails is too long or too clever. Put the page on the wall of the decision room rather than the canteen, updated monthly as new cards arrive, since the readers of a death catalogue should be the people deciding.

Three sentence rules hold the field down. Verbs beat nominalizations: "door plug separated" beats "a door plug separation event", since nominalization hides the action inside an abstraction and is where bureaucratic prose starts. Quantifiers stay conservative: the 30-character limit forbids piling up, yet writers still squeeze in three parallel actions, so write the first physical event and leave the rest to the body. Names stay out: no personal names, no characterizations, because the summary is public-information layer while individual accountability belongs in field 8 and in the investigation documents. All three serve one purpose. The summary is a retrieval tag, a thing that exists to be found rather than read to the end.

### Field 3: What and who

Definition: whose thing failed. Organization name, equipment model, any identifier that can be named: flight number, registration number, construction section.

The field carries a second layer. Write the subject on two levels, the operating level and the owning level. Ask whether the crew sailed for the owner or was hired with the hull, whether the plant runs its own staff or a contractor's. Responsibility and the landing point of remediation usually sit between the two, so write a subject chain of brand owner, operator, facility. Every name on the chain holds a decision point, and primary documents usually write the subject by level, which means the chain can be copied from the report's subject section. The chain pays off in tracking: a requirement handed to one level has to be executed and verified at another, and a card with no chain gives tracking nothing to hang on.

Bad example: "an aircraft operated by a certain airline". One word, "certain", and the case drops to a fable. It cannot be checked, extended, or confirmed at the level of conditions.

Naming is also a weapon against survivorship bias. Narrated failures tend to lose their subject, and once it is gone the reader cannot check whether that company still exists, how it has done since, or whether the accident recurred. A named case allows the full verification pass, and the result is often more instructive than the story. The action is to look up what happened to the organization afterwards: its remediation, its later record, its events of the same kind. Doing this repeatedly is the advanced drill of card reading and the technical form of Chapter 2's instruction to go out and buy the death samples. Enough passes and a reader develops an instinct for the time depth of failure. An accident occupies a stretch of an organization's history; its single day is only the visible part.

Good example: "Alaska Airlines 1282, Boeing 737-9 (N704AL)." Checkable, citable, condition layer complete: the model fixes the airworthiness background, the airline fixes the maintenance system, the registration number lets anyone walk the aircraft's history in public databases.

Where naming carries legal risk, with a judgment not yet final or a penalty not yet published, drop one level: name the industry and the category, and state why the subject is not named.

One recurring argument deserves an answer. Are small subjects worth naming, the sole trader, the one-person company? Yes. Small operators account for most of the statistical mass, and anonymizing them teaches readers that risk belongs to large organizations; naming restores the distribution to its real shape. The privacy boundary is prior publication: where the subject information is already public in a primary document, the card copies it, and where it is not, the card follows the document. Beyond that boundary there is an emotional cost, and it is real. A small operator's failure, written into a book, will be read by the people involved or their families. Write only the facts the documents contain, with no characterization of anyone. Characterization is the sugar of narrative and a second injury to the people in it.

### Field 4: When and where

Definition: the event's year, month, day and location, precise to the day. The investigation's publication date belongs to field 12.

The field carries a geographic discipline. Write the location to the level where it can be found on a map: country, city, facility. Where the facility can be identified, name it; where it cannot, name the administrative area. The level decides whether the reader can place the case in its geographic and regulatory context, because the same mechanism in another jurisdiction carries a different condition layer, and location is the reader's first evidence about the regulator. Where a case cannot be located at all, for open sea or a facility that cannot be disclosed, say why. A stated reason distinguishes a limit from laziness.

Bad example: "early 2024", or "last summer". Early and late in a year are eleven months apart, enough room for a full maintenance cycle.

Good example: "2024-01-05, Portland, Oregon, USA, about 20 minutes after takeoff" (NTSB AIR-25-04). The date anchors the information environment: weather bulletins from before that day, maintenance records, meeting minutes all fall inside what was visible then; anything dated after is hindsight.

Precision has three more rules. Keep one time basis in a card, with event times in local time and the zone marked, and publication times in the issuing body's local time, because a mixed timeline steals the reader's sense of sequence. Distinguish an instant from a window: the minute where a minute is known, the window where only a window is known, with the source's precision marked, since false precision misleads as much as vagueness. Mark the genealogy of the timeline: where a preliminary bulletin and the final report disagree, follow the final report and note the difference, which is itself a record of how the investigation moved.

### Field 5: Domain and mechanism

Definition: the domain code plus the main mechanism. Up to three mechanisms may be attached, the first being the main one. Names come from the twenty-four-term vocabulary in Chapters 11–34. Do not invent one.

Bad example: "management problems", "human factors", "systemic risk". These three phrases turn up in the conclusion paragraph of most postmortems. They can hold anything, and so they explain nothing.

Good example: "av; The Invisibility of Maintenance; Practical Drift." Attaching a mechanism is an act of attribution, and an inaccurate attachment is worse than a single accurate one.

The ratio is one main mechanism and at most two companions. Three or more says the attribution has not converged; go back to the mechanism chapters, compare against their criteria, and attach again. The ratio protects the index, since a card that attaches five mechanisms has voted in five rows of the matrix and thinned the signal-to-noise ratio of every search through it. It also prevents drift. The main mechanism declared here may not change in the body text: a case can be cited in several chapters, and every citation presents it under the same main mechanism. Stable identity is part of what makes a case citable, and it is the specific defence against a case retold in each chapter as a story supporting that chapter's thesis.

### Field 6: What was visible then

Definition: the timestamped information the actors held when they decided. Only records whose phase can be fixed from the material are admissible: meeting minutes, work orders, the issue time of a weather forecast, the previous shift's handover notes. Anything learned only afterwards stays out, without exception.

Bad example: "hidden hazards had long existed, and management cannot escape responsibility." The phrase "long existed" erases every piece of time information. Existing for how long? Who saw it, and when? Did the person who saw it have a duty to report it?

Good example: in the Alaska Airlines 261 case (NTSB AAR-02/01), what was visible then included the inspection records from before the lubrication and end-play check intervals were extended, the application for the extended intervals with the Federal Aviation Administration (FAA) approval, and the accident crew's reports of abnormal jackscrew position and unusual cabin noise. Each item carries the date it entered someone's field of view. The thread wear found when the nut was opened after the accident is post-event information and cannot enter this field.

This is one of the two fields with the highest value density in the book, field 11 being the other. Its purpose is to keep Chapter 2's attribution bias outside the reasoning: only what the actors could see is admitted. Chapter 6 is given over to operating it.

One implicit standard needs stating. Visible does not mean noticed. The field collects information that was reachable, meaning it sat on the desk, in the system, or in the minutes; whether the person saw it is a separate question and belongs to the reader. Conflating the two lets the card quietly excuse or convict, since a thing unseen may be an attention problem or a presentation problem. Keep them apart by recording how the information was reachable: in the system, on paper, or by word of mouth. The three modes carry different attention costs. Once the mode is written, field 6 becomes the material from which a reader rebuilds the desk of that day, and every judgment made from it is the reader's own.

### Field 7: Options ruled out

Definition: the options on the table at the decision point that were rejected, plus the options that should have appeared and did not. Record both and mark which is which.

Bad example: "had they been more careful, it would not have happened." More careful is an option that does not exist. No action, no cost, no decision-maker. Writing it is writing nothing.

Good example, with the format shown on Challenger (Rogers Commission report, 1986). On the teleconference of the evening of January 27, 1986, the options on the table were: launch on schedule on January 28, which was selected; delay until daytime temperatures recovered, rejected on schedule pressure; and honor the engineers' proposed threshold of no launch below 53 degrees Fahrenheit (about 12 degrees Celsius), rejected because launches had already succeeded several times at lower temperatures. The absent option was any reopening of why the launch temperature threshold had been sliding downward launch by launch. Volume 1, Chapter 5 of the Rogers Commission report records that Thiokol engineers recommended against launch below 53 degrees Fahrenheit, resting largely on blow-by data from flight 51-C; the official text is at nasa.gov/history/rogersrep/v1ch5.htm, and this book read it on 2026-11-01.

Ruled-out options are valuable because they expose the structure of the decision: how options were generated, how they were rejected, who was entitled to put them on the table. Most postmortems record what was chosen and omit what was choosable, and the same option-generating machinery then produces the same menu at the next decision.

Absent options need restraint. The evidence for one is a process document. An option that procedure required and the record never shows is a legitimate absence; an option the reviewer thought of afterwards is an invention. Restraint is needed because absent options are the easiest thing in the card to write with hindsight, turning what the actors never considered into what they should have considered, which is Chapter 2's attribution bias returning through the side door. The evidentiary standard is a comparison: the step exists in the procedure, its counterpart is missing from the minutes, and the gap is the evidence. Where the evidence is thin, write the absence weakly: "the procedure appears to have offered this path; no record of discussion appears; unresolved." A weak entry costs nothing. An invented one costs the card.

### Field 8: The decision point

Definition: four elements, person, meeting, document, action. Who decided what, in which meeting or on which document. The date falls on a day.

A discipline is buried in that definition. A decision point has to be an identifiable human action: who, when, in what form, doing what. Automatic system actions and physical processes do not occupy this field; automated actions are recorded in the failure chain, and Chapters 21 and 22 cover the paths taken by things and by systems. The reason is what the field is for. Postmortems improve the environment in which people decide, which covers how options get generated, how information arrives, and how a signature comes to be given; with no identifiable action there is nowhere for the improvement to land. The more automated the system, the fewer human decision points remain and the more each one matters. The takeover moment in Chapter 26 is the scarce form of the decision point, and scarcity raises the standard of description, because those points are everywhere a human being can still intervene.

Bad example: "company management made the wrong decision." No name, no meeting, no document. The sentence can be neither contested nor cited.

Good example: Alaska Airlines 261 (NTSB AAR-02/01, executive summary). Alaska Airlines extended the lubrication interval and the end-play check interval for the horizontal stabilizer jackscrew assembly, and the FAA approved both; the investigation found that the extended intervals let a lubrication shortfall the old schedule would have caught develop into excessive wear and then failure (text from the executive summary, in the portions I read myself). All four elements present: the company as who, the documents and approvals as the vehicle, the interval extension as the action, the FAA approval as the gatekeeping act.

### Field 9: Point of no return

Definition: the moment after which the event's main consequences can no longer be undone by ordinary means. The test is in Chapter 7: money can undo it, time can undo it, a public announcement can undo it; a signature and a go-live cannot.

The register links to the duty to notify. Information arriving after the point of no return, a weather update after takeoff or a test report after the pour, is post-event information, and what it does is open a new decision point: continue, turn back, stop work. At the point of no return the question changes from whether to do the thing to whether to rescue it. Cards handle that phase as a separate entry, the post-irreversible decision, and it carries high value in review because it tests the ability to lose less in a bad position. Most postmortems only train the ability not to lose at all.

Bad example: "from the moment the project started, failure was already certain." Fatalism is not a definition of the point of no return. It folds every decision point into one and erases every position in between where intervention was still possible.

This chapter registers position only: which step, once passed, cannot be walked back. Chapter 7 owns the typology, where incremental, one-way valve, and compound types call for different interventions. The division of labour keeps the card's density manageable, since a list of positions already carries large engineering value; most organizations cannot state the irreversible points in their own key processes. Chapter 7 gives the method for compiling the list the first time, walking the process node by node and asking at each one whether the step can still be reversed. The cost is a single process walkthrough. The output is a register covering every key process, and every row should carry a named custodian, which is where Chapter 18's single-responsible-person clause comes in.

Good example: in the Japan Airlines 516 event (av-037), the point of no return formed when the Coast Guard aircraft entered the runway while the A350 crew held landing clearance. From that combination onward, the two aircraft's speeds and the remaining distance made the collision an event most operating paths could not avoid. Assembly-type cases are cleaner: the door closes, the concrete is poured, the reactor is synchronized to the grid, and every minute of work afterwards is paying the fare for that action.

### Field 10: Scale of consequences

Definition: the figures in the primary material. Deaths, injuries, money lost, hours of downtime, units recalled; write whatever exists and name its source. With no figures, write "no public quantification".

Bad example: "caused enormous economic loss and severe social impact." Enormous is how much? Severe to what degree? The sentence's only function is to hold a place.

Good example: "0 deaths; 7 minor injuries (all passengers); 169 uninjured; aircraft substantially damaged" (av-030, NTSB AIR-25-04). Four figures, each with its own basis, all from one report.

"No public quantification" is a legitimate answer. It means the consequences never entered any primary document. It does not mean they were zero.

Casualty figures follow an official basis and carry its version. Preliminary and final counts often differ, since an initial bulletin gets revised as identities are confirmed, and the card takes the final adjudicated basis while preserving the revision trail. The reason is respect as much as law: every number in a casualty count corresponds to particular people and families, and a careless basis does harm to the people behind the digits. The operation is to date the number, as in "7 minor injuries (adjudicated, 2025-03)". Number and adjudication date travel together, and the reader knows which version is in hand. Version management looks fussy. It is the minimum courtesy this book extends to this field.

### Field 11: Minimum counterfactual

Definition: the one action which, changed, would have avoided the event or sharply reduced its consequences. Work backward from the latest action that did not depend on luck. Book-wide discipline: write exactly one.

Bad example: "had management been strengthened, systems perfected, awareness raised, and oversight tightened, the accident could have been avoided." Four actions amount to none. The reader cannot tell which comes first, and so does none of them.

Good example: Alaska Airlines 261 (AAR-02/01). Leave the end-play check interval unextended and inspect on the original schedule, and the wear had a chance of being found before it reached failure. One action, at the latest position on the chain of decisions actually taken, resting on no luck of the "happened to be spotted" kind. (AAR-02/01 executive summary p. 4, and the Safety Board's statistical study of end-play data in section 1.18.2; PDF verified.)

The field is a training device. Writing it forces the author to answer where the minimal intervention point lay along the whole chain. Chapter 10 gives the backward-walking method. Two counterfactuals amount to none, because the reader remembers the easy one, and the easy one is rarely the minimal intervention point.

One test is gold. Write the counterfactual as an instruction: who, by what date, does what, at what cost, approved by whom. Fill all five and it is usable; fail any and it is a wish. The test pulls the lesson down from the moral layer to the operating layer. "Tighten oversight" fails it; "change this check from annual to semiannual" passes, and the gap between the two is the gap between a lesson and a slogan. Organizations can use the test at scale by turning every passing counterfactual straight into a work order. A counterfactual that reaches a work order is closed. One that stays on the page is decoration.

### Field 12: Evidence grade and sources

Definition: grade (A, full independent investigation report; B, official bulletin or communiqué; C, judgment or penalty document; D, public postmortem by a party involved; E, media lead), a full citation, and a link. Rule: E-grade material may never be the sole source for a case in the main text.

Bad example: "compiled from multiple media reports." When several outlets retell one wire story, "multiple" is a fake number.

Good example: "Grade A. NTSB, Aviation Investigation Final Report DCA21FA085, 2023; link at Appendix B, av-006."

A citation has to resolve to a document name and number, and the link has to have been opened by hand. No exceptions, because this is the collateral behind every credibility claim the book makes.

Readers need a conversion table. Read the grade first; it tells you how the card may be used. Grade A: all details quotable, down to signatory-level actions, and a postmortem can benchmark against it directly. Grade B: the event frame and official conclusions quotable, with detail discounted, since a bulletin carries limited resolution. Grade C: the facts legally established are quotable, and a judgment's fact section has been tested in adversarial proceedings, which is the distinctive value of the grade, though the disputed issues may have shaped which facts were selected. Grade D: frame only, no details, because a party's own postmortem has not been adversarially tested. Grade E: a lead only, to be followed toward primary or secondary material and not cited until something is found. The table also sets house rules: an organization can decide that only A through C cards enter the library used as a basis for decisions, and with that rule standing, the library has a gate.

Link rot needs a policy, because rot is the norm. Sites get rebuilt, agencies merge, PDFs come down, in batches every year. Three layers answer it. Snapshot at first reading, archiving the page or keeping the local PDF. Register the dead link on the errata page with a substitute entry point. Downgrade where no substitute exists, following Appendix C, or convert the entry into a checkpoint. All three belong to the reading routine, and their cost is small: archive while collecting, click the batch once a year. They keep the book's citations checkable five years out, and checkability is the difference between a card library and a scrapbook of news.

## 5.2 Why Three Fields Carry the Value

Of the twelve, fields 2, 3, 4, 5, and 10 supply coordinates, fields 8 and 9 supply structure, and fields 6, 7, and 11 supply training. Strip 6, 7, and 11 from a card and what remains is indistinguishable from news. News tells you that something happened. Those three let you rehearse what you would have done.

Be honest about the cost. The three take more than sixty percent of the hours in one card: field 6 means checking phases along a timeline, field 7 means digging rejected options out of documents, field 11 means the full backward walk. Tooling answers it. Phase markers for field 6 come from a timeline template, the absence record in field 7 from a process comparison table, the backward walk in field 11 from the four questions in Chapter 10, and good tools compress the sixty percent to thirty. Tooling has a second payoff in consistency: cards by different authors reach the same level on the fields that matter, and a library that reads as though one person wrote it becomes possible. Templates sit in Part 5. This chapter's job is to say that the expensive part is expensive for a reason, and that it has tools.

The three relate in a fixed order. Field 6 fixes the information environment, since you can only decide with the cards on the table. Field 7 lists the real options that were on it, including the one never played. Field 11 points at the card whose replacement wins the hand. Together they make one repeatable drill: read field 6, write your own field 7, make your own choice, then turn the page and compare against the actors' choice in field 8 and the minimal intervention point in field 11.

The drill grades by difficulty, and one card can be worked three times. In the first round the card is open: field 6 gives the full information set, and what gets trained is the imagination of options. In the second the card is half covered: fields 7 and 11 are hidden, field 6 and the situation are given, and what gets trained is the handling of information. In the third the card is closed: only time, place, and subject are given, and the reader reconstructs what was visible and what the options were from industry knowledge before comparing, which trains the actual stock of that knowledge and usually stings most. Space the rounds a month apart, since repeating a card too soon contaminates memory and a longer gap keeps the comparison honest. The card is a dumbbell, the weights come in steps, and different weights work different muscles. This is the specific remedy for Chapter 2's attribution bias, and the reason every case in this book stops at the decision point.

Two variants serve readers at different levels. Solo: read field 6 and the situation, write your option list and your choice on paper, then compare. Writing is the point, since an unwritten choice is an imagining while a written one can be tested. Group: split a morning meeting in two, hand out the front of the card, keep the back with the facilitator, discuss the options, then reveal. The group variant buys option diversity, because a room generates a fuller list than one person and absent options surface more easily in company. Both cost about ten minutes per card, and both are the basic forms of the morning meeting script in Chapter 35, which is nothing more than the variants fixed into a procedure.

## 5.3 How to Use the Fields

Three uses. Writing a postmortem: Chapter 38 turns the twelve fields into a template and attaches a paragraph-by-paragraph rewrite of a "strengthen management" style postmortem. Reviewing: the question lists in Chapter 37 are grouped by mechanism, and their answers backfill fields 6 and 7. Building a ledger: an organization indexes its industry's cards by mechanism under field 5, sorts them onto a timeline by field 4, and distils check items out of field 11; that ledger is the ammunition for the rehearsal meeting in Chapter 39.

Two more uses are worth adding. External communication: when an event description goes to a regulator, a customer, or an insurer, the twelve fields are a complete materials list, and a party that prepares by field always has a page number ready when a question comes. The value is that failure knowledge becomes a negotiating asset, and the posture of a party with complete materials in accident communication, claim negotiation, and regulatory inquiry is a different posture. Teaching: an industry induction course can be taught from that industry's cards, which carry three parts less drama and seven parts less bias than an accident story, and ten parts more structure. A newcomer learns how the industry dies faster from cards than from legend.

The five uses converge. The twelve fields are the working language of the field, and someone who has learned them saves a layer of translation in every conversation with this book, with their own organization, and with outside parties.

One caution on the other side of the standard: the twelve fields are a floor, never a ceiling. Additions should still be governed. Use the twelve for three years before considering a thirteenth, and put a candidate through three gates: it has a clear downstream consumer, it has a fill standard that can be executed, and the cost of producing a card stays bearable with it added. The gates stop field inflation, the geriatric disease of every format, since each added field is a tax on every card already written. The exception to the tax is the optional field, marked optional, with no backfill of old cards and no obligation on new ones. Version the field set as Chapter 1 governs IDs, with v1 holding the twelve and v2 listing the optional additions. A format can stay alive, provided it stays disciplined.

Blank space on a card can hold any supplementary material. A case that cannot complete any one of the twelve is demoted to the appendix matrix, which accepts an ID, a domain, a mechanism, and consequences. The main text accepts nothing less.

Demotion runs both ways. A matrix card returns to the main text when the twelve fields are complete, the sources reach grade A through C, and the three key fields are written, and the return is reviewed on the same standard as first admission. Because the clause runs both ways, the matrix is a bench rather than a bin, and the bench matters because it keeps the route back open. Maintaining that route keeps a library alive: once a year, go through the matrix and ask which cards are close to promotion, which fields they lack, and what the path to filling them is. The review produces the work order for the next collection round. Chapter 28 makes the same argument about lists in general, that a list needs a destination. A bench means demotion is not an ending.

## Five Self-Checks

1. Write a twelve-field card for your organization's last major loss. Note which fields the first card cannot fill.
2. In your postmortem documents, which passages are information known only afterwards, written as though it were known at the time? Rewrite one passage.
3. At your last significant decision, which options were on the table? For each rejected option, who supplied the reason, and where is it recorded?
4. Can your organization state the point of no return for each of its key processes? Do the people who can state it hold rank enough to call a halt?
5. Take your industry's most recent investigation report and restate it using only the content of field 6. Has your conclusion changed?

One graduation standard sits beyond the five questions: complete one full card alone, from choosing the report to checking the citation, asking no one for help. Hand it to someone who has read this chapter and have them review it field by field against the requirements here. Their feedback is the final list of gaps between you and this chapter. A reader who clears that list can build a card library for any organization. What the skill is worth in the market, which Chapter 4 discussed as the scarcity of the circulating translator, and in governance, since the postmortem template in Chapter 38 takes this as its skeleton, is argued later in the book. Get the skill into your hands first. The occasions for using it will announce themselves.