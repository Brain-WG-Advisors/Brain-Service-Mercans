# -*- coding: utf-8 -*-
"""Rodada 5 da validacao da research da Colombia (2026-11-02): aplica as decisoes de
pesquisa-2026-11-02/TABELA-RODADA5.md ('Muda os finais' + linha 346 do WTC) em COPIAS -DRAFT-R5 dos finais aprovados.
Os finais em final/ so sao lidos (md5 conferido contra final/MD5-FINAIS.txt antes de tudo).

Saidas (revisao/rodada5/): os DRAFT-R5, mudancas-RODADA5.md (gerado do log), MD5-DRAFTS-R5.txt, apply_r5_log.json.
xlsx: cirurgia no XML (r5lib.xlsx_apply), celula alterada em azul FFDDEBF7. docx: alteracoes controladas, autor
'Wallisson Gomes'. Reproduzivel: rodar de novo regrava os mesmos arquivos a partir dos finais.
Uso: python -I revisao/rodada5/scripts/apply_r5.py
"""
import os, sys, json, re, shutil, hashlib
from decimal import Decimal as D, ROUND_HALF_UP
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import r5lib as L
sys.stdout.reconfigure(encoding='utf-8')
VAL = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
FIN = os.path.join(VAL, 'final')
# depois do release de 2026-11-02 os finais de partida (30/10) ficam em final/_historico/2026-10-30/ (com o MD5-FINAIS.txt deles)
if os.path.exists(os.path.join(FIN, '_historico', '2026-10-30', 'MD5-FINAIS.txt')): FIN = os.path.join(FIN, '_historico', '2026-10-30')
OUT = os.path.join(VAL, 'revisao', 'rodada5')

# ------------------------------------------------------------------ 0. finais intactos
def FP(f):  # final de partida: historico de 30/10 se existir la, senao final/ (specs 002 e 007 nao foram substituidas)
    p = os.path.join(FIN, f)
    return p if os.path.exists(p) else os.path.join(VAL, 'final', f)
md5f = {}
for ln in open(os.path.join(FIN, 'MD5-FINAIS.txt'), encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    h, f = ln.split(None, 1); md5f[f.strip()] = h
for f, h in md5f.items():
    assert L.md5(FP(f)) == h, 'final alterado: ' + f

# ------------------------------------------------------------------ 1. contas (A-1) - conferidas por assert
U = D(52374)
def q4(x): return x.quantize(D('0.0001'), ROUND_HALF_UP)
def tab383(base):
    for lo, hi, r, fix in ((0, 95, '0', 0), (95, 150, '0.19', 0), (150, 360, '0.28', 10), (360, 640, '0.33', 69), (640, 945, '0.35', 162),
                           (945, 2300, '0.37', 268), (2300, 10 ** 9, '0.39', 770)):
        if D(lo) * U < base <= D(hi) * U:
            return (base - lo * U) * D(r) + fix * U, lo, D(r), fix
A790, A1340 = 790 * U, 1340 * U
assert A790 == 41375460 and A1340 == 70181160
# T105 (Exemplo 4, set/2026): salario 8.000.000 desde 1/1; bonus 20.000.000 com pacto; IBC 16.800.000
c_month = 8000000 - D('0.09') * 8000000                      # jan-ago: 7.280.000
used = 8 * D('0.25') * c_month                                # 14.560.000
C105 = 28000000 - D('0.09') * 16800000                        # 26.488.000
E105 = min(D('0.25') * C105, A790 - used)
assert used == 14560000 and E105 == 6622000 and E105 <= D('0.4') * C105 and used + E105 <= A1340
G105 = C105 - E105; W105 = tab383(G105)[0]
assert G105 == 19866000 and W105 == D('3947554.80'), W105
# T180 (out/2026): salario 6.000.000 (abaixo de 4 SMMLV: sem FSP, 8%) jan-set; bonus habitual 12.000.000 em outubro
used180 = 9 * D('0.25') * (6000000 - D('0.08') * 6000000)   # 12.420.000
C180 = 18000000 - D('0.09') * 18000000                        # 16.380.000
E180 = min(D('0.25') * C180, A790 - used180); G180 = C180 - E180; W180 = tab383(G180)[0]
assert used180 == 12420000 and E180 == 4095000 and G180 == 12285000 and W180 == D('1763832.00'), W180
# T183 C3 (pacto): contribuicoes 9% x 10.800.000
C183 = 18000000 - D('0.09') * 10800000; E183 = min(D('0.25') * C183, A790 - used180); W183 = tab383(C183 - E183)[0]
assert C183 == 17028000 and E183 == 4257000 and W183 == D('1899912.00')
# T239 (integral 25.000.000; IBC 17.500.000; contribuicoes 1.575.000): mes de janeiro a julho
C239 = D(23425000); E239m = D('0.25') * C239                # 5.856.250
assert 6 * E239m + E239m <= A790 and A790 - 7 * E239m == D('381710')
G239 = C239 - E239m; W239 = tab383(G239)[0]
assert G239 == D('17568750') and W239 == D('3243282.00')
# Payslip (ago/2026, 19.200.000 todo mes, contribuicoes 1.728.000)
CP = D(19200000 - 1728000); EP = D('0.25') * CP
assert 7 * EP + EP <= A790
WP = tab383(CP - EP)[0]; assert WP == D('1993152.00')
NETP = D(19200000) - 1728000 - WP; assert NETP == D('15478848.00')

def uv(x): return f'{q4(D(x) / U):.4f}'

SRC = {
 'A-1': 'CE S4 rad. 11001-03-27-000-2018-00041-00 (24047), 28/10/2021 (anula "es decir ... UVT mensuales" do DUR 1.2.4.1.6 par. 3); Decreto 2231/2023 art. 9 ("1.340 UVT anuales"); ET 206 num. 10; ET 336 num. 3; DIAN Concepto 011383/2024 IV.1',
 'A-1c': 'A-1 + conta refeita (apply_r5.py §1, assert; oracle_r5_ytd.py)',
 'A-1x': 'A-1 (mesma decisão; local fora da lista do lote A, achado na varredura de "apportion"/"one twelfth"/3,447,955)',
 'A-2': 'Ley 100/1993 art. 135 par. 3; DUR 1625 art. 1.2.4.1.11; DIAN Oficios 8899/2015 e 4358/2019; ET 592 num. 2; ET 247 (lote A §2)',
 'A-2x': 'A-2 (consequência na conta do não residente: 20% só sobre o que é retido; local fora da lista do lote A)',
 'SIM-07': 'Instrutivo Form. 220 (Res. DIAN 22/2024) casilla 59, caso (ii); DIAN Concepto 1302/2019; DIAN Concepto 4443/2025; CST 307 (lote C §3)',
 'S-07': 'Anexo Técnico NE v1.0 §6, pp. 182-232 (contagem do lote C §4, dois métodos)',
 'WTC-Y': 'Anexo Técnico NE v1.0 NIE139-NIE142, pp. 36-37; CST 127/128; precedente WTC v1.7 Y201-206 (lote C §5)',
 'L346': 'CST 128 ("cuando las partes hayan dispuesto expresamente que no constituyen salario en dinero o en especie, tales como la alimentación"); CST 129 num. 1 ("salvo la estipulación prevista en el artículo 15 [128]"); padrão WTC v1.7 linhas 201-206',
 'P-06': 'AT2 v30 p.210 (saída às ARL, campo 28 "Tarifa. En decimales", copiado do campo 61); AT3 v15 §2.2.2.25 p.63 (lote B §3)',
 'DD-21': 'Anexo Técnico NE v1.0 NIE064-NIE068 pp. 23-24; tabelas 5.3.3.1/5.3.3.2 pp. 130-131 (lote B §4)',
 'R2708': 'Res. MinTrabajo 2708/2026 arts. 1, 5.4, 8 (lote B §5); CST 132 num. 1, 161 (Ley 2466 art. 11), 162, 179 par. 3 (Ley 2466 art. 14), 22 (Ley 2466 art. 13); Ley 2101/2021 art. 3',
 'VC': 'Controle de versão do DRAFT-R5',
 'AFC': 'DUR 1625 de 2016 art. 1.2.1.22.43 ("hasta un monto máximo de tres mil ochocientas (3.800) Unidades de Valor (UVT) por año"; par. 1 "en el año"); CE S4 rad. 24047, 28/10/2021 (arts. 126-1 e 126-4 "determinaron unos máximos anuales"; limite mensal sobre aportes AFC "conllevaría un efecto inequitativo"); ET arts. 126-1, 126-4 (passo 0 de 2026-11-02, decidido pelo usuário)',
}

LOG = []
ISSUE_SERIAL = 46328   # 2026-11-02

# ------------------------------------------------------------------ 2. xlsx
NR = "Severance savings and their interest are never withheld, for residents and non-residents alike (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11"
CES_CIT = ('ET arts. 206 num. 4 and par. 2, 385, 386;',
           'ET arts. 206 num. 4 and par. 2, 385, 386; Ley 100 de 1993 art. 135 par. 3 and DUR 1625 de 2016 art. 1.2.4.1.11 (no withholding; DIAN Oficios 8899 de 2015 and 4358 de 2019);')
D_CES = ("No withholding, for residents and non-residents alike: severance savings and their interest are never subject to withholding "
         "(Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019), so the ET art. 408 "
         "flat 20% does not apply to them. Configurable option: a client that wants the conservative position may withhold the 20% for "
         "non-residents (off by default).")
Y_AUX = 'Devengados / Auxilio (AuxilioNS, NIE142, where non-salary under the pact; otherwise AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt'
AB346 = ("Default 'Non-Salary - pacted': meals paid for the employee (in kind, by voucher or to a third party) are salary in kind "
         "(CST art. 129 num. 1) unless a written CST art. 128 pact excludes them ('cuando las partes hayan dispuesto expresamente que no "
         "constituyen salario en dinero o en especie, tales como la alimentacion'), and then they are inside the Ley 1393 40% test. "
         "The ET art. 387-1 41-UVT income-tax exclusion (column F) does not depend on this classification. This is an interpretation; "
         "confirm the pact in the employment contract.")
WTC = [
 # A-1 Tax Credit / Coverage
 ('Tax Credit', 'A41', ('set', "        Annual cap, tracked year-to-date: each month min(25% of the month's figure, 790 UVT - exemption taken YTD)."), 'A-1', None),
 ('Tax Credit', 'A65', ('set', "  Annual cap, tracked year-to-date: each month (D + E) <= min(40% of the month's (C), 1,340 UVT - amount taken YTD)."), 'A-1', None),
 ('Tax Credit', 'A66', ('set', "  NO MONTHLY ONE-TWELFTH LIMIT: the Consejo de Estado (Seccion Cuarta, rad. 24047, 28 October 2021) annulled the monthly"), 'A-1', None),
 ('Tax Credit', 'A67', ('set', "  equivalent ('es decir ... UVT mensuales') of Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3; Decreto 2231 de 2023 art. 9 restated"), 'A-1', None),
 ('Tax Credit', 'A68', ('set', "  it in annual UVT only. DIAN Concepto 011383 de 2024 (IV.1): the agent observes the annual limit per individual."), 'A-1', None),
 # passo 0 (2026-11-02): teto de 3.800 UVT de AFC/AVC/fundos voluntarios anual, pelo acumulado
 ('Tax Credit', 'A34', ('sub', [("SHARED between the two vehicles . ET arts. 126-1, 126-4",
   "SHARED between the two vehicles; annual cap tracked year-to-date, no monthly one-twelfth limit . ET arts. 126-1, 126-4; DUR 1625 de 2016 art. 1.2.1.22.43")]), 'AFC', None),
 ('Global WTC Coverage', 'C16',('sub', [(" (4) The monthly apportionment of the annual 790-UVT and 1,340-UVT tax caps - no regulation prescribes it expressly; Mercans applies one twelfth.", '')]), 'A-1', None),
 # A-2
 ('Global WTC Coverage', 'B22', ('sub', [("The 25% exemption of art. 206 num. 10 does NOT apply to them (art. 206 par. 2).",
   "The 25% exemption of art. 206 num. 10 does NOT apply to them (art. 206 par. 2). NOT WITHHELD for any employee, resident or non-resident (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11): the ET art. 408 flat 20% does not apply to them; the conservative 20% for non-residents is a configurable option, off by default.")]), 'A-2', None),
 ('Global WTC Coverage', 'C22', ('sub', [CES_CIT]), 'A-2', None),
]
for r in (120, 121, 122, 321, 322):
    WTC += [('Wage Type Catalogue', f'N{r}', ('set', 'No'), 'A-2', None),
            ('Wage Type Catalogue', f'P{r}', ('set', 'No'), 'A-2', None),
            ('Wage Type Catalogue', f'D{r}', ('set', D_CES), 'A-2', None),
            ('Wage Type Catalogue', f'Z{r}', ('sub', [CES_CIT]), 'A-2', None)]
# WTC-Y
for r in range(255, 265):
    WTC.append(('Wage Type Catalogue', f'Y{r}', ('set', Y_AUX), 'WTC-Y', None))
for r in (114, 115, 116):
    WTC.append(('Wage Type Catalogue', f'Y{r}', ('set', 'Devengados / Bonificacion - BonificacionS (NIE139)'), 'WTC-Y', None))
for r in range(124, 134):
    WTC.append(('Wage Type Catalogue', f'Y{r}', ('set', 'Devengados / Bonificacion - BonificacionS (NIE139)'), 'WTC-Y', None))
WTC.append(('Wage Type Catalogue', 'V1', ('sub', [("Both values map to the nomina electronica NS element.",
  "'Non-Salary - non-remunerative' maps to the nomina electronica NS element; 'Non-Salary - pacted' maps to the NS element where the non-salary pact holds (DD pact flag set) and, without the pact, to the S element (salary under CST art. 127).")]), 'WTC-Y', None))
# linha 346
for c in 'QRSU':
    WTC.append(('Wage Type Catalogue', f'{c}346', ('set', 'Yes/No'), 'L346', None))
WTC += [('Wage Type Catalogue', 'V346', ('set', 'Non-Salary - pacted'), 'L346', None),
        ('Wage Type Catalogue', 'Y346', ('set', 'Devengados / BonoEPCTV (PagoAlimentacionNS, NIE154, where non-salary under the pact; otherwise PagoAlimentacionS, NIE153)'), 'L346', None),
        ('Wage Type Catalogue', 'AB346', ('set', AB346), 'L346', 'AB201')]
WTC += [('Version Control', 'B20', ('set', '1.8 (DRAFT-R5)'), 'VC', 'B19'), ('Version Control', 'C20', ('num', ISSUE_SERIAL), 'VC', 'C19'),
        ('Version Control', 'D20', ('set', "Validation corrections, round 5 (DRAFT): the 790-UVT and 1,340-UVT caps are annual and tracked year-to-date (Tax Credit; Global WTC Coverage item 15), and so is the shared 3,800-UVT cap of voluntary pension funds and AFC / AVC accounts (Tax Credit B4); severance savings and their interest are not withheld for any employee (rows 120-122 and 321-322, CO-TX-02); third-party meal payments 'Non-Salary - pacted' (row 346); nomina electronica elements of the pacted education allowances, the holiday allowance and the bonus rows (column Y) and of the header of column V."), 'VC', 'D19'),
        ('Version Control', 'E20', ('set', 'Draft'), 'VC', 'E19'), ('Version Control', 'F20', ('set', L.AUTHOR), 'VC', 'F19')]

DD = [
 ('ID Information', 'H7', ('set', "Partial list. Bank name, account type and account number are populated only for account-crediting payment methods (Anexo Tecnico NE v1.0 table 5.3.3.2): 42 (Consignacion bancaria), 45 (Transferencia Credito Bancario), 46 (Transferencia Debito Interbancario), 47 (Transferencia Debito Bancaria) and 98 (CATS: Nequi, Daviplata), and 30 / 31 (Transferencia Credito / Debito) if used; left empty for 10 (Efectivo), 20, 23, 25 and 26 (cheques), 71 (Bonos), 72 (Vales) and ZZZ (Acuerdo mutuo). Cards (48, 49) count as account-based only where the client pays salary to a card linked to an account (an interpretation). The annex makes the three attributes optional (0-1, NIE066-NIE068); requiring all three for account-crediting methods is an engine rule. Must be absent or empty where Payment Method = 10 (cash). The bank / non-bank classification of each code is an interpretation; confirm with DIAN."), 'DD-21', None),
 ('ID Information', 'H8', ('sub', [('where Payment Method is a bank-mediated medium.', 'where Payment Method is an account-crediting method (see Employee Bank Name).')]), 'DD-21', None),
 ('ID Information', 'H9', ('sub', [('where Payment Method is a bank-mediated medium.', 'where Payment Method is an account-crediting method (see Employee Bank Name).')]), 'DD-21', None),
 ('Country Option Mappers', 'C104', ('set', '98'), 'DD-21', 'C103'),
 ('Country Option Mappers', 'D104', ('set', 'CATS'), 'DD-21', 'D103'),
 ('Country Option Mappers', 'E104', ('set', 'Cuentas de Ahorro de Tramite Simplificado (CATS)'), 'DD-21', 'E103'),
 ('Country Option Mappers', 'F104', ('set', 'Simplified-procedure savings accounts (Nequi, Daviplata, etc.). Account-based: the bank attributes are populated.'), 'DD-21', 'F103'),
 ('Version Control', 'B18', ('set', '1.5 (DRAFT-R5)'), 'VC', 'B17'), ('Version Control', 'C18', ('num', ISSUE_SERIAL), 'VC', 'C17'),
 ('Version Control', 'D18', ('set', 'Validation corrections, round 5 (DRAFT): bank attributes only for account-crediting payment methods (ID Information rows 7-9); payment method 98 (CATS) added to the Payment Method mapper (row 104).'), 'VC', 'D17'),
 ('Version Control', 'E18', ('set', 'Draft'), 'VC', 'E17'), ('Version Control', 'F18', ('set', L.AUTHOR), 'VC', 'F17'),
]

def spec_vc(desc):
    return [('Version Control', 'B15', ('set', '1.2 (DRAFT-R5)'), 'VC', 'B14'), ('Version Control', 'C15', ('set', '2026-11-02'), 'VC', 'C14'),
            ('Version Control', 'D15', ('set', desc), 'VC', 'D14'), ('Version Control', 'E15', ('set', 'Draft'), 'VC', 'E14'),
            ('Version Control', 'F15', ('set', L.AUTHOR), 'VC', 'F14'), ('Report Matrix', 'B19', ('set', 'v1.2 (DRAFT-R5)'), 'VC', None)]

NE = [
 ('Population Rules', 'C21', ('sub', [("nor 1,340 UVT per year (the annual limit is apportioned at 111.6667 UVT per month, a configurable apportionment rule).",
   "nor 1,340 UVT per year. The 790-UVT and 1,340-UVT limits are annual and are tracked year-to-date per employee: each month only the part not yet used in the year is available (no monthly one-twelfth limit: Consejo de Estado, Seccion Cuarta, rad. 24047 of 2021; Decreto 2231 de 2023 art. 9).")]), 'A-1x', None),
 ('Population Rules', 'C22', ('sub', [("This applies to salary, to the service bonus, to severance savings, to dismissal indemnity, to equity income and to benefits in kind alike.",
   "This applies to salary, to the service bonus, to dismissal indemnity, to equity income and to benefits in kind alike. " + NR + "; DIAN Oficios 8899 de 2015 and 4358 de 2019); a client may configure the conservative 20% for them (option, off by default).")]), 'A-2', None),
 ('Example Analysis', 'C39', ('sub', [("(within both the 40% and the apportioned 1,340-UVT caps)", "(within the 40% limit and the annual 790-UVT and 1,340-UVT caps, tracked year-to-date)")]), 'A-1', None),
] + spec_vc('Validation corrections, round 5 (DRAFT): the 790-UVT and 1,340-UVT caps tracked year-to-date, no monthly one-twelfth limit (Population Rules C21, Example Analysis C39); severance savings and their interest not withheld for non-residents (Population Rules C22).')

C26_NEW = ("Employment is ongoing, so the window is the six months of 2025, the year before the February 2026 deposit (Form 220 instructions, casilla 59, case (ii); DIAN Concepto 1302 de 2019; DIAN Concepto 4443 de 2025). "
           "Only salary counts: 'las sumas que habitual y periodicamente recibe el trabajador ... como contraprestacion directa del servicio' (DIAN Concepto 1302 de 2019); the service bonus is not salary (CST art. 307). "
           "Assuming the same COP 12,000,000 monthly salary in July-December 2025: average = 12,000,000. For a leaver, use the last six months of employment.")
F220 = [
 ('Field Options', 'D22', ('set', "Annual cap on the 25% exempt income, tracked year-to-date per employee: each month the exemption is limited to the part of the 790 UVT not yet used in the year. There is no monthly one-twelfth limit (Consejo de Estado, Seccion Cuarta, rad. 24047 of 2021; DIAN Concepto 011383 de 2024, IV.1)."), 'A-1', None),
 ('Field Options', 'D23', ('set', "Annual cap on deductions plus exempt income, alongside the 40% limit, tracked year-to-date per employee: each month (D + E) is limited to the part of the 1,340 UVT not yet used in the year (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3, as modified by Decreto 2231 de 2023 art. 9; no monthly one-twelfth limit)."), 'A-1', None),
 ('Report Matrix', 'A34', ('set', "- Severance savings and their interest (casillas 47 to 49) are never withheld, for residents and non-residents alike (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11), so the six-month average of casilla 59 has no effect on casilla 60. For a non-resident it is reported for completeness; the art. 206 num. 4 exemption is applied, if at all, in the employee's own return (an interpretation)."), 'A-2', None),
 ('Population Rules', 'C21', ('sub', [("Casilla 52 carries the gross and casilla 60 carries 20% of it under ET art. 408 - so the two stand in a simple 20% relationship with no depuration visible.",
   "Casilla 52 carries the gross and casilla 60 carries 20% under ET art. 408 of the gross less the severance savings and interest of casillas 47 to 49, which are never withheld (Ley 100 de 1993 art. 135 par. 3) - no depuration is visible.")]), 'A-2x', None),
 ('Population Rules', 'D21', ('set', "Casilla 59 is reported for completeness but has no withholding effect: severance savings and their interest are not withheld for anyone (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11)."), 'A-2', None),
 ('Example Analysis', 'A26', ('set', '12.000.000'), 'SIM-07', None),
 ('Example Analysis', 'C26', ('set', C26_NEW), 'SIM-07', None),
 ('Example Analysis', 'A33', ('set', '169.440.000 / 31.200.000'), 'A-2x', None),
 ('Example Analysis', 'C33', ('set', "The same gross income; the flat 20% of ET art. 408 applies to all of it except the severance savings and interest of casillas 47 and 49 (never withheld, Ley 100 de 1993 art. 135 par. 3): 20% x 156,000,000 = COP 31,200,000."), 'A-2x', None),
 ('Example Analysis', 'D33', ('sub', [("About four and a half times (33,888,000 / 7,407,000 = 4.58)", "About four times (31,200,000 / 7,407,000 = 4.21)")]), 'A-2x', None),
 ('Example Analysis', 'A34', ('set', '12.000.000'), 'SIM-07', None),
 ('Example Analysis', 'D34', ('set', "Severance savings and their interest are not withheld for a non-resident either (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11); the art. 206 num. 4 exemption is applied, if at all, in the employee's own return (an interpretation)."), 'A-2', None),
 ('Formulario 220 Spec', 'K51', ('set', '12000000'), 'SIM-07', None),
 ('Sample File', 'A78', ('sub', [('  13.000.000', '  12.000.000')]), 'SIM-07', None),
 ('Sample File', 'A123', ('sub', [('  13.000.000  (no effect)', '  12.000.000  (no effect)')]), 'SIM-07', None),
 ('Sample File', 'A124', ('set', ' 60  VALOR DE LA RETENCION EN LA FUENTE ..................  31.200.000  <== 20% x 156.000.000'), 'A-2x', None),
 ('Sample File', 'A126', ('set', 'ET art. 408 taxes the GROSS at a flat 20%, except the severance savings and'), 'A-2x', None),
 ('Sample File', 'A127', ('set', 'interest of casillas 47 and 49, never withheld (Ley 100 art. 135 par. 3):'), 'A-2x', None),
 ('Sample File', 'A128', ('set', '20% x 156,000,000 = 31,200,000. Casillas 53 and 54 are still certified because'), 'A-2x', None),
 ('Sample File', 'A129', ('set', 'they were deducted, but they did NOT reduce the withholding base. Casilla 59 is'), 'A-2x', None),
 ('Sample File', 'A130', ('set', 'reported for completeness and has no withholding effect.'), 'A-2x', None),
] + spec_vc('Validation corrections, round 5 (DRAFT): casilla 59 six-month average 12,000,000 (six months of the year before the deposit, salary only); severance savings and interest not withheld for non-residents (non-resident variant 20% x 156,000,000 = 31,200,000); the 790-UVT and 1,340-UVT caps tracked year-to-date (Field Options D22, D23).')

C28_NEW = "Populated because severance was paid and deposited, so ET art. 206 num. 4 applies. " + C26_NEW
F2276 = [
 ('Report Matrix', 'A34', ('set', "- NON-RESIDENT: numeral 29 carries the FLAT 20% of ET art. 408 on the GROSS less the severance numerals 18 to 20, which are never withheld (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11). Numerals 23 and 24 still report the contributions actually deducted, but they did NOT reduce the base - art. 408 admits no depuration. Numeral 33 is reported where severance was paid, without withholding effect."), 'A-2', None),
 ('Report Matrix', 'A35', ('sub', [("a non-resident's numeral 29 is close to exactly 20% of numeral 22,", "a non-resident's numeral 29 is close to exactly 20% of numeral 22 less numerals 18 to 20,")]), 'A-2x', None),
 ('Population Rules', 'C22', ('set', "Accumulate the flat 20% of ET art. 408 applied to the GROSS, excluding severance savings and their interest (numerals 18 to 20), which are never withheld (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11). Numerals 23 and 24 still report the contributions actually deducted, but they did NOT reduce the base - art. 408 admits no depuration. Numeral 33 is reported where severance was paid, without withholding effect."), 'A-2', None),
 ('Population Rules', 'D22', ('sub', [("numeral 29 should be almost exactly 20% of numeral 22.", "numeral 29 should be almost exactly 20% of numeral 22 less numerals 18 to 20.")]), 'A-2x', None),
 ('Example Analysis', 'A28', ('set', '12000000'), 'SIM-07', None),
 ('Example Analysis', 'C28', ('set', C28_NEW), 'SIM-07', None),
 ('Example Analysis', 'A33', ('set', '169440000 / 31200000'), 'A-2x', None),
 ('Example Analysis', 'C33', ('set', "The same gross; the flat 20% of ET art. 408 applies to all of it except the severance numerals 18 and 19 (never withheld, Ley 100 de 1993 art. 135 par. 3): 20% x 156,000,000 = 31,200,000."), 'A-2x', None),
 ('Example Analysis', 'D33', ('sub', [("N29 is almost exactly 20% of N22. Here 33,888,000 / 169,440,000 = 20.00%.", "N29 is almost exactly 20% of N22 less N18 to N20. Here 31,200,000 / (169,440,000 - 13,440,000) = 20.00%.")]), 'A-2x', None),
 ('Example Analysis', 'A35', ('set', '12000000'), 'SIM-07', None),
 ('Example Analysis', 'D35', ('set', "Severance savings and their interest are not withheld for a non-resident either (Ley 100 de 1993 art. 135 par. 3); the art. 206 num. 4 exemption is applied, if at all, in the employee's own return (an interpretation)."), 'A-2', None),
 ('Formato 2276 Spec', 'K42', ('set', '12000000'), 'SIM-07', None),
 ('Sample File', 'A82', ('sub', [('  13000000   (only', '  12000000   (only')]), 'SIM-07', None),
 ('Sample File', 'A96', ('set', '  N29  WITHHOLDINGS MADE .................  31200000   <== 20% x (N22 - N18 - N19), ET art. 408'), 'A-2x', None),
 ('Sample File', 'A97', ('sub', [('  13000000   (reported', '  12000000   (reported')]), 'SIM-07', None),
 ('Sample File', 'A99', ('set', 'INTERNAL CONTROL: for a pure non-resident record N29 / (N22 - N18 to N20) = 20.00%.'), 'A-2x', None),
] + spec_vc('Validation corrections, round 5 (DRAFT): N33 six-month average 12,000,000 (six months of the year before the deposit, salary only); severance savings and interest not withheld for non-residents (non-resident N29 = 20% x 156,000,000 = 31,200,000; control N29 / (N22 - N18 to N20)).')

CES006 = [
 ('Report Matrix', 'A37', ('sub', [("For a NON-RESIDENT the art. 206 num. 4 exemption is unavailable - it belongs to the resident ID card general - and the payment is taxed at the flat 20% of ET art. 408 on the gross with no art. 388 depuration.",
   "For residents and non-residents alike, severance savings and their interest are never withheld (Ley 100 de 1993 art. 135 par. 3; DUR 1625 de 2016 art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019): the flat 20% of ET art. 408 does not apply to them, and a non-resident settles the tax in their own return.")]), 'A-2', None),
] + spec_vc('Validation corrections, round 5 (DRAFT): severance savings and their interest are not withheld for non-residents (Report Matrix A37).')

ARLP = "0.0052200"
PILA003 = [
 ('PILA Spec', 'J131', ('set', 'N(9) - rate as a decimal with a point, left-justified, ZERO-filled to the right (e.g. 0.0052200)'), 'P-06', None),
 ('PILA Spec', 'K131', ('set', ARLP), 'P-06', None),
 ('PILA Spec', 'P131', ('set', "Not an amount - no rounding. Rate written as a decimal with a point, left-justified and zero-filled to 9 positions (class I 0.522% = 0.0052200; class V 6.960% = 0.0696000): the AT2 v30 output layout to the occupational-risk administrators copies this field as 'Tarifa. En decimales' (p.210). Confirm with the information operator during set-up."), 'P-06', None),
 ('Population Rules', 'C17', ('sub', [("T2R2-061 (nine positions) keeps its own format.", "The nine-position occupational-risk rate (T2R2-061) follows the same rule, zero-filled to nine positions (0.522% = 0.0052200), because the AT2 v30 output layout copies it to the occupational-risk administrators as 'Tarifa. En decimales' (p.210).")]), 'P-06', None),
 ('Population Rules', 'D17', ('sub', [(", and it differs between the seven-position and nine-position rate fields.", ".")]), 'P-06', None),
 ('Example Analysis', 'A33', ('set', '1 / ' + ARLP), 'P-06', None),
 ('Sample File', 'A86', ('sub', [('0000000000000052200000000010000627000.04', '00000000000.0052200000000010000627000.04')]), 'P-06', None),
 ('Sample File', 'A113', ('set', '    pos 381-389  0.0052200 - tarifa riesgos laborales, class I, 0.522%'), 'P-06', None),
] + spec_vc('Validation corrections, round 5 (DRAFT): occupational-risk rate T2R2-061 written as a decimal with a point, zero-filled to nine positions (0.0052200), as the other rate fields (PILA Spec row 131, Population Rules C17, Example Analysis A33, Sample File).')

A82_EN = (" (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336).",
          " (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336). The 790-UVT and 1,340-UVT limits are annual and tracked year-to-date per employee, with no monthly one-twelfth limit (Consejo de Estado, Seccion Cuarta, rad. 24047 of 2021); the example assumes the same monthly pay since January 2026.")
A82_ES = (" (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336).",
          " (DUR 1625 de 2016 art. 1.2.4.1.6 par. 3; Art. 336). Los limites de 790 UVT y 1.340 UVT son anuales y se controlan por el acumulado del ano de cada trabajador, sin tope mensual de una doceava parte (Consejo de Estado, Seccion Cuarta, rad. 24047 de 2021); el ejemplo supone el mismo pago mensual desde enero de 2026.")
PAY = []
for sh, a82 in (('Colombia (EN)', A82_EN), ('Colombia (ES)', A82_ES)):
    PAY += [(sh, 'H37', ('num', '1993152'), 'A-1x', None),
            (sh, 'I8', ('cache', '15478848'), 'A-1x', None),
            (sh, 'H38', ('cache', '3,721,152.00 COP'), 'A-1x', None),
            (sh, 'H40', ('cache', '15,478,848.00 COP'), 'A-1x', None),
            (sh, 'A82', ('sub', [a82]), 'A-1x', None)]
PAY += [('Payslip Spec', 'B86', ('set', 'v1.3 (DRAFT-R5)'), 'VC', 'B85'), ('Payslip Spec', 'C86', ('set', '2026-11-02'), 'VC', 'C85'),
        ('Payslip Spec', 'D86', ('set', 'Validation corrections, round 5 (DRAFT): the 790-UVT and 1,340-UVT caps are annual and tracked year-to-date (no monthly one-twelfth limit); worked example (August 2026, same pay since January) withholding 1,993,152.00 and net pay 15,478,848.00; note on the withholding (row 82).'), 'VC', 'D85'),
        ('Payslip Spec', 'E86', ('set', L.AUTHOR), 'VC', 'E85')]
assert 768000 + 768000 + 192000 + 1993152 == 3721152

XLSX = [
 ('WTC', 'CO-WTC-001-v1.7.xlsx', 'CO-WTC-001-v1.8-DRAFT-R5.xlsx', WTC),
 ('DD', 'CO-DD-001-v1.4.xlsx', 'CO-DD-001-v1.5-DRAFT-R5.xlsx', DD),
 ('NE', 'specs/CO-DIAN-001-NominaElectronica-Spec.xlsx', 'CO-DIAN-001-NominaElectronica-Spec-v1.2-DRAFT-R5.xlsx', NE),
 ('F220', 'specs/CO-DIAN-004-Formulario220-Spec.xlsx', 'CO-DIAN-004-Formulario220-Spec-v1.2-DRAFT-R5.xlsx', F220),
 ('F2276', 'specs/CO-DIAN-005-Formato2276-Spec.xlsx', 'CO-DIAN-005-Formato2276-Spec-v1.2-DRAFT-R5.xlsx', F2276),
 ('CES006', 'specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx', 'CO-CESANTIAS-006-ConsignacionAnual-Spec-v1.2-DRAFT-R5.xlsx', CES006),
 ('PILA003', 'specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx', 'CO-PILA-003-AportesSeguridadSocial-Spec-v1.2-DRAFT-R5.xlsx', PILA003),
 ('PAYSLIP', 'CO_Compliance_Payslip_Generator.xlsx', 'CO_Compliance_Payslip_Generator-v1.3-DRAFT-R5.xlsx', PAY),
]

# ------------------------------------------------------------------ 3. CCG (docx, alteracoes controladas)
AN = "Consejo de Estado, Sección Cuarta, rad. 24047 of 28 October 2021"
P661_OLD = None   # whole paragraph (read at run time)
P661_NEW = ("Annual caps, tracked year-to-date. The 790-tax-unit and 1,340-tax-unit caps are annual and are tracked cumulatively per employee for the calendar year. "
            "There is no monthly one-twelfth limit: the Consejo de Estado annulled the monthly equivalent (\"es decir … UVT mensuales\") of Decree 1625 of 2016 art. 1.2.4.1.6 par. 3 "
            "(Sección Cuarta, rad. 24047, 28 October 2021), and Decree 2231 of 2023 art. 9 restated the limit in annual units only (\"1.340 UVT anuales\"). "
            "DIAN Concepto 011383 of 2024 (IV.1): the withholding agent observes the annual limit \"en los pagos realizados a cada persona natural\". "
            "Each month: 25% exemption = the lower of 25% of the month's figure and 790 tax units less the exemption already taken in the year; "
            "(D + E) = the lower of 40% of the month's (C) and 1,340 tax units less the amount already taken in the year. The 40% limit itself stays monthly "
            "(art. 388: on the payment of the month). A mid-year migration must load the consumption to date. A one-twelfth test would over-withhold in high-pay months.")
CCG = [
 # (id, loc, old, new)   old=None -> whole paragraph text
 ('A-1', 'P661', None, P661_NEW),
 ('A-1c', 'P766', 'subject to a valid written non-salary pact.',
  'subject to a valid written non-salary pact. Premise for the annual caps: the same salary since 1 January 2026 and no other deductions or exempt income in the year, so the 25% exemption already taken January–August is 8 × 1,820,000 = 14,560,000 (the resident worked example, August 2026). The 25% of the June statutory service bonus, withheld separately, would add about 1,000,000 and leaves the result unchanged.'),
 ('A-1c', 'P768', None,
  'Two lessons this example makes concrete: the 40% clamp forced COP 8,800,000 of a "non-salary" bonus back into the contribution base, and the 790-tax-unit cap is annual and tracked year-to-date: with COP 26,815,460 of the year\'s cap still unused, the full 25% (COP 6,622,000) is exempt in the bonus month. A one-twelfth monthly figure (COP 3,447,955) has no legal basis (' + AN + ') and would over-withhold COP 1,047,434.85 in this month.'),
 ('A-1x', 'P1047', None, 'Two caps bite hardest on irregular payments; the engine tests them each month against the part of the annual cap not yet used in the year:'),
 ('A-1x', 'P1049', None, 'A one-off payment hits the first cap only when 25% of the depurated base exceeds the part of the COP 41,375,460 not yet used in the year. There is no monthly one-twelfth limit (' + AN + '): in the retention-bonus example in Module 6.3 the full 25% is exempt.'),
 ('A-1c', 'P1066', 'so no valid non-salary pact applies and it is fully salary under Labour Code art. 127.',
  'so no valid non-salary pact applies and it is fully salary under Labour Code art. 127. Premise for the annual caps: the same salary since 1 January 2026 and no other deductions or exempt income in the year; January–September the 25% exemption taken is 9 × 25% × (6,000,000 − 480,000 health and pension; no solidarity fund below 4 minimum wages) = 9 × 1,380,000 = 12,420,000.'),
 ('A-1x', 'P1311', 'and it engages four separate rules at once.',
  'and it engages four separate rules at once. Premise for the annual caps: the same salary since 1 January 2026 and no other exempt income; the month shown is any month from January to July.'),
 ('A-1', 'T91R8C1', None, '790 units = 41,375,460 a year, tracked year-to-date: 12 × 1,820,000 = 21,840,000 → below in every month'),
 ('A-1', 'T91R10C1', None, '1,340 units = 70,181,160 a year, tracked year-to-date: 12 × 1,820,000 = 21,840,000 → below in every month'),
 ('A-1', 'T103R9C0', None, '— 790-unit annual cap (year-to-date)'),
 ('A-1', 'T103R9C1', None, '41,375,460 a year; 12 × 1,145,000 = 13,740,000 → within'),
 ('A-1', 'T103R12C0', None, '— 1,340-unit annual cap (year-to-date)'),
 ('A-1', 'T103R12C1', None, '70,181,160 a year; 12 × 2,912,000 = 34,944,000 → not reached'),
 ('A-1c', 'T105R13C1', None, '25% × 26,488,000 = 6,622,000; 790-unit annual cap, year-to-date: 41,375,460 − 14,560,000 already taken January–August = 26,815,460 → not capped'),
 ('A-1c', 'T105R13C2', None, '(6,622,000.00)'),
 ('A-1c', 'T105R14C1', None, '40% × 26,488,000 = 10,595,200 → 6,622,000 is within; 1,340-unit annual cap: 14,560,000 + 6,622,000 = 21,182,000 ≤ 70,181,160 → within'),
 ('A-1c', 'T105R15C1', None, '26,488,000 − 6,622,000'),
 ('A-1c', 'T105R15C2', None, '19,866,000.00'),
 ('A-1c', 'T105R16C1', None, '19,866,000 ÷ 52,374'),
 ('A-1c', 'T105R16C2', None, uv(G105)),
 ('A-1c', 'T105R18C1', None, f'({uv(G105)} − 360) × 33% + 69 = {q4((q4(G105 / U) - 360) * D("0.33")):.4f} + 69 = {q4(q4((q4(G105 / U) - 360) * D("0.33")) + 69):.4f}'),
 ('A-1c', 'T105R19C1', None, f'{q4(q4((q4(G105 / U) - 360) * D("0.33")) + 69):.4f} × 52,374'),
 ('A-1c', 'T105R19C2', None, f'{W105:,.2f}'),
 ('A-1', 'T117R3C1', None, '790 tax units per year = COP 41,375,460, tracked year-to-date per employee (no monthly one-twelfth limit)'),
 ('A-1', 'T169R5C1', None, '25% × 7,327,500 = 1,831,875; within the 790-unit annual cap (year-to-date) → not capped'),
 ('A-1', 'T175R0C1', None, 'Annual cap 2026, tracked year-to-date per employee'),
 ('A-1', 'T175R1C1', None, 'COP 41,375,460 less the exemption already taken in the year'),
 ('A-1', 'T175R2C1', None, 'COP 70,181,160 less the amount already taken in the year'),
 ('A-1c', 'T180R5C1', None, '25% × 16,380,000 = 4,095,000; 790-unit annual cap, year-to-date: 41,375,460 − 12,420,000 already taken January–September = 28,955,460 → not capped'),
 ('A-1c', 'T180R5C2', None, '(4,095,000.00)'),
 ('A-1c', 'T180R6C1', None, '40% × 16,380,000 = 6,552,000 → 4,095,000 is within'),
 ('A-1c', 'T180R7C0', None, '— 1,340-unit annual cap (year-to-date)'),
 ('A-1c', 'T180R7C1', None, '12,420,000 + 4,095,000 = 16,515,000 ≤ 70,181,160 → not reached'),
 ('A-1c', 'T180R8C1', None, '16,380,000 − 4,095,000'),
 ('A-1c', 'T180R8C2', None, '12,285,000.00'),
 ('A-1c', 'T180R9C1', None, '12,285,000 ÷ 52,374'),
 ('A-1c', 'T180R9C2', None, uv(G180)),
 ('A-1c', 'T180R11C1', None, f'({uv(G180)} − 150) × 28% + 10 = {q4((q4(G180 / U) - 150) * D("0.28")):.4f} + 10 = {q4(q4((q4(G180 / U) - 150) * D("0.28")) + 10):.4f}'),
 ('A-1c', 'T180R12C1', None, f'{q4(q4((q4(G180 / U) - 150) * D("0.28")) + 10):.4f} × 52,374'),
 ('A-1c', 'T180R12C2', None, f'{W180:,.2f}'),
 ('A-1c', 'T181R7C1', None, f'({W180:,.2f})'),
 ('A-1c', 'T181R8C1', None, f'{D(18000000) - 1620000 - W180:,.2f}'),
 ('A-1c', 'T183R9C2', None, f'{W180:,.2f}'),
 ('A-1c', 'T183R9C3', '2,126,444.60', f'{W183:,.2f}'),
 ('A-1', 'T202R10C1', None, 'No proration: annual caps tracked year-to-date per employee (790 units = COP 41,375,460; 1,340 units = COP 70,181,160)'),
 ('A-1x', 'T215R12C0', None, 'Annual cap on the 25% exempt income (790 units), tracked year-to-date; the examples assume the same pay since 1 January'),
 ('A-1x', 'T215R12C1', None, 'COP 41,375,460'),
 ('A-1x', 'T215R13C0', None, 'Annual cap on combined deductions and exempt income (1,340 units), tracked year-to-date'),
 ('A-1x', 'T215R13C1', None, 'COP 70,181,160'),
 ('A-1x', 'T219R5C1', None, '25% × 1,859,800 = 464,950; within the 790-unit annual cap (year-to-date)'),
 ('AFC', 'T228R5C1', 'annual 3,800 units ÷ 12 = COP 16,585,100 → within both',
  '3,800-unit annual cap (COP 199,021,200), tracked year-to-date with no monthly one-twelfth limit: 12 × 2,000,000 = 24,000,000 → within both'),
 ('AFC', 'P602', 'the lower of 30% of labour income or 3,800 tax units.',
  'the lower of 30% of labour income or 3,800 tax units. The 3,800-unit limit is annual ("por año", Decree 1625 of 2016 art. 1.2.1.22.43) and is tracked year-to-date per employee, with no monthly one-twelfth limit: the Consejo de Estado (Sección Cuarta, rad. 24047, 28 October 2021) held that arts. 126-1 and 126-4 set annual limits.'),
 ('A-1x', 'T228R6C1',None, '25% × (10,920,000 − 2,000,000) = 25% × 8,920,000 = 2,230,000. Within the 790-unit annual cap (year-to-date; 12 × 2,230,000 = 26,760,000)'),
 ('A-1x', 'T228R9C0', None, '— 1,340-unit annual cap (year-to-date)'),
 ('A-1x', 'T228R9C1', None, '12 × 4,230,000 = 50,760,000 ≤ 70,181,160 → within'),
 ('A-1x', 'T239R5C1', None, '25% × 23,425,000 = 5,856,250; 790-unit annual cap, year-to-date: at most 6 × 5,856,250 = 35,137,500 taken before July, 6,237,960 left → not capped. In August only 381,710 of the cap is left and from September the 25% exemption is nil'),
 ('A-1x', 'T239R5C2', None, '(5,856,250.00)'),
 ('A-1x', 'T239R7C0', None, '— 1,340-unit annual cap (year-to-date)'),
 ('A-1x', 'T239R7C1', None, 'at most 7 × 5,856,250 = 40,993,750 ≤ 70,181,160 → within'),
 ('A-1x', 'T239R8C1', None, '23,425,000 − 5,856,250'),
 ('A-1x', 'T239R8C2', None, '17,568,750.00'),
 ('A-1x', 'T239R9C1', None, '17,568,750 ÷ 52,374'),
 ('A-1x', 'T239R9C2', None, uv(G239)),
 ('A-1x', 'T239R10C1', None, '> 150 and ≤ 360 → marginal 28%'),
 ('A-1x', 'T239R11C1', None, f'({uv(G239)} − 150) × 28% + 10 = {q4((q4(G239 / U) - 150) * D("0.28")):.4f} + 10 = {q4(q4((q4(G239 / U) - 150) * D("0.28")) + 10):.4f}'),
 ('A-1x', 'T239R12C1', None, f'{q4(q4((q4(G239 / U) - 150) * D("0.28")) + 10):.4f} × 52,374'),
 ('A-1x', 'T239R12C2', None, f'{W239:,.2f}'),
 ('A-1x', 'T240R5C1', None, f'({W239:,.2f})'),
 ('A-1x', 'T240R6C1', None, f'{D(25000000) - 1575000 - W239:,.2f}'),
 # A-2
 ('A-2', 'T86R4C2', None, 'No withholding. Severance savings and their interest are never subject to withholding (Law 100 of 1993 art. 135 par. 3; Decree 1625 of 2016 art. 1.2.4.1.11; DIAN Oficios 8899 of 2015 and 4358 of 2019); the rule does not distinguish by residence, so the art. 408 flat 20% does not apply to them. Because this income was not withheld under arts. 407–411, the non-resident does not meet the non-filing condition of Tax Code art. 592 num. 2 and settles the tax in their own return (art. 26 depuration, art. 247 rate). Configurable option: a client that wants the conservative position may withhold the art. 408 20% (off by default)'),
 ('A-2', 'T150R3C2', None, 'No withholding (Law 100 of 1993 art. 135 par. 3; Decree 1625 of 2016 art. 1.2.4.1.11; DIAN Oficios 8899 of 2015 and 4358 of 2019): the rule does not distinguish by residence, so the art. 408 flat 20% does not apply. The non-resident declares the income in their own return (Tax Code arts. 26, 247 and 592 num. 2), where the art. 206 num. 4 exemption is available (an interpretation: art. 206 does not require residence). The 20% is kept only as a configurable conservative option, off by default'),
 ('A-2', 'P722', 'DIAN Oficio 28380 of 2019;', 'DIAN Oficio 28380 of 2019; Law 100 of 1993 art. 135 par. 3; Decree 1625 of 2016 art. 1.2.4.1.11; DIAN Oficios 8899 of 2015 and 4358 of 2019; Tax Code art. 247;'),
 # Res. 2708 (indices of python-docx; the lote B numbering is one higher)
 ('R2708', 'T11R3C2', ' Circular 101 of 2025 §5 (revoked by Resolution 2708 of 2026) stressed that the substitution is not a discretionary employer choice: it is limited to objective, demonstrable causes such as a continuous production process, imperative public interest, humanitarian or seasonal conditions, or shift patterns that make a collective rest day unworkable', ''),
 ('R2708', 'T33R3C1', 'Circular 101 of 2025 §2.3–2.4 (revoked by Resolution 2708 of 2026) confirmed expressly that piece-rate workers, including in agriculture, are not excluded from minimum-wage or maximum-hours rules',
  'Labour Code art. 132 num. 1 allows pay by time, by output, piece-rate or task "pero siempre respetando el salario mínimo legal", and art. 162 does not exclude piece-rate workers, including in agriculture, from the maximum hours'),
 ('R2708', 'T34R3C2', None, 'Law 2101 of 2021 art. 3 (Labour Code art. 161): 44-hour week to 14 July 2026; divisor 44 × 5 = 220 (30 days ÷ 6 working days), derived'),
 ('R2708', 'T34R4C2', None, 'Labour Code art. 161 (Law 2466 of 2025 art. 11; Law 2101 of 2021 art. 3): 42-hour week from 15 July 2026; divisor 42 × 5 = 210 (30 days ÷ 6 working days), derived'),
 ('R2708', 'T51R7C1', None, 'Included — Labour Code art. 132 num. 1 (piece-rate pay must respect the minimum wage) and art. 162 (not among the exceptions to the maximum hours)'),
 ('R2708', 'P415', 'Circular 101 of 2025 (revoked by Resolution 2708 of 2026) derived the resulting maxima of ordinary plus overtime hours: 56 hours per week to 14 July 2026 and 54 hours per week from 15 July 2026.',
  'The resulting maxima of ordinary plus overtime hours follow from the statute (Labour Code art. 161 plus the 12 weekly overtime hours of art. 22): 56 hours per week to 14 July 2026 (44 + 12) and 54 hours per week from 15 July 2026 (42 + 12).'),
]
CCG_DEL = [('R2708', 'P432')]   # paragrafo da Circular 101 sem objeto (lote B: 'P433 pode sair')
CCG_ROW = ('VC', 1, 6, ['1.6 (DRAFT)', '2 November 2026', L.AUTHOR,
  'Validation corrections, round 5 (DRAFT): the 790-unit and 1,340-unit caps are annual and tracked year-to-date (worked examples recalculated with the premise written: retention bonus, performance bonus, all-inclusive salary), and so is the shared 3,800-unit cap of voluntary pension funds and long-term savings accounts; severance savings and their interest are not withheld for any employee (non-resident matrix); citations of the revoked Circular 101 of 2025 replaced by the statute (rest-day substitution, hourly divisors, piece-rate workers, overtime maxima).'])


def run_ccg(src, dst):
    d = L.Docx(src)
    plan = []
    for sid, loc, old, new in CCG:
        gi = d.para_of(loc, old)
        plan.append((gi, sid, loc, old, new))
    for sid, loc in CCG_DEL:
        plan.append((d.para_of(loc), sid, loc, 'DELETE', None))
    # apply bottom-up so that earlier paragraph indices stay valid (row insert goes last: it is above all edits? no -> handled)
    for gi, sid, loc, old, new in sorted(plan, key=lambda t: -t[0]):
        if old == 'DELETE':
            before = d.delete_para(gi); LOG.append(dict(art='CCG', where=loc + ' (parágrafo apagado)', before=before, after='', src=SRC[sid])); continue
        o = d.text(gi) if old is None else old
        before, after = d.replace(gi, o, new)
        LOG.append(dict(art='CCG', where=loc, before=before, after=after, src=SRC[sid]))
    sid, t, r, texts = CCG_ROW
    d.insert_row_after(t, r, texts)
    LOG.append(dict(art='CCG', where=f'T{t}R{r + 1} (linha nova, Version Control)', before='', after=' | '.join(texts), src=SRC[sid]))
    d.save(dst)


# ------------------------------------------------------------------ 4. SIR (texto para colar)
def run_sir(src, dst):
    t = open(src, encoding='utf-8').read()
    old_block = 'more than 430 validation rules (R = rejection, N = notification), Anexo Técnico NE v1.0 §6'
    new_block = ('Anexo Técnico NE v1.0 §6 lists 519 validation rules: 437 for the payroll documents (NominaIndividual 198 = 189 R + 9 N; '
                 'NominaIndividualDeAjuste 239 = 219 R + 20 N), 56 for the digital signature (54 R; 2 without a flag), 23 for the connection '
                 '(21 R + 2 N) and 3 general rules (R). R = rejection, N = notification.')
    assert t.count(old_block) == 1 and t.count('\nv1.2\n') == 1
    t = t.replace('# CO-SIR-001 v1.2: texto final para colar no Google Doc',
                  '# CO-SIR-001 v1.3 DRAFT-R5: texto para colar no Google Doc (rodada 5, 2026-11-02, NÃO emitido)\n\n'
                  '> DRAFT da rodada 5, gerado por `revisao/rodada5/scripts/apply_r5.py` a partir de `final/CO-SIR-001-v1.2-texto-final.md`. '
                  'Mudanças marcadas com **[R5]** fora dos blocos de código (o que vai para o Doc é só o conteúdo dos blocos).', 1)
    t = t.replace('Campo **Version** (hoje `v1.1`):\n```\nv1.2\n```', 'Campo **Version** (hoje `v1.2`) **[R5] antes: `v1.2`**:\n```\nv1.3\n```', 1)
    t = t.replace('Linha NE, contagem de regras (âncora: `433` / `406` / `27`):\n```\n' + old_block,
                  'Linha NE, contagem de regras (âncora: `430`) **[R5] S-07 — antes: "' + old_block + '"; fonte: Anexo Técnico NE v1.0 §6, pp. 182–232 (contagem do lote C, dois métodos)**:\n```\n' + new_block, 1)
    assert new_block in t and '\nv1.3\n' in t
    open(dst, 'w', encoding='utf-8', newline='\n').write(t)
    LOG.append(dict(art='SIR', where='Section 4, linha NE (texto l. 35 do final)', before=old_block, after=new_block, src=SRC['S-07']))
    LOG.append(dict(art='SIR', where='Document control, Version', before='v1.2', after='v1.3', src=SRC['VC']))


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    outs = []
    for art, src, dst, edits in XLSX:
        e2 = [(sh, ref, op, SRC[sid], sf) for sh, ref, op, sid, sf in edits]
        refs = [(sh, ref) for sh, ref, *_ in edits]; assert len(refs) == len(set(refs)), art + ' duplicate cell'
        L.xlsx_apply(os.path.join(FIN, src), os.path.join(OUT, dst), e2, LOG, art)
        outs.append((art, src, dst, len(edits)))
    run_ccg(os.path.join(FIN, 'CO-CCG-001-v1.5.docx'), os.path.join(OUT, 'CO-CCG-001-v1.6-DRAFT-R5.docx'))
    outs.append(('CCG', 'CO-CCG-001-v1.5.docx', 'CO-CCG-001-v1.6-DRAFT-R5.docx', len(CCG) + len(CCG_DEL) + 1))
    run_sir(os.path.join(FIN, 'CO-SIR-001-v1.2-texto-final.md'), os.path.join(OUT, 'CO-SIR-001-v1.3-DRAFT-R5-texto.md'))
    outs.append(('SIR', 'CO-SIR-001-v1.2-texto-final.md', 'CO-SIR-001-v1.3-DRAFT-R5-texto.md', 2))
    for f, h in md5f.items():
        assert L.md5(FP(f)) == h, 'final alterado: ' + f
    json.dump(LOG, open(os.path.join(OUT, 'apply_r5_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(OUT, 'MD5-DRAFTS-R5.txt'), 'w', encoding='utf-8') as fh:
        fh.write('# MD5 dos DRAFT-R5 (rodada 5, 2026-11-02), gerado por revisao/rodada5/scripts/apply_r5.py; final de partida -> DRAFT\n')
        for art, src, dst, n in outs:
            fh.write(f'{L.md5(os.path.join(OUT, dst))}  {dst}   <- {md5f[src]}  final/{src}\n')
    # mudancas-RODADA5.md
    def cell(s):
        s = (s or '').replace('|', '\\|').replace('\n', ' ⏎ ')
        return s
    M = ['# Mudanças da rodada 5 (DRAFT-R5), Colômbia — 2026-11-02', '',
         'Ligado a [[CONFERENCIA]], [[TABELA-RODADA5]] e [[Colombia]]. Gerado por `revisao/rodada5/scripts/apply_r5.py` (log em `apply_r5_log.json`). '
         'Finais em `final/` só lidos (md5 conferido antes e depois). Research CO não está em produção: versão nova, sem ticket ao Development.', '',
         '| Artefato | Final de partida | DRAFT-R5 | Mudanças (células / parágrafos) |', '|---|---|---|---|']
    cnt = {}
    for x in LOG: cnt[x['art']] = cnt.get(x['art'], 0) + 1
    for art, src, dst, n in outs: M.append(f'| {art} | `final/{src}` | `{dst}` | {cnt.get(art, 0)} |')
    M += ['', '## Célula / parágrafo | antes | depois | fonte', '']
    for art in [o[0] for o in outs]:
        M += [f'### {art}', '', '| Onde | Antes | Depois | Fonte |', '|---|---|---|---|']
        for x in LOG:
            if x['art'] == art: M.append(f"| {cell(x['where'])} | {cell(x['before'])} | {cell(x['after'])} | {cell(x['src'])} |")
        M.append('')
    open(os.path.join(OUT, 'mudancas-RODADA5.md'), 'w', encoding='utf-8').write('\n'.join(M) + '\n')
    for art, src, dst, n in outs: print(f'{art:8} {dst}: {cnt.get(art, 0)} mudanças')
    print('log', len(LOG))
