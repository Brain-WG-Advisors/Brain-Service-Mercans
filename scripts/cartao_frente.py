"""Atualiza o cartão de uma frente no painel ao fim de cada rodada (hook Stop da janela; decidido em 2026-10-29).

Uso (hook, em frentes/<id>/.claude/settings.json):
    python C:/Users/instituto/Documents/brain-service/scripts/cartao_frente.py <id>
O hook recebe no stdin o JSON do Claude Code (transcript_path). O script responde na hora e
dispara em segundo plano o resumo: pega a última resposta da frente, pede ao Haiku (claude -p)
o cartão em linguagem de leigo (situação, o que está acontecendo, o que você precisa fazer)
e grava paineis/cartoes/<id>.json. O servidor do painel junta esses cartões ao entregas.json,
então a tela muda sozinha. Nunca bloqueia nem quebra a janela: qualquer erro vai para paineis/cartoes/_erros.log.
"""
import json
import os
import subprocess
import sys
from datetime import datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, "paineis", "cartoes")
SEM_JANELA = 0x08000000 if os.name == "nt" else 0  # CREATE_NO_WINDOW: nada aparece na tela do usuário

PROMPT = """Você resume, para um gestor leigo, o fim de uma rodada de trabalho de um assistente.
Abaixo está a última resposta do assistente da frente "{nome}" ({tema}).
Devolva SÓ um JSON válido, sem texto antes ou depois, neste formato:
{{"situacao": "voce" | "trabalhando" | "esperando" | "pronto",
  "agora": "o que está acontecendo, em 1 ou 2 frases curtas, português simples, sem siglas sem explicação",
  "voce": ["o que o gestor precisa fazer, item curto", "no máximo 3 itens; lista vazia se nada"],
  "titulo": "título de 3 a 8 palavras para esta entrega"}}
Regras: "voce" = a resposta pede decisão, ok, login ou ação do gestor; "esperando" = depende de outra pessoa;
"trabalhando" = disse que continua sozinho; "pronto" = concluiu sem pendência. Não invente nada que não esteja no texto.

RESPOSTA DO ASSISTENTE:
{texto}"""


def ultima_resposta(transcript):
    with open(transcript, encoding="utf-8") as h:
        linhas = h.readlines()[-300:]
    for l in reversed(linhas):
        try:
            e = json.loads(l)
        except ValueError:
            continue
        if e.get("type") != "assistant":
            continue
        for x in (e.get("message") or {}).get("content") or []:
            if x.get("type") == "text" and x.get("text", "").strip():
                return x["text"]
    return ""


def processar(fid, transcript, rodada=""):
    os.makedirs(PASTA, exist_ok=True)
    texto = ultima_resposta(transcript)
    if len(texto) < 40:
        if rodada:  # marca a rodada como vista para não repetir
            arq = os.path.join(PASTA, f"{fid}.json")
            c = json.load(open(arq, encoding="utf-8")) if os.path.exists(arq) else {"id": fid, "historico": []}
            c["rodada"] = rodada
            json.dump(c, open(arq, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return
    base = json.load(open(os.path.join(RAIZ, "paineis", "entregas.json"), encoding="utf-8"))
    fr = next((f for f in base["frentes"] if f["id"] == fid), {"nome": fid, "tema": ""})
    r = subprocess.run(["claude", "-p", "--model", "claude-haiku-4-5-20251001",
                        PROMPT.format(nome=fr["nome"], tema=fr.get("tema", ""), texto=texto[:6000])],
                       capture_output=True, text=True, encoding="utf-8", timeout=180, cwd=PASTA,
                       stdin=subprocess.DEVNULL, creationflags=SEM_JANELA)
    out = r.stdout.strip()
    ini, fim = out.find("{"), out.rfind("}")
    card = json.loads(out[ini:fim + 1])
    agora = datetime.now()
    arq = os.path.join(PASTA, f"{fid}.json")
    antigo = json.load(open(arq, encoding="utf-8")) if os.path.exists(arq) else {"historico": []}
    hist = antigo.get("historico", [])
    hist.insert(0, {"quando": agora.strftime("%Y-%m-%d %H:%M"), "titulo": card.get("titulo", "Rodada concluída"),
                    "resposta": card.get("agora", "")})
    novo = {"id": fid, "rodada": rodada, "situacao": card.get("situacao", "voce"), "agora": card.get("agora", ""),
            "voce": card.get("voce", [])[:3], "atualizado": agora.strftime("%d/%m %H:%M"), "historico": hist[:15]}
    tmp = arq + ".tmp"
    with open(tmp, "w", encoding="utf-8") as h:
        json.dump(novo, h, ensure_ascii=False, indent=1)
    os.replace(tmp, arq)


def main():
    fid = sys.argv[1]
    if len(sys.argv) > 3 and sys.argv[2] == "--processar":
        try:
            processar(fid, sys.argv[3])
        except Exception as e:  # nunca quebra a janela
            os.makedirs(PASTA, exist_ok=True)
            with open(os.path.join(PASTA, "_erros.log"), "a", encoding="utf-8") as h:
                h.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} {fid} {e!r}\n")
        return
    try:
        dados = json.load(sys.stdin)
    except ValueError:
        return
    if dados.get("stop_hook_active"):
        return
    tp = dados.get("transcript_path")
    if not tp:
        return
    flags = (0x00000008 | 0x00000200 | SEM_JANELA) if os.name == "nt" else 0  # oculto e desligado da janela
    subprocess.Popen([sys.executable, os.path.abspath(__file__), fid, "--processar", tp],
                     creationflags=flags, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL, close_fds=True)


if __name__ == "__main__":
    main()
