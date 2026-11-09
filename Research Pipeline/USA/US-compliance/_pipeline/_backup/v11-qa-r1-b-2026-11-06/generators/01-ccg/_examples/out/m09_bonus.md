**Scenario.** An annual bonus of 5,000.00 is paid on its own check to an employee with 40,000.00 of 2026 wages. Supplemental wages identified separately from regular wages may be withheld at the optional flat rate [US-FEDS5-003]. FICA applies in full.

*Annual bonus, optional flat-rate method (federal layer)*

| Line | Calculation | Result (USD) |
|---|---|---|
| Supplemental payment (paid separately from regular wages) | — | 5,000.00 |
| FIT, optional flat rate (supplemental wages up to [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] in the year) | 5,000.00 × [[FACT:fed.fit.supplemental.flat_rate=22]]% | 1,100.00 |
| OASDI base remaining before this pay | [[FACT:fed.fica.oasdi.wage_base=184,500]] − 40,000.00 | 144,500.00 |
| OASDI base for this pay (lesser of remaining base and pay) | min(144,500.00, 5,000.00) | 5,000.00 |
| OASDI employee | 5,000.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 310.00 |
| Medicare employee | 5,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 72.50 |
| Net payment | 5,000.00 − 1,100.00 − 310.00 − 72.50 | 3,517.50 |
