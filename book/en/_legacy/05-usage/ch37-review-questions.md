# Chapter 37: The Design Review Question List

> What this chapter covers: 130 review questions, grouped into a universal set and the twenty-four mechanisms; each annotated with what an unanswered question means. Usage: use the Chapter 35 assessment table to pick the groups your situation hits, then pass each question in turn.
> When to turn back to it: at design reviews, decision meetings, due-diligence interviews, or when setting an examination for a downstream team.
> Estimated reading time: no need to read it in one sitting. This is a tool page.

Three lines of instructions. First, use the questions by group: whichever mechanisms the assessment table hits, take those groups plus the universal group; twenty to thirty questions is the ceiling for one review — reading the whole list straight through is an editing act, not a review act. Second, the "→" after each question gives the meaning of an unanswered question; writing that meaning into the minutes is more useful than pressing for an answer. Third, answers must land on dated evidence; verbal assurances count as "no answer."

## Where the 130 questions came from

None of the hundred and thirty questions descends from theory. Each traces back to a decision-point field in the book's case cards: at each case's decision point, the files asked "what lay on the table, and what question did nobody ask out loud" — and the nobody-asked question, rewritten as something you can be asked today, became an entry here. The Alaska 261 card carried "whose inspection records support the extension?" (information from the user side only); it became the prototype of the Chapter 11 set's third question. The Travel + Leisure card carried "who independently reviews a caliber change?"; it became the universal set's question seven. The Grafton card carried "after the alarm sounds, who is required to stop what they are doing?"; it maps onto the Chapter 16 set's second question. This origin story fixes the library's nature: it is a decision-point index of a case collection, with a real, paid-for scene standing behind every question. It also explains the uniform wording — "can you answer…" rather than "did you do…". The organizations that paid these tuitions nearly all had procedures and files; what they lacked was someone at the decision point asking the question and demanding an answer.

One more distinction keeps the tool honest: criteria versus questions. A mechanism chapter's criteria answer "has the mechanism started?" — evidence required. The questions answer "does your organization hold any working knowledge of this mechanism?" — an admission of ignorance suffices. In self-audit, run the questions first: they sieve for cognitive black holes cheaply; the criteria then confirm, at the cost of real evidence-gathering, whether the mechanism is actually running. Questions before criteria — the cheap tool goes first.

## How to run the interrogation meeting

A fixed protocol, four phases.

Phase one: set selection before the meeting (ten minutes, the chair). Take the universal ten plus the sets for the located mechanisms, twenty to thirty questions total, into the agenda. Under each question, three lines: answer, evidence (date plus source), verdict (answerable / dark / refused).

Phase two: the pass (ninety seconds per question). The chair reads each question aloud; the named respondent answers with dates and sources; adjectives without dates count as no answer. Ninety seconds without dated evidence means a verdict of dark — no debate, no explanation, no padding. The count of dark marks is the meeting's principal product.

Phase three: disposition of the darks (fifteen minutes). For each dark: what evidence is missing, who supplies it by what date, and who reviews it when it arrives. A dark that cannot be dispositioned (the evidence does not exist and cannot be created) escalates to a design gap and enters the conclusion page of Chapter 36.

Phase four: minutes (five minutes). One page: the dark list plus the disposition commitments, with a verifier under Chapter 36's selection standard.

The two disciplines most often dropped are the time limit and the blunt verdict. Without the clock, the interrogation decays back into a briefing; with explanations allowed, adjectives re-flood the channel. Ninety seconds and the word dark, applied without exception, are the entire secret of turning a document into an instrument.

What minutes look like: a redacted sample (three dark entries; details fictional). "Q7 (caliber-change review): dark. Missing: the automated dependency list does not cover three legacy integrations. Fix: architecture to produce a legacy-integration list within two weeks. Read: standing item at the next review. Q9 (the fate of the last person who stopped something): dark. Missing: no records exist. Disposition: not a fixable gap — escalated as a design issue (stop-work clause into the project charter). Q8 (date of last dependency-list update): answerable. Evidence: register of dependencies, 2026-09-14, independent review signature: risk partner." Three entries, three dispositions: fixable (a name and a date), unfixable (escalate as design), and green (evidence cited). Greens go into the minutes too — six months from now, a review needs to know which lights were on as much as which were dark.

## The universal ten (every review starts here)

1. At which second does this action cross its point of irreversibility? → No answer = the decision-maker has never come face to face with the irreversibility (Chapter 7).
2. Who is the last second-confirmation position before the point of irreversibility, and what do they check? → No answer = the line of defense is nominal.
3. Of the information this decision rests on, which items carry timestamps? → None = the decision is built on secondhand accounts (Chapter 6).
4. If all investment went to zero tomorrow, who would lose the most? → No answer = nobody has ever priced exit (Chapter 27).
5. Who holds unilateral authority to halt this, and in which document is it written? → No answer = the authority to halt does not exist (Chapter 18).
6. In the most recent anomaly of this kind, did the attribution enter a ledger? → No answer = the anomaly was explained away (Chapter 8, Step One).
7. Who independently reviewed the last change of statistical definition? → No answer = the ruler is being swapped (Chapter 12; Chapter 8, Step Five).
8. When was the list of critical dependencies (third parties, suppliers, single systems) last updated? → No list = the dependencies are invisible (Chapters 21, 33).
9. What was the professional fate of the last person who stopped a project? → No answer = stopping is a career risk (Chapters 19, 27).
10. Where does the person who will pay for today's decision three years from now sit at this moment? → No answer = maturity mismatch is running (Chapter 28).

## Normalization of deviation (Chapter 11)

1. How many times has this kind of deviation occurred so far, and on what basis was each judged consequence-free? → No ledger = normalization is already running.
2. In "we still have margin," is margin a number or an adjective? → An adjective = the standard is softening.
3. When was the inspection standard last relaxed, and who approved it? → No answer = the relaxation was done in the dark.
4. How was the most recent question from a newcomer about the old practice handled? → "It has always been done this way" = criterion 3 hit.
5. Which release action can go through without writing down "why it is acceptable this time"? → If one exists = release leaves no record.

## The metric replaces the goal (Chapter 12)

1. How is this metric actually being optimized? Name three real moves. → Cannot name any = you have never been to where it happens.
2. How long are the metric's definitional footnotes, and who has the right to interpret them? → Footnote inflation = the definition is mutating.
3. What happened afterward to the last person who pointed out the metric's distortion? → Paid a price = criterion 3 hit.
4. Which unmeasured channel of observation still runs, and who reads it? → None = the organization has nothing left but the ruler.
5. Has anyone ever written the list of gaps between this metric and the goal it stands for? → Never written = the substitution is unmonitored.

## Narrative precedes evidence (Chapter 13)

1. Through how many independent interpretation routes did the current conclusion pass before being finalized? → One = there was no competing hypothesis.
2. On this team, whose job description includes "responsible for overturning"? → Nobody = refutation has no seat.
3. Was the hypothesis written in a form that could be overturned (what evidence, once found, means we drop it)? → Cannot be written = it is unfalsifiable.
4. To what standard must an objection carry its proof before it counts? → A higher bar than the proponents face = asymmetric burden of proof.
5. When did the early conclusion first enter a formal document? → Before the data was complete = the narrative was already sealed.

## Where expert intuition fails (Chapter 14)

1. Does the experience this judgment rests on still hold in the current environment (rules, technology, population)? → No required answer = running exposed.
2. How often do the rules of the environment change? → Fast change plus heavy reliance on experience = the failure zone.
3. How long is the feedback loop for this class of decision, and who can afford to wait? → Longer than half a year = no learning circuit.
4. In what setting did someone last answer data with "I have been doing this for twenty years"? → It has happened = criterion 1 hit.
5. Is the first move in a new domain an analogy or a measurement? → An analogy = intuition is crossing its boundary.

## Procedural drift (Chapter 15)

1. When was a line-by-line comparison of the manual against actual practice last made? → Never = the drift is invisible.
2. Are newcomers trained by the manual or by the old hand? → The latter = drift is passing down the generations.
3. Which rule can in fact nobody follow anymore? → No answer = nobody dares admit it.
4. What is the immediate consequence of violating this process? → None = a hothouse for drift.
5. Who approves the "informed violations," and in what name? → Verbal custom = ownerless violations.

## Information decays through hierarchy (Chapter 16)

1. Between the frontline's version and the decision layer's version, which items differ? → No answer = the decay is past the midpoint.
2. What is the channel that bypasses the hierarchy, and who is responsible for reading it? → No channel = only secondhand accounts are available.
3. In reporting materials, which way is the ratio of adjectives to numbers moving? → More adjectives = packaging under way.
4. How many layers does bad news cross between frontline and decision-maker, and what does each layer delete? → Cannot say what is deleted = every layer is deleting.
5. What became of the last person who reported over a superior's head? → Sanctioned = the channel is dead.

## Misaligned incentives (Chapter 17)

1. Have the appraisal schemes of every layer been read side by side? In which clause does the angle show? → Never read together = the misalignment is invisible.
2. This layer's decisions produce externalities: into whose books is the price entered? → Nobody's = free discharge.
3. Who is responsible for the overall result: a position of real power or a designated blame slot? → No real power = decoration.
4. Between decision-makers' tenure and the consequence cycle, which is longer? → The tenure is shorter = rational neglect.
5. How densely do the minutes read "as contracted / as required"? → High density = behavior is taking cover inside the contract.

## Diffusion of responsibility (Chapter 18)

1. In whose contract or job description does the halting authority sit, and in which clause? → No clause = halting depends on courage.
2. How many signatures are in the chain, and what exactly does each person sign? → Cannot say = the signatures are idling.
3. What is the organization's first question after an incident? → "Who signed off" instead of "what broke" = a dilution culture confirmed.
4. How many layers of outsourcing are there, and who holds inspection rights at each? → Cannot count the layers = a black box.
5. For a resolution passed by committee: who executes, who supervises, who closes it out? → All three in one = the resolution has no owner.

## Truth-tellers are culled first (Chapter 19)

1. What is the usage record of the internal whistleblower and dissent channels over the past three years? → Zero use = not an absence of problems, an absence of speakers.
2. Where is the person who last raised the sharp question? → Gone or marginalized = criterion 2 hit.
3. Who signs the performance evaluations, unilaterally? → The direct superior alone = the alarm hangs on one person's mood.
4. Which questions have become bound to which leader's reputation? → Cannot list any = the binding runs deep.
5. Of the organization's alarms (independent oversight, rotation audits, external assessment), how many still sound? → All muted = the accident is the only alarm left.

## The slack of success (Chapter 20)

1. Which investments have produced no visible value for a long time? Is there a list? → No list = they are being counted as redundancy.
2. Has "this has never caused an incident" been used as a reason to cut? → It has = criterion 2 hit.
3. After the last cut to a defensive investment, how long was it before the incident appeared? → Within two years = criterion 3 hit.
4. In the financial accounts, does "nothing happened" count as output or as non-output? → Non-output = certain to be cut within a budget cycle.
5. Who was the last person commended or rewarded for "nothing happened"? → Nobody = such work can only reward itself.

## Hidden coupling (Chapter 21)

1. When was the true dependency graph last drawn, by whom, and checked against what? → No graph = the coupling is invisible.
2. Which systems share things deemed "unimportant" (power, accounts, tables, domains, people)? → Cannot list three = the sharing has never been examined.
3. Where is the post-incident review of the last "unexplained" outage filed? → Not filed = the clues are evaporating.
4. Can "whom does this outage hit" be answered automatically? → It cannot = blast radius by guesswork.
5. In whose hands is the list of mergers, outsourcing, and legacy integrations? → Ownerless = the most deeply coupled territory.

## The illusion of redundancy (Chapter 22)

1. Is there a list of the ways the backup shares origins with the primary (same vendor, same drawings, same crew)? → No list = shared origins never faced.
2. When was a switchover last rehearsed during business peak? → Never = the drill is a performance.
3. Has the redundancy ever been verified on its own (by switching the primary off)? → Dare not switch = the redundancy is unproven.
4. Has anyone gamed out the scenario of both systems failing at once? → Never considered = common-cause failure running exposed.
5. Does the integrator's contract contain clauses on redundancy responsibility? → Not written = what you bought is redundancy on paper.

## Extrapolating beyond validated boundaries (Chapter 23)

1. On which page of the rollout plan is the section "what changed compared with the pilot"? → No such section = the extrapolation went undeclared.
2. Does the list of differences explain, item by item, why each difference does not affect the conclusion? → Brushed over in generalities = the differences were never digested.
3. Is "we validated this in A" being used as a reason to skip checks? → It is = criterion 3 hit.
4. Who listed the new environment's differences, and when? → Nobody = the differences will be discovered by accident.
5. Are the valid boundaries of the extrapolation written into the final conclusion? → Not written = the next extrapolation is already scheduled.

## Scale crossing thresholds (Chapter 24)

1. Where is the record of revalidating the core assumptions at the last crossing of an order of magnitude? → No record = the assumptions are running exposed.
2. Are coordination costs measured (number of meetings, management layers, interface documents)? → Unmeasured = the nonlinearity is invisible.
3. Which practices had already gone bad at twice the scale? → No answer = the rot cannot be known.
4. Why was the previous management layer added? → For communication = a threshold signal.
5. When veterans say "it was not like this before," is there a record? → No record = the organization is losing its baseline for comparison.

## Safety margin eaten away (Chapter 25)

1. Where is the ledger of design margins, and who maintains it? → No ledger = the cuts cannot accumulate.
2. Has anyone ever reviewed the full list of past cuts as a whole? → Only the current one = nobody holds the accumulation.
3. What is the quantitative basis for "still sufficient"? → No number = criterion 3 hit.
4. Who will halt the fifth cut? → Nobody = a straight-line slide.
5. Can the original design value of the margin still be found? → It cannot = the reference baseline is gone.

## Automation and skill decay (Chapter 26)

1. What is the mandated frequency of manual operation, and when was it last recorded? → No frequency = the skill is decaying on its own schedule.
2. What share of training covers takeover scenarios? → A low share plus high automation = the takeover will come at the hardest moment.
3. When did "the system handles it" become a reason not to practice? → Already a reason = criterion 3 hit.
4. The manual assumes the human knows certain moves: how is that assumption verified? → Not verified = the assumption is expiring.
5. Are the thresholds for leaving automatic mode written down and rehearsed? → No = the takeover is an improvisation.

## Sunk cost and escalation (Chapter 27)

1. In which section of the project charter are the exit conditions written, and who adjudicates them? → Not written = exit can come only by coup.
2. In which meeting did "we have already invested so much" last appear as the main argument? → Frequent appearances = escalation is running.
3. Who is the external adjudicator, and does that person hold any stake in the project? → None = judging one's own case.
4. Who last adjusted the re-forecast's assumptions toward optimism? → A one-sided adjustment = the model serves the conclusion.
5. What was the career trajectory of the last person who argued for exit? → Sidelined = exit carries a price.

## Maturity mismatch (Chapter 28)

1. Does the budget sheet have a column for "future costs"? → No column = distant costs never enter the books.
2. Have decision-makers' tenures and the consequence cycle ever been drawn on the same chart? → Never drawn = nobody looks the mismatch in the face.
3. Who signs for results that arrive across periods? → Nobody signs = a commons.
4. How do long-term liabilities become visible in the current statements? → They do not = the ledger is forgetting on someone's behalf.
5. Does a "bill list" for the incoming successor exist? → It does not = the handover doubles as blame-shifting.

## The invisibility of maintenance (Chapter 29)

1. Where is the three-year curve of the maintenance budget's share? → Falling every year with a constant equipment count = criterion hit.
2. Is the maintenance ledger auditable (what was done, when, against what standard)? → Not auditable = soft spending.
3. In maintenance accounting, does "nothing happened" count as output? → No = certain to lose the budget review.
4. Who signed the last decision to cut maintenance? → A signer unaware of the consequences = deferred payment.
5. When were the maintenance standards last updated against the vendor manuals? → A full version cycle behind = the standards are expiring.

## Handover gaps (Chapter 30)

1. Does documentation exist for why the key processes are done this way? → Only "how" = judgment is in the process of being lost.
2. Does the handover checklist have a column for "incidents that happened here"? → No column = the lessons leave with the person.
3. After a veteran leaves, what is the channel for asking "why"? → No channel = the gap becomes a fait accompli.
4. Can you list the places where documents record only conclusions? → Cannot list them = the blind spots cannot be known.
5. What answer did a newcomer last receive upon asking "why"? → "It has always been this way" = criterion 3 hit.

## Regulatory lag and capture (Chapter 31)

1. Of the regulator's sources of information, what share comes from the regulated? → Dominant = the structural condition for capture is in place.
2. How large is the gap between the last rule update and the technology change? → A full generation = lag has become the norm.
3. Has the ratio of penalty to the gains of violation ever been computed? → Below 1 = the fine is a membership fee.
4. What is the record of personnel movement between the regulator and the regulated? → Frequent in both directions = the revolving door is turning.
5. Whose hand drafted the first draft of the key clauses? → The regulated = drafting power has leaked out.

## Compliant yet unsafe (Chapter 32)

1. Who owns the seams between inspection items? → No owner = the seams are free.
2. After a compliance check, has anyone ever asked "do these compliant items add up to safety?" → Never = nobody is responsible for the whole.
3. Do the safety meetings compare violations or compare risks? → Only the former = a Safety-I closed loop.
4. Has there been a moment when proof of compliance substituted for a safety judgment? → There has = criterion 3 hit.
5. Is the list of exceptions and waivers growing or shrinking? → Growing = the rules are failing while the paper stays clean.

## Correlated failure (Chapter 33)

1. Does the risk register have a column for third-party dependencies? → No column = other people's risks are not risks.
2. Do you know who supplies your critical supplier? → Unknown = two layers deep, already a black box.
3. Have the isolation and degraded-mode plans ever been rehearsed? → No rehearsal = correlation means total loss.
4. Has anyone estimated the cost of exiting a single-point supplier? → Not estimated = exit capability is evaporating.
5. Have incidents at third parties ever entered your own reviews? → Never = the learning radius ends at the fence.

## Path lock-in (Chapter 34)

1. When was the exercise "if we started from zero today, what would we choose" last run? → Never = locked in without knowing it.
2. How much has the estimated migration cost risen against three years ago? → Rising, unchecked = the lock is deepening.
3. What is the most recent date on which alternatives appeared in a selection review? → Long ago = the evaluation has become a ritual.
4. Has anyone kept books on the gains of lock-in (compatibility, network effects, scale)? → Booking only the pain = the projection will be distorted.
5. Are the unlock trigger conditions written down? → No triggers = the lock has no keyhole.

## In diligence and from the outside

In an outsider's hands the library becomes a different instrument — investment diligence, audit entry, acquisition review, supplier vetting all work by asking the sets and counting the darks. Two differences from internal use.

First, the outsider owes no face-saving, so the counting stays clean. Keep the raw tallies: darks in the universal ten; darks in the hit sets; and whether the disposition phase could name names and dates on the spot. Three numbers sketch a profile of an organization's working knowledge of its own failure modes — harder to fake and more informative than any narrative section of a diligence report.

Second, the outsider adds three questions an insider never asks. One: when did you last run this list on yourselves, and where is the dark list from that run (an organization that has never self-audited will dark almost everything)? Two: of the darks from the last external review, how many were actually cured (the cure rate is the direct read on whether the organization learns)? Three: which questions are, as you put it internally, inconvenient (list them; the inconvenient questions are a map of the relationships)?

The output is a two-page sheet: dark distribution, cure commitments, and the date of the next review. Writing the review date on the output sheet is the final step that makes the usage real.

## Keeping the library alive

The library is not a finished document; three rules maintain it.

Rule one: additions come from post-mortems. After every review under Chapter 38, ask: was there a question which, asked at the decision point, could have changed the course? If yes, rewrite it as a library entry, annotated with its source case and date. This rule lets the question bank grow with the tuition actually paid.

Rule two: demotion and retirement. Questions that go green for three consecutive rounds (everyone answers, evidence attached) move to a spot-check list; green for six, out of the standing sets into the archive. A library kept sharp keeps meetings sharp; all-green questions left standing only dilute the pass.

Rule three: version and changelog. The library carries a version number, and every addition, edit, or removal logs one line: date, question number, action, source. The log exists so that "when did you last update your list" — the first of the three outsider questions — is itself answerable with dated evidence.

Custody sits with quality or safety, the same keeper as the deviation ledger (Chapter 11, Device 1) and the post-mortem archive (Chapter 38): three ledgers, one housekeeper, who reconciles them once a quarter. Cross-audited ledgers tell the truth.

## Three quick recipes

For the highest-frequency situations, a starting selection.

Recipe A, a go-live review: the universal ten, plus sets 21 (hidden coupling), 22 (illusion of redundancy), 26 (skill decay), and 30 (handover gaps) — twenty-five questions. Going live re-wires the coupling diagram wholesale, so the weight falls on dependencies and takeover.

Recipe B, an expansion or acquisition review: the universal ten, plus sets 16 (information decay), 18 (diffusion of responsibility), 24 (nonlinear scaling), and 33 (correlated failure). Expansion lengthens reporting chains, signature chains, and dependency surfaces; the four sets aim at exactly those.

Recipe C, a budget-cut review: the universal ten, plus sets 20 (the slack of success), 25 (margin erosion), 29 (invisible maintenance), and 28 (maturity mismatch). A cut is a bet that certain spending produces nothing; the four sets audit that bet line by line.

Recipes are starting points — the assessment table's hits override recipe habit. Revise the recipes every six months against the post-mortem record: any mechanism that has actually occurred in your organization enters the next recipe automatically.

## Three ways the pass fails

Failure one: the pass becomes a performance. Respondents get the questions early, prepare polished answers, and the meeting replays a briefing. Detection: swap respondents on two questions at random. Answers that survive a swap were real; answers that die were recited. Fix: respondents named at the session, never before.

Failure two: question fatigue. After a year, every question has a template answer, sessions run shorter, darks vanish, and the organization acquires a warm sense of rapid progress. Detection: reword one question (same meaning, new clothes) and watch whether the darks come back — recited greens cannot survive a rewording. Fix: rule two's demotion plus a rotation of phrasings.

Failure three: darks that never settle. Darks recorded, dispositions nodded through, nothing cured. Detection: sample last round's darks and check whether the promised evidence now exists, with dates. Fix: route dark dispositions directly into Chapter 36's conclusion-page actions, sharing its verifiers — let the library ride on machinery that already exists rather than building its own.

All three share one cure: make the list touch reality — swapped respondents, new wording, audited promises. Like every ledger in this book, an unread ledger decays into stationery.

## Three cadences for self-audit

Self-audit is one person and one list, at three depths.

Monthly, fifteen minutes: the universal ten only, answered aloud, unknowns noted by question number. The purpose is familiarity — a question unused atrophies like a muscle.

Quarterly, ninety minutes: the hit sets plus the universal ten, answered in writing with dates and sources, producing a dark list that feeds Chapter 36's action column or the team's dark pool — never a private drawer.

Annually, half a day: the four quarterly dark lists side by side, sorted into three trajectories — dark all four quarters (a structural blind spot; escalate to a design issue), dark-to-green (documented learning), green-to-dark (recent decay; handle first). The annual pass is the most informative act in the whole practice: one list tells you where the holes are; four tell you which way the organization is drifting. And the quiet by-product: one person's answers, kept for a year, become a private growth record — rereading your own year-old answers, most people meet their past optimism face to face, which is the exchange test of Chapter 6 performed on yourself.

## One question, three chairs

The same suspicion changes wording as it changes altitude; here is the universal set's question five (stop-work authority) in three versions. The rest adapt the same way.

Engineer: when I think something here is wrong, what is the shortest path to stopping it, and who will listen? (An answer shaped "tell my lead, who tells their lead" means the stop path is longer than the hazard's radius — Chapter 18's criterion in field form.)

Manager: for the person closest to the danger, how many hops does their stop signal take to reach me, and what decays at each hop? (This makes the manager count their own reporting chain — Chapters 16 and 18 converge in one question.)

Executive: when did someone below stop something on their own initiative, and what happened to them afterwards? (The recency and the career together are the complete evidence for whether stop authority is real.)

The structure is constant: the suspicion unchanged, the addressee and the answer's shape changing with the chair's power. One discipline governs the rewording: never soften the suspicion. A "who will listen" rewritten as "we should all cultivate awareness" is a question killed at the rewriting desk.

## The account, roughly kept

A rough ledger for the hesitating reader. Cost: one interrogation meeting with preparation and minutes, about two hours; quarterly self-audit, ninety minutes; card and library upkeep, an hour a quarter. A ten-person team spends roughly forty person-hours a year — one person-week. Return: set beside the direct losses in any A-grade case in this book — from a $975,000 penalty to eleven lives — and do your own conversion into your organization's units. The account stops there; further arithmetic turns glib. The library does not prevent everything; it prevents the class of failure called "nobody asked," and in the post-mortem record that class appears often enough to be worth the week.

The ledger has an unbookable side too: the pass changes how meetings speak. Adjectives retreat in front of demands for dated evidence, and the retreat spills into meetings where no list is present. Teams that run the pass report it consistently: after one season, the sentence "should be fine" buys noticeably less in that room.

## The closing question, reweighed

The closing question deserves a second reading, because it presses all one hundred and thirty questions into a single number: how many can you answer with dated evidence in three minutes? Organizationally the number measures the thickness of the knowledge stock; personally it measures what you carry out of the room. Every output of the pass ultimately converts into movements of that number, and quarter-over-quarter movement in it is more honest than any narrative of improvement. The instrument closes here: one hundred and thirty questions are the tackle, the closing question is the scale, and the catch is whatever the scale says it is. Weigh it quarterly; the procedure is in the cadences above. The first reading is usually ugly, and ugliness is the normal starting condition — the list's premise has always been that the dark is larger than you assumed.

## One set, case by case

To show what each question stands on, here is the normalization set with its cases attached — every question in the book could be annotated the same way.

Question one (how many times, adjudged harmless on what basis) stands on Challenger and Columbia together: the erosion adjudication history at Marshall, and the flight-by-flight foam table (CAIB p. 124). Both Exhibit A of "consequence-free history" posing as "risk-free proof," and the question makes the sleight visible by demanding the ledger.

Question two (is the margin a number or an adjective) stands on a linguistic phenomenon shared across the book's cases: the evaporation of "margin is sufficient" into "sufficient" into "fine." The question demands the third word be written back as a number with a source — no source, no margin (the review-room form of Chapter 11, Device 2).

Question three (who approved the relaxation) stands on av-034: the interval extension requested by the operator, approved by the regulator, information sourced entirely from the user side. The question interrogates the approval chain's information composition: requester plus requester's data equals nobody watching.

Question four (how was the newcomer's doubt handled) stands on the review-room scenes of mi-001 and the veteran-narrative pattern recurring across the cases: a newcomer's question is a free survey of blind spots, and the disposition — pursued or conventioned-away — is a direct measurement of the organization's cognitive openness.

Question five (which release can complete without a stated reason) stands on nu-002: the tag applied, the compensating measure never verified. The question forces the exemption list into the open — the list's existence is a gap map, and its absence means exemptions are being granted in the dark. Either way, there is work to do.

The usage generalizes: give every set this treatment. Attach one book case per question (Appendix B indexes by mechanism) and one live instance from your own organization. The book case proves the question worth asking; your instance proves it urgent — or proves, in its absence, that you are early. The two together are what installing a question actually means.

## Where the library sits in the toolchain

Upstream, Chapter 35: the assessment table decides which sets to draw — get that wrong and the pass interrogates the wrong things, so hit sets always outrank recipe habit. Downstream, two customers. The post-mortem (Chapter 38) consumes the dark lists as the negative image of the decision moment — what nobody then knew — and reconstructing "the then-unknown" from a dark list is one layer more honest than reconstructing it from memory. The pre-mortem (Chapter 39) is the pass's twin: the rehearsal reasons backward from an assumed death, the pass probes forward through working knowledge, and both survey the same cognitive darkness — which is why their outputs cross-check. If every hazard a rehearsal finds is excluded by some green answer on the pass, the rehearsal is theater; if the pass runs all green while the rehearsal keeps finding real hazards, the greens are wet. Lay the two side by side once a year, and the list acquires a second calibration source.

Remote and cross-team passes add three adaptations: cameras on (the dark verdict reads faces and hesitations; plain text translates "cannot answer" into "will revert by email," one grade softer); minutes projected live on a shared screen with the dark count growing in public (visibility is the discipline's life support — the meeting-room version of Chapter 36's sticky note); and across time zones, split the pass — questions in the overlapping hours, dispositions asynchronous with claims and timestamps in the document. Joint sessions across organizations add one rule: each side runs the universal ten privately before the joint pass; the contrast of the two dark profiles maps the risk at the interface better than any joint discussion — Chapter 33's territory, surveyed by questionnaire.

## One closing question

131. Of all the questions above, how many could you answer with dated evidence within three minutes? → Fewer than five means your organization's stock of knowledge about failure is smaller than its stock of memory about success. That is not your fault; it is the institution's (Chapter 4). But the window for changing it is in your hands (Chapters 38 and 39).

(First draft of this chapter: 5,110 characters.)
