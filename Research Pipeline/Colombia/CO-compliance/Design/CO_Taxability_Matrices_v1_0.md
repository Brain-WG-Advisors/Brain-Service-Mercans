# Colombia — Taxability Matrices

Companion to `CO_Regulation_Design_v1_0.md`. Derived mechanically from all 403 populated rows of `CO-WTC-001-v1.1.xlsx`, sheet `Wage Type Catalogue`.

---

## Finding — Colombia needs FOUR matrices, not ten

The WTC carries ten perimeter columns. Tested pairwise across all 403 rows:

| Comparison | Divergences |
|---|---|
| Health vs Occupational risk (ARL) | **0** |
| Solidarity vs Pension | **0** |
| Health vs Pension | **1** |
| Health vs Payroll levies | **53** |
| Payroll levies vs Statutory-benefit base | **21** |
| Statutory-benefit base vs Vacation base | **52** |

**Health, solidarity, ARL and pension are one perimeter.** They diverge on exactly one row, and that row is a real rule rather than a typo: `Apprentice maintenance support`, where the lectiva phase carries health and ARL but no pension. It is routed on `9170013` rather than held in a matrix, because a matrix cannot express a phase.

**Building ten matrices would create nine accounts that can never diverge from one another**, inviting a future maintainer to edit one and not the rest. Same finding as Bahrain, reached the same way — tested, not assumed.

The four that are genuinely distinct:

| Matrix | Perimeter | Consumed by |
|---|---|---|
| **A** | IBC — contribution base | `9170012`, `9170021`, `9170022`, `9170023`, `9170041`, `9170042`, `9170043`, `9170046` |
| **B** | Payroll levies (CCF / SENA / ICBF) | `9170044` |
| **C** | Statutory-benefit base — prima, cesantías | `9170051` |
| **D** | Vacation base | `9170051` |
| *(tax)* | Withholding perimeter | `9170031` — see note below |

---

## Why B is distinct from A — and it is the one asymmetry that matters

**ET art. 114-1 exonerates employer health, SENA and ICBF for employees earning under 10 SMMLV — but never CCF.** So the payroll-levy perimeter cannot be folded into the IBC perimeter even though the two bases are computed identically. The worked example confirms it: employer health 0, SENA 0, ICBF 0, CCF 70,100.

That asymmetry is statutory, not a modelling choice, and it is the reason 53 rows diverge.

---

## Why C and D are distinct from each other — the transport allowance

The two benefit bases diverge on **52 rows**, and the clearest case is the transport allowance:

- **Out of the IBC** — CST art. 128 makes it non-salary, so no contribution is due on it

- **In the prima and cesantías base** — CST art. 306 brings it in expressly

- **Out of the vacation base** — vacation pay compensates time not worked, and the allowance reimburses travel to work that did not happen

This is why the CCG's worked example accrues prima and cesantías on 2,000,000 while contributing on 1,750,905 and accruing vacation on 1,750,905. **One wage type, three different answers, all correct.**

---

## Codes excluded from the contribution matrices (`NA` — 117 rows)

Deductions, employer-contribution lines, recoveries and information-only rows. They are not earnings and enter no base.

Note the WTC uses `NA` rather than `No` on these, which is the correct distinction: `No` means *an earning that does not enter this base*, `NA` means *not an earning*. Collapsing the two would make the matrices unreadable.

---

## The conditional rows — 34 rows, and why they are not a defect

**34 distinct wage types carry `Yes/No` on at least one perimeter.** A matrix is binary, so these cannot be resolved inside it — but they are not errors. Colombia has a specific mechanism that makes the same wage type genuinely in or out of the base:

**CST art. 128** lets the parties agree a payment is not salary. **Ley 1393 de 2010 art. 30** then caps non-salary payments at 40% of total remuneration and drags the excess back in.

So the answer depends on two facts that live outside the catalogue: whether a non-salary pact exists (`Non-Salary Pact Flag`, `58202`) and whether the 40% threshold is breached (computed in `9170012`).

**Design treatment:** the matrix routes these rows to the non-salary stream `58102`; the clamp regulation tests the result. The condition never sits in a matrix cell.

The WTC states each rule in its explanation column — for profit sharing: *CST art. 128 expressly excludes "la participación de utilidades" from salary, so it stays out of the benefit and vacation bases, but it is fully taxable and counts in the Ley 1393 art. 30 40% test*. That is the rule in the right place; only the routing was missing.

---

## Matrix A — IBC perimeter

**188 `Yes` · 49 `No` · 49 conditional · 117 `NA`**

**Section 1 — `No` overrides**, sorted first: severance and seniority payments, profit sharing where pacted non-salary, reimbursements, and the transport allowance (CST art. 128).

**Section 2 — broad `Yes`**: ordinary salary, overtime and premiums, commissions, and every habitual payment in money that remunerates the service directly (CST art. 127).

**Two rules this matrix cannot express**, which is why they live in `9170012`: the 40% non-salary clamp, and the floor and ceiling at 1 and 25 SMMLV. Both are arithmetic on summed rows.

---

## Matrix B — payroll-levy perimeter

**182 `Yes` · 101 `No`**

Identical in construction to Matrix A except where art. 114-1 applies. The exoneration is **not** modelled here — it is an assertion on `9170042` and `9170044`, because it depends on the employee's salary level rather than on the wage type.

---

## Matrices C and D — benefit bases

**C (prima, cesantías): 190 `Yes`** · **D (vacation): 140 `Yes`**

Both are wider than the IBC on the transport allowance and narrower on several non-salary items. Built as separate matrices because they diverge from each other on 52 rows.

---

## A note on the tax perimeter

The three tax columns (`Subject to Tax`, `Table Tax`, `Special Tax`) are not built as a contribution-style matrix. Withholding runs through the ET art. 388 depuration in `9170032`, which subtracts in a fixed order rather than summing a perimeter.

**The distinction that matters, and the WTC's own `Tax Credit` sheet flags it as the commonest source of error:** Colombia has **no tax credit at all**. Relief is delivered by subtracting from the base in three legally distinct classes — *ingresos no constitutivos*, *deducciones*, and *rentas exentas* — and misclassifying between them produces a plausible but wrong answer.

Related discipline carried into the design: **no tax threshold in Colombia is expressed in minimum wages.** Every tax parameter is in UVT (2026 = COP 52,374); every contribution parameter is in SMMLV (2026 = COP 1,750,905). The two units are never interchanged.
