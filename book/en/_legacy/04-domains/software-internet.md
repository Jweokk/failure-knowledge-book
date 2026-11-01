# Software and Internet Services | sw

> This page has five sections: record quality, feedback delay, coupling, the three deadliest mechanisms, and what outsiders most easily mislearn.

## 1 Record Quality

The world's only voluntary public-postmortem ecosystem (the exception of Chapter 4). Vendor postmortems (the postmortems and monthly availability reports of Cloudflare, GitHub, and others) provide timelines and decision narratives — grade-D material, but of remarkable depth; regulatory penalty documents (CNIL, FTC, ICO) cover the data-compliance side, grade C. This book's 9 sw cases consist of vendor postmortems (6) and regulatory penalties (3). The gap: security incidents (intrusions, breaches) are almost never publicly postmortemed — the postmortem text is itself an attack manual, and legal liability is uncapped — and the public postmortem corpus has been contracting in recent years (Section 4.2). Retrieval channels in Appendix C.4 (when blog-site scraping times out, switch to curl).

## 2 Feedback Delay

The shortest of any industry: feedback on changes arrives in seconds and minutes (staged rollouts expose faults on a percentage of traffic first), feedback on faults in minutes (monitoring and alerting), feedback on postmortems in weeks. This is the material basis of software's postmortem culture: feedback fast enough to sustain a high-frequency learning loop. The distinction inside the industry runs between the data plane and the control plane: data-plane faults feed back fast; control-plane faults (dashboards, permissions, configuration) feed back just as fast but are easier to underestimate (sw-004's retry storm happened on the control plane).

## 3 Coupling

Infrastructure-grade and global: one vendor's edge network carries distribution and security for a large share of the world's traffic (the three global events of sw-001 through sw-003), and a shared foundation turns a single point of semantic ambiguity into synchronized failure across thousands of customers at once. Automated coupling: changes propagate automatically (sw-002's signature file spreading with a deployment), and clients' automatic retries amplify faults (sw-004). Means of isolation genuinely exist (regionalization, staged rollout, rollback), but common-mode failures — the same configuration system, the same permission regime, the same cleanup job — punch through them again and again. Software's conclusion on coupling is the same as aviation's: high coupling has been tamed by engineering, and the taming is a continuous process that must be paid for.

## 4 The Three Deadliest Mechanisms

Hidden coupling (Chapter 21): a database permission change doubling the signature file (sw-002); the retry storm (sw-004); the empty-parameter semantics of a BYOIP cleanup (sw-003). Nonlinear scaling across thresholds (Chapter 24): record-breaking load punching through capacity calibrated to historical peaks (sw-005); bulk abuse of a registration system (the mirror image of fi-004). Cascading failure (Chapter 33): downstream services failing in sync through shared automation. Next most frequent: misaligned incentives (the structural conflict of data compliance in sw-007 and sw-008); practical drift (operations diverging from the documents).

## 5 What Outsiders Most Easily Mislearn

Mislearning one: taking postmortem culture as proof that the industry is safe. Postmortem articles cover availability failures of the "fell ill and was cured" kind; they do not cover security incidents or commercial failures (the boundary of Chapter 4). Mislearning two: importing the word "blameless" without the machinery that makes it true. A blameless review without an anonymization process and insulation from appraisal is blameless rhetoric (the gap between name and substance in Section 4.2). Mislearning three: treating "fast rollback" as a universal remedy. Software can roll back because deployments are atomic and state can be versioned; writing rollback into a non-software contingency plan without asking "can our state be versioned?" is the most common error of cross-industry transplantation (the four-condition criteria of Chapter 4).

## 8 Mechanism Variations in This Domain

Hidden coupling carries a signature: the actor of the change never touched the dependency it triggered. The permission change that oversized a feature file; the cleanup defect that withdrew 1,100 prefixes — both landed on dependencies (permissions, routing, maintenance tasks) that no dependency graph covered. The local metric is change-touch accuracy: declared impact versus actual impact per change. And software coupling grows by itself — libraries and config merges breed dependencies between deploys — so human lists decay faster here than anywhere; automatic generation is not an optimization, it is the floor.

Nonlinear scaling runs on two clocks. Load feedback arrives in seconds — the fastest in the book — while capacity verification runs in quarters: the mismatch is the structure. The local check is the share of components a real production-scale load has ever touched; the record-load case broke precisely on the component outside that coverage. The retry storm adds a software-specific twist for Chapter 22: defenses (retries) become amplifiers under abnormal conditions — every automatic retry needs a breaker and jitter, which is this domain's standing correction to the redundancy concept.

Regulatory lag is measured in platform generations: the compliance asymmetry (data use pays immediately; enforcement arrives discounted by detection probability) is the local texture behind three CNIL actions. Read the three cases as one dataset: consent mechanics, app data flows, credential hygiene — the rulebook updating at legislative speed against products updating at deployment speed.

## 9 Cross-Reading

Pair with Public Policy: the dashboard that grades its own projects and the dashboard that started the retry storm are one irony in two dialects — the metric layer becoming a new failure surface. Pair with Finance: both volumes' enforcement cases share the long-behavior, short-discovery time structure. Pair with Manufacturing: change review against the change-order discipline — a maturity comparison that flatters neither.

