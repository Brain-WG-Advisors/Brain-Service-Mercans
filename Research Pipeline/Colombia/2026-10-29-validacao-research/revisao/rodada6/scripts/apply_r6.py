# -*- coding: utf-8 -*-
"""Rodada 6 (2026-11-02): ajustes so de texto aprovados pelo usuario ("Pode aplicar os ajustes de texto e o SIR v1.4").
Gera os DRAFT-R6 em revisao/rodada6/ a partir dos finais em vigor (CCG v1.6, WTC v1.8, DD v1.5, spec 004 v1.2), com o
mesmo metodo da rodada 5 (r5lib: celula alterada em FFDDEBF7; docx com alteracao controlada). Nenhum valor muda.
Fontes: pesquisa-2026-11-02-r6/TABELA-RODADA6.md (cada fonte reaberta por mim; trechos la).
Uso: python -I revisao/rodada6/scripts/apply_r6.py
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE); os.chdir(VAL); sys.stdout.reconfigure(encoding='utf-8')
import r5lib as L

FIN = 'final/_historico/2026-11-02-r5/'  # finals in force before round 6 (moved there by release_r6.py)
OUT = 'revisao/rodada6/'
ISSUE = '2026-11-02'; ISSUE_SERIAL = '46328'; AUTHOR = 'Wallisson Gomes'
REL = ' Released 2026-11-02 — approved by Wallisson Gomes.'
TP = 'Statutory validation, third pass (text only, no value changes): '
WT = 'Wage Type Catalogue'

# ------------------------------------------------------------------ WTC v1.9
Y_OLD = '(AuxilioNS, NIE142)'; Y_NEW = '(AuxilioNS, NIE142, where non-salary under the pact; otherwise AuxilioS, NIE141)'
Y2_OLD = 'AuxilioNS (NIE142)'; Y2_NEW = 'AuxilioNS (NIE142) where non-salary under the pact, otherwise AuxilioS (NIE141)'
AB_OLD = ("Default 'Non-Salary - pacted': a cash car / fuel / maintenance allowance paid under the contract is salary "
          "(CST art. 127) unless a written CST art. 128 pact excludes it, and then it is inside the Ley 1393 40% test.")
AB_NEW = ("Default 'Non-Salary - pacted'. The test is the purpose of the payment, not its name or a pact (Corte Suprema de "
          "Justicia SL5159-2018): a payment that remunerates the service is salary (CST art. 127) whatever the pact says; a "
          "benefit that does not remunerate the service and is excluded by a written CST art. 128 pact stays 'pacted', "
          "inside the Ley 1393 40% test.")
VAC_NEW = ("Statutory-benefit base and social-security contribution base = No: cash compensation of vacation is not salary "
           "but a kind of indemnity (Corte Suprema de Justicia SL467-2019; Consejo de Estado, Seccion Cuarta, SU 25185 of "
           "2021, rule 1; CST arts. 189, 253, 306). Payroll levies = Yes: it is paid rest ('descanso remunerado') under Ley 21 "
           "de 1982 art. 17 (Consejo de Estado, Sala de Consulta, concepto 2027 of 2010; Consejo de Estado, Seccion Cuarta, "
           "exp. 27226 of 11 May 2023; UGPP ABC Empleadores 2025 p. 7).")
D123_OLD = ("UGPP ABC Empleadores 2025 tells employers to take incapacity and maternity values into account for payroll "
            "levies; the Consejo de Estado ruling is followed here.")
D123_NEW = ("UGPP ABC Empleadores 2025 (p. 7) tells employers to take incapacity and maternity values into account for "
            "payroll levies, while its own table on p. 6 lists these events only for social security; the guide has no "
            "normative force and the Consejo de Estado ruling is followed here.")
D330_NEW = ("Payroll levies = No: the leave is paid by the EPS, not by the employer, so no SENA / ICBF / CCF levies are due "
            "on it (Superintendencia del Subsidio Familiar, Concepto 2-2018-083606). The same applies to paternity, shared "
            "and flexible parental and childcare leave (rows 331-333; childcare leave is reported in the PILA as an IGE "
            "event, Resolucion MSPS 467 de 2025); in flexible parental leave the hours actually worked are ordinary salary. "
            "Health and pension contributions continue.")
C16_SUBS = [
    ("(1) The rate for the employer's first two sick days - Decreto 780 de 2016 art. 3.2.1.10 allocates the days but not "
     "the rate; Concepto MinSalud 202311602174531 of 20 October 2023 applies CST art. 227 (two thirds); Mercans default "
     "66.67%, configurable.",
     "(1) The rate for the employer's first two sick days - closed: two thirds of salary (CST art. 227, applied to days "
     "1-2 by Concepto MinSalud 202311602174531 of 20 October 2023; Decreto 780 de 2016 art. 3.2.1.10 allocates the days "
     "but not the rate); Mercans default 66.67%, configurable for a client that pays 100%."),
    ("(2) The minimum-wage floor on incapacity payments - Corte Constitucional C-543 de 2007 (the sickness benefit may "
     "not fall below the minimum legal wage); Mercans default applies the floor, configurable.",
     "(2) The minimum-wage floor on incapacity payments - closed: Corte Constitucional C-543 de 2007 (the sickness "
     "benefit may not fall below the minimum legal wage); the floor is applied, in proportion to the days."),
]
WTC_EDITS = []
for r in list(range(230, 238)) + [253, 254]:
    WTC_EDITS.append((WT, f'Y{r}', ('sub', [(Y_OLD, Y_NEW)]), 'C-11', None))
for r in (348, 349, 350):
    WTC_EDITS.append((WT, f'Y{r}', ('sub', [(Y2_OLD, Y2_NEW)]), 'C-11', None))
for r in list(range(201, 207)) + [214, 215, 216]:
    WTC_EDITS.append((WT, f'AB{r}', ('sub', [(AB_OLD, AB_NEW)]), 'C-14', None))
for r in (156, 324):
    WTC_EDITS.append((WT, f'D{r}', ('set', VAC_NEW), 'C-13', None))
WTC_EDITS += [
    (WT, 'D123', ('sub', [(D123_OLD, D123_NEW)]), 'B-6a', None),
    (WT, 'D330', ('set', D330_NEW), 'B-6b', 'D332'),
    ('Employer Sick Pay', 'A38', ('sub', [('falls below one SMMLV (1,750,905), market practice and settled',
                                           'falls below one SMMLV (1,750,905), the payment is topped up to one')]), 'B-7', None),
    ('Employer Sick Pay', 'A39', ('sub', [('administrative doctrine top the payment up to one minimum wage. Corte Constitucional C-543 de 2007',
                                           'minimum wage, in proportion to the days: Corte Constitucional C-543 de 2007')]), 'B-7', None),
    ('Employer Sick Pay', 'A41', ('sub', [('the floor, configurable.', 'the floor.')]), 'B-7', None),
    ('Global WTC Coverage', 'C16', ('sub', C16_SUBS), 'B-7', None),
    ('Version Control', 'B21', ('set', '1.9'), 'R6', 'B20'),
    ('Version Control', 'C21', ('num', ISSUE_SERIAL), 'R6', 'C20'),
    ('Version Control', 'D21', ('set', TP + "nomina electronica element of the pacted rows 230-237, 253-254 and 348-350 conditional on the non-salary pact (otherwise AuxilioS, NIE141); car allowance notes (rows 201-206 and 214-216) on the purpose of the payment (CSJ SL5159-2018); vacation compensated in cash (rows 156 and 324) with its sources; payroll levies on incapacity (row 123) and on maternity, paternity, parental and childcare leave (row 330); Employer Sick Pay minimum-wage floor and Global WTC Coverage open items 1 and 2 closed." + REL), 'R6', 'D20'),
    ('Version Control', 'E21', ('set', 'Approved'), 'R6', 'E20'),
    ('Version Control', 'F21', ('set', AUTHOR), 'R6', 'F20'),
]

# ------------------------------------------------------------------ DD v1.6
DD_EDITS = [
    ('ID Information', 'H7', ('sub', [('and 98 (CATS: Nequi, Daviplata); left empty',
                                       'and 98 (CATS: Nequi, Daviplata), and 46 (Transferencia Debito Interbancario) where a client adds it to the mapper; left empty')]), 'C-12', None),
    ('Country Option Mappers', 'G95', ('sub', [('the values below are those used in payroll.',
                                                'the values below are those used in payroll. A client that uses another code of table 5.3.3.2 adds it as a row; 46 (Transferencia Debito Interbancario) is account-based like 47, so the bank attributes are populated.')]), 'C-12', None),
    ('Version Control', 'B19', ('set', '1.6'), 'R6', 'B18'),
    ('Version Control', 'C19', ('num', ISSUE_SERIAL), 'R6', 'C18'),
    ('Version Control', 'D19', ('set', TP + "payment method 46 (Transferencia Debito Interbancario) treated as account-based where a client adds it to the Payment Method mapper (ID Information row 7; Country Option Mappers G95)." + REL), 'R6', 'D18'),
    ('Version Control', 'E19', ('set', 'Approved'), 'R6', 'E18'),
    ('Version Control', 'F19', ('set', AUTHOR), 'R6', 'F18'),
]

# ------------------------------------------------------------------ spec 004 v1.3
S4_SUBS = [('(Ley 100 de 1993 art. 135 par. 3; DUR', '(Ley 100 de 1993 art. 135 par. 3, extended to every payer by Corte Constitucional C-397 de 1994; DUR'),
           ("in the employee's own return (an interpretation).",
            "in the employee's own return (DIAN Concepto 577 de 2020: a non-resident who must file applies ET art. 26 together with arts. 178 and 235-2, which keeps the art. 206 exemptions).")]
S4_EDITS = [
    ('Report Matrix', 'A34', ('sub', S4_SUBS), 'A-2', None),
    ('Example Analysis', 'D34', ('sub', S4_SUBS), 'A-2', None),
    ('Report Matrix', 'B19', ('set', 'v1.3'), 'R6', None),
    ('Version Control', 'B16', ('set', '1.3'), 'R6', 'B15'),
    ('Version Control', 'C16', ('set', ISSUE), 'R6', 'C15'),
    ('Version Control', 'D16', ('set', TP + "legal basis of the non-withholding of severance savings and their interest for non-residents (Corte Constitucional C-397 de 1994; DIAN Concepto 577 de 2020) in the Report Matrix and the Example Analysis." + REL), 'R6', 'D15'),
    ('Version Control', 'E16', ('set', 'Approved'), 'R6', 'E15'),
    ('Version Control', 'F16', ('set', AUTHOR), 'R6', 'F15'),
]

# ------------------------------------------------------------------ CCG v1.7 (tracked)
C397 = ('(Law 100 of 1993 art. 135 par. 3; Decree', '(Law 100 of 1993 art. 135 par. 3, extended to every payer by Constitutional Court C-397 of 1994; Decree')
CCG_OPS = [
    ('T150R3C2', C397[0], C397[1], 'A-2'),
    ('T150R3C2', '(an interpretation: art. 206 does not require residence)',
     '(DIAN Concepto 577 of 2020: a non-resident who must file applies Tax Code art. 26 together with arts. 178 and 235-2, which keeps the art. 206 exemptions)', 'A-2'),
    ('T86R4C2', C397[0], C397[1], 'A-2'),
    ('P297', 'by the Council of State (Section Two, Subsection A) in annulment proceeding 11001-03-25-000-2026-00004-00 by order of 12 February 2026',
     'by order of the reporting councillor of the Council of State, Section Two, of 12 February 2026, in annulment proceeding 11001-03-25-000-2026-00004-00', 'B-9'),
    ('P297', 'On 9 July 2026 the Council of State revoked', 'On 9 July 2026 the Council of State, Section Two, deciding the recurso de súplica, revoked', 'B-9'),
    ('P297', 'with Decree 0159 of 2026 spent.', 'with Decree 0159 of 2026 left without effect by ordinal 3 of the same order.', 'B-9'),
    ('P905', 'market practice and settled administrative doctrine top the payment up to one minimum wage. Mercans default: apply the floor, configurable. Corte',
     'the payment is topped up to one minimum wage, in proportion to the days of incapacity. Corte', 'B-7'),
    ('P905', 'vigente").', 'vigente"). Mercans applies the floor.', 'B-7'),
    ('P7', 'Version 1.6', 'Version 1.7', 'R6'),
    ('T0R7C1', 'CO-CCG-001 v1.6', 'CO-CCG-001 v1.7', 'R6'),
]
CCG_ROW = ['1.7', '2 November 2026', AUTHOR,
           TP + 'non-withholding of severance savings and their interest cites Constitutional Court C-397 of 1994 and, for the non-resident return, DIAN Concepto 577 of 2020 (non-resident matrix); the 2026 minimum-wage note states who issued each order and that Decree 0159 of 2026 was left without effect; the minimum-wage floor on incapacity rests on Constitutional Court C-543 of 2007.' + REL]


def run():
    log = []
    L.xlsx_apply(FIN + 'CO-WTC-001-v1.8.xlsx', OUT + 'CO-WTC-001-v1.9-DRAFT-R6.xlsx', WTC_EDITS, log, 'WTC')
    L.xlsx_apply(FIN + 'CO-DD-001-v1.5.xlsx', OUT + 'CO-DD-001-v1.6-DRAFT-R6.xlsx', DD_EDITS, log, 'DD')
    L.xlsx_apply(FIN + 'specs/CO-DIAN-004-Formulario220-Spec.xlsx', OUT + 'CO-DIAN-004-Formulario220-Spec-v1.3-DRAFT-R6.xlsx', S4_EDITS, log, 'F220')
    d = L.Docx(FIN + 'CO-CCG-001-v1.6.docx')
    targets = [(d.para_of(loc, old), loc, old, new, sid) for loc, old, new, sid in CCG_OPS]
    for gi, loc, old, new, sid in targets:
        before, after = d.replace(gi, old, new)
        log.append(dict(art='CCG', where=loc, before=before, after=after, src=sid))
    d.insert_row_after(1, 7, CCG_ROW)
    log.append(dict(art='CCG', where='T1 new row after R7', before='', after=' | '.join(CCG_ROW), src='R6'))
    fx = d.data['word/footer1.xml'].decode('utf-8')
    assert fx.count('CO-CCG-001 v1.6 |') == 1
    d.data['word/footer1.xml'] = fx.replace('CO-CCG-001 v1.6 |', 'CO-CCG-001 v1.7 |').encode('utf-8')
    log.append(dict(art='CCG', where='word/footer1.xml', before='CO-CCG-001 v1.6 |', after='CO-CCG-001 v1.7 |', src='R6'))
    d.save(OUT + 'CO-CCG-001-v1.7-DRAFT-R6.docx')
    json.dump(log, open(OUT + 'apply_r6_log.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(OUT + 'MD5-DRAFTS-R6.txt', 'w', encoding='utf-8') as f:
        for n in sorted(os.listdir(OUT)):
            if 'DRAFT-R6' in n: f.write(f'{L.md5(OUT + n)}  {n}\n')
    print('edits', len(log))


if __name__ == '__main__':
    run()
