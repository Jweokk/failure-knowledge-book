# Chapter 22: Illusion of Redundancy; Common-Cause Failure

> What this chapter covers: why two backups fail together; three criteria of common-cause failure, four field sites, the arithmetic of redundancy, and the verification standard of "heterogeneous and truly rehearsed."
> When to return: when reviewing a redundancy design, procuring a backup system, or when someone answers a single-point-of-failure challenge with "we have two."
> Reading time: 50 minutes.

"We have two" is the sentence in engineering conversation most in need of a follow-up question. The follow-up is not "where is the second set" but three more expensive questions: how does it differ from the first? Who has verified that it works on its own? Has the act of switching to it ever been performed under real pressure? Ask all three and many "two sets" shrink to "one and a half sets," or even "one set with a manual." This chapter is about that shrinking process: how redundancy loses its independence at every stage — procurement, design, rehearsal — until the day the common cause arrives and every "set" fails together.

## 1 What It Is

Definition: the illusion of redundancy means multiple defences that coexist on paper are in fact one line: they share the same power supply, the same vendor, the same drawings, the same crew, or the same assumption. When the common cause arrives, the sets fail together. Engineering's name for it is common-cause failure; "illusion" stresses its cognitive face: auditors count the number of defences; attackers count the kinds.

Three trigger criteria (if any one appears, the mechanism has already started):

① Two "independent" defences share a common item: power supply, vendor, algorithm, drawings, personnel, location, or the same assumption;
② The redundancy has never been verified in isolation: turning off the primary system to try the backup has never happened;
③ Switchover has never been rehearsed under real pressure (every switchover drill was completed inside a planned window, at low load, with an escape route).

## 2 How It Grows

Three generating conditions. Condition one: the scale logic of procurement. A second system from the same vendor is cheaper, integrates better, and spares the operations team a second learning curve; heterogeneity means double the learning and operations cost, so the budget rationally drifts to a common source. Nobody decides "we want a common source"; each locally optimal step simply points at it. Condition two: design reuse. The backup inherits the primary system's drawings and assumptions, and the error in the design is faithfully copied into the backup — even the error is redundant. Condition three: cost avoidance in rehearsal. A real switchover carries risk, real pressure carries business impact, so the switchover gets arranged as a ritual familiar to both sides: planned window, low load, rollback available at any time. The ritual completes, and the drill record reads "success."

The arithmetic of common-cause failure is the point of this chapter. Let a single defence's annual failure probability be p: the joint probability of two independent sets is roughly p² — redundancy's benefit comes from multiplication. But if the two sets share a common-cause failure probability c, the joint probability is roughly c + p²: the order of magnitude returns from multiplication to addition, and redundancy's benefit evaporates. Until the common cause is removed, the arithmetic of redundancy is false; this is why criterion ① asks about "common items" rather than "number of sets."

## 3 The Mechanism in Four Domains

### Case 1 (Aviation): A Map Treated as a Collision-Avoidance System

av-022. Bell 206L-4 (N193AL) and the floatplane DHC-2 (N97EL), 4 September 2023, roughly 1,000 feet above King Salmon, Alaska. NTSB final report (ANC23LA071, downloaded and reviewed for this book): the two aircraft collided in mid-air; 1 person on the helicopter suffered minor injuries and all 7 on the plane were uninjured. The helicopter crew were operating with the ADS-B electronic map as their traffic-awareness and collision-avoidance reference — and the DHC-2 they collided with had no ADS-B installed: the traffic picture on the helicopter's screen did not, by nature, contain such targets. The paper redundancy of collision avoidance (visual look-out plus electronic map) was left standing on one leg: part of the crew's visual scanning habit had already been ceded to the screen, and the screen stayed silent about targets it could not see.

Stop at the decision point: the flight time during which the helicopter crew treated the map display as their basis for traffic awareness. On the table: the target list on the screen, the operating habit of "see and avoid," and one question nobody had checked — how much is out there that the screen does not display. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Mid-air collision. Primary source: NTSB, ANC23LA071, 2024; link in Appendix B, av-022.

### Case 2 (Construction): Two Layers of Sanding Silent at Once

ce-001. Talerddig, Wales, 21 October 2024. RAIB report (Report 08/2026, reviewed for this book): two passenger trains collided head-on on wet rail; 1 passenger died, 3 were seriously injured and 18 slightly injured (the driver of the other train was seriously injured, with 5 minor injuries). Braking on the long descending gradient depended on sanding for adhesion; the investigation found the automatic sanding system had most likely failed from an electrical fault, and the driver did not activate the manual emergency sander: the designed two-layer enhancement (automatic primary, manual backstop) went silent together on the same wet gradient, and the train overran by more than a thousand metres into an occupied single-line section.

Stop at the decision point: the stretch of descent in which the driver noticed the adhesion problem and decided to trust that the automatic sanding was still working. On the table: the automatic system's alarm-free state (no alarm being read as "working"), the activation steps for manual sanding, and the distance between the gradient and the signals. The redundancy illusion of the two sanding layers was not in the hardware — the hardware really was two sets — it was in the allocation of use: the automatic layer carried the everyday, the manual layer carried the imagination of "if the automatic fails," and the scenario "the automatic fails silently, without alarming" fell into the common blind spot of both. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Head-on collision. Primary source: RAIB, Report 08/2026, 2026; link in Appendix B, ce-001.

### Case 3 (Healthcare): The Purple Syringe and the Second Pair of Eyes

me-003. UK paediatrics, sedation before an elective renal biopsy. HSIB report (Inadvertent administration of an oral liquid medicine into a vein, 2019; archived snapshot reviewed for this book): oral midazolam was drawn into an intravenous syringe and injected into a vein. There were two defences: the purple syringe reserved for oral medicines (device-level separation — the colour makes oral and intravenous equipment physically non-interchangeable) and the two-person check before administration (process-level separation). In the event, both failed at once: the syringe was substituted, and the double check degraded into formality. The child suffered no significant harm; the national count cited in the report was 61 wrong-route administrations, and the report issued four safety recommendations (2019/028–031).

Stop at the decision point: the preparation room, before the double check began and the dose was given. On the table: the purple syringes out of stock or not to hand, two busy colleagues, and the two signature boxes on the check sheet. The common item of the two defences was "conditions normal": the purple syringe in place, the second person available — once that premise broke, both broke together. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Wrong-route administration; no harm caused. Primary source: HSIB, 2019; link in Appendix B, me-003 (archived link, grade A−).

### Case 4 (Chemical): A Backup Plan Sharing the Same Blackout

ch-003. The Arkema organic peroxide plant (Crosby, Texas), late August 2017. CSB report (reviewed for this book): flooding from Hurricane Harvey cut power and disabled the plant's refrigeration; the stored organic peroxides warmed up, the first trailers spontaneously combusted on 31 August, and the remaining trailers were deliberately ignited on 3 September as a controlled disposal. The emergency plan designated "transfer to refrigerated trailers after power loss" as the backstop — and the backstop sat under the same common cause as the primary system: the flood drowned the plant's refrigeration and also drowned the trailers' refrigeration and the roads between. The backup was independent on paper; in the flood's topology it shared one life with the primary system.

Stop at the decision point: the moment the emergency plan listed the refrigerated trailers as the failure backstop and won approval. On the table: the inventory of trailer refrigeration capacity, and the site's historical water-level assumption that it had never been flooded. The common-cause review asks exactly one question: will the cause of the primary system's failure act on you the same way? The flood answered no. 〔Stop point: reader judges first, then turns the page〕〔Outcome〕Chain of fires and explosions; evacuation of the surrounding area. Primary source: CSB, Arkema Inc. Chemical Plant Fire, 2018; link in Appendix B, ch-003.

## 4 What Shows Earliest

Six weak signals, each with the reason that usually overrides it.

1. The backup and the primary system share the same vendor, implementer, or operations team. Override: "better compatibility, faster response."
2. Every switchover drill is run in a night window at low load; never a real drill at business peak. Override: "the business cannot be risked."
3. The monitoring and alerting of both systems converge on one duty desk, one person handling. Override: "centralised monitoring is more efficient."
4. The backup's specification is adapted from the primary system's drawings. Override: "to guarantee consistency."
5. The emergency plan's backstop steps never list their shared failure conditions with the primary system. Override: "the plan is written scenario by scenario." (Arkema's flood was the variable common across scenarios.)
6. The full version of "we have two" has never been pressed: two of what, differing how, verified by whom. Override: "why interrogate it so closely."

## 5 How to Defend

Device one: a common-cause register. Every redundancy pair is required to register its common items: power supply, network, vendor, algorithm, site, personnel, assumptions — each item annotated "if this common cause fails, do both sets fail together." The register is updated yearly and cross-indexed with the dependency graph (Chapter 21). The review entry in the Arkema case comes from here: the backstop's register must carry one line — "failure conditions shared with the primary system."

Device two: a heterogeneity standard. Critical redundancy is forced heterogeneous on at least one dimension: different principle, different vendor, different team. Automatic and manual sanding, the syringe's colour and the double check, the map and the look-out — the failures all happened where things were homogeneous. Heterogeneity's procurement cost is real, and its consideration belongs on the purchase order: the extra money buys "the common cause is not shared."

Device three: real switchover. The verification standard for redundancy is written in hard: the switchover must be performed with the primary system off, under real load, at least once a year; redundancy that cannot be truly switched has its status renamed from "redundant" to "paper backup" and is excluded from the defence calculation. The substance of this downgrade is to return the defence arithmetic from multiplication to addition: the numbers look worse, but they are the true numbers.

Device four: same-cause review of backstops. Every backstop step in an emergency plan must answer one question: "will the cause of the primary system's failure act on you the same way?" The question costs one line; the benefit is stopping Arkema-class scenarios on paper.

## 6 Boundaries with Adjacent Mechanisms

Against hidden coupling (Chapter 21): coupling is a hidden line between independent systems (nobody knows they are connected); the illusion is common ancestry inside a redundancy pair (everybody knows they are connected, and treats it lightly). The hidden lines drawn by Chapter 21's mapping become this chapter's common-cause entries once they land in the redundancy register.

Against failure of success (Chapter 20): slack leaves backups unverified (nobody feels a drill is needed); the illusion leaves backups non-heterogeneous (independence was absent at procurement). Slack is a disease of time, the illusion a disease of structure; an organisation slack for long enough will watch its redundancy register drift toward common ancestry on its own.

Against compliant but unsafe (Chapter 32): compliance checks count the number of defences; this chapter counts the kinds. Domains where the regulator requires "redundancy in place" and acceptance looks only at existence are the illusion's high-incidence zone.

## 7 Self-Check: Five Questions

1. Write down three redundancies your organisation takes pride in; where is each one's list of common items? Without the list, put quotation marks around the word redundant.
2. When did your backup system last run independently of the primary system? And who verified the "independence"?
3. The most recent switchover drill — was the primary system really shut off? Was the business traffic real?
4. In your emergency plan, is the failure condition shared by the backstop and the primary step written down? Run one flood or one blackout through it.
5. Defences that "exist" on screens, in inventories, on drawings, but have never been verified in isolation — how many can you count right now?

## 6bis Installing the Devices: Order, Failure Modes, and Cost

The common-cause list goes first — it is the X-ray that develops every same-source item in one exposure. The heterogeneity standard follows (it writes the remedy direction for each list line), true switchover third (the stress test that prices whatever heterogeneity remains), and the same-cause review last (it faces new purchases and new designs, riding the procurement and architecture calendars). First ninety days: weeks one and two, sweep for common causes in three classes — same vendor, same drawings, same crew — asking of every system "what does my backup share with me," and register every answer; weeks three to six, write the heterogeneity standard (for the three riskiest lines: swap vendor, swap principle, or swap crew — or accept the common cause in writing, with a signature); month two, run one true switchover (main off, backup carrying real traffic, full log); month three, put the redundancy declaration into procurement and architecture templates — the "shared items" field lists every common item with evidence numbers, and an empty field is processed as no redundancy.

Failure modes. The list stops at depth one (same vendor checked; the vendor's own single fab, not; same crew checked; the crew's shared training manual, not) — use a three-layer follow-up template: can this shared item be decomposed further, which layer is the real failure source, does the source itself have a backup. The standard stays on paper (plans written, budgets declined, list lines reclining) — give heterogeneity items deadlines and owners in the ledger, joining Chapter 11's three states as remediation-by-deadline. Switchover windows get cosmetically chosen (quietest day, pre-scaled capacity, the gentlest fault script) — production-aligned conditions, unedited results, Chapter 20's live-testing rule. Declarations get three words ("duly considered") — granularity required: item-by-item shared-item listings with evidence numbers, or the declaration is void.

Cost: the sweep is one to two weeks by system count; heterogeneity ranges from a procurement change to a second crew — the list's real function is making that bill visible, so that accepting or fixing a common cause both become signed decisions instead of ambient facts. A true switchover costs half a day to a day. Against dual hydraulic loss on a 747 freighter, a braking failure on wet rail, or a cannula assumed compatible — phantom redundancy prices at the worst moment; the list and the switchover move the worst moment onto the exercise ground.

Toolchain: the locator triggers on "redundancy mid-or-low plus same-source backups"; the three-class sweep is the opening move. Question set 22's item 3 ("would you dare switch the main system off") is the cheapest possible audit of the switchover device. Post-mortems with "backup failed simultaneously" in the chain feed the common-cause list. And in pre-mortems, common-cause deaths convert to switchover tests: the pre-mortem suspects the redundancy; the switchover pays for the suspicion's answer.

## Quick-Reference Card

**The mechanism in one sentence:** the illusion of redundancy means multiple defences that coexist on paper are in fact one line: they share the same power supply, the same vendor, the same drawings, the same crew, or the same assumption

**The three criteria, compressed:** 

**The devices (Section 5 has the detail):** Device one: a common-cause register; Device two: a heterogeneity standard; Device three: real switchover; Device four: same-cause review of backstops.

**The four loudest weak signals (Section 4):** The backup and the primary system share the same vendor, implementer, or operations team. Override: "better…; Every switchover drill is run in a night window at low load; never a real drill at business peak. Override…; The monitoring and alerting of both systems converge on one duty desk, one person handling. Override…; The backup's specification is adapted from the primary system's drawings. Override: "to guarantee….

**Cost register and case index:** av-022: 直升机1人轻伤；飞机7人未受伤; ce-001: 1名乘客死亡；4人重伤、23人轻伤; ch-003: 无公开量化; me-003: 患儿无明显不良影响；全国61例错误途径给药.

**Domain cross-reference:** this chapter's cases live on the Aviation, Construction, Chemical, Healthcare domain pages; Section 12 of each domain page maps the same mechanism into local industry dialect — worth a glance at each after finishing this chapter.

**One-line takeaway:** Count the shared items on paper defenses: when the common cause arrives, all copies void at once.

**Verification cadence after installation:** criteria walkthrough, five minutes monthly; weak-signal list, half an hour quarterly; spot-check of Section 5 devices, twice a year. Every post-mortem and pre-mortem item hitting this mechanism flows back into the ledger (the ledger-ID field of Ch. 38) — the ledger is the only proof your devices are alive.

**Pre-mortem hint:** Any death phrased as "the backup went down at the same moment" belongs here; the check action is counting the shared items.

**The two fastest self-checks:** first, run your own situation through the three criteria in Section 1 (five minutes; a hit gets marked); second, find one live instance — or plainly state the absence of one — for each of the four signals above (half an hour; a clean sheet is good news, and gets filed).

**Next stops:** adjacent mechanisms: see Section 6 (read the boundary discussion in Section 6 first). Question set 22 of Chapter 37 is this chapter's acceptance checklist; after a pre-mortem sorts deaths into chapters, come back to Section 5 to fit the countermeasures; when a post-mortem hits this mechanism, its improvement actions land on Section 5 devices.

(First draft: 3,899 Chinese characters; English edition independently written.)
