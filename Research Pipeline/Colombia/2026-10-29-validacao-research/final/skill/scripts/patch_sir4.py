"""03-sir.md: CO-SIR-001 v1.3 -> v1.4 (2026-11-02, round 6). The v1.4 Doc changes (final/CO-SIR-001-v1.4-texto-final.md,
checked against the Doc export by SHA-256) are applied to the compiled reference as targeted replacements, marked v1.4;
the navigation index is then recomputed from the headings and checked."""
import os, re, hashlib
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIN = os.path.dirname(S)
P = os.path.join(S, 'payroll-compliance-colombia', 'references', '03-sir.md')
T4 = os.path.join(FIN, 'CO-SIR-001-v1.4-texto-final.md')
E4 = os.path.join(FIN, 'CO-SIR-001-v1.4-export-2026-11-02.txt')
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
t = open(P, encoding='utf-8').read()
M = ' ⟦v1.4⟧'
RD = ("CO-CCG-001 v1.7 (Module 10); the seven Report Specs (CO-DIAN-004 at v1.3; CO-DIAN-001, CO-DIAN-005, CO-PILA-003 and "
      "CO-CESANTIAS-006 at v1.2; CO-DIAN-002 and CO-PILA-007, the pensioners PILA flow, at v1.1); CO-DD-001 v1.6; CO Payslip "
      "Generator v1.3; DIAN-NE Configuration Runbook (P1–P7)")
HIST = ("| v1.4 | 2026-11-02 | Pensioners' PILA (CO-PILA-007) added to the integration inventory (0.1), outbound register (2.1) and "
        "data disaggregation (2.2); in-scope filings corrected from six to seven; internal working-file names removed from section 0 "
        "and Appendix A; related deliverables and Appendix A updated (CO-CCG-001 v1.7, CO-DIAN-004 v1.3, CO-DD-001 v1.6)." + M + " |")
subs = [
 ('# Colombia Statutory Integrations Register (SIR) - CO-SIR-001 v1.3', '# Colombia Statutory Integrations Register (SIR) - CO-SIR-001 v1.4'),
 ('| `CO-SIR-001-v1.3-texto-final.md (v1.3 text, 15 blocks)` |',
  f'| `CO-SIR-001-v1.4-texto-final.md (v1.4 changes)` | {os.path.getsize(T4):,} | `{md5(T4)}` |\n'
  f'| `CO-SIR-001-v1.4-export-2026-11-02.txt (Doc export, v1.4)` | {os.path.getsize(E4):,} | `{md5(E4)}` |\n'
  '| `CO-SIR-001-v1.3-texto-final.md (v1.3 text, 15 blocks)` |'),
 ('and 1.3 (issued 2026-11-02) were released as 15 replacement blocks over version 1.1.',
  'and 1.3 (issued 2026-11-02) were released as 15 replacement blocks over version 1.1; version 1.4 (issued 2026-11-02) '
  'changed sections 0, 0.1, 2.1, 2.2, the related deliverables and Appendix A (marked ⟦v1.4⟧).'),
 ('- **Not in the SIR text:** sections 0 and 2 of the Google Doc still speak of six in-scope filings and do not describe the\n'
  '  pensioners flow (CO-PILA-007); this file adds that flow in Part 1 §0 and §2 from the report specs.',
  "- **Seven in-scope filings** since v1.4: the pensioners' PILA (CO-PILA-007, Anexo Técnico 3) is channel CO-OUT-PILA-002 and\n"
  '  applies only where the employer pays pensions directly as pension payer.'),
 ('Part 1 - CO-SIR-001 v1.3 (Statutory Integration Register)', 'Part 1 - CO-SIR-001 v1.4 (Statutory Integration Register)', 2),
 ('| Version | v1.3 ⟦v1.3⟧ |', '| Version | v1.4' + M + ' |'),
 (re.search(r'\| Related deliverables \| (.*?) ⟦v1\.3⟧ \|', t).group(1) + ' ⟦v1.3⟧ |', RD + M + ' |'),
 ('  document is carried system-to-system; the others are manual (portal or operator upload). The seventh filing, PILA for pensioners\n'
  "  paid by the employer (CO-PILA-007), rides on the same operator channel as the employees' PILA.",
  "  document is carried system-to-system; the others are manual (portal or operator upload). Of the seven in-scope filings, one is\n"
  "  carried system-to-system and six are manual or operator-mediated; one of them, the pensioners' PILA (CO-PILA-007, Anexo Técnico 3),\n"
  '  applies only where the employer pays pensions directly as pension payer.' + M),
 ('| CO-OUT-PILA-001 | PILA via operador de información | Outbound | Yes (file generation only) |\n',
  '| CO-OUT-PILA-001 | PILA via operador de información | Outbound | Yes (file generation only) |\n'
  '| CO-OUT-PILA-002 | PILA (pensioners) via operador de información | Outbound | Yes (file generation only)' + M + ' |\n'),
 ('| CO-OUT-PILA-001 | CO-PILA-003 (employees), CO-PILA-007 (pensioners) | Monthly | Fixed-width TXT (Archivo Tipo 1 + Archivo Tipo 2) |',
  '| CO-OUT-PILA-001 | CO-PILA-003 | Monthly | Fixed-width TXT (Archivo Tipo 1 + Archivo Tipo 2) |\n'
  '| CO-OUT-PILA-002 | CO-PILA-007 (pension payer type 01) | Monthly | Fixed-width TXT (Archivo Tipo 1 + Archivo Tipo 2, Anexo Técnico 3)' + M + ' |'),
 ('IBC by subsystem, days, change events (novedades), health, pension, solidarity fund, ARL, CCF, SENA, ICBF · Cesantías',
  "IBC by subsystem, days, change events (novedades), health, pension, solidarity fund, ARL, CCF, SENA, ICBF · PILA pensioners - per\n"
  "pensioner: pension type, mesada, contribution days, health, solidarity fund and, where they apply, pension and CCF; no occupational\n"
  'risk, SENA or ICBF' + M + ' · Cesantías'),
 ('CCG Module 10 (CO-CCG-001 v1.6) ⟦v1.3⟧ · 7 Report Specs (v1.2; CO-DIAN-002 and CO-PILA-007 v1.1; including CO-PILA-007, pensioners PILA flow) ⟦v1.3⟧',
  "Scope decision of 3 September 2026 (internal scope record): 4 authorities; 7 in-scope filings (the six original filings plus the "
  "pensioners' PILA, CO-PILA-007, added on 21 October 2026), 7 descoped" + M + ' · CCG Module 10 (CO-CCG-001 v1.7)' + M +
  ' · 7 Report Specs (CO-DIAN-004 v1.3; CO-DIAN-002 and CO-PILA-007 v1.1; the others v1.2; including CO-PILA-007, pensioners PILA flow)' + M),
 ('integration landscape (2026-09-04).', 'Integration discovery record of 4 September 2026 (internal working file behind this register).' + M),
]
for s in subs:
    o, n = s[0], s[1]; k = s[2] if len(s) > 2 else 1
    assert t.count(o) == k, (o[:70], t.count(o)); t = t.replace(o, n)
L = t.split('\n')
h3 = [i for i, l in enumerate(L) if l.startswith('| v1.3 | 2026-11-02 |')]; assert len(h3) == 1
L.insert(h3[0] + 1, HIST)
# recompute the navigation index
idx = [i for i, l in enumerate(L) if re.match(r'\| \d+ \| ', l) and i < 60 and '&nbsp;' in l or re.match(r'\| \d+ \| Part \d', l)]
for i in idx:
    label = re.sub(r'^\| \d+ \| ', '', L[i]).rstrip(' |').replace('&nbsp;', '')
    lev = L[i].count('&nbsp;&nbsp;&nbsp;&nbsp;')
    head = ('### ' if lev else '## ') + label
    hits = [j for j, l in enumerate(L) if l == head]; assert len(hits) == 1, head
    L[i] = re.sub(r'^\| \d+ \|', f'| {hits[0] + 1} |', L[i])
t = '\n'.join(L)
for i in idx:
    n = int(t.split('\n')[i].split('|')[1]); assert t.split('\n')[n - 1].lstrip('#').strip().startswith(re.sub(r'^\| \d+ \| ', '', t.split('\n')[i]).replace('&nbsp;', '').rstrip(' |')[:20])
assert 'six in-scope' not in t and 'integration landscape (2026' not in t and 'CO-CCG-001 v1.6 (Module' not in t
open(P, 'w', encoding='utf-8', newline='\n').write(t)
print('03-sir.md', len(t.encode('utf-8')), 'index rows', len(idx))
