"""EG-CCG-001 v1_4 -> v1.5: seguro social a partir de 01/01/2027 (HRBS-15790).
Uso: python -I aplicar_ccg.py <base.docx> <saida.docx> [--dry]
Cada edicao declara o trecho antigo e quantas vezes ele aparece no paragrafo; aborta se nao bater.
Troca dentro do run quando o trecho cabe num run (preserva formatacao); senao reconstroi o paragrafo
com o rPr do primeiro run. Todo run alterado recebe sombreamento DDEBF7.
"""
import sys, re, zipfile, html

BASE, SAIDA = sys.argv[1], sys.argv[2]
DRY = "--dry" in sys.argv
sys.stdout.reconfigure(encoding="utf-8")

F27 = "from 1 Jan 2027"
# (indice do paragrafo, [(trecho antigo, trecho novo)])
ED = [
 (2,   [("EG-CCG-001 v1.1", "EG-CCG-001 v1.5")]),
 (6,   [("v1.1", "v1.5")]),
 (7,   [("QA Patched — 2026-05-27", "Regulation Update — 2026-10-25 (social insurance from 1 January 2027)")]),
 (337, [("Must be between EGP 2,700 and EGP 16,700 for 2026", "Must be between EGP 2,700 and EGP 16,700 for 2026; between EGP 3,200 and EGP 19,300 from 1 January 2027")]),
 (391, [("For 2026, the employer's total SS rate is 18.75% of the capped contribution wage, breaking down as follows:",
         "For 2026, the employer's total SS rate is 18.75% of the capped contribution wage (19.25% from 1 January 2027, when the OAD rate rises to 12.50%), breaking down as follows:")]),
 (397, [("12.00%", f"12.00% (12.50% {F27})")]),
 (398, [("SIL 148/2019 Art. 19", "SIL 148/2019 Art. 19; Executive Regulations Art. 57")]),
 (412, [("**18.75%**", f"**18.75%** (19.25% {F27})")]),
 (415, [("**11.00%** (9% OAD + 1% Sickness + 1% Gratuity)", f"**11.00%** (9% OAD + 1% Sickness + 1% Gratuity); 11.50% {F27} (9.5% OAD)")]),
 (418, [("**29.75%**", f"**29.75%** (30.75% {F27})")]),
 (422, [("(total 29.75% of contribution wage)", "(total 29.75% of contribution wage; 30.75% from 1 January 2027)"),
        ("capped at EGP 16,700/month and floored at EGP 2,700/month for 2026.", "capped at EGP 16,700/month and floored at EGP 2,700/month for 2026, and EGP 19,300/month and EGP 3,200/month from 1 January 2027.")]),
 (657, [("(EGP 2,700) and cap (EGP 16,700) for 2026:", "(EGP 2,700) and cap (EGP 16,700) for 2026, and EGP 3,200 and EGP 19,300 from 1 January 2027:")]),
 (1083, [("12%", f"12% (12.5% {F27})")]),
 (1084, [("9%", f"9% (9.5% {F27})")]),
 (1108, [("**18.75%**", f"**18.75%** (19.25% {F27})")]),
 (1109, [("**11%**", f"**11%** (11.5% {F27})")]),
 (1129, [("The contribution wage is subject to a statutory floor and ceiling that are revised periodically by ministerial decree:",
          "The contribution wage is subject to a statutory floor and ceiling set by Article 53 of the Executive Regulations (PM Decree 2437/2021): EGP 1,000 and EGP 7,000 per month from 1 January 2020, increased by 15% every 1 January for seven years (2021–2027) and by the inflation rate thereafter, rounded up to the nearest EGP 100:")]),
 (1132, [("2026 Monthly Amount", "Monthly Amount (2026 | from 1 Jan 2027)")]),
 (1134, [("EGP 2,700", "EGP 2,700 | EGP 3,200")]),
 (1136, [("EGP 16,700", "EGP 16,700 | EGP 19,300")]),
 (1139, [("Wages between these figures are used at their actual amount.", "Wages between these figures are used at their actual amount. From 1 January 2027 the same rule applies with EGP 3,200 and EGP 19,300.")]),
 (1152, [("the floor/ceiling parameters for 2026:", "the floor/ceiling parameters for 2026 (values from 1 January 2027 in brackets where they change):")]),
 (1163, [("12%", "12% (12.5%)")]),
 (1164, [("9%", "9% (9.5%)")]),
 (1165, [("21%", "21% (22%)")]),
] + [(k, [("2,700", "2,700 (3,200)")]) for k in (1166, 1173, 1180, 1187, 1194)] \
  + [(k, [("16,700", "16,700 (19,300)")]) for k in (1167, 1174, 1181, 1188, 1195)] + [
 (1198, [("**18.75%**", "**18.75%** (19.25%)")]),
 (1199, [("**11%**", "**11%** (11.5%)")]),
 (1200, [("**29.75%**", "**29.75%** (30.75%)")]),
 (1215, [("Ministerial Decree setting contribution wage floor and ceiling for 2026.",
          "Executive Regulations (PM Decree 2437/2021), Arts. 53 (floor and ceiling) and 57 (rate increase every seven years); NOSI notice of 30 November 2025 (2026 floor and ceiling).")]),
 (1226, [("Step 2: Apply the contribution wage floor and ceiling.", "Step 2: Apply the contribution wage floor and ceiling (EGP 2,700 / 16,700 for 2026; EGP 3,200 / 19,300 from 1 January 2027).")]),
 (1237, [("Contribution wage × 12%", f"Contribution wage × 12% (12.5% {F27})")]),
 (1238, [("Contribution wage × 9%", f"Contribution wage × 9% (9.5% {F27})")]),
 (1252, [("**× 18.75%**", f"**× 18.75%** (19.25% {F27})")]),
 (1253, [("**× 11%**", f"**× 11%** (11.5% {F27})")]),
 (1257, [("(11% of the contribution wage)", "(11% of the contribution wage; 11.5% from 1 January 2027)")]),
 (1260, [("ER share (18.75%) plus EE share (11%) = 29.75% of the contribution wage", "ER share (18.75%) plus EE share (11%) = 29.75% of the contribution wage (19.25% + 11.5% = 30.75% from 1 January 2027)")]),
 (3157, [("EGP 16,700 ceiling is the 2026 figure;", "EGP 16,700 ceiling is the 2026 figure (EGP 19,300 from 1 January 2027);")]),
 (3545, [("11% of monthly SS base (capped at EGP 16,700)", "11% of monthly SS base (capped at EGP 16,700); 11.5% capped at EGP 19,300 from 1 Jan 2027")]),
 (3548, [("18.75% of monthly SS base", f"18.75% of monthly SS base (19.25% {F27})")]),
 (3882, [("- Floor: EGP 2,700/month; Ceiling: EGP 16,700/month", "- Floor: EGP 2,700/month; Ceiling: EGP 16,700/month (EGP 3,200 / 19,300 from 1 January 2027)")]),
 (3883, [("11% of SS contribution wage", f"11% of SS contribution wage (11.5% {F27})")]),
 (3884, [("18.75% of SS contribution wage", f"18.75% of SS contribution wage (19.25% {F27})")]),
 (3885, [("then apply 11% / 18.75%", "then apply 11% / 18.75% (11.5% / 19.25% from 1 January 2027)")]),
 (3916, [(None,
   "The floor and ceiling of the contribution wage change automatically every 1 January under Article 53 of the Executive Regulations (PM Decree 2437/2021): +15% per year for seven years from 2021 (the last step is 1 January 2027: EGP 3,200 / 19,300), then by the inflation rate, rounded up to the nearest EGP 100; NOSI announces the amounts (2026: notice of 30 November 2025). The contribution rate rises by 1% every seven years from 1 January 2020, split equally between employer and employee, up to a total of 26% (Law 148/2019 Art. 19, last paragraph; Executive Regulations Art. 57): the first step is 1 January 2027 (OAD 12% / 9% → 12.5% / 9.5%), the next is 1 January 2034. Both changes apply from the January contribution month. Worked examples in this guide use the 2026 parameters (EGP 2,700 / 16,700; EE 11%, ER 18.75%).")]),
 (4217, [("11% of monthly insured wage (up to EGP 16,700).", "11% of monthly insured wage (up to EGP 16,700); 11.5% up to EGP 19,300 from 1 January 2027.")]),
 (4218, [("18.75%.", "18.75% (19.25% from 1 January 2027).")]),
]

SHD = '<w:shd w:val="clear" w:color="auto" w:fill="DDEBF7"/>'
DEPOIS_SHD = ("w:fitText", "w:vertAlign", "w:rtl", "w:cs", "w:em", "w:lang", "w:eastAsianLayout", "w:specVanish", "w:oMath")

def sombrear(rpr):
    if rpr is None:
        return "<w:rPr>" + SHD + "</w:rPr>"
    inner = re.sub(r"<w:shd\b[^>]*/>|<w:highlight\b[^>]*/>", "", rpr[len("<w:rPr>"):-len("</w:rPr>")])
    for tag in DEPOIS_SHD:
        m = re.search("<" + tag + r"\b", inner)
        if m:
            return "<w:rPr>" + inner[:m.start()] + SHD + inner[m.start():] + "</w:rPr>"
    return "<w:rPr>" + inner + SHD + "</w:rPr>"

RUN = re.compile(r"<w:r(?:\s[^>]*)?>.*?</w:r>", re.S)
def texto(p): return html.unescape(re.sub(r"<[^>]+>", "", p))

def editar(p, trocas):
    n = 0
    for velho, novo in trocas:
        if velho is None:  # paragrafo inteiro
            runs = RUN.findall(p)
            rpr = next((re.search(r"<w:rPr>.*?</w:rPr>", r, re.S) for r in runs if "<w:t" in r), None)
            rpr = rpr.group(0) if rpr else None
            novo_run = f'<w:r>{sombrear(rpr)}<w:t xml:space="preserve">{html.escape(novo, quote=False)}</w:t></w:r>'
            primeiro = True
            def sub(m):
                nonlocal primeiro
                if primeiro: primeiro = False; return novo_run
                return ""
            p = RUN.sub(sub, p); n += 1; continue
        assert texto(p).count(velho) == 1, f"trecho {velho!r} aparece {texto(p).count(velho)}x"
        feito = False
        for r in RUN.findall(p):
            ts = re.findall(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", r, re.S)
            if len(ts) == 1 and velho in html.unescape(ts[0]):
                t_novo = html.escape(html.unescape(ts[0]).replace(velho, novo), quote=False)
                m = re.search(r"<w:rPr>.*?</w:rPr>", r, re.S)
                r2 = re.sub(r"<w:t(?:\s[^>]*)?>.*?</w:t>", lambda _: f'<w:t xml:space="preserve">{t_novo}</w:t>', r, flags=re.S)
                r2 = r2.replace(m.group(0), sombrear(m.group(0)), 1) if m else re.sub(r"^(<w:r(?:\s[^>]*)?>)", lambda mm: mm.group(1) + sombrear(None), r2)
                p = p.replace(r, r2, 1); feito = True; break
        if not feito:  # trecho atravessa runs: reconstroi o paragrafo com todas as trocas restantes
            t = texto(p)
            for v2, n2 in trocas[trocas.index((velho, novo)):]:
                assert t.count(v2) == 1, f"trecho {v2!r} aparece {t.count(v2)}x"
                t = t.replace(v2, n2)
            p, _ = editar(p, [(None, t)])
            return p, "reconstruido"
        n += 1
    return p, "run"

z = zipfile.ZipFile(BASE)
doc = z.read("word/document.xml").decode("utf8")
P = list(re.finditer(r"<w:p[ >].*?</w:p>", doc, re.S))
saida, pos, log = [], 0, []
idx = {k: t for k, t in ED}
assert len(idx) == len(ED), "indice repetido"
for i, m in enumerate(P):
    if i in idx:
        antes = texto(m.group(0))
        novo, modo = editar(m.group(0), idx[i])
        saida.append(doc[pos:m.start()]); saida.append(novo); pos = m.end()
        log.append((i, modo, antes, texto(novo)))
saida.append(doc[pos:])
novo_doc = "".join(saida)
assert len(log) == len(ED)
for i, modo, a, d in log:
    print(f"[{i}] ({modo})\n  ANTES : {a}\n  DEPOIS: {d}")
print("EDICOES:", len(log))
rodape = z.read("word/footer1.xml").decode("utf8")
VELHO_R = '<w:t xml:space="preserve">EG-CCG-001 v1.1 | Mercans Compliance Regulations Team | 2026</w:t>'
assert rodape.count(VELHO_R) == 1, "rodape diferente do esperado"
rodape = rodape.replace(VELHO_R, VELHO_R.replace("v1.1", "v1.5"))
print("rodape: EG-CCG-001 v1.1 -> v1.5")
if not DRY:
    with zipfile.ZipFile(SAIDA, "w", zipfile.ZIP_DEFLATED) as out:
        for info in z.infolist():
            data = novo_doc.encode("utf8") if info.filename == "word/document.xml" else rodape.encode("utf8") if info.filename == "word/footer1.xml" else z.read(info.filename)
            out.writestr(info, data)
    print("gravado:", SAIDA)
