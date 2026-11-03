"""Conta as regras de validacao do Anexo Tecnico NE v1.0 (DIAN, Res. 000013/2021), cap. 6.

Uso:  python -I contar_regras_ne.py <caminho do PDF> [--detalhe]

Metodo (reprodutivel, por posicao das palavras, PyMuPDF):
  1. Percorre as paginas 182-232 (indice 181-231).
  2. Secao corrente = ultimo titulo visto ("Se informa la incorporacion", 6.1.1, 6.1.2, 6.1.3, 6.2).
  3. Em cada pagina acha a coluna "Y" do cabecalho da tabela (palavra "Y" isolada).
  4. Uma regra = palavra na coluna da esquerda que casa com o padrao de ID
     (90, 92, VLR01, NIE..., NIAE..., DC.., ZA..-ZE..).
  5. A faixa vertical da regra vai do topo do ID ate o topo do proximo ID (ou o fim da pagina).
     Dentro da faixa, procura a palavra "R" ou "N" sozinha cuja coluna (x) cai na coluna "Y".
  6. Conta IDs unicos por secao e o valor de Y (R, N ou vazio).
Saida: tabela por secao e totais; com --detalhe, lista os IDs sem R/N e os duplicados.
"""
import re
import sys
from collections import OrderedDict

import pymupdf

ID_RE = re.compile(r"^(90|92|VLR\d{2}|NIE\d{3}[a-z]?|NIAE\d{3}[a-z]?|DC\d{2}[a-z]?|Z[A-E]\d{2})$")

SECOES = [
    ("geral", re.compile(r"Se informa la incorporaci")),
    ("6.1.1 NominaIndividual", re.compile(r"^6\.1\.1\.")),
    ("6.1.2 NominaIndividualDeAjuste", re.compile(r"^6\.1\.2\.")),
    ("6.1.3 ds:Signature", re.compile(r"^6\.1\.3\.")),
    ("6.2 Conexao", re.compile(r"^6\.2\.")),
]
FIM = re.compile(r"^Abreviaturas Utilizadas")


def linhas(page):
    """Linhas do texto com a coordenada y do topo, na ordem de leitura."""
    out = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            if txt:
                out.append((ln["bbox"][1], txt))
    return out


def main(pdf, detalhe=False):
    doc = pymupdf.open(pdf)
    secao = None
    regras = OrderedDict((s, OrderedDict()) for s, _ in SECOES)
    duplicados = []
    ultimo_cx = None  # coluna Y herdada quando a pagina nao repete o cabecalho
    for pno in range(181, 232):  # paginas 182..232
        page = doc[pno]
        # marcos de secao nesta pagina (y, nome)
        marcos = []
        fim_y = None
        for y, t in linhas(page):
            for nome, rx in SECOES:
                if rx.search(t):
                    if nome == "6.2 Conexao" and not t.startswith("6.2. "):
                        continue
                    marcos.append((y, nome))
            if FIM.search(t):
                fim_y = y
        words = page.get_text("words")  # x0,y0,x1,y1,word,block,line,wno
        ys = [w for w in words if w[4] == "Y"]
        ids = sorted([w for w in words if ID_RE.match(w[4]) and w[0] < 120], key=lambda w: w[1])
        if fim_y is not None:
            ids = [w for w in ids if w[1] < fim_y]
        for i, w in enumerate(ids):
            top = w[1] - 2
            bot = ids[i + 1][1] - 2 if i + 1 < len(ids) else page.rect.height
            # secao: ultimo marco acima deste ID (ou a secao herdada da pagina anterior)
            sec_aqui = secao
            for my, nome in marcos:
                if my <= w[1]:
                    sec_aqui = nome
            # coluna Y: cabecalho "Y" mais proximo acima do ID
            hdr = [h for h in ys if h[1] < w[1]]
            if hdr:
                yh = max(hdr, key=lambda h: h[1])
            else:
                yh = None  # sem cabecalho acima do ID nesta pagina: herda a coluna anterior
            flag = ""
            cx = (yh[0] + yh[2]) / 2 if yh is not None else ultimo_cx
            if cx is not None:
                ultimo_cx = cx
                cands = [v for v in words if v[4] in ("R", "N") and top <= v[1] < bot
                         and abs((v[0] + v[2]) / 2 - cx) < 12]
                if cands:
                    flag = sorted(cands, key=lambda v: v[1])[0][4]
            if sec_aqui is None:
                continue
            bucket = regras[sec_aqui]
            if w[4] in bucket:
                duplicados.append((sec_aqui, w[4], pno + 1))
                if not bucket[w[4]][0] and flag:
                    bucket[w[4]] = (flag, pno + 1)
            else:
                bucket[w[4]] = (flag, pno + 1)
        # secao herdada para a proxima pagina
        if marcos:
            secao = marcos[-1][1]

    tot = {"n": 0, "R": 0, "N": 0, "": 0}
    print(f"{'Secao':34} {'Regras':>6} {'R':>5} {'N':>5} {'sem Y':>6}")
    for sec, b in regras.items():
        c = {"R": 0, "N": 0, "": 0}
        for f, _ in b.values():
            c[f] += 1
        print(f"{sec:34} {len(b):>6} {c['R']:>5} {c['N']:>5} {c['']:>6}")
        tot["n"] += len(b)
        for k in c:
            tot[k] += c[k]
    print(f"{'TOTAL':34} {tot['n']:>6} {tot['R']:>5} {tot['N']:>5} {tot['']:>6}")
    if detalhe:
        for sec, b in regras.items():
            sem = [(k, p) for k, (f, p) in b.items() if not f]
            nn = [(k, p) for k, (f, p) in b.items() if f == "N"]
            if sem:
                print(f"\n[{sec}] sem R/N: {sem}")
            if nn:
                print(f"[{sec}] N: {[k for k, _ in nn]}")
        print(f"\nIDs repetidos dentro da mesma secao: {duplicados}")


if __name__ == "__main__":
    main(sys.argv[1], "--detalhe" in sys.argv)
