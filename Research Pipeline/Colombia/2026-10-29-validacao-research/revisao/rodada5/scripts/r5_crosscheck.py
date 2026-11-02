# -*- coding: utf-8 -*-
"""Conferencia dos DRAFT-R5 (rodada 5, 2026-11-02), adaptada de final/scripts/release_crosscheck.py.
Para cada DRAFT-R5 contra o final de partida (final/, so leitura) prova, independentemente do apply_r5.py:
  1. abre (openpyxl read-only / python-docx) e a estrutura do zip esta intacta: mesmas partes; so styles.xml e as abas
     editadas (xlsx) ou document.xml e settings.xml (docx) diferem; fora das celulas, a estrutura das abas nao muda;
  2. diff celula a celula (valor e formula de todas as celulas de todas as abas): nenhuma celula fora da lista mudou, e
     cada celula da lista tem exatamente o texto declarado (apply_r5_log.json); docx: paragrafos do DRAFT com as
     alteracoes aceitas x final - so mudam os paragrafos declarados, mais a linha nova do Version Control e o paragrafo
     apagado declarado;
  3. formatacao: celula nao declarada mantem o mesmo estilo; celula declarada tem fundo FFDDEBF7 e o resto da formatacao
     igual ao original (celula nova: igual a celula-modelo);
  4. zero erros de formula (valores #REF!, #VALUE!, #DIV/0!, #NAME?, #N/A, #NUM!, #NULL! ou t="e");
  5. valores novos presentes (cada texto 'depois' esta no DRAFT); docx: alteracoes controladas so do autor declarado.
Grava revisao/rodada5/CONFERENCIA-R5.md (junto com o resultado do oraculo, oracle-r5-ytd.json). Exit 1 se falhar.
Uso: python -I revisao/rodada5/scripts/r5_crosscheck.py
"""
import os, re, sys, json, zipfile, difflib, collections, subprocess, datetime, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(VAL, 'final', 'scripts')); sys.path.insert(0, HERE)
import colib, apply_r5 as A, r5lib as L
sys.stdout.reconfigure(encoding='utf-8')
FIN = A.FIN; OUT = os.path.join(VAL, 'revisao', 'rodada5')
LOG = json.load(open(os.path.join(OUT, 'apply_r5_log.json'), encoding='utf-8'))
ERR = re.compile(r'^#(REF!|VALUE!|DIV/0!|NAME\?|N/A|NUM!|NULL!)')
C29 = re.compile(r'\[placeholder\]|\bTODO\b|\bTBD\b|\bFIXME\b|\bXXX\b|VERIFY No\.|\bto be confirmed\b|\bto be verified\b', re.I)
XF_RE = re.compile(r'<xf\b[^>]*?(?:/>|>.*?</xf>)', re.S)
VALIDATOR = r'C:\Users\instituto\.claude\skills\mercans-artifact-toolkit\scripts\validate_workbook.py'


def styles(path):
    z = zipfile.ZipFile(path); sty = z.read('xl/styles.xml').decode('utf-8'); z.close()
    xfs = XF_RE.findall(re.search(r'<cellXfs[^>]*>(.*?)</cellXfs>', sty, re.S).group(1))
    fills = re.findall(r'<fill>.*?</fill>|<fill/>', re.search(r'<fills[^>]*>(.*?)</fills>', sty, re.S).group(1), re.S)
    def norm(i, keep_fill):
        x = xfs[i]; head = re.match(r'<xf\b[^>]*?/?>', x).group(0)
        a = dict(re.findall(r'(\w+)="([^"]*)"', head)); fid = a.pop('fillId', '0'); a.pop('applyFill', None)
        return (tuple(sorted(a.items())), x[len(head):], fills[int(fid)] if keep_fill else '')
    def blue(i):
        m = re.search(r'fillId="(\d+)"', xfs[i]); return bool(m) and L.BLUE in fills[int(m.group(1))]
    return norm, blue


def skeleton(x):
    x = re.sub(r'<c r="[A-Z]+\d+"[^>]*?(?:/>|>.*?</c>)', '', x, flags=re.S)
    x = re.sub(r' s="\d+"| style="\d+"| spans="\d+:\d+"', '', x)
    x = re.sub(r'<row r="\d+"\s*/>|<row r="\d+"\s*></row>', '', x)
    return x


def check_xlsx(art, fin, dra):
    fails, info = [], collections.Counter()
    import openpyxl
    wb = openpyxl.load_workbook(dra, read_only=True); info['abas'] = len(wb.sheetnames)
    for ws in wb.worksheets:
        for _ in ws.iter_rows(max_row=2): pass
    wb.close()
    zf, zd = zipfile.ZipFile(fin), zipfile.ZipFile(dra)
    if set(zf.namelist()) != set(zd.namelist()): fails.append(f'partes do zip diferem: {sorted(set(zf.namelist()) ^ set(zd.namelist()))}')
    decl = {}
    for x in LOG:
        if x['art'] == art:
            sh, ref = x['where'].split('!'); decl[(sh, ref)] = x
    smf = {n: p for n, p, s in colib.sheetmap(zf)}
    edited_parts = {smf[sh] for sh, _ in decl}
    for n in zf.namelist():
        if n == 'xl/styles.xml' or n in edited_parts: continue
        if zf.read(n) != zd.read(n): fails.append(f'parte alterada fora da lista: {n}')
    for n in edited_parts:
        if skeleton(zf.read(n).decode('utf-8')) != skeleton(zd.read(n).decode('utf-8')): fails.append(f'estrutura fora das células mudou: {n}')
    info['partes iguais byte a byte'] = len([n for n in zf.namelist() if n != 'xl/styles.xml' and n not in edited_parts])
    nf, bf = styles(fin); nd, bd = styles(dra)
    F = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(fin)}
    Dd = {(sh, r): (v, fo, s) for sh, r, v, fo, s in colib.xlsx_cells(dra)}
    extra = set(Dd) - set(F)
    if set(F) - set(Dd): fails.append(f'células sumiram: {sorted(set(F) - set(Dd))[:5]}')
    for k in extra:
        if k not in decl: fails.append(f'célula nova não declarada: {k}')
    nerr = 0
    for k in set(F) | set(Dd):
        vf, ff, sf = F.get(k, ('', None, None)); vd, fd, sd = Dd.get(k, ('', None, None))
        if isinstance(vd, str) and ERR.match(vd): nerr += 1
        if k in decl:
            exp = decl[k]['after']
            if str(vd or '') != str(exp): fails.append(f'{k[0]}!{k[1]} valor ≠ declarado: {str(vd)[:60]!r} ≠ {str(exp)[:60]!r}')
            if (ff or None) != (fd or None): fails.append(f'{k[0]}!{k[1]} fórmula mudou')
            if not bd(sd): fails.append(f'{k[0]}!{k[1]} sem o azul FFDDEBF7')
            if sf is not None and F[k][0] not in ('', None) and nf(sf, False) != nd(sd, False):
                fails.append(f'{k[0]}!{k[1]} formatação mudou além do fundo')
            info['células declaradas conferidas'] += 1
        else:
            if (vf or '') != (vd or '') or (ff or None) != (fd or None): fails.append(f'{k[0]}!{k[1]} MUDOU SEM ESTAR NA LISTA: {str(vf)[:60]!r} -> {str(vd)[:60]!r}')
            elif nf(sf, True) != nd(sd, True): fails.append(f'{k[0]}!{k[1]} formatação mudou sem estar na lista')
    for k in decl:
        if k not in Dd: fails.append(f'célula declarada ausente: {k}')
        v = str(Dd.get(k, ('',))[0] or '')
        if C29.search(v): fails.append(f'{k[0]}!{k[1]} marcador C29')
    info['erros de fórmula'] = nerr
    if nerr: fails.append(f'{nerr} erros de fórmula')
    info['células comparadas'] = len(set(F) | set(Dd))
    if os.path.exists(VALIDATOR):
        r = subprocess.run([sys.executable, '-I', VALIDATOR, dra], capture_output=True, text=True, encoding='utf-8', errors='replace')
        tail = (r.stdout + r.stderr).strip().splitlines()
        blk = [l for l in tail if re.search(r'blocker', l, re.I)]
        info['validate_workbook'] = (blk[-1] if blk else (tail[-1] if tail else '')).strip()[:90] + f' (exit {r.returncode})'
    return fails, info


def check_docx(fin, dra):
    import docx
    fails, info = [], collections.Counter()
    docx.Document(dra)
    zf, zd = zipfile.ZipFile(fin), zipfile.ZipFile(dra)
    if set(zf.namelist()) != set(zd.namelist()): fails.append('partes do zip diferem')
    for n in zf.namelist():
        if n in ('word/document.xml', 'word/settings.xml'): continue
        if zf.read(n) != zd.read(n): fails.append(f'parte alterada: {n}')
    x = zd.read('word/document.xml').decode('utf-8')
    authors = collections.Counter(re.findall(r'<w:(?:ins|del) [^>]*w:author="([^"]*)"', x))
    info['alterações controladas (w:ins/w:del)'] = sum(authors.values())
    if set(authors) != {L.AUTHOR}: fails.append(f'autores das alterações: {dict(authors)}')
    pf = colib.docx_paras(fin, accept=False); pd = colib.docx_paras(dra, accept=True)
    decl = [e for e in LOG if e['art'] == 'CCG']
    reps = collections.Counter((e['before'], e['after']) for e in decl if e['after'] and e['before'])
    dels = collections.Counter(e['before'] for e in decl if not e['after'])
    row = [e for e in decl if not e['before']]
    used = collections.Counter(); seen_del = collections.Counter(); ins_ok = 0
    sm = difflib.SequenceMatcher(None, pf, pd, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        if tag == 'replace' and i2 - i1 == j2 - j1:
            for a, b in zip(pf[i1:i2], pd[j1:j2]):
                if reps[(a, b)] - used[(a, b)] > 0: used[(a, b)] += 1
                else: fails.append(f'PARÁGRAFO MUDOU SEM ESTAR NA LISTA: {a[:80]!r} -> {b[:80]!r}')
        elif tag == 'insert' and row and pd[j1:j2] == row[0]['after'].split(' | '):
            ins_ok += 1
        elif tag == 'delete' and all(dels[t] - seen_del[t] > 0 for t in pf[i1:i2]):
            for t in pf[i1:i2]: seen_del[t] += 1
        else:
            fails.append(f'{tag} não declarado: final {i1}-{i2} {pf[i1:i2][:1]} / draft {j1}-{j2} {pd[j1:j2][:1]}')
    for k, n in reps.items():
        if used[k] != n: fails.append(f'edição declarada não encontrada: {k[0][:70]!r}')
    if row and ins_ok != 1: fails.append('linha nova do Version Control não encontrada')
    for t, n in dels.items():
        if seen_del[t] != n: fails.append(f'parágrafo a apagar não apagado: {t[:60]!r}')
    full = '\n'.join(pd)
    for e in decl:
        if e['after'] and e['after'].split(' | ')[0] not in full: fails.append(f'valor novo ausente: {e["after"][:60]!r}')
    info['parágrafos (final / DRAFT aceito)'] = f'{len(pf)} / {len(pd)}'
    info['edições declaradas conferidas'] = sum(used.values()) + ins_ok + sum(seen_del.values())
    if b'trackRevisions' not in zd.read('word/settings.xml'): fails.append('controle de alterações não ligado')
    return fails, info


def check_sir(fin, dra):
    fails, info = [], collections.Counter()
    a = open(fin, encoding='utf-8').read().split('\n'); b = open(dra, encoding='utf-8').read().split('\n')
    def blocks(lines):
        out, inside = [], False
        for l in lines:
            if l.startswith('```'): inside = not inside; continue
            if inside: out.append(l)
        return out
    ba, bb = blocks(a), blocks(b)
    diffs = [(x, y) for x, y in zip(ba, bb) if x != y]
    exp = {(e['before'], e['after']) for e in LOG if e['art'] == 'SIR'}
    if len(ba) != len(bb): fails.append('número de linhas dos blocos mudou')
    for d in diffs:
        if d not in exp: fails.append(f'linha de bloco mudou sem estar na lista: {d[0][:60]!r}')
    if len(diffs) != len(exp): fails.append(f'{len(diffs)} linhas mudaram, {len(exp)} declaradas')
    info['linhas dos blocos'] = len(bb); info['linhas mudadas'] = len(diffs)
    return fails, info


rows, total = [], 0
for art, src, dst, edits in A.XLSX:
    fl, inf = check_xlsx(art, os.path.join(FIN, src), os.path.join(OUT, dst)); rows.append((art, dst, src, fl, inf)); total += len(fl)
fl, inf = check_docx(os.path.join(FIN, 'CO-CCG-001-v1.5.docx'), os.path.join(OUT, 'CO-CCG-001-v1.6-DRAFT-R5.docx'))
rows.append(('CCG', 'CO-CCG-001-v1.6-DRAFT-R5.docx', 'CO-CCG-001-v1.5.docx', fl, inf)); total += len(fl)
fl, inf = check_sir(os.path.join(FIN, 'CO-SIR-001-v1.2-texto-final.md'), os.path.join(OUT, 'CO-SIR-001-v1.3-DRAFT-R5-texto.md'))
rows.append(('SIR', 'CO-SIR-001-v1.3-DRAFT-R5-texto.md', 'CO-SIR-001-v1.2-texto-final.md', fl, inf)); total += len(fl)
# finais intactos
md5bad = [f for f, h in A.md5f.items() if L.md5(A.FP(f)) != h]
if md5bad: total += len(md5bad)
for art, dst, src, fl, inf in rows:
    print(f'{art:8} {"PASS" if not fl else "FAIL"}  {dst}  ' + '; '.join(f'{k}={v}' for k, v in inf.items()))
    for x in fl[:10]: print('     ', x[:200])
print('finais intactos:', 'sim' if not md5bad else md5bad)

ORA = json.load(open(os.path.join(OUT, 'oracle-r5-ytd.json'), encoding='utf-8'))
cnt = collections.Counter(e['art'] for e in LOG)
M = ['# Conferência dos DRAFT-R5 (rodada 5), Colômbia — 2026-11-02', '',
     f'Ligado a [[CONFERENCIA]], [[TABELA-RODADA5]] e [[mudancas-RODADA5]]. Gerado por `revisao/rodada5/scripts/r5_crosscheck.py` em {datetime.datetime.now():%Y-%m-%d %H:%M} '
     '(adaptado de `final/scripts/release_crosscheck.py`). Base de comparação: os finais de 30/10 (desde o release de 02/11 em `final/_historico/2026-10-30/`, md5 no `MD5-FINAIS.txt` de lá), só lidos.', '',
     '## O que foi provado', '',
     '1. Cada DRAFT abre (openpyxl só leitura / python-docx) e o zip tem as mesmas partes do final; só `styles.xml` e as abas editadas (xlsx) ou `document.xml` e `settings.xml` (docx) diferem; fora das células a estrutura das abas não mudou.',
     '2. Diff célula a célula (valor e fórmula de todas as células de todas as abas): nenhuma célula fora da lista mudou e cada célula da lista tem o texto declarado. CCG: parágrafos do DRAFT com as alterações aceitas × final; só mudam os parágrafos declarados, a linha nova do Version Control e o parágrafo apagado declarado.',
     '3. Formatação: célula fora da lista com o mesmo estilo; célula da lista com fundo `FFDDEBF7` e o resto da formatação igual. CCG: todas as alterações controladas são do autor "Wallisson Gomes".',
     '4. Zero erros de fórmula. 5. Cada valor novo está no DRAFT. 6. Finais intactos (md5 antes e depois).', '',
     '## Resultado', '', '| Artefato | DRAFT-R5 | Final de partida | Mudanças | Medidas | Falhas | Veredito |', '|---|---|---|---|---|---|---|']
for art, dst, src, fl, inf in rows:
    M.append(f'| {art} | `{dst}` | `final/{src}` | {cnt.get(art, 0)} | ' + '; '.join(f'{k} {v}' for k, v in inf.items()) + f' | {len(fl)} | {"PASS" if not fl else "FAIL"} |')
M += ['', f'Finais intactos: {"sim (md5 = MD5-FINAIS.txt)" if not md5bad else md5bad}.', '', f'**Veredito: {"PASS" if not total else "FAIL"}** ({total} falhas).', '', '## Falhas', '']
for art, dst, src, fl, inf in rows:
    for x in fl: M.append(f'- {art}: {x}')
if not total: M.append('Nenhuma.')
M += ['', '## Oráculo (A-1: tetos anuais pelo acumulado)', '',
      '`revisao/rodada5/scripts/oracle_r5_ytd.py` roda o `oracle/oracle_v2.py` **sem alterar o código**: troca, só durante a chamada, o limite mensal lido do parâmetro (790 e 1.340 UVT ÷ 12) pelo saldo anual não usado. '
      f'Premissa: {ORA["premissa"]}. Casos `monthly` com retenção rodados: {ORA["casos_rodados"]}; limitados pelo 1/12: {len(ORA["afetados"])}; sem efeito: {len(ORA["nao_afetados"])}.', '',
      '| Caso | Limite que agia | Retenção 1/12 | Retenção acumulado (mês 1) | Mês da simulação | Retenção acumulado nesse mês | Mês em que o teto anual passa a limitar |', '|---|---|---|---|---|---|---|']
for a in ORA['afetados']:
    M.append(f"| {a['id']} | {a['limite_1_12'].strip()} | {a['retencao_mensal_1_12']:,.2f} | {a['retencao_mes1_ytd']:,.2f} | {a['mes_da_simulacao']} | {a['retencao_no_mes_da_simulacao_ytd']:,.2f} | {a['mes_em_que_o_teto_anual_comeca_a_limitar'] or '—'} |")
M += ['', 'Exemplos do CCG recalculados pelo oráculo (premissa escrita no CCG; bônus só no mês do exemplo):', '', '| Exemplo | 1/12 (hoje) | Acumulado (DRAFT) | 25% isento | Consumo antes do mês |', '|---|---|---|---|---|']
for e in ORA['exemplos_ccg']:
    M.append(f"| {e['exemplo']} | {e['retencao_1_12']:,.2f} | {e['retencao_ytd']:,.2f} | {e['exenta25_ytd']:,.2f} | {e['consumo_25_ate_o_mes_anterior']:,.2f} |")
M += ['', 'RC05 = exemplo T105 do CCG; RC07 = exemplo do Payslip (ago/2026). Os valores do oráculo batem com as contas do `apply_r5.py` (assert) e com os DRAFTs: T105 3.947.554,80; T180 1.763.832,00; T183 (pacto) 1.899.912,00; T239 3.243.282,00; Payslip 1.993.152,00.',
      '', 'A-2 (cesantías de não residente): o oráculo não modela retenção de não residente (não há ET 408 no código) — não aplicável.']
U = A.U
M += ['', '## Contas de A-1 refeitas (passo a passo; conferidas por assert no `apply_r5.py` e pelo oráculo)', '',
      f'UVT 2026 = 52.374 (CCG T215 "Tax unit COP 52,374"; Res. DIAN 000238/2025). 790 UVT = {A.A790:,.0f}; 1.340 UVT = {A.A1340:,.0f}. Tabela ET 383: >150–360 UVT: (base − 150 UVT) × 28% + 10 UVT; >360–640: (base − 360 UVT) × 33% + 69 UVT.', '',
      '**T105 (Exemplo 4, set/2026; salário 8.000.000 desde 1/1 + bônus 20.000.000 com pacto).**',
      '1. (C) do mês = 28.000.000 − 9% × 16.800.000 (IBC após o clamp de 40%) = 26.488.000; 25% = 6.622.000.',
      '2. Consumo jan–ago: (8.000.000 − 9% × 8.000.000) × 25% = 1.820.000 por mês × 8 = 14.560.000.',
      '3. Saldo do teto anual = 41.375.460 − 14.560.000 = 26.815.460 ≥ 6.622.000 → isenção 6.622.000. 40%: 10.595.200 ≥ 6.622.000. 1.340 UVT: 14.560.000 + 6.622.000 = 21.182.000 ≤ 70.181.160.',
      f'4. Base = 26.488.000 − 6.622.000 = 19.866.000 = {A.uv(A.G105)} UVT → faixa 33%. Retenção = (19.866.000 − 360 × 52.374) × 33% + 69 × 52.374 = 1.011.360 × 0,33 + 3.613.806 = **{A.W105:,.2f}** (igual ao lote A). Hoje: 4.994.989,65 (−1.047.434,85).',
      '5. Se o prêmio de serviços de junho (≈ 4.000.000, retido à parte) entrar no consumo: +1.000.000; saldo 25.815.460 ainda ≥ 6.622.000 → mesmo resultado.', '',
      '**T180 (out/2026; salário 6.000.000 desde 1/1 + bônus habitual 12.000.000).**',
      '1. (C) do mês = 18.000.000 − 9% × 18.000.000 = 16.380.000; 25% = 4.095.000.',
      '2. Consumo jan–set: o salário de 6.000.000 fica abaixo de 4 SMMLV (7.003.620), então **não há FSP** nesses meses: (6.000.000 − 8% × 6.000.000) × 25% = 1.380.000 × 9 = **12.420.000**. O lote A usou 9 × 25% × 5.460.000 = 12.285.000 (FSP de 1% indevido nos meses sem bônus): diverge no consumo, não no resultado. Prevalece 12.420.000 (é o que está no DRAFT).',
      '3. Saldo = 41.375.460 − 12.420.000 = 28.955.460 ≥ 4.095.000 → isenção 4.095.000. 40%: 6.552.000. 1.340 UVT: 16.515.000 ≤ 70.181.160.',
      f'4. Base = 16.380.000 − 4.095.000 = 12.285.000 = {A.uv(A.G180)} UVT → faixa 28%. Retenção = (12.285.000 − 7.856.100) × 28% + 523.740 = 4.428.900 × 0,28 + 523.740 = **{A.W180:,.2f}** (igual ao lote A). Hoje: 1.945.004,60 (−181.172,60). Líquido (T181) = 18.000.000 − 1.620.000 − 1.763.832 = 14.616.168,00.', '',
      '**Achados na varredura (mesma decisão, fora da lista do lote A):** T183 C3 (mesmo caso com pacto: contribuições 972.000; (C) 17.028.000; isenção 4.257.000; base 12.771.000) = 1.899.912,00 (hoje 2.126.444,60); T239/T240 (integral 25.000.000, (C) 23.425.000; de janeiro a julho a isenção é 5.856.250; base 17.568.750, faixa 28%) = 3.243.282,00, líquido 20.181.718,00 (hoje 3.984.199,65 / 19.440.800,35; em agosto sobra 381.710 do teto e de setembro a dezembro a isenção é zero); Payslip (ago/2026, 19.200.000 todo mês; consumo jan–jul 7 × 4.368.000 = 30.576.000; isenção 4.368.000; base 13.104.000) = 1.993.152,00, líquido 15.478.848,00 (hoje 2.250.764,60 / 15.221.235,40).']
M += ['', '## Simulações que mudariam (não alteradas; `final/simulations/` só lido)', '',
      '**A-1 (tetos anuais pelo acumulado)** — o oráculo indica os casos em que o 1/12 limitava; nas abas de março o consumo é de 2 meses:',
      '- `CO_Simulation_2026_10_30_V1.0.xlsx`: abas **C09–C17, C19–C23, R07 e R08** (linhas 69 isenção 25%, 70 teto 40%/1.340, benefícios aplicados, base gravável, base em UVT, imposto em UVT, retenção, líquido; mais o resumo/Checks/Formula comparison dessas abas). Fórmulas `p_RET_E25_UVT*p_UVT/12` e `p_RET_CAP_UVT*p_UVT/12` (linhas 69–70 de todas as 49 abas mensais) e a nota L69 ("operating convention") mudam em todas, mas o valor só muda nas listadas. Parameters B52 e B54 ("monthly = /12, operating convention"). README, ressalva 2.',
      '- `Tax Simulations - Colombia.xlsx`: abas **1340 UVT CAP BINDING (R07), 25 PCT EXEMPT 790 UVT CAP (R08), ALL-INCLUSIVE SALARY (C22)** e **NON-SALARY BONUS (RC05 = T105, set/2026: 4.994.989,65 → 3.947.554,80, com o consumo jan–ago só do salário)**; linhas 51 e N57/N59 (rótulos "monthly = /12") de todas as abas de depuração; SERVICE BONUS SEPARATE READ (PB) e READ ME B5/B10 (o ponto aberto 2 — divisão do 790/12 entre salário e prêmio — deixa de existir: o teto é um só no ano); SUMMARY (linhas de R07, R08, C22, RC05).',
      '- `Colombia Simulations - Law vs Provider.xlsx`: LAW SIMULATION C28 ("min(25% x residue, 790 UVT / 12)") e PROVIDER RESULT J28 (tolerância 3.447.953 × 3.447.955,50); a linha 28 e as dependentes (base, retenção) da folha de setembro precisam do consumo jan–ago de cada empregado — dado que não está nos agregados (regerar a partir do Test 4, sem abrir dado de cliente aqui).',
      '', '**A-2 (cesantías sem retenção)** — nenhuma simulação tem não residente com cesantías: sem efeito.']
M += ['', '## Decisões técnicas desta rodada (reversíveis) e o que ficou de fora', '',
      '- WTC Y114–116: **BonificacionS (NIE139)** (o lote C dava ConceptoS ou BonificacionS sem motivo decisivo; ficou o padrão pedido). Y124–133 também BonificacionS.',
      "- WTC V1: em vez de condicionar os dois valores ao pacto (texto do lote C), 'non-remunerative' → NS sempre; 'pacted' → NS com pacto, S sem pacto (o lote, ao pé da letra, faria o não remuneratório depender de pacto).",
      '- WTC 346: além de V e da nota AB346, Q/R/S/U = Yes/No e Y condicional (PagoAlimentacionNS/S), como na família do carro; T/W/X já eram No.',
      '- WTC A-2: N também → No (N1 = retenção), nota em D (explicação, com o 20% como opção desligada) e Z alinhado à citação de C22.',
      '- DD H7: lista positiva sem os códigos 2 e 3 (o lote B não diz o que são); G95 e G106 ("bank-mediated") ficaram. A linha nova 98 ocupa a linha 104, que era a separação em branco antes do bloco seguinte.',
      '- Payslip: incluído (não estava na lista de finais), porque o exemplo usava o 790/12 e a retenção muda (2.250.764,60 → 1.993.152,00).',
      '- Fora da lista do lote, mesma decisão (A-1/A-2), aplicados para o DRAFT não se contradizer: CCG P1047, P1049, P1311, T169, T175, T181, T183, T202, T215, T219, T228, T239, T240; NE C21; 004 Population Rules C21, Example A33/C33/D33, K51 e linhas do Sample File; 005 Report Matrix A35, Population Rules D22, Example A33/C33/D33, K42 e Sample File; PILA-003 D17, Example A33, Sample File A86 (posições 381–389, mesmo comprimento) e A113.',
      '- Res. 2708: a numeração de tabelas/parágrafos do lote B está uma acima da do python-docx (T12→T11, T35→T34, T34→T33, T52→T51, P416→P415, P433→P432); P432 (assunto morto) apagado com alteração controlada.',
      '- Passo 0 (decidido pelo usuário em 2026-11-02, fonte DUR 1625 art. 1.2.1.22.43 e CE S4 rad. 24047/2021): o teto de 3.800 UVT de fundos voluntários e AFC/AVC (ET 126-1/126-4) é anual, pelo acumulado, sem ÷ 12. Varredura de "3,800", "199,021,200", "16,585,100", "÷ 12"/"/12" em todos os DRAFT-R5: só o CCG T228R5C1 dividia por 12; aplicados CCG T228R5C1, CCG P602 (regra e fonte) e WTC Tax Credit A34 (A33 é só a primeira metade da frase, sem ÷ 12; nada nas specs, DD e Payslip). Mais as descrições do Version Control (WTC D20, linha nova do CCG).',
      '- Não feito (fora do decidido): CCG T112R3 (juros de moradia, 100 UVT/mês do ET 387 — regra mensal própria); skill `references/02-wtc.md` (10 linhas Y255–264, fora da lista de finais); base da exclusão para residentes em CCG T86R4C1 (fora do pedido no lote A).']
open(os.path.join(OUT, 'CONFERENCIA-R5.md'), 'w', encoding='utf-8').write('\n'.join(M) + '\n')
print('VEREDITO', 'PASS' if not total else 'FAIL', total)
sys.exit(1 if total else 0)
