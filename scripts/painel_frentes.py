"""Painel das frentes, versão simples (decidido em 2026-10-29: entender em segundos, sem jargão).

Uso:  python scripts/painel_frentes.py            # gera paineis/frentes.html
      python scripts/painel_frentes.py --abrir    # gera e abre no navegador
      python scripts/painel_frentes.py --servir   # gera e serve ao vivo em http://127.0.0.1:8765/frentes.html
                                                  (a página busca entregas.json a cada 2 s: mudou o JSON, mudou a tela)

Dados: paineis/entregas.json. Por frente, a janela geral mantém, em linguagem simples:
  situacao   voce | trabalhando | esperando | pronto
  tema       do que se trata (1 frase)
  agora      o que está acontecendo (1–2 frases)
  voce       o que o usuário precisa fazer (no máximo 2–3 itens curtos)
  atualizado "DD/MM HH:MM"
As entregas (histórico) ficam escondidas em "ver histórico" de cada cartão.
Uma tela, um cartão por frente; quem precisa do usuário aparece primeiro.
"""
import json
import os
import sys
import webbrowser
from datetime import datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DADOS = os.path.join(RAIZ, "paineis", "entregas.json")
SAIDA = os.path.join(RAIZ, "paineis", "frentes.html")

HTML = r"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Painel das Frentes</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#000000;--card:#141414;--ink:#ffffff;--mute:#cfccc4;--line:#262626;--acc:#d97757;--acc-soft:#2a1d17;
--voce:#c96442;--trab:#6a7fa8;--esp:#8a7a9e;--ok:#6b8e5a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.6 "Inter","Segoe UI Variable Text","Segoe UI",system-ui,sans-serif;font-weight:400;font-feature-settings:"cv11","ss01";letter-spacing:-.005em;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}
.serif{font-family:"Source Serif 4",Georgia,"Times New Roman",serif}
.top{max-width:1180px;margin:0 auto;padding:36px 20px 4px}
.marca{display:flex;align-items:center;gap:10px;color:var(--mute);font-size:15px;font-weight:600}
.marca svg{width:22px;height:22px;color:var(--acc)}
.top h1{margin:10px 0 0;font:700 36px/1.2 "Source Serif 4",Georgia,serif;letter-spacing:-.01em}
.top p{margin:6px 0 0;color:var(--mute);font-size:15px}
.frase{margin:22px 0 0;padding:14px 18px;border-radius:10px;background:var(--acc-soft);font:600 20px/1.4 "Source Serif 4",Georgia,serif}
.frase b{color:var(--voce);font-weight:600}
.grid{max-width:1500px;margin:0 auto;padding:22px 20px 40px;display:flex;flex-direction:column;gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--c);border-radius:10px;overflow:hidden}
.linha{display:grid;grid-template-columns:300px 1fr 1fr;gap:28px;padding:20px 24px}
@media (max-width:900px){.linha{grid-template-columns:1fr;gap:10px}}

.faixa{display:flex;flex-direction:column;gap:2px}
.pill{font-weight:700;font-size:16px;color:var(--c)}
.pill i{display:none}
.faixa small{color:var(--mute);font-size:15px}

.card h2{margin:6px 0 0;font:700 28px/1.2 "Source Serif 4",Georgia,serif}
.tema{color:var(--mute);font-size:16px;margin:6px 0 0}
.rot{font-size:15px;font-weight:700;color:var(--acc);letter-spacing:.02em}
.agora{margin:6px 0 0;font-size:18px}
.voce{margin:6px 0 0;font-size:18px}
.voce ul{margin:0;padding-left:20px}.voce li{margin:5px 0}
.nada{color:var(--mute);margin:6px 0 0;font-size:18px}
details{border-top:1px solid var(--line);padding:10px 24px;font-size:16px}
summary{cursor:pointer;color:var(--mute)}summary:hover{color:var(--acc)}
.ao{display:flex;align-items:baseline;gap:14px;padding:12px 24px;border-top:1px solid var(--line);font-size:16px;font-weight:500;color:#e8e6e0;flex-wrap:wrap}
.ao .st{font-weight:700;white-space:nowrap}.ao .st.on{color:#7fb3ff}.ao .st.off{color:var(--mute)}
@keyframes pisca{50%{opacity:.35}}.ao .on::before{content:"● ";animation:pisca 1.2s infinite}
.ao .ag{font-weight:700;color:#7fb3ff;white-space:nowrap}.ao .fala{flex:1;min-width:240px}
.h{margin:10px 0}.h b{display:block;font-weight:600}.h span{color:var(--mute)}
</style></head><body>
<div class="top"><div class="marca"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l1.6 6.4L20 7l-4.8 4.6L22 14l-6.6.6L17 21l-5-4.4L7 21l1.6-6.4L2 14l6.8-2.4L4 7l6.4 1.4z"/></svg>Brain Service</div><h1>Painel das Frentes</h1><p id="atual">Atualizado em __GERADO__</p>
<div class="frase" id="frase"></div></div>
<div class="grid" id="grid"></div>
<script>
let D=__DADOS__;
function render(){
const S={voce:["Precisa de você","var(--voce)"],trabalhando:["Trabalhando","var(--trab)"],esperando:["Esperando outras pessoas","var(--esp)"],pronto:["Pronto","var(--ok)"]};
const ORD={voce:0,trabalhando:1,esperando:2,pronto:3};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const fs=[...D.frentes].sort((a,b)=>(ORD[a.situacao]??9)-(ORD[b.situacao]??9));
const n=fs.filter(f=>f.situacao==="voce").length;
document.getElementById("frase").innerHTML=n?`<b>${n} de ${fs.length}</b> frentes estão esperando uma decisão sua.`:"Nenhuma frente está esperando você agora.";
document.getElementById("grid").innerHTML=fs.map(f=>{const s=S[f.situacao]||S.trabalhando;
const hist=D.entregas.filter(e=>e.frente===f.id).sort((a,b)=>b.quando.localeCompare(a.quando));
return `<div class="card" style="--c:${s[1]}"><div class="linha">
<div class="faixa"><span class="pill">${s[0]}</span><h2>${esc(f.nome)}</h2><div class="tema">${esc(f.tema)}</div><small>Atualizado ${esc(f.atualizado||"")}</small></div>
<div><div class="rot">O que está acontecendo</div><p class="agora">${esc(f.agora||"")}</p></div>
<div><div class="rot">O que você precisa fazer</div>
${(f.voce||[]).length?`<div class="voce"><ul>${f.voce.map(v=>`<li>${esc(v)}</li>`).join("")}</ul></div>`:`<p class="nada">Nada por enquanto.</p>`}</div>
</div><div class="ao" id="ao-${f.id}"></div>${hist.length?`<details><summary>Ver histórico (${hist.length})</summary>${hist.map(e=>`<div class="h"><b>${esc(e.quando.slice(11))} · ${esc(e.titulo)}</b><span>${esc(e.resposta)}</span></div>`).join("")}</details>`:""}</div>`}).join("");
}
render();
let ult=JSON.stringify(D);
const hora=()=>new Date().toLocaleTimeString("pt-BR",{hour:"2-digit",minute:"2-digit",second:"2-digit"});
const abertos=()=>[...document.querySelectorAll("details")].map(d=>d.open);
async function vivo(){try{const r=await fetch("entregas.json?t="+Date.now(),{cache:"no-store"});if(!r.ok)throw 0;const t=await r.text();const novo=JSON.stringify(JSON.parse(t));
if(novo!==ult){ult=novo;D=JSON.parse(t);const ab=abertos();render();document.querySelectorAll("details").forEach((d,i)=>{if(ab[i])d.open=true});document.getElementById("atual").textContent="Ao vivo · última mudança às "+hora()}
else if(!document.getElementById("atual").textContent.startsWith("Ao vivo"))document.getElementById("atual").textContent="Ao vivo · conferindo a cada 2 segundos"}catch(e){document.getElementById("atual").textContent="Sem conexão com o servidor do painel (rode: python scripts/painel_frentes.py --servir)"}}
setInterval(vivo,2000);vivo();
let V={};const curta=t=>{t=String(t||"");const i=t.search(/[.!?](\s|$)/);t=i>0&&i<160?t.slice(0,i+1):t;return t.length>160?t.slice(0,157).replace(/\s\S*$/,"")+"…":t};const escV=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));function pinta(){const esc=escV;for(const [id,v] of Object.entries(V)){const el=document.getElementById("ao-"+id);if(!el)continue;
el.innerHTML=`<span class="st ${v.trabalhando?"on":"off"}">${v.trabalhando?"Trabalhando agora":"Parada desde "+esc(v.hora)}</span>${(v.agentes||[]).length?`<span class="ag">${v.agentes.length} agente${v.agentes.length>1?"s":""}</span>`:""}<span class="fala">${esc(curta(v.trabalhando&&!(v.agentes||[]).length&&v.acao?v.acao:v.resposta))}</span>`}}
async function aovivo(){try{const r=await fetch("vivo.json?t="+Date.now(),{cache:"no-store"});if(r.ok){V=await r.json();pinta()}}catch(e){}}
setInterval(aovivo,3000);aovivo();
const _r=render;render=function(){_r();pinta()};
</script></body></html>"""


def main():
    with open(DADOS, encoding="utf-8") as f:
        dados = json.load(f)
    html = (HTML.replace("__DADOS__", json.dumps(dados, ensure_ascii=False))
            .replace("__GERADO__", datetime.now().strftime("%d/%m/%Y às %H:%M")))
    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Painel gerado: {SAIDA} ({len(dados['frentes'])} frentes)")
    if "--abrir" in sys.argv:
        webbrowser.open("file:///" + SAIDA.replace("\\", "/"))
    if "--servir" in sys.argv:
        servir()


PROJ = os.path.join(os.path.expanduser("~"), ".claude", "projects")


def _texto(c):
    if isinstance(c, str):
        return c
    for x in c or []:
        if x.get("type") == "text":
            return x.get("text", "")
    return ""


def _limpa(t, n=260):
    import re
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[*`#|>]+", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def vivo():
    """Lê a conversa mais recente de cada frente (~/.claude/projects/...-frentes-<id>) e diz o que ela faz agora."""
    import glob
    from datetime import timezone
    out = {}
    for d in glob.glob(os.path.join(PROJ, "*brain-service-frentes-*")):
        fid = d.rsplit("-frentes-", 1)[1]
        arqs = glob.glob(os.path.join(d, "*.jsonl"))
        if not arqs:
            continue
        f = max(arqs, key=os.path.getmtime)
        try:
            with open(f, encoding="utf-8") as h:
                linhas = h.readlines()[-400:]
        except OSError:
            continue
        ev = []
        for l in linhas:
            try:
                ev.append(json.loads(l))
            except ValueError:
                pass
        pedido, resposta, acao, quando, trabalhando = "", "", "", "", False
        for e in reversed(ev):
            t = e.get("type")
            if t in ("user", "assistant", "system") and not quando and e.get("timestamp"):
                quando = e["timestamp"]
                trabalhando = not (t == "system" or (t == "assistant" and (e.get("message") or {}).get("stop_reason") == "end_turn"))
            m = e.get("message") or {}
            c = m.get("content")
            if t == "assistant" and not resposta:
                tx = _texto(c)
                if tx:
                    resposta = tx
                if not acao and isinstance(c, list):
                    for x in c:
                        if x.get("type") == "tool_use":
                            nome = x.get("name", "")
                            acao = (x.get("input") or {}).get("description") or next(
                                (v for k, v in (("claude-in-chrome", "Usando o navegador"), ("Bash", "Rodando um comando"),
                                                ("PowerShell", "Rodando um comando"), ("Read", "Lendo um arquivo"),
                                                ("Edit", "Editando um arquivo"), ("Write", "Gravando um arquivo"),
                                                ("Grep", "Procurando nos arquivos"), ("Glob", "Procurando arquivos"),
                                                ("WebSearch", "Pesquisando na web"), ("WebFetch", "Lendo uma página da web"),
                                                ("Agent", "Chamando um agente"), ("SendMessage", "Mandando mensagem a outra janela"))
                                 if k in nome), "Trabalhando")
            if t == "user" and not pedido and not (isinstance(c, list) and any(x.get("type") == "tool_result" for x in c)):
                tx = _texto(c)
                if e.get("isCompactSummary") or e.get("isMeta") or tx.startswith(("This session is being continued", "Base directory for this skill")) or "[Subagent hand-back]" in tx[:400] or "<task-notification" in tx[:200]:
                    continue
                tx = tx.replace("Another Claude session sent a message:", "")
                if tx and not tx.startswith("<command") and "system-reminder" not in tx[:40]:
                    pedido = ("[Janela geral] " if "cross-session-message" in tx else "") + tx
            if pedido and resposta and quando:
                break
        agentes = []  # subagentes rodando: transcrição mexida nos últimos 3 min e sem resposta final
        import time
        sub = os.path.join(f[:-6], "subagents")
        for a in glob.glob(os.path.join(sub, "agent-*.jsonl")):
            if time.time() - os.path.getmtime(a) > 180:
                continue
            try:
                with open(a, encoding="utf-8") as h:
                    ult = [json.loads(l) for l in h.readlines()[-30:] if l.strip()]
            except (OSError, ValueError):
                continue
            ult = [e for e in ult if e.get("type") in ("assistant", "user")]
            if ult and ult[-1].get("type") == "assistant" and (ult[-1].get("message") or {}).get("stop_reason") == "end_turn":
                continue
            desc = ""
            try:
                with open(a[:-6] + ".meta.json", encoding="utf-8") as h:
                    desc = json.load(h).get("description", "")
            except (OSError, ValueError):
                pass
            agentes.append(desc or "agente")
        if agentes:
            trabalhando = True
        hora = ""
        if quando:
            try:
                hora = datetime.fromisoformat(quando.replace("Z", "+00:00")).astimezone().strftime("%H:%M:%S")
            except ValueError:
                pass
        out[fid] = {"trabalhando": trabalhando, "hora": hora, "pedido": _limpa(pedido, 220),
                    "resposta": _limpa(resposta), "acao": _limpa(acao, 120), "agentes": agentes}
    return out


def juntar():
    """entregas.json + paineis/cartoes/<id>.json (gravados pelo hook Stop de cada frente ao fim da rodada)."""
    import glob
    with open(DADOS, encoding="utf-8") as h:
        d = json.load(h)
    for arq in glob.glob(os.path.join(os.path.dirname(DADOS), "cartoes", "*.json")):
        try:
            with open(arq, encoding="utf-8") as h:
                c = json.load(h)
        except (OSError, ValueError):
            continue
        f = next((x for x in d["frentes"] if x["id"] == c.get("id")), None)
        if not f:
            continue
        for k in ("situacao", "agora", "voce", "atualizado"):
            if c.get(k) is not None:
                f[k] = c[k]
        for i, h in enumerate(c.get("historico", [])):
            d["entregas"].append({"id": f"auto-{f['id']}-{i}", "frente": f["id"], "quando": h["quando"],
                                  "titulo": h["titulo"], "resposta": h["resposta"], "status": "pronto"})
    return d


def fim_de_rodada(transcript):
    """Hora (ISO) do último fim de rodada da conversa, ou '' se ela ainda está no meio de uma rodada."""
    with open(transcript, encoding="utf-8") as h:
        linhas = h.readlines()[-200:]
    for l in reversed(linhas):
        try:
            e = json.loads(l)
        except ValueError:
            continue
        t = e.get("type")
        if t == "system" and e.get("subtype") == "turn_duration":
            return e.get("timestamp", "")
        if t == "assistant":
            m = e.get("message") or {}
            return e.get("timestamp", "") if m.get("stop_reason") == "end_turn" else ""
        if t == "user":
            return ""
    return ""


def vigiar(intervalo=5):
    """Fica de olho nas conversas das frentes do painel; a cada rodada nova terminada, refaz o cartão (Haiku)."""
    import glob
    import threading
    import time
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import cartao_frente
    rodando = set()

    def tarefa(fid, tp, rod):
        try:
            cartao_frente.processar(fid, tp, rod)
        except Exception as e:
            os.makedirs(cartao_frente.PASTA, exist_ok=True)
            with open(os.path.join(cartao_frente.PASTA, "_erros.log"), "a", encoding="utf-8") as h:
                h.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} {fid} {e!r}\n")
        finally:
            rodando.discard(fid)

    while True:
        try:
            with open(DADOS, encoding="utf-8") as h:
                ids = [f["id"] for f in json.load(h)["frentes"]]
            for fid in ids:
                if fid in rodando:
                    continue
                arqs = glob.glob(os.path.join(PROJ, f"*brain-service-frentes-{fid}", "*.jsonl"))
                if not arqs:
                    continue
                tp = max(arqs, key=os.path.getmtime)
                if time.time() - os.path.getmtime(tp) < 4:  # ainda escrevendo
                    continue
                rod = fim_de_rodada(tp)
                if not rod:
                    continue
                card = os.path.join(cartao_frente.PASTA, f"{fid}.json")
                visto = ""
                if os.path.exists(card):
                    try:
                        with open(card, encoding="utf-8") as h:
                            visto = json.load(h).get("rodada", "")
                    except (OSError, ValueError):
                        pass
                if rod != visto:
                    rodando.add(fid)
                    threading.Thread(target=tarefa, args=(fid, tp, rod), daemon=True).start()
        except Exception:
            pass
        time.sleep(intervalo)


def servir(porta=8765):
    """Serve paineis/ em http://127.0.0.1:8765/frentes.html sem cache; a página busca entregas.json a cada 2 s."""
    import functools
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

    class SemCache(SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

        def log_message(self, *a):
            pass

        def do_GET(self):
            if self.path.startswith("/entregas.json"):
                corpo = json.dumps(juntar(), ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(corpo)))
                self.end_headers()
                self.wfile.write(corpo)
                return
            if self.path.startswith("/vivo.json"):
                corpo = json.dumps(vivo(), ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(corpo)))
                self.end_headers()
                self.wfile.write(corpo)
                return
            super().do_GET()

    import threading
    threading.Thread(target=vigiar, daemon=True).start()
    h = functools.partial(SemCache, directory=os.path.dirname(SAIDA))
    print(f"Painel ao vivo: http://127.0.0.1:{porta}/frentes.html")
    ThreadingHTTPServer(("127.0.0.1", porta), h).serve_forever()


if __name__ == "__main__":
    main()
