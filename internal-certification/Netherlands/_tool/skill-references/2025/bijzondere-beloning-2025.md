# Witte tabel bijzondere beloningen — Nederland, Standaard, uitgave januari 2025

Transcribed cell-by-cell from `witte-tabel-bijzondere-beloning-2025.pdf`
(Belastingdienst, `wit_bb_nl_std_20250101.pdf`), bundled in this folder.
Verified against that PDF on 2026-09-19.

Applies to bijzondere beloningen: vakantiegeld, 13e maand, bonus,
eenmalige uitkeringen, overwerk paid in one go, eindejaarsuitkering.

**This is the `Nederland, Standaard` table only.** It applies to residents of
the Netherlands with no herleidingsregels — code loonbelastingtabel beginning
`0`. Separate tables exist for residents of Belgium, residents of other
countries, and for each herleidingsregel. If an income relation carries any
other tabelcode, this table is the wrong one; get the matching publication
before concluding anything about its rate.

## READ THIS BEFORE FLAGGING ANY RATE

Each column pair is **standaardtarief** and **verrekeningspercentage
loonheffingskorting**, and they are **added**. The Belastingdienst's own
footnote: the verrekeningspercentage is added to the standaardtarief, the two
may also be applied separately, and the result is rounded to cents in the
employee's favour.

The verrekeningspercentage can be **negative** — see jaarloon 11.050, 13.144
and 24.342, where it is −8,05%, −30,03% and −2,26%. A negative value produces
an effective rate far *below* the standaardtarief. That is correct, not an error.

**A real incident this guardrail exists to prevent:** a prior validation run
treated the two columns as alternatives and flagged 55 employees' withholding
as impossibly high, above a supposed 49,50% maximum. Every one was a valid
addition:

- 35,82 + 4,08 = **39,90**
- 37,48 + 4,08 = **41,56**
- 37,48 + 12,85 = **50,33**
- 49,50 + 6,51 = **56,01**
- 37,48 + 21,43 = **58,91** (AOW age, jaarloon 45.309–58.875)

**Procedure before escalating a rate:** compute
`observed_rate − standaardtarief` for the employee's jaarloon bracket, and
check whether the remainder equals that bracket's verrekeningspercentage in
the column that matches the employee's age, loonheffingskorting status and
alleenstaandeouderenkorting status. Escalate only if no column reproduces it.

## Reading the table

Take the last row whose jaarloon is **not above** the employee's jaarloon.

Pick the column block by age, then the pair by loonheffingskorting status:

- **Jonger dan AOW-leeftijd** — zonder LHK, or met LHK
- **AOW-leeftijd en ouder, geboren in 1945 of eerder** — zonder LHK, met LHK excl. AOK, met LHK incl. AOK
- **AOW-leeftijd en ouder, geboren in 1946 of later** — zonder LHK, met LHK excl. AOK, met LHK incl. AOK

AOK = alleenstaandeouderenkorting. Use the **incl.** pair only where the
employee's master data or regulation-base flags show that credit applies;
otherwise **excl.** Getting this wrong in either direction produces findings
that do not exist.

## Jonger dan AOW-leeftijd

| Jaarloon vanaf | Zonder LHK std | Met LHK std | Met LHK verrek. | Met LHK effectief |
|---:|---:|---:|---:|---:|
| 0 | 35,82 | 0,00 | 0,00 | 0,00 |
| 11.050 | 35,82 | 35,82 | −8,05 | 27,77 |
| 13.144 | 35,82 | 35,82 | −30,03 | 5,79 |
| 24.342 | 35,82 | 35,82 | −2,26 | 33,56 |
| 28.407 | 35,82 | 35,82 | 4,08 | 39,90 |
| 34.001 | 35,82 | 35,82 | 4,08 | 39,90 |
| 36.661 | 35,82 | 35,82 | 4,08 | 39,90 |
| 38.442 | 37,48 | 37,48 | 4,08 | 41,56 |
| 40.503 | 37,48 | 37,48 | 4,08 | 41,56 |
| 43.072 | 37,48 | 37,48 | 12,85 | 50,33 |
| 45.309 | 37,48 | 37,48 | 12,85 | 50,33 |
| 58.876 | 37,48 | 37,48 | 12,85 | 50,33 |
| 76.818 | 49,50 | 49,50 | 6,51 | 56,01 |
| 139.405 | 49,50 | 49,50 | 0,00 | 49,50 |

## AOW-leeftijd en ouder — geboren in 1945 of eerder

| Jaarloon vanaf | Zonder LHK | excl. AOK std | excl. AOK verrek. | incl. AOK std | incl. AOK verrek. |
|---:|---:|---:|---:|---:|---:|
| 0 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 11.050 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 13.144 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 24.342 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 28.407 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 34.001 | 17,92 | 17,92 | 2,04 | **0,00** | **0,00** |
| 36.661 | 17,92 | 17,92 | 2,04 | 17,92 | 2,04 |
| 38.442 | 17,92 | 17,92 | 2,04 | **17,92** | 2,04 |
| 40.503 | 37,48 | 37,48 | 2,04 | 37,48 | 2,04 |
| 43.072 | 37,48 | 37,48 | 6,43 | 37,48 | 6,43 |
| 45.309 | 37,48 | 37,48 | 21,43 | 37,48 | 21,43 |
| 58.876 | 37,48 | 37,48 | 6,43 | 37,48 | 6,43 |
| 76.818 | 49,50 | 49,50 | 3,26 | 49,50 | 3,26 |
| 139.405 | 49,50 | 49,50 | 0,00 | 49,50 | 0,00 |

## AOW-leeftijd en ouder — geboren in 1946 of later

| Jaarloon vanaf | Zonder LHK | excl. AOK std | excl. AOK verrek. | incl. AOK std | incl. AOK verrek. |
|---:|---:|---:|---:|---:|---:|
| 0 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 11.050 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 13.144 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 24.342 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 28.407 | 17,92 | 0,00 | 0,00 | 0,00 | 0,00 |
| 34.001 | 17,92 | 17,92 | 2,04 | **0,00** | **0,00** |
| 36.661 | 17,92 | 17,92 | 2,04 | 17,92 | 2,04 |
| 38.442 | 37,48 | 37,48 | 2,04 | 37,48 | 2,04 |
| 40.503 | 37,48 | 37,48 | 2,04 | 37,48 | 2,04 |
| 43.072 | 37,48 | 37,48 | 6,43 | 37,48 | 6,43 |
| 45.309 | 37,48 | 37,48 | 21,43 | 37,48 | 21,43 |
| 58.876 | 37,48 | 37,48 | 6,43 | 37,48 | 6,43 |
| 76.818 | 49,50 | 49,50 | 3,26 | 49,50 | 3,26 |
| 139.405 | 49,50 | 49,50 | 0,00 | 49,50 | 0,00 |

The three rows in bold are the ones most often transcribed wrongly. At jaarloon
34.001 the incl.-AOK pair is **0,00 / 0,00** in both AOW blocks, not 17,92 /
2,04. At 38.442 in the *geboren 1945 of eerder* block the incl.-AOK
standaardtarief is **17,92**, not 37,48.

## Ceilings — the quickest sanity test

- **56,01%** is the highest rate for an employee below AOW age (49,50 + 6,51).
- **52,76%** is the highest for an employee at or above AOW age (49,50 + 3,26).
- Above those, the only legitimate rate is the **52% anoniementarief**, which is
  carried as code loonbelastingtabel **940** (or 950 for afkoop). A rate above
  the ceilings on any other tabelcode is wrong.

## Jaarloon BT

The lookup needs a jaarloon. Where `Jaarloon BT` is 0,00 on the payslip, no
reader can verify the percentage — report the count and treat it as a finding
in its own right, and state the column that applies plus its ceiling rather
than asserting a "correct rate" for that employee.

Where the BT percentage is supplied to the engine as an **uploaded override**
rather than derived, the upload file itself is the thing to test: check each
uploaded percentage against the employee's date of birth, loonheffingskorting
status and AOK flag. A percentage that is a valid cell of this table can still
be the wrong cell for that employee, and an override will never self-correct.
