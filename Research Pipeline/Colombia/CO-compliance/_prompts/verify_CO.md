# INDEPENDENT LEGISLATION AUDIT — Colombia (CO) PAYSLIP, FY2026

You are an independent compliance auditor. A payslip generator was built for
Colombia. Your job is to VERIFY it against primary-source Colombia payroll
legislation for FY2026 — do NOT trust the payslip's own numbers; reverify each
one against an authoritative source via web search.

## STEP 1 — Extract everything from the payslip

Open with openpyxl (data_only=True):
  /c/Users/Wallison Gomes/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx

The visual payslip lives on two sheets: "Colombia (EN)" and "Colombia (ES)". Read both. Also verify the local-language sheet is genuinely translated (no leftover English labels).

Also read these sheets: "Payslip Spec 1", "Field Option", "Population Range",
"UnitRate Account Details".

Extract into a list every: earning line, deduction line (employee), employer
contribution line, every rate/percentage, every ceiling/floor/threshold, the
minimum wage, every legal citation (law/article/decree number), and the
worked example numbers (gross → deductions → net; employer cost).

## STEP 2 — Research the REAL FY2026 legislation

Web-search primary/authoritative sources for Colombia. Hints on what to check
and where: Ley 100 de 1993 (salud 12.5%/pension 16%); SMMLV 2026; auxilio de transporte; ARL Decreto 1295; parafiscales SENA/ICBF/Caja; retencion en la fuente UVT DIAN

For EACH of the following, find the current FY2026 value from an authoritative
source and cite it:
- Income tax: system type, rate(s)/brackets, standard deduction/allowance
- Each social security / payroll contribution: employee rate, employer rate,
  ceiling/floor, administering authority
- Any additional mandatory payroll tax (levy, solidarity contribution, etc.)
- Minimum wage (FY2026)
- Statutory leave basics (annual, sick — who pays which days, maternity)
- Payslip legal requirement (which law/article; what must be disclosed)
- Correct local identifiers (employer registration number; employee tax ID)

Prefer government sites and reputable tax/payroll references. Note the date of
each source. If FY2026 figures aren't published yet, say so and note the most
recent confirmed figure.

## STEP 3 — Compare and report

For every item, mark:
- **MATCH** — payslip value equals the verified primary-source value
- **MISMATCH** — payslip value differs from the verified value (state both,
  cite the source, and say which is correct)
- **UNVERIFIABLE** — you could not find an authoritative FY2026 source (say so;
  do not guess)
- **STALE** — payslip uses a prior-year value that has since changed

Pay special attention to:
- Wrong tax rate or bracket
- Wrong social security rate, ceiling, or split between employee/employer
- A contribution shown as an employee deduction when it is employer-only
  (or vice versa)
- Wrong minimum wage
- Wrong or fabricated law/article citation
- Any [VERIFY WITH RA] flag left in the payslip — check whether you can now
  resolve it, and give the resolved value
- Structural: 7 or 8 sheets correct, Mercans logo present, no Spain/Mozambique
  residue (note: local-language institution names like "Seguridad Social",
  "IRPF", "Nómina" ARE legitimate for Spanish-speaking countries — do not flag
  those as residue; only flag genuine Spain-specific leakage like Spanish tax
  brackets, "Beckham Law", "Solidarity Quota", NIF/CIF where the country uses
  a different identifier)

## OUTPUT

Write a markdown report to:
  /c/Users/Wallison Gomes/mercans-pipeline/CO-compliance/07-qa-crosscheck/CO-PAYSLIP-VERIFICATION.md

Structure:

```markdown
# Colombia (CO) Payslip — Independent Legislation Verification

**Audited:** <date>
**Overall verdict:** PASS | PASS WITH NOTES | FAIL
**Critical issues (count):** N

## Verification table
| Item | Payslip value | Verified value | Source | Result |
|---|---|---|---|---|
| Income tax rate | ... | ... | ... | MATCH/MISMATCH/... |
| (one row per rate/threshold/citation checked) |

## Critical issues (must fix before handover)
[Each real MISMATCH or fabricated citation, with the correct value + source.
 If none, write "None."]

## [VERIFY WITH RA] items — now resolved
[For each flag the payslip left, give the resolved value + source, or say it
 remains unverifiable and why.]

## Structural check
- Sheets: <list — correct order?>
- Logo present: yes/no
- Residue (genuine Spain leakage only): none / <list>
- Local-language sheet genuinely translated: yes/no/NA

## Wage-type codes
Real (from WTC) or placeholder "XXXXX -"? [note it — placeholder is expected
where no WTC existed and is NOT a failure, just flag for later patching]

## Sources consulted
[list with dates]
```

## FINAL LINE

Print exactly one line to stdout as your very last output, in this format:
VERDICT: <PASS|PASS WITH NOTES|FAIL> | CRITICAL: <count> | <one-sentence summary>
