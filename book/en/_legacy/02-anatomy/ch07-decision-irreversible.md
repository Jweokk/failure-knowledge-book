# Chapter 7 Decision Points and Points of No Return

> What this chapter covers: how to identify the two most valuable positions on a failure chain — the decision point, where the track can still be switched, and the point of no return, where it no longer can — with a reversibility test table you can apply directly.
> When to turn back: when setting checkpoints in a process, defining signature authority, or judging "is there still time to brake".
> Estimated reading time: 40 minutes.

Every moment on a failure chain deserves your attention only in small measure; most moments are merely the event advancing. At a few moments, someone stands at a fork holding roads not yet taken. This chapter supplies two tools: recognizing the fork (the decision point), and recognizing, past the fork, the step from which no road leads back (the point of no return). Both tools come with one test table.

## 7.1 The Decision Point: Three Necessary Conditions

Definition: a moment satisfying three conditions at once is a decision point.

Condition one: at least two real options exist. Real means: the option has a concrete action, a concrete cost, and could have been chosen at the time. "Being more careful" is not an option; "delaying until the next day, when daytime temperatures rose" is one (the option rejected in the Challenger case; Rogers Commission report, 1986).

Condition two: the person with authority to choose sits within reach. In the meeting room, on the other end of the line, at the next node of the approval flow. The commonest form of options laid on the wrong table: the one who could actually veto is absent, while those present believe they hold no veto. The core symptom of Chapter 18's responsibility diffusion is precisely the collapse of this condition: everyone present, no one feeling authorized to call a stop.

Condition three: the consequences of the choice appear later. Time separates decision point from consequence, and that interval is both a window for repentance and a hothouse for illusion. Deferred appearance supports two readings — "we chose right, since nothing happened" and "our turn has not come yet". Telling the two apart waits for Chapter 11 (normalization of deviance); here, hold only this: a deferred decision is psychologically free and never free on the ledger.

Moments satisfying all three conditions usually appear more than once on a failure chain. The discipline for writing and for postmortems is to take the latest one: the latest decision point on the failure chain is the anchor of the minimal counterfactual (field 11 of Chapter 5; Chapter 10 gives the full backward-walking method). The latest decision point carries the lowest intervention cost, sits closest to the consequence, and holds the most complete evidence.

One further distinction needs planting: a decision point and a point of accountability are two different things. The postmortem chases decision points (where the track could be switched); courts and disciplinary processes chase points of accountability (who owes a legal duty for the consequence). The two often coincide, yet the coincidence is luck rather than necessity: the latest feasible switch point may sit in the hands of someone with no authority, while the authorized narrowed the options to zero at several earlier positions. Take the courtroom's answer as the postmortem's answer, and the organization learns "sign carefully" while missing the lesson of "who narrowed the options, in which meeting, on what reasoning". Here Chapter 2's attribution bias takes an institutionalized form: accountability procedures converge on the point of accountability by nature, and the postmortem must resist that gravity.

## 7.2 The Three Currencies of Reversibility

Irreversibility is a spectrum, never a switch. Decompose "undoing an action" into the capacity to pay in three currencies:

Currency one: money. After the action, can money buy it back? Rebuild a part, switch suppliers, recall a batch. Money works while the thing is unused, unconsumed, ungrafted onto something else. A bad supplier on the approved list costs a switching fee to replace; concrete already poured into a wall, no sum buys back.

Currency two: time. After the action, can waiting undo it? Postpone the release, the takeoff, the construction window. Time works while the window stands open: before it closes, postponement is a costless undo; after it closes, the same action jumps from the "reversible" column into the "irreversible" one with no transition in between.

Currency three: credibility. After the action, can it be publicly withdrawn? A correction notice, a recall statement, an apology with compensation. Credibility works while nobody has yet taken an irreversible action of their own on the strength of your announcement: correcting a notice nobody acted on costs little; correcting a standard the downstream has been executing for six months costs according to the breadth of that execution.

What no currency can buy back forms the fourth category: signatures and go-lives. The release engineer signs the airworthiness release, the software's deploy button is pressed, the aircraft completes its takeoff roll, the reactor synchronizes to the grid, the drug enters prescriptions, the announcement goes out. These actions share one structure: a statement has been made to the world ("this thing is good"), the world has begun acting on the statement (passengers buy tickets, clients call the interface, doctors prescribe), and withdrawal is decided by what others have already sunk, never by your capacity to pay.

One-line test — the expanded version of Chapter 5's field 9: money can undo it, time can undo it, a public correction can undo it; a signature and a go-live cannot.

## 7.3 The Reversibility Test Table

Turn section 7.2 into a table you can apply directly. For the action under evaluation, answer row by row:

| Row | Question | "Yes" means | "No" means |
|---|---|---|---|
| 1 | Does undoing it cost within the normal budget? | Money-reversible | Move to the next row |
| 2 | Does an unclosed window still allow postponement or redo? | Time-reversible | Move to the next row |
| 3 | Can the external commitment be withdrawn, with nobody yet having acted on it? | Credibility-reversible | Move to the next row |
| 4 | Is the bearer of the undo cost identified, and does that bearer consent to bear it? | Executable | Irreversible, even if rows 1–3 answered "yes" |
| 5 | Does a second confirmation point still stand between action and effect? | One intervention slot remains | You have reached the point of no return |

Reading: the count of "yes" answers in rows 1–3 gives the reversibility grade (all three present: reversible; two or more missing: irreversible); row 4 carries a single-vote veto; row 5 tells you whether one last intervention slot remains.

The table has three uses, one per kind of person. The decider: fill it in before acting; the moment row 5 answers "no" is your point of no return — write it into the decision record. The process designer: place a second confirmation point ahead of every point of no return, and set the confirmation point's minimum information standard (Chapter 6's visible at the time). The postmortem writer: mark the point of no return on the failure chain, then examine what happened at the last second-confirmation slot before it.

## 7.4 Points of No Return in the Cases

Case one: the 737-9 door plug (av-030, NTSB AIR-25-04). The point of no return was the door closing on the final assembly line, the aircraft passing into delivery and service. Before that position, a single records check on critical-area opening work (manual, or forced by system) could have stopped everything downstream; after it, the risk entered the life ledger of the 176 people on board (169 uninjured and 7 with minor injuries; figures from AIR-25-04), and the currency of withdrawal switched from person-hours to lives. The design-view question is therefore very concrete: in the factory's release chain, was the information "critical area had been opened" entitled to trigger a mandatory re-check? At the time it triggered none — and that is the generating condition taken up by Chapter 29 (invisible maintenance) and Chapter 15 (procedural drift).

Case two: Alaska Airlines 261 (av-034, AAR-02/01). This case contributes a fine-grained type to the test table: an institutional decision's irreversibility realizes itself one installment at a time. The approval to extend the check intervals (company application, FAA approval) was itself reversible — the intervals could have been set back; but from the day the approval took effect, every flight released under the new intervals was a micro point of no return: the aircraft flew carrying components no longer checked to the original standard. The failure did not happen on the day of approval; it cashed out on one of the dozens of successive releases. Recognizing this "installment-realized irreversibility" means counting the exposures: the more often an institutional decision is exposed, the less negligible the cumulative probability of a single deviation — the arithmetic foundation of Chapter 11's normalization of deviance.

Case three: the Haneda runway collision (av-037, JTSB Interim Report No. 2, 2025). The point of no return was the moment the combination formed: the Coast Guard aircraft on the runway with the A350 holding landing clearance. From then on, the option space left to the two aircraft was set by speed, distance, and lighting conditions, and the entire value of the postmortem lies before the point of no return: the check before the stop line, the readback and understanding of the control instruction, the cockpit's visual search for runway occupancy. The final report (unreleased as of this book's writing) should concentrate its hypothesis space on the same segment; material from the interim-report stage carries grade A-minus (an independent investigation body's document, though not the final one) — keep the minus sign when citing (use of evidence grades in Chapter 10).

## 7.5 Designing Your Own Points of No Return

Beyond identification, this chapter's output should be design moves. Four of them:

Move one: place a second confirmation slot ahead of every point of no return, and set the slot's information threshold. Aviation's release order is the most mature template: the checks required before signing are listed item by item on the form, and a signature declares "every item on the form has been verified". Every go-live, loan release, product launch, and public announcement in your organization deserves an equivalent form.

Move two: give irreversible decisions a cooling-off period. Judging "is it reversible" costs far less than judging "is it right" — most of all for the third currency (credibility): public announcements and public commitments, without exception, wait one night. The overnight rule filters impulse far more reliably than it filters outright error — and impulse is the larger share of the problem.

Move three: write the point of no return into the decision record. Three lines: what moment the point of no return was, where the last second-confirmation slot before it stood, and what the visible-at-the-time information then was (Chapter 6's two columns). Three years on, this record is the only raw material a postmortem can still use.

Move four: the signer is the terminal of responsibility; a chain of signers is the absence of responsibility. State in contracts, processes, and job descriptions: who signs for this action's point of no return, and whether the signer holds unilateral authority to halt. Chapter 18 will show the case structure in which seven signers equal zero signers.

## Self-Check: Five Questions

1. Write down three points of no return in your project over the coming thirty days, and test each against the table in section 7.3.
2. What was your organization's most recent case of "money-reversible allowed to drift into irreversible"? Was the drifting done by the process or by a person?
3. Of the signatures you have signed, on how many did you fail to verify the items one by one? Can you afford that ratio?
4. At your process's last second-confirmation slot, does the check examine records or the physical thing? Do the two fail in the same way?
5. Does your organization carry "installment-realized" irreversibility — a reversible institutional decision accumulating exposure through every routine release? Can you count the installments?

(First draft of this chapter: 3362 characters; to be expanded as case examples are added)
