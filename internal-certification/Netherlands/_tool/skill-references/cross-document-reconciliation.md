# Cross-document reconciliation methodology

The order below matters. Each step either resolves a finding cleanly or tells
you exactly which additional data to ask for. Work through it in sequence.

## Contents

- 0. Load everything with pandas/openpyxl, never by eye
- 1. Period integrity — run this first, after the systematiek gate
- 1a. Retro reconciliation
- 2. Headcount reconciliation across every document
- 3. Payslip is the anchor
- 4. Employer premium recalculation
- 5. Internal consistency of the return
- 6. Indicator consistency across documents
- 7. Cumulatives
- 8. Payments and ledger
- 9. Gross-to-net presentation
- 10. Transaction-level ground truth
- 11. What not to fabricate
- 12. Structural XML validation caveats

## 0. Load everything with pandas/openpyxl, never by eye

Real payroll exports are not plain CSVs. Expect:

- A 6–10 row metadata header block (Organization, Country, Period, Total
  headcount, Report generation date) before the real header row. Locate the
  real header row with `header=None, nrows=15` first; never assume `header=0`.
- Legacy `.xls` files — read with `engine='xlrd'`.
- Employee ID columns coming back as floats (`10000110.0`). Normalise with
  `.astype(str).str.replace(r'\.0$', '', regex=True)` before any join.
- Footer rows such as `Confidential` or `GRAND TOTAL` sitting in the Employee ID
  column. Filter these before counting headcount or summing anything.
- Headcount stated in the metadata block that differs from the row count —
  usually multiple income relations per employee, or effective-dated duplicates.
  Resolve rows to IKVs before reconciling to the XML nominative count.

## 1. Period integrity — run this first, after the systematiek gate

This is the highest-value test and the one most often skipped, because a pack
can be internally consistent and still declare the wrong period.

**Do not start until `systematiek-determination.md` has been worked through and
the reviewer has confirmed loon-in or loon-over.** The two give opposite answers
on the same file. Under loon-in the period block should carry current-period
wage plus retro paid in the run; under loon-over it should carry current-period
wage only, with retro in the correction blocks. Running the wrong test produces
a confident conclusion pointing the wrong way, and a remediation instruction
that creates a larger error than the one it fixes.

Until confirmed, report period integrity as not tested.

1. From the payslips, take only the payslips for the period under review. For
   each, read the fiscal wage and the withheld loonheffing. Total them.
2. From the loonaangifte, read the collective `TotLnLbPh` and `IngLbPh` of the
   **`TijdvakAangifte`** block — not the `TijdvakCorrectie` blocks.
3. From the gross-to-net, total gross wage and the withheld tax elements.
4. Put the three side by side. They should state the same fiscal wage.

If the return is higher than the payslips, test whether it equals the sum of
**every** payslip in the pack across **all** periods. Do this per employee as
well as in total. If it matches the all-period sum for nearly every employee
and the current-period figure for only a minority, the period block is carrying
back-pay for earlier periods.

Then check whether those same earlier periods **also** appear as
`TijdvakCorrectie` blocks in the same file. If they do, the same wages are
presented twice in one return.

**Whichever systematiek applies, wage in both places is a finding.** If the
period block carries the retro and the correction blocks carry the same retro,
the engine is applying loon-in on one side and loon-over on the other. Only the
direction of the remedy depends on the determination. **Do not treat
multi-period content as the explanation that clears a difference.** A correction run may legitimately bundle restated prior periods
alongside the current declaration — but that is a hypothesis to test, not a
conclusion. Verify that the collective totals equal the sum of the
*current*-period blocks only, and verify that nothing appears in both the period
block and a correction block. Double presentation is a real defect and it looks
exactly like a legitimate bundle until you check.

`SaldoCorrectiesVoorgaandTijdvak` gives the net change per historical period.
Check each date range against the tijdvak table in `codes-2025.md` — they must
be genuine period boundaries of the same year. Flag any saldo dramatically
larger than the others in the series as needing a root cause, not necessarily
as an error.

Report the three figures, the difference, and the per-employee match counts.

## 1a. Retro reconciliation — the arithmetic that settles section 1

Where a transaction-level pay-element export is available, period integrity
stops being an inference. The export tags each element with the period it
originates from, so split it and reconcile.

```
retro loonheffing         = tax elements tagged to prior periods
current loonheffing       = tax elements tagged to the current period
retro SV base             = SV base element tagged to prior periods
current SV base           = SV base element tagged to the current period
```

Three ties to test:

1. `current + retro` SV base equals the declared `TotLnSV`. If it does, the
   period block contains the retro.
2. `current + retro` loonheffing equals `IngLbPh`.
3. The correction saldi equal `retro loonheffing + retro SV base x combined
   employer premium rate` (Aof + Wko + AWf + Zvw + Whk). If it reconciles, the
   correction blocks are entirely the retro and nothing else is inside them.

On a real P09 pack this closed to within €162 on €292.921, the residual being
the AWf hoog/laag mix. Getting that residual below about 1% is what turns the
finding from an assertion into arithmetic, which is what a legal reader needs.

Watch for three things in the export itself: rows tagged to **future** periods,
negative retro on special-rate tax, and a negative SV base on retro — each is a
separate observation.

## 2. Headcount reconciliation across every document

Build the set of employee IDs in each document — G2N, GL, SEPA `EndToEndId`,
loonaangifte `PersNr`, master file, payslips — and diff them pairwise. Explain
every gap with named employees and a reason, never as a bare count.

- Paid in G2N but **absent from the loonaangifte**: a compliance gap. Always
  flag, whatever the amount.
- Paid but **absent from SEPA**: check G2N net pay first. Negative net pay is
  correctly absent from an outgoing batch. Zero net is also fine. Only a
  **positive** net missing from SEPA is a concern.
- In G2N but **absent from the master file**: check for a termination date.
  Leavers absent is often legitimate; an active employee with real pay and no
  master record is a data-completeness gap.
- **Present last period, absent now, with no reden einde code**: this is the
  test that catches a silently dropped employee. L2501 covers the case where an
  end date exists without a reason code; nothing covers a disappearance with
  neither, so it has to be caught here by diffing against the prior period.

## 3. Payslip is the anchor

Two files agreeing with each other is not evidence that either is right. In a
real P09 pack the gross-to-net and the return agreed exactly on a figure that
neither the period nor the payslips supported.

Check against the payslips, not only between files.

For every employee, compare the return's `LnLbPh`, `IngLbPh` and `LnTabBB`
against that employee's payslip. Report how many match exactly and list every
one that does not, with the difference.

Related rule: **do not use one field under test to judge another.** AOW status
comes from the date of birth, never from `IndWW` or `IndWAO` — those indicators
are themselves under test and have been wrong in real packs.

And: **a correction applied to one file is not a correction.** If the return was
edited but the payslips were not regenerated, say so and name the employees
where the two now disagree. Compare the new payslip PDF against the previous one
before accepting that anything was fixed.

## 4. Employer premium recalculation

For every income relation in the period block, recalculate each premium from its
own declared premium wage and compare with the declared premium. Rates and field
names are in `rates-2025.md`.

Then, separately:

- Report every income relation that declares a premium wage above zero with a
  premium of **zero**, and total that premium wage. Controls L2341–L2343,
  L2401–L2405 and L2268 cover Aof, AWf and Ufo. **There is no equivalent control
  for Whk** — see `controls-2025.md`.
- For Whk specifically, derive the rate the employer actually applies from the
  records that do carry a premium, then test every record against it. Label the
  derived rate **inferred, not verified** unless the beschikking is supplied.
- Check the gross-to-net for the mirror image: if the same amount appears as an
  employee deduction with the employer element at zero, the premium is being
  recovered from employees. Under art. 20 Wfsv the premium is owed by the
  employer and declared in full whatever is recovered; recovery is limited to
  half the WGA component, taken from net pay (art. 34(2) Wfsv, art. 3.18
  Regeling Wfsv). Report the shortfall in euros.
- Before raising anything on Aof laag versus hoog, check the employer size test
  in `rates-2025.md`. An entire population at Aof hoog is correct for a large
  employer.

## 5. Internal consistency of the return

1. Every collective total must equal the sum of the nominal records for the same
   field, in the period block. Test **all** of them and cite the rubriek's own
   poortcontrole number.
2. `TotGen` must equal `TotTeBet` plus the sum of the
   `SaldoCorrectiesVoorgaandTijdvak` entries.
3. Check each income relation's code loonbelastingtabel against the employee's
   actual pay frequency and table colour using the composition rule in
   `codes-2025.md`. Report any value that does not match and say what it means.
4. Report any negative amount in a collective field.

## 6. Indicator consistency across documents

The principle: a calculation applied in one deliverable must be reflected in the
indicator carried by every other. Run these per employee:

| Logic applied | Must agree across |
|---|---|
| Loonheffingskorting | payslip LH/LHK field, `IndLhKort`, master data tax-credit flag |
| Insured for WW / WAO | payslip ZVW/WW/WIA field, `IndWW` / `IndWAO`, date of birth |
| AWf laag versus hoog | contract indicators J-J-N, the aanwas fields, the declared premium |
| Zvw situation | `CdVerzSitZvw`, `IngBijdrZvw`, `WghZvw`, tabelcode |
| Table colour | master data tax method, second digit of the tabelcode, arbeidskorting presence |
| Bijzondere beloning rate | payslip percentage, uploaded override file, jaarloon, DOB, AOK flag |

Every row above maps to one or more official controls — see
`controls-2025.md` for the numbers to cite.

## 7. Cumulatives

Read the cumulative block at the foot of each payslip and test three things:

1. Cumulative at period N = cumulative at N−1 + the period N movement, per
   employee, per column. This is the test most often omitted.
2. Cumulative withheld loonbelasting/premie volksverzekeringen per income
   relationship may not be negative. Report any that are.
3. Cumulative fiscal wage may not be negative. Report any that are.

Sub-totals within the payslip must sum to the stated totals, and the stated
totals must agree with the G2N row for the same employee and period.

## 8. Payments and ledger

1. SEPA: `NbOfTxs` and `CtrlSum` in the group header must equal the number and
   sum of the transactions. The control sum should equal the sum of the
   **positive** net pay in the G2N; list employees with a negative net
   separately, as they are correctly excluded.
2. The payment report total must equal the SEPA control sum.
3. The GL must balance debit against credit — but that is nearly vacuous on a
   generated journal. The test that matters is **mapping**: each wage type to
   its GL account per the pay-elements file, and each account total back to the
   corresponding G2N subtotal.
4. Report the SEPA requested execution date against the period end date.

## 9. Gross-to-net presentation

1. Test `gross − total deductions = net` on every row. Where it fails, check
   whether the difference equals the bijtelling columns; that explains it but
   remains a presentation issue the client will query. List anything not
   explained that way.
2. List every employee with a negative net, and every one shown as 0,00 where
   the columns compute a non-zero net.
3. State explicitly whether the G2N covers the period only or the whole payroll
   run including earlier-period recalculations. **Prove it**: pick one employee
   with back-pay, total their payslips across all periods in the pack, and
   compare with their G2N row.

## 10. Transaction-level ground truth

If discrepancies do not resolve from the documents provided, ask for a
transaction-level pay-elements or retro export before guessing which document is
right.

When using one, match retro accounts to the G2N's own column codes **by exact
numeric prefix** (`62100` for `62100 - Basic Salary`), not by a broad
account-number range. Retro exports include notional rate-reference accounts
("Overtime & Leave rate", "Parental leave rate 70%") that echo the basic salary
figure for internal calculation purposes and are not separate earnings.
Including them overstates gross by a large and confusing margin.

## 11. What not to fabricate

Finding an error and being asked to fix the file are different asks with
different risk.

**Two rules before writing any instruction**

*Split corrections that move in opposite directions.* Removing a wrongly
applied cap increases a figure; reallocating retro decreases it. A single net
number hides both and destroys the audit trail.

*A value absent from a master extract is not by itself a defect.* Test the value
that drove the calculation. An extract gap is a data question unless a
calculation depends on it.

**Safe to correct directly**

- A SEPA/pain.001 file, where you have the missing employee's IBAN from a
  reliable source and the correct amount. Flag any field you inferred — a BIC
  derived from the IBAN bank code, for instance — for the client to confirm
  before payment executes.
- A specific, well-evidenced field in a data export, where transaction-level
  ground truth confirms the exact correct value.

**Not safe to overwrite silently**

- **GL exports.** A real fix is a journal entry and you likely do not know the
  offsetting account. Provide a correction schedule — old value, correct value,
  net adjustment — for the client's accounting team to post.
- **Loonaangifte XML.** This is a government filing. An error found after filing
  needs a correctiebericht, not a quiet edit. Give the client the employees and
  amounts to correct through their own process.
- **Payslips.** You cannot faithfully reproduce the client's template. A
  best-effort recreation risks looking official while being wrong. Name the
  employees needing a reissue from the payroll system.
- **Payment and reconciliation reports** carrying system-generated reference
  numbers you do not hold. Do not invent one. These regenerate from the source
  system once the underlying batch is corrected.

## 12. Structural XML validation caveats

Check the namespace year before trusting any structural result:
`xml.belastingdienst.nl/schemas/Loonaangifte/<year>/01`. A validator built for a
different belastingjaar silently fails to match anything and returns an empty,
falsely clean result.

The XSD itself is not published. It is distributed through the Belastingdienst
ODB/OSWO channel and needs an ondersteuningsabonnement. Where the XSD is not
available, structural validation here is **spec-based, not schema-based** —
field presence, format and code lists tested against the gegevensspecificaties
and the codes document. State that limitation in the report rather than implying
a schema pass.

The official online validator at vts.belastingdienst.nl requires
organisation-specific OSWO credentials and cannot be used from here. It is also
a developer test facility: putting a client's production return with real BSNs
through it is a data-protection decision, not a technical one. Direct the client
to it rather than attempting to submit on their behalf.
