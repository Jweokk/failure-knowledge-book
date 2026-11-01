# Appendix D: Evidence Grading and Reconstruction Methods

> Operational manual for the evidence-grading system described in Chapter 10: five-grade definitions, matrix interpretation, reconstruction annotation, link archiving, and the four-part number provenance template.

## D.1 Five-Grade Definitions

| Grade | Definition | Criteria | Supports |
|---|---|---|---|
| A | Full text of independent investigation agency report | Agency independent of investigated party and penalty function; full text (not summary) public; contains fact and analysis sections. Process reports (e.g., JTSB interim reports) graded A−. | Decision sequences, excluded options, minimal counterfactuals, escalation points |
| B | Official bulletins, regulator notices | Officially signed, unilateral statement, no evidence annex | Consequence magnitude, conclusive findings; main-text use requires "reconstructed" tag |
| C | Court judgments, penalty decisions, arbitration rulings | Facts tested through adversarial process, but fact selection serves the legal dispute | Amounts, responsible parties, behavioural timelines; technical process outside the dispute tagged "reconstructed" |
| D | First-party public postmortems | Voluntarily published by organisation/individual; postmortems with timelines are the strong form, announcements the weak form | Internal process shape; requires cross-validation with A/B/C before supporting factual claims |
| E | Media reporting | All retyped text | Lead generation only; prohibited as sole source for main-text cases |

Upgrade/downgrade rules: Core facts confirmed by B＋C cross-validation can support "reconstructed" main-text cases; single-source B cannot. A− cases do not support escalation points (signatory-level detail). Links dead with no archive: downgrade to pending; quoted text mismatching original: remove entirely (Gate 1 soft-404 check and Gate 2 number-source audit enforce this).

## D.2 Reading the Matrix

Three rules for interpreting the mechanism × domain matrix in Appendix A.

Rule one: two kinds of blank. Cells marked "to be collected" mean that cell has not yet been searched; cells marked "no record" mean searched with no qualifying primary source found. The meanings are opposite: the former is this book's gap, the latter may be the domain's structural silence (evidence for the recording bias of Chapter 2).

Rule two: row density. A row (one mechanism) with strong cases across multiple domains indicates cross-industry robustness; a row with cases in only one domain warrants first suspecting collection coverage gaps before accepting industry specificity.

Rule three: column density. A column (one domain) with many cases usually reflects strong recording institutions (aviation, chemical), not accident frequency; a near-empty column warrants checking whether that domain's primary sources are accessible (Chapter 3's four-device checklist) before drawing conclusions.

## D.3 Reconstruction Annotation

Medium-evidence cases (primarily B, C, D grade) remain worth writing, provided inference is explicitly tagged. Format: factual sentences state directly with source in parentheses; inference sentences begin with "Reconstruction:" and cite their basis. Example:

"The 14 March review meeting minutes show this risk listed as item 7 (factual sentence; Grade C: meeting minutes). Reconstruction: based on agenda order and total meeting duration, discussion of this item likely took less than five minutes and produced no resolution entry (inference; basis: page 2 time allocation)."

Three rules: every inference must be re-checkable by the reader along the cited trail; inference without a checkable trail is not written; inferences do not support each other (two "reconstructions" added together are still one inference).

## D.4 Links, Archives, and Soft 404s

Every case's primary link must be personally opened and content read (WebFetch returning body text, or curl producing HTTP 200 with file type, page count, and topic matching expectations). Two common traps require separate detection: soft 404s (HTTP 200 but returning an error page or placeholder — detected by abnormally small file size, presence of "404/Forbidden/Not Found" text, or topic mismatch) and anti-scraping placeholders (status code 200 but content is a CAPTCHA or login wall).

When original links die, Internet Archive (web.archive.org) links are permitted under three conditions: the text notes "original dead, archived link"; the archive snapshot postdates the cited content's publication; and the grade is halved (A→A−, B→B−).

## D.5 Number Provenance Template

Every number in the main text is registered at the source-card level with this template:

```
Number:
Source institution:
Document and reference number:
Publication date:
Sample and scope:
Link:
Used in which chapter/section:
```

If any of the four provenance elements is missing: first attempt to source it; failing that, remove the number and substitute mechanism narrative. Gate 2's difference audit runs against these cards: the set of numbers in the main text must be a subset of the numbers in the source cards; a non-empty difference set triggers chapter rejection.
