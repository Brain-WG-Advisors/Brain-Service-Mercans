# Round 2 (finding 6): fuller Field Explanations (column M) in us_state.py. Applied once by the builder.
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
R = [
# DOR-C-005
('''          f"State income tax withheld in the period for the State; computation per {CCG_REF} Module 6 and the State annex.",''',
 '''          f"State income tax withheld in the period for the State, computed per pay period as stated in {CCG_REF} Module 6 and "
          f"the State annex. It is the sum of the State tax withheld on the period payroll results of the employees whose wages "
          f"are sourced to this State (row DOR-C-004, {tag('rspec.multi.ui_qtr.recipient')} for the routing) and must equal the "
          f"tax on the employees' pay records for the same State and period. Reported in cents unless the State rule in the State "
          f"section says whole dollars (column P); it is never negative: a withholding error found after filing goes through the "
          f"State's amended-return route, not through the next period's return.",'''),
# DOR-C-007
('''          "Many States require a return for every period even with nothing withheld; examples: "
          f"{tag('rspec.co.wh_return.zero')} [{rid('rspec.co.wh_return.zero')}]; {tag('rspec.al.wh_return.quarterly')}.",''',
 '''          "Indicator that a return is filed for a period with no State wages paid or no State tax withheld. Many States require "
          "a return for every period even with nothing withheld; examples: "
          f"{tag('rspec.co.wh_return.zero')} [{rid('rspec.co.wh_return.zero')}]; {tag('rspec.al.wh_return.quarterly')} "
          f"[{rid('rspec.al.wh_return.quarterly')}]. The flag is set from the jurisdiction configuration (State section rows "
          "classified Zero-return rule or Return form); when it is Y the return generator files the period with every amount at "
          "zero, and where the State section states no zero-return rule it stays N. One character, Y or N.",'''),
# MBT-C-002
('''          "Payroll result: employer health benefit cost", f"Deducted from the base: {tag('nv.mbt.base')}.", "Yes", "Not applicable",''',
 '''          "Payroll result: employer health benefit cost",
          f"Employer-paid health benefits for the quarter, deducted from the Modified Business Tax base: {tagr('nv.mbt.base')}. "
          f"The amount is the employer's cost for the quarter, taken from the payroll result for employer health benefit cost "
          f"(employee contributions are not part of it), and is reported in cents next to the wages of row MBT-C-001. It is "
          f"reported only for a quarter in which the employer paid such benefits; otherwise the field is zero and the base is the "
          f"UI gross wages alone.", "Yes", "Not applicable",'''),
# MBT-C-003
('''          f"(Base minus {tag('nv.mbt.general.quarterly_threshold')} a quarter) x {tag('nv.mbt.general.rate')}% (general business); "
          f"financial institutions and mining {tag('nv.mbt.financial_mining.rate')}%.", "Yes", "Not applicable", "Cents", "N",''',
 '''          f"Taxable wages and the tax due for the quarter, computed by the return generator and never keyed: (base of rows "
          f"MBT-C-001 minus MBT-C-002, minus {tag('nv.mbt.general.quarterly_threshold')} a quarter) x {tag('nv.mbt.general.rate')}% "
          f"for general business [{rid('nv.mbt.general.rate')}]; the quarterly exclusion is [{rid('nv.mbt.general.quarterly_threshold')}]. "
          f"Financial institutions and mining use {tag('nv.mbt.financial_mining.rate')}% and are out of this return's general "
          f"business form. When the base does not exceed the exclusion the tax is zero, but the return is still filed: "
          f"{tag('rspec.nv.mbt.form')}. Rounded to the cent, half-up (see Example Analysis).", "Yes", "Not applicable", "Cents", "N",'''),
# TRN-C-002
('''          f"TriMet {tag('or.transit.trimet.employer.rate')}%, Lane Transit {tag('or.transit.lane.employer.rate')}% [US-ORS5-010]; "
          f"New York MCTMT: zone payroll x the rate of its payroll band (rate table in the NY section).", "Yes", "Not applicable",''',
 '''          f"Employer transit tax due for the quarter, computed by the return generator from the wages of row TRN-C-001 and never "
          f"keyed. Oregon: wages for work in the district x TriMet {tag('or.transit.trimet.employer.rate')}% or Lane Transit "
          f"{tag('or.transit.lane.employer.rate')}% [{rid('or.transit.trimet.employer.rate')}], reported on {tag('rspec.or.oq.form')}. "
          f"New York MCTMT: zone payroll x the rate of its payroll band (rate table in the NY section). The tax is employer-borne "
          f"and never withheld from employees; it is rounded to the cent, half-up (see Example Analysis).", "Yes", "Not applicable",'''),
# LOC-C-002
('''          "Wages subject to the local tax in the period, per locality (CCG Module 6 and the State annex).", "Yes", "Not applicable",''',
 '''          f"Wages subject to the local income or wage tax in the period, per locality of row LOC-C-001, as defined in {CCG_REF} "
          f"Module 6 and the State annex (the local base can differ from the State base, e.g. by work or residence locality). "
          f"Taken from the local wage accumulator of the payroll results, one amount per locality and employee, in cents. An "
          f"employee working in several localities has one amount per locality; a locality without wages in the period is not "
          f"reported.", "Yes", "Not applicable",'''),
# CITY-C-001
('''          "Compensation paid for work in the city in the period (base per city in the CCG annex).", "Yes", "Not applicable", "Cents",''',
 '''          f"Compensation paid for work in the city in the period, the base of the city's employer payroll tax, as defined per city "
          f"in {CCG_REF} (State annexes of NJ, MO and PA). Taken from the city payroll expense accumulator of the payroll results, in "
          f"cents; it includes only the compensation the city rule assigns to work in the city, so an employee working partly "
          f"outside the city contributes only that part. The tax itself is computed in row CITY-C-002.", "Yes", "Not applicable", "Cents",'''),
# CITY-C-003
('''          "See Example Analysis", "Payroll result: St. Louis earnings tax accumulator", f"{tagr('rspec.mo.local.st_louis')}.",''',
 '''          "See Example Analysis", "Payroll result: St. Louis earnings tax accumulator",
          f"Earnings tax withheld from employees for St. Louis in the period: {tagr('rspec.mo.local.st_louis')}. The amount is the "
          f"sum of the earnings tax withheld on the period payroll results at {tag('mo.pit.local.st_louis.earnings_tax.rate')}% "
          f"[{rid('mo.pit.local.st_louis.earnings_tax.rate')}], reported in cents on the same return as the employer payroll expense "
          f"tax of row CITY-C-002. Only St. Louis carries this field; for the other cities it is not reported.",
