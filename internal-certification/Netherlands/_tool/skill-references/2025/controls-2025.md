# Official controls — belastingjaar 2025

Two numbering schemes, both from the Belastingdienst, both bundled here.

- **Poortcontrole numbers** (four digits, e.g. 0003, 1615, 2205) — from
  `gegevensspecificaties-2025.pdf`. Split into `Poortcontrole xsd`
  (mandatory/optional) and `Poortcontrole overig` (cross-total and conditional
  rules). These govern acceptance of the message.
- **L-codes** (e.g. L1314, L2201) — from `toelichting-foutmeldingen-2025.pdf`,
  "Toelichting foutmeldingen werknemersgegevens bij de aangifte loonheffingen
  2025". These are the quality checks the Belastingdienst and UWV run on
  employee data after acceptance, reported back in a foutenrapport.

**Cite the control number in every finding it supports.** A finding that traces
to an authority control number is materially stronger than one that rests on
this skill's own reasoning.

## Contents

- Acceptance is not validation
- Collective versus nominative totals
- Insured status and AOW age
- AWf laag / hoog / herzien
- Premium declared as zero
- Leavers, end dates and retro
- Zvw codes
- Tabelcode consistency
- Identity and mandatory fields
- Where there is no control

## Acceptance is not validation

Chapter 1 of the toelichting states plainly that not all employee data is
checked in 2025, and that the Belastingdienst may return to what it did not
check. A return that was accepted, and that produced no foutenrapport, has
**not** been validated. Say so in the report when a client argues that a filed
return must be correct because it was accepted.

## Collective versus nominative totals

`Poortcontrole overig` attaches a numbered rule to each collective rubriek
requiring it to equal the rounded sum of the same field across all
inkomstenverhoudingen for the tijdvak. Worked examples from the spec:

| Control | Rule |
|---|---|
| 0003 | `IngLbPh` collective = rounded sum of `IngLbPh` over all IKVs in the tijdvak |
| 1026 | `TotAanwCumPrlnUfo` = rounded sum of the per-IKV Ufo aanwas |
| 0031 | If `TotPrUfo` ≠ 0 then `TotAanwCumPrlnUfo` must also be ≠ 0 |
| 0326 | `IngLbPh` verplicht |

Test **every** collective field this way, not a sample. Read the rubriek's own
`Poortcontrole overig` entry in the gegevensspecificaties for its number rather
than assuming 0003 applies generally.

Separately: `TotGen` must equal `TotTeBet` plus the sum of the
`SaldoCorrectiesVoorgaandTijdvak` entries. Report any negative amount in a
collective field.

## Insured status and AOW age

| Control | Rule |
|---|---|
| L1314 | `IndWAO` = J for a person who has reached AOW age. Not possible. |
| L1315 | `IndWW` = J for a person who has reached AOW age. Not possible. |
| L1907 | WW and/or WAO indicator J while aard arbeidsverhouding is 7 (stagiair), or the employee has reached AOW age, and no datum einde IKV is supplied |
| L2322 | AWf laag/hoog/herzien/uitkering or Ufo aanwas ≠ 0 for an employee already at AOW age on the period start date |
| L2328 | Whk aanwas ≠ 0 for an employee already at AOW age on the period start date |
| L2337 | Aof laag/hoog/uitkering aanwas ≠ 0 for an employee already at AOW age on the period start date |

L1314 and L1315 both describe the mid-period transition: where the employee
reaches AOW age **inside** the tijdvak and keeps working, a new
inkomstenverhouding arises — one period insured, one not — and the existing IKV
may be split into two inkomstenperiodes. Report that as a transition, not a
flat error.

## AWf laag / hoog / herzien

The contract indicators are `IndArbovkOnbepTijd`, `IndSchriftArbovk` and
`IndOprovk`. AWf **laag** requires the combination **J-J-N**: indefinite,
written, not on-call.

| Control | Rule |
|---|---|
| L2201 | AWf laag aanwas ≠ 0 while the indicators imply it must be 0 — indefinite N, or written N, or on-call J — or the employee was under 21 at period start, or aard = 83, or SrtIv in 31/32/33/38/39/40/46 |
| L2225 | AWf hoog aanwas ≠ 0 while aard = 83 or SrtIv in that benefit range, **or** while the indicators are J-J-N (i.e. the employee qualifies for laag) |
| L2302 | AWf herzien aanwas ≠ 0 while the indicators are not J-J-N |
| L2306 | AWf laag aanwas ≠ 0 while SrtIv = 15 and code fase indeling F&Z is 1 or 17 |
| L2103 | Any of the three indicators supplied while aard is 4, 6, 7, 18, 79 or 81 |
| L2221 / L2222 / L2223 | Indefinite / written / on-call indicator supplied while SrtIv is not 11, 13, 15, 53 or 62 |
| L2202 | On-call indicator N while contracturen per week is 0, for SrtIv 11/13/15 and aard 1/21/22/23/24/82/83 with no end date |
| L2502 | Indefinite indicator N while SrtIv = 15 and fase F&Z is 4 or 19, with no end date |
| L2503 | On-call indicator N while fase F&Z is 38 or 43 |

These are the tests to run where master data leaves the contract indicators
blank or unpopulated — the XML carries the values even when the master extract
does not.

## Premium declared as zero against a non-zero base

| Control | Premium |
|---|---|
| L2341 | Aof laag |
| L2342 | Aof hoog |
| L2343 | Aof uitkering |
| L2401 | AWf laag |
| L2402 | AWf hoog |
| L2403 | AWf herzien |
| L2404 | AWf uitkering |
| L2405 | Ufo |
| L2268 | Opslag Wko = 0 while any Aof premie ≠ 0 |

Each reads: premium filled with €0 while the corresponding aanwas in the
cumulative premieloon is €1 or more.

## Leavers, end dates and retro

| Control | Rule |
|---|---|
| L2501 | No code reden einde arbeidsverhouding while a datum einde IKV is supplied |
| L2303 | IKV still supplied more than 4 months after its end date, with all amounts €0 or absent |
| L1818 | All werknemersverzekeringen indications N while Loon SV ≠ 0 and no datum einde IKV supplied |
| L1913 | `IndWW` = N while the IKV is not ended and premie Ufo > €0 |
| L2024 | Reden einde code supplied while SrtIv is not 11, 13 or 15 |
| L2307 | Reden einde 50 or 51 while aard is not 18 or 83 |
| L0039 | Datum aanvang IKV after the period end date |
| L0040 | Datum einde IKV after the period end date |
| L2209 | Datum aanvang inkomstenperiode outside the tijdvak, for the listed SrtIv values where aard ≠ 11 |

These run on the XML alone and need no leavers master-data extract.

Note the code-list change at the year boundary: reden einde code **31** was
withdrawn on 1 January 2026 and replaced by 32, 33 and 34. Corrections over
2025 and earlier must still carry **31**, because 32/33/34 do not exist in
those years' specifications. Never validate a 2025 return against the 2026
code list.

## Zvw codes

| Control | Rule |
|---|---|
| L1310 | `IngBijdrZvw` must be 0 unless code verzekeringssituatie Zvw = M |
| L1911 | Code L (0%-tarief, zeelieden) requires werkgeversheffing Zvw = €0 |
| L1814 | Zvw code K, L, M or N while the tabelcode does not begin 0, 3 or 7 and is not 210, 226, 250, 940, 950 or 999 |
| L2301 | Zvw code A, B or I while the tabelcode begins 0, 3 or 7 or equals 226 |
| L2408 | SrtIv 42 or 43 with tabelcode 250 requires Zvw code A, K or M |
| L2509 | Werkgeversheffing Zvw ≠ €0 while SrtIv = 17 (DGA not insured) |

## Tabelcode consistency

| Control | Rule |
|---|---|
| L2505 | Verrekende arbeidskorting > €0 requires the **second digit** of the tabelcode to be 1 (wit), unless the code is 210, 220, 221, 224, 225, 226, 227, 228, 940, 950 or 999 |
| L0050 | Address may not be missing unless the tabelcode is 940 |
| L2287 | BSN is mandatory unless the tabelcode is 221, 224, 225, 940 or 999 |

L2505 is the green-table test: arbeidskorting on a green-table income relation
is a finding.

## Other conditional rules worth running

| Control | Rule |
|---|---|
| L2208 | Loon SV ≠ 0 while SrtIv is 17, 22, 23, 24, 34, 36, 37, 42–45, 50, 52 or 55–63 |
| L2219 | Loon SV = 0 while SrtIv is 11/13/15/18/31–33/38–40/46, at least one WV indication is J, Loon LB/PH ≠ 0, aard ≠ 6 and tabelcode not 221/224/225 |
| L2336 / L2340 | Aof laag / hoog aanwas ≠ 0 while SrtIv is not 11, 13, 15, 18 or 53 |
| L2338 / L2339 | AWf / Aof uitkering aanwas ≠ 0 for the listed benefit SrtIv values |
| L2203 | SrtIv 11 (ambtenaar) requires aard 1, 18 or 83 |
| L2085 | Declared sector differs from the beschikte sector |
| L0091 | BSN and date of birth combination disagrees with the BRP |
| L1812 / L1813 | Code reden geen bijtelling auto supplied while the bijtelling value (or its net of employee contribution) is > 0 |
| 2205 / 1615 | Contractloon: not supplied or 0 unless SrtIv is 11, 13, 15, 17, 33, 53 or 62; mandatory for 11, 13, 15, 17 |
| 2206 / 1614 | Aantal contracturen per week: same condition set as contractloon |

## Where there is no control

There are L-codes for a zero premium against a non-zero base for Aof, every AWf
variant and Ufo — **but none for Whk**. A Whk premium declared as zero against
a non-zero `PrlnWhkAnw` therefore passes the gate silently.

It is still wrong. The premium is owed by the employer under art. 20 Wfsv and
must be declared in full whatever is recovered; recovery from the employee is
limited to half the WGA component, taken from net pay (art. 34(2) Wfsv, art.
3.18 Regeling Wfsv). The absence of an automated control is the reason this
check has to live here.

The same logic applies generally: the Belastingdienst's silence is not a pass.

## Tolerance

Apply **€0,50 per employee per field** as the rounding threshold. Below that,
record as rounding and do not raise. Above it, raise as a finding. Report the
count of sub-threshold differences so the reader knows they were tested.

At collective level, expect per-IKV rounding to accumulate: across several
hundred income relations a €20–€40 difference between a recalculated premium
and the declared total is ordinary. A difference an order of magnitude larger
is not.
