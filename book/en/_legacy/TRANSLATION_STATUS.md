# English Edition — Translation Status

## Approach

Not a word-for-word translation. The English edition is independently written per the book's own bilingual spec (Writing Standards §5): the fact layer (numbers, dates, institution names, document titles) is language-neutral; the narrative layer is written fresh in English, not translated from Chinese. Chinese source text is consulted for accuracy; English prose is written for readability.

## Status

| Component | Chinese | English | Notes |
|---|---|---|---|
| README | ✅ | ✅ | |
| Preface (读者契约) | ✅ | ✅ | |
| Glossary (术语表) | ✅ | Mechanism names translated; institution/equipment translations embedded in chapter texts | |
| Part 1: Meta-Question (Ch. 1–4) | ✅ | ✅ | |
| Part 2: Anatomy (Ch. 5–10) | ✅ | ✅ | |
| Part 3: Mechanisms (Ch. 11–34) | ✅ | ✅ | All 24 chapters |
| Part 4: Domain Profiles (14) | ✅ | ✅ | |
| Part 5: Usage (Ch. 35–39) | ✅ | ✅ | |
| Part 6: Boundaries (Ch. 40–42) | ✅ | ✅ | |
| Appendix A: Mechanism × Domain Matrix | ✅ | ✅ | Regenerated from source TSVs (138/336 cells filled); English headers and reading notes |
| Appendix B: Case Table | ✅ | ✅ | English column headers; case titles kept in original language per spec | |
| Appendix C: Retrieval Handbook | ✅ | ✅ | |
| Appendix D: Evidence Grading | ✅ | ✅ | |
| Appendix E: Mechanism Genealogy | ✅ | ✅ | |
| Fact layer (`facts/`, 158 YAML) | ✅ | ✅ | Language-neutral per bilingual spec; canonical headlines kept in Chinese; `referenced_in_en` auto-indexed |
| Mechanism chapters sync (Ch. 11–34) | ✅ | ✅ | Each chapter now carries Section 6bis (device installation order, failure modes, cost, toolchain) and a Quick-Reference Card, synced with the Chinese 2026-11-01 expansion |

## Bilingual Conventions

- Case IDs (`av-001`, `fi-013`, etc.) are identical in both editions.
- Mechanism names use the bilingual glossary: Chinese full name + English name on first occurrence, Chinese abbreviation thereafter (Chinese edition); English full name thereafter (English edition).
- Institution names: Chinese full name + abbreviation on first occurrence (Chinese edition); English abbreviation throughout (English edition).
- Document titles in citations remain in their original language in both editions, with translation in parentheses where helpful.
- Numbers, dates, and case card structured fields are language-neutral.

## Remaining Work Estimate

- ALL COMPLETE

## 2026-11-01 Sync Notes

- Rogers Commission report (Challenger) citations upgraded in both editions from 〔卡点/Verification pending〕 to verified references: Vol. 1 Ch. 3 (launch time, 73 seconds), Ch. 5 (the caucus and the "management hat" exchange, the 53-degree recommendation), Ch. 6 (erosion history, the "not desirable but acceptable" filing) — official text at nasa.gov/history/rogersrep/, read and verified 2026-11-01.
- English Appendix A regenerated from the source TSVs; blanks are sampling gaps, not claims of absence.
- Domain pages now carry Section 8 (mechanism variations in this domain) and Section 9 (cross-reading), written fresh in English per the bilingual spec.
- Usage (Ch. 35–39) and boundary (Ch. 40–42) chapters brought to full parity (2026-11-01): each now carries the complete 2026 Chinese expansion — evidence checklists, worked examples, calibration and fingerprints, rollout timetables, meeting protocols, forensics, field manuals, reader routes, FAQ, and closings — written fresh in English per the bilingual spec. Word counts: 35: 4,633; 36: 4,102; 37: 5,848; 38: 5,813; 39: 4,940; 40: 4,405; 41: 3,996; 42: 5,148.

- Full-parity alignment of the English edition complete: every part (meta, anatomy, 24 mechanisms with 6bis + Quick-Reference Cards, 14 domain pages with Sections 8–9, usage, boundaries, appendices, fact layer) now carries the structure and substance of the Chinese 550,215-character edition, independently written.
