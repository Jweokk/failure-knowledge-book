# Chapter 21: Hidden Interactions; Interactive Complexity and Tight Coupling (Perrow)

> What this chapter covers: how two systems that "should have nothing to do with each other" come to share one inconspicuous thing; Perrow's interactive complexity, three criteria, four field sites, and an annual dependency-mapping regime.
> When to return: after system mergers, architecture restructuring, or supplier changes; when fault reports start saying "unknown cause."
> Reading time: 50 minutes.

Hidden coupling has one feature that distinguishes it from every other mechanism in this book: it cannot be managed before it is seen, and once it is managed it is no longer hidden. That sounds like a tautology; in fact it is the hardest problem statement in the entire field. You cannot initiate, budget, or schedule what you do not know exists. Perrow, in Normal Accidents (1984), listed interactive complexity as a structural source of accidents: the connections among components of modern systems exceed anyone's complete understanding, and faults propagate along paths their designers never imagined. Forty years on, systems are only more complex, and what this chapter can offer is a set of mapping disciplines that turn "unseen" into "seen" step by step.

## 1 What It Is

Definition: hidden coupling is the engineering face of interactive complexity: connections exist between systems that neither designer nor operator is aware of, and small faults travel across systems along invisible paths. The "hidden" in hidden coupling is not in the physical layer — the path really exists — it is in the cognitive layer: no one has ever drawn it, and therefore no one has ever managed it.

Three trigger criteria (if any one appears, the mechanism has already started):

① Two systems believed to be independent are found to share one "inconsequential" thing (an account, a pipe run, a permission, a battery, a bearing supply chain);
② Nobody can answer "if this goes down, who is affected";
③ Fault reports begin to contain "unknown cause" or "unexpected propagation path."

## 2 How It Grows

Four generating conditions. Condition one: organisational mergers and system integration. The connection between two systems is crossed off in the merger's diagrams but remains physically connected in the world; the merger documentation records "functional migration complete" and not "legacy connection physically retained." Condition two: legacy leftovers. A stopgap wiring from twenty years ago has outlived everyone who remembers it; the half-life of a stopgap is set by how long the person who originally installed it stays employed. Condition three: the depth of outsourcing and supply chains. What you buy is not the component but the component's component (a close cousin of Chapter 33's cascading failure: that chapter deals with the concentration of dependencies, this one with the invisibility of connections). Condition four: configuration drift. Permissions, parameters, and switches quietly link into new paths across successive changes; each change passed its own review, and the review examined the change itself, not the change's combination with the whole network.

One asymmetry about hiddenness must be carved into memory: coupling that has been seen gets managed, and coupling that gets managed is no longer hidden — so the stock of this mechanism always equals "the part nobody has drawn yet." The defence is therefore an unending survey, not a one-time cleanup.

## 3 The Mechanism in Four Domains

### Case 1 (Aviation): The Hidden Path between Control Channels

av-040. Leonardo AW169 (G-VSKP), 27 October 2018, Leicester City's stadium. AAIB formal report (AAR 1/2023, reviewed for this book; the report PDF states on page 14: a right yaw developed rapidly during the departure, and the pilot's immediate corrective inputs failed to arrest it): the helicopter lost control after lifting off at night from the centre-circle point of the pitch, struck the ground, and burned; all 5 people aboard (the pilot and 4 passengers) died (the report's casualty table: 1 crew fatality, 4 passenger fatalities, verified for this book). The investigation pointed to coupling behaviour between the channels of the flight control system: the interactions among the various control inputs, under a specific departure configuration, exceeded the pilot's immediate understanding 〔precise page citation of the agency-level coupling analysis〔open item: to be verified by deeper reading of the report volume〕〕. Two control functions each certified, each qualified — their combined behaviour was on no certification checklist.

Stop at the decision point: the night departure from the confined site, the seconds in which the pilot faced an unexpected control response. On the table: the instruments' indications, the city-light references, and a composite state training had never presented — plus a question the certification system never required anyone to answer: when these two channels act together, where will the pilot's hands and feet be. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Impact and fire; 5 people dead; the formal report took nearly five years to publish. Primary source: AAIB, AAR 1/2023, 2023; link in Appendix B, av-040.

### Case 2 (Software): One Permission Doubled a File

sw-002. The Cloudflare global edge network, 18 November 2025. Official postmortem (reviewed for this book): a database permission change doubled the size of the bot management feature file and pushed it over a limit; the bad file spread across the network through the deployment mechanism, and core traffic was widely disrupted for about three hours (11:20–14:30 UTC), with full system recovery at 17:06. The permission system and the feature distribution system were two governances, two monitors, two ledgers; their connection point was an "inconsequential" database grant. At the moment the change review passed, nobody was required to answer: once this permission is granted, whose file gets bigger?

Stop at the decision point: the moment the permission change request was approved. On the table: the justification for the grant, the completeness of the change process, and one field missing from every form: the downstream physical consequence of this grant. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Core traffic disrupted for about three hours; the response was to halt propagation of the bad file and roll back to the last-known-good configuration. Primary source: Cloudflare, 2025; link in Appendix B, sw-002.

### Case 3 (Chemical): The Relief Line Became a Propagation Path

ch-005. The Dow Louisiana Glycol II ethylene oxide unit, 14 July 2023, Plaquemine, Louisiana. CSB report (No. 2023-03-I-LA; the PDF of this report was downloaded and reviewed for this book): debris from a portable work lamp left behind during maintenance pierced a rupture disk and set off an explosion and fire; more than 31,000 pounds of ethylene oxide were released, and hundreds of nearby residents sheltered in place. The designed coupling point: the relief line was piped back into the ethylene oxide reflux drum — the system meant to route abnormal releases to a safe location became the path by which the explosion's energy entered the process system; and the vessel-closing procedure contained no "confirm emptied" step, so the work lamp left inside the reflux drum was known to no one.

Stop at the decision point: two moments. The first is the design and change review that routed the relief system back into the reflux drum: the review passed on process reasonableness, and nobody examined "the relief path connects to the process system" as a disaster-propagation path. The second is the execution of the closing work at the end of maintenance: the checklist had no "confirm emptied" item, and the work lamp stayed inside. On the table (the first): the line's relief-capacity calculations and the way the existing drawings drew it. On the table (the second): the work's completion status and the checklist's tick boxes. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Explosion, fire, and a large-scale release. Primary source: CSB, No. 2023-03-I-LA, 2026; link in Appendix B, ch-005.

### Case 4 (Maritime): Non-OEM Bearings and the Ship That Could Not Drop Anchor

ma-001. The survey vessel Kommandor Susan, 25 January 2025, the Firth of Forth, Scotland. MAIB report (Report 10/2026; PDF reviewed for this book): the main generator was catastrophically damaged by fire and the ship lost all electrical power; 1 engineer suffered severe lung, kidney, and eye injuries from smoke during the evacuation. The chained consequence of the blackout was that the anchor windlass could not work: the ship could not drop anchor in near-shore waters. The root cause traces to non-OEM bearings fitted during the 2019 shore overhaul, which wore out early — the substitution was made without the owner's knowledge (original text: non-OEM components, fitted without Hays Ships' knowledge). One decision in the supply chain (save money, save schedule) connects in a line to emergency capability six years later (the anchor windlass depends on the main electrical plant).

Stop at the decision point: the moment the overhaul plan approved the non-OEM part without disclosing it to the shipowner. On the table: the spare part's price and lead time, the equivalence declaration for the non-OEM part — and one question outside the overhaul contract's review scope: some night six years from now, what will this generator take away. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕1 person seriously injured; main machinery destroyed. Primary source: MAIB, Report 10/2026, 2026; link in Appendix B, ma-001.

## 4 What Shows Earliest

Six weak signals, each with the reason that usually overrides it.

1. Answering "if this goes down, who is affected" requires convening a meeting. Override: "systems are complex; that is normal."
2. Fault reports repeatedly show "propagation path unclear" or "recovered for unknown reasons." Override: "we logged it in the knowledge base."
3. The maintenance windows and change windows of two systems overlap heavily. Override: "one combined downtime saves effort."
4. The inventory of shared resources (accounts, certificates, pipe runs, power, people) does not exist or has not been updated in years. Override: "it is all in people's heads."
5. After a merger or outsourcing, the legacy system's ledger was never merged in. Override: "the functions were already migrated."
6. In some change's review record, the impact-scope field reads "none." Override: "a very small change."

## 5 How to Defend

Device one: annual dependency mapping. Once a year, draw the real dependency graph, working bottom-up: start from the least conspicuous shared resources (accounts, pipe runs, certificates, people) and ask "who uses this, and if it breaks, who is affected." The parts that cannot be drawn are the risk zone; register them separately (criterion ② becomes a ledger entry on the spot). The organisational key to mapping: the people unfamiliar with the system ask the questions; the people familiar with it answer — when the people who know the system draw it themselves, they draw the system in their memory, not the system in the physical world.

Device two: a mandatory impact-scope field in change review. The "impact scope" field on a change ticket is barred from saying "none": it must list at least three classes of parties to be queried (downstream systems, shared resources, emergency paths), with the queries on record. Cloudflare's permission ticket and Dow's pipeline change ticket both should have carried this question. The mandatory field does not make people smarter; it makes "never asked" checkable.

Device three: independent verification of emergency paths. For every critical emergency capability (dropping anchor, relief release, evacuation, rollback), run one independent drill per year on the assumption "the primary system is unavailable," verifying its true dependence on the primary system. Kommandor Susan's anchor windlass and Chapter 22's switchover drills converge here: an emergency capability's dependence on the primary system is the most expensive line on the coupling map, because it is only energised at the worst moment.

Device four: a register of shared resources. Every resource used by more than one system is registered item by item: name, users, failure impact, responsible person. The register is the skeleton of the dependency graph; without it, the graph starts from zero every year.

## 6 Boundaries with Adjacent Mechanisms

Against the illusion of redundancy (Chapter 22): coupling is a hidden line between independent systems (nobody knows they are connected); the illusion is common ancestry inside a redundancy pair (everybody knows they are connected; nobody treats it as a problem). The hidden lines drawn by Chapter 21's mapping, once entered into a redundancy register, become this chapter's common-cause entries.

Against cascading failure (Chapter 33): cascading deals with the concentration of dependency and the scale of propagation (suppliers, cloud, logistics networks); this chapter deals with the cognition of connection (nobody knows the line exists). Chapter 33's dependency register is the supply-chain subgraph of this chapter's mapping.

Against nonlinear scaling (Chapter 24): scale magnifies the search space of coupling: as node counts grow, unmapped connections grow faster. Organisations in rapid expansion should tighten annual mapping to quarterly — this is not advice; it is geometry.

## 7 Self-Check: Five Questions

1. In your system, name three things shared by more than one subsystem. If you cannot, how long has the mapping debt been running?
2. The most recent "unknown cause" fault — where is its postmortem filed? The hidden line usually hides in the second postmortem.
3. On your emergency capability list, which item has never been verified under the premise "primary system unavailable"?
4. When did your organisation last merge, outsource, or undergo a major restructuring? Did that round's legacy system ledger get merged in?
5. Pick a recent change ticket and look at the "impact scope" field. If it reads "none," ask the three classes of parties today — what comes back?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

The dependency map goes first — it is the atlas; change review and emergency verification are both flying blind without it. The shared-resource register follows (it collects the darkest class: power, accounts, tables, domains, people), the change-review impact-field mandate third (it moves the map into daily motion), independent emergency-path verification last (it audits the atlas's emergency sub-map). First ninety days: weeks one to three, the first map — not exhaustively but truthfully, reverse-engineered from the last three incidents' actual propagation paths (a reverse-drawn map beats a forward-filled form); weeks four to eight, open the shared-resource register with five categories to start — power, domains, shared accounts, common tables, single-person multi-role, the recurring cast of past incidents; month two, write the impact field into the change-review template (affected list, verification method, verification evidence); month three, run one emergency path with an independent walker — someone who didn't write the plan walks it as written, and wherever they stick is the first crack between plan and reality.

Failure modes. The map ages (eleven quiet months of silent dependency growth between annual surveys) — couple it to change review: new dependencies enter the map at review time, and the annual pass becomes a full audit of an incrementally maintained thing. The register drifts toward the visible (shared power gets a page; the shared service account never does) — install a trigger phrase: any design document containing "shared," "common," or "reuse" routes through registration. The impact field degrades into copy-paste ("none," or last change's text) — sample three changes a quarter and compare declared versus actual impact; big misses get a write-back and a retraining. Verification gets rehearsed in advance — no previews: minimal context, unannounced, and log the time-to-stuck.

Cost: the first map runs one to two weeks by system count, with the annual full pass at one to three days on top of incremental upkeep; register entries cost minutes each; the impact field is a form block; each emergency walk costs half a day. Against the 1,100 prefixes withdrawn by one cleanup bug, a relief line plumbed back into the process, or one tainted stabilizer reaching plants in multiple states — discovery is priced in hours and concealment in incidents, and the ratio is this chapter's whole reason.

Toolchain: the locator triggers on "high coupling plus a dependency question nobody can answer"; the reverse-drawn first map is the opening move. Question set 21's item 4 ("can 'who does this outage hit' be generated automatically") audits the map's maturity. Post-mortems: any "unseen propagation path" in the technical layer adds register entries. And the pre-mortem material pack's third item is Device 1's output — map and pack must appear in the same room, or the pack is decoration.

## Quick-Reference Card

**The mechanism in one sentence:** hidden coupling is the engineering face of interactive complexity: connections exist between systems that neither designer nor operator is aware of, and small faults travel across systems along invisible paths

**The three criteria, compressed:** 

**The devices (Section 5 has the detail):** Device one: annual dependency mapping; Device two: a mandatory impact-scope field in change review; Device three: independent verification of emergency paths; Device four: a register of shared resources.

**The four loudest weak signals (Section 4):** Answering "if this goes down, who is affected" requires convening a meeting. Override: "systems are complex…; Fault reports repeatedly show "propagation path unclear" or "recovered for unknown reasons." Override: "we…; The maintenance windows and change windows of two systems overlap heavily. Override: "one combined downtime…; The inventory of shared resources (accounts, certificates, pipe runs, power, people) does not exist or has….

**Cost register and case index:** av-040: 机上5人全部死亡（飞行员1人、乘客4人）；撞击后起火机体烧毁; ch-005: 释放超31,000磅环氧乙烷；周边数百居民就地避险; ma-001: 1名工程师重伤（烟尘致肺、肾、眼损伤，原文核实）；主发电机损毁; sw-002: 核心流量大面积中断约3小时（11:20–14:30 UTC）；17:06全系统恢.

**Domain cross-reference:** this chapter's cases live on the Aviation, Chemical, Maritime, Software domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** The invisible path is the real path: failures travel along dependencies, not along the org chart.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "who knew it would touch that" belongs here; the check action is the shared-resource register.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: see Section 6 (read the boundary discussion in Section 6 first). Question set 21 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(First draft: 4,081 Chinese characters; English edition independently written.)
