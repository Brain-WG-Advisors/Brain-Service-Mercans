# ===================================================================== PART 6
at("part6")
A("## PART 6 — Open items", "",
  "Each item gives the design reading and the research reading. Where they differ the research wins. A limitation is written "
  "*Not configured in this release* with its identifier.", "")
table(["#", "Item", "Design reading", "Research reading", "Disposition"], [
    ["1", "Utah withholding before the new table", "One table selected by 58421", f"The table in force from {fact('ut.pit.base_allowance.single.annual')['effective_from']} is carried; the earlier table is not", NC("DESIGN-RQ-01")],
    ["2", "Form W-4 before the 2020 revision (allowance method, nonresident alien Table 1)", "2020 revision only; pre-2020 employees handled manually", "Allowance method and Table 1 exist in the research; the Data Dictionary has no field for the revision or the allowance count; change request for Data Dictionary 1.1", NC("DESIGN-RQ-02")],
    ["3", "Supplemental withholding method", "Flag 58414 from the legal-entity field; default rule in Part 1", "Payer chooses flat rate or aggregate method; the Data Dictionary carries the field", "Closed: no limitation"],
    ["4", "State unemployment insurance assigned rate", "Legal-entity rate per State and year (58429)", "The State assigns the rate by notice; the Data Dictionary carries the field", G("DD-RQ-11") + " (how each State notifies the rate)"],
    ["5", "Employee abroad: statement that stops withholding", "Withheld normally", "The statement stops withholding; the Data Dictionary has no field; change request for Data Dictionary 1.1", NC("DESIGN-RQ-05")],
    ["6", "New-employer unemployment rate for some States", "Single rate per State", "Some States carry a rate by industry or by class and no single number", NC("DESIGN-RQ-06")],
    ["7", "FUTA credit reduction", "Potential rate recorded", "Final only after the year-end determination", f"{NC('RQ-402')}; {NC('RQ-403')}"],
    ["8", "2027 federal income tax schedules", "Schedules of the build year only", "Indexation for the next year is not published in the research", NC("RQ-530")],
    ["9", "Hawaii withholding for 2027", "Not modelled", "The State changes the brackets for 2027 and has not published the tables", NC("RQ-170")],
    ["10", "Virginia withholding for 2027", "Not modelled", "The statute changes the standard deduction for 2027; the formula is not published", NC("RQ-351")],
    ["11", "District of Columbia withholding method", "Method as recorded for the build year", "A change revoked personal exemptions and no method is published", NC("RQ-138")],
    ["12", "Programme rows without a parameter", "Row listed, no value written", "Wyoming workers' compensation, New York MCTMT and the Iowa school district have no value or row", NC("DESIGN-RQ-07")],
    ["13", "Programme parameters with no 2027 value", "2027 payment or earned dates use the last carried value only where the research says it continues", "Parameters listed in the limitation have no entry for 2027", NC("DESIGN-RQ-08")],
    ["14", "Date rule of programmes other than Massachusetts", "Selected by the date earned (58428)", "The research proves the earned-date rule for Massachusetts only", "Applied to all rows until a State annex says otherwise"],
], )
A("**Statute against published method.** Where a State's published withholding method differs from the statute, the research "
  "directs which one the configuration follows. Both readings:", "")
for k in sorted(k for k in C.FACTS if k.startswith("practice.")):
    try:
        A(f"- {tag(k)} {R(C.regid(k))}")
    except ValueError:
        pass
A("", "---", "")

