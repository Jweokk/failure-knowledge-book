# Chapter 4 Why This Method Did Not Spread

> What this chapter covers: five domains proved that failure can be turned into an institution, so why has that institution stayed inside them for sixty years, and what special conditions let software become the one exception.
> When to come back: when you are about to propose "let's build a postmortem system" to management, or when you need to judge whether an industry's failure knowledge can be expected to grow on its own.
> Reading time: about 25 minutes.

None of the four devices listed in Chapter 3 depends on advanced technology, and none is expensive to legislate. Aviation had the full set installed by the middle of the twentieth century. In the seventy years since, no industry outside safety regulation has copied the set whole. The reason is structural. It sits in the incentive structure, and no one's negligence is required. This chapter counts the five gates in the way, takes apart the software exception, then hands over a framework for judging your own industry: whether it could grow this system, and whether you should wait for it.

The chapter's place in the book is worth stating once. It works as a pressure valve. A reader who finishes Chapter 3 tends to ask why, if the arrangement is this good, their own industry does not have it. The answer this chapter gives is that the absence is not a verdict on your industry. It is the mechanics of five gates.

Relief is followed by a turn, from waiting for an institution to building one. The templates in Chapters 38 and 39 exist for people who will not wait. The psychological threshold on that turn is loneliness. An organization that builds its own system is a minority inside its industry, and a minority does not need encouragement. It needs proof that peers exist. Software and the five precedent domains supply that proof: building your own was never naive, because it has precedents, tools, and an endpoint.

This chapter hands over all three. Precedents are in Chapter 3. Tools are in Part 5. The endpoint is in Chapter 40, which draws the boundary of a self-built methodology.

## 4.1 The Five Gates

Gate one: liability. Writing down the details of a failure amounts to organizing the evidence for a lawsuit nobody has filed yet.

The five gates do not weigh the same, and the weight distribution varies enormously across industries. Aviation carries a light liability gate, because statutory liability isolation exists, and a heavy cost gate, because the public does not read accident reports. Software carries the lightest liability gate of any industry and the heaviest institutional gate, since nothing is legislated. Manufacturing carries the heaviest competition gate, because process detail is intelligence. A reader can score the five gates for their own industry, one to five each, and treat the two highest scores as the principal obstacles. Resources belong there. Spreading effort evenly across all five is the standard waste of institution building.

The distribution also moves. Technology changes the weight of the competition gate, since digitized process information lowers the threshold for arming a rival. Changes in the legal environment move the liability gate. Re-scoring once a year is routine work for anyone who keeps an industry's records.

Where the liability gate sits for internal postmortems is a question every legal department knows cold, under the discovery rules that govern what must be produced in litigation. The clearer the document, the harder the defense later. The rational choice is to write the postmortem vaguely, or to leave it unwritten. Compliance documents such as inspection records and training sign-in sheets have mandated formats and must exist. A causal postmortem carries no such obligation, and is better not written at all. That is the real legal position of postmortem culture in a great many organizations.

There is a mature line of remedy for the liability gate, and it lives inside the law. Privilege and protection regimes already exist in various forms across legal systems: privilege attaching to audit workpapers, statutory protection for quality assessments, immunity clauses covering investigation reports. The design point is to pin down what a document may be used for, safety improvement only, never liability or litigation. Pinning it down takes a written clause plus usage discipline, and the clause has to specify where each part of the document is allowed to travel.

Protected documents already exist in regulated industries, which shows the route works: operating event reports in nuclear power enjoy limited protection under the laws of several countries. Resistance to transplanting the idea comes from an instinct inside legal departments, since every newly protected document is one more object that can be challenged. The trade-off between resistance and benefit is best settled in one three-party legal meeting, with corporate counsel, industry association counsel, and the regulatory line arguing it out together. Loosening the liability gate has always been talked through by lawyers. It has never been shouted through by engineers.

A document management protocol is the second tool on this gate, and it complements protection. Most jurisdictions have well-developed means for handling internal documents: labeling the purpose, restricting distribution, applying retention rules. The purpose is not to destroy evidence, which is a serious offense, but to keep causal discussion and compliance records under separate management during normal operations, before any litigation starts.

The protocol has to be signed jointly by legal and safety. Safety understands what the content is worth. Legal understands where exposure begins. A protocol designed by one side alone will be defective on the other side. The output is a single document: which class of postmortem text carries which purpose label, how long it is kept, who may read it. The cost is one cross-department meeting and half a page of text. What it buys is a downgrade of the liability gate from absolute barrier to manageable constraint.

The boundary clause goes in the first paragraph. The protocol covers causal analysis written voluntarily; it does not cover records under a statutory retention obligation. Once that boundary is clear, the protocol survives scrutiny from both legal and the regulator. 〔Verification pending: a cross-jurisdiction comparison would need legal databases; this passage is a qualitative statement〕

Gate two: competition. Failure detail is concentrated competitive intelligence. A crash investigation report names the component, the fuel line, the checklist that failed. A postmortem of a commercial failure names the supplier, the parameter, the channel that failed. The first is read by the whole industry. The second is read by your competitors, among others. The patent system protects technical solutions. It does not protect lessons. Lessons lie in the rubble of the loser, and only competitors go digging there.

One economic exit exists for this gate: the alliance scale of a shared pool. The competition gate is tight between two rivals and loose among forty, because competitive intensity is diluted by scale. The more members a pool has, the less any single firm exposes and the more it gains.

A pool needs two mechanisms. A contribution threshold, meaning you submit cards to get in. An access rule, meaning you see as much as you contribute. Both exist to stop free-riding, since read-only members will kill the pool. Precedents are everywhere once you look: insurance loss pools, and shared engine fleet data in aviation, which is a mature model. The model rests on two conditions, member homogeneity and a trusted third-party custodian, usually an industry association or a reinsurer. If competition in your industry is too fierce to share anything, the first question is whether a custodian has been found.

Gate three: face. The organizational narrative is an asset.

The deepest layer of this gate is individual psychology, where admitting error collides with narrative identity. A manager's professional identity is built on the correctness of past decisions, and a postmortem that looks directly at error is a direct challenge to that identity. At the individual level, the face gate runs on the motivated reasoning of Chapter 13.

The individual remedy comes out of psychology as identity expansion: fold the ability to write postmortems into the professional identity itself, so that a manager's image moves from never wrong to good at correction. Redefinition turns the postmortem from a threat into a stage. The driver of that redefinition is almost always the top of the organization, because only modeling from the top gives it credibility. Chapter 19's endpoint criterion, senior people admitting error in public at no cost, functions here as a cultural switch again.

A listed company's prospectus carries a section headed "Risk Factors", and any reader can run an experiment on it. Pull ten prospectuses at random and compare how the risk factors are written. The language comes out heavily templated. Disclosure specific enough to say "this accident happened in our history, and it cost us this much" is rare, because that would be using a statutory document to characterize your own past. 〔Verification pending: systematic testing would require sampling full prospectus text on SEC EDGAR; this is an operational suggestion the reader can check in an afternoon〕

The face gate reaches well past listed companies. Founders' public narratives, anniversary celebrations, government achievement reports, all of them run in the same direction. Failure has no column inches in that direction.

Inside the organization the gate has a human resources variant, since the space for failure in the internal narrative is just as scarce. The annual meeting tells success stories. The internal newsletter profiles excellent teams. Promotion defenses report achievements. Internal memory skews toward success exactly as the external narrative does. The consequence is quiet: failure knowledge can only circulate as gossip, passed by word of mouth and private aside. Gossip has no structure, fails all three tests of Chapter 1, and the more of it circulates the lower the quality of the organization's failure knowledge.

The remedy is to give failure a formal slot: a standing item on the monthly review meeting agenda, a lessons column in the internal newsletter, a failure section in the internal knowledge base. All three share one requirement, a named-credit system that makes writing about failure an achievement that can appear in a promotion file. The cost of the arrangement is opening an agenda item and a column. What changes is the ratio of the organizational narrative, and a ratio held for one year changes the failure literacy of a generation inside that organization.

A communications exit exists as well: turn failure into an honor narrative, finance it from the opposite direction. An industry award for the best postmortem makes writing about failure an act that earns standing. The design point is the judging standard, which should score by this book's card quality criteria, the completeness of fact layer, condition layer, and structural layer, and not by how good the story is. The supplier of such an award should be an industry association or a foundation, a third party with credibility. The output is an annual selection, and that selection is the industry's first batch of qualified cards.

Loosening an honor gate has plenty of precedent in human experience. Medicine's morbidity and mortality conference turned public discussion of death cases into part of professional honor. The M&M conference is a ready template for industries outside healthcare to copy, and its charter, its blameless culture, and its conventions of frequency are all documented in public literature.

Gate four: institutions. The most expensive of the four devices is the independent investigation body, and it needs legislation. A body without investigative powers cannot write the full process. Reporters cannot obtain the docket, scholars cannot get onto the site, insiders cannot publish the whole text. Investigative power is a public power, and public power is generally paid for by a disaster large enough. Section 4.3 takes that up.

A lighter substitute sits in the middle: an industry joint investigation panel. No standing institution, no permanent staff. An association convenes it, member firms supply experts, and the team forms per event. Independence and expertise land between an internal postmortem and a national agency. The panel fits industry-level accidents of medium size, the ones too small for a national case and too murky for an internal review. Its institutional cost is very low, a charter plus an expert roster. Its credibility rests on two clauses: recusal, so that no investigator has a material interest in the company involved, and a commitment to publish the report in full. Prototypes of the joint panel can be found in industry bodies of the Flight Safety Foundation type. The distance from prototype to working model is one charter meeting and five live investigations.

Gate five: cost. Writing a postmortem consumes hours. Reading one consumes capability. Indexing and maintaining the collection consumes headcount.

One remedy on this gate is underestimated: let students and newcomers make the cards. Card production is unusually good entry training, since it drills reading a report, extracting fields, and mapping to mechanisms in a single pass. The channel is a course partnership with a school, with the accident analysis course using real cards as assignments and the best of them entering the industry library under the student's name. The design point is the quality gate. The inclusion standard does not drop because the author is a student. A single standard is what keeps a library alive.

The economics work out on both sides: teaching needs real material, the industry needs throughput, and cards are the medium of exchange. Of all the remedies on the cost gate this is the most elegant. The education system is the circulation partner this field should always have had and never did.

Circulation works for success because a media industry pays for it. Failure has no business model. Nobody subscribes to accident reports, nobody pays for a postmortem, and retelling one generates no traffic.

The cost gate has a hidden dimension, an asymmetry in capability. Writing can be made cheaper with a template. Reading cannot, because reading needs a pattern library: without the twenty-four mechanisms as a frame, what comes off the page is a story. That half of the capability is the reason this book exists. The routes to building it are laid out in Chapters 35 to 39, through the morning meeting, the positioning table, the playbook, and the budget. This chapter only needs to explain why the capability belongs on the cost ledger. Teaching one person to read postmortems well takes dozens of cards read closely, and those hours are a real cost. If the cost never enters a budget, the capability never gets built.

Writing reading capability into job descriptions and the training budget, which the budget template of Chapter 39 carries as a line item, is the enterprise-side remedy for this gate. An enterprise can treat exactly one of the five: cost. The other four sit at industry and legal level. Enterprise readers should therefore put all of their attention here.

Of the five gates, the first four are incentive problems. The fifth is plain market failure.

A technical exit on the cost gate is maturing: make the reports machine-readable. Regulatory documents are trending toward structured data, and XBRL in financial reporting proves that a document can be read by a person and by a machine at once. Machine-readable failure knowledge pushes reading cost down by an order of magnitude, since retrieval, comparison, and aggregation become automatic. Reading three hundred pages by hand and extracting fields by machine belong to two different eras.

The precondition is a field standard for the document. This book's twelve fields are one candidate: if regulatory reports were labeled to a comparable scheme, the reading cost of circulation would drop a tier at once. The promoter of such a standard can be a user alliance, with financial institutions, insurers, and research bodies jointly proposing structure to a regulator. Collective user voice is the strongest force behind document standardization, and the model is the history of financial data users pushing XBRL into place.

## 4.2 The Software Exception: How the Public Postmortem Survived

Over the past decade and a half, the software and internet services industry grew the only large-scale body of public failure knowledge in the world with no statutory basis behind it: the public postmortem, and the methodology built around it. A landmark is the methods literature that Google's Site Reliability Engineering (SRE) team published openly in 2016, whose operating discipline for the blameless postmortem has been widely paraphrased since. Earlier practice took shape inside several leading internet companies, and the name itself is usually traced to the engineering blogs of a handful of those firms in the early 2010s. The representative public text is the SRE handbook at sre.google, verified as accessible. Earlier texts that carried the name as it spread have been lost or migrated, and are not cited here.

The exception deserves a device-by-device dissection, because it shows how four devices get assembled with no legislation at all.

The substitute for device one, mandatory reporting: changes and outages are high-frequency events, monitoring systems generate event records automatically, and the on-call regime requires a postmortem. The ticket does not close until the write-up is done. No statute exists, but a workflow does.

The substitute for device two, independent investigation: the postmortem is moderated by an engineer from a team that was not involved, on a fixed pattern. The people involved narrate, the moderator probes, the conclusions are anonymized. Independence comes from rotating the process, with no institutional headcount behind it.

The substitute for device three, publication of the full text: status page culture and incident notices to customers. Public postmortems cover only outages with a wide blast radius, yet the public libraries of the leading firms have accumulated several hundred entries, all of them searchable in full.

The substitute for device four, liability isolation: the blameless principle. The output of a postmortem is defined as a set of system improvements, never as a list of human errors. Whether the performance system actually quarantines incident records varies from company to company. This is the device most often honored in name only across software's postmortem institutions: the institution is called blameless, and the incident history still counts in a promotion defense.

There is a blunt way to test whether the name matches the practice. Trace where one incident record flows after it is written. Who read it, whose file it entered, whose evaluation it affected. Tracing the flow is the measurement.

The measurement usually produces embarrassment. The readers turn out to be management rather than the improvement group, and the attachment turns out to be review material rather than a work ticket. That embarrassment is the starting point for governance, because unless the flow changes, blameless is decoration. The design work for flow governance is set out in full in Chapter 19, covering external custody, immunity clauses, and archive separation. This chapter sets one test: a postmortem that cannot answer where it goes means the postmortem culture around it sits somewhere between the name and the practice.

The substitutes hold together because of four conditions in the industry.

A portability test is a small tool worth carrying away: score your own industry against the four conditions, present or absent. An industry missing one or two cannot copy the software model whole, but it can copy its parts. The blameless moderation process, the change-linked method of attribution, the output definition inside a postmortem template. Parts do not need the full set of industry conditions, and the parts-level transplant list is laid out in the templates of Part 5. What this chapter owes the reader is the reason parts detach and still work: their conditions are an order of magnitude looser than those of the assembled system. Parts solve the technical side of a postmortem, how to moderate, how to attribute, how to define the output. The industry conditions constrain the incentive side, why anyone writes at all and who reads the result. Technical parts carry no incentive precondition. Only the incentive side needs the conditions. Keep the two apart and the transplant budget goes to the right place.

Condition one: the object of failure is infrastructure. A service outage has no criminal dimension, the loss is capped by service level agreement (SLA) payouts, and the legal exposure of writing a postmortem is far smaller than in other industries.

Condition two: the industry has a written culture. Design documents, code review, change tickets. An engineer's ordinary work already lands on the page, and a postmortem is one more document type among familiar ones.

Condition three: failures are frequent and causally traceable. Canary releases and change management systems let the link between a given change and a given outage be drawn automatically. The sample size and the attributability are things other industries do not have.

Condition four: talent moves quickly. Engineers pass between companies and carry postmortem practice as a job skill, so the norm standardizes across the industry without any legislation.

Those same conditions mark the boundary of the exception. Software postmortems cover availability failures. Security incidents, data breaches and intrusions, hardly ever get a public postmortem, because the text itself is an attack manual and the legal liability is nowhere near capped. Product failures, meaning the wrong feature was built, and business failures, meaning the wrong market was chosen, sit outside this tradition altogether and fall back under the five gates of section 4.1.

A further boundary is a trend. In recent years the complete public postmortems from leading companies have grown fewer, status page disclosure has grown briefer, and the public libraries have slowed their rate of update. 〔Verification pending: a quantitative trend would need year-by-year counts of the public libraries; this is a qualitative judgment〕 The exception has no legislative moat. It is a function of industry conditions, and when the conditions shift, the exception contracts.

The contraction can be read in the other direction too, and that reading should be stated plainly. Contraction is market behavior rather than decline. The volume of public postmortems rises and falls with the cost-benefit calculation of the industry publishing them. It follows the market.

That reading carries a warning for anyone who cites these libraries. Do not treat any industry's transparency as a permanent feature. The library you quote may stop updating in five years, so cited knowledge needs a local copy. The knowledge pack principle of Chapter 30 applies here: an external library will walk away, your own card library will not. The same discipline serves researchers and procurement people alike. Archive a snapshot whenever you cite an external postmortem, because the archiving rules in Appendix C are as necessary in software as anywhere else.

## 4.3 The Institution Is the Price a Disaster Paid

Look back at the legislative history of the four devices and one pattern repeats. They are almost always written after a major disaster.

In chemicals, the U.S. Chemical Safety and Hazard Investigation Board (CSB) was established under the Clean Air Act Amendments of 1990. The legislative backdrop included the pressure from events such as the December 1984 toxic gas release at the pesticide plant in Bhopal, India, where thousands died; the count of immediate deaths is a matter for later investigations and government statistics. 〔Verification pending: the official figure would require Indian government archives; estimates vary widely, and the text keeps the qualitative "thousands"〕 In finance, the Sarbanes–Oxley Act of 2002 followed close behind the 2001 bankruptcies of Enron and WorldCom.

In aviation, the international investigation framework ratcheted upward through a run of accidents in the postwar jet age. After the collision of two aircraft at Tenerife on 27 March 1977, which killed 583 people and was investigated by the Dutch, Spanish, and American sides with the final report issued by the Spanish authorities, the International Civil Aviation Organization (ICAO) moved revisions through on radio phraseology and cockpit communication procedure. 〔Verification pending: the official archive page for the Spanish investigation report remains to be located; this sentence has been written as a qualitative statement〕 〔Verification pending: the original ICAO Doc series texts need checking〕

Disaster pays first and the institution is written afterwards. That order tells you institutions are not created because someone recognized their importance. They are forced into existence by the pricing of loss.

The order has an observable byproduct. An institution built after a disaster usually fixes only the class of problem that disaster belonged to, which is what targeted legislation looks like: chemicals after Bhopal, financial audit after Enron. Targeting makes legislation fast, since the problem is clear and the pressure is concentrated. It also fragments the record system. Each disaster yields one agency or one act, and the institutions share no infrastructure with each other. The five precedent industries cannot exchange anything.

The direction out of fragmentation is to make the institution's infrastructure. Shared field standards for reports, shared retrieval infrastructure, mutually recognized evidence grading. One build at the infrastructure layer would serve every targeted institution at once. The promoter of that can only be a cross-industry user alliance, with insurance, academia, and media as natural members, and the object of the push is a shared tool of the kind this book is. If the twelve-field standard gets adopted by card libraries in several industries at once, infrastructure has begun to exist.

Three uses follow for the reader.

Use one: assess your industry. If your industry has no failure record system, the meaning is that losses have not yet grown large enough to force legislation, or that losses are absorbed by many small parties whose aggregation never becomes legislative pressure.

Use two: look for cheaper substitutes. Waiting for a disaster to buy the institution is the most expensive route there is. Industry self-regulatory alliances, shared postmortem libraries with liability immunity clauses, and insurer-led data pools have all been used as substitutes in the past, and section 4.4 gives the conditions under which each one stands.

Use three: the timing problem for whoever builds institutions. The disaster-buys-institution model has a corollary that runs against intuition. The window after a disaster is very short, since a legislative window usually closes before public memory fades. The operational answer is to pre-draft: an industry body keeps a finished legislative proposal on the shelf year round, so that when the disaster arrives, while everyone else is mourning, it has text.

Pre-drafting has precedent throughout legislative history. Most of the provisions that pass quickly after a disaster existed as proposals before it. The cost of keeping text ready is one drafting pass and an annual update. The return shows up in the catch rate at each window. The case format and the appendix system in this book are half of that pre-drafted text for your industry. The other half has to be filled in with your industry's own parameters.

## 4.4 Will Your Industry Grow This System?

Three criteria. Score each one.

Criterion one: the externality of failure. Does the failure hurt you, or the public? A failure that hurts the public eventually draws regulation, and regulation will sooner or later be pushed into building a record system. All five precedent domains are high-externality industries. A failure that hurts only you will never grow an institution, and self-discipline is the ceiling.

Criterion two: the rate of technical iteration. When the rules update more slowly than the technology, a regulator's record system cannot keep up with its own object. Fast-iterating industries are more likely to spread the norm through practitioner mobility, which is the necessary condition of the software model. Slow-iterating industries get there through legislation, which is the nuclear model.

Criterion three: practitioner mobility. Talent flow is what turns a case lesson into industry common knowledge. In low-mobility industries, utilities and some monopolies among them, lessons stay trapped in the original organization until that organization disappears.

An industry scoring on all three can expect a software-style postmortem tradition to grow on its own. An industry missing two of the three should build internally and stop waiting for the industry, and Chapters 38 and 39 supply the templates. The judgment is itself a form of prevention: knowing which kind of disaster your industry is waiting to pay the bill means at least knowing the shape of the invoice.

One addition at the level of use: read the three criteria dynamically. All three parameters move with time. Mobility rises and falls with the industry cycle, externality heats up as a regulatory issue gains prominence, iteration speed shifts with each technology generation. The operational form is to fold the three criteria into the annual industry scan, which the intelligence function of Chapter 33 can do in passing: rescore once a year.

The movement of the scores carries more information than the level of the scores. An industry whose mobility has turned from rising to falling is losing the conditions for the software model. The window is not only legislative. It is also cultural. The annual scan of windows is the last lesson this chapter has for an industry observer: institutions do not wait indefinitely, and they have a flowering season.

The shape of the invoice can be drawn as a prediction table from your industry's parameters. Score the three criteria, then lay the combination against the history of the five precedent industries and ask which way your industry's institution would arrive. The columns of the table are institutional forms: a national investigation body, an industry joint panel, an insurance data pool, an enterprise-built system, or nothing ever. The rows are combinations of scores.

The table is not fatalism. It gives a baseline, meaning the default trajectory with no intervention, and the value of a baseline is that it makes the need for intervention calculable. If the baseline says nothing ever appears, and you judge that the industry needs a record system, then the material for your argument is the difference row.

The difference row is the strongest opening a policy discussion can have: by baseline our industry will never grow a record system, and our loss curve says we need one, which is why there is a proposal on the table.

A ready comparison is the Indian cryptocurrency exchange Koinex, case st-002 in Appendix B. The founders' shutdown postmortem put the cause of death on banks freezing payment channels. Regulatory uncertainty travelled through financial infrastructure, and the industry made no wrong product decision at any point. This is the startup-shaped sample of criterion one, with the externality landing outside the practitioner: the disaster your industry is waiting for is sometimes one you did not make.

## Five Self-Checks

1. In your organization's most recent internal postmortem, did legal take part in reviewing the draft? What did the review change?
2. In your industry, how much is failure detail worth as competitive intelligence? Name one specific field where writing it down amounts to arming a rival.
3. In your industry's prospectuses, annual reports, or public materials, how templated is risk disclosure? Compare two of them and count the places where disclosure gets as far as a number.
4. Of the four software conditions, infrastructure as the object of failure, a written culture, frequent and attributable failures, and talent mobility, which does your industry lack? The missing conditions decide whether you copy the software model or the nuclear model.
5. The last time your industry's disaster bought an institution, what did it buy? If that invoice were issued again, where would your organization rank among the claimants?
