"""Busca local por trecho no material longo do cérebro (RAG local, decidido em 2026-10-28).

Uso:  python scripts/buscar.py "<pergunta ou termos>" [-n 8] [--fonte reunioes|oficiais|tickets|chats|extracoes] [--reindexar]
      ex.: python scripts/buscar.py "Lithuania BAU validation SIR" --fonte reunioes
           python scripts/buscar.py "Marko automatic submission government" -n 10

Para que serve: em vez de ler o arquivo inteiro (transcrição, lei, ticket), achar os trechos certos
e abrir só eles. Devolve arquivo:linha + trecho; o bloco de prova continua exigindo ler a fonte citada.

Indexa (só leitura): raw/reunioes, raw/docs/oficiais, raw/tickets/api (só os .md; ticket repetido em
várias datas → vale a coleta mais nova; anexos fora), raw/chats e extracoes/.
Nunca entra: 02-client-reports-raw/, 99-local-only/, .env.
Tudo roda na máquina (BM25 em Python puro, sem rede, sem modelo). O índice fica em .busca/ (fora do git)
e é refeito só para arquivos novos ou alterados.
Dica: as reuniões e os tickets estão quase todos em inglês; buscar com os termos em inglês.
"""
import argparse
import html
import math
import os
import pickle
import re
import sys
import unicodedata
import zipfile
from collections import Counter

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(RAIZ, ".busca", "indice.pkl")
VERSAO_INDICE = 1

FONTES = {
    "reunioes": ("raw/reunioes", {".txt", ".md", ".pdf", ".docx"}),
    "oficiais": ("raw/docs/oficiais", {".txt", ".md", ".pdf", ".html", ".htm", ".xsd"}),
    "tickets": ("raw/tickets/api", {".md"}),
    "chats": ("raw/chats", {".txt", ".md"}),
    "extracoes": ("extracoes", {".md"}),
}
PROIBIDO = ("02-client-reports-raw", "99-local-only", ".env")
JANELA, PASSO = 12, 8  # linhas por trecho e avanço (sobreposição de 4)

STOP = set("""a o e é de da do das dos em no na nos nas um uma uns umas para por com sem que se ao aos à às
ou como mais mas foi ser são está esta isso este essa esse já não sim the of and to in is it that for on
with as at by be this are was or an from we you they he she i so if do not have has had will can just
yeah okay ok um uh like know""".split())


def norma(txt):
    txt = unicodedata.normalize("NFKD", txt.lower())
    return "".join(c for c in txt if not unicodedata.combining(c))


def termos(txt):
    out = []
    for t in re.findall(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*", norma(txt)):
        if t in STOP or len(t) < 2:
            continue
        if len(t) > 4 and t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]
        out.append(t)
    return out


def ler(caminho):
    ext = os.path.splitext(caminho)[1].lower()
    try:
        if ext == ".pdf":
            import pymupdf as fitz
            fitz.TOOLS.mupdf_display_errors(False)
            with fitz.open(caminho) as doc:
                return [l for p in doc for l in p.get_text().splitlines()]
        if ext == ".docx":
            if os.path.exists(os.path.splitext(caminho)[0] + ".txt"):
                return []  # o .txt extraído ao lado já entra
            with zipfile.ZipFile(caminho) as z:
                xml = z.read("word/document.xml").decode("utf-8", "ignore")
            xml = re.sub(r"</w:p>", "\n", xml)
            return html.unescape(re.sub(r"<[^>]+>", "", xml)).splitlines()
        with open(caminho, encoding="utf-8", errors="ignore") as f:
            txt = f.read()
        if ext in (".html", ".htm"):
            txt = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", txt)
            txt = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>|</li>", "\n", txt)
            txt = html.unescape(re.sub(r"<[^>]+>", " ", txt))
        return txt.splitlines()
    except Exception as e:  # arquivo ilegível não derruba a busca
        print(f"  (pulei {os.path.relpath(caminho, RAIZ)}: {e.__class__.__name__})", file=sys.stderr)
        return []


def arquivos():
    """(fonte, caminho relativo) de tudo que entra no índice."""
    vistos_ticket = {}
    for fonte, (pasta, exts) in FONTES.items():
        base = os.path.join(RAIZ, pasta)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if d not in PROIBIDO and d != "anexos")
            for nome in sorted(filenames):
                if os.path.splitext(nome)[1].lower() not in exts or any(p in nome for p in PROIBIDO):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, nome), RAIZ).replace("\\", "/")
                if fonte == "tickets":
                    vistos_ticket[nome] = rel  # pastas em ordem de data: a última coleta vence
                    continue
                yield fonte, rel
    for rel in vistos_ticket.values():
        yield "tickets", rel


def trechos(linhas):
    linhas = [l.rstrip() for l in linhas]
    n = len(linhas)
    for i in range(0, max(n, 1), PASSO):
        bloco = linhas[i:i + JANELA]
        txt = "\n".join(bloco).strip()
        if txt:
            yield i + 1, txt
        if i + JANELA >= n:
            break


def carregar_indice(reindexar):
    idx = None
    if not reindexar and os.path.exists(CACHE):
        try:
            with open(CACHE, "rb") as f:
                idx = pickle.load(f)
            if idx.get("versao") != VERSAO_INDICE:
                idx = None
        except Exception:
            idx = None
    idx = idx or {"versao": VERSAO_INDICE, "arquivos": {}}
    atuais, mudou = {}, False
    for fonte, rel in arquivos():
        mtime = os.path.getmtime(os.path.join(RAIZ, rel))
        antigo = idx["arquivos"].get(rel)
        if antigo and antigo["mtime"] == mtime:
            atuais[rel] = antigo
            continue
        mudou = True
        partes = [(ln, txt, Counter(termos(txt))) for ln, txt in trechos(ler(os.path.join(RAIZ, rel)))]
        atuais[rel] = {"fonte": fonte, "mtime": mtime, "trechos": partes}
    if mudou or set(atuais) != set(idx["arquivos"]):
        idx["arquivos"] = atuais
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        with open(CACHE, "wb") as f:
            pickle.dump(idx, f)
    return idx


def buscar(idx, consulta, n, fonte):
    q = list(dict.fromkeys(termos(consulta)))
    if not q:
        return []
    docs = [(rel, a, ln, txt, tf) for rel, a in idx["arquivos"].items() if not fonte or a["fonte"] == fonte
            for ln, txt, tf in a["trechos"]]
    if not docs:
        return []
    N = len(docs)
    media = sum(sum(d[4].values()) for d in docs) / N
    df = Counter(t for d in docs for t in q if t in d[4])
    k1, b = 1.4, 0.75
    res = []
    for rel, a, ln, txt, tf in docs:
        dl = sum(tf.values())
        s, achados = 0.0, 0
        for t in q:
            f = tf.get(t)
            if not f:
                continue
            achados += 1
            idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
            s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * dl / media))
        if s:
            res.append((s * (1 + achados / len(q)), rel, ln, txt))  # premia trecho que cobre mais termos
    res.sort(key=lambda r: -r[0])
    saida, por_arquivo = [], Counter()
    for r in res:  # no máximo 2 trechos por arquivo, para variar as fontes
        if por_arquivo[r[1]] < 2:
            saida.append(r)
            por_arquivo[r[1]] += 1
        if len(saida) == n:
            break
    return saida


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description="Busca local por trecho (reuniões, leis, tickets, chats, extrações).")
    ap.add_argument("consulta")
    ap.add_argument("-n", type=int, default=8)
    ap.add_argument("--fonte", choices=sorted(FONTES))
    ap.add_argument("--reindexar", action="store_true")
    a = ap.parse_args()
    idx = carregar_indice(a.reindexar)
    total = sum(len(x["trechos"]) for x in idx["arquivos"].values())
    print(f"Índice: {len(idx['arquivos'])} arquivos, {total} trechos.  Consulta: {a.consulta}\n")
    res = buscar(idx, a.consulta, a.n, a.fonte)
    if not res:
        print("Nada encontrado. Tente sinônimos ou os termos em inglês.")
    for i, (s, rel, ln, txt) in enumerate(res, 1):
        corpo = re.sub(r"\n{2,}", "\n", txt)
        corpo = corpo if len(corpo) <= 700 else corpo[:700] + " …"
        print(f"{i}. {rel}:{ln}  (pontos {s:.1f})")
        print("   " + corpo.replace("\n", "\n   ") + "\n")


if __name__ == "__main__":
    main()
