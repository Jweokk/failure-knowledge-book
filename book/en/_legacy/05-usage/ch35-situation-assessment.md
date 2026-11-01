# Chapter 35: The Situation Assessment Table

> What this chapter covers: a six-parameter self-assessment that, once filled in, points to the two or three failure mechanisms you are most likely running at this moment. This is the entrance that turns the book's twenty-four mechanism chapters into a personal tool.
> When to turn back to it: before taking over a new project, reviewing a new system, an organizational expansion, or a change of appraisal scheme; and as the first step of Chapter 36's thirty-minute walkthrough.
> Estimated reading time: 35 minutes (including the time to fill in the table).

## 35.1 Why six parameters

Nobody can check all twenty-four mechanism chapters every time. The assessment table compresses your situation into six parameters, three levels each, and the combination points directly to a small set of mechanism chapters. Compression buys speed at the price of misses, so the table promises only two things: it puts the most likely mechanisms at the front of the queue, and it eliminates the clearly inapplicable ones. It does not promise exhaustive coverage.

The selection standard for the six parameters: each must be assessable by you alone, within half an hour, without an external audit. For any parameter you cannot answer with confidence, fill in the most dangerous level. The table exists to find risk; an optimistic form only deceives the person filling it.

How the six were chosen is worth one paragraph, because it explains what the table can and cannot be trusted with. The candidates once numbered nineteen: alongside the current six sat team culture, leadership style, industry cycle, technology maturity, attrition rate, outsourcing share, and a dozen more. Three rounds of screening cut them. Round one applied three standards: assessable solo (attrition and outsourcing fell — the accurate numbers live in HR and procurement, so a solo filler can only guess); stably mappable to at least three mechanism chapters (industry cycle fell — the same cycle position exposes different organizations to entirely different mechanisms); and level boundaries sharp enough to be decidable (culture and leadership style fell — continuous spectra with a personal definition for every judge, so level assignment decays into a personality test). Round two back-tested the survivors against the book's own fully documented cases: parameters whose combinations failed to point at the mechanisms that actually occurred were cut again. Six remained. The survivorship also states the table's nature: these six are everything that survived "assessable solo, stably mappable, decidable in three levels" simultaneously. Factors outside the intersection still operate on your organization; they simply are not this table's business.

A related question deserves a direct answer: why not twenty parameters and be done with it. Because filling cost grows three times faster than information. Triple the parameters, triple the filling time, and the correlations among parameters mean the new information is far sublinear. The six-parameter design targets a fifteen-minute screen that produces an executable reading list; that target caps the table's width. Finer grain exists further down the toolchain: coarse screening here, criteria-level inspection inside the hit chapters there — granularity refines along the chain.

## 35.2 The six parameters and their three levels

Parameter 1: Coupling. In your system, how fast and how far does one component's failure spread?

- Low: failure can be isolated physically or by process; the blast radius is countable (one line, one customer).
- Medium: failure spreads within one department or one business chain; isolation requires a manual act (stopping a queue, failing over a data center).
- High: failure crosses systems or departments or spreads directly outward, and no list of the spread paths exists (Chapter 21's test: nobody can answer "whom does this outage hit?").

Parameter 2: Redundancy authenticity. How well would your backups survive a real switchover?

- High: the redundancy is heterogeneous (different vendors, different principles, different people), and switchover has been rehearsed under real pressure, successfully.
- Medium: redundancy exists but shares origins with the primary (same vendor, same drawings, same crew), or switchover has been rehearsed only in planned drills.
- Low: redundancy exists only on paper and has never been verified; or the critical link is a single point to begin with.

Parameter 3: Incentive alignment. The angle between the appraisal and reward system and the risk exposure.

- Aligned: those who create risk bear its consequences, and the consequences count in their appraisal.
- Partially misaligned: tension exists between local metrics and overall risk, but counterweights are present (risk control and safety supervision hold real power).
- Systemically misaligned: locally rational choices at every layer sum into collective loss, and the person who finds the problem is the person who profits from it (Chapter 17's criterion).

Parameter 4: Time pressure. The window between the decision and the appearance of its consequences.

- Short: the window is measured in days, and the direct gain from skipping verification is immediately visible (a release deadline, a delivery date, a shift).
- Medium: the window is measured in quarters; compressing the process pays within the current period and costs within the year.
- Long: the window is measured in years, and a decision-maker's tenure will most likely not cover the consequence cycle (the soil of Chapter 28).

Parameter 5: Scale. The number of collaborators, nodes, and dependency-chain length.

- Single team: one meeting with one team can settle every question.
- Multiple teams: cross-team interface documents are needed just to say who depends on whom.
- Network: outsourcing, franchisees, multi-party suppliers, platform ecosystems — a layer of dependency beyond the organization's own boundary (the territory of Chapters 24 and 33).

Parameter 6: Regulatory density. The frequency, depth, and penalty weight of external inspection.

- None or sparse: outsiders hardly look at your failures; the market and your own conscience are the main constraints.
- Dense: high-frequency inspection, item-by-item checks, substantive penalties.
- Dense but captured: inspection is frequent, but rules update more slowly than the business, information sources are singular, and penalties sit below the gains of violation (Chapter 31's criterion).

Note the trap in the regulatory-density levels: a high level does not mean safe. Environments with dense inspection are exactly where "compliant yet unsafe" (Chapter 32) flourishes, because the felt proof that every checked item passed substitutes for the inquiry into overall safety. Be honest about your industry's regulatory climate; the density on paper does not count.

## 35.2bis Evidence checklists: the level follows the proof

For each parameter there is a checklist; consult it before choosing a level, and let the level follow the evidence.

Coupling: the impact list from the last cross-system failure (was the radius actually countable?); the age of the dependency documentation; and an oral test — ask three senior people at random "if this component dies, who is affected," and see whether the answers agree. An organization whose seniors cannot answer raises its coupling self-assessment by one level, automatically.

Redundancy authenticity: the record of the last real switchover (date and result); the vendor overlap between backup and primary; the difference list between drill scripts and production. No real switchover in three years caps redundancy at medium, regardless of the diagrams.

Incentive alignment: where risk items sit in the live appraisal scheme, and at what weight; the most recent instance of anyone paying an appraisal price for stopping something; the track record of risk or safety functions actually vetoing a line decision. If no veto instance can be found, treat systemic misalignment as the working assumption.

Time pressure: this quarter's delivery commitments; the last three decisions to compress verification or review, and their stated reasons; an estimate of the consequence cycle — how long between fault and discovery. Write the two cycles side by side and the window length reads itself.

Scale: the count and freshness of interface documents; the supplier and outsourcing list; how many teams one change must notify. A change-notification list beyond ten names is a network in disguise — assess it at network level.

Regulatory density: the number and depth of external inspections in the past year (item-by-item checks, or briefings?); penalty size against violation gain; concrete instances of rules lagging the business. Three pieces of evidence, and the level names itself.

The checklists share one property: everything comes from documents and records that already exist, so filling the table spawns no new work streams. And a checklist you cannot complete is itself a finding: whichever parameter has the scarcest evidence in your organization is the dimmest region of your own knowledge — and dim regions are filled at the most dangerous level.

## 35.3 Combination rules: from parameter combinations to mechanisms

The table below is the core of this chapter. Each mechanism carries its trigger combination (parameter abbreviations: C = coupling, R = redundancy authenticity, I = incentive alignment, T = time pressure, S = scale, D = regulatory density). How to read it: fill in your six parameters, then check line by line; wherever your combination falls inside a row's trigger zone, that mechanism enters the candidate list. Candidates usually number three to six; then narrow to two or three with the filters in Section 35.4.

| Chapter | Mechanism | Trigger combination |
| -- | --------- | ------------------------- |
| 11 | Normalization of deviation | T = long (consequences delayed) + the same deviation has occurred at least twice with no consequence |
| 12 | The metric replaces the goal | I = systemically misaligned + superiors read only the numbers |
| 13 | Narrative precedes evidence | the decision has been publicly committed + time pressure short (no time to reopen the analysis) |
| 14 | Where expert intuition fails | S = network (entering unfamiliar terrain) + T = long (feedback delayed) |
| 15 | Procedural drift | T = short (violations carry no immediate consequence) + rules mismatch the real workload |
| 16 | Information decays through hierarchy | S = multiple teams or more + reporting is itself appraised (I ≠ aligned) |
| 17 | Misaligned incentives | I = systemically misaligned (the strongest single-parameter trigger on this table) |
| 18 | Diffusion of responsibility | S = multiple teams + a multi-party signature structure |
| 19 | Truth-tellers are culled first | I = systemically misaligned + performance decided unilaterally by superiors |
| 20 | The slack of success | T = long + a long accident-free history |
| 21 | Hidden coupling | C = high + the dependency list cannot be produced (a history of mergers, integrations, legacy systems) |
| 22 | The illusion of redundancy | R = medium or low + backups sharing origins with the primary |
| 23 | Extrapolating beyond validated boundaries | a pilot-to-rollout or cross-industry transplant is under way |
| 24 | Scale crossing thresholds | S = climbing from multiple teams toward a network + fast growth |
| 25 | Safety margin eaten away | T = medium or long + two or more consecutive cuts with no cumulative ledger |
| 26 | Automation and skill decay | high automation + falling hours of manual practice |
| 27 | Sunk cost and escalation | the investment is publicly visible + exit equals admitting error (I ≠ aligned) |
| 28 | Maturity mismatch | T = long + decision-makers' tenure shorter than the consequence cycle |
| 29 | The invisibility of maintenance | T = long + maintenance has no output metric + budget pressure |
| 30 | Handover gaps | S = multiple teams + fast staff turnover + documents that record only conclusions |
| 31 | Regulatory lag and capture | D = dense but captured |
| 32 | Compliant yet unsafe | D = dense + safety meetings discuss only whether a rule was violated |
| 33 | Correlated failure | C = high + S = network + concentrated dependencies (outsourcing, single supplier) |
| 34 | Path lock-in | the choice is 5 or more years old + alternatives no longer appear in selection discussions |

Three reminders for reading the table. First, I (incentive alignment) carries the highest weight: systemic misalignment lights up rows 12, 17, 19, and 27 at once; if you scored that level, build your candidate list on those four chapters. Second, the C and R combination (high + medium/low) lights up 21, 22, and 33 directly — the main axis for software and infrastructure situations. Third, "in progress" triggers (23's rollout, 24's scale climb) differ from state triggers: while the action is under way, fill the table again — when the rollout reaches its second region, the parameters may already have changed.

## 35.4 Narrowing from six candidates to two or three

Narrowing uses three filters, applied in order.

Filter one: evidence. For each candidate mechanism ask: in my situation, is there concrete evidence of the kind the mechanism's trigger criteria describe (Chapter 15's procedural drift, for instance, is triggered by "formal process and actual practice long diverged")? If you cannot produce a single concrete instance, demote it to an observation item; it does not enter the main list.

Filter two: layer position (Chapter 9). Which layer can you move? A frontline engineer can move only the technical and organizational layers, so mechanisms triggered primarily in the incentive layer (12, 17, 27, 28) are, for you, "findings to escalate" — rewrite them as a report moving upstream to someone who can act, not as "mechanisms I can prevent."

Filter three: time window. Consequences that land within your tenure go on the main list; consequences outside it go into a ledger with a named receiver. This is not avoidance: a risk nobody can act on is handled only when it is written into the handover (Chapter 30).

## 35.4bis The layer filter, worked once

Filter two is the one most often skipped, so here is a miniature demonstration. A mid-level engineer at a platform company completes the table; the main list includes Chapter 28 (maturity mismatch): no exit provisions anywhere, consequence cycles visibly outlasting every decision-maker's tenure, criteria matching on all counts. Then the layer question arrives: the engineer cannot move exit provisions — that terrain belongs to financing structure and the board. Chapter 28 therefore converts to an escalation item, and the escalation has a format: the criteria checked one by one, the evidence cited, the verified facts, and the recommended action for the decision layer, written in the shape that survives the upward journey (every upstream technique from Chapter 16 applies). The engineer also copies one line for personal use: a known structural risk, once written out, discharges the duty of discovery; left unwritten, it approaches complicity. Here the layer filter shows its real function — converting "what I cannot prevent" into "what I can report," so that the main list contains only locks to which you actually hold keys.

## 35.5 Printable version

```
Situation Assessment Table (Date: ____ Filled by: ____ Subject: ____ project/system)
┌──────────────────────────────────────────────────────────┐
│ 1 Coupling: low / medium / high             (basis: ____) │
│ 2 Redundancy authenticity: high / medium / low (basis: ____) │
│ 3 Incentive alignment: aligned / partially misaligned /     │
│   systemically misaligned                   (basis: ____) │
│ 4 Time pressure: short / medium / long      (basis: ____) │
│ 5 Scale: single team / multiple teams / network (basis: ____) │
│ 6 Regulatory density: none-sparse / dense / dense-but-captured │
│                                             (basis: ____) │
├──────────────────────────────────────────────────────────┤
│ Rows hit (against the 35.3 table): Ch. ____ _____________ │
│                  Ch. ____ _____________ │
│                  Ch. ____ _____________ │
│ Main list after filtering (2–3): ________________________ │
│ Moved to ledger with a named receiver: ___________________ │
└──────────────────────────────────────────────────────────┘
```

Filling discipline: every level must carry its basis (one sentence will do); a level without a basis is filled at the most dangerous level. What to do after filling is Chapter 36: fifteen minutes in the library, ten minutes writing the conclusion — the output is "which three deaths I most resemble."

## 35.6 Two filled examples

Two completed tables, side by side, show the instrument working.

Example one: a payments team at a SaaS company, fourteen people, two large customers signed and a third in the pipeline. Coupling: medium — payment failures spread along the order chain but manual rerouting contains them within the business line. Redundancy authenticity: medium — the fallback payment channel comes from the same vendor as the primary, and the switchover was rehearsed once, at launch. Incentive alignment: partially misaligned — release cadence counts in the team's appraisal, but risk control holds veto power over loss-bearing changes. Time pressure: short — quarterly revenue commitments make compressed verification pay immediately. Scale: multiple teams — payments depends on risk, reconciliation, and merchant integration. Regulatory density: sparse — the industry is lightly regulated; customer contracts do most of the constraining. Against the 35.3 table, four rows light up: 16 (multiple teams plus appraised reporting), 22 (medium redundancy, same-source), 24 (climbing toward network), and 12 on the edge — "superiors read only the numbers" lacks evidence, so it demotes to an observation item. The filters then run. Evidence: 16 stays (a loss-bearing complaint took three weeks to reach the team — a concrete instance); 22 stays (the fallback channel has never carried real traffic); 24 stays as "in progress," with the refilling date noted. Layer: all three live in the team lead's reachable layers. Time window: nothing to hand over. Main list: 16, 22, 24. Action list, three lines: read the three chapters' prevention sections; schedule one real switchover of the fallback channel, with the result logged; put "information arrival delay" on the agenda of the next quarterly review, named as such.

Example two: a surgical nursing unit, filled in by the charge nurse. Coupling: high — any check skipped acts on a patient directly; there is no containment. Redundancy authenticity: medium — second-line cover comes from the same roster pool. Incentive alignment: partially misaligned — theater turnover rate counts in performance, but the nursing directorate holds independent inspection authority. Time pressure: medium — complications surface in weeks to months. Scale: multiple teams — one operation is a three-way collaboration of surgery, anesthesia, and nursing. Regulatory density: dense. Three rows hit: 16, 18 (multi-party signature structure), and 32 (dense oversight; the unit's safety meetings, on a six-month minute review, have discussed violations exclusively — not one near-miss). The filters: 18 and 32 survive on evidence (the three-way check completes at signature, content-checking by conscience — 18 holds; 32 holds on the minutes); 16 demotes to escalation (the cross-department reporting structure is above the charge nurse's reach). Main list: 18, 32.

The comparison makes the point: same six parameters, different lives. The software team's list lands on information and redundancy; the nursing unit's lands on structure and compliance. The parameter combination decides which chapters you read — the table's job is not to answer, it is to stop you reading at random.

The table also runs as a ninety-minute meeting: fifteen minutes filling individually; an hour reading levels and bases aloud, parameter by parameter; the last fifteen minutes produce exactly one output — the two parameters with the widest disagreement, written up as action items. The discipline is Chapter 39's: argue about the basis, never about the person.

## 35.7 Calibration: making the table smarter over time

Calibration data must land in a format to compound. A minimal row: date, subject, the six levels, chapters hit, and a follow-up column. Six months later the follow-up column takes two entries: did the subject develop symptoms (what happened — or an explicit "nothing"), and did the hit hold (symptom mechanism matching the hit chapter means a hit; a mismatch is recorded as a miss, with the actual mechanism named). Versioning follows: the 35.3 mapping table carries a version number; each quarter governance reviews hits and misses against accumulated calibration; a mapping line is revised only after three or more misses, and every revision cites its calibration rows. The rules have one purpose — a table that gets smarter with use instead of aging at factory accuracy. And long calibration series yield a by-product: the mechanisms your organization hits repeatedly, year over year, are your failure fingerprint, and Chapter 39's pre-mortem topics come straight off it.

## 35.8 The three fingerprints

Certain parameter combinations recur so often they are worth naming, for fast triage.

Fingerprint A, the growing internet product: coupling medium-to-high, redundancy medium, incentives partially misaligned, time short, scale climbing, regulation sparse. Expect 16, 22, 24, 33. The theme: expansion converts yesterday's redundancy into today's single point — during a scale climb, last year's adequate backup no longer covers this year's dependency surface.

Fingerprint B, the heavily regulated operating unit — hospitals, nuclear, aviation maintenance: coupling high, redundancy medium, incentives partially misaligned, time medium-to-long, scale multiple teams, regulation dense or dense-but-captured. Expect 18 and 32, plus 31 where capture has evidence. The theme: the feeling of compliance replaces the inquiry into safety — every item passing becomes the proof that the whole is sound.

Fingerprint C, long-cycle infrastructure — construction, pipe networks, platform foundations: coupling high, redundancy low-to-medium, systemic misalignment common, time long, scale network, regulation dense but slow-updating. Expect 21, 25, 28, 29. The theme: invisible maintenance meets maturity mismatch — the consequence lands in the next term, the cut happens in this one.

Fingerprints save time: if your situation resembles one closely, read its chapters in the order given, then return and complete the evidence checklists. A fingerprint is a starting point; evidence is the landing. Where they conflict, trust the evidence.

## 35.9 Five common filling errors

Error one: optimistic levels. The basis column is blank, or the basis is a wish ("redundancy: high — we intend to build DR"). The design already answers this (no basis, most dangerous level), but the real cure is cross-filling: two people fill independently, and the level disagreements are more eloquent than any reminder.

Error two: filling the target state. The organization is mid-reform, and the filler describes the organization as it will be. Split the sheets: a present-state table for mechanism screening, a target-state table for the reform case — the level differences between them are precisely what the reform is buying. One blended table silences every warning, because you are matching triggers against an organization that does not exist.

Error three: filling once. The table becomes a one-time diagnosis. Parameters move — expansion raises scale, layoffs cut redundancy, a new appraisal scheme worsens incentives. Rutinize it: quarterly by calendar, plus event triggers (a new appraisal scheme, an expansion, a peer's major accident — each warrants a refill). The event-triggered fills are usually the most informative, because the event just changed your situation.

Error four: treating hits as diagnoses. The main list arrives and prevention devices get installed before any criterion is checked. The table yields candidates; confirmation requires each chapter's Section 1 criteria against concrete evidence — criteria with evidence stay, the rest demote to observation. Devices installed without confirmed criteria are placebos.

Error five: filling and hiding. The table goes in a drawer because the levels look bad. The private value of the table is finding risk; the organizational value is trend and distribution, and both require being seen. An unseen table equals no table — its entire content improved one person's intuition, and Chapter 14 has already described when intuition fails.

## 35.10 Filling by role

The same table reads differently from different chairs, and four common roles deserve their own instructions.

Frontline engineers: you can move the technical and organizational layers, so incentive misalignment — which you will usually score — is not your level to fix but your material to report. Keep two columns: preventable (mechanisms in your layers, with this chapter's devices attached) and reportable (incentive-layer mechanisms, written as evidence-bearing escalation items). Two columns, or the table degrades into a grievance list.

Middle managers: you operate four of the six parameters directly, and your filling precision determines the quality of the organizational roll-up. You are also the most exposed to error two, because you are usually the person executing the reform. Have your direct reports cross-fill your table: their incentive-alignment level is closer to the truth than yours.

Executives and boards: your evidence access is best for scale and regulation — fill those two; take the other four from the managers' roll-up rather than self-assessment. The executive view is the distribution chart and the extreme-quadrant list, not any single sheet.

External parties — auditors, diligence teams, regulators: you are filling someone else's situation without their ledgers, so discount by evidence availability: any parameter you cannot evidence starts at medium, marked "externally invisible," never at optimistic. The external table's highest value is comparison: lay it beside the subject's self-assessment, parameter by parameter, and the largest gaps become the first items of the question list.

One discipline spans all four roles: fill only the parameters you hold evidence for, and cite someone else's fill for the rest. The higher the chair, the stronger the temptation to imagine the front line — and the table distorts upward through power exactly the way information distorts upward through hierarchy (Chapter 16).

## 35.11 A rollout timetable

Week one: every key project owner fills a present-state table, one cross-fill each; outputs are main lists and draft actions. Organizational roll-ups are not the goal yet — a completed basis column is.

Quarter one: two things. First, convert the reading list into a two-hour collective reading session (one presenter per hit chapter; afterward each participant writes "which level I would now change" — the pre/post level shift is the direct measure of learning). Second, run one full follow-up loop: record the status of the first fill's subjects into the follow-up column, even if the entry reads "no symptoms; hit confirmed."

Year one: after four quarters, governance should hold four artifacts — a versioned mapping table, at least three rounds of calibration data, one distribution chart, and at least one pre-mortem scheduled off the distribution (Chapter 39). All four present, the table has become a system; any one missing, it is still paper.

The common break point is quarter two: novelty spent, the follow-up column starves. Bind follow-ups to a standing agenda item — ten minutes at the quarterly review, immovable. Agenda-ization is the only reliable antidote to forgetting, and it is the same underlying principle as Chapter 29's maintenance: what has no routine carrier vanishes into busyness.

## 35.12 Position in the book's toolchain

The assessment table is the first link of a chain with four downstream couplings. Chapter 36's thirty-minute walkthrough takes its input from here — the first half of the walkthrough (which three deaths) is the main list; without the table, walkthrough topics are chosen by impression, and impressions choose recent accidents, which are not necessarily where mechanisms are most active. Chapter 37's question sets are selected by hit — twenty-four sets are too many for one review; the hit chapters' questions go first, by chapter number. Chapter 38's post-mortems tag conclusions with mechanism names; tagged archives aggregate by mechanism and feed the calibration data, closing the loop into the 35.3 table. Chapter 39's pre-mortems take their topics from the distribution chart's extreme quadrant — one high-risk carrier per session. The chain's completion signal: a pre-mortem finding that survives a post-mortem and lands as one row of calibration data. Four couplings, one summary: the table converts "read a thick book" into "read two chapters, do three concrete things," and the rest of the chain carries each thing the rest of the way.

## 35.13 When the table hits nothing

Occasionally the six parameters come back clean and no row fires. Three explanations, in order of likelihood. First, optimism — error one in a cleaner costume; return to the evidence checklists, concentrating on incentive and redundancy, the two parameters most easily bent by self-image. Second, genuine cleanliness: low coupling, true redundancy, aligned incentives, sane cadence, countable scale, effective oversight — such situations exist, mostly small and stable teams, and for them the table's job is done; refill annually. Third, the most interesting: parameters all green and a bodily unease that will not clear — the opening line's "numbers look fine but something feels wrong." Unease usually tracks a dimension the parameters do not carry: the state of a key person, a process awkwardness nobody can name. Write it down anyway; it is the candidate for the table's next version. The order of operations for an empty result: suspect the table, then the filler, and only then believe the result.

## Self-check: five questions

1. Fill in the 35.5 table in five minutes: which level did you mark for incentive alignment? Would you dare show the basis to your team?
2. Of the six parameters, which can you answer with least confidence? What kind of information does that uncertainty say you are missing?
3. In your situation, which rows of the 35.3 table did you hit? Among the hit rows, which chapter have you never read?
4. In the past year, did your organization carry out one "rollout to a new environment"? Did anyone list "what changed compared with the pilot"?
5. Which level did you mark for time pressure? Recall your most recent decision to compress a verification process: does the reason still hold now?

(First draft of this chapter: 3,414 characters.)
