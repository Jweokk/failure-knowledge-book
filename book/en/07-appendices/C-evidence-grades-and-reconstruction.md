# Appendix C: Evidence Grades and the Reconstruction Method

> This appendix is the operating manual for the grade system of Chapter 10: the five definitions with their tests, how to read the matrix, the labelling convention for reconstruction, how links are archived, and the working sheet for the four-part number record.

## C.1 Five grades, definitions and tests

| Grade | Definition | Test | What it can support in the body |
|---|---|---|---|
| A | Full text of an independent investigating body's report | The body is independent of the party investigated and of the penalty function; the full text, not a summary, is public; it carries a factual part and an analytical part, or an equivalent structure. A process report, such as the JTSB's 経過報告, is graded A− | The decision sequence, the options ruled out, the minimum counterfactual, the escalation point |
| B | Official bulletins, communiqués, regulatory announcements | Officially signed, one party's statement, no evidentiary section | The magnitude of the consequence, conclusive findings. Entry into the body requires the "reconstructed" label |
| C | Judgments, penalty decisions, arbitration documents | The facts have been through adversarial testing, but the selection of facts serves the issue in dispute | Amounts, responsible parties, the timeline of acts. Technical process outside the dispute is labelled "reconstructed" |
| D | The party's own public postmortem | Published voluntarily by a company or an individual; a postmortem carrying a timeline is the strong form, an announcement the weak one | The shape of internal organizational process. Supports a finding of fact only after cross-verification against A, B or C |
| E | Media reporting | Any retold text | Lead generation only. Never a source of fact for the body |

The rules for movement between grades: a core fact corroborated by B and C together can support a body case labelled "reconstructed"; an A− case does not support the escalation point, which turns on detail at the level of the signatory; a case whose links have died and which has no archive is downgraded to pending verification; quoted text that does not match its original is removed. the link check and the number-to-source check carry this out.

## C.2 Reading the matrix

The mechanism × domain matrix in Appendix A takes three readings.

Start with the blanks, which carry two meanings. A blank marked "to collect" means the cell has not been searched yet. A blank marked "no record" means it has been searched and no qualifying primary material was found. The two are entirely different: the first is a gap in this book, the second may be a structural silence in the domain, which is Chapter 2's evidence of recording skew.

Row density comes second. A row, meaning one mechanism, with strong cases in several domains says the mechanism holds across industries. A row with cases in only one domain is first suspected of thin collection coverage, and only after that of the mechanism being industry-specific.

Column density comes last. A column, meaning one domain, with many cases usually reflects a strong recording institution (aviation, chemical processing) rather than a high accident rate. A column that is nearly blank calls first for a check on whether that domain's primary library is reachable (Chapter 3's device checklist), and only then for a conclusion.

## C.3 Labelling a reconstruction

Cases on medium evidence, mostly grades B, C and D, are still worth writing, on one condition: the inference is labelled explicitly. The convention: a factual sentence in the body states the fact and cites the source in parentheses; an inference opens with "Reconstructed:" and closes with its basis in parentheses. An example:

"Minutes of the 14 March review meeting show the risk listed as agenda item 7 (factual sentence; grade C: meeting minutes). Reconstructed: from the agenda order and the meeting's total length, the item got less than 5 minutes and no resolution entry was formed (inference; basis: the time allocation on page 2 of the minutes)."

Three disciplines. An inference must be re-checkable by the reader along the basis it cites. An inference with no re-check path is not written. Inference may not prop up inference, since two "reconstructed" sentences still add up to one inference.

## C.4 Links, archives and the soft 404

Every case's primary link has to be opened by hand and read to its content: WebFetch returning body text, or curl returning HTTP 200 with a file type, a page count and a subject that match. Two common traps need testing separately. The soft 404 is an HTTP 200 that returns an error page or a placeholder, and the test is any one of three: an abnormally small file, text containing "404/Forbidden/Not Found", or a subject that does not match expectation. The anti-scraping placeholder is a status 200 whose content is a CAPTCHA or a login wall.

When the original link is dead, an Internet Archive (web.archive.org) snapshot is allowed on three conditions: the body notes "original link dead, archive link"; the snapshot date is later than the publication of the cited content; the grade drops half a step from the original's (A to A−, B to B−).

## C.5 Working sheet for the four-part number record

Every number in the body gets its four parts registered at the material end. The template:

```
Number:
Issuing body:
Document and number:
Date of publication:
Sample and definition:
Link:
Chapter and section where used:
```

When a part is missing, go back to the source and fill it first. Where it cannot be filled, delete the number and rewrite the mechanism narration. The difference audit takes this sheet as its authority: the set of numbers in the body is a subset of the set of numbers in the material cards, and a non-empty difference sends the chapter back.

Three notes on use. The grade evaluates the form of the material, not its truth: a speculative passage inside an A-grade report is still speculation and is cited as speculation, and a dated, specific fact inside an E-grade report may be accepted, though any key number must be traced back to a higher grade. The rules of downgrade and upgrade are not symmetric: retelling does not upgrade, since a conclusion taken from second-hand material is graded as second-hand, while a new investigation can upgrade, since a fact confirmed by an independent investigation is graded by the new material. The table also serves as the template for a reader's own case library: internal postmortem material grades the same way (system logs A, meeting minutes B, participants' oral accounts D), so an organization's library and this book's library can cite each other directly.
