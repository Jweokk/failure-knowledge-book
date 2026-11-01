# Software and Internet Services | sw

> Five columns: record quality, feedback delay, coupling, the three deadliest mechanisms, and what outsiders most easily learn wrong.

## 1 Record quality

The world's only public postmortem ecosystem that no statute requires (the exception in Chapter 4). Vendor postmortems, the kind Cloudflare and GitHub publish along with monthly availability reports, give a timeline and a narrative of decisions; that is D-grade material, and the depth is substantial. Regulatory penalty documents from CNIL, the FTC and the ICO cover the data compliance side at C grade. The 9 sw cases here are made up of vendor postmortems (6) and regulatory penalties (3). The gap is security incidents. Intrusions and breaches almost never get a public postmortem, because the postmortem text doubles as an attack manual and legal liability has no ceiling; the public postmortem library has also been shrinking in recent years (Section 4.2). Retrieval channels are in, where blog scraping that times out should be retried with curl.

## 2 Feedback delay

The shortest in any industry. Change feedback arrives in seconds and minutes, since a canary release exposes the fault on a percentage of traffic first. Incident feedback arrives in minutes, through monitoring and alerting. Postmortem feedback arrives in weeks. That speed is the material basis of software's postmortem culture: feedback fast enough to carry a high-frequency learning loop. Inside the field the useful distinction is control plane against data plane. Data plane failures report back fast; control plane failures (dashboards, permissions, configuration) report back just as fast but are more easily underestimated, and the retry storm in sw-004 happened in the control plane.

## 3 Coupling

Coupling at global infrastructure scale. A single vendor's edge network carries distribution and security for traffic across the internet, as the three global events sw-001 to sw-003 show, and a shared substrate turns one point of semantic ambiguity into simultaneous failure for thousands of customers. Automated coupling adds a second layer: changes propagate by themselves (the feature file in sw-002 spreading with the deployment) and client retries amplify a fault (sw-004). Isolation measures are real (regionalization, canaries, rollback), yet common-mode failure keeps penetrating them, because the same configuration system, the same permission model or the same cleanup job sits underneath. The conclusion on coupling matches aviation's. High coupling has been pushed down by engineering, and the pushing down is a continuous process that carries a cost.

## 4 The three deadliest mechanisms

Hidden coupling (Chapter 21): a database permission change doubles the feature file (sw-002), a retry storm (sw-004), the empty-parameter semantics of a BYOIP cleanup (sw-003). Crossing a scale threshold (Chapter 24): record load breaks capacity that was calibrated on historical peaks (sw-005), bulk abuse of a registration system (the mirrored form of fi-004). Cascading failure (Chapter 33): downstream synchronization failing because the automation was shared. Next in frequency come misaligned incentives (the structural conflict in the data compliance cases sw-007 and sw-008) and practical drift (operations and documentation diverging).

## 5 What outsiders most easily learn wrong

Wrong lesson one: read postmortem culture as proof that the industry is safe. Postmortems mostly cover availability incidents that fell ill and recovered, not security incidents and not commercial failure, which is the boundary drawn in Chapter 4. Wrong lesson two: copy the word blameless without the machinery behind it. A blameless postmortem with no anonymization process and no separation from performance review is blameless rhetoric, the name-reality gap of Section 4.2. Wrong lesson three: treat fast rollback as a universal answer. Software can roll back because deployment is atomic and state can be versioned. Writing rollback into another industry's emergency plan without asking whether our state can be versioned is the commonest error in cross-industry transplant, and Chapter 4 states the four conditions that decide it.

## 6 Three questions from an outsider

Question one: what use is software's postmortem practice outside software? Software is the only living sample of a public postmortem culture, and Chapter 4 takes it apart. The blameless process, the game day exercise and the status page are all parts that travel, and Chapter 4 gives the conditions under which transplanting them works. Question two: are cloud platform outages far from my business? If your business depends on any cloud service or SaaS product, you are the downstream party in the cases on this page (Chapter 33, cascading failure). Do those providers appear on your supplier list? Question three: how can a software fault be isomorphic to a chemical explosion? The three layers of the failure chain do not care about industry. A bug in the technical layer, a missing review in the organizational layer, launch pressure in the incentive layer: when all three break at once the shape is the same, which is why Chapter 9 puts the two industries inside one model.

## 7 Mechanism distribution at a glance

This domain holds 9 cases, distributed as follows, most frequent first:

- Hidden coupling (6): sw-001, sw-002, sw-003, sw-004, sw-006, sw-008
- Cascading failure (3): sw-003, sw-004, sw-005
- Margin erosion (2): sw-001, sw-009
- Crossing a scale threshold (2): sw-002, sw-005
- Misaligned incentives (2): sw-007, sw-008
- Extrapolating past the validated domain (1): sw-001
- Illusion of redundancy (1): sw-006
- Compliant and unsafe (1): sw-007
- Invisibility of maintenance (1): sw-009

How to use the list: when a new incident write-up lands, guess the mechanism against this table before reading it. Your hit rate is your familiarity with the field's accent. Then read the text and check. Where you guessed wrong is the industry skin still sitting between you and the domain.

## 8 How this page is updated

A domain page is a live document. Once a year, take the new A and B grade reports in Software and Internet Services and check them against the five columns and the list in section 7. A mechanism that appears for the first time gets a line in section 4. A shift in frequency gets a new count in section 7. A new A-grade case enters the library under the field standards of Chapter 5. Trigger, owner and review date go into the user's calendar (Chapter 39). A domain page, like the ledger, is dead the moment nobody updates it.

## 9 The starter kit

Three items for a reader new to Software and Internet Services. Entry case: sw-001 (a WAF regular expression backtracks catastrophically, exhausts CPU, global outage; Cloudflare, 2019; link at Appendix B). Read it first for the house style and the grain size of a write-up in this field. Entry data source: the primary collection listed under software and internet services in. Find the entrance, bookmark it, visit once a quarter. Entry mechanism: start with the top row of the section 7 list and read that chapter against a case from here. One mechanism gets two passes, once in the mechanism chapter for the criteria, once in this domain for the local parameters. The three items take about one working day, and at the end of it you own a first coordinate system for the field.

## 10 Reservations

Three limits sit on the judgments above. The case library samples toward events with rich public records, and the skew is described in Chapter 2. The frequency order reflects this book's library, not the true distribution in the field. Institutions and technology move, so this page has a shelf life measured in years, and any citation of it should carry the year. Those three are the book's general disclaimer, and the threshold check of Chapter 1 applies to this book as much as to any other artifact.

## 11 The three layers in the software accent

The software accent is that the technical break is the youngest of the three. Code and configuration breakpoints travel from deploy to exposure in hours and days (the empty parameter in sw-003, the regular expression in sw-001), and the breakpoints in the organizational and incentive layers are just as young: the design of a monitoring blind spot, the approval exemption granted under launch pressure. The entire history of the industry is a few decades. The practical consequence for the nine-box walkthrough is that one table shows a full set of young breakpoints at every layer. Elsewhere a decade of evolution is needed to lay them down; software does it in a single release. The walkthrough is therefore efficient, and the lesson density is correspondingly high.

## 12 Case-to-chapter lookup

| Case ID | Mechanism chapter | One line |
|---|---|---|
| sw-001 | Chapter 21 Hidden Coupling | WAF regular expression backtracks catastrophically, exhausts CPU, global outage |
| sw-002 | Chapter 21 Hidden Coupling | Database permission change pushes the feature file past its limit, core traffic interrupted |
| sw-003 | Chapter 21 Hidden Coupling | BYOIP cleanup defect withdraws about 1,100 prefixes by mistake, outage over 6 hours |
| sw-004 | Chapter 21 Hidden Coupling | Retry storm from a dashboard overwhelms the tenant service |
| sw-005 | Chapter 24 Crossing a Scale Threshold | Record load breaks an under-provisioned component, authentication fails in cascade |
| sw-006 | Chapter 22 The Illusion of Redundancy | Background cleanup job drags down the primary database, order creation widely blocked |
| sw-007 | Chapter 17 Misaligned Incentives | CNIL fines Google €325 million: ads inserted between emails, invalid cookie consent |
| sw-008 | Chapter 21 Hidden Coupling | CNIL fines FNAC DARTY €7 million: app sent browsing data without consent |
| sw-009 | Chapter 25 Margin Erosion | CNIL fines France Travail €5 million: no MFA, weak passwords, data leak |

How to use the lookup: guess the mechanism from the section 7 distribution, then come here to find the chapter that carries the criteria and the countermeasures. The table does not replace the reading. It is a map, not the journey.

## 13 Closing note

A last piece of advice for software readers. The public postmortem culture is the industry's gift to everyone else (Chapter 4), but the gift's shelf life depends on conditions inside the industry, and the warning at the end of Chapter 4 is that culture has no legislative moat. Two self-checks. When was your organization's last public postmortem? If you cannot answer, the public culture is shrinking where you work. Does your blameless commitment have any isolation from the IT system, in the sense of Chapter 8? Software has already proved this can grow. Keep the four conditions of Chapter 4 in place and it will not be a flash in the pan.

The cases on this page share a feature no other industry has: the party writes its own postmortem. Cloudflare's and GitHub's texts are published in full, with technical detail reaching down to API parameters and individual lines of code, which would be unthinkable elsewhere and is itself one of the objects Chapter 4 studies. The reading advice is to read them in series. One company, four cases, sw-001 through sw-004: read four in a row and a single organization's failure fingerprint appears. The root cause differs every time and the propagation path repeats its pattern. Recognizing that pattern is the advanced training for a software reader, and what it produces is sensitivity to the fingerprint of your own organization. One more observation: every case here sits at a top platform. Outages at small and mid-size software companies get no public postmortem, so survivorship skew runs in this field too.

## 14 How the mechanisms vary here

Hidden coupling, software variation: the coupling cases share one signature, in that whoever executes the change does not know what the change touched. The lesson in sw-002 (a database permission change pushing the feature file past its limit) and sw-003 (a cleanup defect withdrawing prefixes by mistake) both sit in the coverage of the dependency graph: the dependencies of the permission system, the routing system and the cleanup job were never modelled. Read it this way: the reach rate of a change, meaning the ratio of the impact surface declared beforehand to the one found afterwards, is Chapter 21's criterion expressed as a number here. Software coupling is more hidden than chemical coupling in one respect: dependencies grow by themselves as versions drift (library upgrades, configuration merges), so a manual inventory decays faster than in any other industry. Automatic generation of the dependency graph is therefore a floor requirement, not an optimization.

Crossing a scale threshold, software variation: sw-005 (record load breaking an under-provisioned component) and sw-004 (a retry storm overwhelming the tenant service) show the two scales of software, load magnitude and feedback speed. Feedback here is measured in seconds, the fastest in the book, while capacity decisions are validated on a quarterly cycle through load testing. That mismatch of cycles is the structure of scale failure in software. Read it this way: component coverage between the load test environment and production, meaning how many components have never met real pressure. The lesson of sw-005 is that the weak component sat outside that coverage. The retry storm adds a layer specific to software: a defence (retry) becomes an amplifier under abnormal conditions, so any automatic retry needs a circuit breaker and jitter. That rule is the field's correction to the concept of redundancy in Chapter 22.

Regulatory lag and capture, software variation: sw-007 through sw-009, the three CNIL cases, show the enforcement style of data regulation. Fines are set as a share of turnover, remediation orders come as a system, and violations are found through complaints and audits. Read it this way: the ratio of compliance cost to violation benefit is badly asymmetric here, since the marginal return on using data is high and the chance of being caught is low, and the escalation of fines in the GDPR era is regulation catching up. Chapter 31's criterion, that rules update more slowly than the business, is measured in generations in this field, as the ratio of platform iteration cycle to legislative cycle. The sense that regulation is dense and still late is stronger for readers here than in any other field.

## 15 Reading in pairs

Read the software page against the public policy page, where po-003's dashboard rating and sw-004's dashboard retry make a mutual irony: in both, the metric layer has become the new failure surface. Against finance: the sw and fi enforcement cases share a time structure of long behavioural period and short discovery period, and fi-004's shell advisers beside sw-007's cookie consent shows compliance formalized in the same shape in two industries. Against manufacturing: software change management beside the manufacturing change order shows how far apart the two industries sit in the maturity of one device, since the change order is a more complete instrument than the software change approval.
