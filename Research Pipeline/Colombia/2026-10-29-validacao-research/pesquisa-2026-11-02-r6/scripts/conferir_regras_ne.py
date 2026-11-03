"""Conferencia cruzada da contagem de contar_regras_ne.py (metodo independente).

Uso: python -I conferir_regras_ne.py <PDF>
(a) Conta todas as palavras "R"/"N" isoladas na coluna Y (x central a +-12 pt da coluna do cabecalho
    da secao) nas pp. 182-232, sem olhar o ID. Deve dar R+N da contagem por ID (517) se nenhuma
    linha tiver Y sem ID.
(b) Procura, no texto corrido das pp. 182-232, todo token com formato de ID em qualquer posicao e
    lista os unicos por prefixo, para ver se algum ID ficou fora da coluna da esquerda.
"""
import re, sys
from collections import Counter
import pymupdf

doc = pymupdf.open(sys.argv[1])
ycols = []
cnt = Counter()
for pno in range(181, 232):
    pg = doc[pno]
    words = pg.get_text("words")
    fim = [w[1] for w in words if w[4] == "Abreviaturas"]
    limite = min(fim) if fim else 1e9
    hdrs = sorted([w for w in words if w[4] == "Y"], key=lambda w: w[1])
    cx_atual = ycols[-1] if ycols else None
    marcas = [((h[0] + h[2]) / 2, h[1]) for h in hdrs]
    for w in sorted(words, key=lambda w: w[1]):
        if w[1] >= limite:
            break
        acima = [m for m in marcas if m[1] <= w[1]]
        cx = acima[-1][0] if acima else cx_atual
        if cx is None:
            continue
        if w[4] in ("R", "N") and abs((w[0] + w[2]) / 2 - cx) < 12:
            cnt[w[4]] += 1
    if marcas:
        ycols.append(marcas[-1][0])
print("(a) R/N na coluna Y, sem olhar ID:", dict(cnt), "total", sum(cnt.values()))

ID_RE = re.compile(r"\b(VLR\d{2}|NIAE\d{3}[a-z]?|NIE\d{3}[a-z]?|DC\d{2}|Z[A-E]\d{2})\b")
ids = set()
for pno in range(181, 232):
    t = doc[pno].get_text()
    t = t.split("Abreviaturas Utilizadas")[0]
    ids.update(ID_RE.findall(t))
pref = Counter(re.match(r"[A-Z]+", i).group(0) for i in ids)
print("(b) IDs unicos no texto corrido (qualquer posicao):", dict(pref), "total", len(ids), "+ 90 e 92")
