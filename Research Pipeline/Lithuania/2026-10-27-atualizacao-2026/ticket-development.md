# Rascunho — ticket para o Development (Lituânia, regras de 2026)

Status: **gravado como rascunho no Gmail em 27/10 (sem destinatário, com os 4 arquivos anexados), não enviado.** No Gmail o texto diz "attached" em vez do caminho do Drive. Base: [[CONFERENCIA]] desta pasta. Hub: [[Lituania]].

---

**Title:** Lithuania – implement 2026 statutory rules (CCG 2026, Alert 2026, WTC V3.1, DD V3.1)

**Description:**

Hi team,

Please implement the 2026 rules for Lithuania, effective from 2026-01-01. The current build still uses 2025 rules.

Updated compliance artifacts (Drive › Country Folders › Lithuania):
- 05 - Payroll Regulation Guide › 2026 Regulation guide › Lithuania Payroll Regulation Guide_2026.docx
- 09 - Alerts › 2026 › Lithuania_Changes in Tax Rates & social security Rates - 1st January 2026
- 03 - WTC › Lithuania WTC V3.1
- 02 - DD › Lithuania Data Dictionary V3.1

Changes are highlighted in light blue in each file.

**Income tax (GPM)**
1. Annual brackets: 20% up to €83,237.40; 25% from €83,237.40 to €138,729; 32% above €138,729 (36 and 60 × VDU €2,312.15). By default, the rates apply by reference to each payment on its own (in practice 20%). On the employee's request, they apply by reference to the total annual payments from the employer (DD field Elective Tax Rate).
2. NPD: single monthly formula, NPD = €747 − 0.49 × (monthly employment income − €1,153), with a minimum of 0. NPD is €747 up to €1,153 and zero above €2,677.49. The former formula (€400 − 0.18 × (income − €642)) no longer applies. Reduced capacity: €1,127 (0–25%) and €1,057 (30–55%).
3. Employer-paid voluntary health insurance premiums are non-taxable up to €350 per year. This sits within the 25% annual employment income cap shared with life insurance and pension contributions. Only the excess is taxable (WTC 65630; wording also updated on 23610, 65810 and 65835).

**Social security (Sodra)**
4. Minimum monthly wage: €1,153. If monthly pay is below it, the employer also pays, at its own cost, the employee and employer Sodra contributions on the difference (exceptions apply; I-1336 art. 10(7)).
5. Annual ceiling of the social insurance base: €138,729 (60 × VDU). The ceiling does not apply to health insurance (PSD).
6. Accidents at work, Group II: 0.49% (Group I 0.14%, III 0.7%, IV 1.4%).
7. Employee 12.52% (8.72% + 1.99% + 1.81%); unemployment 1.31% (fixed-term 2.03%).

Sources: Law on Personal Income Tax IX-1007 (arts. 6(1), 17(1)(14)/(14¹), 20, 23(7), as amended by XV-343); Law XV-632 (arts. 3 and 4); Law on State Social Insurance I-1336 (art. 10(7) and 10(9)); Government Resolution No. 700 of 16.10.2025.

Thanks,
