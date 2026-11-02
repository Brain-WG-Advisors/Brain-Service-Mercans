# Chrome re-hunt (mandate pass 2) — common instructions

BASE = C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance

You are acting as **compliance-source-hunter** (read its doctrine first: C:/Users/instituto/.claude/agents/compliance-source-hunter.md — §G-NUMBER, tiers, register columns). You research; you never write a deliverable, never edit MANDATE.md or build-manifest.json.

## Why this pass exists
Pass 1 (WebFetch) was blocked by many state .gov hosts (403 / DNS / script-rendered). The owner decided (2026-10-29) to read those sources through **Claude in Chrome** — the owner's own browser, like a person reading the page. The six-part per-state questions are NOT reduced: every part must be answered or proven NOT LOCATED after a real read.

## Browser rules (mandatory)
- Load the Chrome tools with ONE ToolSearch: `select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__find,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__browser_batch`.
- Call tabs_context_mcp once, then **create your OWN tab** with tabs_create_mcp and use ONLY that tabId (other workers share the browser). Close it at the end.
- Read with navigate + get_page_text. To find a page, use the site's own search (e.g. `https://search.mass.gov/?q=...`) or the agency's publications index. PDFs: open the PDF URL in your tab and get_page_text.
- Read only; never log in, never fill forms, never accept cookie banners beyond declining non-essential, never download files. Never solve a CAPTCHA: if one appears, record the URL as `gated` and move on.
- **Never use javascript_tool** (no script injection, no loading external libraries such as pdf.js into a page). **Never alter or strip output to get past a "[BLOCKED: …]" filter** — a blocked output is recorded as unreadable. If a PDF cannot be read with get_page_text, record it as `unreadable-pdf` with its URL for the owner (added 2026-10-29).
- Do not use curl/user-agent tricks. WebFetch/WebSearch may still be used for hosts that are not blocked.

## Per state, the six parts (from MANDATE.md US-MQ-{id})
1. Wage income tax: statute + withholding guide 2026 (method, certificate, supplemental rate, rounding).
2. Local wage taxes: exist? which (city/county/school district/transit)? who administers/collects (state return vs separate)?
3. SUI: agency, 2026 taxable wage base, new-employer rate, employee contribution yes/no.
4. SDI/TDI/PFML/LTC/other employee or employer levies: programme, authority, 2026 rate/cap.
5. Multistate: reciprocity agreements (statute or DoR publication), resident credit, convenience rule, nonresident day/dollar thresholds.
6. Pay-statement statute; state POA form for a third-party filer; official calculator/oracle; primary-language notice if any.

## What to do
1. Read your group's existing answers file `_research/mandate-answers/{GROUP}.md` and shard `00-official-sources/_register-shards/mandate-{GROUP}.csv`.
2. Re-read in Chrome every row that is MANUAL, gated, LOW, snippet-only, listing-only or has an empty verification_method. Confirm or correct the figure from the primary page; set status `active` and verification_method `chrome-read <date>` only after a real read.
3. Fill every NOT LOCATED part of the six above.
4. **Append** new rows to the same shard (same 20 columns, new register_ids continuing the group's sequence); update rows in place when re-verified. Write incrementally.
5. Rewrite `_research/mandate-answers/{GROUP}.md` per state: each of the six parts → answer, register_id(s), effective date, confidence; NOT LOCATED only after a real read showed absence (say which page).
6. Every number with its effective date (vigência), read from the primary page — never from a search summary.

Budget: up to 12 page reads per state; state it in your first line.
Final report (max 12 lines): per state, parts answered x/6, remaining gaps, CAPTCHA/gated URLs.

## Pass 4 additions (2026-10-29) — gap-fill by wave
- Work ONLY on the parts listed as missing for your states in `_pipeline/build-manifest.json` → `_seal_assessment_2026-10-29.blocking_jurisdictions_parts_missing` (read it first).
- Part 6 is mandatory for every state: pay-statement statute (cite section), state prevailing-wage statute (exists? agency), state POA / third-party agent authorization form for withholding AND for UI, official calculator/oracle (or "none; re-derive from official tables").
- Source order: (1) WebFetch/WebSearch to the official host; (2) Claude in Chrome own tab (get_page_text / find only); (3) Wayback copy `https://web.archive.org/web/2026/<official-url>` — accept only 2025/2026 snapshots; for PDFs you may save the archived file (`https://web.archive.org/web/<ts>id_/<url>`) under `00-official-sources/pdfs/<UF>/<name>_wayback-<ts>.<ext>` and read it locally with PyMuPDF (`python -I`).
- Owner decision: no state may be excluded from validation (US-MQ-11).
- Write to your group shard and append a `PASS 4 (wave …)` section to the group answers file; for each state list the six parts with status after this pass.
