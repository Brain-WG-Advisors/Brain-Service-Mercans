# Rascunhos — 3 tickets de reports da Lituânia (Gmail, sem destinatário, não enviados)

Base: [[CONFERENCIA]] desta pasta. Hub: [[Lituania]].

---

## 1. SAM (Sodra)

**Subject:** Lithuania – SAM (Sodra) report: implement per spec LT-SODRA-003 v1.0

Hi team,

Please implement the Lithuanian monthly social insurance report SAM, with annexes SAM3SD and SAM3SDP, as defined in the attached spec LT-SODRA-003 v1.0.

- Form version 07, FFData file defined by the Sodra MXFD sam-v07 (pages SAM, SAM3SD with 6 lines per page, SAM3SDP with 3 lines per page).
- Due by the 15th of the following month (Sodra SAM instruction, point 52).
- SAM3SD: income on which contributions are calculated (A11), the total rate applied at the start of the month (P3) and the contributions (A12), per insured person. SAM3SDP: special cases with period and reason code 01–10 (points 51.2 and 56).

The spec was re-checked on 27/10/2026 against the current Sodra instruction (points 48–56) and the sam-v07 form definition. All fields match.

Thanks,

---

## 2. GPM313 (VMI)

**Subject:** Lithuania – GPM313 (VMI) report: implement per spec LT-VMI-001 v1.1

Hi team,

Please implement the Lithuanian monthly income tax return GPM313 as defined in the attached spec LT-VMI-001 v1.1.

- Due by the 15th of the following month (VMI order VA-121 as amended by VA-105 of 20/11/2025, point 12).
- FFData file defined by the VMI MXFD GPM313 (version 1, EDS file version 31/12/2025). The XML field names are in column H of the spec (B_MM_ID, B_MM_Pavadinimas, B_ML_Metai, B_ML_Menuo, G5–G12), and the lengths are in column I.
- GPM withheld on employment payments is split by payment date: up to and including the 15th (G6) and after the 15th (G7) (points 9.2–9.3).

v1.1 updates only the electronic format (XML field names, field lengths, month without leading zero). The 2026 rules in v1.0 are unchanged. Changes are highlighted in light blue.

Thanks,

---

## 3. GPM312 (VMI)

**Subject:** Lithuania – GPM312 (VMI) report: implement per spec LT-VMI-002 v1.1

Hi team,

Please implement the Lithuanian annual income tax return GPM312, with annexes GPM312L (residents) and GPM312U (non-residents), as defined in the attached spec LT-VMI-002 v1.1.

- Due by 15 February of the following year (VMI order VA-9 as amended by VA-24 of 26/03/2026, point 57).
- FFData file defined by the VMI MXFD GPM312 (version 1, EDS file version 12/06/2026). Pages are GPM312, GPM312L (10 lines per page) and GPM312U (5 lines per page). The XML field names are in column H of the spec, and the lengths are in column I.
- 2026 changes in VA-24 that are already in the spec: income code 06 removed; new U7 marker "U"; 25% rate.
- Rates (L9/U9) come from the MXFD closed list, with 2 decimals.

v1.1 updates only the electronic format (XML field names, field lengths, lines per page, date format, rate list). Changes are highlighted in light blue.

Thanks,
