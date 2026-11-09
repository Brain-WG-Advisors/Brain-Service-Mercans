p='overrides.py'; s=open(p,encoding='utf-8').read()
s=s.replace('GAP_CLOSE = {}','''GAP_CLOSE = {
    ("CT", "ct.wh.tables.per_period"): "the DRS withholding tables in IP 2026(1) transcribed as keyed per-period tables, together with the owner's choice of engine method (rules or tables)",
    ("CT", "ct.payslip.consolidated_text_lag"): "a consolidated text of 31-13a that includes PA 26-12 s.38; until then PA 26-12 governs",
    ("MULTI", "multi.sui.other_state_wage_credit.ar"): "the Arkansas UI handbook page that states the transfer-credit clause, registered as a source",
    ("MULTI", "multi.nonresident.sc.threshold"): "SC Code 12-8-520(A) reconciled with the SC DOR withholding guide (WH-1603F / WH105)",
    ("AR", "ar.wh.formula.switch_date"): "the DFA withholding release or notice of May 2026 announcing the start date of the reissued formula (the Act itself does not state it)",
    ("AR", "ar.live.bulletin_sweep"): "the arkleg Acts index for the 2025 Regular and 2026 Fiscal Sessions",
    ("AZ", "az.live.bulletin_sweep"): "the ADOR news archive and DES employer bulletins for 2026",
    ("AZ", "az.report.w2.pub701_edition"): "the ADOR Pub 701 2026 edition",
    ("AR", "ar.garn.iwo.employer_fee"): "the OCSE employer guide or Ark. Code 9-14-218 / 9-14-226",
    ("CO", "co.famli.split.next_year"): "7 CCR 2702-3 and C.R.S. 8-13.3-507 on famli.colorado.gov or in the Colorado Register",
    ("CO", "co.leave.sick.amendments_and_payslip_econsent"): "the current Healthy Families and Workplaces Act text and CDLE INFO #6 / #13",
    ("FED", "fed.fica.oasdi.wage_base.next_year_reverification"): "the SSA 2027 COLA fact sheet or contribution-and-benefit-base page, or the 2027 Federal Register notice",
    ("FED", "fed.leave.eo13706.accrual"): "29 CFR 13.5 on eCFR",
    ("MULTI", "multi.newhire.multistate_registration_channel"): "the ACF multistate employer registration page",
    ("MULTI", "multi.sui.other_state_wage_credit.la"): "R.S. 23:1536",
    ("AK", "ak.garn.iwo.employer_fee"): "AS 25.27.062 on the Alaska Legislature site, or the CSED ACSESS Business Portal employer guide",
    ("AK", "ak.live.bulletin_sweep"): "the Alaska Administrative Register issues for 2026 and the BASIS passed-legislation list of the 34th Legislature",
    ("CT", "ct.live.public_act_texts"): "the Public Act PDFs on cga.ct.gov",
    ("CT", "ct.garn.employer_fee"): "a full read of 52-362 and 52-361a(j)-(k)",
    ("CO", "co.local_minwage.other_cities"): "the coloradolaborlaw.gov local minimum wage list or each city or county notice (Edgewater, Boulder, Boulder County) and the Denver 2027 rate notice",
    ("CA", "ca.local_minwage.hourly"): "each city labour-standards office bulletin for the 2026-07-01 and 2027-01-01 rates",
    ("AL", "al.local.occupational_tax.census"): "the Alabama League of Municipalities occupational-tax list, then each city ordinance or tax page (Birmingham, Auburn, Bessemer, Gadsden, Opelika, Fairfield, Macon County)",
    ("AL", "al.garn.iwo.employer_fee"): "Ala. Code 30-3-60 to 30-3-71 in full, or the DHR Child Support employer page",
    ("AL", "al.live.overtime_withholding_exemption.end_date"): "the ADOR page on the overtime pay exemption as amended by Act 2024-437",
}''')
open(p,'w',encoding='utf-8').write(s)
c='content.py'; t=open(c,encoding='utf-8').read()
t=t.replace('''        f"| Weekly withholding | {_fmt(annual)} / 52 | — | {_fmt(per)} |",
        f"Result {_fmt(per)} equals the published value {value_cell(out)}. If the employer rounds the period tax to the "
        "whole dollar, the weekly amount is the rounded figure.",''','''        f"| Weekly withholding | {_fmt(annual)} / 52 | — | {value_cell(out)} |",
        "The computed weekly withholding equals the published value. If the employer rounds the period tax to the "
        "whole dollar, the weekly amount is the rounded figure.",''')
t=t.replace('''        f"| Bracket 4 tax | {_fmt(mid)} x {tag(b4)} % - {value_cell(s4)} | {_fmt(gross_tax)} - {_fmt(_d(s4['value']))} = {_fmt(tax)} |\n"''','''        f"| Bracket 4 tax | {_fmt(mid)} x {tag(b4)} % - {value_cell(s4)} | {_fmt(gross_tax)} - {tag(s4)} = {_fmt(tax)} |\n"''')
t=t.replace('''        f"| Monthly withholding | {_fmt(net_tax)} / 12 | {_fmt(per)} |",
        f"Result {_fmt(per)} equals the published value {value_cell(out)}.",''','''        f"| Monthly withholding | {_fmt(net_tax)} / 12 | {value_cell(out)} |",
        "The computed monthly withholding equals the published value.",''')
t=t.replace('''        f"| Monthly withholding | {_fmt(net)} / 12 | {_fmt(per)} |",
        f"Result {_fmt(per)} equals the published value {value_cell(f_out)}. Example E (semi-monthly) published value: "''','''        f"| Monthly withholding | {_fmt(net)} / 12 | {value_cell(f_out)} |",
        "The computed monthly withholding equals the published value. Example E (semi-monthly) published value: "''')
open(c,'w',encoding='utf-8').write(t)
print(t.count('value_cell(out)} |'), t.count('value_cell(f_out)} |'), 'tag(s4)} =' in t)
