# CO-CCG-001 - rejected suggestions S86 and S87 (verbatim)

Source: Drive Google Doc CO-CCG-001_v1.2, export of 21 Oct 2026 ([[Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/base/CO-CCG-001_v1.2-gdoc-export-2026-10-21.docx|CO-CCG-001_v1.2-gdoc-export-2026-10-21.docx]]), Module 13 "Other prevalent non-statutory practices worth recording", row on the bonus. Tracked insertions by author "Claude". Both rejected (verdicts in `suggestions-verdicts-A.json`): they review one client's automation spec and client wage types, which is ticket / hub material, not CCG content. Not in CO-CCG-001 v1.3. Destination: `paises/Colombia.md` (ticket record HRBS-12487).

## S86 (inserted 2026-09-18, author Claude)

Reason for rejection: Out of CCG scope. It reviews one client's automation spec for one client wage type (a bonus) and gives build instructions for it, but the CCG states statutory rules and does not classify client wage types. The statutory points it relies on (flat 4%+4% on the monthly IBC, +1% FSP from 4 SMMLV, the Ley 1393 art. 30 40% limit, the ET art. 383 table) are already in the CCG and in S85. Record the finding in paises/Colombia.md / the HRBS-12487 ticket record instead.

Text as inserted:

> STRONGER WARNING for any automated build of this wage type (HRBS-12487, 18 September 2026): the client-side automation spec reviewed for this ticket applies an 8%/9%/10% bracket structure DIRECTLY TO THE BONUS AMOUNT before computing withholding (e.g. 9% x a bonus of 12,940,200 = 1,164,618 treated as 'SS'). This does not correspond to any real Colombian social-security mechanism -- contributions are a FLAT percentage of the employee's MONTHLY IBC (8% baseline, +1% FSP only when that month's TOTAL IBC reaches 4 SMMLV), never a graduated bracket applied to one isolated payment, and this bonus, when paid non-salary, stays out of the IBC except for any part of the month's non-salary payments above the 40% limit of Ley 1393 de 2010 art. 30. Built as specified, the engine would withhold social security not owed, THEN compute income-tax withholding on a base already wrongly reduced by that deduction -- one defect compounding into a second. The art. 383 progressive-table mechanics in the same spec (bracket boundaries, 28% rate, 10 UVT fixed value) ARE correctly transcribed; the error is entirely upstream, in treating the bonus as social-security-contributable at all. Build with NO social-security deduction on this wage type; add the bonus to the month's other labour income for ordinary depuration only.

## S87 (inserted 2026-09-18, author Claude)

Reason for rejection: Out of CCG scope. It names client wage types (WT 62837 bonus, WT 62838 becas) and decides how a client spec should book withholding; that is client wage-type classification and ticket closure. Move it to the country hub / ticket record.

Text as inserted:

> CLOSED, with the client-side spec file itself now reviewed (18 September 2026): the spec asks whether WT 62837 (the bonus) can carry the withholding as a separate deduction line instead of being netted down directly, for auditability. Given there is no bonus-specific social-security deduction on this wage type (only the part of the month's non-salary payments above the Ley 1393 de 2010 art. 30 40% limit, if any, enters the IBC at the ordinary flat rates), the build is simpler than the spec frames it -- 62837 stays at the GROSS bonus, with one deduction line for withholding tax only, computed under ordinary art. 383/388 depuration. The spec correctly excludes WT 62838 (becas/scholarships) from any deduction regardless of amount -- that exclusion is right and should be preserved unchanged.
