# Audit 2 change maps - build notes (2026-10-23)

These are proposals only. No xlsx was modified and make_final.py was not run. `02-client-reports-raw/` and `99-local-only/` were not opened.

## Maps written (`04-output/final-prep/<SPEC>-audit2-map.json`)
| Spec | Edits | Findings |
|---|---|---|
| CO-DIAN-001 | 30 | #7 extra (5 pointers/labels), #9 (18), #20 (5), #23, #25 |
| CO-DIAN-002 | 49 | #7 (19 annex + 28 extra), #9 (C38), #22 |
| CO-DIAN-004 | 31 | #7 (9 annex + 15 extra), #8 (C22), #9 (C38), #11 (C8, C32), #20 (M22, M73), #25 (M45) |
| CO-DIAN-005 | 24 | #7 (16 annex + 6 extra), #9 (C39), #20 (M28) |
| CO-PILA-003 | 36 | #7 (10 annex + 14 extra), #8 (C22), #9 (C39), #10 (M110), #20 (M93, M131, M138, M140-M145) |
| CO-CESANTIAS-006 | 54 | #7 (34 annex + 19 extra), #9 (C41) |
| CO-PILA-007 | 2 | #24 (C18, Report Matrix A35) |

`current` = exact cell text of `05-final/` (read with openpyxl); every replacement was asserted against it.

## How #7 was sourced
- The glossary swap is already in `01-specs/`, so the kit history holds no clean wording. The pre-glossary text was taken from the pipeline workbooks `Research Pipeline/Colombia/CO-compliance/04-reports-spec/*-v1.x-DRAFT-MINOR07.xlsx` (same cell, matched by similarity; generators `co_r*.py` hold the same strings).
- Each restored quotation was then checked against the official text: Form 350 instructivo (`CO-compliance/_txt/form350.txt`), Form 220 (`_txt/form220.txt`), Res. DIAN 000227 de 2025 (`_txt/res227.txt`), AT2 v30 PDF, the Simple S.A. / SOI layouts, the MinTrabajo draft decree and Ley 2466 de 2025.
- Where the pre-glossary quotation itself was not verbatim, the official text was used. Cells affected:
  - 350 M42 (adds the parentheses '(Pagos o abonos en cuenta)' / '(Tarifa (%))');
  - Cesantías C25 / M28 / C8 (adds 'Corresponde al');
  - Cesantías M40 (adds 'ocho punto treinta y tres por ciento');
  - Cesantías M42 / B64 ('-PILA' and 'deberan reportarse');
  - Cesantías M46 ('se entregara').
- PILA-003 M68 lists the full AT2 v30 sub-type labels.
- Accents are dropped, as everywhere else in the specs.
- **Extra cells:** about 80 cells outside the annex had the same defect. They were found by scanning the 7 finals and are included, marked "outside the audit annex list". They cover:
  - literal option values (350 SIN/CON CONVENIO, Persona natural/juridica);
  - Field Options pointers;
  - mixed labels such as 'Tipo de document' and 'Code del Severance-savings fund';
  - quotations (350 D42, PILA M4 / M42, Cesantías B9 / D9).
- English renderings of labels that are fully English (e.g. 220 'Salary payments') were left as they are, except 220 File Structure B11 / B13 / B14 / B16, PILA B37 and 2276 B10, which were restored whole because they mixed Spanish and English.

## Could not source / judgement calls
1. **PILA-003 M93 (Ley 776 de 2002 art. 3):**
   - The Secretaría del Senado page refused the connection, and the FuncionPublica and normograma URLs returned 404.
   - The text used is the transcription in Corte Constitucional C-543/2007 (local file).
   - 'From day one' was changed to 'from the day after the accident', as the statute says.
2. **PILA-003 M131, 8.7% maximum:** not legible in the local Decreto 1072 copy (the maximum column is missing). It is kept on the Decreto 1772 art. 13 citation already in Field Options A165-D170.
3. **PILA-003 M145 (MEN 1%):**
   - The SENA copy of Ley 21 art. 11 prints ESAP 1/2% (num. 3) and Escuelas Industriales 1% (num. 4).
   - The FuncionPublica copy shows num. 3 as modified by Ley 812 de 2003 art. 87, with 1/2% for the Escuelas Industriales.
   - The rate is not confirmed. It only affects a zero-filled public-sector field.
4. **NE M48 and M51:** the cited 'art. 5 item 11' is the generation date and time. No mandatory-content item covers the employer country or address, so the citation is deleted and nothing is invented.
5. **NE item numbers corrected** while replacing the article numbers: M46 item 1 → 2; M58 item 2 → 3; M76 item 5 deleted (it is the consecutive number); M212 item 8 dropped.
6. **NE M152:** 'fully in the contribution base' is replaced by Decreto 780 art. 3.2.5.1. Contributions for paid leave are due on the last IBC before the leave, not on the leave pay.
7. **#28:** no spec part. The process word is only in CCG P835 and the DD (out of these maps).
8. **#8 scope:** only C22 in PILA-003 and 220 was changed. Rows 17 / 45 of PILA-003 were not changed.

## Found while working, not changed (for Wallisson)
- PILA-003 M92 cites Decreto 1072 art. 2.2.4.2.5.6 for 'the class attaches to the work centre'. That article covers contribution and payment periods for contractors. The work-centre rule is art. 2.2.4.3.9, which the M131 proposal uses.
- 2276 Field Options heading cites 'Res. 227 art. 1.30.7.1.1'. The article is 1.3.7.1.1.
- PILA-003 M68 says 'Twelve-value list', but the annex lists 11 values (0-6, 9-12). The English text was left unchanged.
- 220 Payroll Scope Summary A32 and M51 still say 'rolling six-month average'. M51 was not to be changed.
- NE Report Matrix A43 'QR of at least 2 cm on EVERY page' is not in Res. 227 art. 1.5.3.8.3. Only the article numbers were changed.
