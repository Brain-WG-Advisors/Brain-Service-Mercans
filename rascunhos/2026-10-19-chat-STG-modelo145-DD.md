# Chat STG Spain — Modelo 145 × DD (rascunho, não enviado)

> Frente Pipeline, 2026-10-19, a pedido da janela geral; versão objetiva reescrita pela janela geral (19/10). O usuário envia no chat.
> Base: `Research Pipeline/Spain/2026-10-19-modelo145-x-DD/matriz-modelo145-x-DD.md` (fontes em `raw/docs/oficiais/ES/2026-10-19-*`).
> DD: `Spain_Data_Dictionary_V5.0.xlsx`.

---

Hi Nihita,

I checked every box of Modelo 145 against the Data Dictionary. A box only needs a field if payroll uses it to calculate IRPF withholding or to report Modelo 190.

**Result:** most boxes were already covered. 8 were missing and are now added in DD V5.0 (shared Drive > Spain > 02 - DD, rows in light yellow), under Employee Tax Relief Declaration:

1. **Spousal Compensatory Pension (annual amount)**: reduces the withholding base (RIRPF art. 83.3.f).
2. **Child Maintenance Annuities (annual amount)**: changes how withholding is calculated (RIRPF art. 85.2).
_Note: these two are not the existing garnishment wage types (e.g. 21920 Child Support), which only deduct from net pay. They hold the annual amount the employee declares on Modelo 145, even if paid outside payroll._
3. **Home Loan Deduction (flag)**: home bought before 2013 with a loan; reduces the withholding rate by 2 points (RIRPF art. 86.1).
4. **Irregular Income Reduction Not Applied (flag)**: allows payroll to apply the 30% reduction again, which payroll already calculates (WT 58161) (RIRPF art. 83.3.a).
5. **Child 1-4 - Adoption/Foster Year**: extra EUR 2,800 for 3 years after adoption, at any age (LIRPF art. 58.2).
6. **Ascendant 1-2 - Cohabitation Count**: the ascendant allowance is split among the relatives they live with (LIRPF art. 61).
7. **Geographic Mobility - Relocation Date**: the benefit applies only in the year of the move and the next one, so Yes/No alone is not enough (LIRPF art. 19.2.f).
8. **Child 5 to Child 16** (same fields as Child 1-4): the law has no limit on children (EUR 4,500 each from the 4th, LIRPF art. 58.1); 16 is the maximum accepted by the AEAT withholding service.

**Not needed as fields:** place, date and signatures. The employer only has to keep the signed form, which can be electronic (RIRPF art. 88.1).

**Open question:** ESS access. The DD sets this group as ESS = Read. If employees fill it in through ESS, should it be ESS = Write?
