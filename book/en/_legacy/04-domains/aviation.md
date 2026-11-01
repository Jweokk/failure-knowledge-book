# Aviation | av

> This page has five sections: record quality, feedback delay, coupling, the three deadliest mechanisms, and what outsiders most easily mislearn. Case IDs point to Appendix B.

## 1 Record Quality

Aviation has the most complete failure-recording system of any domain in the world (all four devices of Chapter 3 are present). The entry points and the degree of verifiability for primary materials are as follows (operational retrieval details in Appendix C).

United States, NTSB: every accident carries a coded identifier (e.g., DCA21FA085); formal reports (the AAR/AIR/AAB series) are published as full-text PDFs; the CAROL database query system covers all accident and incident records. Note from hands-on testing: the HTML pages of the NTSB website have anti-scraping restrictions, but direct PDF links and the data interfaces are reachable, which determines the correct path for automated collection — locate the case number in the database, download the PDF via the direct link.

United Kingdom, AAIB: formal reports (AAR numbers) and general investigation reports are published in full on the gov.uk platform, in both HTML and PDF, with no retrieval barriers; the list pages cover all public reports in reverse chronological order.

Japan, JTSB: a dual track of final reports and "keika hōkoku" (progress reports), full-text PDFs in Japanese, hosted under the Ministry of Land, Infrastructure, Transport and Tourism domain (the www.jtsb.go.jp domain does not resolve; the correct entry is the mlit.go.jp path). The progress-report system deserves note: for major accidents, progress reports are issued in installments before the final report appears, and the Haneda collision (av-037) was still at the progress-report stage nearly two years after the event.

France's BEA, Germany's BFU, Italy's ANSV, Spain's AESA: full-text PDFs in French, German, Italian, and Spanish; depth is sufficient, and language is the practical barrier.

Civil Aviation Administration of China: publishes investigation reports and progress bulletins under the ICAO Annex 13 framework (e.g., the MU5735 progress bulletins, av-038); an official channel is usable, and full-text depth varies with the case's tier.

Overall assessment of record quality: the world's highest density of grade-A material, with non-English material matching English in depth. Near misses below the reporting threshold are compensated by voluntary reporting systems (e.g., NASA's ASRS), but the skew of voluntary samples must be handled per Chapter 2.

## 2 Feedback Delay

Aviation's feedback delay shows two extremes.

For design and management decisions, the delay is measured in years. The consequences of extending maintenance intervals, issuing airworthiness directives, or revising training syllabi take years, or hundreds of thousands of flight hours, to appear. Alaska Airlines 261's lubrication-interval extension (av-034) ran from approval to consequence on a scale of years; the 737-9 door plug (av-030) took about eight months from the final-assembly work to the event, but from the standpoint of the design-certification system the delay is measured in decades. This means decision makers at aviation's organizational and incentive layers face the consequences of their own decisions almost always outside their own tenure (the typical soil of Chapter 28's horizon mismatch).

For crew operational decisions, the delay is measured in seconds. The effects of a takeoff, an approach, a go-around cash in immediately. Because delay at this layer is so short, the evidence chain for crew-level error is the most complete and the most reproducible; NTSB's brief final reports (about five pages) can nearly always lay out the whole operational chain.

The middle band between the two layers: feedback at the maintenance front line is measured in weeks; feedback to the company safety management system (SMS) in quarters. Readers borrowing aviation's experience should note which band they occupy: borrow "interval management" and the validation plan runs on a horizon of years; borrow "checklists" and it runs on a horizon of weeks.

## 3 Coupling

Within a single aircraft, coupling is suppressed by design to very low levels: redundant systems, fail-safe design, and segregation requirements are the result of seventy years of institutional investment. Hidden coupling in Perrow's sense is controlled at the individual aircraft level.

Cross-aircraft coupling is aviation's real risk surface, and it takes the form of common-cause failure. Three diffusion paths: the same fleet (the global grounding of the 787 fleet after the battery events, av-002; the fleet-wide grounding for inspection of all 737-9s after the door-plug event, av-030); the same maintenance and management system (Alaska 261's interval extension applied across the entire fleet, av-034); the same training and operational culture (Asiana 214's automation dependence carried the common features of an airline's and a region's training culture, av-031). Isolation instruments exist and are used institutionally — grounding orders, airworthiness directives, survey-style fleet inspections — and diffusion is usually cut off within days.

What this means for other industries: aviation's conclusion on coupling is not "low" but "high coupling, institutionally tamed." Taming costs what the devices of Chapter 3 cost. An industry whose coupling appears low without a corresponding institutional investment is probably coupling it has not seen (Chapter 21).

## 4 The Three Deadliest Mechanisms

First: practical drift (Chapter 15). Aviation has the world's densest procedures, and the fork between the formal process and actual practice is therefore the most worth studying. Samples: an air ambulance helicopter's crew looking down in flight to consult the record book (av-020, the behavior chain complete); exiting an R22 with the engine running becoming routine (av-010, the manufacturer's safety notice had long stated the risk explicitly); a 737's takeoff performance computed for the full runway while the takeoff ran from an intersection, with nobody intercepting it (av-028). Aviation supplies every generating condition for practical drift: rules written by people who do not fly, heavy workloads, and violations that almost never carry consequences.

Second: margin erosion (Chapter 25). Samples: approved extensions of the horizontal-stabilizer lubrication and inspection intervals (av-034 — the margin cut had a document, an approver, and delivered itself flight by flight); a 747 freighter's cargo door left unsealed in the rain, letting water in (av-026 — no recheck requirement for the fairing and seals). Aviation has a ledger tradition for margins, but the ledger is held by the operator, and regulatory approval is the legal channel for the cut.

Third: automation and skill degradation (Chapter 26). Samples: the autothrottle inadvertently shut off during Asiana 214's visual approach (av-031); a helicopter cleared to a helipad that landed on a runway instead (av-017, no reconfirmation before final approach). The combination of automation dependence and compressed training hours is aviation's most repeatedly validated failure path, and the industry's own countermeasures — manual-flying quotas and scenario-based simulator training — are worth copying as a complete set by anyone looking to borrow them.

## 5 What Outsiders Most Easily Mislearn

Mislearning one: treating the checklist as culture. Aviation checklists work because three supports are in place: the person signing has the authority to stop the line; findings are recorded, and the records are not used for blame; and missed checks are caught by data systems (FDM, flight data monitoring). Without those three supports, the checklist degenerates into a signature campaign (Chapter 32, compliance without safety). Transplanting the form without the system is the most common cross-industry mis-transplant.

Mislearning two: treating a case's lesson as the mechanism. The safety recommendations at the end of every report address specific conditions; lifting one directly (say, "improve communication") is taking the prescription without seeing the patient. The correct use is the case card's mechanism field: classify first (which chapter it hangs on), then read that chapter's Section 5 for the countermeasures.

Mislearning three: mistaking aviation's transparency for the industry norm. Aviation's ability to publish full reports is an institution paid for by disaster (Chapter 4). Using "if aviation can publish, why can't we" in an internal debate points the right way, but do not overestimate how easy the publishing is: behind every page of a public report stands statutory investigative power.

(First draft: 2,325 Chinese characters; English edition: about 1,300 words)

## 8 Mechanism Variations in This Domain

This domain hosts more verified cases than any other, and the thick report corpus lets the mechanisms be read at a fineness no other page matches. Three variations worth carrying. Normalization here is interval-shaped: the jackscrew case (av-034) shows relaxation as an approved document — the deviation written into the interval itself — so the local check reads approval chains, not workshop floors: who requested the extension, whose inspection records supported it. Hidden coupling here is battery- and map-shaped (the 787 emergencies, the风筝-line strike on a pitot): certification assumed separation that the physical world declined, and the instrument is the certification-assumption log versus incident history. Practical drift is inspection-shaped: the fan-blade low-amplitude signal filed as noise (av-006) closed an anomaly without a state, exactly the fourth-state filing that Chapter 11's ledger forbids — in aviation the ledger exists, which is what makes the closed-without-state entry legible as a defect rather than a mystery.

The domain's standing lesson is institutional: NTSB-grade investigation, mandatory reporting, and tracked recommendations compressed accident rates by orders of magnitude inside two generations (Chapter 3's five-witness domains). The hardware did not change; the record-keeping did. Any other domain importing this page's devices is importing institutional density, and the density is purchasable.

## 9 Cross-Reading

Pair with Nuclear (reporting institutions and the independent-verification habit), with Military (release and airworthiness share a dialect; the foam-strike file is the interval-extension case at program scale), and with Maritime (general aviation and small-boat fishing are the two regulatory-density lowlands in this book — the paired cases show what thin oversight costs per flight hour and per fishing hour).

