# Chapter 5 The Twelve Fields of the Case Card

> What this chapter covers: the twelve fields of the case card — the analytic unit used uniformly throughout this book — each one defined, each given one badly written counterexample and one corrected version.
> When to turn back: when you write a postmortem of your own, review someone else's, or need to compress an investigation report onto a single page.
> Estimated reading time: 40 minutes.

A three-hundred-page investigation report is information-complete and hard to read; a postmortem article is easy to read and information-incomplete. The case card is the layer between: one page, twelve fields, hard requirements on each field, and a case that cannot fill the fields is not admitted to the main text. This chapter defines each field in turn and gives one badly written counterexample per field. The counterexamples all come from real postmortem and reporting prose; you will find the same species inside your own organization.

First, the twelve-field master table:

| # | Field | Hard requirement |
|---|---|---|
| 1 | ID | domain code-serial, unique across the book |
| 2 | One-line summary | ≤30 characters, states only what happened |
| 3 | Subject | organization + equipment/project, nameable down to model and registration number |
| 4 | Time and place | year-month-day + location |
| 5 | Domain and mechanism | domain code + main mechanism (up to 3 attachable; main mechanism first) |
| 6 | Visible at the time | timestamped information available to the decision-makers at the moment of decision |
| 7 | Options ruled out | options tabled and rejected, plus options that never reached the table |
| 8 | Decision point | who did what, in which meeting or on which document |
| 9 | Point of no return | the action after signature, go-live, takeoff, or pour |
| 10 | Scale of consequences | figures from primary materials; if none, write "no public quantification" |
| 11 | Minimal counterfactual | one action, changed, avoids the event; write exactly one |
| 12 | Evidence grade and source | grade A–E + full citation + link |

## 5.1 Definitions and Good/Bad Examples, Field by Field

### Field 1: ID

Definition: `domain code-serial`. Aviation av, chemicals ch, nuclear nu, healthcare me, pharmaceuticals ph, construction ce, maritime ma, software sw, finance fi, startups st, public policy po, military mi, manufacturing mn, agriculture ag.

Counterexample: "Accident Case No. 3" or "Compilation of Typical Cases in Our City in Recent Years (XI)". The serial hangs off a table of contents; revise the contents and the serial dies, severing every citation.

Correct example: `av-037`. Three years later, after a contents revision, this ID still points to the record of the Japan Airlines A350 and Japan Coast Guard aircraft collision. The ID is the anchor between this book and other materials, and the primary key of the master case table in Appendix B.

### Field 2: One-Line Summary

Definition: within 30 characters, stating only what happened. The test: the sentence contains no cause, no judgment, no adjective.

Counterexample: "Due to inadequate safety management and employees' weak safety awareness, an avoidable serious accident occurred." This sentence holds six information slots: four judgments (inadequate, weak, avoidable, serious) and zero facts.

Correct example: "737-9 door plug separates in climb; rapid decompression; return." Fifteen characters in the original Chinese, one action sequence: component, phase, consequence, outcome. The reader learns what happened, and neither knows nor needs to know, for now, why.

The operational method for this field: find the first moment on the accident timeline at which "something went wrong physically", and write it in subject-verb-object. "Door plug separated." "Jackscrew nut worn to failure." "Oxygen generator caught fire." Evaluative words come in later, if at all.

### Field 3: Subject

Definition: whose thing failed. Organization name, equipment model, nameable identifiers (flight number, registration number, construction lot).

Counterexample: "an aircraft operated by a certain airline." The moment "certain" appears, the case degrades into parable: unverifiable, unextendable, its condition layer unconfirmable.

Correct example: "Alaska Airlines 1282, Boeing 737-9 (N704AL)." The subject is checkable, citable, its condition layer complete (the model determines the airworthiness background, the airline determines the maintenance system, the registration number allows history lookups in public databases).

Where naming carries legal risk (a judgment not yet final, a penalty not yet published), drop one level: name the industry and category, and note "why the subject is not named".

### Field 4: Time and Place

Definition: the event's year-month-day and location, precise to the day. The publication date of the investigation belongs in field 12; keep the two apart.

Counterexample: "early 2024" or "last summer". The start and the end of a year are eleven months apart — enough for a full maintenance cycle.

Correct example: "2024-01-05, Portland, Oregon, USA, about 20 minutes after takeoff" (NTSB AIR-25-04). The time stamp fixes the information environment: weather bulletins issued before that day, maintenance records, meeting minutes — all within "visible at the time"; everything after that day counts as hindsight.

### Field 5: Domain and Mechanism

Definition: domain code plus main mechanism; up to three mechanisms may be attached, the first being the main one. Mechanism names come from the twenty-four-term vocabulary (Chapters 11–34); inventing new ones is not allowed.

Counterexample: "management problems", "human factors", "systemic risk". These three phrases appear in the conclusion paragraphs of most postmortems; they can hold anything, and therefore explain nothing.

Correct example: "av; invisible maintenance; procedural drift." Attaching mechanisms is itself an act of attribution; if you cannot attach them accurately, attach only one. When the same case is cited in different chapters, its main mechanism stays fixed, preventing case drift: the same event retold in each chapter as a story supporting that chapter's thesis.

### Field 6: Visible at the Time

Definition: timestamped information available to the decision-makers at the moment they decided. Sources are limited to records whose phase can be fixed from the materials: meeting minutes, work orders, the release time of weather forecasts, the previous shift's handover notes. Anything learned only afterward stays out of this field, without exception.

Counterexample: "hidden dangers had long existed, and management cannot escape responsibility." "Had long existed" erases every piece of time information: existing for how long? Who saw it, and when? Was anyone who saw it obliged to report it?

Correct example: in the Alaska Airlines 261 case (NTSB AAR-02/01), the information visible at the time included: inspection records from before the lubrication and check intervals were extended; the application for the interval-extension scheme and the Federal Aviation Administration's (FAA) approval documents; the flight crew's reports, on the accident flight, of abnormal jackscrew position and unusual cabin noise. Each item carries a date on which it entered someone's field of view. The wear on the nut's threads found in teardown after the accident is post hoc information and cannot enter this field.

This is one of the two fields with the highest value density in the book (the other is field 11). Its purpose is to shut Chapter 2's attribution bias outside the reasoning: only what the actors could see at the time is admitted. Chapter 6 is devoted entirely to operating it.

### Field 7: Options Ruled Out

Definition: options placed on the table at the decision point and rejected, plus options that by rights should have appeared and never did. Record both, marked to distinguish them.

Counterexample: "had they been more careful, it would not have happened." "More careful" is a nonexistent option: no action, no cost, no decision-maker. Writing it equals writing nothing.

Correct example (format demonstrated with Challenger, Rogers Commission report 1986): on the teleconference call on the evening of January 27, 1986, the options on the table were: launch on schedule on January 28 (selected); delay until daytime temperatures rose (rejected, on grounds of schedule pressure); honor the engineers' proposed threshold of no launch below 53 degrees Fahrenheit (about 12 degrees Celsius) (rejected — launches at still lower temperatures had already succeeded multiple times). The absent option: reopen the question of why the launch temperature threshold had been sliding downward launch by launch. (Rogers Commission report, Volume 1, Chapter 5, records that Thiokol engineers recommended against launch below 53 degrees Fahrenheit, based largely on blow-by data from flight 51-C; official full text at nasa.gov/history/rogersrep/v1ch5.htm, read and verified for this book, November 1, 2026)

The value of ruled-out options lies in exposing the structure of decision: how options get generated, how they get rejected, who is entitled to put them on the table. Most organizational postmortems record only "what was chosen" and omit "what else was choosable" — so the same option-generation machinery produces the same menu at the next decision.

### Field 8: Decision Point

Definition: the four elements — person, meeting, document, action: who made what decision, in which meeting or on which document. Dates must fall on the day.

Counterexample: "company management made the wrong decision." No name, no meeting, no document — a sentence that can neither be contested nor cited.

Correct example: Alaska Airlines 261 (NTSB AAR-02/01 executive summary): Alaska Airlines extended the lubrication interval and the end-play check interval for the horizontal stabilizer jackscrew assembly, and the FAA approved both extensions; the investigation found that the extended intervals allowed lubrication missed under the original schedule to progress to excessive wear and then to failure (text in the report's executive summary, in the portions I verified). All four elements present: the company (who), the documents and approvals (the carrier), the interval extension (the action), the FAA approval (the gatekeeping action).

### Field 9: Point of No Return

Definition: the moment after which the event's main consequences can no longer be undone by ordinary means. The test appears in Chapter 7: money can undo it, time can undo it, a public correction can undo it — a signature and a go-live cannot.

Counterexample: "from the moment the project started, failure was already destined." Fatalism is a poor definition of the point of no return; it folds every decision point into one, erasing every intermediate position where intervention was possible.

Correct example: in the Japan Airlines flight 516 event (av-037), the point of no return was the moment the combination formed — the Coast Guard aircraft on the runway while the A350 crew held landing clearance; from then on, the two aircraft's speeds and remaining distance made collision an event that most operational paths could not avoid. For assembly-type cases the point is clearer still: the door closed, the concrete poured, the reactor synchronized to the grid — every minute of work afterward is paying the fare for that action.

### Field 10: Scale of Consequences

Definition: figures from primary materials. Deaths, injuries, losses in money, downtime, units recalled — write whatever exists, with the source named. With no figures, write "no public quantification".

Counterexample: "caused enormous economic losses and a bad social impact." Enormous is how much? Bad down to what degree? The sentence's only function is to occupy space.

Correct example: "0 deaths; 7 minor injuries (all passengers); 169 uninjured; aircraft substantially damaged" (av-030, NTSB AIR-25-04). Four figures, each with its own basis of measurement, from the same report.

"No public quantification" is a legitimate answer. It means the case's consequences never entered any primary document; it does not mean the consequences were zero.

### Field 11: Minimal Counterfactual

Definition: the one action which, changed alone, would have avoided the event (or shrunk its consequences drastically). Work backward from the latest action that did not depend on luck. Book-wide discipline: write exactly one.

Counterexample: "had management been strengthened, systems improved, awareness raised, and supervision intensified, the accident could have been avoided." Four actions equal zero actions: the reader cannot tell which to do first, and so does none.

Correct example: Alaska Airlines 261 (AAR-02/01): leave the end-play check interval unextended and inspect on the original schedule, and the wear had its chance of being detected before it progressed to failure. One action, at the latest position on the chain of decisions actually made, dependent on no luck of the "happened to be found" kind. (AAR-02/01 executive summary p.4 and the Safety Board's statistical study of end-play data in section 1.18.2; PDF verified)

This field is a training device. Writing it forces the author to answer: where, along the whole failure chain, lay the minimal intervention point? Chapter 10 gives the full backward-walking method. Two counterfactuals equal none: readers will remember the easy one, and the easy one is rarely the minimal intervention point.

### Field 12: Evidence Grade and Source

Definition: grade (A full independent investigation report / B official bulletin or communiqué / C judgment or penalty document / D public postmortem by the party involved / E media lead) + full citation + link. Rule: E-grade material may never serve as the sole source for a case in the main text.

Counterexample: "as reported by multiple media outlets." When many outlets retell the same wire story, "multiple" is a fake number.

Correct example: "Grade A. NTSB, Aviation Investigation Final Report DCA21FA085, 2023; link at Appendix B av-006."

The citation must resolve to a document name and number, and the link must have been opened by hand. No exceptions to this one: it is the collateral behind every claim of credibility the book makes.

## 5.2 Why the Three Key Fields Are Where the Value Lives

Of the twelve fields, 2, 3, 4, 5, and 10 supply coordinates; 8 and 9 supply structure; 6, 7, and 11 supply training. Strip fields 6, 7, and 11 from a case card and what remains is indistinguishable from news: news tells you something happened; these three let you rehearse "if it had been me, what would I have done".

The logical relations among the three: field 6 fixes the information environment (you can only decide with the cards on the table), field 7 lists the real options on the table (including the one never played), field 11 points to the card whose swap wins the whole hand. Together they compose one repeatable training move: the reader reads field 6, lists field 7 alone, chooses alone, then turns the page to compare against field 8's actual choice and field 11's minimal intervention point. This is the targeted cure for Chapter 2's attribution bias, and the reason every case in this book stops at the decision point.

## 5.3 Putting the Fields to Work

Three uses. Writing a postmortem: Chapter 38 turns the twelve fields into a postmortem template, with a paragraph-by-paragraph rewrite of a "strengthen management" style postmortem attached. Reviewing: the question lists of Chapter 37 are grouped by mechanism, and the answers backfill fields 6 and 7. Building a ledger: an organization indexes its industry's case cards by mechanism (field 5), lines them up on a timeline (field 4), and distills check items from field 11 — this ledger is the ammunition store for Chapter 39's rehearsal meeting.

A caution on the other side of the standard: the twelve fields are a floor, never a ceiling. A case card's margins may hold any supplementary material, but a case unable to complete any one of the twelve is demoted to the appendix matrix: the matrix accepts ID, domain, mechanism, and consequences alone; the main text never does.

## Self-Check: Five Questions

1. Write a twelve-field card for your organization's most recent major loss, and see on which fields the first card cannot be filled.
2. In your own postmortem documents, which passages count as "information known afterward written as if known at the time"? Rewrite one of them.
3. At your last major decision, which options were on the table? For each rejected option — who gave the reason, and where is it recorded?
4. Can your organization state the point of no return for each of its key processes? And does whoever can state it hold rank enough to call a halt?
5. Take your industry's most recent investigation report and retell it using only the content of field 6 (visible at the time). Has your conclusion changed?

(First draft of this chapter: 4675 characters; to be expanded as case examples are added)
