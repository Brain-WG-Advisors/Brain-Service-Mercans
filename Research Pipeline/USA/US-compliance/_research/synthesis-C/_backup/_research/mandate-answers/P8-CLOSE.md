# P8-CLOSE - six remaining mandate items (2026-10-30)

Hunter: compliance-source-hunter. Files saved under `00-official-sources/pdfs/<UF>/` with `2026-10-30` in the name (plain curl; Wayback raw `2026id_` where noted). Shard: `_register-shards/mandate-P8-close-r1.csv`, 11 rows `US-<UF>P8-NNN`, appended to `legal-basis-register.csv` (1149 -> 1160 rows, 20 columns on all rows, ids unique). MANDATE.md and build-manifest.json untouched.

Budget used: about 55 tool calls, well under 2 h.

## Verdicts

| # | Item | Verdict | Register ids | Evidence |
|---|---|---|---|---|
| 1a | NH prevailing wage, public works | CLOSED (repeal shown at chapter level) | US-NHP8-001, US-NHP8-002 (A.1) | gc.nh.gov Title XXIII chapter list entry: "CHAPTER 280: MINIMUM WAGES OF EMPLOYEES IN PUBLIC WORKS - Chapter is repealed". Limit: the repealing session law, its date and any residual rule NOT located (280:1 ff. pages not archived; direct gc.nh.gov fetches failed with socket/403). Cite as "RSA ch. 280 repealed", no session-law number. The old MANUAL row US-NHR3-001 can now be replaced by US-NHP8-001 in consumers. |
| 1b | NHES authorized-agent procedure newer than 2016 | STILL OPEN (nothing newer found) | US-NHP8-003 (A.3) | Only NHES 0041 (US-NHP6-001) states the procedure. The NHUIS "Employer TPA Info" help page covers portal registration (account number, FEIN, registration code from the NHES letter, phone 603-223-6100), not agent authorization. nhes.nh.gov employer pages and the NHUIS employer guide return 403 to curl; guide not archived. Closes with: the current NHES agent/TPA form or the NHUIS employer guide, from NHES (603-223-6100) or the owner's browser. |
| 2 | NJ N.J.S.A. 34:11-4.6 pay statement | CLOSED (authority copy, A.2) | US-NJP8-001 | pub.njleg.gov and lis.njleg.state.nj.us do not connect from this machine (timeout), Wayback has no capture. The NJ DOL "State Wage Payment Law and Other Selected Labor Laws" page prints the full text: statement of deductions each pay period; employers with 10+ employees add gross wages, net wages, rate of pay, hours if relevant; electronic allowed unless employee asks for paper. Tier is A.2 (authority's own reproduction), not the Legislature's site. Replaces MANUAL US-NJ-P5-2-001 (not flipped: not in the named list). |
| 3 | NM NMSA 50-4-2 | CLOSED with limit | US-NMP8-001 (A.1), US-NMP8-002 (A.3), US-NMP8-003 (defect) | nmonesource.com cannot be read with curl (script-rendered; a fresh fetch returned a Chapter 46 shell). Primary text found on nmlegis.gov: 2005 SB 639 final text amends 50-4-2 and contains the written-receipt sentence verbatim; the 2023 HB 23 reprint shows the same sentence as current law. The two saved files `nm-nmsa-50-4-2_...html` (Chapter 49 Land Grants) and `nm-nmsa-7-3-3_...html` (Chapter 47 Property Law) ARE shell pages, unusable; marked in US-NMP8-003 (status not_applicable). No register row cited them. Limit: amendments after 2023 not excluded; compilation text not read. |
| 4 | VT rule 24-090-003 official copy | STILL OPEN | none (LII row US-VTP6-001 stays tier B MANUAL) | sos.vermont.gov returns 403 and sec.state.vt.us does not resolve; secure.vermont.gov/SOS/rules is only the proposed-rules service; the CVR host (lexisnexis.com/hottopics/codeofvtrules) returns an empty script page; no Wayback capture of any SOS PDF; searches return only LII/Justia mirrors and VDOL WH-13 (A.3, US-VT-P5-2-004). Closes with: the 24-090-003 text from the Vermont Code of Rules viewer (owner's browser) or the owner accepting LII + WH-13. |
| 5 | US-MQ-03 language, KY and NM | CLOSED for the statutes read | KY: US-KYP8-001, -002, -003 (A.1); NM: US-NMP8-001, -002 | KY: no requirement found in KRS 337.070 (deduction statement, 10+ employees, paper or electronic, in force since 2017-06-29), 337.320 (records) or 337.325 (posting of state summaries). NM: no requirement found in 50-4-2 as passed in 2005 and reprinted in 2023. Not read in either state: 803 KAR, NMAC, poster texts. LANG-2 (IN, KY), LANG-4 (NM), LANG-5 (UT) rows refreshed in the answer files. |
| 6 | NY PFL 2026 rate | CONFIRMED | US-NYP8-001 (A.2) | DFS decision page (HTTP 200, saved): "The 2026 PFL rate will be set at 0.432% of an employee's wages each pay period up to and not to exceed an annual maximum employee contribution of $411.91"; +11.31% over 2025. Matches US-NYP7-002 exactly. US-NYP7-002 left `active`; its note "DFS page 403" is outdated, cite US-NYP8-001. paidfamilyleave.ny.gov contributions URL returned 404 (not used). |

## Defects fixed in the register (P6-ACCESS list)
- 19 rows set to `superseded` (US-INR3-007, US-LAR3-003, US-FEDR3-011, US-MNR3-003/-004/-005, US-NHR3-002, US-NJR3-001, US-NJ-P5-1-005, US-NJR3-002, US-NJR3-006, US-NM-P5-2-006, US-NM-P5-2-008, US-UT-P5-1-004, US-UT-P5-2-002, US-UT-P5-1-005, US-UT-P5-2-003, US-UT-P5-2-004, US-VA-P5-2-004). Only column 20 changed on 18 of them; backup of the pre-edit register kept in the session scratchpad.
- US-NJR3-001 figure text corrected to the Newark page ("more than 50%"; "does not say whether the tax may be withheld"); correction noted in `verification_method`.
- LANG-2 (IN, KY), LANG-4 (NM), LANG-5 (UT) answer rows refreshed to cite the P6/P8 rows.

## Files saved (2026-10-30)
NH: NH_RSA-280_wayback, NH_RSA-title23-index_wayback, NH_NHUIS-Employer_TPA_Info_wayback. NJ: NJ_DOL-selectedstatelaborlaws. NM: NM_SB0639-2005-final, NM_HB0023-2023.pdf. KY: KY_KRS-337-070/-320/-325.pdf, KY_KRS-337-chapter. NY: NY_PFL-rate-decision-2026. Failed or empty downloads (403, 404, shell pages) were deleted, not kept.

## Bloco de prova
- **Pedido -> resposta:** items 1-6 each have a verdict and ids above; item 1 split into 1a closed and 1b open; defects fixed.
- **Fontes:** each new row names the saved file and section; text extracted from the saved files (HTML stripped, pdftotext).
- **Teste:** register 1160 rows, all 20 columns, ids unique; only the 19 named rows differ from the pre-edit register; shard 11 rows x 20 columns.
- **Confianca:** NY 95%; KY 90%; NJ 90% (A.2 not legislature copy); NM 75% (legislature text, not compilation); NH repeal 80% (chapter-level, no session law); NH agent procedure, VT open.
