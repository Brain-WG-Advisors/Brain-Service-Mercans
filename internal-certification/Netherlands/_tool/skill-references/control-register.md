# Control register

The enumerated check list. **Every run produces every row**, in one of four
states: Pass, Finding, Not tested (with reason), Out of scope.

This list is not a cap on what may be found. Genuine new checks are added as a
dated revision of the register, with new rows marked as new. What it prevents is
a check that already exists being run only when someone asks about it.

Columns below: control ID, what it tests, the source authority, whether the
script runs it (S) or the reviewer does (R).

## A. Scope and integrity

| ID | Check | Authority | By |
|---|---|---|---|
| A-01 | Namespace year matches the validation year | Gegevensspecificaties | S |
| A-02 | Tijdvak is a published period boundary; filing deadline stated | Tijdvakcodes | S |
| A-03 | Correction block date ranges are published periods of the same year | Tijdvakcodes | S |
| A-04 | No tijdvak appears as both period block and correction block | Gegevensspecificaties h.2 | S |
| A-05 | Systematiek determined and confirmed; carve-out resolved | Handboek §9.2.1 | R |
| A-06 | Period integrity under the confirmed systematiek | Handboek §9.2 / §9.2.1 | R |
| A-07 | Retro export reconciles to period block and correction saldi | — | S |
| A-08 | Berichtversie and gegevensspecificaties version recorded | Gegevensspecificaties | S |
| A-09 | Correction blocks present with all saldi zero | Handboek §9.2.1, h.14 | S |

## B. Return internal consistency

| ID | Check | Authority | By |
|---|---|---|---|
| B-01 | Every collective total equals the sum of its nominative field | Poortcontrole overig | S |
| B-02 | `TotGen` equals `TotTeBet` plus correction saldi | Gegevensspecificaties h.4 | S |
| B-03 | No negative amount in a collective field | — | S |
| B-04 | No negative `LnLbPh` / `LnSV` at income-relation level without explanation | — | S |
| B-05 | Nominative record count equals the population expected | — | R |

## C. Wage basis

| ID | Check | Authority | By |
|---|---|---|---|
| C-01 | `LnSV` is the SV wage **before** the maximum premieloon | Gegevensspecificaties rubriek Loon SV; Handboek h.5 | S |
| C-02 | The cap is applied in the aanwas fields, not in `LnSV` | Handboek h.5 (VCR) | S |
| C-03 | Tabelloon composition against the wage type catalogue tax flags | Handboek | R |
| C-04 | `LnSV` = 0 where SrtIv requires it | L2208 | S |
| C-05 | `LnSV` ≠ 0 where SrtIv and indicators require it | L2219 | S |
| C-06 | Cumulative maximum premieloon applied across the year, not per period | Handboek h.5 | R |

## D. Tax tables

| ID | Check | Authority | By |
|---|---|---|---|
| D-01 | Code loonbelastingtabel composition matches pay frequency and colour | Codes document | S |
| D-02 | Regular withholding recalculated against the period table | Witte tabel tijdvak | R |
| D-03 | Bijzondere beloningen rate exists in the applicable column | Witte tabel bb | R |
| D-04 | Rate does not exceed the 56,01 / 52,76 ceilings except on code 940/950 | Witte tabel bb | S |
| D-05 | Jaarloon BT populated so the rate is verifiable | Handboek §9.3.6 | S |
| D-06 | Uploaded BT override values are cells of the table | Witte tabel bb | S |
| D-03 | Supplied BT percentage exists in the column implied by DOB and LHK | Witte tabel bb | S |
| D-07 | Applied rate equals the client-supplied rate (conformity) | Client input; §9.3.6 | S |
| D-10 | BT upload structure — end dates, employees with no row | Client configuration | S |
| D-11 | BT bracket derivation from jaarloon | **Out of scope where client-supplied** | — |
| D-12 | Alleenstaandeouderenkorting materiality | Witte tabel bb | S |
| D-08 | Arbeidskorting only where the tabelcode is white | L2505 | S |
| D-09 | Anoniementarief applied where BSN is absent | L2287; art. 26b Wet LB | S |

## E. Employer premiums

| ID | Check | Authority | By |
|---|---|---|---|
| E-01 | Each premium recalculates from its own declared base | Handboek Tabel 9 | S |
| E-02 | Premium not zero against a non-zero base | L2341-L2343, L2401-L2405 | S |
| E-03 | Whk premium not zero against a non-zero base (**no L-code exists**) | Art. 20 Wfsv | S |
| E-04 | Whk rate consistent across all records carrying a premium | — | S |
| E-05 | Opslag Wko = 0,50% of the Aof base in the same record | L2268; Tabel 9 | S |
| E-06 | Employer premium not recovered from the employee beyond the WGA limit | Art. 20, 34(2) Wfsv; art. 3.18 Regeling Wfsv | R |
| E-07 | Aof laag/hoog consistent with the employer size test | Handboek Tabel 9 | R |
| E-08 | Zvw employer levy — VCR-aware across the year | Handboek Tabel 11/12 | R |
| E-09 | No premium wage or aanwas for an employee at AOW age at period start | L2322, L2328, L2337 | S |
| E-10 | No premium charged for an employee at AOW age (**no control exists**) | Wfsv; Handboek Tabel 9 | S |

## F. AWf classification

| ID | Check | Authority | By |
|---|---|---|---|
| F-01 | AWf laag only where the contract indicators are J-J-N | L2201; Handboek §7.2 | S |
| F-02 | AWf hoog not applied where the indicators are J-J-N | L2225 | S |
| F-03 | AWf herzien only where the indicators are J-J-N | L2302 | S |
| F-04 | Contract indicators present where required by SrtIv and aard | L2103, L2221-L2223 | S |
| F-05 | AWf laag zero where fase F&Z is 1 or 17 with SrtIv 15 | L2306 | S |

## G. Indicators and insured status

| ID | Check | Authority | By |
|---|---|---|---|
| G-01 | `IndWW` / `IndWAO` not J at AOW age | L1314, L1315, L1907 | S |
| G-02 | Insured status agrees between payslip, return and master | Methodology §6 | R |
| G-03 | `IndLhKort` agrees with payslip and G2N flag | Methodology §6 | R |
| G-04 | All WV indications N with non-zero Loon SV and no end date | L1818 | S |
| G-05 | `IndWW` = N with premie Ufo > 0 and no end date | L1913 | S |
| G-06 | Zvw code consistent with bijdrage, levy and tabelcode | L1310, L1814, L1911, L2301, L2408, L2509 | S |
| G-07 | Zvw code K/M agrees with payslip and master | Codes document | R |

## H. Verloonde uren and contract data

| ID | Check | Authority | By |
|---|---|---|---|
| H-01 | `AantVerlU` reflects hours paid, not contract hours | Gegevensspecificaties rubriek | S |
| H-02 | `AantVerlU` population does not cluster on a single value | — | S |
| H-03 | `AantVerlU` = 0 explained | — | S |
| H-04 | `Ctrctln` supplied where SrtIv requires it | 1615, 2205 | S |
| H-05 | `AantCtrcturenPWk` supplied where SrtIv requires it | 1614, 2206 | S |
| H-06 | On-call indicator N with zero contract hours | L2202 | S |

## I. Leavers and income relations

| ID | Check | Authority | By |
|---|---|---|---|
| I-01 | Reden einde code supplied where an end date exists | L2501 | S |
| I-02 | Reden einde code 99 justified, not used as a fallback | Codes document | S |
| I-03 | IKV not declared >4 months after end with all amounts zero | L2303 | S |
| I-04 | Reden einde code valid for the SrtIv and aard | L2024, L2307 | S |
| I-05 | Start and end dates inside the tijdvak where required | L0039, L0040, L2209 | S |
| I-06 | Employee present last period and absent now, with no reden einde | Methodology §2 | R |
| I-07 | Ontslagvergoeding on its own `NumIV` with SrtIv 62 | Gegevensspecificaties | S |

## J. Payslips

| ID | Check | Authority | By |
|---|---|---|---|
| J-01 | Payslip pack parsed; slips separated by period and run number | — | S |
| J-01b | Statutory content complete | Art. 7:626 BW | R |
| J-02 | Cumulative block rolls forward: N = N−1 + movement | Handboek | S |
| J-03 | Cumulative LB/PVV not negative | Handboek | S |
| J-04 | Cumulative fiscal wage not negative | Handboek | S |
| J-05 | Sub-totals sum to stated totals | — | R |
| J-06 | A payslip exists for every income relation in the return | — | S |
| J-07 | Footer fields populated, not nil across the pack | Handboek §9.3.6 | S |
| J-08 | Reservering block against live accrual elements | — | S |

## K. Payments and ledger

| ID | Check | Authority | By |
|---|---|---|---|
| K-01 | SEPA `NbOfTxs` equals the transaction count | ISO 20022 | S |
| K-02 | SEPA `CtrlSum` equals the sum of instructed amounts | ISO 20022 | S |
| K-03 | Control sum equals positive net pay in the G2N | — | R |
| K-04 | Negative-net employees correctly absent from SEPA | — | R |
| K-05 | Payment report total equals the SEPA control sum | — | R |
| K-06 | GL balances debit against credit | — | R |
| K-07 | GL account mapping per wage type ties to G2N subtotals | Pay-elements file | R |
| K-08 | SEPA execution date against period end | — | S |

## L. Gross-to-net

| ID | Check | Authority | By |
|---|---|---|---|
| L-00 | Statutory recalculation complete; reference frame built | — | S |
| G-S1 | SV base against the maximum premieloon (VCR, cumulative) | Handboek h.5 | S |
| G-S2a-e | Aof, Wko, AWf laag/hoog, Zvw ER recalculated from the SV base | Tabel 9 / 12 | S |
| G-S2f | Ingehouden bijdrage Zvw where charged | Tabel 12 | S |
| G-S3 | Special-rate tax against the client-supplied percentage | Client input 52572 | S |
| G-S4 | Regular loonheffing against the witte tijdvaktabel | Witte tabel 4-wekelijks | S |
| G-S5 | Tax base and SV base recomposed from the flagged wage types | Wage Type Catalogue | S |
| G-S6 | Gross − deductions = net; bijtelling residual classified | — | S |
| G-S7/8 | Negative and nil net pay | — | S |
| G-S9 | Total employer contributions foots to its elements | — | S |
| L-03 | Report basis stated and proven: period or run-level | — | R |
| L-04 | G2N agrees with payslips per employee | — | R |
| X-02 | Return Loon SV, fiscal wage and bb wage equal the G2N per employee | — | S |
| X-20 | Every income relation in the return has a G2N row | — | S |

## M. Master data and configuration

| ID | Check | Authority | By |
|---|---|---|---|
| M-01 | Master tax method agrees with the declared tabelcode | Codes document | R |
| M-02 | Contract indicators populated where a premium depends on them | Handboek §7.2 | R |
| M-03 | BT override source is single and authoritative | — | R |
| M-04 | Termination dates and reasons populated | — | R |
| M-05 | Employees with no BT override row have a documented derivation | — | R |

Apply the regrading principle throughout: **a value absent from a master
extract is not by itself a defect.** Test the value that drove the calculation.
An extract gap is a data question unless a calculation depends on it.
