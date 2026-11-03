"""Radar de esquecidos: pendências abertas no cérebro, por idade e dono.

Fontes:
- paises/*.md: linhas "- [ ]" (pendências abertas dos hubs);
- frentes/*/estado.md: itens das seções "Esperando ..." e "Em andamento";
- ESTADO.md: itens das seções "Esperando o usuário" e "Em aberto".

Idade = dias desde que a linha entrou no git (git blame); linha ainda não
commitada conta como 0 dias. Para cada ticket citado (ex.: HRBS-16407), mostra
a última data em que ele aparece no log.md ("último movimento").

Uso: python scripts/radar_esquecidos.py [--dias 7] [--saida paineis/radar.md]
Só lê; grava apenas o relatório.
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
HOJE = dt.date.today()
TICKET = re.compile(r"\b(?:HRBS|CT|SR|CT-A|XVP|HRBSD)-\d{2,6}\b")
DATA_LOG = re.compile(r"^\s*-?\s*(\d{4}-\d{2}-\d{2})")
RESOLVIDO = re.compile(r"resolvid|fechad|conclu[íi]d|enviad[oa] pelo|publicad|superad|obsolet", re.I)
VOCE = re.compile(r"Wallisson|usu[áa]rio", re.I)
SECOES_FRENTE = re.compile(r"esperando|em andamento", re.I)
SECOES_ESTADO = re.compile(r"esperando o usu|em aberto", re.I)


def idades_por_linha(arquivo: Path) -> dict[int, dt.date]:
    """Linha (1-based) -> data em que entrou no git; vazio se o arquivo não está no git."""
    try:
        saida = subprocess.run(
            ["git", "blame", "--line-porcelain", "--", str(arquivo.relative_to(RAIZ))],
            cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace", check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return {}
    datas, linha_atual = {}, None
    for ln in saida.splitlines():
        partes = ln.split()
        if len(partes) >= 3 and re.fullmatch(r"[0-9a-f]{40}", partes[0]):
            linha_atual = int(partes[2])
        elif ln.startswith("author-time ") and linha_atual is not None:
            datas[linha_atual] = dt.date.fromtimestamp(int(ln.split()[1]))
    return datas


def limpar(texto: str, n: int = 170) -> str:
    texto = re.sub(r"^\s*- (\[ \] )?", "", texto).replace("**", "").replace("|", "/").strip()
    return texto if len(texto) <= n else texto[: n - 1] + "…"


def coletar() -> list[dict]:
    itens = []

    for hub in sorted((RAIZ / "paises").glob("*.md")):
        datas = idades_por_linha(hub)
        for i, ln in enumerate(hub.read_text(encoding="utf-8").splitlines(), 1):
            if re.match(r"^\s*- \[ \]", ln):
                itens.append({"onde": f"paises/{hub.name}", "linha": i, "texto": ln,
                              "data": datas.get(i, HOJE), "secao": "Pendências"})

    fontes = [(p, SECOES_FRENTE) for p in sorted((RAIZ / "frentes").glob("*/estado.md"))]
    fontes.append((RAIZ / "ESTADO.md", SECOES_ESTADO))
    for arq, filtro in fontes:
        datas = idades_por_linha(arq)
        secao, dentro = "", False
        for i, ln in enumerate(arq.read_text(encoding="utf-8").splitlines(), 1):
            if ln.startswith("#"):
                secao = ln.lstrip("# ").strip()
                dentro = bool(filtro.search(secao)) and not secao.lower().startswith("instru")
                continue
            if dentro and re.match(r"^- ", ln) and not re.match(r"^- \[x\]", ln, re.I) and "✅ fechada" not in ln:
                itens.append({"onde": str(arq.relative_to(RAIZ)).replace("\\", "/"), "linha": i,
                              "texto": ln, "data": datas.get(i, HOJE), "secao": secao})
    return itens


def ultimo_movimento() -> dict[str, dt.date]:
    mov = {}
    for ln in (RAIZ / "log.md").read_text(encoding="utf-8").splitlines():
        m = DATA_LOG.match(ln)
        if not m:
            continue
        try:
            d = dt.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        for t in set(TICKET.findall(ln)):
            mov[t] = max(mov.get(t, d), d)
    return mov


def dono(item: dict) -> str:
    sec = item["secao"].lower()
    if "esperando o usu" in sec or "esperando ação" in sec or "em aberto" in sec:
        return "você"
    if "esperando outros" in sec:
        return "outros"
    if VOCE.search(item["texto"].split(" — ")[-1]) or VOCE.search(item["texto"][-60:]):
        return "você"
    return "outros/sem dono"


def faixa(dias: int) -> str:
    if dias > 30:
        return "Mais de 30 dias"
    if dias > 14:
        return "15 a 30 dias"
    if dias >= 7:
        return "7 a 14 dias"
    return "Menos de 7 dias"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7, help="idade mínima para entrar no radar (padrão 7)")
    ap.add_argument("--saida", default="paineis/radar.md")
    a = ap.parse_args()

    mov = ultimo_movimento()
    itens = coletar()
    for it in itens:
        it["dias"] = (HOJE - it["data"]).days
        it["dono"] = dono(it)
        tks = sorted(set(TICKET.findall(it["texto"])))
        it["tickets"] = tks
        ultimos = [mov[t] for t in tks if t in mov]
        it["mov"] = max(ultimos) if ultimos else None

    velhos = [i for i in itens if i["dias"] >= a.dias]
    ordem = ["Mais de 30 dias", "15 a 30 dias", "7 a 14 dias"]
    linhas = [
        f"# Radar de esquecidos — {HOJE.isoformat()}",
        "",
        f"Pendências abertas no cérebro: **{len(itens)}**. Paradas há {a.dias}+ dias: **{len(velhos)}** "
        f"(você: {sum(i['dono'] == 'você' for i in velhos)}; outros/sem dono: {sum(i['dono'] != 'você' for i in velhos)}).",
        "",
        "Idade = desde que a linha entrou no cérebro (git). \"Mov.\" = última vez que o ticket aparece no log.",
        "Para fechar: marcar `- [x]` no hub (ou tirar do estado.md) com o desfecho; se não vale mais, escrever o porquê.",
        "",
    ]
    for quem in ["você", "outros/sem dono"]:
        grupo = [i for i in velhos if i["dono"] == quem]
        if not grupo:
            continue
        linhas += [f"## Esperando {'você' if quem == 'você' else 'outros ou sem dono'} ({len(grupo)})", ""]
        for f in ordem:
            sub = sorted([i for i in grupo if faixa(i["dias"]) == f], key=lambda i: -i["dias"])
            if not sub:
                continue
            linhas += [f"### {f} ({len(sub)})", "", "| Dias | Onde | Pendência | Mov. |", "|---|---|---|---|"]
            for i in sub:
                movtxt = f"{i['mov']:%d/%m}" if i["mov"] else "—"
                marca = " ⚠️ parece resolvida: conferir e marcar [x]" if RESOLVIDO.search(i["texto"]) else ""
                linhas.append(f"| {i['dias']} | {i['onde']}:{i['linha']} | {limpar(i['texto'])}{marca} | {movtxt} |")
            linhas.append("")

    por_lugar = {}
    for i in velhos:
        por_lugar[i["onde"]] = por_lugar.get(i["onde"], 0) + 1
    linhas += ["## Onde se acumulam", "", "| Arquivo | Paradas |", "|---|---|"]
    linhas += [f"| {k} | {v} |" for k, v in sorted(por_lugar.items(), key=lambda kv: -kv[1])[:15]]

    saida = RAIZ / a.saida
    saida.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    print(f"  parecem resolvidas (só falta marcar): {sum(bool(RESOLVIDO.search(i['texto'])) for i in velhos)}")
    print(f"Radar: {len(itens)} abertas; {len(velhos)} paradas há {a.dias}+ dias "
          f"(você {sum(i['dono'] == 'você' for i in velhos)}). Relatório: {a.saida}")
    for f in ordem:
        print(f"  {f}: {sum(faixa(i['dias']) == f for i in velhos)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
