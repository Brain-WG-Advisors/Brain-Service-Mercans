# -*- coding: utf-8 -*-
"""Release of the Colombia finals, issue 2026-11-02 (CCG v1.6, WTC v1.8, DD v1.5, five specs v1.2, Payslip v1.3,
SIR v1.3), from the DRAFT-R5 of revisao/rodada5/. Same method as release.py (issue 2026-10-30), whose functions are
reused unchanged: xlsx = highlight FFDDEBF7 removed + declared cell edits (XML surgery, no openpyxl save);
docx = all tracked changes accepted + declared paragraph edits (+ declared footer edit); issue metadata = 2026-11-02.

Before writing, the finals of 2026-10-30 that this issue replaces are MOVED to final/_historico/2026-10-30/ (with
their MD5-FINAIS.txt), so that final/ holds one version of each final. Idempotent: if they are already there (md5 =
the 2026-10-30 MD5-FINAIS), the move is skipped.
Usage: python -I final/scripts/release_r5.py
"""
import os, re, sys, json, shutil, hashlib, zipfile
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import release as R, release_r5_edits as E
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(VAL)
import calendar, time
R.DAY = E.ISSUE; R.STAMP = E.ISSUE + 'T09:00:00Z'; R.AUTHOR = E.AUTHOR
R.EPOCH = calendar.timegm(time.strptime(E.ISSUE + ' 09:00:00', '%Y-%m-%d %H:%M:%S'))
R.LOG = []
FIN = 'final'; HIST = 'final/_historico/2026-10-30'
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()

# ------------------------------------------------------------- 1. move the replaced finals of 2026-10-30
OLD = ['CO-CCG-001-v1.5.docx', 'CO-WTC-001-v1.7.xlsx', 'CO-DD-001-v1.4.xlsx', 'CO-SIR-001-v1.2-texto-final.md',
       'CO_Compliance_Payslip_Generator.xlsx', 'specs/CO-DIAN-001-NominaElectronica-Spec.xlsx',
       'specs/CO-DIAN-004-Formulario220-Spec.xlsx', 'specs/CO-DIAN-005-Formato2276-Spec.xlsx',
       'specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx', 'specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx']


def read_md5(p):
    out = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        h, f = ln.split(None, 1); out[f.strip()] = h
    return out


if not os.path.exists(os.path.join(HIST, 'MD5-FINAIS.txt')):
    old = read_md5(os.path.join(FIN, 'MD5-FINAIS.txt'))
    for f in OLD:
        assert md5(os.path.join(FIN, f)) == old[f], 'final de 30/10 alterado: ' + f
    os.makedirs(os.path.join(HIST, 'specs'), exist_ok=True)
    for f in OLD:
        shutil.move(os.path.join(FIN, f), os.path.join(HIST, f))
    shutil.copy2(os.path.join(FIN, 'MD5-FINAIS.txt'), os.path.join(HIST, 'MD5-FINAIS.txt'))
    print('moved', len(OLD), 'finals of 2026-10-30 to', HIST)
old = read_md5(os.path.join(HIST, 'MD5-FINAIS.txt'))
for f in OLD:
    assert md5(os.path.join(HIST, f)) == old[f], 'historico alterado: ' + f
for f in E.UNCHANGED:
    assert md5(os.path.join(FIN, f)) == old[f], 'spec inalterada mudou: ' + f


# ------------------------------------------------------------- 2. docx (release.docx_release + footer edit)
def docx_release_r5(art, draft, out, edits, footer):
    zd = zipfile.ZipFile(draft); infos = zd.infolist(); data = {i.filename: zd.read(i.filename) for i in infos}; zd.close()
    x, n0 = R.accept_all(data['word/document.xml'].decode('utf-8'))
    for e_ in edits:
        old_, new_ = e_[0], e_[1]
        x, before, after = R.para_edit(x, old_, new_, e_[2] if len(e_) > 2 else None)
        R.LOG.append((art, 'paragraph', before, after))
    data['word/document.xml'] = x.encode('utf-8')
    for part, ops in footer.items():
        fx = data[part].decode('utf-8')
        for old_, new_ in ops:
            ts = re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', fx)
            assert sum(t.count(R.esc(old_)) for t in ts) == 1, f'footer "{old_}"'
            before = ''.join(ts)
            fx = fx.replace(R.esc(old_), R.esc(new_), 1)
            R.LOG.append((art, part, before, ''.join(re.findall(r'<w:t(?: [^>]*)?>([^<]*)</w:t>', fx))))
        data[part] = fx.encode('utf-8')
    data['word/settings.xml'] = re.sub(rb'<w:trackRevisions[^>]*/>', b'', data['word/settings.xml'])
    if 'word/comments.xml' in data:
        c = data['word/comments.xml'].decode('utf-8')
        assert not re.search(r'<w:comment ', c), 'comments in the DRAFT-R5'
    R.write_zip(out, infos, data)
    return n0


# ------------------------------------------------------------- 3. SIR v1.3 (text to paste)
SIR_HEAD_OLD = ('# CO-SIR-001 v1.3 DRAFT-R5: texto para colar no Google Doc (rodada 5, 2026-11-02, NÃO emitido)\n\n'
                '> DRAFT da rodada 5, gerado por `revisao/rodada5/scripts/apply_r5.py` a partir de `final/CO-SIR-001-v1.2-texto-final.md`. '
                'Mudanças marcadas com **[R5]** fora dos blocos de código (o que vai para o Doc é só o conteúdo dos blocos).')
RD_OLD = 'CO-CCG-001 v1.5 (Module 10); the seven Report Specs v1.1 (including CO-PILA-007, the pensioners PILA flow); CO-DD-001 v1.4; CO Payslip Generator v1.2; DIAN-NE Configuration Runbook (P1–P7)'
RD_NEW = 'CO-CCG-001 v1.6 (Module 10); the seven Report Specs (five at v1.2; CO-DIAN-002 and CO-PILA-007, the pensioners PILA flow, at v1.1); CO-DD-001 v1.5; CO Payslip Generator v1.3; DIAN-NE Configuration Runbook (P1–P7)'
VH_OLD_LINE_START = 'v1.2 | 2026-10-30 | '
VH_NEW = ('v1.3 | 2026-11-02 | Statutory validation, second pass: NE validation-rule count (Anexo Técnico NE v1.0 §6: 519 rules); '
          'related deliverables and Appendix A updated (CO-CCG-001 v1.6, Report Specs v1.2, CO-DD-001 v1.5, Payslip Generator v1.3).')
SIR_SUBS = [
 (SIR_HEAD_OLD, '# CO-SIR-001 v1.3: texto final para colar no Google Doc'),
 ('Emissão 2026-10-30.', 'Emissão 2026-11-02 (substitui o texto da v1.2 de 2026-10-30, guardado em `_historico/2026-10-30/`).'),
 ('`changelogs/CO-SIR-001-v1.2-CHANGELOG.md` e no redline `revisao/SIR/CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE.md`',
  '`changelogs/CO-SIR-001-v1.3-CHANGELOG.md`, no redline `revisao/SIR/CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE.md` e em `revisao/rodada5/mudancas-RODADA5.md`'),
 ('Ligado a [[CONFERENCIA]] e [[RELEASE-CROSSCHECK]].', 'Ligado a [[CONFERENCIA]] e [[RELEASE-CROSSCHECK-R5]].'),
 ('Campo **Version** (hoje `v1.2`) **[R5] antes: `v1.2`**:', 'Campo **Version** (hoje `v1.2`):'),
 ('(hoje começa por `CO-CCG-001 v1.1 (Module 10)`)', '(hoje começa por `CO-CCG-001 v1.5 (Module 10)`)'),
 (RD_OLD, RD_NEW),
 ('**Version history**: acrescentar a linha, depois da v1.1:',
  '**Version history**: acrescentar a linha, depois da v1.2 (se a linha v1.2 ainda não estiver no Doc, colar antes a linha v1.2 do texto de 2026-10-30):'),
 ('Linha NE, contagem de regras (âncora: `430`) **[R5] S-07 — antes: "more than 430 validation rules (R = rejection, N = notification), Anexo Técnico NE v1.0 §6"; fonte: Anexo Técnico NE v1.0 §6, pp. 182–232 (contagem do lote C, dois métodos)**:',
  'Linha NE, contagem de regras (âncora: `430`):'),
 ('Entrada do CCG (hoje `CO-CCG-001 v1.1`):', 'Entrada do CCG (hoje `CO-CCG-001 v1.5`):'),
 ('CCG Module 10 (CO-CCG-001 v1.5)', 'CCG Module 10 (CO-CCG-001 v1.6)'),
 ('Entrada das specs (hoje fala em seis specs, sem a CO-PILA-007):', 'Entrada das specs (hoje `7 Report Specs v1.1`):'),
 ('7 Report Specs v1.1 (including CO-PILA-007, pensioners PILA flow)', '7 Report Specs (v1.2; CO-DIAN-002 and CO-PILA-007 v1.1; including CO-PILA-007, pensioners PILA flow)'),
 ('Conferir no Doc: Version `v1.2`, a linha nova do Version history e os 15 blocos acima.', 'Conferir no Doc: Version `v1.3`, a linha nova do Version history e os 15 blocos acima.'),
]


def sir_release(src, dst):
    t = open(src, encoding='utf-8').read()
    log = []
    for o, n in SIR_SUBS:
        assert t.count(o) == 1, 'SIR: ' + o[:70]
        t = t.replace(o, n); log.append(('SIR', 'texto', o, n))
    lines = t.split('\n')
    k = [i for i, l in enumerate(lines) if l.startswith(VH_OLD_LINE_START)]
    assert len(k) == 1
    log.append(('SIR', 'Version history (bloco)', lines[k[0]], VH_NEW)); lines[k[0]] = VH_NEW
    t = '\n'.join(lines)
    assert '[R5]' not in t and 'DRAFT-R5' not in t
    open(dst, 'w', encoding='utf-8', newline='\n').write(t)
    R.LOG.extend(log)


if __name__ == '__main__':
    for art, d, b, f, v in E.PAIRS:
        out = os.path.join(FIN, f)
        if f.endswith('.docx'):
            n0 = docx_release_r5(art, d, out, E.DOCX.get(art, []), E.FOOTER.get(art, {}))
            print(f'{art:8} {f}: {n0} tracked changes accepted, {len(E.DOCX.get(art, []))} paragraph edits, footer edits {sum(len(v_) for v_ in E.FOOTER.get(art, {}).values())}')
        else:
            st, pok, nadd = R.xlsx_release(art, d, b, out, E.XLSX.get(art, {}))
            print(f'{art:8} {f}: highlight removed {st} (base styles usable: {pok}; new xf {nadd}); {len(E.XLSX.get(art, {}))} cell edits')
    sd, sb, sf, sv = E.SIR
    sir_release(sd, os.path.join(FIN, sf))
    print('SIR     ', sf)
    json.dump([dict(artifact=a, where=w, before=bf, after=af) for a, w, bf, af in R.LOG],
              open(os.path.join(FIN, 'scripts', 'release_r5_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('edits logged', len(R.LOG))
