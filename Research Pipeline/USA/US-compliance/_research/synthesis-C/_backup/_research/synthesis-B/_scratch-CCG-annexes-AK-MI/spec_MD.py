NAME = 'Maryland'
SUMMARY = 'Minimum wage 15.00 (not indexed; under-18 85%); county minimum wages Montgomery 18.00/16.50/15.95, Howard 16.00, Prince George\'s 15.30 from 2026-07-01. State tax 2%-6.50% (new 6.25/6.50 bands) plus county-of-residence local tax piggybacked on MW506 (T3); percentage method with 3,200 exemption and 3,400 standard deduction, ten local tables (2.25-3.30, use equal-or-next-higher); nonresident special 2.25%; reciprocity DC/PA/VA/WV. UI base 8,500, Table A 0.30%-7.50%, new 1.0-2.6%. FAMLI contributions from 2027 (0.9%, 0.45/0.45). LE 3-504 pay statement + ESSL balance; SSN may NOT appear on check/stub.'
U = 'USD'
G = 'US-MDS5-021'
FACTS = [
 ('labour_code','md.minwage.hourly',15.00,'US-MDS5-005','2024-01-01',None,{'u':U,'n':'All sizes; not indexed; no 2027 step.'}),
 ('labour_code','md.minwage.under18.percent',85,'US-MDS5-005','2024-01-01',None,{'u':'percent','n':'= 12.75 [US-MDS5-015].'}),
 ('labour_code','md.minwage.tipped.cash_wage',3.63,'US-MDS5-007','2026-01-01',None,{'u':U,'n':'Max tip credit 11.37; restaurant Tip Credit Wage Statement each pay period.'}),
 ('labour_code','md.local_minwage.montgomery.51_plus',18.00,'US-MDS5-015','2026-07-01',None,{'u':U,'c':'medium','n':'DOL page only (ordinance unread). 11-50 employees (and 501(c)(3)/Medicaid home care 11+) 16.50; <= 10 15.95; CPI-W Washington-Baltimore July 1; under 19 <= 20 h/week excluded; under 20 at 85% first 6 months; tipped cash 4.00.'}),
 ('labour_code','md.local_minwage.montgomery.11_50',16.50,'US-MDS5-015','2026-07-01',None,{'u':U,'c':'medium'}),
 ('labour_code','md.local_minwage.montgomery.10_or_fewer',15.95,'US-MDS5-015','2026-07-01',None,{'u':U,'c':'medium'}),
 ('labour_code','md.local_minwage.howard',16.00,'US-MDS5-015','2026-07-01',None,{'u':U,'c':'medium'}),
 ('labour_code','md.local_minwage.prince_georges',15.30,'US-MDS5-015','2026-07-01',None,{'u':U,'c':'medium'}),
 ('labour_code','md.overtime.weekly_threshold_hours',40,'US-MDS5-006','2026-01-01',None,{'u':'hours','n':'No daily OT; 48 h bowling and non-hospital residential care; 60 h FLSA-exempt agriculture.'}),
 ('labour_code','md.pay_frequency.rule','at least every 2 weeks or twice a month (EAP less often); nonworkday payday moves to preceding workday','US-MDS5-008','2026-01-01',None,{}),
 ('labour_code','md.payment.method','cash or check at face value; direct deposit only with authorisation; pay card only with authorisation and fees disclosed in writing in >= 12-point type','US-MDS5-008','2026-01-01',None,{}),
 ('income_tax','md.pit.rates','2 / 3 / 4 / 4.75 / 5 / 5.25 / 5.5 / 5.75 / 6.25 / 6.50 percent (TG 10-105); single 6.25% > 500,000 and 6.50% > 1,000,000; joint 6.25% > 600,000 and 6.50% > 1,200,000','US-MDS5-001','2025-01-01',None,{'n':'6.25/6.50 bands from 2025 BRFA (new for 2026 withholding) [US-MDS5-003]. 2% capital-gain surcharge at assessment only.'}),
 ('income_tax','md.pit.top_rate',6.50,'US-MDS5-001','2025-01-01',None,{'u':'percent'}),
 ('income_tax','md.wh.method','wages - standard deduction - exemptions x per-period exemption; apply the local table that equals or slightly exceeds the county rate (tables start at 4.75%, ignoring 2/3/4% bands); ten tables 2.25, 2.40, 2.65, 2.75, 2.85, 3.00, 3.05, 3.10, 3.20, 3.30',G,'2026-01-01','2026-12-31',{'vm':'derived arithmetically','n':'3.30 table single bases 8,050 / 10,125 / 12,262.50 / 21,062.50 / 43,687.50 / 91,437.50 reproduce from state band + 3.30; joint exact. Per-period: weekly 61.54/65.38, monthly 266.67/283.33; biweekly 130.76 and semimonthly 141.66 TRUNCATED; daily /365 8.77/9.31.'}),
 ('income_tax','md.wh.exemption.annual',3200,G,'2026-01-01','2026-12-31',{'u':U}),
 ('income_tax','md.wh.std_deduction',3400,G,'2026-01-01','2026-12-31',{'u':U,'n':'TG 10-217: 3,350 indexed from 2026 rounding down to 50 [US-MDS5-002]; 3,400 consistent; Comptroller COLA figure not read.'}),
 ('income_tax','md.wh.floor.annual',5000,G,'2026-01-01','2026-12-31',{'u':U,'n':'No withholding below weekly 96, biweekly 192, semimonthly 208, monthly 417, daily 13.70, annual 5,000.'}),
 ('income_tax','md.wh.certificate','MW507 (MW507M military spouse, MW507P annuity/sick pay); none filed = one exemption; unknown county default 3.30% (state payroll memo)',G,'2026-01-01',None,{}),
 ('income_tax','md.wh.supplemental.lump_sum_bonus','top state rate 6.50% + county top local rate (e.g. 9.80% in 3.30 table; 9.70% in 3.20 table); no flat rate for other supplemental pay; computed in cents (retirement whole dollars)',G,'2026-01-01','2026-12-31',{}),
 ('local_tax','md.local.county_rate.default_unknown',3.30,'US-MDS5-003','2026-01-01','2026-12-31',{'u':'percent','n':'New county maximum from TY2026.'}),
 ('local_tax','md.local.county_rates','2.25 Worcester (24), out-of-state (25-76); 2.40 Talbot (21); 2.65 Garrett (12); 2.74 Cecil (08); 2.95 Washington (22); 3.03 Carroll (07), Charles (09); 3.06 Harford (13); 3.20 Allegany, Baltimore Co, Baltimore City, Calvert, Caroline, Howard, Montgomery, Prince George\'s, Queen Anne\'s, St. Mary\'s, Somerset, Wicomico; 3.30 Dorchester (10), Kent (15); graduated Anne Arundel (02) and Frederick (11)','US-MDS5-003','2026-01-01','2026-12-31',{'vm':'second independent authority','n':'Cross-checked with DLS [US-MDS5-004]; Allegany 3.03 -> 3.20, Kent 3.20 -> 3.30 vs 2025.'}),
 ('local_tax','md.local.anne_arundel.single','2.70 to 50,000 / 2.94 to 400,000 / 3.20 over (joint 2.70 to 75,000 / 2.94 to 480,000 / 3.20 over)','US-MDS5-003','2026-01-01','2026-12-31',{}),
 ('non_resident','md.nonres.special_rate',2.25,G,'2026-01-01','2026-12-31',{'u':'percent','n':'Residents of nonreciprocal states: state rate + special nonresident 2.25%, no local; flat nonresident 7.0% (4.75 + 2.25). Reciprocal DC/PA/VA/WV exempt with MW507 [US-MULTI-008], lost if MD abode > 6 months AND 183+ days (not WV). MD residents working in DE/nonreciprocal: Delaware table with local + credit.'}),
 ('non_resident','md.reciprocity.states','DC, PA, VA, WV',G,'2026-01-01',None,{}),
 ('social_security','md.sui.employer.rate.min',0.30,'US-MDP9V-001','2026-01-01','2026-12-31',{'u':'percent','n':'Experience 0.30-7.50%; standard 7.50%; foreign construction contractors industry average.'}),
 ('social_security','md.sui.employer.rate.max',7.50,'US-MDP9V-001','2026-01-01','2026-12-31',{'u':'percent'}),
 ('social_security','md.sui.new_employer.rate.range','1.0% - 2.6%','US-MDP9V-001','2026-01-01','2026-12-31',{}),
 ('social_security','md.pfml.contributions.start','2027-01-01 (no contribution in 2026)','US-MDS5-014','2027-01-01',None,{}),
 ('social_security','md.pfml.rate.total',0.9,'US-MDS5-014','2027-01-01',None,{'u':'percent','n':'0.45 employer + 0.45 employee (employer may withhold up to 50%); wages to SS base; < 15 employees (all locations, one EIN) remit employee share only; cap 1.2%; quarterly with wage-and-hour report, first due 2027-04-30; coverage follows UI localization (LE 8-202) [US-MDS5-019]; benefits from 2028-01-01 up to 1,000/week, 12 weeks.'}),
 ('social_security','md.pfml.employee_share.max_percent',50,'US-MDS5-014','2027-01-01',None,{'u':'percent'}),
 ('social_security','md.pfml.small_employer.threshold',15,'US-MDS5-014','2027-01-01',None,{'u':'employees'}),
 ('payslip_statute','md.payslip.essl_balance.required',True,'US-MDS5-013','2026-01-01',None,{'n':'LE 3-1305(f): available ESSL balance each time wages are paid (online system satisfies). Core LE 3-504 content on legacy row US-MD-P5-1-005.'}),
 ('data_protection','md.payslip.ssn.prohibited',True,'US-MDS5-008','2026-01-01',None,{'n':'LE 3-502(d): SSN may not be printed on the wage check, any attachment, direct-deposit notice or card-credit notice; covers governmental units; no truncation safe harbour - treat truncated SSN as barred.'}),
 ('data_protection','md.records.withholding.retention_years',3,G,'2026-01-01',None,{'u':'years'}),
 ('reporting_instruments','md.report.wh.mw506','MW506 on Maryland Tax Connect: accelerated (15,000+ prior year and 700+ accumulated, within 3 business days); monthly (> 700 in any quarter, 15th); quarterly (< 700/quarter); seasonal (approval); annual (< 250/yr, Jan 31); amendments MW506A/AM; final MW506FR; CRA registration (8-digit CRN)',G,'2026-01-01',None,{}),
 ('reporting_instruments','md.report.annual.mw508','MW508 + W-2s due 31 January; electronic mandatory at 25+ W-2s (TG 13-706.1; 100 penalty); SSA EFW2 modified MD format by bulk upload; RS FEIN 328-336, CRN 338-345; RV = MW508 with NAICS 333-338; date-time stamp 497-512; zero MW508 required for open accounts','US-MDS5-016','2025-01-01',None,{'n':'TY2025 spec ("layouts unchanged"); TY2026 not posted.'}),
 ('reporting_instruments','md.report.w2.efile_threshold',25,'US-MDS5-016','2025-01-01',None,{'u':'forms'}),
 ('reporting_instruments','md.report.sui.quarterly','BEACON within 1 month after quarter end; online, CSV, XML, ICESA or EFW2 (spec 2026-04-20); cents without decimal point; adjustment codes 00-10; 35 per late report; 1.5%/month interest; optional out-of-state taxable wages field','US-MDS5-017','2026-04-20',None,{}),
 ('reporting_instruments','md.newhire.report_days',20,'US-MDS5-018','2026-01-01',None,{'u':'days','n':'LE 8-626.1: SSN, name, address, hire date, employer name/address, starting wage, employer health insurance offered, FEIN, MD UI account; penalty warning then 20/month (500 conspiracy).'}),
 ('leave','md.leave.essl.paid_employer_threshold',15,'US-MDS5-013','2026-01-01',None,{'u':'employees','n':'HWFA LE 3-1301..1311: 15+ paid, <= 14 unpaid; 1 h per 30 h; caps earn 40 / use 64 / balance 64; use after 106 days; no accrual in periods < 24 h (biweekly) / 26 h (semimonthly); carryover 40 or front-load; rehire within 37 weeks reinstated; no payout; advanced leave recoverable with signed agreement; excluded < 12 h/week, under 18, agricultural, certain temps; post-2017 local laws pre-empted (Montgomery survives).'}),
 ('leave','md.leave.essl.accrual.hours_worked_per_hour',30,'US-MDS5-013','2026-01-01',None,{'u':'hours'}),
 ('leave','md.leave.essl.annual_earn_cap_hours',40,'US-MDS5-013','2026-01-01',None,{'u':'hours'}),
 ('leave','md.leave.essl.use_cap_hours',64,'US-MDS5-013','2026-01-01',None,{'u':'hours'}),
 ('termination','md.final_pay.rule','on or before next regular payday, discharge or resignation; accrued vacation payable unless written policy limits payout, employee notified at hire and policy denies it; ESSL not payable','US-MDS5-010','2026-01-01',None,{}),
 ('deductions_garnishments','md.deductions.rule','only if court-ordered, authorised in writing, allowed by the Commissioner or required by law (LE 3-503)','US-MDS5-009','2026-01-01',None,{}),
 ('deductions_garnishments','md.garn.creditor.weekly_exempt_floor',450.00,'US-MDS5-011','2024-01-01',None,{'u':U,'vm':'derived arithmetically','n':'CL 15-601.1: greater of 75% of disposable or 30 x State MW x weeks = 30 x 15.00; medical insurance deductions also exempt; per pay period.'}),
 ('collective_agreements','md.prevailing_wage.threshold',250000,'US-MDS5-012','2026-01-01',None,{'u':U,'n':'Not for Davis-Bacon-funded parts; extends to TIF-bond construction and mechanical systems service contracts above SCA threshold.'}),
 ('live_change','md.live.county_rates_2026','county maximum 3.30% from TY2026 (Dorchester, Kent 3.30; Allegany 3.20); level withholding','US-MDS5-004','2026-01-01',None,{}),
]
LEGACY = [('social_security','md.sui.wage_base',8500,'US-MD-P5-1-002','2026-01-01',None,'Not indexed; employer-only; other-state credit implied by BEACON field.'),('payslip_statute','md.payslip.items','employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online (LE 3-504); notice at hire and change one pay period ahead','US-MD-P5-1-005','2026-01-01',None,'')]
CITED = ['US-MDS5-019','US-MDS5-020','US-MD-P5-1-001','US-MD-P5-1-002','US-MD-P5-1-003','US-MD-P5-1-006','US-MDP9V-002','US-MDP9L-001','US-MDP9L-002','US-MDL-001','US-MULTI-008']
NARR = {
 'income_tax': 'Oracle: the Comptroller online withholding calculator and the Central Payroll Bureau Net Pay Calculator are referenced [US-MDS5-003] but were not run; the 3.30-table base reproduction is the arithmetic proof.',
 'social_security': 'No SDI/TDI; no other levy beyond withholding [US-MDP9V-002].',
 'benefits_in_kind': 'MD withholding wages track federal; non-cash at FMV; tips are wages [US-MDS5-021]. No departure found for 401(k)/125/HSA/transit/GTL; TG 10-203/204 not read (70%).',
 'collective_agreements': 'Rates set by the Commissioner [US-MD-P5-1-006 legacy]; certified-payroll duty (SFP 17-220) not read.',
 'indexation': 'State MW fixed; Montgomery CPI-W July 1; std deduction IRC 1(f)(3) COLA from TY2026 rounded down to 50; brackets/exemption statutory; county rates set by counties (max 3.30); SUI base fixed, table yearly; FAMLI rate yearly from Nov 2027; garnishment floor follows MW.',
 'live_change': '2026 BRFA postponement of taxable-income changes to TY2027 rests on a tier-B summary (no number, Q10).',
}
SPECIAL = '''- Domestic: MD withholding not required (private home, college club, fraternity); UI domestic threshold unread [US-MDS5-021].
- Agricultural: withheld when subject to FICA; UI 20,000/quarter or 10 in 20 weeks; OT after 60 h FLSA-exempt farm work; ESSL excluded [US-MDS5-021, US-MDS5-020, US-MDS5-006, US-MDS5-013].
- Minors: 85% under 18; Montgomery under 19/20 rules; ESSL excludes under 18 [US-MDS5-005, US-MDS5-015, US-MDS5-013].
- Tipped: 3.63 (Montgomery 4.00); Tip Credit Wage Statement; ESSL paid at not more than MW [US-MDS5-007, US-MDS5-015, US-MDS5-013].
- Clergy: withholding not required; churches/ministers outside UI [US-MDS5-021, US-MDS5-020].
- Students: below filing threshold (15,750 / 17,750 65+) may be exempt; own-school, camp (< 13 weeks), work-study UI-excluded [US-MDS5-021, US-MDS5-020].
- NRAs: general nonresident treatment [US-MDS5-021]. Nonresident seamen: not withheld in MD port.
- Commission workers: insurance producers, real estate, yacht salespersons, direct sellers etc. UI-excluded [US-MDS5-020].
- Government: withholding applies; elected officials/legislators/judges/Guard etc. UI-excluded [US-MDS5-020].
- Military spouses: MW507M. Low earners < 5,000/yr: no withholding [US-MDS5-021].'''
LANG = 'LE 3-1301..3-1311 has no language clause [US-MDP9L-001, US-MDP9L-002]; payslip English (US-OWN-006).'
UNRES = [
 {'key':'md.report.w2.spec_next_edition','why':'TY2026 Maryland W-2/MW508 EFW2 spec not posted.','close':'"2026 Maryland Employer Reporting of W2s Instructions and Specifications" on marylandcomptroller.gov /tax/instructions/2026/.'},
 {'key':'md.sui.wage_base.other_state_credit','why':'Implied by the BEACON "Out of State taxable wages" field only; taxable-wages statute not located (LE 8-101, 8-606 read).','close':'The LE Title 8 taxable-wage section on mgaleg.'},
 {'key':'md.leave.essl.multistate_scope','why':'Whether the 12 h/week threshold and accrual count MD hours only.','close':'COMAR 09.12.80 or DOL HWFA FAQ.'},
 {'key':'md.leave.essl.montgomery','why':'Montgomery County Code ch. 27 Art. XIII (pre-2017 ESSL) not read.','close':'County code text on codelibrary.amlegal.com.'},
 {'key':'md.records.wagehour.retention','why':'LE 3-424 record period and e-delivery consent not read.','close':'LE 3-424 on mgaleg.','blocking':False},
 {'key':'md.termination.ui_separation_notice','why':'COMAR 09.32.01 separation notice and Economic Stabilization Act (LE 11-301) not read.','close':'Those texts.','blocking':False},
 {'key':'md.pit.conformity','why':'TG 10-203/204/205 and annual IRC conformity act not read.','close':'Those sections.'},
 {'key':'md.garn.iwo_and_salary_lien','why':'IWO employer fee/remittance (FL 10-123/10-128) and Comptroller salary lien (TG 13-811) not read.','close':'Those sections on mgaleg.'},
 {'key':'md.prevailing_wage.certified_payroll','why':'SFP 17-220 certified payroll duty not read.','close':'SFP 17-220 on mgaleg.','blocking':False},
 {'key':'md.live.brfa2026','why':'2026 BRFA effect on TY2027 taxable income/withholding rests on tier-B summary.','close':'2026 BRFA as enacted or a Comptroller 2027 withholding alert.'},
 {'key':'md.sui.domestic_coverage','why':'LE Title 8 domestic-service threshold (expected 1,000/quarter) not verified.','close':'The LE 8-2xx domestic service section.','blocking':False},
 {'key':'md.local_minwage.ordinances','why':'County ordinances not read (montgomerycountymd.gov 404); figures from DOL page only.','close':'Montgomery, Howard and Prince George\'s ordinance/notice pages.','blocking':False},
]
