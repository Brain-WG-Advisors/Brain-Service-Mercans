# ASSUMPTIONS — Colombia design v2.0

## Engine semantics (not confirmed in the production engine; each is a switch or a rule in the engine)

```
S1  Order: regulations run by ascending ordinal; each reads the balance of every account posted so far (inputs, flags,
    WTC-row amounts, 58xxx results of earlier regulations).
S2  Matrix (taxabilityRules): exact account rules only (Colombia has no Mercans codes yet, so no wildcard pattern); isTaxable
    true = in, false or absent = out. Signed sum; the final base is never below 0.
S3  A regulation that has a matrix and whose matrix base is 0 does not execute (SKIP_ZERO_BASE). A regulation without a
    matrix always executes (its formula reads accounts).
S4  Bands: floorAmount / ceilingAmount are not used by this design (limits are written inside the formula, as the Dev does
    inside MIN()).
S5  Flat: $band_amount_raw = base x rate / 100, the rate from employeeRate / employeeRateAccount (employee share) or from
    employerRate / employerRateAccount (employer share), as the development team codes them (one field per band; an account
    holds a percentage computed by an earlier regulation). The engine records which share each band posted (self.share).
S6  Post formula: the posted value is the formula value; $band_amount_raw is available inside it. Taxation type formula:
    $band_amount_raw = base (rate 100) and the value is the formula's.
S7  Posting: debitAccount += value (several regulations may post to the same account, e.g. two illness segments to R327).
    creditAccount 99999 is the clearing account and holds nothing here.
S8  No differential construct: the art. 383 table is a flat lookup written as nested IF() (design Part 4).
S9  Rounding only where a formula rounds (ROUND = half-up to the peso; CEILING(x;n) = smallest multiple of n >= x).
S10 Unknown variables are an error (not 0): every read must be an input / flag, a constant, or posted by an earlier ordinal;
    a WTC wage type (R<row>) not paid in the period reads 0.
S11 Flags and HR fields enter as accounts (582xx, 64992) with the values given by the case.
S12 Assertion false = the regulation does not execute (nothing posted).
S13 Effective-dated constants (52504 hours divisor, 52505 rest-day surcharge) are read at the date carried by the pay line
    (per-line execution of a band that has a unitAccount: one evaluation per hours line of that wage type).
S14 `$<acct>_ytd` = sum of <acct> over the prior periods of the same calendar year (the run keeps the history).
S15 `$<acct>_raw` = sum of the $band_amount_raw of the regulations that posted <acct> (before the post formula).
S16 Decimal arithmetic, 40 significant digits.
S17 Bands of one regulation run in their order. This design never lets a band read the account of another band of its own
    regulation (the employer share is written from the base), so it does not depend on that order.
S18 Deduction wage types carry negative amounts (signed sum of S2), as the development team's negative accounts.
```

## Design assumptions

| # | Assumption | Effect | Confidence |
|---|---|---|---|
| A1 | Service bonus and salary in the same month (Procedure 1): the salary read uses the annual 790 / 1,340 UVT room first; the service-bonus read uses what is left (`9170091`, `9170092`). The law does not say how the annual cap is shared between the two reads. | the service-bonus withholding in a month where the annual cap is nearly used | 80% — configurable |
| A2 | One rounding per contributor and fund, up to the next COP 100 (Decree 780 art. 3.2.1.5 num. 2: "El valor de los aportes liquidados por cada cotizante … múltiplo de 100 superior"; AT2 v30 field 47). The employee share is the statutory rate rounded to the peso (Law 100 arts. 20, 204: 4%); the employer pays the residue of the rounded total. Where the employee pays the whole fund (exonerated health, solidarity fund) the employee share carries the rounding. The split itself is not regulated. | the employer bears the rounding | 92% |
| A3 | The 70% factor of the all-inclusive salary is applied to the whole IBC and levy matrix (salary rows) of an all-inclusive employee. | only if an all-inclusive employee also has non-integral salary rows | 90% |
| A4 | Sub-30-day projection of Procedure 1 (Decree 1625 art. 1.2.4.1.3 lits. a-b: "podrá") is an entity option, off by default (`58214`). | withholding in hiring / leaving months | 95% (the decree makes it optional) |
| A5 | Tax residence is read from `$64552` (1 resident, 2 non-resident), the account of the development team's draft 9170132; the DD field Tax Residence Status must feed it. | none | — |
| A6 | `DAYS360` (30/360, inclusive) is available for the service days of the art. 64 indemnity (`58288`), as the development team computes month counts with `YEARS_BETWEEN`. | indemnity days | — |
| A7 | `CEILING(x;n)` exists in the formula vocabulary; if not, an equivalent must be confirmed on boundary values (IBC 992,179.50 → 992,180). | IBC and every contribution | — (blocking if absent) |
| A8 | The illness benefit floor (C-543 of 2007) is applied per day to every segment, days 91–180 included; a client paying more is lawful (Labour Code art. 13). | days 91–180 below 2 SMMLV | 93% |
| A9 | Non-taxable income = the contributions withheld from the employee, rounded (Tax Code arts. 55, 56: "los aportes obligatorios que efectúen los trabajadores"). | withholding base up to COP 100 per fund lower than with the contributions before rounding | 90% |
| A10 | `regulationId` carries the 9170xxx code (the development team stores a UUID there and the code in name / ordinal); `systemTaxYearIds` = `co_2026` by analogy with `td_2026`. | none | — |
