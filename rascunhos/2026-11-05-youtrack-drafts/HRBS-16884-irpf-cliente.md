@nkeer @lli Compared the client's IRPF file (2608 ES03 %IRPF.xlsx) with the August G2N:
- The rate applied (2552 ÷ 58552) is the client's rate for 58 of 60 employees. The client's "Mercans" column is 58118, the rate the system calculates, which isn't the one applied.
- The payslip prints 58118, not the applied rate, which is why the rates look wrong. Fix: print the applied rate (item 5 above).
- 1001440: 58217 is empty, so 30.63% was applied instead of 34.85%. Fix: load 34.85% in 58217 (item 4 above).
- 1018096: non-resident, 24% applied through 2582, same as the client.
- 1020209 is in the file but not in this run.
