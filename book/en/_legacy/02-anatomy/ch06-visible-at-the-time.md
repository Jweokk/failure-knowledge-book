# Chapter 6 Visible at the Time

> What this chapter covers: how to drive the hindsight perspective out of your postmortems and your reading: three operating disciplines, one test, three worked examples.
> When to turn back: when writing a postmortem, reading one, reviewing a design, or catching yourself saying "they should have seen it coming".
> Estimated reading time: 45 minutes.

The great enemy of the postmortem is a psychological fact: someone who knows the ending can no longer re-experience the thinking of someone who does not. This chapter supplies an operating discipline that keeps the contamination from that fact to a minimum. The discipline has three rules: use only timestamped materials, use only information the actors could obtain, and sequester everything learned later. Executed together, the three lock hindsight outside the door.

## 6.1 Why the Rearview Mirror Cannot Be Shut Off

Psychological experiments of the 1970s gave the phenomenon its name. Baruch Fischhoff's classic study had two groups read the same historical scenario, one told the outcome and one not; the outcome-told group systematically judged that outcome "more likely all along", and were unaware that knowing the ending was why they thought so (Fischhoff, "Hindsight Foresight: The Effect of Outcome Knowledge on Judgment under Uncertainty", 1975 — full citation: Fischhoff, 'Hindsight-foresight', Journal of Experimental Psychology: Human Perception and Performance 1(3): 288–299, 1975; bibliographic record verified via Crossref). Later research gave the effect a plainer name: creeping determinism — once the ending is known, memory rewrites the process into a one-way road leading to it.

Inside organizations the consequences run deeper than in the laboratory, because postmortems are written by people who know the ending, for readers who will know it too. Three layers of contamination stack: the author knows the outcome, the reader knows it, and both feel it was "obvious at the time". Postmortems therefore fail to train judgment: on paper, every fork looks like open road; the reader assumes he too would have seen it, returns to the field, and finds information arriving mixed with noise.

Accident investigation agencies maintain a whole set of procedural defenses against this. Reports of the NTSB type split "facts" and "analysis" into two parts: the facts section admits only sourced, phase-fixable material; the analysis section, when it reasons, annotates every statement with the fact it rests on. The structure's deeper function is to sort events by time: for any statement, first ask whether it occurred before the accident or after. This chapter's discipline compresses that procedure into three rules an individual or team can run directly.

## 6.2 Discipline One: Use Only Timestamped Materials

Operational definition: every item of information admitted to the "visible at the time" set must answer "at what moment did this information enter whose field of view". Only what can answer that may serve as input to the actors' decision.

Timestamped materials include: meeting minutes (date, attendees, order of agenda), work orders and checklists (completion time, signatory), the release moments of weather and market data, the timelines of recordings and chat logs, the sequence of approvals in a workflow. Materials without timestamps include: participants' recollections, summary reports, press retellings, undated statements like "hidden dangers had been found repeatedly before".

One aviation case demonstrates how strong this discipline is. In the fact chain of Alaska Airlines 261 (NTSB AAR-02/01), the timestampable items include: the application documents for extending the lubrication and end-play check intervals, with the FAA approval dates; the crew's in-flight reports to the ground of abnormal stabilizer jackscrew position (with call times); cabin reports of unusual noise (with times). The wear morphology of the nut's threads found in the post-accident teardown, and the laboratory metallurgical analysis, have no moment of "entering anyone's field of view at the time" and go wholly into the hindsight column. With the two columns separated, the reader sees the hands plainly: the decision-makers held the cards "the intervals were extended by us ourselves" and "the aircraft has started reporting abnormal position"; they never held the card showing what the nut's threads already looked like.

The high-frequency error in practice is treating "the information existed somewhere in the organization" as "the decision-maker could see it". Between existing and visible lie four gaps: channel, format, timing, language. A test report buried on the ninth folder level of a shared drive does not exist, as far as the engineer making a release decision in the middle of the night is concerned. To judge visibility, ask four questions: did it enter the channel the actor actually used (the night desk reads the duty system, never the shared drive)? Could its format be read on the spot (an English-language raw report, for a night-shift assembler)? Did it arrive before the action or after it? Could its magnitude be grasped on the spot (one critical figure inside a hundred pages)?

## 6.3 Discipline Two: Use Only Information the Actors Could Obtain

The direct corollary: every piece of "data at the time" you cite in a postmortem must state whose hands it was in. The distribution of the same information across an organization decides its value. The risk department knew the customer-concentration limit had been breached, but the lending decision belonged to a branch manager whose system showed only customer revenue rankings. A postmortem that writes "the bank lent despite knowing the concentration limit was breached" has placed the risk department's knowledge inside the branch manager's field of view, where it never was. The accurate version: "the branch's lending system interface carried no customer-concentration field; the field appeared only in the head office's monthly risk report (report date: the 15th of each month)." The two sentences describe one organization; the first invents a decision-maker who never existed.

The Challenger case displays the necessity of this discipline most completely. On the teleconference call on the evening of January 27, 1986, the engineers' hand contained: O-rings from booster joints recovered after previous flights showing erosion and blow-by (with flight numbers and photo records); a statistical association between these signs and cold temperature; the joint's worst performance at the lowest launch temperature to date. Their hand did not contain: on-site high-speed imagery (which comes into existence only after the accident), the precise sequence of the joint's failure (reconstructed afterward), data on the second O-ring's dynamic behavior at low temperature (filled in by later experiments). The decision in that meeting was made under the first hand alone. The Rogers Commission report can support organizational-layer attribution precisely because its evidence chain keeps the two hands strictly apart. (Each card in the engineer's hand is traceable in the Rogers report, Volume 1: the flight-numbered erosion and blow-by history and Thiokol's July 31, 1985 memo warning of "a catastrophe of the highest order" sit in Chapter 6, "An Accident Rooted in History"; the meeting itself, with the engineers' photos and sketches entered as evidence, sits in Chapter 5. Official full text at nasa.gov/history/rogersrep/, read and verified for this book, November 1, 2026)

## 6.4 Discipline Three: Sequester Whatever Was Learned Later

On the page, this lands as two columns. Left column, "visible at the time"; right column, "reconstructed afterward", with each right-column entry noting how it became known (teardown, interview, experiment, data analysis). The columns must never interleave, and any sentence borrowing from the right column to support left-column reasoning gets rewritten or deleted.

| Visible at the time (left column) | Reconstructed afterward (right column) |
|---|---|
| Around 20:00 on January 27, contractor engineers recommended on a teleconference against launching below 12 degrees Celsius | Launch imagery shows joint gas leakage beginning around the 58th second after liftoff (teleconference account per Rogers report Vol. 1 Ch. 5; verified full text at nasa.gov/history/rogersrep/v1ch5.htm) |
| Erosion records for O-rings recovered from earlier flights (flight numbers checkable) | Laboratory cold-temperature elasticity test data (conducted after the accident) |
| Contractor management reversed position and approved launch after a pause of roughly 30 minutes | Vaughan's 1996 quantified reconstruction of the downward slide of launch temperature thresholds |

The value of the two columns lies in the right column's mere existence: it openly admits which content is hindsight, exposing the author's and readers' shared illusion on paper. The interleaved postmortem never writes the words "afterward", yet leans on hindsight in every sentence; the two-column postmortem forces such sentences into the annotation column, where they stand in plain sight.

## 6.5 The Test: Three Signal Families and One Dissection

A quick test for readers. When a narration contains any of the following three families of signal words, the hindsight perspective is doing the talking:

Signal family one: "if only, at the time, ..." A counterfactual inside process narration shows the author filtering the process through the outcome.

Signal family two: "had they known / to everyone's surprise / unexpectedly / nobody saw it coming / and yet." The subject of these words is someone who knows the ending, never the actor.

Signal family three: "in fact, at the time, ... had already ..." Behind every "in fact" hides a piece of information with no timestamp. Chase it down: who saw it, when, through what channel?

For depth, use dissection. Break the narration into event cards, each card carrying two lines: the moment the event happened, and the moment the information reached the decision-maker's field of view. The gap between the two lines is the hindsight content. Do this once and you will find that on most of your own cards the two lines carry the same moment — because as you wrote, you quietly promoted the ending into the information environment of the time.

## 6.6 Three Worked Examples

Walkthrough one: rewriting an Alaska Airlines 261 postmortem.

The hindsight version: "the jackscrew nut's threads were already severely worn, the safety margin exhausted; crashing into the sea was only a matter of time." Three hindsight components sit in this sentence: degree of wear (knowable only on teardown), "margin exhausted" (an analysis conclusion), "only a matter of time" (inferred backward from the ending). The visible-at-the-time version: "on the accident flight the crew reported, in succession, abnormal stabilizer position and motor overload, with call records of repeated attempts and communication over roughly ten-plus minutes; the assembly's lubrication and check intervals had previously been extended on the company's application, with FAA approval (AAR-02/01 executive summary p.4, verified)." Both versions describe the same event. The first teaches the reader "watch out for wear"; the second teaches "watch the decision chain that extended the intervals, and the procedure for handling abnormal signals". The first cannot be acted on; the second can.

Walkthrough two: the 737-9 door plug (av-030, NTSB AIR-25-04).

Among the safety issues listed in the report's executive summary is the state of work on the door area during final assembly at Boeing's Renton factory. Sorted by the two-column discipline: on the visible-at-the-time side sit the operational fact, inside the assembly flow, that "this door had been opened for riveting rework", together with the work-order record states along the release chain; on the hindsight side sit the laboratory confirmations, after the accident, that four positioning bolts were missing with no record of reinstallation (AIR-25-04 PDF pp. 10, 22, 26, verified). Standing at the release node, what the actors could see was "records incomplete"; what they could not see was "bolts missing". A postmortem that writes "they knew the bolts were not installed and released anyway" has stuffed the right column's physical evidence into the left column's heads. The accurate question lives in the left column: how did work on a critical area with no reinstallation record pass down the release chain without triggering any additional confirmation? That question points at structure (work on critical areas, once its records are incomplete, should itself trigger manual re-check), with remedies in Chapter 29 (invisible maintenance) and Chapter 15 (procedural drift); the "they knew and did it anyway" attribution points at nothing.

Walkthrough three: the R44 that took off at night in fog (av-021, NTSB CEN23FA125).

Visible at the time: the pilot's night-flight qualification and instrument experience status (checkable in person and in records), the pilot's own visual reading of the weather at the departure point, night visual conditions before departure and in the direction of the destination. Reconstructed afterward: the flight track rebuilt from ADS-B data (ground impact within an extremely short distance after takeoff). A postmortem that writes "he did not know he had entered dense fog" breaks discipline two: whether he "knew" cannot be proven from the materials; what can be proven is the climb and the turn he executed at that moment. Write actions, leave minds out — the implementation here of writing rule 2 from Chapter 5's case method.

## 6.7 The Limits of the Discipline

The three disciplines carry an honest boundary: in most organizations, timestamped materials do not cover every key decision. Meetings without minutes, decisions made in hallways, verbal orders leaving no trace — the organization's own recording gaps will thin the "visible at the time" column itself. This is a diagnostic result, never a failure of the discipline: a key decision point of some failure bearing no timestamped record at all is itself a failure report on the organization's record-keeping system (Chapter 38 lists a "record-keeping requirement" as a standing clause of the postmortem system). Gaps in the record must be marked as gaps; filling them from memory is not permitted.

## Self-Check: Five Questions

1. Take your most recent postmortem and scan it with the three signal families of section 6.5. How many hits?
2. In your organization, what key information lives somewhere in a system yet never appears on the decision-maker's screen? Name the system and the field.
3. For your last major decision, can you reconstruct the timestamped arrival sequence of information? Where reconstruction fails, is the record missing, or is it your memory?
4. Does your team's postmortem template separate "visible at the time" from "reconstructed afterward"? If not, whose resistance will adding the column meet?
5. Rewrite one paragraph of a recent public postmortem in your industry using the two columns — three entries per column.

(First draft of this chapter: 3986 characters; to be expanded as case examples are added)
