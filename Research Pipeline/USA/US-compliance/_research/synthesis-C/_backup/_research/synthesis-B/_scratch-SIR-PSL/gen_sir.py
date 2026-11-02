import sys
sys.path.insert(0, r"C:/Users/INSTIT~1/AppData/Local/Temp/claude/C--Users-instituto-Documents-brain-service-frentes-eua/272453a3-1ad8-4a54-b824-fda2544cbf81/scratchpad/synthB")
from gen_common import build, write, BASE

S = []
def F(key, value, rid, **kw):
    d = {'key': key, 'value': value, 'rid': rid}; d.update(kw); S.append(d)
D = 'days'; N = 'forms'; E = 'employees'

# ---------------- FEDERAL ----------------
F('sir.fed.agent_authorization.form', 'Form 8655 Reporting Agent Authorization (Rev. 1-2024), one per EIN', 'US-FED-028')
F('sir.fed.agent_authorization.returns', 'Line 15: 940, 941, 943, 944, 945, 1042, CT-1; line 16 deposits; line 19 extends the authorisation to state/local returns related to lines 15/16', 'US-FED-028')
F('sir.fed.agent_authorization.employer_liability_retained', True, 'US-FED-008', note='Rev. Proc. 2012-32 sec. 5.05: the authorisation does not relieve the taxpayer of responsibility or liability for timely filing and deposit; agent gives a written statement at engagement and at least quarterly. Level: employer reporting/deposit.')
F('sir.fed.agent_authorization.revision', 'Form 8655 current revision January 2024; related Pub. 1474 (Rev. 4-2026) and Rev. Proc. 2012-32', 'US-FED-009')
F('sir.fed.reporting_agent.tech_spec', 'Pub. 1474 (Rev. 4-2026): reporting agent = accounting service, franchiser, bank, service bureau or other payroll-services entity; agent list additions/deletions electronic above 100 submissions a week via SLFT B2B; deposits via EFTPS or FTA', 'US-FIL-001')
F('sir.fed.third_party_payer.rules', 'Pub. 15 (2026) third-party payer arrangements (reporting agents, sec. 3504 agents, CPEOs) - liability allocation per arrangement', 'US-FED-P5-1-002', conf='medium')
F('sir.fed.deposit.lookback_period', '2024-07-01 to 2025-06-30 for calendar 2026', 'US-FEDS5-004')
F('sir.fed.deposit.monthly_max_lookback_liability', 50000, 'US-FEDS5-004', cur='USD', note='50,000 or less in the lookback = monthly depositor (15th of next month); more = semiweekly (Wed/Thu/Fri paydays -> next Wednesday; Sat-Tue -> next Friday).')
F('sir.fed.deposit.next_day_threshold', 100000, 'US-FEDS5-004', cur='USD', note='Any day with 100,000 or more accumulated: deposit next business day.')
F('sir.fed.941.due', 'Quarterly, last day of the month after the quarter; amounts in cents; 944 only on IRS written notice (liability 1,000 or less)', 'US-FEDS5-004', conf='medium', note='941/944 mechanics per FED stage-5 findings citing the deposit row; 941 form instructions row US-FED-005.')
F('sir.fed.w2.due_ty2026', '2027-02-01 to SSA and employees', 'US-FEDS5-007')
F('sir.fed.w2.format', 'EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online', 'US-FIL-002', note='TY2026 record layout itself NOT read (26efw2.pdf gated, US-FIL-003 / US-FEDS5-032).')
F('sir.fed.new_hire.days', 20, 'US-FEDS5-024', uom=D, note='42 U.S.C. 653a: name, address, SSN, first day of work; employer name, address, FEIN; electronic filers may send two monthly transmissions 12-16 days apart; multistate employers may designate one state.')
F('sir.multi.new_hire.single_state_election', 'Electronic multistate employers may report all new hires to one designated state after notifying HHS in writing', 'US-MULTIS5-006')
F('sir.multi.w2.state_boxes', 'W-2 boxes 15-20: up to two states and two localities per form; additional W-2 for more', 'US-MULTIS5-011')

# ---------------- STATES ----------------
# AK
F('sir.ak.withholding.return', 'none: no state wage tax', 'US-AK-WT-001')
F('sir.ak.ui.wage_report', 'TQ01C quarterly with wage schedule, due last day of month after quarter; per employee SSN, name, wages, 6/8-digit occupational code and 2-digit geographic code; CSV upload (no headings), ES Tax portal or paper', 'US-AKS5-013')
F('sir.ak.ui.online_mandate', 'Online filing mandatory with 50+ employees in a quarter, 1M+ taxable wages, or when a payroll agent files', 'US-AKS5-005')
F('sir.ak.ui.csv_layout', 'Header record 11 columns + wage detail record 12 columns (rev. 2016-05-17)', 'US-AKS5-014')
F('sir.ak.ui.agent_authorization', 'UI Tax Power of Attorney (Rev. 7/24), eight checkable areas', 'US-AK-P5-1-006')
F('sir.ak.new_hire.days', 20, 'US-AKS5-007', uom=D)
# AL
F('sir.al.withholding.returns', 'A-6 monthly (if >1,000 withheld in month 1 or 2 of quarter, due 15th); A-1 quarterly; A-3 annual reconciliation + W-2s by 31 January; My Alabama Taxes', 'US-ALS5-001')
F('sir.al.w2.format', 'EFW2 RS record only, 512 bytes; RS includes federal income tax withheld cols 298-307', 'US-ALS5-006')
F('sir.al.w2.efile_threshold', 10, 'US-ALS5-006', uom=N)
F('sir.al.ui.wage_report', 'Quarterly Contribution and Wage Report via eGov (online_form or file_upload); computer-generated paper not accepted; corrections UC-10C', 'US-ALS5-007')
F('sir.al.ui.agent_authorization', 'Department of Workforce UC Power of Attorney (rev. 02/2025): TAX, BENEFITS, TAX AND BENEFITS, TAX REPORTS ONLY', 'US-AL-P5-2-002')
F('sir.al.new_hire.days', 7, 'US-ALS5-008', uom=D, note='Electronic: twice a month 12-16 days apart; electronic mandatory for 5+ employees.')
F('sir.al.local.occupational_tax', 'Municipal occupational taxes filed with each city/county or its agent (e.g. Leeds via Avenu, Birmingham via HdL)', 'US-ALS5-017')
# AR
F('sir.ar.withholding.returns', 'AR941M monthly by 15th (new registrations); AR941A annual by 31 Jan if under 1,000; AR3MAR annual reconciliation 28 Feb; EFT mandatory at 20,000/month average', 'US-AR-P5-1-002')
F('sir.ar.w2.format', 'EFW2 (RA, RE, RW, RS, RT, RF, RCS required; RV not allowed) via ATAP bulk upload, due 31 Jan with ARW-3', 'US-AR-P5-1-002')
F('sir.ar.w2.efile_threshold', 125, 'US-AR-P5-1-002', uom=E, note='Read in the registered local file (DFA instructions: employers with 125 or more employees are required to file electronically), not in the row summary text.')
F('sir.ar.ui.wage_report', 'Quarterly via Tax21 or paper (DWS-ARK-209B); e-file mandatory at 250+ employees', 'US-ARP9V-001')
F('sir.ar.withholding.agent_authorization', 'DFA Power of Attorney (rev. September 2025)', 'US-AR-P5-2-003')
F('sir.ar.new_hire.days', 20, 'US-ARP9V-001', uom=D)
# AZ
F('sir.az.withholding.returns', 'A1-QRT quarterly (even zero); A1-R annual reconciliation with W-2s by 31 Jan; A1-APR annual payment filers under 200; EFT at 500+', 'US-AZ-P5-2-005')
F('sir.az.w2.format', 'Electronic mandatory: EFW2 .txt via AZTaxes/AZFSET or transmitter; RS required, RV optional, state code 04; SSN/EIN not truncated', 'US-AZS5-025', conf='medium')
F('sir.az.withholding.agent_authorization', 'Form 821-PSC Withholding Tax Payroll Service Company Authorization', 'US-AZ-P5-2-001')
F('sir.az.ui.agent_authorization', 'DES UIT-1146A Limited Power of Attorney', 'US-AZ-P5-2-002')
F('sir.az.new_hire.days', 20, 'US-AZS5-012', uom=D)
# CA
F('sir.ca.ui_pit.returns', 'DE 9 + DE 9C quarterly, electronic only (per employee subject wages, PIT wages, PIT withheld); DE 88 deposits on the federal schedule; no annual reconciliation; W-2 NOT filed with EDD/FTB', 'US-CAS5-018')
F('sir.ca.agent_authorization', 'DE 48 Power of Attorney Declaration (e-Services or mail)', 'US-CA-EDD-006')
F('sir.ca.de9c.efile_spec', 'DE 8300 e-file guide: Upload Bulk Return File (zip <=10 MB) XML, ICESA or MMREF-1, CSV, or FSET XML web service', 'US-FIL-006')
F('sir.ca.new_hire.days', 20, 'US-CAS5-002', uom=D, note='DE 34; rehire after 60+ days separation; contractors on DE 542.')
# CO
F('sir.co.withholding.returns', 'Quarterly (<7,000/yr), monthly (7,000-50,000), weekly (>=50,000, EFT); zero returns required; DR 1094 paper', 'US-COS5-006')
F('sir.co.w2.filing', 'Due 31 Jan; e-file mandatory when federally required (10+ W-2s); Revenue Online .txt or CDOR XLSX template (10-100 employees)', 'US-COS5-013')
F('sir.co.withholding.agent_authorization', 'DR 0145 Tax Information Designation and Power of Attorney', 'US-CO-P5-1-006', conf='medium')
F('sir.co.ui.agent_authorization', 'TPA assigned online in MyUI Employer+ (Account Maintenance > TPA authorization)', 'US-CO-P5-2-003')
F('sir.co.local.denver_opt', 'Denver Occupational Privilege Tax withheld by employer, returned to Denver Treasury', 'US-CO-P5-2-001')
# CT
F('sir.ct.withholding.returns', 'CT-941 quarterly via myconneCT even with zero; remitter class weekly/monthly/quarterly by 12-month lookback; CT-W3 + all W-2s by 31 Jan (key-and-send, EFW2 upload or DRS CSV)', 'US-CTS5-013')
F('sir.ct.ui.wage_report', 'Quarterly via ReEmployCT (entry, upload, TPA, FSET); 276-character fixed-length S/T records; optional occupation, hours, worksite ZIP from Q3 2026', 'US-CTS5-032')
F('sir.ct.withholding.agent_authorization', 'DRS LGL-001 / LGL-003', 'US-CT-P5-1-007', conf='medium')
F('sir.ct.ui.agent_authorization', 'TPA Certificate of Representation (COR) and client link in ReEmployCT', 'US-CT-P5-2-002')
F('sir.ct.paid_leave.return', 'CT Paid Leave quarterly return via portal or batch XML/CSV', 'US-CTS5-022', note='File Specification Toolkit not downloaded.')
F('sir.ct.new_hire.days', 20, 'US-CTS5-019', uom=D)
# DC
F('sir.dc.withholding.returns', 'FR-900Q quarterly on MyTax.DC.gov (electronic mandatory since TY2023); FR-900A annual under 200; payments over 5,000 electronic', 'US-DCS5-014')
F('sir.dc.w2.format', 'EFW2/EFW2C with required RS record via MyTax.DC.gov, due 31 Jan; TY2025 edition read', 'US-DCS5-015', conf='medium')
F('sir.dc.w2.efile_threshold', 25, 'US-DCS5-015', uom=N)
F('sir.dc.ui.wage_report', 'UC-30 quarterly via DOES ESSP; machine-readable mandatory at 250+ employees; PFL same channel', 'US-DCS5-018')
F('sir.dc.withholding.agent_authorization', 'OTR D-2848', 'US-DC-P5-1-014')
F('sir.dc.ui.agent_authorization', 'DOES OUCTAX-1 Statutory Power of Attorney', 'US-DC-P5-2-003')
F('sir.dc.new_hire.days', 20, 'US-DCS5-022', uom=D)
# DE
F('sir.de.withholding.returns', 'Quarterly / monthly / eighth-monthly by July-June lookback (statutory 4,500 / 25,000, indexed); WTH-REC annual reconciliation with W-2s by end of January', 'US-DES5-005', note='2026 indexed thresholds not read.')
F('sir.de.w2.format', 'EFW2 with Delaware RS records via the Delaware Taxpayer Portal; SSN not truncated; paper only for 10 or fewer', 'US-DES5-008')
F('sir.de.ui.wage_report', 'UC-8 tax report + UC-8A wage report, quarterly, Online Employer Services Portal', 'US-DES5-011')
F('sir.de.ui.agent_authorization', 'DUI Power of Attorney (UI); withholding representation by IRS 2848 only', 'US-DE-P5-2-002')
F('sir.de.paid_leave.return', 'Quarterly Hours & Wage Report and contributions in Delaware LaborFirst', 'US-DES5-013')
F('sir.de.new_hire.days', 20, 'US-DES5-005', uom=D)
F('sir.de.local.wilmington', 'Wilmington earned income tax 1.25% collected by the City', 'US-DE-P5-2-001')
# FL
F('sir.fl.withholding.return', 'none: no income tax on natural persons', 'US-FL-001')
F('sir.fl.ui.wage_report', 'RT-6 quarterly; e-file and e-pay mandatory at 10+ employees in any quarter of the prior state fiscal year', 'US-FLS5-006')
F('sir.fl.ui.flat_file', 'Flat File Web Import v7 (Dec 2023): records 00/01/02/03/99, 2 implied decimals', 'US-FLS5-022')
F('sir.fl.ui.xml', 'FL_RT_XML_Schemas_v2026 1.0: 9 XSD, IRS efile transmission envelope; required above 20,000 employee records; sample validates (lxml)', 'US-FLS5-023')
F('sir.fl.agent_authorization', 'DR-835 Power of Attorney (section 4 RT agent); RTS-9 agent registration', 'US-FL-005')
F('sir.fl.new_hire.days', 20, 'US-FLS5-008', uom=D, note='FL also requires reporting non-employees paid 600+ within 20 days.')
# GA
F('sir.ga.withholding.returns', 'G-7 (semi-weekly / monthly / quarterly / annual by lookback); EFT and e-file mandatory once a G-7 exceeds 500', 'US-GAS5-002')
F('sir.ga.w2.filing', 'G-1003 + W-2s by 31 Jan (TY2026: 2027-02-01) via GTC, Excel/CSV template or EFW2 + GA RS; 1099s via IRIS XML only', 'US-GAS5-003')
F('sir.ga.ui.wage_report', 'DOL-4N quarterly; electronic required at 25+ employees; portal entry, CSV/Excel (100-15,000), SFTP (>15,000 and payroll service providers)', 'US-GAS5-005')
F('sir.ga.withholding.agent_authorization', 'RD-1061 POA, RD-1062 disclosure, RD-1063 Reporting Agent Authorization', 'US-GA-W1B-003')
F('sir.ga.ui.agent_authorization', 'GDOL power of attorney', 'US-GA-W1B-001')
F('sir.ga.new_hire.days', 10, 'US-GAS5-012', uom=D)
# HI
F('sir.hi.withholding.returns', 'HW-14 quarterly (15th after quarter) with VP-1 deposits quarterly/monthly/semi-weekly; W-2/HW-2 to DOTAX by 31 Jan', 'US-HIS5-005')
F('sir.hi.w2.efile_threshold', 10, 'US-HIS5-006', uom=N, note='From 2026-01-01 (TA 2025-05).')
F('sir.hi.ui.wage_report', 'UC-B6 quarterly, last day of month after quarter; bulk spec not located', 'US-HIS5-012')
F('sir.hi.withholding.agent_authorization', 'Form N-848 Power of Attorney', 'US-HI-P5-1-004', conf='medium')
F('sir.hi.ui.agent_authorization', 'Online employer profile authorises users (staff, CPA, service company) incl. UC-B6 filing', 'US-HI-P5-2-003')
F('sir.hi.new_hire.days', 20, 'US-HIS5-021', uom=D)
# IA
F('sir.ia.withholding.returns', 'Quarterly return via GovConnectIowa; deposits quarterly/monthly/semimonthly; no annual reconciliation (VSPs no longer filed)', 'US-IAS5-016')
F('sir.ia.w2.format', 'IDR-unique EFW2-based ASCII 512 bytes (SSA file rejected): RS state code 19, permit 248-267, Iowa RV total; e-file by 15 Feb, W-2s with Iowa withholding only', 'US-IAS5-017')
F('sir.ia.ui.wage_report', 'Contribution and Payroll Report 65-5300 + wage detail by SSN, electronic', 'US-IAS5-024', note='myIowaUI upload layout not acquired.')
F('sir.ia.withholding.agent_authorization', 'IA 2848 (14-101a, 06/18/2026)', 'US-IA-P5-1-003')
F('sir.ia.ui.agent_authorization', 'IWD 68-0092 Power of Attorney or Authorized Representative', 'US-IA-P5-1-004')
F('sir.ia.new_hire.days', 15, 'US-IAS5-012', uom=D)
# ID
F('sir.id.withholding.returns', 'Form 910 in TAP (semimonthly / monthly / quarterly / annual); Form 967 + W-2s last day of January', 'US-IDS5-009')
F('sir.id.w2.format', 'EFW2 plus Idaho state records uploaded in TAP (spec on STC developers page, not read)', 'US-IDS5-010', conf='medium')
F('sir.id.ui.wage_report', 'TX20 + TX26 quarterly, Employer Portal mandatory', 'US-IDS5-021')
F('sir.id.withholding.agent_authorization', 'Form ID-POA (withholding)', 'US-IDR3-001')
F('sir.id.ui.agent_authorization', 'IDOL Employer Portal Authorization form', 'US-IDR3-002')
F('sir.id.new_hire.days', 20, 'US-IDS5-015', uom=D)
# IL
F('sir.il.withholding.returns', 'IL-941 quarterly, electronic; no annual reconciliation; deposits monthly or semi-weekly (>12,000 lookback)', 'US-ILS5-011')
F('sir.il.w2.filing', 'Electronic only: MyTax (entry, CSV, EFW2 under IDR-996) or bulk EFW2 with ETIN (IDR-986); 2026 W-2s by 2027-02-01; 1099 bulk via IRIS from 2026-09-18', 'US-ILS5-013')
F('sir.il.ui.wage_report', 'UI-3/40 quarterly + monthly wage report for 25+ employees (months 1-2, MyTax CSV)', 'US-ILS5-017')
F('sir.il.ui.agent_authorization', 'IDES service bureau MOU with POA option; E-POA bulk file (caret-delimited, max 1000 rows/day)', 'US-IL-P5-2-010')
F('sir.il.withholding.agent_authorization', 'Form IL-2848 POA incl. withholding income tax accounts', 'US-IL-004', conf='medium')
F('sir.il.new_hire.days', 20, 'US-ILS5-018', uom=D)
# IN
F('sir.in.withholding.returns', 'WH-1 via INTIME (annual / monthly / early filer); WH-3 + W-2 by 31 Jan, electronic above 25 statements', 'US-INS5-010')
F('sir.in.w2.format', 'XML IDORWTH2016V1.0 for new filers; EFW2 for existing filers (RS 306-343 county code, local wages/tax); schema not downloaded', 'US-INS5-011', conf='medium')
F('sir.in.ui.wage_report', 'Quarterly via E S S/UPLINK; file upload (CSV or Indiana ICESA) required above 50; SOC code and start date per worker', 'US-INS5-014')
F('sir.in.withholding.agent_authorization', 'POA-1 or INTIME ePOA', 'US-INR3-003')
F('sir.in.ui.agent_authorization', 'Agent authorised in ESS at one of three levels (UI Agent Handbook)', 'US-INR3-004')
F('sir.in.new_hire.days', 20, 'US-INS5-016', uom=D)
# KS
F('sir.ks.withholding.returns', 'KW-5 each period (quad-monthly / semi-monthly / monthly / quarterly / annual); KW-3 + W-2s electronically by 31 Jan', 'US-KSS5-007')
F('sir.ks.w2.format', 'EFW2 with Kansas RS (K-2MT Rev. 10-25) or KW-2CSV; no CF/SF', 'US-KSS5-026')
F('sir.ks.w2.efile_threshold', 51, 'US-KSS5-026', uom=N)
F('sir.ks.ui.wage_report', 'Quarterly wage report and contribution return; MMREF/NASWA upload; e-file at 25+ employees (stricter reading of a self-contradicting page)', 'US-KSS5-022', conf='medium')
F('sir.ks.withholding.agent_authorization', 'DO-10 Power of Attorney', 'US-KS-P5-1-005')
F('sir.ks.ui.agent_authorization', 'K-CNS-032 TPA link form', 'US-KS-P5-2-003')
F('sir.ks.new_hire.days', 20, 'US-KSS5-019', uom=D, note='Statute says 20 business days (K.S.A. 75-5743); KDOL page says 20 days; statute governs.')
# KY
F('sir.ky.withholding.returns', 'MyTaxes: K-3 annual / K-1 quarterly / monthly / twice-monthly; zero returns required', 'US-KYS5-013')
F('sir.ky.w2.format', 'SSA EFW2 with DOR-defined RS or K-5; electronic at 26+ statements; paper W-2s not processed', 'US-KYS5-013')
F('sir.ky.ui.wage_report', 'Quarterly in KUIP (replaced KEWES 2026)', 'US-KYS5-019')
F('sir.ky.new_hire.recipient', 'Office of the Attorney General since 2025-07-01, within 20 days', 'US-KYS5-020')
F('sir.ky.local.occupational', 'Local occupational taxes administered by cities/counties/school districts (Louisville W-1/W-3; Lexington)', 'US-KY-P5-2-002')
# LA
F('sir.la.withholding.returns', 'L-1 quarterly electronic; L-3 + W-2s by first business day after 31 Jan via LaWage', 'US-LAS5-003')
F('sir.la.w2.efile_threshold', 50, 'US-LAS5-009', uom=N)
F('sir.la.ui.wage_report', 'Quarterly, mandatory electronic via LAWATS', 'US-LAS5-007', conf='medium')
F('sir.la.ui.agent_authorization', 'Online Power of Attorney in LAWATS', 'US-LA-P5-2-005')
F('sir.la.new_hire.days', 20, 'US-LAS5-010', uom=D)
# MA
F('sir.ma.withholding.returns', 'M-941 via MassTaxConnect: annual / quarterly / monthly / quarterly with 3-business-day accelerated payments by annual amount', 'US-MAS5-013')
F('sir.ma.w2.format', 'EFW2 RA/RE/RS/RT; RT must equal sum of RS; PDF/CSV refused; 50+ W-2s electronic', 'US-MAS5-019', conf='medium', note='Handbook served is Rev. 20191219.')
F('sir.ma.w2.due', '31 January (W-2 page and handbook); the Withholding Tax Guide says end of March for 50+ (conflict; Jan 31 recommended)', 'US-MAS5-015', conf='medium')
F('sir.ma.ui.wage_report', 'DUA quarterly wage detail by 3 p.m. on due date; CSV, EFW2 or ICESA; includes hours and state income tax withheld', 'US-MAS5-018')
F('sir.ma.agent_authorization', 'M-2848 (POA before DOR; no MassTaxConnect access); third-party access initiated by representative', 'US-MA-P5-1-007')
F('sir.ma.new_hire.days', 14, 'US-MAS5-016', uom=D)
# MD
F('sir.md.withholding.returns', 'MW506 on Maryland Tax Connect (accelerated / monthly / quarterly / seasonal / annual)', 'US-MDS5-021')
F('sir.md.w2.format', 'MW508 + W-2s by 31 Jan; modified Maryland EFW2 bulk upload; RS FEIN 328-336, CRN 338-345; RV=MW508 with NAICS', 'US-MDS5-016')
F('sir.md.w2.efile_threshold', 25, 'US-MDS5-016', uom=N)
F('sir.md.ui.wage_report', 'BEACON quarterly: online, CSV, XML, ICESA or EFW2 (spec 2026-04-20)', 'US-MDS5-017')
F('sir.md.withholding.agent_authorization', 'Form 548P limited POA / reporting agent authorization (Comptroller)', 'US-MD-P5-1-001')
F('sir.md.new_hire.days', 20, 'US-MDS5-018', uom=D, note='Adds starting wage, health-insurance offered, MD UI account number.')
# ME
F('sir.me.withholding.returns', '941ME quarterly electronic (Rule 104); semiweekly deposits at 18,000+ lookback; no W-3ME after TY2023', 'US-ME-P5-2-002')
F('sir.me.w2.filing', 'Electronic to MRS by 31 Jan, paper not accepted; Maine Tax Portal bulk spec not read', 'US-MES5-011')
F('sir.me.ui.wage_report', 'ME UC-1 quarterly via ReEmployME, filed with MRS', 'US-MES5-021')
F('sir.me.pfml.return', 'PFML quarterly wage report and premium in the PFML portal; third-party payroll designation in the portal', 'US-MES5-024')
F('sir.me.payroll_processor_licence', 'Payroll processors must hold a Bureau of Consumer Credit Protection licence', 'US-MES5-011')
F('sir.me.new_hire.days', 7, 'US-MES5-016', uom=D)
# MI
F('sir.mi.withholding.returns', 'SUW 5080 monthly/quarterly (20th); 5081 annual reconciliation 2027-02-28; accelerated EFT at 480,000+', 'US-MIS5-018')
F('sir.mi.ui.wage_report', 'MiUI quarterly (25th after quarter): CSV v3, ICESA v2, EFW2 v2, XML v1', 'US-MIS5-022')
F('sir.mi.withholding.agent_authorization', 'Treasury Form 151 Authorized Representative Declaration', 'US-MI-P5-2-011')
F('sir.mi.ui.agent_authorization', 'UIA 1488 Power of Attorney', 'US-MI-P5-2-005', conf='medium', note='A MANUAL lead says UIA 1488 is no longer required (TPA adds POA in MiUI); not confirmed.')
F('sir.mi.w2.filing', 'Due 31 Jan; 10+ forms via MTO in EFW2 / Pub 1220; W-2s not via CF/SF', 'US-MI-PIT-001')
# MN
F('sir.mn.withholding.returns', 'Quarterly via e-Services; W-2 info to DOR by 31 Jan; e-Services mandatory above 10 W-2+1099; bulk filers need each client MN ID', 'US-MNS5-010')
F('sir.mn.ui.wage_report', 'Quarterly wage detail electronic incl. paid hours (268.044)', 'US-MNS5-015')
F('sir.mn.paid_leave.return', 'Paid Leave quarterly wage detail and premium to DEED, electronic', 'US-MNS5-018')
F('sir.mn.withholding.agent_authorization', 'REV184b Business Power of Attorney', 'US-MN-P5-2-005')
F('sir.mn.ui.agent_authorization', 'UI Agent Self-Service ID (8-digit Agent ID)', 'US-MNP6-003')
F('sir.mn.new_hire.days', 20, 'US-MNS5-016', uom=D)
# MO
F('sir.mo.withholding.returns', 'MO-941 monthly / quarterly / annual; quarter-monthly payments at 9,000+', 'US-MOS5-001')
F('sir.mo.w2.efile_threshold', 250, 'US-MOS5-001', uom=N, note='EFW2 with RV carrying MO W-3 data.')
F('sir.mo.ui.wage_report', 'MODES-4 quarterly on UInteract (NASWA/ICESA); electronic at 50+ employees who e-file W-2 with SSA; spec M-INF-368', 'US-MOS5-013')
F('sir.mo.ui.agent_authorization', 'DES Power of Attorney (signed written agreement)', 'US-MO-P5-2-008')
F('sir.mo.new_hire.days', 20, 'US-MOS5-008', uom=D)
# MS
F('sir.ms.withholding.returns', '89-105 via TAP, 15th after the period; no depository; e-file at 20,000+ liability', 'US-MSS5-019')
F('sir.ms.w2.format', 'EFW2 RS (state code 28) via TAP; electronic at 10+ W-2s or when one payroll provider all year; Pub 89-145 Rev 10/25', 'US-MSS5-005')
F('sir.ms.ui.wage_report', 'UI-2 + UI-3 quarterly; ICESA S record (275) or EFW2 RS', 'US-MSS5-013')
F('sir.ms.ui.agent_authorization', 'MDES J-9 Reporting Agent Authorization', 'US-MS-P5-2-005')
F('sir.ms.new_hire.days', 15, 'US-MSS5-006', uom=D)
# MT
F('sir.mt.withholding.returns', 'Accelerated / monthly / annual deposits; MW-3 + all W-2s by 31 Jan via TAP (EFW2); truncated SSNs not accepted', 'US-MTS5-005')
F('sir.mt.ui.wage_report', 'Quarterly via UI eServices; electronic mandatory from 2025-07-01 (ARM 24.40.1609)', 'US-MTS5-025', conf='medium')
F('sir.mt.withholding.agent_authorization', 'Montana Form POA or federal 2848; third-party access in TAP', 'US-MTS5-005')
F('sir.mt.new_hire.days', 20, 'US-MTS5-012', uom=D)
# NC
F('sir.nc.withholding.returns', 'NC-5 quarterly/monthly, NC-5P semiweekly + NC-5Q; NC-3 + W-2s by 31 Jan via eNC3 (fixed-field .txt)', 'US-NC-001')
F('sir.nc.w2.spec_ty2026', 'TY2026 specs version 9-2026 (use beginning January 2027)', 'US-NCS5-028')
F('sir.nc.ui.wage_report', 'NCUI 101 via NCSUITS; electronic at 10+ wage items', 'US-NCS5-025')
F('sir.nc.ui.agent_authorization', 'DES Power of Attorney and Declaration of Representative (one per agent per employer)', 'US-NC-P5-1-003')
F('sir.nc.new_hire.days', 20, 'US-NCS5-020', uom=D)
# ND
F('sir.nd.withholding.returns', 'Form 306 quarterly; e-file if prior-year withholding 1,000+ or a provider e-files federally; Form 307 + W-2 EFW2 by 31 Jan', 'US-NDS5-002')
F('sir.nd.ui.wage_report', 'Quarterly via UI EASY or Secure FTP', 'US-NDS5-011')
F('sir.nd.withholding.agent_authorization', 'Form 500 Authorization to Disclose / Designation of Representative; payroll provider designated on registration', 'US-ND-P5-1-002')
F('sir.nd.new_hire.days', 20, 'US-NDS5-013', uom=D)
# NE
F('sir.ne.withholding.returns', '941N quarterly; 501N/EFT monthly deposits when >500 in month 1 or 2', 'US-NES5-010')
F('sir.ne.w2.format', 'W-3N + W-2 by 31 Jan; >50 forms via NebFile; EFW2 with NE RS (state code 31) and RV', 'US-NES5-017')
F('sir.ne.ui.wage_report', 'Combined Tax Report + Wage Report quarterly via NEworks online or FTP', 'US-NES5-011')
F('sir.ne.agent_authorization', 'DOR Form 33; NDOL UI POA', 'US-NE-P5-1-004', conf='medium')
F('sir.ne.new_hire.days', 20, 'US-NES5-014', uom=D)
# NH
F('sir.nh.withholding.return', 'none: no state wage tax', 'US-NH-006')
F('sir.nh.ui.wage_report', 'Quarterly Employer Tax and Wage Report via WebTax/NHUIS (2016 handbook figures)', 'US-NHS5-013', conf='medium')
F('sir.nh.ui.agent_authorization', 'Written request to NHES for an authorized agent; TPA registration in NHUIS', 'US-NHP6-001', conf='medium')
F('sir.nh.new_hire.days', 20, 'US-NHS5-006', uom=D, note='NH also requires non-casual contractors expected over 2,500.')
# NJ
F('sir.nj.withholding.returns', 'NJ-927 quarterly electronic; NJ-500 monthly; NJ-W-3 + W-2s by 15 Feb, electronic since TY2020', 'US-NJ-P5-1-001')
F('sir.nj.ui.wage_report', 'WR-30 quarterly, electronic (online or SFTP), due the 30th with no weekend extension', 'US-NJS5-017')
F('sir.nj.withholding.agent_authorization', 'M-5008-R Appointment of Taxpayer Representative (6/26)', 'US-NJR3-004')
F('sir.nj.ui.agent_authorization', 'NJ DOL Division of Employer Accounts Power of Attorney', 'US-NJR3-005')
F('sir.nj.new_hire.days', 20, 'US-NJS5-018', uom=D)
F('sir.nj.local.payroll_tax', 'Newark and Jersey City quarterly employer payroll tax returns', 'US-NJP6-001')
# NM
F('sir.nm.withholding.returns', 'TRD-41414 (25th after period) and new TRD-41431 quarterly from 2026-01-01; e-file mandate from 2026', 'US-NMS5-012')
F('sir.nm.w2.filing', 'Electronic only from 2026; TAP bulk TXT or CF/SF; due 31 Jan (FYI-330)', 'US-NM-P5-2-005', conf='medium')
F('sir.nm.ui.wage_report', 'Quarterly electronic only; Delimited, ICESA, XML, EFW2 published', 'US-NMS5-016')
F('sir.nm.withholding.agent_authorization', 'ACD-31102 Tax Information Authorization', 'US-NM-P5-1-004')
F('sir.nm.ui.agent_authorization', 'ES-905 Power of Attorney / Authorization of Agent or TPA login', 'US-NMP6-001')
F('sir.nm.new_hire.days', 20, 'US-NMS5-010', uom=D)
# NV
F('sir.nv.withholding.return', 'none: no state wage tax', 'US-NV-P5-1-001', conf='medium')
F('sir.nv.ui.wage_report', 'RPT3795 + NEW0098 quarterly in ESS (entry, SFTP EFW2, CSV/tab)', 'US-NVS5-008')
F('sir.nv.mbt.return', 'MBT TAX-F003 quarterly on My Nevada Tax; from 2026-01-01 MBT wages compared with ESD wages', 'US-NVS5-009')
F('sir.nv.ui.agent_authorization', 'Agent added as external ESS user', 'US-NVR3-003')
F('sir.nv.new_hire.days', 20, 'US-NVS5-007', uom=D)
# NY
F('sir.ny.nys45', 'NYS-45 quarterly combined withholding + wage reporting + UI; e-file and ACH mandatory; no W-2 filed with NY', 'US-NYS5-010')
F('sir.ny.bulk_spec', 'Pub. 72.5 (2/25) NYS-45 Web Upload: prior approval, test file, agent identification number', 'US-FIL-007')
F('sir.ny.new_hire.days', 20, 'US-NYS5-010', uom=D)
F('sir.ny.mctmt.return', 'MTA-305 quarterly', 'US-NY-003', conf='medium')
# OH
F('sir.oh.withholding.returns', 'IT 501 (quarterly / monthly / partial-weekly) and IT 941 by 31 Jan; W-2 upload by 31 Jan with school district code', 'US-OH-009', conf='medium')
F('sir.oh.bulk_filing', 'Bulk Filing Guide Part A: IT 501, IT 941, SD 101, SD 141, FSET v4.4; ETIN + OHID', 'US-FIL-012')
F('sir.oh.withholding.agent_authorization', 'WT 8655 Payroll Service Company Authorization', 'US-FIL-011')
F('sir.oh.representative', 'TBOR 1 Declaration of Tax Representative', 'US-OH-P5-2-005')
F('sir.oh.ui.agent_authorization', 'JFS-20106 Employer Representative Authorization', 'US-OHR3-001')
F('sir.oh.local.municipal', 'Municipal returns to each municipality/collector (monthly if >2,399 prior year or >200 in a month)', 'US-OH-P5-2-003')
# OK
F('sir.ok.withholding.returns', 'Quarterly return 20th after quarter via OkTAP; W-2 via EFW2 or entry by 31 Jan', 'US-OKS5-010')
F('sir.ok.ui.wage_report', 'OES-3 via EZ Tax Express; ICESA 275 E/S/T', 'US-OKS5-020', note='Statutory due date not confirmed (OK-OQ-1).')
F('sir.ok.withholding.agent_authorization', 'BT-129 Power of Attorney (Rev. 7-2026)', 'US-OK-P5-1-004')
F('sir.ok.ui.agent_authorization', 'OES-190T Appointment of Account Representative', 'US-OK-P5-1-005')
F('sir.ok.new_hire.days', 20, 'US-OKS5-007', uom=D)
# OR
F('sir.or.oq', 'Form OQ quarterly via Frances Online: withholding, UI, Paid Leave, WBF, TriMet, Lane, STT; Schedule B; Form 132', 'US-ORS5-010')
F('sir.or.w2.filing', 'OR-WR + W-2s via iWire (EFW2 or template) by 31 Jan', 'US-ORS5-010')
F('sir.or.local.portland_metro_multnomah', 'Quarterly returns and annual reconciliation on Portland Revenue Online; XML ReturnBatch 1.0; W-2 EFW2 by 31 Jan', 'US-ORS5-024')
F('sir.or.agent_authorization', 'OR-AUTH-REP / OR-AUTH-INFO', 'US-OR-P5-1-005', conf='medium')
F('sir.or.new_hire.days', 20, 'US-ORS5-016', uom=D)
# PA
F('sir.pa.withholding.returns', 'myPATH deposits; quarterly W-3; REV-1667 + W-2s by 31 Jan, electronic at 10+', 'US-PAS5-010')
F('sir.pa.ui.wage_report', 'UC-2 + UC-2A via UCMS; layout UC-2010 (ICESA/CSV)', 'US-FIL-008')
F('sir.pa.withholding.agent_authorization', 'REV-677 Power of Attorney (07-25)', 'US-FIL-010')
F('sir.pa.ui.agent_authorization', 'UCMS electronic TPA handshake (no paper POA)', 'US-PA-P5-1-004')
F('sir.pa.local.eit_lst', 'EIT/LST quarterly returns and W2-R to the collector; Philadelphia quarterly returns', 'US-PAS5-017')
F('sir.pa.new_hire.days', 20, 'US-PAS5-008', uom=D)
# RI
F('sir.ri.withholding.returns', 'Weekly/monthly/quarterly deposits; RI-941 quarterly; RI W-3 by 31 Jan; W-2 EFW2 with RS via Tax Portal', 'US-RIS5-018')
F('sir.ri.ui.wage_report', 'DLT TX-17 quarterly (UI/TDI/JDA); electronic wage data at 25+ employees', 'US-RIS5-017')
F('sir.ri.withholding.agent_authorization', 'RI-2848', 'US-RI-P5-1-004')
F('sir.ri.new_hire.days', 14, 'US-RIS5-010', uom=D)
# SC
F('sir.sc.withholding.returns', 'WH-1605 Q1-Q3 and WH-1606 Q4 + annual reconciliation via MyDORWAY', 'US-SCS5-002')
F('sir.sc.w2.format', 'EFW2 .txt with SC RS (state code 45, full SSN); electronic at 10+; filing with SSA does not satisfy SC', 'US-SCS5-016')
F('sir.sc.ui.wage_report', 'Quarterly via SUITS: ICESA, EFW2, XML or CSV (spec v1.6)', 'US-SCS5-006')
F('sir.sc.withholding.agent_authorization', 'SC2848', 'US-SC-P5-2-001')
F('sir.sc.ui.agent_authorization', 'UCE-1010 Written Authorization', 'US-SCR3-008', conf='low', note='Form text read only from a 2022 capture.')
F('sir.sc.new_hire.days', 20, 'US-SCS5-011', uom=D)
# SD
F('sir.sd.withholding.return', 'none: no state wage tax', 'US-SDS5-001', conf='medium')
F('sir.sd.ui.wage_report', 'Form 21 quarterly (online, CSV upload, CD/DVD 85-byte E/S)', 'US-SDS5-013')
F('sir.sd.ui.agent_authorization', 'RA POA Rev. 01/2026 (Tax, Benefits or Limited)', 'US-SD-P5-1-001')
F('sir.sd.new_hire.days', 20, 'US-SDS5-007', uom=D)
# TN
F('sir.tn.ui.wage_report', 'LB-0851 + LB-0456 quarterly in Employer e-Services (ICESA variants, 58-char text)', 'US-TNS5-005')
F('sir.tn.ui.agent_authorization', 'No POA needed since 2025-05-27; TPA uses manage-client link', 'US-TNR3-002')
F('sir.tn.new_hire.days', 20, 'US-TNS5-008', uom=D)
# TX
F('sir.tx.withholding.return', 'none: no state income tax', 'US-TXS5-001')
F('sir.tx.ui.wage_report', 'Electronic only: Unemployment Tax Services or QuickFile (ICESA, MMREF-1, delimited)', 'US-TX-SUI-006')
F('sir.tx.ui.agent_authorization', 'Form C-42 Written Authorization to Represent Employing Unit', 'US-TX-P5-2-008', conf='medium')
F('sir.tx.wage_report.enhanced_content', 'Labor Code 204.0025 (2025 amendments): wage, industry, occupation, FT/PT, county, remote status inside routine wage filings; implementing layout not read', 'US-TXS5-008', conf='medium')
F('sir.tx.new_hire.days', 20, 'US-TXS5-016', uom=D, note='OAG form; TWC page US-TXS5-017 states the same (second independent authority); statute 234.102 [US-TXS5-012].')
# UT
F('sir.ut.withholding.returns', 'TC-941E e-file only, quarterly (monthly payments at 1,000+); annual reconciliation with W-2s by 31 Jan', 'US-UTS5-013')
F('sir.ut.w2.format', 'EFW2 with RS required, RV optional; lowercase .txt; fixed-length mandatory at 250+', 'US-UTS5-014')
F('sir.ut.ui.wage_report', 'Quarterly Wage List and Contribution Report online only', 'US-UTS5-004')
F('sir.ut.withholding.agent_authorization', 'TC-737 Power of Attorney (Rev. 9/26)', 'US-UTP6-002')
F('sir.ut.ui.agent_authorization', 'DWS UI Power of Attorney (Rev. 08/24)', 'US-UTP6-003')
F('sir.ut.new_hire.days', 20, 'US-UTS5-003', uom=D)
# VA
F('sir.va.withholding.returns', 'VA-5 quarterly/monthly, VA-15/VA-16 semi-weekly; VA-6 by 31 Jan; all electronic', 'US-VAS5-013')
F('sir.va.w2.format', 'Web Upload EFW2 / Pub 1220 (state code 51) by 31 Jan; upload does not create VA-6', 'US-VAS5-009')
F('sir.va.ui.wage_report', 'VEC quarterly via ESS, eForm or Web Upload (Excel, MMREF/EFW2, ICESA, delimited)', 'US-VAS5-014')
F('sir.va.withholding.agent_authorization', 'PAR 101 (person, not business)', 'US-VA-P5-1-007')
F('sir.va.ui.agent_authorization', 'ESS TPA invitation; ID.me login from 2026-08-01', 'US-VAP6-001')
F('sir.va.new_hire.days', 20, 'US-VAS5-006', uom=D)
# VT
F('sir.vt.withholding.returns', 'WHT-436 quarterly (carries CCC); WHT-434 annual by 31 Jan, e-file at 10+ and always for payroll services; no CF/SF', 'US-VTS5-017')
F('sir.vt.ui.wage_report', 'Quarterly via Employer e-Services; hourly workers also gender and hourly wage', 'US-VTS5-007')
F('sir.vt.withholding.agent_authorization', 'Form PA-1 Special Power of Attorney', 'US-VT-P5-1-012')
F('sir.vt.ui.agent_authorization', 'Form C-50 Limited Power of Attorney', 'US-VT-P5-1-013')
F('sir.vt.new_hire.days', 10, 'US-VTS5-014', uom=D)
# WA
F('sir.wa.withholding.return', 'none: no income tax', 'US-WAS5-013', conf='medium')
F('sir.wa.ui.wage_report', 'ESD quarterly via EAMS/SAW: name, SSN, gross, hours, SOC code', 'US-WAS5-013')
F('sir.wa.ui.agent_authorization', 'UI power of attorney per client', 'US-FED-P5-1-016')
F('sir.wa.local.seattle_pet', 'Seattle payroll expense tax: Taxpayer Authorization Form per client', 'US-WA-P5-1-001')
F('sir.wa.new_hire.days', 20, 'US-WAS5-018', uom=D)
# WI
F('sir.wi.withholding.returns', 'WT-6 (DOR-assigned frequency), WT-7 by 31 Jan (TY2026 2027-02-01); electronic only', 'US-WIS5-011')
F('sir.wi.w2.format', 'EFW2 with RS (state code 55); 10+ electronic; no transmittal', 'US-WIS5-012')
F('sir.wi.ui.wage_report', 'Quarterly; electronic at 25+ employees (108.205(2))', 'US-WIS5-013')
F('sir.wi.withholding.agent_authorization', 'Form A-222 Power of Attorney', 'US-WI-P5-2-003')
F('sir.wi.ui.agent_authorization', 'UCT-8291-E Employer Power of Attorney Assignment', 'US-WI-P5-1-002')
F('sir.wi.provider_registration', 'Payroll service providers must register and test their software with DOR', 'US-WIS5-016')
F('sir.wi.new_hire.days', 20, 'US-WIS5-013', uom=D)
# WV
F('sir.wv.withholding.returns', 'IT-101Q quarterly (15th remittance); IT-103 + W-2s by 31 Jan, EFW2 with RS (54) and WV RV via MyTaxes', 'US-WVS5-010')
F('sir.wv.efile_threshold', 10, 'US-WVS5-013', uom=E, note='10+ employees or a payroll service, periods after 2024-12-31; Wayback statute copy says 25/50 (stale).')
F('sir.wv.ui.wage_report', 'Quarterly via UC Employer System; SOC/job title, county', 'US-WV-UI-001')
F('sir.wv.withholding.agent_authorization', 'WV-2848', 'US-WV-P5-1-006')
F('sir.wv.ui.agent_authorization', 'WorkForce WV Power of Attorney (Rev. 3.23)', 'US-WV-P5-2-006')
F('sir.wv.new_hire.days', 14, 'US-WVS5-016', uom=D)
# WY
F('sir.wy.withholding.return', 'none: no income tax', 'US-WY-P5-1-001')
F('sir.wy.ui.wage_report', 'WYUI quarterly (Apr 30 / Jul 31 / Oct 31 / Jan 31); file spec not read', 'US-WYS5-009')
F('sir.wy.service_supplier', 'PEO/service supplier files a separate quarterly report per client; client jointly liable (27-3-502)', 'US-WYS5-019')
F('sir.wy.ui.agent_authorization', 'POA form MODES-4444 (7/19)', 'US-WYR3-001', conf='medium')
F('sir.wy.new_hire.days', 20, 'US-WYS5-006', uom=D)

facts, blocked, unresolved, consumed = build(S, 'SIR', 'third_party_provider_handoff')

U = [
 ('sir.provider.selection', 'US-MQ-09 owner decision 2026-10-29: the filing provider is a business decision outside this build; vendor pages read are tier B and none states it accepts an external engine file', 'Owner/BAU RFP to candidate providers (6 questions: external file/API, IRS reporting agent, state POAs 50+DC, deposit account, local returns, SLA/penalty liability); provider-specific input spec then replaces the generic minimum data set'),
 ('sir.fed.efw2.layout_ty2026', 'ssa.gov 26efw2.pdf returned 403; Wayback 404 (US-FIL-003, US-FEDS5-032 gated)', 'SSA EFW2 Pub. 42-007 TY2026 PDF downloaded by the user in a browser'),
 ('sir.ny.withholding.agent_authorization', 'NY POA-1 not read (US-FIL-021 gated)', 'Form POA-1 from tax.ny.gov/poa read on the official host'),
 ('sir.me.withholding.agent_authorization', 'Form 2848-ME row US-ME-P5-1-004 is superseded; UC-28 row US-ME-P5-2-008 is MANUAL (edition 09/2013)', 'Current Maine Revenue Services Form 2848-ME and Maine DOL UC-28 read on maine.gov'),
 ('sir.ms.withholding.agent_authorization', 'DOR Form 21-002 text not read (US-MS-P5-1-006 MANUAL B)', 'Mississippi DOR Form 21-002 PDF read on dor.ms.gov'),
 ('sir.ky.agent_authorization', 'No Kentucky withholding POA or UI agent instrument located in the stage-5 findings', 'Kentucky DOR Form 20A100 and the KUIP TPA/agent authorization page'),
 ('sir.la.withholding.agent_authorization', 'R-7006 row US-LA-P5-1-006 is superseded and no active successor carries the form', 'Louisiana LDR Form R-7006 current edition read on revenue.louisiana.gov'),
 ('sir.wy.ui.agent_authorization_form_text', 'WY DWS POA form linked as Google Drive file is unreadable (US-WY-P5-2-003 gated)', 'WY DWS POA PDF downloaded by the user'),
 ('sir.ca.de9c.file_spec', 'DE 9C FSET/e-file field spec not fetched (CA open question 5)', 'EDD DE 8300 annexes / FSET schema download'),
 ('sir.in.w2.xml_schema', 'IDORWTH2016V1.0 schema not downloaded (ACCESS gap)', 'Indiana DOR XML schema archive, extracted and inspected'),
 ('sir.ct.paid_leave.file_spec', 'CT Paid Leave File Specification Toolkit PDF not downloaded', 'CTPL File Specification Toolkit from ctpaidleave.org'),
 ('sir.w2.state_specs_ty2026', 'TY2026 state W-2 editions not yet posted on 2026-11-02 for GA, MD, SC, WV, IA, KS, MS, DC (TY2025 editions read)', 'Re-check each state W-2 spec page in January 2027 before the first TY2026 file'),
 ('sir.ui.file_specs_missing', 'UI wage-file layouts not read for AZ (403), CO (403), IA, KY (KUIP), LA, MT, NE, NM (403), UT, WY, OK (due date 404)', 'One official spec per state, downloaded and inspected; parallel lookups'),
 ('sir.tx.ui.due_date', 'TWC rule 815.107 text ACCESS-blocked; due date only from tier-B leads', 'TWC rule 815.107 text (40 TAC 815) read on the official host'),
 ('sir.mi.new_hire.statute', 'Michigan new-hire statute and penalty not located (federal 20 days applies)', 'MCL 400.231 et seq. text on legislature.mi.gov'),
]
for k, why, close in U:
    unresolved.append({'key': k, 'why': why, 'what_would_close_it': close, 'blocking': k in ('sir.fed.efw2.layout_ty2026',)})

extra = {
 '_owner_decisions': [
  {'register_id': 'US-OWN-*/MANDATE US-MQ-09', 'decision': 'Statutory filings (federal and state) go through a third-party filing provider; no ADP integration (owner, biweekly 2026-10-21). Provider choice is a business decision outside the build (2026-10-29). SIR = provider-agnostic hand-off: Mercans produces provider input; the employer keeps liability.'}],
 '_scope_note': 'Unit third_party_provider_handoff: what each authority receives, on which channel, under which agent authorisation, and what a provider must be given. Mercans does not submit to authorities.',
}
write(BASE + '/_research/SIR-facts.json', 'SIR', 'third_party_provider_handoff', facts, blocked, unresolved, extra)
print('facts', len(facts), 'blocked', len(blocked), 'unresolved', len(unresolved))
print('consumed', ';'.join(sorted(consumed)))
