# CCG ready after the practice facts re-sync (2026-11-04)
Copy: _pipeline/_backup/pre-m13-2026-11-04/ (modules, annexes, docx). CCG docx md5 b9de40ce69edefd94c76439261c3318b.
Changed lines (fact-bound): m06_tax 10, m12_worked_examples 2, m13_practices 10 (practice.ct/ga/ne/oh/sc keys), annex_MA 1 (ma.pfml.rate.selection_basis; one table fewer, 928 to 927).
Checks: tag_sync 0 stale in CCG, SIR, RSPEC, DD, WTC, PSL; C11, C29, C38, C40, C70, period-aware C46 and vocab lint pass.

```
m06_tax.md: -| Georgia | [[FACT:practice.ga.rate_change_2026=4.99% for TY2026 (5.19% before); 2027 0.125-point step conditional on OPB report of 2026-12-01]] | [US-GAS5-009] |
m06_tax.md: +| Georgia | [[FACT:practice.ga.rate_change_2026=4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one y
m06_tax.md: -| SC | [[FACT:practice.sc.withholding_rates_2026=Use WH-1603 tables 0/3/6% for 2026 withholding; Act 110 rates (1.99%/5.21%) apply at the 2026 annual return only]] | [US-SCS5-004] |
m06_tax.md: +| SC | [[FACT:practice.sc.withholding_rates_2026=Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% 
m06_tax.md: -| NE | [[FACT:practice.ne.use_circular_en_tables=Withholding uses DOR Circular EN tables (2026 2.26-4.60%), not the statutory 4.55% rate]] | [US-NES5-018] |
m06_tax.md: +| NE | [[FACT:practice.ne.use_circular_en_tables=Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax y
m06_tax.md: -| OH | [[FACT:practice.oh.flat_rate_vs_tables=TY2026 statute flat 2.75% but withholding tables graduated to 3.4% (5747.06 rule vs 5747.02 rate) - use the tables]] | [US-OHS5-007] |
m06_tax.md: +| OH | [[FACT:practice.oh.flat_rate_vs_tables=Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC
m06_tax.md: -| CT | [[FACT:practice.ct.tables_vs_rules=DRS permits tables or TPG-211 rules; results differ up to 0.48/period; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2,
m06_tax.md: +| CT | [[FACT:practice.ct.tables_vs_rules=DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-peri
m12_worked_examples.md: -| SC | oracle.example_1 | [[FACT:sc.pit.oracle.example_1.withholding=10.58]] | US-SCP51-002 | re-derived from the published method | Recomputed in 12.2.2: agrees 2026 withholding tables, not the Act 
m12_worked_examples.md: +| SC | oracle.example_1 | [[FACT:sc.pit.oracle.example_1.withholding=10.58]] | US-SCP51-002 | re-derived from the published method | Recomputed in 12.2.2: agrees 2026 withholding tables, not the Act 
m13_practices.md: -| SC | [[FACT:practice.sc.withholding_rates_2026=Use WH-1603 tables 0/3/6% for 2026 withholding; Act 110 rates (1.99%/5.21%) apply at the 2026 annual return only]] | US-SCS5-004 |
m13_practices.md: +| SC | [[FACT:practice.sc.withholding_rates_2026=Withholding tables in force: SCDOR WH-1603 (Rev. 10/30/25) 2026 tables, 0/3/6%; SCDOR Information Letter #26-20 gives the Act 110 2026 schedule 1.99% 
m13_practices.md: -| NE | [[FACT:practice.ne.use_circular_en_tables=Withholding uses DOR Circular EN tables (2026 2.26-4.60%), not the statutory 4.55% rate]] | US-NES5-018 |
m13_practices.md: +| NE | [[FACT:practice.ne.use_circular_en_tables=Withholding uses the DOR Circular EN 2026 percentage-method tables (2.26% to 4.60% rates); the statute (77-2715.03) sets 4.55% for rate three in tax y
m13_practices.md: -| CT | [[FACT:practice.ct.tables_vs_rules=DRS permits tables or TPG-211 rules; results differ up to 0.48/period; configured: DRS per-period tables up to each table maximum, TPG-211 rules above (CT.2,
m13_practices.md: -| OH | [[FACT:practice.oh.flat_rate_vs_tables=TY2026 statute flat 2.75% but withholding tables graduated to 3.4% (5747.06 rule vs 5747.02 rate) - use the tables]] | US-OHS5-007 |
m13_practices.md: +| CT | [[FACT:practice.ct.tables_vs_rules=DRS: 'Use either the withholding calculation rules or the withholding tables' (TPG-211); the two methods can give different amounts; configured: DRS per-peri
m13_practices.md: +| OH | [[FACT:practice.oh.flat_rate_vs_tables=Ohio withholding follows the tax commissioner's tables under ORC 5747.06, graduated 1.6% / 2.99% / 3.4% from 2026-08-01 (US-OH-006, US-OHS5-001); the ORC
m13_practices.md: -| GA | [[FACT:practice.ga.rate_change_2026=4.99% for TY2026 (5.19% before); 2027 0.125-point step conditional on OPB report of 2026-12-01]] | US-GAS5-009 |
m13_practices.md: +| GA | [[FACT:practice.ga.rate_change_2026=4.99% for taxable years beginning on/after 2026-01-01 (5.19% before); from 2027-01-01 reduced by 0.125 point annually to 3.99%, each step delayed one year i
annex_MA.md: +| `ma.pfml.rate.selection_basis` | [[FACT:ma.pfml.rate.selection_basis=The new contribution rate applies to wages earned on or after January 1 of each year; rates are set annually for January 1-Decem```

STATUS: COMPLETE
