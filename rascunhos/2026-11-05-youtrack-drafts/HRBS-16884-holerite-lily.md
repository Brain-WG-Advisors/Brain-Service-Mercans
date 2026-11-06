@lli Two payslip fixes for STG, the amounts don't change:
1. IRPF rate: print the rate applied (2552 ÷ 58552, i.e. 58217 when it's loaded), not 58118. Today the payslip shows the calculated rate, so the client sees a rate that wasn't used.
2. 2515 and 2535: print as the base the salary above the maximum base (58535 − 52991), not 58535. Example 1019084: 7,500.00 − 5,101.20 = 2,398.80; amounts 4.94 and 24.54 are right.
Also for 1001440: load 34.85% in 58217 again (it was removed for the test).
