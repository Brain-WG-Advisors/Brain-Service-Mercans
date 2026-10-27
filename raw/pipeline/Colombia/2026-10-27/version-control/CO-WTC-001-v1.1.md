# CO-WTC-001-v1.1.xlsx

> Só o Version Control. Origem: `~/mercans-pipeline/CO-compliance/02-wtc/CO-WTC-001-v1.1.xlsx` (2026-09-24, md5 `c120b88451657fe0b27a36e4b07ccea0`). Coleta 2026-10-27, F6 Passo 2.

### Aba `Version Control` (10 linhas)

|  | Wage Type Catalogue |  |  |  |  |
|---|---|---|---|---|---|
|  | Colombia (CO) |  |  |  |  |
|  | Version | Effective Date | Change Description | Status | Updated By |
|  | 1 | 2026-09-04 00:00:00 | Initial Colombia Wage Type Catalogue for FY2026. All 300 global baseline codes configured fresh for Colombia (CST arts. 127/128 salary classification, the THREE separate bases, the Ley 1393/2010 40% clamp, the ET art. 114-1 exoneration cliff, the ET art. 388 depuration and the art. 383 table) plus 102 Colombia-specific wage types. Social-insurance column expanded into five per-fund columns (Salud / FSP / ARL / Parafiscales / Pension) and three Colombia-specific base columns added (salary flag / statutory-benefit base / vacation base). Includes the Global WTC Coverage sheet and the Form Reference Guide (C17); every tax code defined and sourced to a Colombian authority publication (C9). Wage-type code numbers for Colombia-specific rows are DERIVED (no Mercans code range has been assigned for Colombia). | Released | Mercans Compliance (build_co_wtc.py) |
|  | 2 | 2026-09-18 00:00:00 | SUPERSEDED -- CZ template residue. This row was inherited unedited from shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx row 14 during the initial Colombia build and never carried genuine Colombia content (original text: 'Wage codes Mapping', dated 2025-09-09, author Devshree Vyas -- confirmed identical to the Czech source). Corrected here rather than silently deleted, per CO-QA-REPORT.md MINOR-01, so the version sequence and audit trail stay intact. | Corrected | Devshree Vyas |
|  | 3 | 2026-09-18 00:00:00 | HRBS-12487: added CO-PRIMA-VACACIONES-EXTRALEGAL (row 317), the extra-statutory vacation bonus under a written CST art. 128 non-salary pact, as a directly-discoverable named entry carrying the same treatment as CO-BONIF-NOSALARIAL (row 316, cross-referenced both ways). Confirms no statutory 95-tax-unit threshold exists for vacation bonuses; the figure is simply the ET art. 383 table's zero-rate ceiling. | Released |  |
|  | 4 | 2026-09-18 00:00:00 | Post-handover artefact-alignment pass (MINOR-01, MINOR-09 from CO-QA-REPORT.md). MINOR-01: row 14 (above) corrected from uncleaned CZ-template residue to an honest superseded-content note. MINOR-09: Global WTC Coverage row 28 (CO-TX-08) annotated to state it is a residency-driven overlay applied via column P, not a per-wage-type assignment -- zero rows carrying the code is therefore expected. | Released |  |
|  | Business Analyst |  |  |  |  |
|  | Regulation Analyst |  |  |  |  |
| Note: The empty columns are not required as part of country configuration. |  |  |  |  |  |

