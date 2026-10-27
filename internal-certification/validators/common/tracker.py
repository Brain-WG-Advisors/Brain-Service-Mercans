"""Builds Acompanhamento_Internal_Certification.xlsx (progress tracker) from the package workbooks.
Refuses to overwrite: the tracker is edited by hand after creation. Usage: python -I tracker.py"""
import glob
import os
import sys

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "Acompanhamento_Internal_Certification.xlsx")
if os.path.exists(OUT):
    sys.exit(f"refusing to overwrite {OUT}")

HEAD = PatternFill("solid", fgColor="1F3864")
WHITE = Font(bold=True, color="FFFFFF")
WRAP = Alignment(wrap_text=True, vertical="top")
THIN = Border(*(Side(style="thin", color="BFBFBF"),) * 4)
SEV = {"High": "F8CBAD", "Medium": "FFE699", "Low": "DDEBF7", "Observation": "E2EFDA"}

# key, país, cliente, período, contato, pasta, pass(+reviewed), finding, not tested, recibo, situação, próximo passo
PKG = [
    ("NO-HENKEL", "Noruega", "Henkel Norway AS", "set/26", "Umesh Gaikwad", "Norway/Henkel Norway - 2026-09", 34, 9, 4, "Sim",
     "Fechado", "Cobrar GL 'CORRECTED', dados do carro, termos OTP, nome do sindicato"),
    ("DK-SHERWIN", "Dinamarca", "Sherwin-Williams Denmark A/S", "set/26", "Rakshitha Nagesh",
     "Denmark/Sherwin Williams Denmark - 2026-09", 18, 5, 2, "Sim", "Fechado", "Confirmar o arquivo enviado ao eIndkomst"),
    ("DK-KGS", "Dinamarca", "KGS Fire & Security Danmark ApS", "set/26", "Rakshitha Nagesh",
     "Denmark/KGS Fire & Security Denmark - 2026-09", 15, 5, 4, "Sim", "Fechado", "Tipo do seguro-saúde; master data"),
    ("NL-QUEST", "Holanda", "Quest Software", "set/26", "Athul Satheesh", "Netherlands/Quest Software - 2026-09", 56, 6, 6, "Não",
     "Falta recibo", "Resposta Digipoort; qual arquivo bancário"),
    ("NL-SHERWIN", "Holanda", "Sherwin Williams (Valspar B.V.)", "set/26", "Umesh Gaikwad",
     "Netherlands/Sherwin Williams - 2026-09", 45, 14, 7, "Não", "Falta recibo", "Digipoort do 002879487L01"),
    ("NL-EXCERPTA", "Holanda", "Excerpta Medica", "set/26", "Suresh Jalihal", "Netherlands/Excerpta Medica - 2026-09", 53, 4, 8,
     "Não", "Falta recibo", "Digipoort; mensagens originais de agosto"),
    ("SE-ONEID", "Suécia", "One Identity Sweden AB", "set/26", "Athul Satheesh", "Sweden/Quest Software - 2026-09", 19, 6, 6,
     "Não", "Falta recibo", "Kvittens 559400-9267, master, banco, skattebeslut do Magnus"),
    ("KZ-MASTERCARD", "Cazaquistão", "Mastercard (Rep. office)", "out/26", "Malika Iskakova", "Kazakhstan/Mastercard - 2026-10",
     14, 6, 5, "Não", "Parcial", "Form 200.00 + recibo, YTD do ИПН, GL"),
    ("UA-ALTIUM-08", "Ucrânia", "Altium", "ago/26", "Nataliia Hahan", "Ukraine/Altium - 2026-08", 33, 13, 12, "Parcial",
     "Falta recibo", "XML desempacotado + recibos DPS; recibo do 1-PV"),
    ("UK-MCDERMOTT", "Reino Unido", "McDermott UK", "set/26", "Srikanth Kondam", "United Kingdom/McDermott UK - 2026-09", 50, 4, 17,
     "Não", "Falta recibo", "Resposta HMRC ao FPS/EPS"),
    ("UA-ALTIUM-09", "Ucrânia", "Altium", "set/26", "Nataliia Hahan", "Ukraine/Altium - 2026-09", 9, 4, 7, "Não", "Parcial",
     "Report de setembro quando for preparado"),
    ("AZ", "Azerbaijão", "A confirmar", "set/26", "Pari Azizzade", None, 0, 0, 0, "Não", "Pulado",
     "Autorização do Wallisson para abrir o zip"),
    ("FI", "Finlândia", "-", "-", "Marju Martinson", None, 0, 0, 0, "Não", "Sem arquivos", "Cobrar a Marju"),
    ("EE", "Estônia", "-", "-", "Marju Martinson", None, 0, 0, 0, "Não", "Sem arquivos", "Cobrar a Marju"),
    ("IE", "Irlanda", "-", "-", "(sem SBC)", None, 0, 0, 0, "Não", "Sem SBC", "Definir SBC com Manju/Marko"),
    ("RU", "Rússia", "-", "-", "Sadaf Nishat", None, 0, 0, 0, "Não", "Sem contato", "Obter contato via Sadaf"),
]

ACOES = [
    ("A-01", "Configuração", "NO", "Contribuição sindical (21126): deduzir da base do forskuddstrekk e informar como fradrag "
     "'fagforeningskontingent' na A-melding. Revisar todos os clientes NO com sindicato.", "NO-HENKEL F-01",
     "Implementation / dev", "Pendente"),
    ("A-02", "Configuração", "DK", "Seguro-saúde do empregador: tributar (0013) e informar no campo 0026, como a Sherwin já faz. "
     "Revisar todos os clientes DK.", "DK-KGS F-01", "Implementation / dev", "Pendente"),
    ("A-03", "Configuração", "DK", "Indenização (fratrædelsesgodtgørelse): campo 0069 com o valor bruto, antes dos 8.000 kr.",
     "DK-SHERWIN F-01", "Implementation / dev", "Pendente"),
    ("A-04", "Configuração", "SE", "Payout de férias acumuladas (79421): reter pela tabela de engångsbelopp (SFL 11 kap. 17 §).",
     "SE-ONEID F-02", "Implementation / dev", "Aguarda decisão Wallisson"),
    ("A-05", "Configuração", "DK", "Base do Store Bededag 0,45% e do ferietillæg (Sherwin x KGS diferentes).",
     "DK-SHERWIN F-03/F-04", "Implementation / Compliance", "Aguarda decisão Wallisson"),
    ("A-06", "Contracheque", "NO/DK/SE/KZ", "Templates de contracheque: renda tributável sem benefícios (NO), sem CPR e cálculo "
     "zerado no desligado (DK KGS), imposto acumulado = período (SE), totais errados (KZ).",
     "NO F-02, DK-KGS F-02, SE F-03, KZ F-02", "Implementation / dev", "Pendente"),
    ("A-07", "Processo", "Todos", "Pedir às SBCs o arquivo exatamente como enviado + recibo da autoridade em todo pacote.",
     "DK-SHERWIN F-02, NL, SE, UK", "Compliance", "Pendente"),
    ("C-01", "Cobrança", "NO", "Umesh: GL 'CORRECTED', dados do carro, termos OTP, sindicato",
     "Norway/.../02 Validation/followups.md", "Umesh Gaikwad", "Rascunho"),
    ("C-02", "Cobrança", "DK", "Rakshitha: arquivo enviado ao eIndkomst (Sherwin)",
     "Denmark/Sherwin.../followups.md", "Rakshitha Nagesh", "Rascunho"),
    ("C-03", "Cobrança", "DK", "Rakshitha: tipo do seguro-saúde e master data (KGS)", "Denmark/KGS.../followups.md",
     "Rakshitha Nagesh", "Rascunho"),
    ("C-04", "Cobrança", "SE", "Athul: Kvittens 559400-9267, master One Identity, banco, skattebeslut do Magnus",
     "Sweden/.../followups.md", "Athul Satheesh", "Rascunho"),
    ("C-05", "Cobrança", "KZ", "Malika: 200.00 do 3º tri + recibo, YTD do ИПН, pedido de dedução básica, GL",
     "Kazakhstan/.../followups.md", "Malika Iskakova", "Rascunho"),
    ("C-06", "Cobrança", "NL", "Umesh: resposta Digipoort do 002879487L01 (Sherwin NL)", "PLANO §2", "Umesh Gaikwad", "A verificar"),
    ("C-07", "Cobrança", "NL", "Suresh: mensagens originais de agosto (Excerpta)", "PLANO §2", "Suresh Jalihal", "A verificar"),
    ("C-08", "Cobrança", "NL", "Athul: qual arquivo bancário (Quest NL)", "PLANO §2", "Athul Satheesh", "A verificar"),
    ("C-09", "Cobrança", "UK", "Srikanth: resposta HMRC ao FPS/EPS", "PLANO §2", "Srikanth Kondam", "A verificar"),
    ("C-10", "Cobrança", "UA", "Nataliia: recibo do 1-PV; D1 de julho", "PLANO §2", "Nataliia Hahan", "A verificar"),
    ("C-11", "Cobrança", "FI/EE", "Marju: pacote da Finlândia e da Estônia (2ª cobrança, cópia Manju)", "PLANO §3",
     "Marju Martinson", "A fazer"),
    ("C-12", "Cobrança", "RU", "Sadaf: contato para a Rússia", "PLANO §3", "Sadaf Nishat", "A fazer"),
    ("C-13", "Decisão", "IE", "Definir SBC da Irlanda", "PLANO §3", "Manju Shetija / Marko Taylor", "A fazer"),
    ("D-01", "Decisão", "AZ", "Autorizar abrir o zip do Azerbaijão (senha no e-mail)", "PLANO §4", "Wallisson Gomes", "A fazer"),
    ("D-02", "Decisão", "SE", "Confirmar leitura da SFL 11:17 para o payout de férias (A-04)", "SE-ONEID F-02", "Wallisson Gomes",
     "A fazer"),
    ("D-03", "Decisão", "DK", "Confirmar base do Store Bededag/ferietillæg (A-05)", "DK-SHERWIN F-03/F-04", "Wallisson Gomes",
     "A fazer"),
]


def findings_of(folder):
    wbp = glob.glob(os.path.join(ROOT, folder, "02 Validation", "*_Validation.xlsx"))
    if not wbp:
        return []
    ws = load_workbook(wbp[0], read_only=True)["Findings Register"]
    rows = list(ws.iter_rows(values_only=True))
    hi = next(i for i, r in enumerate(rows) if r and r[0] == "ID")
    hdr = list(rows[hi])
    out = []
    for r in rows[hi + 1:]:
        if not r or not r[0]:
            continue
        d = dict(zip(hdr, r))
        out.append(d)
    return out


def style_header(ws, row, ncol):
    for c in range(1, ncol + 1):
        cell = ws.cell(row=row, column=c)
        cell.font, cell.fill, cell.alignment, cell.border = WHITE, HEAD, WRAP, THIN


wb = Workbook()

# ---------------- Achados ----------------
wa = wb.active
wa.title = "Achados"
wa["A1"] = "Achados de todos os pacotes (origem: Findings Register de cada workbook) - atualize Status/Responsável/Data"
wa["A1"].font = Font(bold=True, size=12)
ah = ["Pacote", "ID", "Severidade", "Área", "Achado", "Impacto", "Base legal", "Status", "Responsável", "Data status",
      "Comentário"]
wa.append([])
wa.append(ah)
style_header(wa, 3, len(ah))
for p in PKG:
    if not p[5]:
        continue
    for d in findings_of(p[5]):
        wa.append([p[0], d.get("ID"), d.get("Severity"), d.get("Area"), d.get("Finding"), d.get("Impact"),
                   d.get("Statutory basis"), "Aberto", "", "", ""])
last_a = wa.max_row
for i, w in enumerate([15, 7, 12, 24, 80, 34, 34, 14, 18, 12, 30], 1):
    wa.column_dimensions[get_column_letter(i)].width = w
for row in wa.iter_rows(min_row=4, max_row=last_a):
    for c in row:
        c.alignment, c.border = WRAP, THIN
    f = SEV.get(row[2].value)
    if f:
        row[2].fill = PatternFill("solid", fgColor=f)
dv = DataValidation(type="list", formula1='"Aberto,Em correção,Corrigido,Aceito pelo cliente,Descartado"', allow_blank=True)
wa.add_data_validation(dv)
dv.add(f"H4:H{last_a + 200}")
wa.freeze_panes = "A4"
wa.auto_filter.ref = f"A3:K{last_a}"
for st, col in (("Corrigido", "C6EFCE"), ("Em correção", "FFEB9C"), ("Aberto", "FFC7CE")):
    wa.conditional_formatting.add(f"H4:H{last_a + 200}",
                                  CellIsRule(operator="equal", formula=[f'"{st}"'], fill=PatternFill("solid", fgColor=col)))

# ---------------- Painel ----------------
wp = wb.create_sheet("Painel", 0)
wp["A1"] = "Internal Certification - Reports | Painel de avanço"
wp["A1"].font = Font(bold=True, size=14)
wp["A2"] = ("Cobertura = controles executados ÷ (executados + Not tested). Contagens de achados por fórmula a partir da aba "
            "Achados. Atualize as colunas de controles quando um pacote for revalidado.")
wp["A2"].alignment = WRAP
wp.merge_cells("A2:R2")
wp.row_dimensions[2].height = 30
ph = ["Pacote", "País", "Cliente", "Período", "Contato (SBC)", "Pass", "Finding", "Not tested", "Cobertura",
      "Recibo prova aceite?", "High abertos", "Medium abertos", "Low abertos", "Obs abertas", "Achados abertos",
      "Achados corrigidos", "Situação", "Próximo passo"]
wp.append([])
wp.append(ph)
style_header(wp, 4, len(ph))
r0 = 5
for i, p in enumerate(PKG):
    r = r0 + i
    k = p[0]
    rng = f"Achados!$A$4:$A${last_a + 200}"
    sev = f"Achados!$C$4:$C${last_a + 200}"
    st = f"Achados!$H$4:$H${last_a + 200}"
    vals = [k, p[1], p[2], p[3], p[4], p[6], p[7], p[8], f"=IFERROR((F{r}+G{r})/(F{r}+G{r}+H{r}),0)", p[9]]
    vals += [f'=COUNTIFS({rng},$A{r},{sev},"{s}",{st},"<>Corrigido",{st},"<>Descartado")'
             for s in ("High", "Medium", "Low", "Observation")]
    vals += [f'=COUNTIFS({rng},$A{r},{st},"<>Corrigido",{st},"<>Descartado")', f'=COUNTIFS({rng},$A{r},{st},"Corrigido")',
             p[10], p[11]]
    wp.append(vals)
rl = r0 + len(PKG) - 1
tr = rl + 1
wp.append(["TOTAL", f'=COUNTA(B{r0}:B{rl})&" pacotes/países"', "", "", "", f"=SUM(F{r0}:F{rl})", f"=SUM(G{r0}:G{rl})",
           f"=SUM(H{r0}:H{rl})", f"=IFERROR((F{tr}+G{tr})/(F{tr}+G{tr}+H{tr}),0)", f'=COUNTIF(J{r0}:J{rl},"Sim")&" com aceite"',
           f"=SUM(K{r0}:K{rl})", f"=SUM(L{r0}:L{rl})", f"=SUM(M{r0}:M{rl})", f"=SUM(N{r0}:N{rl})", f"=SUM(O{r0}:O{rl})",
           f"=SUM(P{r0}:P{rl})", f'=COUNTIF(Q{r0}:Q{rl},"Fechado")&" fechados"', ""])
for c in wp[tr]:
    c.font = Font(bold=True)
    c.border = THIN
for i, w in enumerate([15, 13, 30, 9, 18, 7, 8, 10, 11, 12, 9, 9, 9, 9, 10, 10, 14, 55], 1):
    wp.column_dimensions[get_column_letter(i)].width = w
for row in wp.iter_rows(min_row=r0, max_row=tr):
    for c in row:
        c.border = THIN
        c.alignment = Alignment(vertical="top", wrap_text=True)
    row[8].number_format = "0%"
wp.conditional_formatting.add(f"I{r0}:I{rl}", ColorScaleRule(start_type="num", start_value=0, start_color="F8696B",
                                                             mid_type="num", mid_value=0.7, mid_color="FFEB84",
                                                             end_type="num", end_value=1, end_color="63BE7B"))
wp.conditional_formatting.add(f"K{r0}:K{rl}", CellIsRule(operator="greaterThan", formula=["0"],
                                                         fill=PatternFill("solid", fgColor="F8CBAD")))
dvs = DataValidation(type="list", formula1='"Fechado,Falta recibo,Parcial,Em validação,Pulado,Sem arquivos,Sem SBC,Sem contato"',
                     allow_blank=True)
dvr = DataValidation(type="list", formula1='"Sim,Não,Parcial"', allow_blank=True)
wp.add_data_validation(dvs)
wp.add_data_validation(dvr)
dvs.add(f"Q{r0}:Q{rl}")
dvr.add(f"J{r0}:J{rl}")
for st, col in (("Fechado", "C6EFCE"), ("Falta recibo", "FFEB9C"), ("Parcial", "FFEB9C")):
    wp.conditional_formatting.add(f"Q{r0}:Q{rl}", CellIsRule(operator="equal", formula=[f'"{st}"'],
                                                             fill=PatternFill("solid", fgColor=col)))
wp.freeze_panes = "B5"

# ---------------- Ações ----------------
wc = wb.create_sheet("Ações", 2)
wc["A1"] = "Ações: configuração (implementation), cobranças às SBCs e decisões pendentes"
wc["A1"].font = Font(bold=True, size=12)
ch = ["ID", "Tipo", "País", "Ação", "Origem", "Responsável", "Status", "Data", "Comentário"]
wc.append([])
wc.append(ch)
style_header(wc, 3, len(ch))
for a in ACOES:
    wc.append(list(a) + ["", ""])
lc = wc.max_row
for i, w in enumerate([7, 13, 11, 80, 30, 26, 22, 12, 30], 1):
    wc.column_dimensions[get_column_letter(i)].width = w
for row in wc.iter_rows(min_row=4, max_row=lc):
    for c in row:
        c.alignment, c.border = WRAP, THIN
dva = DataValidation(type="list", formula1='"A fazer,Rascunho,Aprovado para envio,Enviado,Recebido,Pendente,Em andamento,'
                                         'Concluído,A verificar,Aguarda decisão Wallisson"', allow_blank=True)
wc.add_data_validation(dva)
dva.add(f"G4:G{lc + 100}")
for st, col in (("Concluído", "C6EFCE"), ("Recebido", "C6EFCE"), ("Rascunho", "FFEB9C"), ("Aguarda decisão Wallisson", "F8CBAD")):
    wc.conditional_formatting.add(f"G4:G{lc + 100}", CellIsRule(operator="equal", formula=[f'"{st}"'],
                                                                fill=PatternFill("solid", fgColor=col)))
wc.freeze_panes = "A4"
wc.auto_filter.ref = f"A3:I{lc}"

# ---------------- Legenda ----------------
wl = wb.create_sheet("Legenda")
rows = [
    ("Legenda", ""),
    ("Cobertura", "Controles executados (Pass, Pass reviewed, Finding) ÷ (executados + itens Not tested). Out of scope fica fora."),
    ("Recibo prova aceite?", "Sim = recibo/confirmação da autoridade é do mesmo report (identificadores conferidos)."),
    ("High", "Valor retido/declarado errado, ou sem prova de aceite do report."),
    ("Medium", "Campo do report ou documento ao cliente errado sem mover dinheiro no período."),
    ("Low", "Apresentação ou arredondamento."),
    ("Observation", "Precisa de confirmação do cliente/método antes de classificar."),
    ("Situação 'Fechado'", "Validação concluída com prova de aceite; achados podem continuar abertos (aba Achados)."),
    ("Fonte dos números", "Workbooks em <País>/<Cliente>/02 Validation/*_Validation.xlsx, gerados em 14-10-2026."),
]
for r in rows:
    wl.append(r)
wl["A1"].font = Font(bold=True, size=12)
wl.column_dimensions["A"].width = 22
wl.column_dimensions["B"].width = 110
for row in wl.iter_rows(min_row=2):
    row[0].font = Font(bold=True)
    for c in row:
        c.alignment = WRAP

wb.save(OUT)
print("written", OUT, "| findings:", last_a - 3, "| actions:", len(ACOES))
