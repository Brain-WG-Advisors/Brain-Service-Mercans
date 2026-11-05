# Rascunho — Colômbia: lista consolidada de mudanças (v1.4 → v1.7) para o Mohit e o Ram

> Hub: [[Colombia]] · Conferência: [[Research Pipeline/Colombia/2026-10-29-validacao-research/CONFERENCIA|CONFERENCIA]] · Frente: Validação CO. **RASCUNHO — não enviado.** Pedido da janela geral (call de 04/11, `raw/reunioes/2026-11-04-collaboration-dev-design.txt` 39:36–41:18: "a consolidated list so you know what was changed").
>
> Base (versão que o Dev recebeu, 22/10–26/10): CCG v1.4 (22/10), WTC v1.6 (22/10), DD v1.3 (22/10), 7 Report Specs v1.0 (26/10), SIR v1.1 (21/10), Payslip Generator v1.1.
> Vigente: CCG v1.7, WTC v1.9, DD v1.6, CO-DIAN-004 v1.3, CO-DIAN-001/005/CESANTIAS-006/PILA-003 v1.2, CO-DIAN-002/PILA-007 v1.1, SIR v1.4, Payslip v1.3 (md5 em `final/MD5-FINAIS.txt`, iguais ao `achar_versao` de 04/11).
>
> Ponto que corrige a leitura da call: **a base mensal não virou YTD.** A retenção continua mês a mês (Procedimento 1: "Each month stands alone", CCG v1.7 Módulo 6) e a seguridade social continua mensal, sem ajuste anual (CCG v1.7 Módulo 5: "Colombian contributions are definitively settled month by month"). O que passou a acumulado no ano foram só os **tetos** de 790 / 1.340 / 3.800 UVT (antes 1/12 por mês).

---

## Texto para enviar (inglês)

**Colombia — consolidated changes from the versions of 22–26 October to the current versions**

What changes the calculation, in short:
1. Withholding tax is still monthly (Procedure 1, each month stands alone). Only the annual caps of 790 UVT (25% exempt income), 1,340 UVT (combined cap) and 3,800 UVT (voluntary pension / AFC) are now tracked year-to-date per employee instead of a monthly 1/12 figure. The monthly taxable base itself did not change.
2. Social security is still monthly. What changed is the contribution base in three cases: all-inclusive salary, the 40% test (pacted non-salary payments only) and the payroll-levy base.
3. A few withholding cases moved: the dismissal indemnity is withheld separately, non-residents are withheld at a flat 20%, severance savings are never withheld, and the 72-UVT dependant deduction stays out of monthly withholding.
4. Everything else is wording, legal references, worked examples and report mappings. CCG v1.7, WTC v1.9, DD v1.6 and Form 220 spec v1.3 are text only.

### CCG (v1.4 → v1.7)

| Section | Before (v1.4) | Now (v1.7) | Legal basis | Design impact |
|---|---|---|---|---|
| Mod. 6.1.1, 6.2, 7.1, examples in Mod. 9 and 12 | 790-UVT and 1,340-UVT caps applied as a monthly 1/12 figure (COP 3,447,955 / 5,848,430) | Annual caps (COP 41,375,460 / 70,181,160) tracked year-to-date per employee; no monthly limit. The monthly base and the art. 383 table read are unchanged | Consejo de Estado S4 rad. 24047 (28/10/2021) annulled the monthly equivalent in DUR 1625 art. 1.2.4.1.6 par. 3; Decreto 2231 de 2023 art. 9; ET 206 num. 10, 336 num. 3 | Calculation: YTD accumulator of exempt income / deductions used |
| Mod. 7.1 (voluntary pension, AFC/AVC) | 3,800 UVT ÷ 12 per month | 3,800 UVT per year, tracked year-to-date | DUR 1625 art. 1.2.1.22.43 ("por año"); ET 126-1, 126-4 | Calculation: same YTD accumulator |
| Mod. 7.1 (dependants) | 72 UVT per dependant deducted in monthly withholding | Not deducted in withholding (annual return only); the 40% / 1,340-UVT cap still applies in withholding | DIAN Concepto 011383 de 2024 §IV.2; DUR 1625 art. 1.2.4.1.6 par. 3 | Calculation: remove the 72-UVT step |
| Mod. 9.1 (dismissal indemnity) | Inside the ordinary monthly base | Withheld separately: 20% where income exceeds 204 UVT, otherwise the table % of the 12-month average | ET 401-3; DUR 1625 arts. 1.2.4.1.8, 1.2.4.1.13 | Calculation: separate withholding line |
| Mod. 9.1 (indemnity base) | Not specified | CST art. 127 salary with its variable parts (average of the last year for variable pay) | CST 127, 253; CSJ SL1659-2025 | Calculation (base of the indemnity) |
| Mod. 2.2, 6.3, 11.2 (non-residents) | Same art. 383 progressive table as residents | Flat 20% (ET 408–415) until tax residence; residence from the 184th day in any 365-day period, the second year when it spans two years | DIAN Concepto 011108 de 2026 items 10 and 13; ET art. 10 num. 1 | Calculation: residence flag drives the rate |
| Mod. 6.1.1, 9.1 (severance savings) | 20% for non-residents | Never withheld, resident or non-resident; 20% only as an optional conservative setting, off by default | Ley 100 art. 135 par. 3; Corte Constitucional C-397 de 1994; DUR 1625 art. 1.2.4.1.11; DIAN Concepto 577 de 2020 | Calculation |
| Mod. 5.1, 5.2 (ET 114-1 exoneration) | Employees earning below 10 minimum wages | Both limbs below 10 minimum wages: salary payments of the month and health contribution base (PILA field 76); employer must be a legal person filer or a natural person with 2+ employees | ET 114-1; DIAN Conceptos 8380 de 2024 and 7196 de 2025 | Calculation + PILA mapping (field 76) |
| Mod. 5.1.1 (all-inclusive salary) | 40% test, then 70% | 70% of the salary, then the Ley 1393 excess added (not reduced to 70%) | Ley 100 art. 18; CE SU 25185 de 2021; exp. 25907 de 2022 | Calculation (IBC) |
| Mod. 4.6, 5.1.1 (40% test) | All non-salary payments | Only non-salary payments by pact; non-salary by nature stays out of the base and the test | CE SU 25185 de 2021; UGPP ABC Empleadores 2025 | Calculation (IBC) |
| Mod. 5.1.1 (payroll levies) | Ley 1393 excess also in SENA / ICBF / CCF base | Excess only in health, pension and ARL; levy base never takes it | Ley 1393 art. 30; Ley 21 de 1982 art. 17 | Calculation |
| Mod. 5.1 (ARL class IV) | Maximum 6.060% | Maximum 6.960% | Decreto 1772 de 1994 art. 13 | Calculation (rate table) |
| Mod. 5.1 (solidarity fund bands) | 16 to 17, 17 to 18… minimum wages | Band edges stated ("above 17 up to 18"); note on the 2.8% band up to 20 SMMLV from 1/4/2027 | Ley 2381 de 2024 art. 20; Corte Constitucional C-264 de 2026 | Calculation (band edges) |
| Mod. 4.1, 4.3 (transport allowance) | Full month in a month with absences | Pro rata to days worked | Ley 15 de 1959 art. 2 par.; Decreto 1258 de 1959 art. 5 | Calculation |
| Mod. 4.3 (hire mid-month example) | Hire on 12 August = 20 days | 19 days (30-day month convention) | CCG 30-day convention | Example only |
| Mod. 8.1 (vacation paid in cash during employment) | Salary ÷ 720 | Salary ÷ 30 × days (÷ 720 only on termination) | CST arts. 186, 189 | Calculation |
| Mod. 7.3 (garnishments) | Maintenance first (Constitution art. 44) | Child maintenance first, ceiling 50% | Ley 1098 de 2006 arts. 130, 134; CST 155, 156 | Calculation (priority) |
| Mod. 5.2 (unpaid leave, public employer) | Public employer "may" pay 75% | Public employer must keep paying its 12% share; private employer may report its rate or 16% | Decreto 1083 de 2015 art. 2.2.5.5.7; PILA AT2 v30 | Calculation (public employers only) |
| Mod. 5.3, 6.1.1 (employer voluntary contribution to mandatory fund) | Not taxable | Not taxable up to 25% / 2,500 UVT; excess taxable | ET 55; DUR 1625 art. 1.2.1.12.9 | Calculation |
| Mod. 10 (Form 350 corrections) | 2 years | 3 years | ET art. 588 (Ley 2010 art. 107) | Text only |
| Mod. 2.3 (record retention) | 3–5 years | Minimum 5 years from 1 January of the following year | ET arts. 632, 714 | Text only |
| Mod. 1, 4.4 and others | Ministry of Labour Circular 101 de 2025 cited | Statute cited (Circular revoked by Res. MinTrabajo 2708 de 2026); no value changes | CST 161, 179; Ley 2101 de 2021 art. 3 | Text only |
| Mod. 4.1, 5.2, 6.1.1, 8.1 (v1.7) | — | Legal basis wording: C-397 / Concepto 577 (severance), Decreto 0159 de 2026 note (minimum wage), C-543 de 2007 (incapacity floor) | as cited | Text only |

### WTC (v1.6 → v1.9)

| Rows / sheet | Before (v1.6) | Now (v1.9) | Legal basis | Design impact |
|---|---|---|---|---|
| Tax Credit; Global WTC Coverage | 790 / 1,340 / 3,800-UVT caps monthly 1/12 | Annual, tracked year-to-date | as CCG row 1 | Calculation |
| Tax Credit | 72-UVT dependant deduction in withholding | Left to the annual return | DIAN Concepto 011383 de 2024 | Calculation |
| 120–122, 321–322 | Severance savings and interest: 20% for non-residents | Not withheld for anyone | as CCG | Calculation |
| Long-term disability, incapacity, maternity / paternity / parental leave (incl. 123, 326–333) | Levy / ARL / benefit-base flags as in v1.6 | Payroll levies No; ARL No; out of the statutory-benefit base | Ley 21 de 1982 art. 17; AT2 v30 field 26; Decreto 1072 art. 2.2.4.2.1.6; SSF Concepto 2-2018-083606 | Calculation (flags) |
| 156, 324 (vacation paid in cash) | In the prima / cesantías base | Out of that base | CST 189, 253, 306; CSJ SL467-2019 | Calculation (flags) |
| Cooperative compensation, representation expenses (353, 356) | Not taxable | Taxable; occasional per diem exempt only under DUR 1625 art. 1.2.4.7 | ET 103 par. 2; DUR 1625 art. 1.2.4.7 | Calculation (tax flag) |
| 350 (employer voluntary contribution) | Not taxable | Not taxable up to 25% / 2,500 UVT | ET 55; DUR 1625 art. 1.2.1.12.9 | Calculation |
| 311–312 (night premium on rest days) | — | Night premium on rest days outside the vacation base (v1.7 note) | see the row note | Calculation (flag) |
| 322 (interest on severance savings) | — | Tax treatment of the interest restated; no withholding for anyone (as rows 120–122) | Ley 100 art. 135 par. 3; DUR 1625 art. 1.2.4.1.11 | Calculation (tax flag) |
| Integral salary IBC; levy base | As CCG v1.4 | 70% + Ley 1393 excess; levy base without the excess | as CCG | Calculation |
| Termination indemnity base | — | CST 127 salary with variable parts | as CCG | Calculation |
| 346 (third-party meal payments) | Non-remunerative | Non-Salary - pacted | CST 128 | Calculation (40% test) |
| Column V | — | Salary-nature values reviewed | CST 127, 128 | Mapping |
| Column Y (230–237, 253–264, 348–350 and others) | Pacted rows → AuxilioS | AuxilioNS (NIE142) with a pact, otherwise AuxilioS (NIE141) | Anexo Técnico NE v1.0 pp. 32–39 | NE report mapping |
| 201–206, 214–216 (car allowance notes) | — | Note on the purpose of the payment | CSJ SL5159-2018 | Text only |
| Employer Sick Pay | — | Minimum-wage floor note; open items closed | Corte Constitucional C-543 de 2007 | Text only |

### DD (v1.3 → v1.6)

| Where | Change | Legal basis | Design impact |
|---|---|---|---|
| Country Fields (new) | New fields: subsidised-regime permanence (worker type 75), PILA salary type, special pension rate indicator, work-centre ARL activity and risk-class link, housing-loan interest and voluntary-savings certificates, termination cause, pension payer / pensioner data (CO-PILA-007) | PILA AT2 v30, AT3 v15 | Mapping (new inputs) |
| Mappers | Apprentice codes (Ley 2466 de 2025); document types and identifier rules (AT2 v30); bank payment-method list | Ley 2466 art. 21; AT2 v30; Anexo NE tables 5.3.3.1/2 | Mapping |
| ID Information 7–9; Mappers 95, 104 | Bank attributes only for account-crediting methods (42, 45, 47, 98; 46 if a client adds it); method 98 (CATS) added | Anexo NE NIE064–068 | Mapping |

### Report Specs (v1.0 → current)

| Spec | Change | Legal basis | Design impact |
|---|---|---|---|
| CO-PILA-003 (v1.2) | ET 114-1 two-limb test (field 76); integral salary IBC with the 1393 excess; rate fields as decimals with a point (ARL 0.0052200); contributor type 75 and subtypes; solidarity bands; document types (AT2 v30); correction returns (type N) | ET 114-1; AT2 v30 fields 28, 61, 76 | Report mapping + calculation |
| CO-DIAN-001 NE (v1.2) | Sample XML on XSD v1.0.6; no negative amounts; days not worked; overtime / night window (Ley 2101, Ley 2466); YTD caps; bank attributes for 42/45/47/98 | XSD v1.0.6; DIAN Concepto 014745 de 2025 | Report mapping |
| CO-DIAN-004 Form 220 (v1.3) | Worked example: gross 169,440,000; casilla 59 average 12,000,000 (6 months before the deposit, salary only); non-resident variant 20% × 156,000,000; annual withholding rounded to 1,000 | Instructivo Form 220 (Res. DIAN 22 de 2024); DIAN Concepto 1302 de 2019 | Report mapping |
| CO-DIAN-005 Format 2276 (v1.2) | Official XSD element names; N33 = 12,000,000; non-resident N29 = 31,200,000; no 1,000 rounding in this format | Res. DIAN 000227 de 2025; XSD 2276 | Report mapping |
| CO-DIAN-002 Form 350 (v1.1) | Casilla 28 disabled from June 2026; withholding rounded to 1,000 only on the return; casilla 996 added | DIAN Oficio 15662 de 2026; DUR 1625 art. 1.6.1.11.11 | Report mapping |
| CO-CESANTIAS-006 (v1.2) | Transport allowance in the severance base; no minimum month (CST 310); fund codes; no withholding for non-residents | Ley 1 de 1963 art. 7; Corte Constitucional C-078 de 2023 | Calculation + mapping |
| CO-PILA-007 (v1.1) | Document type PC added; pension field and IBC rounding notes | AT3 v15 | Mapping |

### SIR (v1.1 → v1.4) and Payslip (v1.1 → v1.3)

| Artifact | Change | Design impact |
|---|---|---|
| SIR | Pensioners' PILA (CO-PILA-007) added as channel CO-OUT-PILA-002 (7 in-scope filings); NE as support for costs and deductions (Res. DIAN 000227 art. 1.5.3.2.1); Format 2276 calendar; NE contingency 48 h; validation-rule count | Report mapping (new channel) |
| Payslip | Worked example on the YTD caps (withholding 1,993,152; net 15,478,848); solidarity fund rounded per sub-account; disclosure basis Ley 1393 art. 32; QR / CUNE / period fields | Payslip layout + example |

---

## Bloco de prova (para o usuário)
- **Pedido → resposta:** lista única em inglês ✔; uma tabela por artefato com onde / antes → depois / por quê / impacto ✔; resumo de 4 linhas no topo ✔; conferido contra os finais ✔ (abaixo); sem citar erro interno ✔ (texto neutro: "before / now").
- **Fontes:** CCG = histórico de versões do `final/CO-CCG-001-v1.7.docx` (linhas 1.5–1.7) + trilha célula a célula em `final/changelogs/CO-CCG-001-v1.6-CHANGELOG.md` (linhas 141–204, 230–537); WTC/DD/specs = aba Version Control dos finais (`CO-WTC-001-v1.9.xlsx`, `CO-DD-001-v1.6.xlsx`, `final/specs/*.xlsx`); decisões e fontes legais = `pesquisa-2026-10-30/TABELA-CONSOLIDADA.md`, `pesquisa-2026-11-02/TABELA-RODADA5.md`; SIR = `CO-SIR-001-v1.3-CHANGELOG.md` + texto v1.4; Payslip = `CO_Compliance_Payslip_Generator-CHANGELOG.md`. "Monthly / YTD": CCG v1.7 parágrafos "Each month stands alone", "No year-end reconciliation of social security", "Annual caps, tracked year-to-date".
- **Teste:** `achar_versao.py Colombia ccg|wtc|dd|sir` (04/11) → maiores versões = finais locais com o md5 do `MD5-FINAIS.txt`; Version Control lida direto dos xlsx finais (openpyxl só leitura); histórico do CCG lido do XML do docx.
- **Confiança: 90%.** Falta: (a) as linhas de "antes" da WTC vêm do resumo da Version Control e das tabelas de decisão, não de um diff célula a célula v1.6 × v1.9 refeito hoje; (b) WTC 311–312 e 322: linhas conferidas no final, mas o "antes" ficou em branco (só no diff); (c) a coluna "Section" do CCG agrupa por módulo pelo assunto (a trilha do changelog usa índices de tabela/parágrafo). Se quiser 100% antes de enviar, rodo o diff v1.6 × v1.9 e preencho os números de linha.

## Onde registrar depois do envio
Hub `paises/Colombia.md` (Pendências/Histórico), `log.md`, estado da frente; anexar no ticket CT-4593 só com ok (ticket é da janela Suporte).
