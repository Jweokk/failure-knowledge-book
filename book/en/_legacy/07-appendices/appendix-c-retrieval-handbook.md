# Appendix C: Primary Source Retrieval Handbook

> All entries tested-first: channels marked 〔Tested〕 were personally opened during this book's writing; channels marked 〔To verify〕 are known entry points not yet tested. WebSearch tools being unavailable, all collection relied on portal navigation — this handbook is written for that scenario.

## C.0 General Techniques (read these five first)

1. PDF direct links bypass HTML anti-scraping. NTSB and similar sites block web scraping of HTML pages, but report PDF direct links are accessible. Correct path: find the report number from a database or listing page, then construct the PDF direct link (numbers from pages, not guessed).
2. Listing-page scraping. gov.uk listing pages can be scraped wholesale; use the prompt "list the first N items with titles and links," then enter each item.
3. PDF text extraction. After downloading a PDF, extract text (e.g., PyMuPDF) from the first few pages: title page, casualty table, conclusions. HTTP status codes alone do not count as verification.
4. Soft-404 detection. HTTP 200 but abnormally small file size, text containing "404/Forbidden/Not Found," or topic mismatch — treat as failure.
5. Rate limits and timeouts. Government sites are concurrency-sensitive (SEC times out above 2 concurrent); blog sites that time out on fetch can be retried with curl plus a standard browser User-Agent.

## C.1 Aviation (av) 〔All tested〕

- NTSB (US): database at carol.ntsb.gov; report PDFs at `www.ntsb.gov/investigations/AccidentReports/Reports/XXXXX.pdf`; recent brief reports via `data.ntsb.gov/carol-repgen/api/Aviation/ReportMain/GenerateNewestReport/<docid>/pdf`. Warning: the agency's HTML pages (.aspx) time out — don't waste time fetching them.
- AAIB (UK): `www.gov.uk/aaib-reports` listing page covers all published reports in reverse chronological order; HTML report pages and PDF dual-track.
- MAIB (UK maritime, see C.3) same platform.
- JTSB (Japan): correct entry is `www.mlit.go.jp/jtsb/` (note: `www.jtsb.go.jp` does not resolve); report PDFs under `jtsb.mlit.go.jp/aircraft/rep-acci/` and `rep-inci/`.
- BEA (France): report PDFs under `bea.aero/fileadmin/user_upload/`; older cases (AF447, Concorde) have no direct links on the new site — navigate via investigation topic pages 〔To verify〕.
- BFU (Germany): reports at `bfu-web.de/DE/Publikationen/Untersuchungsberichte/` with `?__blob=publicationFile` parameter.
- ANSV (Italy): report PDFs under `ansv.it/wp-content/uploads/YYYY/MM/`.
- CIAIAC/AESA (Spain): `seguridadaerea.gob.es/sites/default/files/`; site search has poor coverage of pre-2000 cases.
- CAAC (China): caac.gov.cn disclosure section carries investigation reports and progress bulletins (e.g., MU5735 progress bulletin).
- Unavailable: Taiwan TTSB and aviation-safety.net unreachable from this collection environment (connection timeout); use archive alternatives per Appendix D.4 if necessary.

## C.2 Chemical and Process Industries (ch) 〔Tested〕

- CSB (US): case pages at `csb.gov/<event-name>/`; report PDFs at `csb.gov/file.aspx?DocumentId=<number>` (number from case page). Warning: file.aspx returns application/pdf which some tools cannot handle — use curl then extract.
- China MEM (Ministry of Emergency Management): full-text reports for especially major accidents at `mem.gov.cn/gk/sgcc/tbzdsgdcbg/` (Qingdao 11·22, Kunshan 8·2 verified as full-text HTML); lesser accidents are bulletins, not full text; site search unavailable — navigate by listing pages.
- UK HSE: `hse.gov.uk` public investigation reports navigable from homepage 〔Partially tested: site reachable〕.

## C.3 Maritime and Transport (ma) 〔Tested〕

- MAIB (UK): `www.gov.uk/maib-reports` listing page; report PDFs at `assets.publishing.service.gov.uk/media/<id>/<filename>.pdf` (links provided by listing page).
- ATSB (Australia): connection failed from this environment (HTTP 000) 〔To verify on different network〕.

## C.4 Software and Internet Services (sw) 〔Tested〕

- Vendor postmortems: Cloudflare `blog.cloudflare.com` (tag pages and individual posts); GitHub `github.blog` (outage statements under news-insights/company-news and monthly availability reports). Warning: both sites occasionally time out on fetch — retry with curl plus browser User-Agent.
- Regulatory penalties: CNIL English site `cnil.fr/en/sanctions` and individual decision pages 〔Tested〕; French original decisions on Légifrance (403 from this environment) 〔To verify〕; UK ICO penalty listings are JS-rendered — standard fetch returns no entries 〔To verify: headless browser〕; FTC case library accessible but search is page-based 〔To verify〕.
- Chinese vendor announcements: Alibaba Cloud and similar help/status pages are JS-rendered; static fetch returns no content 〔To verify〕.

## C.5 Finance (fi) 〔Tested〕

- SEC litigation releases: `sec.gov/enforcement-litigation/litigation-releases/lr-<number>`; the listing page's first screen covers only the most recent two years — older years require year-by-year navigation. Warning: concurrency above 2 triggers rate-limiting timeouts.
- FINRA monthly disciplinary summaries: `finra.org/sites/default/files/<year-month>/disciplinary-actions-<month>.pdf` (link from the official Actions page). Historical interactive indexes are unfriendly to scraping; monthly PDFs are the most reliable channel.
- CSRC (China): penalty decision body pages at `csrc.gov.cn/csrc/c101928/<content>.shtml` are fetchable; the penalty listing is JS-rendered — lists cannot be scraped, but individual pages linked from the homepage work 〔To verify: headless browser for lists〕.
- Unavailable: UK FCA (site-wide 403), US OCC (internal pages 302-redirect loop) from this environment 〔To verify〕.

## C.6 Remaining Domains 〔To verify〕

- Healthcare (me): HSSIB original site unreachable from this network; Internet Archive snapshots verified working (see me-001–016 in Appendix B). AHRQ PSNet/WebM&M available.
- Pharma/Devices (ph): FDA openFDA API (`api.fda.gov`) for drug/device/food enforcement — highly reliable, supports precise recall_number queries.
- Construction/Infrastructure (ce): RAIB (UK rail) on gov.uk platform — same as AAIB/MAIB, tested working. NIST disaster-failure pages accessible.
- Energy/Nuclear (nu): French ASNR regulation-control pages accessible (`reglementation-controle.asnr.fr`); NRC news releases accessible (`nrc.gov/about-nrc/news-releases/`); NRC ADAMS document library and IAEA IRS require member access.
- Manufacturing/Supply chain (mn): CPSC recalls fully accessible (`cpsc.gov/Recalls/`); NHTSA 403 from this environment.
- Agriculture/Food (ag): CDC MMWR fully accessible (`cdc.gov/mmwr/`); FDA food enforcement via openFDA food API; FSIS 403.
- Public policy (po): GAO product pages accessible (`gao.gov/products/`); listing pages 403 — navigate from homepage topics. NAO reports accessible (`nao.org.uk/reports/`). China Audit Office PDFs accessible (`audit.gov.cn`).
- Military (mi): NASA history pages accessible for aerospace investigation reports; defence safety publications largely restricted.
