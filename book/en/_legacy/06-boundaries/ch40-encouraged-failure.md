# Chapter 40: The Failures That Should Be Encouraged

> What this chapter covers: the boundary criteria (three of them) between exploratory failure and preventable failure, and the two symmetric pathologies — dressing preventable failure up as "trial and error," and punishing exploratory failure as dereliction.
> When to return: when you are setting the accountability rules for failure; when you hear "we need a culture tolerant of failure" or "we must have zero tolerance."
> Reading time: 30 minutes.

## 1 One Boundary, Two Diseases

Failure is not one category but two. A new drug failing its clinical trials, a product line being shut down, a technical route being falsified — these are the price an organization pays to buy information. Releasing with a known defect, skipping verification, ignoring an alarm — these are the consequences of violating rules already known. The information of the first kind does not exist before the failure; the information of the second kind was already written into the system before the failure. The two kinds call for opposite governance: exploratory failure should be budgeted, declared, and rewarded for the information it produces; preventable failure should be ledgered, postmortemed, and traced to structure. An organization that handles both kinds with the same set of rules will contract one of the two diseases, and usually both.

Disease one: preventable failure dressed up as exploration. A launch that skipped verification is called "rapid iteration"; a gamble that ignored alarms is called "daring to commit"; operations with no records are called "agility." The dressing lets preventable failure escape the ledger, the same mode of death recurs, and every recurrence comes with the line "we learned a lot."

Disease two: exploratory failure punished as dereliction. The team that tried and failed is held to account, so next time nobody declares an attempt, and exploration goes underground: failures keep happening, only they are no longer recorded and no longer discussed. Failures appear to fall; what has actually happened is that the information flow was cut.

Both diseases point to the same boundary. The criterion lies neither in the size of the failure nor in subjective attitude, but in three objectively checkable conditions.

## 2 The Three Criteria

Criterion one: information gain. Did the failure produce a piece of information that did not exist before it?

The information of exploratory failure takes the form "this road is closed": the drug does not act on the target, the market will not accept this price, this architecture cannot carry this scale. The "information" of preventable failure is pseudo-information: insufficient mortar strength causes hollow walls, an alarm ringing for two hours deserves a look, underinflated tires blow out. Those rules existed before the failure, in standards, manuals, or industry lessons. How to check: write the cause of failure as one sentence and ask whether that sentence is a quotation from an existing document. A quotation means preventable; a new proposition means exploratory.

Criterion two: bounded cost. Was the cost of the failure fixed in advance?

Exploratory failure is the purchase of information under bounded stakes: a phase-one trial of a few hundred subjects, one prototype, a pilot in one city — the cost is written into a budget with a computable ceiling. The cost of preventable failure has no ceiling: its scale is set by luck, and the fact that nothing has happened once or twice only means their turn has not come yet. How to check: ask whether there is a piece of paper, written beforehand, stating the maximum loss. If there is one and the actual loss falls within it, exploratory; if there is none, or the loss runs far past the paper, preventable.

Criterion three: declared route. When the failure happened, was the organization on a route declared in advance?

Declaration turns an attempt into an organizational decision rather than a personal gamble: the plan, the boundaries, the stop-loss points, and who approves all land in a document. A failure inside the declared route goes through exploratory governance; a deviation outside it — skipped steps, exceeded limits, unauthorized changes — goes through preventable governance, however much the original intent resembles innovation. How to check: produce the declaration document and look for the failing action on it. If the document does not exist, treat it as preventable by default, because there is no way to prove it was a controlled attempt.

Rule of use: all three hit means exploratory; any one missed means preventable. A gray zone (two clear, one weak) may be labeled "pending classification," but it must be registered in the ledger — going unregistered is not allowed. The point of the criteria is to block post hoc reinterpretation: the urge to retell a preventable failure as exploration is permanent, but every criterion points at documents created before the fact, and those cannot be rewritten afterward.

## 3 Governing the Two Kinds of Failure

The three-piece kit for exploratory failure: portfolio management (a quota on the number of concurrently attempted routes, judged as a whole like an investment portfolio rather than case by case), loss budgets (each route states its maximum loss in advance; crossing the line triggers a mandatory review), and fast funerals (speed of falsification is the metric — a falsification in one month beats a confirmation in a year, and delayed falsification is the largest cost of exploratory governance).

The three-piece kit for preventable failure: the ledger (every case entered, with the mechanism chapter attached), the postmortem (the Chapter 38 template), and structural accountability (question the process and the incentives, not only the people). The two kits share one infrastructure: record-keeping, the ledger, independent verification (Chapter 38, Section 4). Only the classification rules and the consequences differ.

The criteria at work: three miniature cases, judged in full.

Case A: a team tries a new caching strategy in production without declaring it; it saves budget, and on day three a cache avalanche takes the service down for two hours. Criterion one, information: "cache stampedes happen" is quoted in the operations manual — pseudo-information, preventable. Criterion two, cost: no paper exists (nothing was declared) — preventable. Criterion three, path: no document — preventable. All three read preventable, whatever the owner calls it. Disposition: ledger, review, structural accountability.

Case B: a team declares a materials pilot (maximum loss stated: 500,000; three stop-loss signals written), runs eight months, misses the metrics, closes the project at a cost of 470,000. Information: the material's failure threshold under this duty cycle is a new proposition — exploratory. Cost: inside the declared envelope. Path: on the declared path. All three hit: exploratory. Disposition: open review, information to the library, the team commended.

Case C: a declared pilot (paper cap 300,000) overshoots to 800,000 chasing a window, and the direction turns out right. Criterion one: the information is real. Criterion two: 1.6 times over paper — fails. Criterion three: on-path but over-limit — fails. Two fails: preventable track — with one separate entry recording that the direction was right. Direction and process are two accounts; organizations that merge them learn neither directions nor process.

The common lesson: every check reads pre-existing paper. The criteria cannot be gamed afterwards, because a declaration is to exploration what preregistration is to an experiment — it converts "exploration" from an after-the-fact adjective into a before-the-fact status.

## 2bis The filing system: the five fields

Criterion three needs paper to live on. The declaration is one page, five mandatory fields.

One, the hypothesis: what proposition is this attempt testing, in one sentence ("the adhesive withstands X under duty Y"). A attempt that cannot state its hypothesis may not enter the flow — an action that cannot say what it is testing has no information increment to promise, and fails criterion one on its face. Two, the boundary: scope, conditions, duration. This is the paper criterion three reads against. Three, the maximum loss: money, person-hours, and worst spillover to live operations, as numbers. This page is the whole of criterion two. Four, the stop-loss: which observable signal stops the attempt — an indicator, a date, an event. "We'll pull the plug when it feels wrong" is not a stop-loss. Five, the information exit: where the learning goes, and for whom. This field moves criterion one's codifiability requirement upstream — decide before starting where the learning lands, and afterwards it will not be left as vibes.

Approval clocks: small stakes (a single path under one tenth of the team's quarterly budget) team-approved within 48 hours; middle stakes (a tenth to a half) one countersignature within a week; large stakes (over half) governance within two weeks. Silence past the clock counts as refusal — an approval process that kills declarations by drag equals no process. Both approvals and refusals carry two written lines: an approval is itself a judgment on record (the approver is also declaring), and a refusal must point at a specific field defect ("boundary too wide," "stop-loss unobservable") — "not now" is an information-free refusal, and information-free refusals push declarers back underground. Approved attempts enter the exploration ledger; boundary or stop-loss changes mid-run go through a change declaration — the paper changes on paper, never by mouth, or criterion three becomes unauditable after the fact.

## 3bis Governing the two kinds: the details

The exploration toolkit, expanded.

Portfolio management: a workable opening cap is the number of paths the organization can honestly post-mortem at once — for most teams, three to five. Check monthly; a full portfolio means the only legal way to open a new path is to close an old one. The cap does not prevent waste; it prevents attention dilution — five paths at a fifth of everyone's attention each are five unguarded ones.

Loss budgets in three tiers, approval cost scaling with stakes: small stakes move fast and die fast; large stakes move slowly under scrutiny. And the mandatory review on crossing the line executes within forty-eight hours of the breach, with the day's overrun frozen, on two questions only: is the case for continuing new evidence or old hope (Chapter 13), and who exactly is delaying the stop, at what price?

The fast funeral keeps one ceremony: a hundred-word epitaph for every closed path — what was learned, under what conditions the route might revive — filed to the knowledge base. The epitaph is the exploration's final deliverable: a failure that can write its epitaph finished its information purchase; one that cannot has not even closed the bill.

The preventable toolkit's expansions live in their own chapters (ledger, 11; review, 38; structural accountability, 9). One addition belongs here: keep the two ledgers separate. Merged, within two years nobody can say which failures were bought information and which were squandered tuition — and mixed ledgers are where makeovers graze, because a gray-zone entry in a mixed ledger is one retrospective edit away from "exploration." Separate ledgers, separate colors, separate mechanism-field conventions: infrastructure-level isolation, the same logic as Chapter 38's split between the review system and the personnel system. Where culture promises fail, permission groups do not.

## 4 Counterfeits: Three Marks of the Makeover

Mark one: the narrative contains no criteria. When you hear "this trial and error was very valuable," ask three questions: where is the advance declaration, what was the stated maximum loss, what is the information gain? If none of the three can be answered, the makeover is confirmed. Real explorers are boring before the fact — documents, quotas, stop-loss points — and talk about value afterward. The counterfeit is the reverse: nothing before the fact, meaning everywhere after.

Mark two: the cost is known only afterward. The cost of exploratory failure is capped in advance; the cost of a made-over failure is astonishing afterward. Wherever "trial and error" and "far over budget" appear together, treat it as preventable.

Mark three: the same mode of death appearing a second time. Exploratory failure is a purchase of information, and the same piece of information should not be paid for twice. A repeated pattern means the first failure's information never entered the ledger — or that it was never information at all, but dereliction.

## 5 The Mirror Image: What Punishing Exploration Costs

What an organization loses when it punishes exploration is not a few attempts but its declaration system. Once an explorer who failed is publicly held to account, rational practitioners stop declaring in advance (a declaration is evidence) and shift to covert attempts: success counts as performance, failure counts as an accident. The organization's true risk exposure is unchanged while its visibility drops to zero — this is Chapter 16, information attenuation in the hierarchy, in its form on innovation topics. The governance criterion: look at an organization's declaration rate, not its failure rate. A low failure rate paired with a low declaration rate is usually not safety; it is silence.

## 4bis A fourth mark, in language

The makeover also has a verbal tell, layered on top of the three structural ones: the narration runs on unverifiable sentences — "the whole industry does it this way," "the direction was right, only the execution slipped." Direction was what the declaration's hypothesis field was for; execution is what the ledger and review are for. Each claim has a home document; when both are argued in the air, away from their paper, the speaker has conceded that no paper supports them. Ask "which version of the declaration says that," and the missing answer is the fourth mark.

## 5bis Three detectors per disease

At organizational scale, each disease has early detectors — paper symptoms, arriving years before personnel ones.

The makeover's three. Detector A: the ratio of exploration-ledger to incident-ledger entries; a book that is eighty percent self-declared exploration is using the criteria as rhetoric. Detector B: the frequency of "we learned so much" against the completion rate of mechanism-field entries; much learning, few chapter numbers, makeover proven. Detector C: the annual audit of large undeclared losses — every line found is a makeover escapee with a receipt.

The purge's three. Detector A: the declaration count's yearly curve, flat or falling while volume grows — declarations are dying. Detector B: what refused teams do next — re-route and re-declare (healthy), or simply proceed (disease). Detector C: one question in internal exit interviews: "here, would you tell someone before trying something?" — the hesitation itself is the reading.

Read both detector sets the same way: not at the proclaimed culture, but at the shape of the ledgers and the curves of behavior. Disease starts on paper; only late does it reach personnel.

## 5ter Raising the declaration rate

Raising declarations is structural, not motivational — three changes.

Make the win rate visible: of refused declarations, how many returned with a re-routed resubmission and succeeded; of closed paths, how many epitaphs were later cited by live projects. Published numbers let declarers see the institution producing value, which is what pays for the page of paperwork. Make refusal cost something: refusals log the refuser's name, and the yearly tally shows each approver's refusal rate alongside the count of refusals later bypassed into incidents — refusal is a recorded judgment, and random refusals become visible too. Decouple the declaration calendar from the appraisal calendar: declaration surges before review deadlines and droughts after mark the declaration as a performance; the ledger stays out of appraisal (the same rule as review governance), and appraisal reads only portfolio-level outcomes.

The shared logic: the enemy of declaration is not laziness but negative expected value. Fix visibility, responsibility, and the calendar, and the expected value turns positive on its own.

## 6 The gray zone and its precedent book

The gray zone is the disputed territory both diseases contest — the makeover wants it read as exploration, the purge wants it read as dereliction. The precedent book is its government.

Six columns per entry: the event, de-identified; the three criteria's readings (which held, which failed); the point in dispute (both readings, stated fairly); governance's ruling with reasons; the two-year follow-up (did this ruling make such behavior more or less common — the ruling itself is on trial); and the precedent number. The fifth column is what makes this a precedent book rather than a casebook: rulings with tracked consequences.

Three rules run it. Rulings are made by governance, but the docket belongs to the front line: any team judged "preventable" may petition for gray-zone review, free of charge, which adds a precedent without touching the original ruling. Precedents inform, they do not bind: the next gray zone re-runs the criteria against its own pre-existing paper, using the precedent as guide, never as statute. And the book sits for annual audit in both directions — precedents that reward disguised violation (too lenient), precedents that punished real exploration (too harsh).

Scale expectation: a healthy organization sees one to three gray zones a year. The book grows slowly, and every page is a development of the organization's actual values — what this organization counts as exploration, what as dereliction, answered in rulings rather than on the culture wall.

## 7 The criteria at every altitude

The three criteria run at all levels, with local dialects.

The individual career: a personal exploration (a switch of specialization, a skill bet, a side venture) runs the same checks — a budget (living costs and hours reserved), a declaration (to family or partners, honestly), a stop-loss. The personal diseases are isomorphic too: the third recurrence of the same mistake dressed as "I'm experimenting," and the necessary experiment punished as "not a real job" — where the personal declaration is the promise made to oneself, in writing.

The industry: the regulatory sandbox is filing-system governance at industry scale — caps (users and amounts), declarations (sandbox entry is public), stop-losses (exit clauses). And the industry-scale diseases translate directly: treating consumers as free test subjects ("innovation needs someone to pay for it"), and treating every novel format as contraband ("no precedent means prohibited") — both, at bottom, refusals of the tedious paperwork of prior declaration, in favor of the freedom to explain afterwards.

One test question spans the levels: ask, at the personal, team, organizational, and industry altitudes, "where is the pre-existing paper?" If the paper thins as altitude rises — declarations everywhere at the bottom, none at the top — the filing system has failed at altitude. Senior exploration without paper is an unbounded bet with better rhetoric, which is Chapter 28's mismatch projected onto the innovation ledger: long consequence cycles plus no paper equals an open tab.

## 8 What "encouragement" actually means

For a failure that passes all three criteria, encouragement must be made of something; three forms, each with its forbidden twin.

Form one: a better review. Exploratory failures enter the Chapter 38 template with the mechanism field reading "route falsified," and the review extracts propositions and evidence, not structural blame. Forbidden twin: running preventable-track accountability questions in an exploration review — the wrong ledger's questions poison the right one.

Form two: honored information. The epitaph enters the knowledge base; the proposition enters the case library; the falsification feeds the assessment table and the question bank. Honor the information, not the emotion: the citation may contain no "bravery" and must contain "proposition falsified, evidence No. X." Forbidden twin: casting the failed team as tragic heroes — hero narratives load the next attempt with performance pressure (stop-loss signals get swallowed to stay worthy of the story), and the calmer the tribute, the longer the institution lives.

Form three: a renewed budget. Failure does not shrink the team's exploration budget (portfolios are judged as portfolios, not per path). Forbidden twin: automatic renewal — a team whose last three epitaphs contain no codifiable information renews only with conditions: a new proposition territory or a new proposer.

All three forms aim at one target: the next person declares, and declares properly. Anything that serves that target is encouragement; everything else is ceremony.

## 9 The interfaces with the mechanism chapters

Four connections keep this chapter from quarreling with the twenty-four.

With Chapter 20 (the slack of success): slack eats defensive spending — detection, maintenance, redundancy; this chapter budgets informational spending. Both look useless while nothing goes wrong and both get cut at budget season, but they are different ledgers: defensive spending is guarded by Chapter 20's questions, exploration budget by this chapter's portfolio management. One merged line item guarantees that whoever wants a cut always finds a "no visible output" tab to pull.

With Chapter 27 (escalation): an exploratory follow-on and an escalation follow-on are indistinguishable in the cash flows and separable on one fact — the paper. Follow-on spend inside the declared boundary with the stop-loss untriggered is exploration's normal rhythm. Spend continued after the stop-loss has fired is Chapter 27's case, and its external adjudicator wakes up. Criterion three's paper works twice: first to classify (exploration or violation), then to govern the pace (continue or stop).

With Chapter 13 (narrative before evidence): the declaration is that chapter's antidote in document form — the proposition stated, in falsifiable form, before the data arrives. A team's declaration quality is a serviceable proxy for its Chapter 13 immunity: vague hypotheses in, narrative reconstruction out.

With Chapter 36 (the reverse warning): exploration decisions do not run the death rehearsal, because the rehearsal hunts preventable deaths and an exploration has none to hunt — the two chapters divide the field precisely. Operating decisions rehearse their deaths; exploration decisions file their declarations. One tool governs death, one buys life, and an organization that installs only one is either timid or naked.

The common thread: this chapter's criteria are not a free-standing poster. They are the "permitted" side of the same system whose twenty-four chapters describe the "prevented" side, and the system only closes when both sides print on the same paper.

## 10 The regulated variant

In heavily regulated industries, declarations meet the rulebook, and three additions apply.

A rules-survey field joins the five: which clauses this attempt touches, and the expected compliance posture (within current rules; needs a waiver; rules silent). The survey turns legal from the last-minute veto into the advance cartographer — and where Chapter 31's lag meets this chapter's needs, the silent zones of the rulebook are precisely exploration's lawful open space, the reason sandboxes exist.

Waivers file simultaneously: any attempt needing one submits the waiver request with the declaration, never after the fact. A retroactive waiver reads, to a regulator, exactly like a violation (Chapter 32's logic); a simultaneous one moves the boundary dispute to before the loss.

The exploration ledger gets a disclosure policy designed in advance: which epitaphs and precedents can be shown to the regulator, decided calmly before any inspection rather than improvised during one. Chapter 31 argued that single-source information breeds capture; structured, voluntary supply of exploration data is one of the few levers a regulated party holds over that composition — a regulator who can see your declared boundaries has something to update the rules against.

The one-line floor under all three: every freedom this chapter grants hangs on pre-existing paper, and the regulated industries' paper is one layer thicker. The cost of freedom rises; the structure of the criteria does not change.

## 11 Three misunderstandings

Misunderstanding one: encouraging failure means raising the failure rate. The criteria's objective function was never the number of failures; it is the unit price of information — the same lesson bought cheaper. Portfolio caps and fast funerals push the price down, and the failure rate falls as a by-product, because the pseudo-explorations have left the pool. An organization that reads this chapter as "fail more" has installed the poster and left out the machinery.

Misunderstanding two: a forgiving organization skips accountability. The three preventable criteria are printed on the same page as the three exploratory ones: the more you encourage exploration, the tighter the preventable口径 must be drawn, or the violators will consume the explorers' budget (the mechanism of Section 1's two diseases co-occurring). High-reliability industries' just-culture ladders — from pure no-blame to full accountability, graded by intent and by substitutability (would a competent peer have done the same?) — share this chapter's skeleton; the difference is that the grading materials here are front-loaded into pre-existing paper, moving the judgment from recollection to file.

Misunderstanding three: declarations kill inspiration. Sudden ideas are the filing system's best customers: five fields, one page — an inspiration that can state its own hypothesis is worth chasing, and one that cannot is mostly impulse wearing inspiration's jacket. The system does not filter out inspiration; it filters out the label. Some genuine gold gets filtered with the impulse — that is the insurance premium, and it is cheaper by an order of magnitude than the tail of covert attempts.

The common cure is the criteria themselves: they neither reward failure nor punish it; they sort two kinds of bills — the information purchase and the wasted tuition. An organization that keeps the two books separate can afford both.

## 12 The exit ramp, marked

One last part of the map, easily missed: the portfolio's internal structure. Within the cap, hedged portfolios are allowed — two opposite propositions running at once, each with its own independent stop-loss — and their yield is bidirectional: whichever side falsifies, the other's proposition strengthens. One discipline: the two legs' stop-loss signals may not share a data source (a shared source is Chapter 22's common cause, in exploration costume — one bad sensor blinds both stop-losses at once). And the portfolio needs a crowding check: a star path that soaks up all the attention delays every other path's stop-loss signals being read (attention is a resource), so the monthly review asks one question — how many times was each path's ledger opened this month? A lopsided answer is the crowding reading.

This chapter's exit, like every exit in the book, is a piece of paper: a template, two sets of criteria, and an empty precedent book. The first declaration your organization files is the moment the position stops being an argument and becomes a ledger — and the ledger, as always, will be more persuasive than the chapter.

## Self-Check: Five Questions

1. Take your organization's most recent failure publicly praised as bold trial and error and run it through the three criteria. How many does it pass?
2. For your organization's most recent failure that led to accountability, was there a declaration document from beforehand? Having no declaration channel at all is itself the problem.
3. Does your team have the concept of a loss budget? Of the attempts currently running, how many sheets of paper state the maximum loss?
4. How long did the last attempt take to falsify? Is that cycle getting longer or shorter?
5. Through which process does your organization's failure declaration run? If the answer is "no process," who is attempting things covertly right now?

(Draft: about 5,900 Chinese characters; English edition: about 1,400 words)
