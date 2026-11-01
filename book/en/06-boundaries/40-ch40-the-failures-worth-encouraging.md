# Chapter 40 The Failures Worth Encouraging

> What this chapter covers: three checkable criteria that separate exploratory failure from preventable failure, and the two symmetrical diseases that follow a badly drawn line, dressing preventable failure up as trial and error, or punishing exploratory failure as dereliction.
> When to turn back: when you are setting the accountability standard for failure; when you hear "we need to be tolerant of failure", or "zero tolerance".
> Estimated reading time: 30 minutes.

Every page of this book is about preventing failure. Not one of them says failure is forbidden. This chapter draws the boundary of what should be encouraged: which failures deserve encouragement, which deserve sanction, and where the line sits.

An encouraged failure has to pass three criteria. One: the cost stays inside a budget, and the exploration budget is money that gets spent until it runs out, not a hole with no bottom. Two: the knowledge produced can be coded, and what was learned can be written down rather than only felt. Three: the failure did not touch a point of no return (Chapter 7: once you have signed, gone live, announced, the action has stopped being exploration). All three hit, and the failure deserves encouragement. The form of that encouragement is a public postmortem, recognition for the team, and the lesson entered in the knowledge base.

A failure worth sanctioning also has three criteria. One: a known rule was broken (the rule exists, you knew it, you broke it, which makes the act a violation and not an exploration). Two: it was concealed after the fact (worse than the failure itself, by the logic of Chapter 19). Three: the same failure repeated (Chapter 11: when the same class of anomaly appears a second time and draws the same explanation again, the first step of the ladder is already in motion).

Between the three encouraging criteria and the three sanctioning ones lies a grey zone: cost over budget but knowledge of value, a point of no return touched but a new opportunity found by accident. Discretion over the grey zone belongs to the governance layer, and the decision goes into the case library, so the next grey-zone event has a precedent to consult. The grey zone exists because the line between encouragement and sanction is not a physical line. Organizations draw it in each instance, and each drawing leaves a trace. The traces are the organization's boundary history.

Before the criteria are used, three worked examples (pedagogical composites, not cases from the library) are worth filling in, because the sharpness of a criterion only shows against a filled form.

Case A. A team trials a new caching strategy in production without declaring it, saves budget, and on the third day a cache avalanche takes the service down for two hours. Criterion one, information increment: "cache stampede will avalanche" is already cited in the operations manual, so the information is pseudo-information, and the failure is preventable. Criterion two, cost constraint: no paper existed beforehand, undeclared, preventable. Criterion three, path declaration: no document, preventable. All three point at preventable, whatever the team lead calls it. Handling: ledger, postmortem, structural accountability.

Case B. A team declares a pilot on a new material, with a maximum loss of 500,000 written on the paper and three indicators named as stop-loss. Eight months later the indicators have not been met, the project closes, and the loss comes to 470,000. Information increment: the failure threshold of this material under this working condition is a new proposition, so this is exploration. Cost constraint: the actual loss sits inside the paper. Path declaration: the failure happened on the declared path. All three hit, exploratory. Handling: public postmortem, information into the library, recognition for the team.

Case C. A team declares a pilot with a paper ceiling of 300,000, then goes past the ceiling to 800,000 mid-course to catch a market window, and the direction later proves sound. Criterion one: the direction was sound, so the information is real. Criterion two: 1.6 times past the paper, a miss. Criterion three: over the limit while staying on the path, a miss. Two misses, so it is handled as preventable, but the postmortem records one separate line: the direction judgment was correct. Whether the direction was right and whether the process was lawful are two accounts, and an organization that adds them together learns neither the direction nor the discipline. The taste of the grey zone appears here, and 40.6 comes back to it.

What the three examples teach in common: every document used to check a criterion is a pre-event document, which is what stops the urge to reword the story afterwards. The declaration holds the same position in this system that preregistration holds in an experiment. It turns exploration from a retrospective figure of speech into a status held in advance.

## 40.1 One Boundary, Two Diseases

Failure is not one category. It is two.

A failed clinical trial, a closed product line, a technology route disproved: these are prices an organization pays to buy information. Shipping with a known defect, skipping verification, ignoring an alarm: these are the consequences of a known rule being broken. The information in the first kind did not exist before the failure. The information in the second kind was written into the rules before the failure happened. The two need opposite governance. Exploratory failure wants a budget, a declaration, and a reward for the information it produced. Preventable failure wants a ledger, a postmortem, and accountability traced back to structure. An organization that runs both through one standard will develop one of two diseases, and often both at once.

Disease one: preventable failure dressed up as exploration. A launch that skipped verification becomes "moving fast and testing cheaply". A gamble that ignored the alarm becomes "the courage to commit". An operation with no record becomes "agile". The dressing keeps preventable failure out of the ledger, so the same death recurs, and each recurrence arrives with the sentence "we learned a great deal".

Disease two: exploratory failure punished as dereliction. A team that tried and failed is held to account, nobody declares the next attempt, and exploration moves underground. Failure continues. It simply stops being recorded and stops being discussed. The organization's visible failure count falls while its information flow stops.

Both diseases point at the same boundary. The test is not the size of the failure, and not the attitude of the person who owned it. It is three objective conditions that anyone can check.

## 40.2 The Three Criteria

Criterion one: information increment. Did this failure produce a piece of information that did not exist before it?

The information from exploratory failure takes the form "this road does not go through": the drug does nothing at the target, the market will not pay this price, this architecture cannot hold this scale. The "information" from preventable failure is pseudo-information: weak mortar will hollow out, an alarm that has rung for two hours is an instruction to go and look, low tyre pressure will burst a tyre. Those rules existed before the failure, in a standard, a manual, or an industry lesson. The check: write the cause of the failure in one sentence and ask whether that sentence is a citation of some existing document. A citation means preventable. A new proposition means exploration.

Criterion two: cost constraint. Was the cost of the failure bounded in advance?

Exploratory failure is information bought under a capped bet. A phase-one trial of a few hundred subjects, one prototype, one pilot city: the cost appears in a budget and the ceiling can be calculated. The cost of preventable failure has no ceiling. Its size is set by luck, and a run of quiet years only means its turn has not come. The check: ask whether a piece of paper existed before the event stating the maximum loss. If it existed and the actual loss fell inside it, exploration. If there was no paper, or the loss ran far past it, preventable.

Criterion three: path declaration. When the failure happened, was it on a path declared beforehand?

Declaration is what turns an attempt into an organizational decision instead of a personal adventure. The plan, the boundary, the stop-loss point and the approver all sit in a document. A failure inside the declared path gets exploratory governance. A failure on a departure from that path, a skipped step, an exceeded limit, a private modification, gets preventable governance, however much the intention resembled innovation. The check: take out the pre-event declaration and see whether the failing action appears on it. If no document exists, the default is preventable, because nothing can show the attempt was controlled.

How the criteria are used: all three hit, exploratory. Any one miss, preventable. A grey zone, two hits and one weak, may be marked "pending classification", but it must be entered in the ledger. Being unclassified is allowed. Being unrecorded is not.

The point of the criteria is to prevent the after-the-fact explanation. The urge to relabel a preventable failure as exploration never goes away, and since every criterion points at a pre-event document, the relabelling has nothing to work with.

Now the exploratory trio, item by item.

Portfolio management. The path limit starts from an operational formula: the number of paths open at one time does not exceed what the organization can honestly postmortem at the same time. For most teams the real number is three to five. The limit is checked monthly. When the limit is full and someone wants a new path, the only legal move is to close an old one, and running over the limit is not permitted. What the limit prevents is not waste. It prevents the dilution of attention, because an organization splitting attention five ways, a fifth each, has five paths running naked.

Loss budget. Three tiers. A small note, where a single path's loss cannot exceed a tenth of the team's quarterly budget, is approved by the team. A medium note, between a tenth and a half, is countersigned one level up. A large note, above a half, is approved by the governance layer. The tiers make the cost of deciding proportional to the cost of being wrong: small notes open fast and close fast, large notes open slowly and close under scrutiny. The mandatory review triggered by an overrun has its own detail: additions freeze on the day the line is crossed, a review conclusion is due within 48 hours, and the review asks two questions only. Is the reason to continue new evidence or old hope (Chapter 13), and who is delaying the stop-loss.

Quick funeral. Once the speed of falsification becomes a metric, the reverse game starts: stop-loss lines set low so that paths can be closed quickly and look decisive. The declarant sets the stop-loss line, the budget approver reviews it, and the two rights are kept apart. One ritual is worth keeping at the funeral: the closed path gets a hundred-character epitaph (what was learned, under what conditions this road reopens) and the epitaph goes into the knowledge base. The epitaph is the final product of exploratory failure. A failure that can produce a hundred characters has completed the information purchase. A failure that cannot produce them has not even closed its books.

The preventable trio is already laid out elsewhere (ledger in Chapter 11, postmortem in Chapter 38, structural accountability in Chapter 9). One item is unique to this chapter: keep the two ledgers apart. Put exploratory entries and anomaly entries in one book and two years later nobody can say which failure was money spent on information and which was a fee paid for nothing. A shared book is the breeding ground for prettification, and grey-zone entries are the easiest of all to paint over as exploration once they sit in a mixed book. Separate books, separate colours, separate field definitions for the mechanism column. This is infrastructure-level separation, and it works on the same principle as the separation of the postmortem system from the personnel system in Chapter 38: where a cultural promise will not hold, a permission group will.

Criterion one needs one more layer, because pseudo-information has an in-house variant. A rule sits in an industry standard or a vendor manual, and this organization never internalized it. Nobody read it, or someone read it and it never entered a procedure. The cause of the failure is still "a citation of an existing document", so the failure is handled as preventable. That lenient reading attracts objections ("we genuinely did not know"), and there are two reasons to hold it. The criterion system exists to protect the structure of the pre-event paper, and accepting "a rule nobody read does not count" would reward ignorance, making illiteracy a passport into exploration. And information unknown to this organization was available at low cost, one search, so the claim of information increment does not stand. The humane side of the lenient reading sits in Chapter 9: structural accountability runs as usual (why did this rule never enter a procedure, which is a matter for the ledger and the postmortem), while the treatment of individuals goes through the fair-culture substitution test. Leniency and mercy are two different things. The criteria settle the account. The culture sets the penalty.

## 40.3 Governance of the Two Classes

The exploratory trio: portfolio management (a cap on the number of paths open at once, read as a portfolio rather than case by case), loss budget (each path states its maximum loss in advance, and a breach triggers mandatory review), quick funeral (the speed of falsification is the metric, one month to disprove beating a year to confirm, and delayed falsification is the largest cost in exploratory governance).

The preventable trio: ledger (every event entered, tagged with a mechanism chapter number), postmortem (the Chapter 38 template), structural accountability (ask about process and incentives, not only about people). The two systems share one infrastructure: records, ledger, independent review (Section 38.4). They differ in standard and consequence.

Here is the minimum design of a declaration system, so that criterion three can actually be applied. One page, five required fields.

Field one: hypothesis. One sentence stating what proposition this attempt tests ("this adhesive holds under working condition XXX"). An attempt whose proposition cannot be written does not enter the process. An action that cannot say what it tests has no information increment to offer and falls outside criterion one by construction.

Field two: boundary. In what scope, under what conditions, for how long. This field is the paper against which criterion three checks the failing action.

Field three: maximum loss. Money, person-hours, and the largest impact on existing business, in numbers. This sheet is the whole of criterion two.

Field four: stop-loss point. Which signal means stop. The signal must be observable (an indicator, a date, an event), and "stop when it feels wrong" is not a stop-loss point.

Field five: information outlet. Where the learning gets written and who uses it. This field moves the codability requirement of criterion one to the front: decide where the learning goes before the fact, and afterwards there will be more than a feeling.

Approval has a time discipline. Small note, 48 hours. Medium, one week. Large, two weeks. Past the deadline, the default is refusal, because an approval process that dies of delay is worth exactly as much as no process. Both decisions are written in two lines. An approval gives a reason that can be tested later, since the approver is also declaring a judgment. A refusal has to name a specific defect in one of the five fields ("the boundary is too wide", "the stop-loss is not observable"). Refusals of the "not for now" kind are not allowed, because a refusal with no information pushes the declarant back into an undeclared attempt.

A declared attempt enters the exploratory ledger, and a failure goes through the exploratory governance of 40.3. Changing the boundary or the stop-loss mid-course requires a change declaration: edit the paper, leave the trace. Verbal changes are prohibited, because a paper amended by mouth leaves criterion three with nothing to check afterwards.

Declaration rates do not rise on exhortation. They rise on three structural changes.

Change one: make the win rate visible. How many refused declarations came back on a different path and succeeded, and how many epitaphs from closed paths were later cited by other projects. Publish both numbers. Declarants have to see the system produce value before they keep paying the cost of a page.

Change two: make refusal cost something. An approver who rejects a declaration signs the ledger, and the annual statistics report each approver's refusal rate alongside the number of times work went around the process and then had an incident. Approval becomes a recorded judgment, and a careless refuser becomes visible too.

Change three: decouple the declaration window from the performance cycle. The flood of declarations before a review and the drought after it show that declaring has been filed as a performance act. Decouple by keeping the declaration ledger out of the appraisal numerator and denominator, the same rule the postmortem runs on, and let appraisal look only at the portfolio's final output.

The three changes share one logic. The enemy of the declaration rate was never laziness. It is a negative expected return on declaring. Fix visibility, liability and timing, and the return turns positive, and behaviour walks over on its own.

## 40.5bis Organizational Detectors

Both diseases have detectors at the organizational scale, and they find the condition earlier than case-by-case diagnosis does.

Disease one has three. Detector A: the ratio of exploratory entries to anomaly entries in the two ledgers. Where exploratory entries dominate to an implausible degree, with more than eight in ten failures described as exploration, the criteria are being used as rhetoric rather than as a check. Detector B: the frequency of "we learned a great deal" set against the completion rate of the mechanism field's chapter number. Said often, and no chapter number to show, is evidence of prettification. Detector C: the annual inventory of large undeclared losses. Every one it turns up is direct evidence of a case that slipped past the dressing.

Disease two has three as well. Detector A: the annual curve of declaration count. Flat or falling while business volume rises means declaring is dying. Detector B: tracking behaviour after a refusal. What share of refused teams came back on a different path, which is healthy, and what share simply went ahead, which is the disease presenting. Detector C: one question in internal recruitment interviews, "would you say in advance here that you were about to attempt something that might fail". The pause before the answer is the reading.

Both sets are read the same way. Ignore the culture as stated. Look at the shape of the ledger and the curve of behaviour. Both diseases are early on paper and late in personnel files.

Four interfaces with the rest of the book, so that this chapter's criteria do not contradict the twenty-odd chapters before it.

Interface one, with Chapter 20 (the slack of success). What slack consumes is defensive investment: inspection, maintenance, redundancy. This chapter's exploration budget is informational investment. Both kinds of money look useless while nothing goes wrong, and both get cut easily, but the reasons for cutting differ and the diseases they prevent are unrelated. Book them as separate lines. Protect defensive investment with the Chapter 20 questions and the exploration budget with this chapter's portfolio management. Book them together and whoever wants to cut will always find a line that looks useless.

Interface two, with Chapter 27 (sunk cost and escalation). Additional spending on an exploration and additional spending on an escalation are indistinguishable in the cash flow. The distinction is the pre-event paper. An addition inside the declared boundary, with the stop-loss point not yet triggered, is the normal rhythm of exploration. An addition after the stop-loss point has triggered is escalation, and the external adjudicator of Chapter 27 takes over. Criterion three's paper does its second job here: the first job settled the character of the failure, exploration or violation, and the second settles the rhythm, continue or stop.

Interface three, with Chapter 13 (narrative before evidence). The declaration is the antonym of a narrative: it forces the proposition to be fixed before the data arrives, and fixed in falsifiable form. The quality of a team's declarations can stand as a proxy for that team's immunity to Chapter 13. A declaration with a vague proposition is almost certain to slide into narrative reconstruction after it fails.

Interface four, with Chapter 36 (the reverse reminder from the thirty-minute procedure). Chapter 36 said that exploratory decisions are not served by the death rehearsal, because a rehearsal looks for preventable ways to die and an exploratory decision has no preventable death to find. That gives the two chapters a precise division of labour: operational decisions use the rehearsal to find death, exploratory decisions use the declaration to buy life. One instrument manages dying and one manages living, and an organization needs both. An organization with only one installed is either over-cautious or running naked.

The common thread through all four: these criteria are not a loose sheet. They close the loop of the book's mechanism system on the side that permits failure. The other half of that loop, preventable failure, occupies twenty-odd chapters. This chapter supplies the missing side, and only then is the system drawn complete.

The accounting detail behind criterion two deserves its own passage, because "how much do we write as the maximum loss" is the field most easily gamed in any declaration system. The motive to write it small is obvious: a lower paper ceiling is easier to approve and lighter to answer for once it is breached. Three countermeasures.

Countermeasure one: define maximum loss as inclusive of spillover. Direct spend plus the largest impact on existing business (downtime, recall, compensation), verified by the budget approver, not calculated by the declarant. Estimate the spillover with the cascading-failure approach of Chapter 33: if this path fails, who receives it along the dependencies.

Countermeasure two: decouple the paper ceiling from the penalty. A breach is handled under the ledger logic of Chapter 11 (entry, postmortem, structural accountability) rather than fined by the size of the overrun. Once the overrun amount is tied to the penalty, declarants learn a reverse skill and write the paper enormously high to stay under it, which destroys the budget. Accountability always attaches to "no paper" and "concealed", and the amount itself is only a number in the postmortem.

Countermeasure three: audit the loss definition after the fact. Each quarter, pull two closed paths and check whether the calculation of actual loss matches the definition used on the paper. A paper that counted spillover and a postmortem that counted only direct spend is a silent overrun. Definition audit guards against bookkeeping compliance, where the ceiling was never breached because the definition went on a diet first.

The principle under all three: criterion two protects the structure of the capped bet. How large the bet is remains a matter for both parties to agree, and any unilateral change after agreement, writing it smaller or counting it smaller, hollows the structure out.

## 40.10 Three Misreadings

Misreading one: encouraging failure means raising the failure rate. The objective function of the criteria was never the number of failures. It is the unit price of information: the same piece of information bought as cheaply as possible. Portfolio management and the quick funeral press the unit price down, and the failure rate falls behind it, because once pseudo-exploration leaves, the remaining failures are all money spent on information. An organization that reads this chapter as "fail more often" has installed the shell of the policy without the core of the criteria.

Misreading two: a tolerant organization needs no accountability. The other half of the criteria, the three preventable ones, is printed on the same sheet as the three encouraging ones. The more exploration you encourage, the harder the preventable standard has to be nailed down, or violators will spend the exploration allowance (Section 40.1 explains why the two diseases usually arrive together). The fair-culture spectrum in high-hazard industries, graded between pure no-blame and full accountability, is structurally the same as these criteria: the grade is set by intent and by the substitution test, whether another person would have done the same. This chapter moves the material for that judgment forward into a pre-event paper, so the judgment returns to a document instead of a memory.

Misreading three: a declaration system kills inspiration. The improvised attempt born of inspiration is in fact the declaration system's best customer. One page, five fields, and an inspiration that can fill them is worth pursuing, while an "inspiration" that cannot state a proposition is usually an impulse. The system does not filter out inspiration. It filters out impulses wearing inspiration's clothes. Real gold is occasionally among the filtered impulses, and that is the insurance premium of the system, an order of magnitude cheaper than the tail cost of undeclared attempts.

The common antidote to all three: go back to the criteria. The criteria do not reward failure and do not punish failure. They separate two accounts, money spent on information and fees paid for nothing. An organization that keeps the accounts apart can afford to spend from both.

## 40.9 A Compliance and Legal Addendum

In heavily regulated industries the declaration needs one more layer: a mapping against the rules. Three additions.

Addition one: put a "rule mapping" field ahead of field five. It lists the current rule clauses this attempt touches, and the expected compliance position (inside current rules, exemption required, not covered). Mapping turns legal from the last veto into the person who draws the boundary in advance. The regulatory lag of Chapter 31 meets the demand for exploration here: the ground the rules do not cover is the lawful space for exploration, and it is the reason regulatory sandboxes exist.

Addition two: file the exemption in step. Where an exemption is needed, the exemption application goes in with the exploration declaration, rather than being sorted out after a failure. An exemption obtained afterwards looks no different to a regulator than a violation (the compliance logic of Chapter 32), while filing both together moves the boundary dispute ahead of the loss.

Addition three: design the transparency strategy toward the regulator in advance, deciding what range and what wording will be disclosed, which precedents and epitaphs the regulator may see. Do not decide this during an inspection. Chapter 31 described how a single information source produces capture, and a regulated party voluntarily supplying structured exploration information is one of the few available levers for changing the composition of that source: when the regulator can see where your exploration boundary runs, a rule update has somewhere to land.

The floor under this section is one sentence. Every freedom this chapter grants rests on a pre-event paper, and in a regulated industry the paper carries one more layer than elsewhere. Freedom costs more there. The structure of the criteria applies unchanged.

## 40.8 The Morphology of Encouragement

For an exploratory failure that hits all three criteria, the word "encouragement" has to become something concrete. Three forms, each with its taboo.

Form one: the postmortem changes specification. An exploratory failure enters the Chapter 38 template with the mechanism field tagged "exploratory path disproved". The session does not hunt for structural defects. It extracts the proposition and the evidence: which later judgments this falsification changed. Taboo: letting preventable-accountability questions into an exploratory postmortem. Wrong book, wrong questions.

Form two: courtesy toward the information. The epitaph enters the knowledge base, the proposition enters the case library, and the falsification feeds the position table and the question library, so a failed path leaves the question library one question larger. What receives the courtesy is the information, not the feelings: a citation can omit the word "brave" and must include "the proposition is falsified, evidence number X". Taboo: turning the person who ran the exploratory failure into a tragic hero. Hero narrative loads the next attempt with a performance obligation, and people suppress stop-loss signals to live up to it. The calmer the wording of the courtesy, the more durable the system.

Form three: renewal of the budget. A failure does not shrink that team's exploration budget, because the budget is assessed on portfolio performance rather than on a single path. Taboo: letting renewal become automatic. For a team whose last three epitaphs produced no codable information, renewal comes with conditions, a change of proposition domain or a change of the person holding the proposition. The whole design target of the encouragement machinery is one thing: the next person dares to declare, and must declare by the rules. Calibrate the three forms to that target and encouragement will not deform.

Portfolio management has one internal structure still to explain: the relation between paths. Inside the limit, a hedged pair is allowed, two paths with opposite propositions open at once, each with an independent stop-loss. The value of a hedge is that its information output runs in both directions: whichever side is falsified, the opposite proposition strengthens. The hedge has one rule. The two paths may not share a data source for their stop-loss signals. A shared stop-loss is the common-cause failure of Chapter 22 replayed in an exploration setting: the data source goes down and both stop-losses go blind at once. Beyond the portfolio view, the paths also need a read on crowding out. Once a star path absorbs the attention, the stop-loss signals on the others get read late, because attention is a resource. Add one question to the monthly portfolio check: in the past month, how many times was each path's ledger opened. The spread in those counts is the reading on crowding out.

## 40.4 Counterexample: Three Marks of Prettification

Mark one: the story contains no criteria. When you hear "that trial was valuable", ask three questions. Where is the pre-event declaration, what maximum loss was written, and what was the information increment. Three blanks and the prettification is confirmed. A real explorer is boring before the fact (documents, limits, stop-loss points) and talks about value afterwards. The prettifier runs in reverse: nothing before, all meaning after.

Mark two: the cost only becomes known afterwards. The cost of exploratory failure is capped in advance. The cost of a prettified failure is startling afterwards. Whenever "trial and error" appears in the same breath as "far over budget", handle it as preventable.

Mark three: the same death appears a second time. Exploratory failure is the purchase of information, and one piece of information should not be bought twice. A pattern that recurs means the first round's information never reached the ledger, or that what happened was not information but dereliction.

There is a fourth mark, and it lives in the language. Prettified accounts are dense with unverifiable sentences: "the whole industry is like this", "the direction was right, execution was the problem". Whether the direction was right is exactly what the proposition and the stop-loss in the declaration were meant to answer. Whether execution was the problem is exactly what the ledger and the postmortem were meant to answer. Each sentence has a paper it belongs on. Saying them out loud while avoiding the paper is an admission that the paper holds nothing in your favour. When you hear either sentence, ask which version of the declaration carries the proposition. The absence of an answer is the fourth mark.

## 40.5 Counterexample Two: What Punishing Exploration Costs

An organization that punishes exploration loses more than a few attempts. It loses the declaration system. Once a person who ran an exploratory failure is publicly held to account, rational practitioners stop declaring, because declaring leaves evidence, and shift to undeclared attempts: success becomes performance and failure becomes an incident. The organization's real exposure is unchanged and its visibility falls to zero. This is the form that information attenuation up the hierarchy (Chapter 16) takes on innovation topics. The governance test follows: look at an organization's declaration rate rather than its failure rate. A low failure rate with a low declaration rate is usually not safety. It is silence.

## 40.6 The Grey Zone and the Precedent Library

The grey zone deserves full operational detail, because it is the ground both diseases fight over. The prettifier wants to read the grey zone as exploration. The fault-finder wants to read it as dereliction. The precedent library is the governing form for the grey zone.

Six columns per entry: a de-identified summary of the event; the result of the three criterion checks, which hit and which missed; the point in dispute, with each side's reading; the governance layer's ruling and its reasons; the after-the-fact verification, meaning a look two years later at whether this class of behaviour became more or less common after the ruling; and the precedent number. The fifth column is what distinguishes a precedent library from an ordinary case library. The consequence of a ruling is tracked, and the ruling itself is submitted for testing.

Three operating rules. Rule one: the ruling is made by the governance layer, but the right to open a case sits with the front line. Any team whose failure was judged preventable may apply for grey-zone review, and the review is free, does not overturn the original finding, and only adds a precedent. Rule two: precedents carry retrieval value and no force of law. When the next grey zone appears, precedents inform the discussion and the ruling is made fresh, because the criterion check has to rest on that event's own pre-event papers. Rule three: the library is reviewed once a year, in both directions. Check whether any precedent now rewards a disguised violation, which means the ruling was too loose, and whether any precedent punishes real exploration, which means the ruling was too strict.

A forecast of scale: a functioning organization produces roughly one to three grey-zone events a year. The library grows slowly, and each entry that appears is a developing agent for the organization's values. What counts as exploration here and what counts as dereliction is answered more honestly in a precedent than on a culture poster.

## 40.7 The Criteria at Every Level

The three criteria are not confined to the project level. They run upward and downward, changing shape a little at each level.

The individual career level. Personal exploratory failure, a change of field, learning a new skill, testing a side business, takes the same three criteria: a budget (living costs and time set aside), a declaration (candour with family or a partner), a stop-loss point. The individual version catches the same diseases. A preventable repeated mistake gets dressed as "I am experimenting" (the third fall into the same pit), or necessary exploration gets punished as "not serious work", where criterion three means declaring to yourself.

The industry level. The regulatory sandbox is a declaration system at industry scale: a limit (caps on users and on money), a declaration (the plan for entering the sandbox is published), a stop-loss (the exit clause). The sandbox shows the three criteria are executable at that scale too. Industry-level diseases have their analogues: dressing up consumers as free test subjects ("innovation always has someone paying for it"), and the fault-finding that bans every new business form ("no precedent means it is a violation"). Both refuse the dull device of declaring in advance, and both want the freedom to explain afterwards.

Cross-level consistency has one test question. Take a single matter and ask "where is the paper" at four levels: individual, team, organization, industry. If the answers thin out as you go up, the declaration system has failed at the top, and nobody up there dares ask for paper on exploration. This is the horizon mismatch of Chapter 28 projected onto exploration: the consequences of senior exploration already take longer to arrive, and without paper the bet has no boundary at all.

One recommendation on sequence, the same shape as the other usage chapters. Start with the one-page declaration template. Try it in a team that genuinely has an exploration need, where one path reaching closure inside a quarter makes a complete sample. Run the criteria three times for real, the way Cases A, B and C are run, and only then discuss the organization's policy standard. The wrong order looks like this: policy first, so the organization paints the slogan ("we are tolerant of failure"), the slogan lands with no criteria and no template to catch it, and six months later the slogan is fuel for disease one. Template first, criteria with it, policy last. This is the same rollout ladder as earlier chapters: cost rises from zero, resistance rises from zero, and you climb in order.

Closing. This is the only chapter in the book whose main business is saying what not to defend against. The twenty-four mechanisms and every device work to shrink an organization's exposure. This chapter opens one controlled hole in that exposure: paper sets its size, declaration sets its position, and the epitaph collects its output. An organization without the hole relieves the pressure somewhere else, since undeclared attempts are water seeping through a crack in the foundation. An organization with an uncontrolled hole takes preventable failure in through it. The whole job of the criteria is to make the hole a valve: three criteria open it, three criteria close it, and the grey zone goes to precedent. Put together, the book's position on failure is one line. For the unknown, buy. For the known, defend. Between buying and defending, the paper is explicit.

Those four words, the paper is explicit, are also the whole deliverable of this chapter: one template, two sets of criteria, an empty precedent register, and the blank cells waiting for your organization's first declaration. On the day the first cell is filled, the book's position on failure moves off the page and into your ledger, which is a more solid milestone than any reaction you might have to finishing a chapter. The criteria stop being three lines to be read and become a form in use. A form speaks for itself, and more accurately than this chapter does.

If your answers to the five questions cluster on the third one, no loss budget, then your organization's exploration is currently running with no paper at all, and the first sheet is the starting point. If they cluster on the second, no declaration channel, fix the channel before discussing tolerance, because an organization with no channel can only be tolerant of buried mines. Both are jobs you can start within a week: the template sits one section before 40.5bis, the channel hangs off the existing approval flow, and the budget starts at one percent of next quarter's project budget. A low starting point does no harm. The virtue of a criterion system is that it holds for small organizations too: a three-person team can still cap its exploration at three paths, declare on one page, and enter epitaphs in a register. The value of a system is in its structure, and structure does not discount for scale.

## Five Self-Checks

1. Take the last failure your organization publicly praised for "daring to try". Run the three criteria on it. How many does it pass?
2. Take the last failure your organization held someone to account for. Was there a declaration before it? Having no declaration channel is itself the finding.
3. Does your team have the concept of a loss budget? Of the attempts running now, how many have a sheet stating a maximum loss?
4. How long did it take the last attempt to be falsified? Is that period getting longer or shorter?
5. Which process does a failure declaration travel through in your organization? If the answer is "there is no process", who is running undeclared attempts right now?
