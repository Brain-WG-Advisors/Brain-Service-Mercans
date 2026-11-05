# QA report

The United States package (v1.0) reached QA pass in every artifact. Review verdicts come from independent audits of each artifact.

| Artifact | Final review round | Verdict | Reviewed on | Stated accuracy |
|---|---|---|---|---|
| CCG | r6 | PASS | 2026-11-04 | about 89% federal core and modules; 75-85% per State reference |
| SCOPE | r3 | PASS | 2026-11-03 | about 92% |
| RSPEC | r3d | PASS | 2026-11-04 | mean 78% over 227 return rows |
| DD | r3 | PASS | 2026-11-03 | about 80% |
| WTC | r3 | PASS | 2026-11-04 | about 85% |
| SIR | r4 | PASS | 2026-11-04 | 75-85% |
| PSL | r3 | PASS | 2026-11-04 | 85% |

## Validation exemptions recorded by the owner

- US-OWN-010: checks on validation of filing files against an official norm, validator or plugin are exempted for the Report Specifications; no machine-callable national validator exists (SSA AccuWage validates EFW2 only inside an authenticated session; State validators are State-specific).
- US-OWN-011: three narrowly scoped content-check findings are exempted (WTC row for W-2 box 12 code TA valid only from 2026-07-04; a Kansas guide id that matches a wage-type code pattern; the Georgia SUI wage-type wording).

## Limitations that carry into this skill

- Open research gaps and documented limitations are listed in `14-known-gaps.md`; each is printed in the references as 'Not configured in this release (open gap id)'.
- No real filed sample exists for any Report Specification; every return layout is derived from official authority pages and file specifications.
- The payslip has no tested US sample; State pay-statement rules are statute readings.

## Source-change log

- 2026-11-04: skill re-synced after the CCG and SIR citation rebuild (practice rows cite their additional rows, two social-security citations, SIR Form 940 and Ohio school-district cells).
- 2026-11-04: skill re-synced after the run-close rebuilds (practice notes GA/SC/NE/OH/CT, data dictionary fields er.supplemental_wage_method and er.state_sui_rate, ma.pfml.rate.selection_basis, superseded legal-basis rows re-pointed to their successors); 13 reference files changed.
- 2026-11-04: skill re-synced after the CCG rebuild (m10 payslip wording, annex_LA channel wording, annex_DC wording, annex_MS payslip gap PSL-RQ-14, m04 Hawaii row), the WTC wording fix and the UT/MS/LA fact fixes; references regenerated.
- 2026-11-04: skill references flattened from the approved CCG (13 modules, federal, multistate and 51 jurisdiction references), WTC, DD, SIR, 20 Report Specifications and the payslip generator at package version 1.0. Append one line here whenever any source document changes, even when a full re-sync is deferred.
