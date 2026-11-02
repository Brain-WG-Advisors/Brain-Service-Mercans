"""03-sir.md: CO-SIR-001 v1.3 (Google Doc only) = v1.1 content + the 15 blocks of the v1.3 text verbatim (marked v1.3 where
they differ from the v1.2 text, v1.2 otherwise) + the v1.2 version-history line; plus the authority index.
Copy of build_sir.py (2026-10-30, v1.2), same method."""
import os, re, hashlib
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
B = r'C:\Users\instituto\Documents\brain-service\Research Pipeline\Colombia'
FIN = os.path.join(B, '2026-10-29-validacao-research', 'final')
REF = os.path.join(FIN, 'skill', 'payroll-compliance-colombia', 'references')
SIRT = os.path.join(FIN, 'CO-SIR-001-v1.3-texto-final.md')
SIR2 = os.path.join(FIN, '_historico', '2026-10-30', 'CO-SIR-001-v1.2-texto-final.md')
CAP = os.path.join(B, '2026-10-29-validacao-research', 'linha-de-base', 'CO-SIR-001-v1.1-captura-2026-10-29.md')
IDX = os.path.join(B, 'CO-compliance', '03-statutory-integrations', 'CO-SIR-INDEX-001-v1.0.docx')
def md5(p): return hashlib.md5(open(p, 'rb').read()).hexdigest()
def size(p): return f'{os.path.getsize(p):,}'

# the 15 blocks, read from the released text (code blocks in order)
blocks = re.findall(r'```\n(.*?)\n```', open(SIRT, encoding='utf-8').read(), flags=re.S)
assert len(blocks) == 15, len(blocks)
(V, DELIV, HIST, NE_DEDUCT, NE_RULES, CES, PEN_NE, PEN_PILA, DL_PILA, DL_2276, DL_INT, DL_NE, APP_CCG, APP_SPECS, APP_PILA) = blocks
blocks2 = re.findall(r'```\n(.*?)\n```', open(SIR2, encoding='utf-8').read(), flags=re.S)
assert len(blocks2) == 15
HIST2 = blocks2[2]; assert HIST2.startswith('v1.2 | 2026-10-30 | ')
CHANGED = {b for b, b2 in zip(blocks, blocks2) if b != b2}

def q(t):  # mark a verbatim block: v1.3 where it differs from the v1.2 text, v1.2 otherwise
    return f'{t} ⟦v1.3⟧' if t in CHANGED else f'{t} ⟦v1.2⟧'

idx = open(os.path.join(OUT, 'sir10.md'), encoding='utf-8').read()
idx = idx.replace(' (produced by si-discovery (Agent 3 / STAGE 6a))', '')
idx = idx.replace(' per scope_manifest v1.0 (6 in-scope filings, 7 descoped)', ' (6 in-scope filings at v1.0)')
idx = idx.replace('Source: 03-statutory-integrations/integration-landscape.json  |  ', '')
idx = idx.replace('Authority index generated from integration-landscape.json.', 'Authority index generated from the integration discovery record.')
assert 'scope_manifest' not in idx and 'integration-landscape' not in idx, 'leftover'
idx = re.sub(r'^(#{1,5}) ', lambda m: '###' + m.group(1)[1:] + ' ', idx, flags=re.M)
assert 'Agent' not in idx and 'STAGE' not in idx

body = f"""## Part 1 - CO-SIR-001 v1.3 (Statutory Integration Register)

### Document control

| Field | Value |
|---|---|
| Document ID | CO-SIR-001 |
| Version | {q(V)} |
| Country | Colombia (CO) |
| Jurisdictions | National - DIAN (tax); Ministerio de Salud y Protección Social via licensed operadores de información (PILA); Fondos de Cesantías via operador |
| Tax year | 2026 |
| Currency | COP |
| Status | Issued |
| Related deliverables | {q(DELIV)} |

Version history:

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-09-04 | Initial issue |
| v1.1 | 2026-10-21 | Citations of Res. DIAN 000013 de 2021 updated to Res. DIAN 000227 de 2025. |
| {HIST2.split(' | ')[0]} | {HIST2.split(' | ')[1]} | {HIST2.split(' | ')[2]} ⟦v1.2⟧ |
| {HIST.split(' | ')[0]} | {HIST.split(' | ')[1]} | {HIST.split(' | ')[2]} ⟦v1.3⟧ |

### 0. Purpose and scope

- Discovery verdict **HAS_INTEGRATIONS**: 4 authorities; 1 system-to-system channel. Of the in-scope filings, the electronic payroll
  document is carried system-to-system; the others are manual (portal or operator upload). The seventh filing, PILA for pensioners
  paid by the employer (CO-PILA-007), rides on the same operator channel as the employees' PILA.
- Integration inventory:

| ID | Authority / channel | Direction | Integration |
|---|---|---|---|
| CO-OUT-NE-001 | DIAN - Servicio de Validación de Nómina Electrónica | Outbound | Yes |
| CO-IN-NE-APPRESPONSE | DIAN - ApplicationResponse / GetStatus | Inbound | Yes |
| CO-OUT-MUISCA-001 | DIAN - Muisca (Form 350) | Outbound | No |
| CO-OUT-PILA-001 | PILA via operador de información | Outbound | Yes (file generation only) |
| CO-IN-PILA-001 | PILA settlement return | Inbound | No |
| CO-OUT-CESANTIAS-001 | Fondos de Cesantías via operador | Outbound | Yes (file generation only) |
| CO-IN-CESANTIAS-CONFIRMATION | Severance-fund confirmation | Inbound | No |

- Electronic payroll sources: Res. DIAN 000227 de 2025 (which compiles Res. DIAN 000013 de 2021), Anexo Técnico del Documento Soporte de
  Pago de Nómina Electrónica v1.0 (269 pp.), XSD v1.0.6 and the WSDL (obtained 2026-09-04). Where the annex and the WSDL diverge,
  the WSDL governs.

### 1. Inbound

- {q(NE_DEDUCT)}
- Inbound register: CO-IN-NE-APPRESPONSE (SendNominaSync response + GetStatus by CUNE; mandatory) · CO-IN-PILA-001 (operational) ·
  CO-IN-CESANTIAS-CONFIRMATION (records E10, E11, E90, E91, E93; operational).

### 2. Outbound

| Channel | Report spec | Frequency | Format |
|---|---|---|---|
| CO-OUT-NE-001 | CO-DIAN-001 | Monthly | SOAP 1.2; base64 ZIP holding exactly one signed XML; UTF-8; 500 KB maximum |
| CO-OUT-MUISCA-001 | CO-DIAN-002 | Monthly | Portal entry, no file |
| CO-OUT-PILA-001 | CO-PILA-003 (employees), CO-PILA-007 (pensioners) | Monthly | Fixed-width TXT (Archivo Tipo 1 + Archivo Tipo 2) |
| CO-OUT-CESANTIAS-001 | CO-CESANTIAS-006 | Annual | Fixed TXT, XLS 97-2003 or CSV, per operator |

Content per channel: NE - per employee: salary, overtime, allowances, bonuses, severance savings and interest, vacation; health,
pension, solidarity fund, withholding, garnishments, third-party payments · Form 350 - withholding aggregated by concept · PILA -
IBC by subsystem, days, change events (novedades), health, pension, solidarity fund, ARL, CCF, SENA, ICBF · Cesantías - annual
liquidation at 31 December, fund, contact, start date · Form 220 - issued to the employee, not filed with DIAN · Format 2276 -
income and withholding per beneficiary for the year.

### 3. Authentication

- **NE:** the annex (§9.3/§9.4) describes mutual TLS, while the WSDL policy has `sp:HttpsToken RequireClientCertificate="false"`:
  TLS 1.2 server-side only, with WS-Security 1.0 message security (X.509 Token Profile 1.1, Basic256Sha256Rsa15, timestamp) and
  WS-Addressing (signed `To`). Document signature XAdES-EPES (SHA-1 rejected); certificate from an ONAC-accredited authority;
  habilitación (SoftwareID, PIN, test set; global rule 92). Third-party transmitter: Res. 227/2025 art. 1.5.3.8.1 (enabled third
  party, registered in the RUT, mandate).
- **Muisca (Form 350, Format 2276):** interactive session with the Instrumento de Firma Electrónica (IFE); no machine credential.
- **PILA:** operator credentials (Aportes en Línea, Enlace Operativo, MiPlanilla, Asopagos, SOI, ...); no government-published
  authentication.
- **Cesantías:** operator login. The "APIS PILA" developer portal of one operator was only a shell on 2026-09-04 and is not used.

### 4. Technical specifications

- **NE:** SOAP 1.2 document/literal; operations SendNominaSync and GetStatus (2 of the 15 operations in scope); production host
  `vpfe.dian.gov.co`, habilitación host `vpfe-hab.dian.gov.co` (`/WcfDianCustomerServices.svc`); XSD v1.0.6; {q(NE_RULES)}; 500 KB;
  no batch (one document per beneficiary).
- **Muisca:** portal. **PILA:** two fixed-width TXT files; government layout plus operator pre-validation.
- **Cesantías:** {q(CES)}

### 5. Errors

- Seven classes: Container, Signature, Schema, Business (R), Business (N), global rule 90 (document number reused), global rule 92
  (issuer not enabled).
- No idempotent retry: query GetStatus by CUNE before resending; corrections by adjustment note; ApplicationResponse 02 = validated,
  04 = rejected.
- Penalties: {q(PEN_NE)} · Form 350 (ET 641, 634) · {q(PEN_PILA)} · Cesantías (one day's salary per day of delay, uncapped; Ley
  50/1990 art. 99 num. 3).

### 6. Deadlines

- NE: first 10 days of the month following payment; one document per employee per month (Res. 227/2025 arts. 1.5.3.2.2 and
  1.5.3.4.1.1).
- Form 350: 7th to 16th business day, by the last digit of the NIT (DUR 1625/2016 art. 1.6.1.13.2.33).
- {q(DL_PILA)}
- Cesantías: before 15 February (Ley 50/1990 art. 99 num. 3).
- {q(DL_2276)}
- Form 220: by the last business day of March; not filed with DIAN (DUR 1625/2016 art. 1.6.1.13.2.40).
- {q(DL_INT)}
- {q(DL_NE)}

### Appendix A - sources cited by the SIR

{q(APP_CCG)} · {q(APP_SPECS)} · DIAN-NE Configuration Runbook (P1-P7) · Res. DIAN 000227/2025 arts. 1.5.3.1.1 to 1.5.3.9.8 ·
Anexo Técnico DSPNE v1.0 · XSD v1.0.6 · WSDL · {q(APP_PILA)} · severance-fund operator manual · operator portal ·
integration landscape (2026-09-04).


## Part 2 - Authority index (CO-SIR-INDEX-001 v1.0, 2026-09-04)

The discovery index the SIR was built on: one row per authority, with the channel, direction and developer portal. Verbatim,
except three provenance phrases naming internal working files. Read it with Part 1: the filing count is now **seven** (CO-PILA-007,
pensioners, rides on the PILA operator channel), and the deductibility citation is the one in Part 1 §1.

{idx}
"""

intro = ('The Colombia statutory-integration register: for each authority a payroll engine must interact with, the channel, '
         'direction, authentication, technical format, error classes, penalties and deadlines - and whether the channel is '
         'machine-to-machine (only the DIAN electronic payroll web service) or a portal / operator round-trip (Form 350, Format '
         '2276, PILA, severance funds).')
prov = [('CO-SIR-001-v1.3-texto-final.md (v1.3 text, 15 blocks)', size(SIRT), md5(SIRT)),
        ('CO-SIR-001-v1.2-texto-final.md (v1.2 text; its version-history line)', size(SIR2), md5(SIR2)),
        ('CO-SIR-001 v1.1 Google Doc, text capture of 2026-10-29 (base of v1.2)', size(CAP), md5(CAP)),
        ('CO-SIR-INDEX-001-v1.0.docx (authority index)', size(IDX), md5(IDX))]
verb = ('CO-SIR-001 exists only as a Google Doc; versions 1.2 (issued 2026-10-30) and 1.3 (issued 2026-11-02) were released '
        'as 15 replacement blocks over version 1.1. Part 1 is therefore the v1.1 content (from the read-only text capture, '
        'restated in English) with the 15 blocks of the v1.3 text inserted **verbatim**; a block is marked ⟦v1.3⟧ where it '
        'changed in v1.3 and ⟦v1.2⟧ where it is unchanged since v1.2. Where Part 1 and Part 2 differ, Part 1 '
        'governs. Part 2 is a verbatim conversion of the index docx.')
notes = [
 '- **Electronic payroll as support for costs and deductions:** Res. DIAN 000227 de 2025 art. **1.5.3.2.1** (formerly Res. 000013',
 '  de 2021 art. 2). Art. 1.5.3.2.3 only defines the obligated parties - do not cite it for deductibility.',
 '- **Validation rules:** Anexo Técnico NE v1.0 §6 lists **519** rules (437 for the payroll documents); the split is in Part 1 §4.',
 '- **NE contingency:** transmit within 48 hours counted from the day after the service is restored (art. 1.5.3.5.1.5).',
 '- **Not in the SIR text:** sections 0 and 2 of the Google Doc still speak of six in-scope filings and do not describe the',
 '  pensioners flow (CO-PILA-007); this file adds that flow in Part 1 §0 and §2 from the report specs.',
 '- Detailed NE transport, signature, CUNE and code tables: `04-reports-spec.md` CO-DIAN-001 (File Structure, Field Options).',
]

def assemble(rows):
    h = ['# Colombia Statutory Integrations Register (SIR) - CO-SIR-001 v1.3', '', intro, '', '', '## Provenance', '',
         '| Source artifact | Bytes | MD5 |', '|---|---|---|']
    h += [f'| `{a}` | {b} | `{c}` |' for a, b, c in prov]
    h += ['', verb, '', '', '## Reading notes (added at compilation, 2026-11-02)', '', *notes, '', '',
          '## Navigation index', '', 'Read with `offset` / `limit` rather than opening the whole file.', '',
          '| Line | Section |', '|---|---|', *rows, '', '---', '', '']
    return '\n'.join(h) + body
bl = body.split('\n')
ent = [(i, l) for i, l in enumerate(bl) if re.match(r'#{2,3} ', l)]
first = assemble(['| 0 | x |'] * len(ent))
off = first.count('\n') - body.count('\n')
rows = [f'| {i + off + 1} | {"&nbsp;&nbsp;&nbsp;&nbsp;" * (l.count("#", 0, 3) - 2)}{l.lstrip("#").strip()} |' for i, l in ent]
txt = assemble(rows)
tl = txt.split('\n')
for (i, l), r in zip(ent, rows):
    assert tl[int(r.split('|')[1]) - 1] == l
for b in blocks:
    assert b in txt, b[:50]
open(os.path.join(REF, '03-sir.md'), 'w', encoding='utf-8', newline='\n').write(txt)
print('03-sir.md', len(txt.encode('utf-8')))
