# Statutory parameters — belastingjaar 2025

Every figure below is transcribed from `handboek-loonheffingen-2025-okt.pdf`
(Handboek Loonheffingen 2025, versie oktober 2025), bundled in this folder.
Table numbers refer to that document's "Tarieven, bedragen en percentages
loonheffingen vanaf 1 januari 2025" annex. Verify against the PDF before
citing a figure in a client-facing finding.

**Do not use any figure here for a period outside 2025.** See
`../2026/` for the 2026 documents.

## Werknemersverzekeringen — premium percentages (Tabel 9)

| Premium | Rate | Declared premium-wage field (XML) |
|---|---|---|
| AWf laag | 2,74% | `PrlnAwfAnwLg` |
| AWf hoog | 7,74% | `PrlnAwfAnwHg` |
| AWf herzien | 7,74% | `PrlnAwfAnwHz` |
| Aof laag | 6,28% | `PrlnAofAnwLg` |
| Aof hoog | 7,64% | `PrlnAofAnwHg` |
| Opslag Wko | 0,50% | `PrlnAofAnwHg` (and Aof laag / uitkering base) |
| Ufo premie | 0,68% | `PrLnUFO` |
| Gedifferentieerde premie Whk | **employer-specific** | `PrlnWhkAnw` |

**Whk has no published rate.** It is set per employer by beschikking. If the
beschikking is not supplied, derive the applied rate from the income relations
that do carry a premium, and label the result **inferred, not verified** in the
findings register. Never state a Whk finding as "wrong against the beschikking"
without the beschikking.

The Whk beschikking (and the sector code) reach the employer in the
*Aangiftebrief* each November, and in the *mededeling/beschikking
gedifferentieerd premiepercentage Werkhervattingskas*, usually November or
December — see foutmelding L2085.

### Aof laag versus hoog is an employer-size test, not a per-employee one

Based on the employer's premieloonsom in 2023 (Tabel 9):

| Employer size | Premieloonsom threshold |
|---|---|
| Gemiddeld premieloon werknemer | € 39.600 |
| Kleine werkgever | ≤ € 990.000 (25× average) |
| Middelgrote werkgever | ≤ € 3.960.000 (100× average) |
| Grote werkgever | > € 3.960.000 |

Only small employers pay Aof laag. So an entire population declared at Aof hoog
is *correct* for a large employer and is not a finding. Check the size before
raising anything on Aof laag/hoog.

## Zorgverzekeringswet (Tabel 12)

| Item | Rate |
|---|---|
| Werkgeversheffing Zvw | 6,51% |
| Ingehouden bijdrage Zvw | 5,26% |
| Zeevarenden (incl. deelvissers) | 0,00% |

The ingehouden bijdrage applies only where the employer levy does not — and
per foutmelding **L1310**, `IngBijdrZvw` must be 0 unless code
verzekeringssituatie Zvw is **M**.

## Loontijdvakbedragen — maximum premieloon and bijdrageloon (Tabel 11)

Identical for werknemersverzekeringen and Zvw.

| Dag | Week | 4 weken | Maand | Kwartaal | Jaar |
|---|---|---|---|---|---|
| € 291,78 | € 1.458,92 | € 5.835,69 | € 6.322,00 | € 18.966,00 | € 75.864,00 |

**A period base above the period maximum is not automatically wrong.** The
ceiling is annual and applied cumulatively through voortschrijdend cumulatief
rekenen (VCR), so a period may exceed the period figure where earlier periods
fell below it. Test the cumulative position, not the period figure in isolation.

## Other parameters

| Item | Value | Source |
|---|---|---|
| Anoniementarief | 52% | Handboek §2.6; carried as code loonbelastingtabel **940** |
| 52% on negatieve uitgaven bij afkoop | 52% | code loonbelastingtabel **950** |
| Afbouw arbeidskorting | 6,510% (3,257% at AOW age) | Handboek tariefannex |
| Minimum gebruikelijk loon aanmerkelijk belang | € 56.000,00 | Tabel 12 |
| Bijtelling privégebruik auto, 1e toelating ≥ 01-01-2017 | 22% | Tabel 12 |
| Bijtelling privégebruik auto, 1e toelating < 01-01-2017 | 25% | Tabel 12 |
| AOW-leeftijd in 2025 | 67 jaar | Handboek |
| Holiday allowance (vakantiebijslag) minimum | 8% | WML |

Minimum wage changes on 1 January **and** 1 July. For a period spanning the
change, take the rate in force on each day of the period. The full WML table,
including the youth and BBL percentages, is in the Handboek tariefannex — read
it there rather than caching a figure here.

## Rounding

Handboek §9.3.6: round the result to cents **in the employee's favour**. A
difference in rounding *direction* is a finding in its own right, but a minor
one. See `controls-2025.md` for the tolerance the validator applies.

## Verification log

| Item | Verified against | Date |
|---|---|---|
| All premium percentages, Tabel 9 | Bundled Handboek, oktober 2025 | 2026-09-19 |
| Loontijdvakmaxima, Tabel 11 | Bundled Handboek, oktober 2025 | 2026-09-19 |
| Zvw percentages, Tabel 12 | Bundled Handboek, oktober 2025 | 2026-09-19 |
| Bijzondere beloningen table | `wit_bb_nl_std_20250101.pdf`, Belastingdienst | 2026-09-19 |
