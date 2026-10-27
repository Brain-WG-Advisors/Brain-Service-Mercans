"""Skill payroll-compliance-egypt: Fundo dos Mártires (0,05%) vale para o setor privado.

Fonte: Lei 4/2021 art. 1 (novo art. 8 da Lei 16/2018), Gazette nº 8 bis (هـ) de 03/03/2021, pp. 5-6
(raw/docs/oficiais/EG/2026-10-22-lei-4-2021-fundo-martires-gazette.pdf); Circular Geral MoF 14/2021 de 10/05/2021,
itens 1-3 e "ثانيا" 2 (cópia em aliateck.com); ETA Payroll FAQ v4, Q110. Só os trechos do Fundo dos Mártires mudam.
Uso: python -I aplicar_correcao.py <pasta payroll-compliance-egypt>
"""
import sys, pathlib

ROOT = pathlib.Path(sys.argv[1])
LAW = ("Law 16/2018 art. 8(1) as replaced by Law 4/2021 art. 1 (Official Gazette No. 8 bis (هـ), 3 March 2021, "
       "in force 4 March 2021)")

EDITS = {
'SKILL.md': [
 ("Where a reference describes a public-sector rule (Civil-Service-Law fields, proportional salary stamp duty, the martyrs'-fund deduction) it is there to explain **why it does not apply** to a private employer.",
  "Where a reference describes a public-sector rule (Civil-Service-Law fields, proportional salary stamp duty) it is there to explain **why it does not apply** to a private employer. The **martyrs'-fund contribution (0.05%) does apply** to private-sector employees (`references/01-ccg.md` §8.2)."),
 ("- **Eight sections are below the 95% confidence floor and are marked as such**: the social-insurance/health-insurance rate boundary for a UHI-covered employee; the UHI governorate rollout list; the Training and Rehabilitation Fund's collection mechanics; the martyrs'-fund private-sector exclusion; the public-holiday list;",
  "- **Seven sections are below the 95% confidence floor and are marked as such**: the social-insurance/health-insurance rate boundary for a UHI-covered employee; the UHI governorate rollout list; the Training and Rehabilitation Fund's collection mechanics; the public-holiday list;"),
],
'references/01-ccg.md': [
 ("and — for private-sector employers — **no payroll stamp duty and no martyrs'-fund deduction** (both are confined to government and public-business-sector disbursements; see §8).",
  "and — for private-sector employers — **no payroll stamp duty** (confined to government and public-business-sector disbursements; see §8.3). The **martyrs'-fund contribution (0.05%) does apply** to private-sector employees (§8.2)."),
 ("## 8.2 Martyrs' Fund contribution — NOT a private-sector payroll item\n",
  "## 8.2 Martyrs' Fund contribution — applies to private-sector employees\n"),
 ("""**Its scope is public.** The salary deduction applies to employees of **government agencies, public-sector entities and their companies, and public-business-sector companies and their affiliates**. Private-sector employers are **not** within it.

The ETA payroll system nonetheless computes it, because the system serves all sectors: ETA FAQ Q110""",
  f"""**Its scope includes the private sector.** {LAW}: *"تخصم شهريًا نسبة تعادل خمسة من عشرة آلاف من راتب العاملين بالجهات العامة ، وهيئات القطاع العام وشركاته ، وشركات قطاع الأعمال العام ، وما يتبع هذه الجهات والهيئات والشركات من وحدات ذات طابع خاص والصناديق الخاصة ، والعاملين لدى الأشخاص الاعتبارية الخاصة الذين تسرى بشأنهم أحكام القانون الخاص بالعمل ، وذلك فيما عدا العمالة غير المنتظمة أو باليومية"* — 5 per 10,000 of the salary is deducted monthly from employees of public entities **and from employees of private legal persons governed by the Labour Law**, **except irregular or daily labour**. It is an **employee** deduction: the paying entity pays the salary net of it, and the Ministry of Finance collects it for the Fund.

**Base and remittance.** MoF General Circular 14/2021 (10 May 2021), item 3, restates the article and defines the salary for this purpose as *"إجمالي الراتب الشهري"* — the **total monthly salary**. For entities other than public bodies (part 2, "ثانيا"), ETA issues the collection instructions and remits the amounts monthly, by the 10th of the month following collection. (Copy obtained from a secondary host, aliateck.com; no copy found on the MoF or ETA site.)

The ETA payroll system computes it: ETA FAQ Q110""",
 ),
 ("""> **CONFIDENCE FLAG.** The **rate and mechanics** are from ETA's own March 2026 FAQ and are solid. The **restriction to public-sector payrolls** rests on reporting of the amending law's text rather than on the gazette article itself, which I could not retrieve. If you operate a mixed group with public-business-sector entities, verify per entity. See `07-qa-report.md` §3.""",
  """> **Scope: verbatim gazette text (resolved 22 Oct 2026).** The earlier statement that the fund was *not* a private-sector item was wrong; the gazette article is quoted above. Two readings to keep in view: the law excludes **all** irregular and daily labour, while FAQ Q110 excludes **Egyptian** daily labour; and the circular's base is the **total monthly salary**, while FAQ Q110 computes on **basic disbursements** (the disbursement type, as opposed to additional disbursements). Follow the ETA system's computation and disclose. See `07-qa-report.md` §3.4."""),
],
'references/07-qa-report.md': [
 ("**READY FOR REVIEW — with eight sections honestly below the 95% floor",
  "**READY FOR REVIEW — with seven sections honestly below the 95% floor"),
 ("Eight items are stated below floor.", "Seven items are stated below floor."),
 ("| **01** | Martyrs' Fund — **private sector not subject** | **80%** ⚠ | See §3.4 |",
  "| **01** | Martyrs' Fund — **private sector subject** (except irregular/daily labour) | **98%** | Law 4/2021 art. 1 gazette text verbatim (new art. 8 of Law 16/2018); MoF General Circular 14/2021 item 3. Resolved 22 Oct 2026 — see §3.4 |"),
 ("""## 3.4 Martyrs' Fund — the private-sector exclusion — **80%**

The **rate and mechanics** (EGP 5 per EGP 10,000 of basic disbursements, all labour except Egyptian daily labour, its own Core claim) are from ETA's March 2026 FAQ and are solid at ~90%.

**The scope restriction to public agencies, the public sector and the public business sector rests on reporting of the 2021 amending law's text**, not on the gazette article itself. I retrieved Law 16/2018's existence and purpose but not the article listing the Fund's resources.

**Why it matters.** If the restriction is wrong, every private employer in Egypt owes 0.05% of basic pay that this pack says they do not. **In a mixed group containing public-business-sector entities, verify per entity.**

**What would close it.** The gazette text of the 2021 amendment to Law 16/2018, or **ETA circular 119/2021** on the Fund.""",
  f"""## 3.4 Martyrs' Fund — private-sector scope — **CLOSED (22 Oct 2026)**

The **rate and mechanics** (EGP 5 per EGP 10,000 of basic disbursements, all labour except Egyptian daily labour, its own Core claim) are from ETA's March 2026 FAQ and are solid at ~90%.

**The earlier finding was wrong.** This pack said the fund was confined to public agencies, the public sector and the public business sector. The gazette text says otherwise: {LAW} deducts 0.05% monthly from the salary of employees of public entities **and of private legal persons governed by the Labour Law**, except irregular or daily labour. MoF General Circular 14/2021 (10 May 2021), item 3, restates it and defines the salary as the **total monthly salary** (*"إجمالي الراتب الشهري"*); ETA collects from entities other than public bodies.

**Residual points (not below floor).** The law excludes **all** irregular/daily labour; FAQ Q110 excludes **Egyptian** daily labour. The circular's base is total monthly salary; FAQ Q110 computes on basic disbursements. Follow the ETA system and disclose. See `01-ccg.md` §8.2."""),
 ("| 5 | Obtain ETA circular **119/2021** or the 2021 amendment to Law 16/2018 | §3.4 martyrs'-fund scope | Medium |",
  "| 5 | ~~Obtain ETA circular **119/2021** or the 2021 amendment to Law 16/2018~~ — **done 22 Oct 2026** (Law 4/2021 gazette; MoF General Circular 14/2021) | §3.4 martyrs'-fund scope | — |"),
],
'references/04-reports-spec.md': [
 ("| Per disbursement | With the salary-tax claim | Basic disbursements at a **subject** entity | 75% |",
  "| Per disbursement | With the salary-tax claim | Basic disbursements to all employees, **private sector included**, except irregular/daily labour | 90% |"),
 ("| **Scope** | **Government agencies, public-sector entities and their companies, and public-business-sector companies and their affiliates.** **Not private-sector employers** |\n| Legal basis | Law 16/2018 establishing the Fund, as amended in 2021 to widen its resources; ETA circular **119/2021** addresses the Fund |",
  f"| **Scope** | Employees of public entities **and of private legal persons governed by the Labour Law**, **except irregular or daily labour** — **private-sector employers are within it** |\n| Legal basis | {LAW}; MoF General Circular 14/2021 item 3 (salary = total monthly salary); MoF circular letter 119/2021 opens the Fund's collection accounts |"),
 ("> **Confidence 75%.** Rate and mechanics from ETA's March 2026 FAQ (solid). The **public-sector restriction** rests on reporting of the amending law rather than the gazette article, which I could not retrieve. Verify per entity in a mixed group. See `07-qa-report.md` §3.",
  "> **Confidence 90%.** Scope from the gazette text (verbatim, `01-ccg.md` §8.2); rate and mechanics from ETA's March 2026 FAQ. The earlier public-sector-only statement was wrong (corrected 22 Oct 2026). See `07-qa-report.md` §3.4."),
],
'references/05-data-dictionary.md': [
 ("| `martyrs_fund_subject` | Y / N | Public / public-business-sector only |",
  "| `martyrs_fund_subject` | Y / N | **Y** for every employee, private sector included; **N** only for irregular/daily labour (Law 16/2018 art. 8 as amended by Law 4/2021) |"),
 ("| Legal form / sector | Determines stamp-duty and martyrs'-fund scope, and Civil-Service-Law field applicability |",
  "| Legal form / sector | Determines stamp-duty scope and Civil-Service-Law field applicability (not martyrs'-fund scope, which covers the private sector) |"),
],
}

for rel, pairs in EDITS.items():
    p = ROOT / rel
    t = p.read_text(encoding='utf-8')
    for old, new in pairs:
        n = t.count(old)
        assert n == 1, (rel, n, old[:70])
        t = t.replace(old, new)
    p.write_text(t, encoding='utf-8', newline='')
    print('ok', rel, len(pairs))
