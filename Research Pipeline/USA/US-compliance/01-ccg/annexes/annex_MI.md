# Annex MI: Michigan


United States Country Configuration Guide, jurisdiction annex MI. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the Michigan layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section MI.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T4 (verified) |
| Basis | State flat rate [[FACT:mi.pit.rate.flat=4.25]] percent [US-MIP52-001]; [[FACT:mi.local.cities.count=24]] cities levy income tax, the Treasury administers Detroit only, the other 23 administer their own filing [US-MIP52-002, US-MIP51-002] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- The state deduction for qualified tips and overtime (`mi.pit.tips_overtime_deduction`) operates at assessment only, on the individual return. It does not change withholding; do not model it in the payroll calculation.
- City income taxes: Detroit is administered by the state Treasury ([[FACT:mi.local.detroit.rate.resident=2.4]] percent residents, [[FACT:mi.local.detroit.rate.nonresident=1.2]] percent nonresidents). The other self-administered cities file on their own city returns (tier T4). Their uniform-ordinance defaults ([[FACT:mi.local.uniform.resident_rate_default=1.0]] / [[FACT:mi.local.uniform.nonresident_rate_default=0.5]] percent) are defaults, not confirmed city rates; per-city rates are a blocking gap (section MI.2c).
- Reciprocity ([[FACT:mi.reciprocity.states=IL, IN, KY, MN, OH, WI (state tax only, not city tax)]]) covers the state tax only; city taxes still apply.
- Prevailing wage follows the state act (`mi.prevailing_wage.certified_payroll`). Never read Michigan prevailing-wage status from the US Department of Labor state table, whose edition predates Michigan's restoration of its law.
- The Social Security number shown on any pay document is limited to [[FACT:mi.payslip.ssn.max_digits=4]] digits.

## MI.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.minwage.hourly` | [[FACT:mi.minwage.hourly=13.73]] USD | 2026-01-01 | 2026-12-31 | US-MIS5-001 (A.1, Michigan Legislature) | IWOWA MCL 408.934 (2018 PA 337 as amended by 2025 PA 1); employers with 2+ employees, employees 16+; not FLSA-covered employers unless federal lower (408.940(1)). |
| `mi.minwage.hourly` | [[FACT:mi.minwage.hourly=15.0]] USD | 2027-01-01 | open | US-MIS5-001 (A.1, Michigan Legislature) | Enacted. From Oct 2027 Midwest CPI-U by State Treasurer (published by 1 Nov, effective 1 Jan); no increase above a statutory prior-year unemployment threshold. |
| `mi.minwage.tipped.percent` | [[FACT:mi.minwage.tipped.percent=40]] percent | 2026-01-01 | 2026-12-31 | US-MIS5-003 (A.1, Michigan Legislature) | Schedule 42% (2027), 44% (2028), 46% (2029), 48% (2030), 50% (2031); conditions: tips cover gap, declared for FICA, kept by employee (pool within chain of service), written notice and consent at hire. |
| `mi.minwage.tipped.percent` | [[FACT:mi.minwage.tipped.percent=42]] percent | 2027-01-01 | 2027-12-31 | US-MIS5-003 (A.1, Michigan Legislature) |  |
| `mi.minwage.tipped.cash_wage` | [[FACT:mi.minwage.tipped.cash_wage=5.492]] USD | 2026-01-01 | 2026-12-31 | US-MIS5-003 (A.1, Michigan Legislature) | [[FACT:mi.minwage.hourly=13.73]] x 0.40; statute gives no rounding rule. |
| `mi.minwage.tipped.cash_wage` | [[FACT:mi.minwage.tipped.cash_wage=6.3]] USD | 2027-01-01 | 2027-12-31 | US-MIS5-003 (A.1, Michigan Legislature) | 15.00 x 0.42. |
| `mi.minwage.minor.percent` | [[FACT:mi.minwage.minor.percent=85]] percent | 2026-01-01 | open | US-MIS5-003 (A.1, Michigan Legislature) | Under 18: [[FACT:mi.minwage.hourly=13.73]] x 0.85 = 11.6705 (derived, no rounding rule). |
| `mi.minwage.training_wage` | [[FACT:mi.minwage.training_wage=4.25]] USD | 2026-01-01 | open | US-MIS5-003 (A.1, Michigan Legislature) | First 90 days, new employees under 20. |
| `mi.local_mandates.preempted` | [[FACT:mi.local_mandates.preempted=True]] | 2015-01-01 | open | US-MIS5-014 (A.1, Michigan Legislature) | 2015 PA 105 (MCL 123.1385-.1389): local MW, prevailing wage (except state projects), leave and scheduling mandates pre-empted. |
| `mi.overtime.weekly_threshold_hours` | [[FACT:mi.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 | open | US-MIS5-002 (A.1, Michigan Legislature) | MCL 408.934a: 1.5x; public hospitals 8/80; exemptions EAP, seasonal amusement, agriculture; comp time 1.5 h per OT hour, cap 240 h, cash out within 30 days of request and at termination; comp time on the earnings statement. |
| `mi.comp_time.cap_hours` | [[FACT:mi.comp_time.cap_hours=240]] hours | 2026-01-01 | open | US-MIS5-002 (A.1, Michigan Legislature) |  |
| `mi.pay_frequency.rule` | [[FACT:mi.pay_frequency.rule=default semi-monthly (1-15 paid by 1st next month; 16-end by 15th); weekly/biweekly payday <= 14 days after period end; monthly within 15 days; December OT may go to next payday (MCL 408.472)]] | 2026-01-01 | open | US-MIS5-005 (A.1, Michigan Legislature) |  |
| `mi.payment.method` | [[FACT:mi.payment.method=cash, check, direct deposit, payroll debit card; DD/paycard need full free written consent (mandated DD-or-card election: no return within 30 days = presumed consent); method change within 1 pay period; paycard 1 free withdrawal per period, 21 days notice of fee changes, free balance inquiries; no cost pass-through (MCL 408.476)]] | 2026-01-01 | open | US-MIS5-006 (A.1, Michigan Legislature) |  |

- Not configured in this release [[GAP:RQ-036]]: Michigan coverage thresholds are configured only for agricultural and domestic employment (`mi.sui.coverage.ag_domestic`); thresholds for other special populations are not established.

## MI.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.pit.rate.flat` | [[FACT:mi.pit.rate.flat=4.25]] percent | 2026-01-01 | open | US-MIPIT-001 (A.2, Michigan Department of Treasury) | Guide 446 Rev. 02-26 [US-MIPIT-001]; MCL 206.703. |
| `mi.wh.method` | [[FACT:mi.wh.method=4.25% x (compensation - 5,900 x MI-W4 exemptions / pay periods)]] | 2026-01-01 | 2026-12-31 | US-MIS5-019 (A.2, Michigan Department of Treasury) | Per-period exemption weekly 113.46, biweekly [[FACT:mi.wh.exemption.biweekly=226.92]], semi-monthly 245.83, monthly 491.67 (derived). No rounding rule. |
| `mi.wh.exemption.annual` | [[FACT:mi.wh.exemption.annual=5900]] USD | 2026-01-01 | 2026-12-31 | US-MIS5-015 (A.1, Michigan Legislature) | Indexed: 3,700 x CPI ratio + 600, rounded to 100 (2026 not re-derivable from read sources); 2027 unpublished. |
| `mi.wh.exemption.biweekly` | [[FACT:mi.wh.exemption.biweekly=226.92]] USD | 2026-01-01 | 2026-12-31 | US-MIS5-019 (A.2, Michigan Department of Treasury) | 5,900/26. |
| `mi.wh.supplemental.rate` | [[FACT:mi.wh.supplemental.rate=4.25]] percent | 2026-01-01 | open | US-MIPIT-001 (A.2, Michigan Department of Treasury) | Bonuses and separate payments are withheld at the flat rate with no exemption adjustment (Treasury Guide 446). |
| `mi.wh.certificate` | [[FACT:mi.wh.certificate=MI-W4 (Rev. 12-20); federal W-4 may not substitute; line 6 exemptions, line 7 additional, 8a/8b exempt; none = zero exemptions; copies to Treasury for 10+ exemptions or exempt; nonresidency proof by employer certificate/letter]] | 2020-12-01 | open | US-MIS5-019 (A.2, Michigan Department of Treasury) |  |
| `mi.pit.tips_overtime_deduction` | [[FACT:mi.pit.tips_overtime_deduction=2025 PA 24 (MCL 206.30(1)(ee)): tax years 2026-2028 deduct federally allowed qualified tips (IRC 224) and overtime (IRC 225); level ASSESSMENT (MI-1040) only - no withholding change]] | 2026-01-01 | 2028-12-31 | US-MIV6-002 (A.1, Michigan Legislature) | Caution: secondary claim that employers stop withholding on tips is unsupported - do not model. 2026 PA 39 (2026-07-22) amended 206.30 again (content open) [US-MIS5-015]. 2026 PA 39 (approved 2026-07-21, eff. 2026-07-22) re-enacts MCL 206.30(1)(ee): TY2026-2028 deduction of federal qualified tips (IRC 224) and overtime (IRC s.225); nonresidents only for MI services; ASSESSMENT level only, no withholding effect stated. |
| `mi.oracle.state.biweekly_2000_1ex` | [[FACT:mi.oracle.state.biweekly_2000_1ex=75.36]] USD | 2026-01-01 | 2026-12-31 | US-MIS5-019 (A.2, Michigan Department of Treasury) | (2,000 - [[FACT:mi.wh.exemption.biweekly=226.92]]) x 0.0425 = [[FACT:mi.oracle.state.biweekly_2000_1ex=75.36]]. Official oracle: Treasury withholding calculator (michigan.gov/taxes/business-taxes/withholding/tax-calculator). |
| `mi.oracle.detroit.resident_biweekly_2000` | [[FACT:mi.oracle.detroit.resident_biweekly_2000=47.45]] USD | 2026-01-01 | 2026-12-31 | US-MIR3-002 (A.2, Michigan Department of Treasury - City Tax Administration) | (2,000 - 23.08) x 0.024 = [[FACT:mi.oracle.detroit.resident_biweekly_2000=47.45]]. |

- Not configured in this release [[GAP:RQ-028]]: The withholding guide (Form 446: rate, supplemental, nonresident and W-2 rules) is carried by an older register row; the values in this annex cite the MI-W4 row, which carries the same rate and exemption.

## MI.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.nonres.rules` | [[FACT:mi.nonres.rules=withhold nonresidents for MI work unless reciprocity; residents temporarily working elsewhere still withheld; out-of-state employers register and withhold for MI workers]] | 2026-01-01 | open | US-MIS5-019 (A.2, Michigan Department of Treasury) | Guide 446 [US-MIPIT-001]. |
| `mi.reciprocity.states` | [[FACT:mi.reciprocity.states=IL, IN, KY, MN, OH, WI (state tax only, not city tax)]] | 2026-01-01 | open | US-MIP51-001 (A.2, Michigan Department of Treasury) | [US-MULTI-010]. |

## MI.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.local.detroit.rate.resident` | [[FACT:mi.local.detroit.rate.resident=2.4]] percent | 2026-01-01 | open | US-MIR3-002 (A.2, Michigan Department of Treasury - City Tax Administration) | Treasury-administered; nonresident [[FACT:mi.local.detroit.rate.nonresident=1.2]]% (predominant place of work Detroit); exemption 600/yr (weekly 11.54, biweekly 23.08, semi-monthly 25.00, monthly 50.00, daily 1.64); DW-4 (Form 5527), none = resident rate no exemption; Form 5323 monthly by 15th; Form 5321 annual due 2027-02-28 for TY2026 [US-MIP51-002]. |
| `mi.local.detroit.rate.nonresident` | [[FACT:mi.local.detroit.rate.nonresident=1.2]] percent | 2026-01-01 | open | US-MIR3-002 (A.2, Michigan Department of Treasury - City Tax Administration) |  |
| `mi.local.detroit.exemption.annual` | [[FACT:mi.local.detroit.exemption.annual=600]] USD | 2026-01-01 | open | US-MIR3-002 (A.2, Michigan Department of Treasury - City Tax Administration) |  |
| `mi.local.cities.count` | [[FACT:mi.local.cities.count=24]] cities | 2026-01-01 | open | US-MIB5-401 (A.2, Michigan Department of Treasury) | Detroit plus 23 self-administered cities that file on separate city returns (T4). The uniform ordinance sets the default resident and nonresident rates (section MI.2c) unless a city resolves a lower rate (MCL 141.611) [US-MIR3-003]. The rates, forms and due dates of the 23 cities are not yet confirmed. |
| `mi.local.uniform.resident_rate_default` | [[FACT:mi.local.uniform.resident_rate_default=1.0]] percent | 2026-01-01 | open | US-MIR3-003 (A.1, Michigan Legislature) |  |
| `mi.local.uniform.nonresident_rate_default` | [[FACT:mi.local.uniform.nonresident_rate_default=0.5]] percent | 2026-01-01 | open | US-MIR3-003 (A.1, Michigan Legislature) |  |
| `mi.local.cities.list` | [[FACT:mi.local.cities.list=Treasury-administered: Detroit. Self-administered (23): Albion, Battle Creek, Benton Harbor, Big Rapids, East Lansing, Grand Rapids, Flint, Grayling, Hamtramck, Highland Park, Hudson, Ionia, Jackson, Lansing, Lapeer, Muskegon, Muskegon Heights, Pontiac, Port Huron, Portland, Saginaw, Springfield, Walker.]] | 2026-01-01 | open | US-MIB5-301 (A.2, Michigan Department of Treasury) | Treasury "Which cities impose an income tax?" page (verbatim text), consistent with mi.local.cities.count = 24 (US-MIB5-401, a different Treasury page). The page gives no rates. |
| `mi.local.detroit.eservices_from` | [[FACT:mi.local.detroit.eservices_from=2026-11-12]] | 2026-11-12 | open | US-MIB5-301 (A.2, Michigan Department of Treasury) | Detroit city income taxes move to Michigan Treasury eServices on 2026-11-12 (michigan.gov/taxes/citytax, read 2026-11-02). |

- Not configured in this release [[GAP:RQ-029]]: The rates, forms and due dates of the self-administered city income taxes other than Detroit were not verified against the official source. No city rate other than Detroit's is configured.

## MI.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.sui.wage_base` | [[FACT:mi.sui.wage_base=9000]] USD | 2026-01-01 | 2026-12-31 | US-MIS5-025 (A.2, Michigan LEO - Unemployment Insurance Agency) | MCL 421.44(4): the base of 9,500 is reduced to 9,000 for non-delinquent employers when the trust fund is at least 2.5 billion on the prior June 30 [US-MIS5-010]; delinquent employers keep 9,500. Not CPI-indexed; the 2027 base depends on the fund at 2026-06-30. |
| `mi.sui.wage_base.delinquent` | [[FACT:mi.sui.wage_base.delinquent=9500]] USD | 2026-01-01 | open | US-MIS5-010 (A.1, Michigan Legislature) |  |
| `mi.sui.new_employer.rate` | [[FACT:mi.sui.new_employer.rate=2.7]] percent | 2026-01-01 | open | US-MIS5-012 (A.1, Michigan Legislature) | Years 1-2 (MCL 421.19); construction pays average construction rate ([[FACT:mi.sui.new_construction.rate=5.0]]% for 2026). |
| `mi.sui.employer.rate.min` | [[FACT:mi.sui.employer.rate.min=0.06]] percent | 2026-01-01 | 2026-12-31 | US-MIP9W-001 (A.2, Michigan Unemployment Insurance Agency (LEO)) | Range [[FACT:mi.sui.employer.rate.min=0.06]]%-[[FACT:mi.sui.employer.rate.max=12.2]]% (15.2% with penalty); no transit/workforce/admin surcharge [US-MIP9V-001, US-MIP9W-002]. |
| `mi.sui.employer.rate.max` | [[FACT:mi.sui.employer.rate.max=12.2]] percent | 2026-01-01 | 2026-12-31 | US-MIP9W-001 (A.2, Michigan Unemployment Insurance Agency (LEO)) |  |
| `mi.sui.wages.definition` | [[FACT:mi.sui.wages.definition=FICA-reported tips included; retirement/health plan payments, employer-paid employee FICA, 401(a) trust payments, SUB pay excluded; wages paid in other states count toward the limit]] | 2026-01-01 | open | US-MIS5-010 (A.1, Michigan Legislature) |  |
| `mi.sui.coverage.ag_domestic` | [[FACT:mi.sui.coverage.ag_domestic=Agricultural: 10+ individuals in 20 weeks or cash remuneration >= 20,000 USD in a quarter; domestic service: cash remuneration >= 1,000 USD in a quarter (current or preceding year)]] | 2016-05-23 | open | US-MIV6-001 (A.1, Michigan Legislature) | Register: US-MIV6-001 |

- Not yet published [[GAP:RQ-030]]: The 2027 unemployment wage base depends on the fund balance at 2026-06-30, and the 2027 personal exemption is not yet published.

## MI.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.payslip.items` | [[FACT:mi.payslip.items=hours worked, gross wages, pay-period identification, separate itemisation of deductions (piece-rate hand harvesters: units); hours may be omitted for EAP-exempt, elected officials, political appointees (MCL 408.479(2)); comp time earned/paid]] | 2026-01-01 | open | US-MIS5-009 (A.1, Michigan Legislature) | IWOWA 408.937 repeats hours/wages/deductions; e-delivery: statute silent. |

- Not configured in this release [[GAP:RQ-032]]: Whether Michigan allows electronic pay statements (MCL 408.479) is not established from an official source.

## MI.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.report.wh.5080` | [[FACT:mi.report.wh.5080=Form 5080 monthly/quarterly due 20th after period (combined SUW return; frequency assigned yearly); late penalty 5%; MTO, software or paper]] | 2026-01-01 | open | US-MIS5-018 (A.2, Michigan Department of Treasury) |  |
| `mi.report.annual.5081` | [[FACT:mi.report.annual.5081=Form 5081 annual reconciliation for 2026 due 2027-02-28 (every filer)]] | 2026-01-01 | open | US-MIS5-021 (A.2, Michigan Department of Treasury) |  |
| `mi.report.wh.accelerated_eft_threshold` | [[FACT:mi.report.wh.accelerated_eft_threshold=480000]] USD | 2026-01-01 | open | US-MIS5-021 (A.2, Michigan Department of Treasury) | Prior-year liability >= 480,000: EFT on the federal deposit day (notified April, from July). |
| `mi.report.sui.quarterly` | [[FACT:mi.report.sui.quarterly=MiUI (live 2026-02-23) due 25 Jan / 25 Apr / 25 Jul / 25 Oct; file formats CSV v3 (2026-04-08), ICESA v2, EFW2 v2 (2026-04-03, 512-byte RE/RS UIA profile), XML v1; MiWAM format retired]] | 2026-02-23 | open | US-MIS5-022 (A.2, Michigan LEO - Unemployment Insurance Agency) | Due dates [US-MIS5-020]. |
| `mi.newhire.report_days` | [[FACT:mi.newhire.report_days=20]] days | 2026-01-01 | open | US-MIB5-001 (A.2, Michigan Department of Health and Human Services, Child Support Division (New Hires Operation Center)) | Calendar days from hire, new and returning employees working in Michigan (page cites 42 USC 653A). |
| `mi.newhire.fields` | [[FACT:mi.newhire.fields=Employee SSN, name, address, date of birth (optional), date of hire (first day services performed for wages); employer FEIN (same as on quarterly wage reports), name, payroll address, email, phone, fax]] | 2026-01-01 | open | US-MIB5-001 (A.2, Michigan Department of Health and Human Services, Child Support Division (New Hires Operation Center)) |  |
| `mi.newhire.channels` | [[FACT:mi.newhire.channels=Michigan New Hires Operation Center (MDHHS Child Support): online entry, file upload, SFTP (800-524-9846), fax 877-318-1659, mail PO Box 51041 Livonia MI 48151-51041; electronic filers two transmissions per month 12-16 days apart]] | 2026-01-01 | open | US-MIB5-001 (A.2, Michigan Department of Health and Human Services, Child Support Division (New Hires Operation Center)) |  |
| `mi.newhire.rehire_gap_days` | [[FACT:mi.newhire.rehire_gap_days=60]] days | 2026-01-01 | open | US-MIB5-001 (A.2, Michigan Department of Health and Human Services, Child Support Division (New Hires Operation Center)) | Rehire = new W-4 required or 60 consecutive days since last employment; terminations reported only if an income withholding notice was in effect; only tribal enterprises on federal tribal land exempt. |

- Not configured in this release [[GAP:RQ-033]]: The Michigan statute establishing the New Hires Operation Center duty, the state penalty and the required fields was not established from an official source.

## MI.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.leave.esta.accrual.hours_worked_per_hour` | [[FACT:mi.leave.esta.accrual.hours_worked_per_hour=30]] hours | 2025-02-21 | open | US-MIS5-004 (A.1, Michigan Legislature) | Earned Sick Time Act (2018, as amended in 2025): every employer; small employers (10 or fewer) cap 40 hours or front-load 40 (from 2025-10-01); others cap 72 or front-load 72; FLSA-exempt employees assumed to work 40 hours; pay at the greater of the base rate or the minimum wage (excluding overtime, bonus, commission and tips); 1-hour increments; new hires may wait up to 120 days; no payout; rehire within 2 months restores the balance; documentation for absences over 3 days; records kept 3 years. |
| `mi.leave.esta.cap_hours.small` | [[FACT:mi.leave.esta.cap_hours.small=40]] hours | 2025-10-01 | open | US-MIS5-004 (A.1, Michigan Legislature) |  |
| `mi.leave.esta.cap_hours.large` | [[FACT:mi.leave.esta.cap_hours.large=72]] hours | 2025-02-21 | open | US-MIS5-004 (A.1, Michigan Legislature) |  |
| `mi.leave.esta.small_employer_threshold` | [[FACT:mi.leave.esta.small_employer_threshold=10]] employees | 2025-02-21 | open | US-MIS5-004 (A.1, Michigan Legislature) |  |
| `mi.leave.esta.payout_on_separation` | [[FACT:mi.leave.esta.payout_on_separation=False]] | 2025-02-21 | open | US-MIS5-004 (A.1, Michigan Legislature) |  |

## MI.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.final_pay.rule` | [[FACT:mi.final_pay.rule=discharge and quit: as soon as the amount can with due diligence be determined (hand harvesters within 3 days); contract workers estimated pay then final at contract end; deceased: designee/next-of-kin (MCL 408.475)]] | 2026-01-01 | open | US-MIS5-007 (A.1, Michigan Legislature) | Vacation payout per written contract/policy (408.471(e)/.473); withholding a benefit due at termination needs written consent (408.474); comp time paid; ESTA no payout. |

## MI.8 Benefits in kind and taxable wages

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.pit.conformity` | [[FACT:mi.pit.conformity=MI taxable income starts from federal AGI (rolling); fringe benefits follow Pub. 15 (401(k), cafeteria); no departure located]] | 2026-01-01 | open | US-MIS5-015 (A.1, Michigan Legislature) |  |

## MI.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.deductions.rule` | [[FACT:mi.deductions.rule=written consent for each deduction not required by law/CBA; for employer benefit consent each pay and not below MW; overpayment recovery within 6 months, clerical error, notice 1 period ahead, max 15% of gross, not below MW (MCL 408.477)]] | 2026-01-01 | open | US-MIS5-008 (A.1, Michigan Legislature) |  |
| `mi.deductions.overpayment.max_percent_gross` | [[FACT:mi.deductions.overpayment.max_percent_gross=15]] percent | 2026-01-01 | open | US-MIS5-008 (A.1, Michigan Legislature) |  |
| `mi.garn.child_support.cap_percent` | [[FACT:mi.garn.child_support.cap_percent=50]] percent | 2026-01-01 | open | US-MIS5-016 (A.1, Michigan Legislature) | MCL 552.608: total under all support orders max 50% of disposable (stricter than CCPA); remit to MiSDU [US-MIS5-024]. |
| `mi.garn.iwo_fee_and_periodic` | [[FACT:mi.garn.iwo_fee_and_periodic=Withheld income paid to FOC/SDU within 3 days after withholding; order binding on source of income 7 days after service of notice; order has priority over other legal process. Payer processing fee NOT found in 552.609/.611 (552.607 and 552.626 also read: no fee); fee remains open]] | 2009-12-28 | open | US-MIV6-003 (A.1, Michigan Legislature) | Register: US-MIV6-003 |

## MI.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.prevailing_wage.certified_payroll` | [[FACT:mi.prevailing_wage.certified_payroll=state projects (2023 PA 10, from 2024-02-13; energy >= 2 MW and contractor registration from 2025-04-02): no dollar threshold; certified payroll within 10 days after each pay period to contracting agent then LEO database; records 3 years; fine up to 5,000]] | 2025-04-02 | open | US-MIS5-023 (A.1, Michigan Legislature) |  |

## MI.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## MI.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.records.retention_years` | [[FACT:mi.records.retention_years=3]] years | 1979-01-04 | open | US-MIS5-009 (A.1, Michigan Legislature) | Name, address, birth date, occupation, rate, hours and wages per period, deductions, fringe benefits. |
| `mi.payslip.ssn.max_digits` | [[FACT:mi.payslip.ssn.max_digits=4]] digits | 2005-01-01 | open | US-MIS5-013 (A.1, Michigan Legislature) | SSN Privacy Act (MCL 445.83/.84): no more than 4 sequential digits displayed; SSN privacy policy required. |

## MI.13 Live legal change

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mi.live.miui` | [[FACT:mi.live.miui=MiUI replaced MiWAM for the UI tax side on 2026-02-23 with new wage-file specs]] | 2026-02-23 | open | US-MIS5-022 (A.2, Michigan LEO - Unemployment Insurance Agency) |  |
| `mi.live.2026_pa_39` | [[FACT:mi.live.2026_pa_39=Approved 2026-07-21, effective 2026-07-22. MCL 206.30(1)(ee): for tax years beginning after 2025-12-31 and before 2029-01-01 deduct federal qualified tips (IRC s.224) and qualified overtime (IRC s.225); nonresidents only for services performed in MI. Personal exemption base stated 3,700 USD (indexed under 206.30a). Level: assessment (taxable-income computation); withholding effect not stated in act]] | 2026-07-22 | open | US-MIV6-002 (A.1, Michigan Legislature) | Register: US-MIV6-002 |

## MI.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## MI.15 Special populations

- Agricultural: state OT exempt; harvest piece-rate outside act until scale set; H-2A UI-excluded. (US-MIS5-002, US-MIS5-005, US-MIS5-011)
- Minors: ESTA excludes youth-employment minors; UI excludes child for parent. (US-MIS5-003, US-MIS5-004, US-MIS5-011)
- Tipped: tips employee property; reported tips UI wages. (US-MIS5-003, US-MIS5-010, US-MIV6-002)
- Clergy: MI withholding follows federal duty; church employment UI-excluded. (US-MIS5-011)
- NRAs: follow federal duty; H-2A UI-excluded. (US-MIS5-011)
- Statutory employees: commission-only real estate/investment/insurance agents and direct sellers UI-excluded. (US-MIS5-011)
- Government: federal employees excluded from ESTA. (US-MIS5-002, US-MIS5-004)
- Not configured in this release [[GAP:RQ-036]]: Michigan coverage thresholds are configured only for agricultural and domestic employment (`mi.sui.coverage.ag_domestic`); thresholds for other special populations are not established.

## MI.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## MI.S Sources

| Source | Authority |
|---|---|
| US-MIB5-001 | Michigan Department of Health and Human Services, Child Support Division (New Hires Operation Center) |
| US-MIB5-301 | Michigan Department of Treasury |
| US-MIB5-401 | Michigan Department of Treasury |
| US-MIP51-001 | Michigan Department of Treasury |
| US-MIP9W-001 | Michigan Unemployment Insurance Agency (LEO) |
| US-MIPIT-001 | Michigan Department of Treasury |
| US-MIR3-002 | Michigan Department of Treasury - City Tax Administration |
| US-MIR3-003 | Michigan Legislature |
| US-MIS5-001 | Michigan Legislature |
| US-MIS5-002 | Michigan Legislature |
| US-MIS5-003 | Michigan Legislature |
| US-MIS5-004 | Michigan Legislature |
| US-MIS5-005 | Michigan Legislature |
| US-MIS5-006 | Michigan Legislature |
| US-MIS5-007 | Michigan Legislature |
| US-MIS5-008 | Michigan Legislature |
| US-MIS5-009 | Michigan Legislature |
| US-MIS5-010 | Michigan Legislature |
| US-MIS5-012 | Michigan Legislature |
| US-MIS5-013 | Michigan Legislature |
| US-MIS5-014 | Michigan Legislature |
| US-MIS5-015 | Michigan Legislature |
| US-MIS5-016 | Michigan Legislature |
| US-MIS5-018 | Michigan Department of Treasury |
| US-MIS5-019 | Michigan Department of Treasury |
| US-MIS5-021 | Michigan Department of Treasury |
| US-MIS5-022 | Michigan LEO - Unemployment Insurance Agency |
| US-MIS5-023 | Michigan Legislature |
| US-MIS5-025 | Michigan LEO - Unemployment Insurance Agency |
| US-MIV6-001 | Michigan Legislature |
| US-MIV6-002 | Michigan Legislature |
| US-MIV6-003 | Michigan Legislature |
