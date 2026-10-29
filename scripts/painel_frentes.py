"""Painel das frentes, versão simples (decidido em 2026-10-29: entender em segundos, sem jargão).

Uso:  python scripts/painel_frentes.py            # gera paineis/frentes.html
      python scripts/painel_frentes.py --abrir    # gera e abre no navegador

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
<meta http-equiv="refresh" content="120"><title>Painel das Frentes</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,600;8..60,700&display=swap" rel="stylesheet">
<style>
:root{--bg:#000000;--card:#141414;--ink:#ffffff;--mute:#cfccc4;--line:#262626;--acc:#d97757;--acc-soft:#2a1d17;
--voce:#c96442;--trab:#6a7fa8;--esp:#8a7a9e;--ok:#6b8e5a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.6 "Segoe UI Variable Text","Segoe UI",system-ui,-apple-system,sans-serif;font-weight:450;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}
.serif{font-family:"Source Serif 4",Georgia,"Times New Roman",serif}
.top{max-width:1180px;margin:0 auto;padding:36px 20px 4px}
.marca{display:flex;align-items:center;gap:10px;color:var(--mute);font-size:15px;font-weight:600}
.marca svg{width:22px;height:22px;color:var(--acc)}
.top h1{margin:10px 0 0;font:700 36px/1.2 "Source Serif 4",Georgia,serif;letter-spacing:-.01em}
.top p{margin:6px 0 0;color:var(--mute);font-size:15px}
.frase{margin:22px 0 0;padding:14px 18px;border-radius:4px;background:var(--acc-soft);font:600 20px/1.4 "Source Serif 4",Georgia,serif}
.frase b{color:var(--voce);font-weight:600}
.grid{max-width:1500px;margin:0 auto;padding:22px 20px 40px;display:flex;flex-direction:column;gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--c);border-radius:4px}
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
.h{margin:10px 0}.h b{display:block;font-weight:600}.h span{color:var(--mute)}
</style></head><body>
<div class="top"><div class="marca"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l1.6 6.4L20 7l-4.8 4.6L22 14l-6.6.6L17 21l-5-4.4L7 21l1.6-6.4L2 14l6.8-2.4L4 7l6.4 1.4z"/></svg>Brain Service</div><h1>Painel das Frentes</h1><p>Atualizado em __GERADO__ · a página se atualiza sozinha</p>
<div class="frase" id="frase"></div></div>
<div class="grid" id="grid"></div>
<script>
const D=__DADOS__;
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
</div>${hist.length?`<details><summary>Ver histórico (${hist.length})</summary>${hist.map(e=>`<div class="h"><b>${esc(e.quando.slice(11))} · ${esc(e.titulo)}</b><span>${esc(e.resposta)}</span></div>`).join("")}</details>`:""}</div>`}).join("");
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


if __name__ == "__main__":
    main()
