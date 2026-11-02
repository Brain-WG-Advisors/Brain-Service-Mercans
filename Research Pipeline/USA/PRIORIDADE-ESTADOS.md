# Prioridade de estados para a research EUA

> Proxy de mercado, **não** a lista real de clientes da Mercans. Serve para ordenar a fila de builds até termos a master list do BAU; trocar pelo dado real quando existir.

## Método (3 linhas)
1. Peso 60% = participação do estado no emprego das afiliadas norte-americanas de multinacionais estrangeiras (BEA, 2024), proxy da base de clientes (multinacionais não americanas com empregados nos EUA).
2. Peso 40% = participação do estado no emprego privado (BLS QCEW, 2024), proxy do volume geral de folha.
3. Score = 0,6 x % afiliadas + 0,4 x % privado (base = soma das 51 jurisdições); a coluna Tier vem de `US-compliance/_pipeline/build-manifest.json` (`tier._by_jurisdiction`), sem pesquisa nova.

## Fontes
- BEA, *Employment of Majority-Owned U.S. Affiliates, State by Country of UBO* (aba 2024, coluna All countries, milhares de empregados), ano de referência 2024: https://apps.bea.gov/international/xls/mousa-all-employ-state-ctry.xls (página: https://bea.gov/international/di1fdiop; release: https://www.bea.gov/news/2026/activities-us-affiliates-foreign-multinational-enterprises-2024). O total BEA do arquivo é 8.574,9 mil e inclui PR, outras áreas e exterior; a base dos 51 soma 8426.7 mil.
- BLS, QCEW Open Data API, média anual de emprego 2024, setor privado (own_code 5, todas as indústrias, nível estado): https://data.bls.gov/cew/data/api/2024/a/industry/10.csv. Base dos 51 = 132570 mil. Já existe QCEW 2025, mas usamos 2024 para casar o ano com o BEA.
- Opcional (FDI novo), BEA *New Foreign Direct Investment in the United States, 2024*: fora do score; a release só traz os maiores estados em emprego novo (FL 32,7 mil; TX 18,2 mil; NY 14,2 mil): https://bea.gov/news/2025/new-foreign-direct-investment-united-states-2024.
- Tier: `Research Pipeline/USA/US-compliance/_pipeline/build-manifest.json`, `tier._by_jurisdiction` (lido em 2026-10-29).

## Tabela (51 jurisdições)
| Rank | Estado | Afiliadas estrangeiras (mil) | % | Privado (mil) | % | Score | Tier (complexidade) |
|---|---|---|---|---|---|---|---|
| 1 | California (CA) | 885.2 | 10.50% | 15547 | 11.73% | 10.99 | T3 |
| 2 | Texas (TX) | 717.4 | 8.51% | 11911 | 8.98% | 8.70 | T1 (MANUAL only) |
| 3 | New York (NY) | 556.7 | 6.61% | 8303 | 6.26% | 6.47 | T3 provisional (NYC/Yonkers return linkage MANUAL) |
| 4 | Florida (FL) | 472.1 | 5.60% | 8729 | 6.58% | 6.00 | T1 |
| 5 | Illinois (IL) | 371.3 | 4.41% | 5236 | 3.95% | 4.22 | T3 (MANUAL only) |
| 6 | Pennsylvania (PA) | 349.0 | 4.14% | 5346 | 4.03% | 4.10 | T4 (local limb MANUAL) |
| 7 | Ohio (OH) | 322.4 | 3.83% | 4784 | 3.61% | 3.74 | T4 (MANUAL only) |
| 8 | North Carolina (NC) | 345.9 | 4.10% | 4185 | 3.16% | 3.73 | T3 |
| 9 | Michigan (MI) | 335.4 | 3.98% | 3825 | 2.89% | 3.54 | UNCLASSIFIED (gated; lead T4: city income taxes) |
| 10 | Georgia (GA) | 307.0 | 3.64% | 4184 | 3.16% | 3.45 | T3 |
| 11 | New Jersey (NJ) | 306.8 | 3.64% | 3679 | 2.78% | 3.29 | T3 |
| 12 | Massachusetts (MA) | 237.9 | 2.82% | 3199 | 2.41% | 2.66 | UNCLASSIFIED (gated; lead T3) |
| 13 | Virginia (VA) | 202.9 | 2.41% | 3369 | 2.54% | 2.46 | T3 |
| 14 | Tennessee (TN) | 215.7 | 2.56% | 2839 | 2.14% | 2.39 | T1 (MANUAL only) |
| 15 | Indiana (IN) | 204.9 | 2.43% | 2780 | 2.10% | 2.30 | T3 (MANUAL only; county tax piggybacked) |
| 16 | Washington (WA) | 154.0 | 1.83% | 3003 | 2.27% | 2.00 | T1 (verified; 2028 watch item) |
| 17 | South Carolina (SC) | 194.8 | 2.31% | 1918 | 1.45% | 1.97 | T3 |
| 18 | Minnesota (MN) | 158.7 | 1.88% | 2541 | 1.92% | 1.90 | T3 |
| 19 | Arizona (AZ) | 145.1 | 1.72% | 2815 | 2.12% | 1.88 | T3 (MANUAL only) |
| 20 | Wisconsin (WI) | 144.5 | 1.71% | 2558 | 1.93% | 1.80 | T3 |
| 21 | Missouri (MO) | 133.3 | 1.58% | 2483 | 1.87% | 1.70 | UNCLASSIFIED (gated; lead T4: KC/St. Louis earnings taxes) |
| 22 | Colorado (CO) | 130.2 | 1.55% | 2436 | 1.84% | 1.66 | T3 provisional (local limb NOT LOCATED; T4 candidate) |
| 23 | Kentucky (KY) | 152.8 | 1.81% | 1694 | 1.28% | 1.60 | T3 provisional (local occupational license taxes NOT LOCATED; T4 candidate) |
| 24 | Maryland (MD) | 128.9 | 1.53% | 2238 | 1.69% | 1.59 | T3 (county tax piggybacked, verified) |
| 25 | Alabama (AL) | 136.5 | 1.62% | 1717 | 1.30% | 1.49 | T4 (local limb MANUAL) |
| 26 | Connecticut (CT) | 116.8 | 1.39% | 1460 | 1.10% | 1.27 | T3 |
| 27 | Louisiana (LA) | 81.4 | 0.97% | 1616 | 1.22% | 1.07 | T3 |
| 28 | Oregon (OR) | 73.5 | 0.87% | 1702 | 1.28% | 1.04 | T4 (verified) |
| 29 | Nevada (NV) | 70.2 | 0.83% | 1377 | 1.04% | 0.92 | T1 (MANUAL only) |
| 30 | Kansas (KS) | 77.9 | 0.92% | 1183 | 0.89% | 0.91 | T3 (MANUAL only) |
| 31 | Iowa (IA) | 68.6 | 0.81% | 1315 | 0.99% | 0.89 | T3 provisional (school-district surtax NOT LOCATED) |
| 32 | Utah (UT) | 60.5 | 0.72% | 1452 | 1.10% | 0.87 | T3 (MANUAL only) |
| 33 | Oklahoma (OK) | 59.9 | 0.71% | 1356 | 1.02% | 0.84 | T3 |
| 34 | Arkansas (AR) | 52.9 | 0.63% | 1098 | 0.83% | 0.71 | T3 |
| 35 | Mississippi (MS) | 52.4 | 0.62% | 937 | 0.71% | 0.66 | T3 |
| 36 | Nebraska (NE) | 39.4 | 0.47% | 853 | 0.64% | 0.54 | T3 (MANUAL only) |
| 37 | New Hampshire (NH) | 49.8 | 0.59% | 604 | 0.46% | 0.54 | T1 (MANUAL only) |
| 38 | Maine (ME) | 35.7 | 0.42% | 548 | 0.41% | 0.42 | UNCLASSIFIED (gated; lead T3) |
| 39 | Hawaii (HI) | 37.0 | 0.44% | 517 | 0.39% | 0.42 | T3 |
| 40 | Delaware (DE) | 36.4 | 0.43% | 410 | 0.31% | 0.38 | T4 (local limb MANUAL) |
| 41 | West Virginia (WV) | 29.8 | 0.35% | 560 | 0.42% | 0.38 | T3 (MANUAL only) |
| 42 | Idaho (ID) | 21.5 | 0.26% | 735 | 0.55% | 0.37 | T3 (MANUAL only) |
| 43 | New Mexico (NM) | 21.0 | 0.25% | 686 | 0.52% | 0.36 | T3 (MANUAL only) |
| 44 | District of Columbia (DC) | 25.3 | 0.30% | 524 | 0.40% | 0.34 | T3 (MANUAL only) |
| 45 | Rhode Island (RI) | 26.0 | 0.31% | 433 | 0.33% | 0.32 | T3 (MANUAL/gated only) |
| 46 | South Dakota (SD) | 15.7 | 0.19% | 382 | 0.29% | 0.23 | T1 |
| 47 | North Dakota (ND) | 16.2 | 0.19% | 354 | 0.27% | 0.22 | T3 |
| 48 | Montana (MT) | 10.9 | 0.13% | 427 | 0.32% | 0.21 | UNCLASSIFIED (gated; lead T3) |
| 49 | Alaska (AK) | 14.9 | 0.18% | 254 | 0.19% | 0.18 | T1 (lead; unproven) |
| 50 | Vermont (VT) | 13.9 | 0.16% | 256 | 0.19% | 0.18 | T3 |
| 51 | Wyoming (WY) | 9.7 | 0.12% | 215 | 0.16% | 0.13 | T1 (wage-tax limb MANUAL) |

## Plano de ondas sugerido
- **Onda 1 (top 10):** CA, TX, NY, FL, IL, PA, OH, NC, MI, GA
- **Onda 2 (11 a 25):** NJ, MA, VA, TN, IN, WA, SC, MN, AZ, WI, MO, CO, KY, MD, AL
- **Onda 3 (26 a 51):** CT, LA, OR, NV, KS, IA, UT, OK, AR, MS, NE, NH, ME, HI, DE, WV, ID, NM, DC, RI, SD, ND, MT, AK, VT, WY

Dentro de cada onda, começar pelos estados de tier mais baixo e deixar os T4 (camada local manual) para o fim. Reordenar quando o usuário trouxer a lista real de clientes ou a master list do BAU.
