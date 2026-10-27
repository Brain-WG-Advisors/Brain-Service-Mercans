# Loon-in or loon-over — the determination gate

Read this before running any period-integrity test. The two systematieken give
**opposite** answers on the same file, so getting this wrong does not produce a
smaller error — it produces a confident error pointing the wrong way.

This skill does not decide the question. It gathers the evidence, states the
unresolved point, and hands the decision to the reviewer.

## The two methods

**Loon-in** is the hoofdregel. Wage becomes wage at the genietingsmoment, which
is the moment of payment. A nabetaling is declared *in de aangifte over het
aangiftetijdvak waarin u de nabetaling doet*, using the same nummer
inkomstenverhouding and the same begin and end dates as before. Retro paid in
period 9 is period 9 wage.

**Loon-over** puts the genietingsmoment in the tijdvak in which the employee
earned the wage. Retro is allocated back to the originating periods, fresh wage
calculations are made for those periods, and the earlier declarations are
corrected. Handboek, §9.2.1.

## Conditions for loon-over

The Handboek permits loon-over only where all of the following hold:

1. **Same calendar year.** The wage relates to an earlier tijdvak in the same
   kalenderjaar. Loon-over does not apply across the year boundary.
2. **Bestendige gedragslijn.** A consistent practice, satisfied by any of:
   - it was already usual in prior years to declare nabetalingen in the period
     they relate to;
   - the employer has taken into use payroll software built only on the
     loon-over systematiek;
   - the employer is changing systematiek with the intention of keeping to it.

   The consistency requirement also covers processing: wage relating to earlier
   tijdvakken in the year is handled the same way **for all employees**, with
   new wage calculations made for those periods.
3. **Correction filed alongside.** Where the earlier tijdvak has already been
   declared, that declaration is corrected, and the correction is sent
   **together with** the return for the period in which the nabetaling is made.

The Handboek's own examples are a monthly wage always paid in the following
month, and a retrospective individual or CAO pay rise within the same year.

## The carve-out that has to be resolved

In the same section the Handboek states that where a payment, or part of it,
relates to a tijdvak of **2025 or earlier**, that payment must always be treated
under the hoofdregel — as wage of the tijdvak in which it is paid — **even where
loon-over is otherwise applied**.

Read literally in the 2025 edition this points the opposite way from the rest of
the section, and it is capable of reversing the whole determination for a 2025
pack.

**Do not resolve this from the Handboek text alone.** Check paragraphs 9.2.1 and
9.3.5 in full, and put the question to the client's Dutch tax counsel or to the
Belastingdienst. A material restatement resting on a paragraph that reads both
ways is the thing to settle before filing, not after.

Until it is resolved, period-integrity results are reported as **not tested —
systematiek unconfirmed**. Never as a pass.

## Evidence to gather from the pack

Assemble these and present them with the determination:

| Signal | Points to |
|---|---|
| Correction blocks filed alongside the period return | loon-over (condition 3) |
| Every `Inkomstenperiode` in the period block dated to the period start | loon-in behaviour in the period block |
| Period block total equals current-period payslips only | loon-over |
| Period block total equals current period **plus** retro | loon-in behaviour |
| Correction saldi equal the retro tax plus employer premiums on the retro base | the retro is being declared in the correction blocks |
| Payroll engine documented as loon-over only | bestendige gedragslijn satisfied |

**The diagnostic that matters most:** if the period block carries the retro
**and** the correction blocks carry the same retro, the engine is applying
loon-in on one side and loon-over on the other, and the same wage is declared
twice. That is a finding whichever systematiek is ultimately correct — only the
direction of the remedy changes.

## The two period tests

Once the reviewer confirms, run the matching test and only that one.

**Under loon-in**

- Period block should equal current-period payslips **plus** retro paid in the
  run.
- No correction block should exist for a prior period merely because retro
  relating to it was paid now. A correction is for an error in the earlier
  declaration.
- Remedy for a duplicate: withdraw the correction blocks.

**Under loon-over**

- Period block should equal current-period payslips **only**.
- Retro sits in correction blocks against the originating periods, filed with
  this return.
- Remedy for a duplicate: restate the period block to current-period figures.

## Quantifying the duplicate

Where a transaction-level retro export is available, the arithmetic closes
exactly. Split the pay elements by originating period, then:

```
retro loonheffing        = sum of tax elements tagged to prior periods
retro SV base            = sum of the SV base element tagged to prior periods
expected employer premium = retro SV base x (Aof + Wko + AWf + Zvw + Whk)
```

The correction saldi should equal `retro loonheffing + expected employer
premium`. On a real P09 pack this reconciled to within €162 on €292.921 — the
residual being the AWf hoog/laag mix. If it reconciles, the correction blocks
are entirely the retro and nothing else is hidden inside them.

## What to record

On the Assumptions sheet, state: which systematiek was confirmed, by whom, on
what basis the bestendige gedragslijn is satisfied, and whether the 2025
carve-out has been resolved and how. A €448k restatement needs that line, and a
lawyer will look for it first.
