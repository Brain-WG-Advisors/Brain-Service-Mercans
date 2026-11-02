**Scenario.** An employee whose position is eliminated receives severance pay of 18,000.00 in a separate payment, after 60,000.00 of 2026 wages from this employer. Severance is wages for FIT, FICA and FUTA [US-FEDS5-029]. Paid separately, it is withheld as supplemental wages at the optional flat rate. FUTA is already exhausted for the year at this wage level. State withholding and final-pay timing follow the work State (Table 9.1.1). Alabama, for example, exempts severance up to [[FACT:al.wh.severance.exempt_max=50,000]] from its withholding [US-ALS5-001].

*Redundancy severance payout (federal layer)*

| Line | Calculation | Result (USD) |
|---|---|---|
| Supplemental payment (paid separately from regular wages) | — | 18,000.00 |
| FIT, optional flat rate (supplemental wages up to [[FACT:fed.fit.supplemental.mandatory_threshold=1,000,000]] in the year) | 18,000.00 × [[FACT:fed.fit.supplemental.flat_rate=22]]% | 3,960.00 |
| OASDI base remaining before this pay | [[FACT:fed.fica.oasdi.wage_base=184,500]] − 60,000.00 | 124,500.00 |
| OASDI base for this pay (lesser of remaining base and pay) | min(124,500.00, 18,000.00) | 18,000.00 |
| OASDI employee | 18,000.00 × [[FACT:fed.fica.oasdi.rate.employee=6.2]]% | 1,116.00 |
| Medicare employee | 18,000.00 × [[FACT:fed.fica.medicare.rate.employee=1.45]]% | 261.00 |
| Net payment | 18,000.00 − 3,960.00 − 1,116.00 − 261.00 | 12,663.00 |
