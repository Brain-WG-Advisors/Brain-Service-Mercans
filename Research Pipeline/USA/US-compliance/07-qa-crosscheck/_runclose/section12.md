

## 12. Re-check 4 (C39), 2026-11-05

**Verdict: RELEASE-READY.** C39 now PASSes, and it was the only gate still failing. This section supersedes sections 10 and 11 where they differ.

- **What changed.** The user opened five of the blocked pages live on their official hosts through a browser VPN (Americas region) and saved them to `00-official-sources/ccg-sources/_test0-opera-2026-11-05/`.
- **Independent check by the auditor.** Each quote was looked up in the saved file (`_runclose/c39_vpn.py`):

| Test | Saved file | Text found in the file | Supports the assertion |
|---|---|---|---|
| T46 IN 2.95 % | IN-DOR-rates.html | "The Indiana Individual adjusted gross income tax rate for 2026 is 2.95% and will adjust in 2027 to 2.9…" | Yes |
| T49 NC 3.99 % | NC-GS105-153.7.html | "Taxable Years Beginning … In 2025 4.25% After 2025 3.99%" | Yes |
| T50 KY 3.5 % | KY-KRS141.020.pdf | "(f) For taxable years beginning on or after January 1, 2026, the tax shall be three and one-half percent (3.5%) of net income" | Yes |
| T55 TX Form C-42 | TX-C42.html | "Form C-42 is used to authorize an individual or service company to represent you…"; title "Written Authorization to Represent Employing Unit (Form C-42)" | Yes |
| T56 OR other-state wages | OR-ORS657.html | ORS 657.095(2): "The remuneration paid by an employer located in this state for work performed in other states … shall be included in payroll when the work in the other states is covered by unemployment insurance laws. The Director … shall prescribe the manner of providing proof of the payment of payroll taxes on the wages of an employee earned while working in other states." | Yes. The statute counts wages taxed in another State toward the Oregon payroll (the taxable-wage computation), with proof of the other State's tax. The section does not use the word "credit"; that word is the CCG's paraphrase of this rule |

- **Shared check.** `test0_check.py`: **C39 PASS, 55/56 = 98.2 %** (target 95 %).
  - By artifact: CCG 20/21, WTC 14/14, SIR 4/4, DD 6/6, PSL 5/5, RSPEC 6/6.
  - 33 of the 56 items are high risk. There are 0 FAIL.
- **md5.** No artifact changed. Every deliverable matches its md5_final: WTC 1/1, SIR 22/22, RSPEC 22/22, DD 17/17, PSL 22/22, DESIGN 1/1, SKILL 99/99. The CCG is still 333e8ee60a3d97a9b229b859c4f5da7c (reviewed in r7) and SCOPE is 8c1b7e8a. The other checks were not re-run, because only `US-TEST0.json` changed.
- **Non-blocking, before production.** Re-read T51 (UT income tax 2026 = 4.45 %, [US-UTS5-001], https://le.utah.gov/xcode/Title59/Chapter10/C59-10-S104_2026050620260506.html) from a US IP. Record the quote in `US-TEST0.json` and re-run `test0_check.py`. The registered local copy already holds 4.45.
- **Still open, non-blocking.** RC-5 (major, register closed-period rows), the `LIMITATION_KEYS` pin (minor), and everything named in section 6, including the owner confirmations US-OWN-009, US-OWN-010 and US-OWN-011.
- **Accuracy.** As in section 9. Test 0 is 98.2 % (55/56 assertions confirmed on the authority hosts).
