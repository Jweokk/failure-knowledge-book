# The Knowledge of Failure

**A Cross-Domain Manual of Structural Failure**

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Chinese + English](https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87%20%2B%20English-7c6cff.svg)](#)
[![Edition](https://img.shields.io/badge/edition-v1.0-f59e0b.svg)](CHANGELOG.md)

[中文说明](./README.zh.md) · [Read online](https://tkf.fly2ai.top/) · [中文版](https://tkf.fly2ai.top/)

24 mechanisms · 14 domains · 159 cases · 53 full case cards · Chinese + English

---

## What this is

Most books about failure collect stories and draw morals. This one treats failure as a class of knowledge: a finite set of mechanisms that recur across domains, each with a way it grows, an earliest point where it becomes visible, and conditions under which it holds.

Every mechanism chapter takes four to six cases from different fields — aviation, chemical processing, construction, software, medicine, nuclear power, public procurement, shipping. The point is not that the cases resemble each other. The point is that the same structural parameters recur: coupling, redundancy, what the incentive rewards, time remaining, regulatory intensity, scale.

Case cards are written only from what the people inside could see at the time. Nothing from the outcome enters the left-hand column, no inner motives are invented, and each escalation point lands on a specific date, meeting or signature. Every card stops at the decision. You judge before you turn the page.

## What's inside

| Part | Chapters | Line |
|---|---|---|
| Meta | 1–4 | Why failure knowledge is expensive, three ways records distort, five fields that record failure seriously, why the method did not spread |
| Anatomy | 5–10 | The anatomy of a failure, what was visible then, the shape of a case, evidence grades, how to read a case |
| Mechanisms | 11–34 | Twenty-four mechanisms, from normalization of deviance to crossing a scale threshold |
| Domains | 1–14 | Aviation, chemical processing, construction, software, medicine, nuclear, rail, maritime, mining, finance, public projects, product, food and agriculture, energy |
| Usage | 35–39 | Lookup, use, practice, share, and the ninety-minute rehearsal |
| Boundaries | 40–42 | What this method cannot do, contested cases, and the limits of the mechanism list |
| Appendices | A–D | Mechanism × domain matrix, case index, evidence grades, genealogy of mechanisms |

Every mechanism chapter ends with five self-check questions rather than a summary. Appendix A is a 24 × 14 matrix with 138 cells; appendix B indexes all 159 cases by number, domain, and chapter.

## Build

Requires Python 3.11+, `mkdocs-material` for the site, `weasyprint` for the PDFs, and Noto Serif / Noto Serif SC fonts.

```bash
python3 book/_spec/build_pdf.py          # Chinese PDF  -> dist/失败的知识.pdf
python3 book/_spec/build_pdf_en.py       # English PDF  -> dist/failure-knowledge.pdf
python3 site/build_site.py               # assembly + mkdocs.yml
mkdocs build -f site/mkdocs.yml          # Chinese site -> site/build
python3 site/build_site_en.py
mkdocs build -f site/mkdocs-en.yml       # English site -> site/build-en
rm -rf site/build/en && cp -r site/build-en site/build/en
```

## Layout

```
book/            Chinese manuscript (Markdown, one file per chapter)
book/en/         English manuscript, written separately, not translated
book/_spec/      PDF pipeline: build_pdf.py, build_pdf_en.py, CSS
site/            site assembly, navigation, theme overrides, counter script
dist/            build output (PDF, not tracked)
```

## Errata and method

`book/勘误.md` records every correction made during review, with the source each correction was checked against. `book/交付说明.md` records what changed from the delivered draft and why. The method itself is in appendix C, and no number in this book is stated without a source that can be opened.

## License

Text and figures: CC BY-NC-SA 4.0. Scripts: MIT. See [LICENSE](./LICENSE).
