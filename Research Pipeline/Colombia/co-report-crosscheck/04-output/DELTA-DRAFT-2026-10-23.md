# Delta para o time do Mohit (design) - RASCUNHO 23/10, não enviado

Notas internas (não vão no texto):
- Data no plano: 28 Oct (PENDING #59). Vale depois da subida final ao Drive (os nomes e versões abaixo são os da subida).
- Quem envia: o Wallisson (decidido em 26/10). Fica em rascunho até ele enviar.
- Texto neutro: só as regras como estão, sem histórico de correção.
- 26/10: item 6 (trava dos 40%) acrescentado a pedido do usuário; "Legal references" passou a 7. Rascunho do Gmail a atualizar pela janela Gmail.

---

**Subject:** Colombia (PMI) – compliance artifacts for design

Hi all,

The Colombia (PMI) compliance artifacts are final on the Compliance Team Drive (links on Monday). Below are the rules that matter most for design, and the points that stay open.

**Artifacts**
- Statutory report specs (v1.0): CO-DIAN-001 Nómina Electrónica, CO-DIAN-002 Formulario 350, CO-DIAN-004 Formulario 220, CO-DIAN-005 Formato 2276, CO-PILA-003 PILA (employees), CO-PILA-007 PILA (pensioners paid by the employer – new), CO-CESANTIAS-006 Consignación de cesantías.
- CCG v1.4, WTC v1.6, DD v1.3, SIR v1.1.

**Rules for design**
1. Pensioners paid by the employer:
   - They are in the electronic payroll (Res. DIAN 000227 de 2025).
   - Their PILA is the new CO-PILA-007 (Res. MSPS 2388 de 2016, Anexo Técnico 3 v15). Health is on the mesada at 4% / 10% / 12% by pension band. FSP is 1% above 10 SMMLV and 2% above 20 SMMLV. Pension contributions apply only to the pension types that require them. CCF is optional.
2. Withholding: the monthly totals reconcile to Formulario 350 casillas 93 + 94. Voluntary pension is reported only where it is deducted from the employee.
3. PILA for employees (CO-PILA-003):
   - Vacation paid in cash is outside the health, pension, occupational-risk and FSP base. It is inside the CCF / SENA / ICBF base.
   - Enjoyed vacation: health and pension are on the prior month's IBC, and no occupational-risk contribution is due.
   - Return types: N for corrections (C ≥ A), E for late payment, M only for periods before health period March 2014.
   - Apprentices in the lectiva phase are code 19 from health period August 2025.
4. Termination date: taken from the system Termination record (DD).
5. Cesantías: only the annual deposit to the fund, by 14 February. The monthly advance deposit of Ley 2466 de 2025 art. 64 par. 1 is not in force (its decree is still a draft), so it is not in the spec. Monthly payment of the 1% interest requires a written agreement (par. 2).
6. 40% cap on non-salary payments (Ley 1393 de 2010 art. 30):
   - Only pacted non-salary payments count towards the cap. Payments that are non-salary by nature are outside both the numerator and the total (Consejo de Estado, SU 25185 de 2021, rule 3).
   - Total remuneration = all salary payments + pacted non-salary payments + paid leave. Indemnities, unpaid leave, incapacities and social benefits are excluded (UGPP, ABC Empleadores 2025).
   - The excess over 40% is added to the pension, health and occupational-risk bases only, not to the CCF / SENA / ICBF base (Ley 21 de 1990 art. 17).
   - The extralegal vacation premium agreed in writing as non-salary is a pacted non-salary payment (CST art. 128).
7. Legal references: Res. DIAN 000227 de 2025 replaces Res. 000013 de 2021 in every artifact.

**Open points (no primary source, or a client fact still needed)**
- Electronic payroll code for a pensioner who does not work: the DIAN annex has no TipoTrabajador / SubTipoTrabajador code for this case. The current provider uses 01 / 01, contract type 2, Sueldo 0.00, and reports the pension as OtroConcepto. A formal query to DIAN is Manju's decision.
- Health and FSP on the June / December extra mesadas: not settled in law, and PILA has no field for them. This is a client-confirmed parameter with no default.
- CO-PILA-007 client facts: pension type of each of the 454 pensioners, pensioner type 5 vs 6, pensioners resident abroad, additional UPC, which WT carries each health band, WT 62830.
- Fractional vacation days in the electronic payroll: the quantity is a whole number (XSD), and DIAN has no rounding rule.

**Seen in the September provider files (no spec change)**
- Vacation paid on termination is sent as OtroConcepto 'Vacaciones Definitivas'.
- WT 62151 (voluntary retirement plan) is sent as OtroConcepto.
- 37 employees have Sueldo 0.00; the spec requires the contract salary.

Thanks,
Wallisson
