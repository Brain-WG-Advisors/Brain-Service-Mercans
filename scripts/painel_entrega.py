"""Painel de entrega no navegador (decidido em 2026-10-23).
Gera uma aba HTML por entrega (comentario de ticket ou arquivo) + um painel, com medidas
(perguntas respondidas, afirmacoes relidas na fonte x so agente, palavras, itens alem do pedido,
pendencias), checklist de prontidao e decisao (ok / ajustar / nao entregar) guardada no navegador.
Uso: python -I scripts/painel_entrega.py <dados.json> [--abrir]
As paginas saem na mesma pasta do dados.json. Formato do JSON: ver rascunhos/2026-10-23-shruti/entrega/dados.json.
Fonte de cada afirmacao: "eu" = relida pela janela na fonte primaria; "agente" = so o agente leu; "sem" = sem fonte.
Nada sai da maquina: paginas locais (file://), sem publicar.
"""
import html, json, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')
DADOS = sys.argv[1]
OUT = os.path.dirname(os.path.abspath(DADOS))
D = json.load(open(DADOS, encoding='utf-8'))
ITENS, PENDENTES = D["itens"], D.get("pendentes", [])
E = html.escape
CSS = """
:root{--bg:#f6f7f9;--card:#fff;--tx:#1d2330;--mut:#5d6677;--bd:#dfe3ea;--acc:#7a3e8e;--ok:#1d7a46;--warn:#a76200;--bad:#b42318;--code:#f1f2f5}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14161b;--card:#1d2027;--tx:#e6e8ee;--mut:#9aa3b5;--bd:#30343e;--acc:#c48ad6;--ok:#4cc38a;--warn:#f0a64a;--bad:#f07a6e;--code:#262a33}}
:root[data-theme="dark"]{--bg:#14161b;--card:#1d2027;--tx:#e6e8ee;--mut:#9aa3b5;--bd:#30343e;--acc:#c48ad6;--ok:#4cc38a;--warn:#f0a64a;--bad:#f07a6e;--code:#262a33}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 "Segoe UI",system-ui,sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px 60px}
h1{font-size:22px;margin:0 0 4px}h2{font-size:16px;margin:0 0 10px;color:var(--acc)}
.sub{color:var(--mut);margin-bottom:18px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:16px}
.m{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:12px}
.m b{display:block;font-size:24px}.m span{color:var(--mut);font-size:12px}
.card{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:16px;margin-bottom:14px}
pre{white-space:pre-wrap;background:var(--code);border-radius:8px;padding:14px;font:13.5px/1.5 Consolas,monospace;margin:0}
table{width:100%;border-collapse:collapse;font-size:14px}td,th{border-bottom:1px solid var(--bd);padding:7px 6px;text-align:left;vertical-align:top}
th{color:var(--mut);font-weight:600}
.tag{display:inline-block;border-radius:99px;padding:1px 9px;font-size:12px;font-weight:600}
.eu{background:color-mix(in srgb,var(--ok) 18%,transparent);color:var(--ok)}
.agente{background:color-mix(in srgb,var(--warn) 18%,transparent);color:var(--warn)}
.sem{background:color-mix(in srgb,var(--bad) 18%,transparent);color:var(--bad)}
ul{margin:4px 0 0 18px;padding:0}li{margin:3px 0}
.dec button,.cp{border:1px solid var(--bd);background:var(--card);color:var(--tx);border-radius:8px;padding:7px 14px;margin:0 6px 6px 0;cursor:pointer;font:inherit}
.dec button.on{border-color:var(--acc);background:color-mix(in srgb,var(--acc) 15%,transparent)}
textarea{width:100%;min-height:70px;background:var(--code);color:var(--tx);border:1px solid var(--bd);border-radius:8px;padding:8px;font:inherit}
label{display:block;margin:4px 0}a{color:var(--acc)}
.bar{height:8px;background:var(--code);border-radius:99px;overflow:hidden}.bar i{display:block;height:100%;background:var(--ok)}
"""

JS = """
const K=document.body.dataset.k;function g(k){try{return localStorage.getItem(K+k)}catch(e){return null}}
function s(k,v){try{localStorage.setItem(K+k,v)}catch(e){}}
document.querySelectorAll('input[type=checkbox]').forEach(c=>{c.checked=g(c.id)==='1';c.onchange=()=>{s(c.id,c.checked?'1':'0');pr()}});
function pr(){const cs=[...document.querySelectorAll('input[type=checkbox]')];const n=cs.filter(c=>c.checked).length;
 const e=document.getElementById('prog');if(e){e.style.width=(100*n/cs.length)+'%';document.getElementById('progt').textContent=n+'/'+cs.length}}
pr();
const dv=g('dec');document.querySelectorAll('.dec button').forEach(b=>{if(b.dataset.v===dv)b.classList.add('on');
 b.onclick=()=>{document.querySelectorAll('.dec button').forEach(x=>x.classList.remove('on'));b.classList.add('on');s('dec',b.dataset.v);
 document.title=b.textContent.split(' ')[0]+' '+document.body.dataset.t}});
if(dv){const b=document.querySelector('.dec button[data-v="'+dv+'"]');if(b)document.title=b.textContent.split(' ')[0]+' '+document.body.dataset.t}
const ta=document.querySelector('textarea');if(ta){ta.value=g('nota')||'';ta.oninput=()=>s('nota',ta.value)}
const cp=document.querySelector('.cp');if(cp)cp.onclick=()=>{navigator.clipboard.writeText(document.getElementById('txt').innerText);cp.textContent='Copiado ✓'};
"""

CHECK = ["Responde só o que foi perguntado","Cada afirmação tem fonte primária com artigo/seção","Afirmações do agente reconferidas por mim",
         "Sem dados pessoais de empregados","Tom neutro, sem instrução a outros times","Itens além do pedido resolvidos (tirados ou aprovados)",
         "Pendências resolvidas (placeholders, datas)"]

def page(it):
    a = it["afirm"]; eu = sum(1 for x in a if x[1]=="eu"); ag = sum(1 for x in a if x[1]=="agente"); se = sum(1 for x in a if x[1]=="sem")
    palavras = len(re.findall(r"\w+", it["texto"]))
    titulo = f"{it['n']} · {it['id']} {it['pais'].split(' /')[0]}"
    rows = "".join(f"<tr><td>{E(t)}</td><td><span class='tag {q}'>{ {'eu':'relido por mim','agente':'só agente','sem':'sem fonte'}[q] }</span></td><td>{E(f)}</td></tr>" for t,q,f in a)
    li = lambda xs: "<ul>"+"".join(f"<li>{E(x)}</li>" for x in xs)+"</ul>" if xs else "<p style='color:var(--mut)'>Nenhum.</p>"
    chk = "".join(f"<label><input type=checkbox id='c{i}'> {E(c)}</label>" for i,c in enumerate(CHECK))
    return f"""<!doctype html><html lang=pt-BR><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>⏳ {E(titulo)}</title><style>{CSS}</style></head><body data-k="ent-{E(it['id'])}-" data-t="{E(titulo)}"><main>
<p><a href="00-painel.html">← Painel</a></p>
<h1>{it['n']} · {E(it['id'])} — {E(it['pais'])}</h1>
<div class=sub>{E(it['tipo'])} · para {E(it['para'])} · análise: <code>{E(D['pasta_analise'])}/{E(it['arquivo'])}</code> · <b>nada gravado nem enviado</b></div>
<div class=grid>
<div class=m><b>{it['respondidas']}/{len(it['pedido'])}</b><span>perguntas respondidas</span></div>
<div class=m><b>{eu}/{len(a)}</b><span>afirmações relidas por mim</span></div>
<div class=m><b>{ag}</b><span>só o agente leu</span></div>
<div class=m><b>{se}</b><span>sem fonte</span></div>
<div class=m><b>{palavras}</b><span>palavras no texto</span></div>
<div class=m><b>{len(it['alem'])}</b><span>itens além do pedido</span></div>
<div class=m><b>{len(it['pend'])}</b><span>pendências</span></div>
</div>
<div class=card><h2>O que foi pedido</h2>{li(it['pedido'])}</div>
<div class=card><h2>Texto para entrega</h2><pre id=txt>{E(it['texto'])}</pre><p><button class=cp>Copiar texto</button></p></div>
<div class=card><h2>Afirmações e fonte</h2><table><tr><th>Afirmação</th><th>Conferência</th><th>Fonte</th></tr>{rows}</table></div>
<div class=card><h2>Além do pedido</h2>{li(it['alem'])}</div>
<div class=card><h2>Pendências antes de entregar</h2>{li(it['pend'])}</div>
<div class=card><h2>Checklist de prontidão <span id=progt></span></h2><div class=bar><i id=prog></i></div>{chk}</div>
<div class=card dec><h2>Sua decisão</h2><div class=dec>
<button data-v=ok>✅ Aprovado para gravar</button><button data-v=aj>✏️ Ajustar</button><button data-v=fora>⛔ Não entregar</button></div>
<textarea placeholder="Anotações (ficam só neste navegador)"></textarea></div>
</main><script>{JS}</script></body></html>"""

def pend_page(it):
    titulo = f"{it['n']} · {it['id']}"
    return f"""<!doctype html><html lang=pt-BR><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>🔄 {E(titulo)}</title><style>{CSS}</style></head><body data-k="ent-p{it['n']}-" data-t="{E(titulo)}"><main>
<p><a href="00-painel.html">← Painel</a></p><h1>{it['n']} · {E(it['id'])} — {E(it['pais'])}</h1>
<div class=sub>{E(it['tipo'])}</div><div class=card><h2>Status</h2><p>🔄 {E(it['nota'])}</p>
<p>Quando chegar: campos totais × alterados, mapeados antes → depois, afirmações com fonte, ⚠️ pendentes, veredito do revisor.</p></div>
</main><script>{JS}</script></body></html>"""

def nome(it): return f"{it['n']:02d}-{it['id'].replace(' ','_')}.html"
links=[]
for it in ITENS:
    f=nome(it); open(os.path.join(OUT,f),"w",encoding="utf-8").write(page(it))
    a=it["afirm"]; eu=sum(1 for x in a if x[1]=="eu")
    links.append(f"<tr><td>{it['n']}</td><td><a href='{f}'>{E(it['id'])}</a></td><td>{E(it['pais'])}</td><td>{E(it['tipo'])}</td><td>{it['respondidas']}/{len(it['pedido'])}</td><td>{eu}/{len(a)}</td><td>{len(re.findall(r'\\w+',it['texto']))}</td><td>{len(it['alem'])}</td><td>{len(it['pend'])}</td><td>⏳ revisar</td></tr>")
for it in PENDENTES:
    f=f"{it['n']:02d}-{it['id'].replace(' ','_')}-arquivo.html"; open(os.path.join(OUT,f),"w",encoding="utf-8").write(pend_page(it))
    links.append(f"<tr><td>{it['n']}</td><td><a href='{f}'>{E(it['id'])}</a></td><td>{E(it['pais'])}</td><td>{E(it['tipo'])}</td><td colspan=5 style='color:var(--mut)'>—</td><td>🔄 agentes</td></tr>")
tot_a=sum(len(i['afirm']) for i in ITENS); tot_eu=sum(sum(1 for x in i['afirm'] if x[1]=='eu') for i in ITENS)
painel=f"""<!doctype html><html lang=pt-BR><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>0 · {E(D["titulo"].replace("Painel de entrega — ",""))}</title><style>{CSS}</style></head><body data-k="ent-painel-" data-t="Painel"><main>
<h1>{E(D['titulo'])}</h1><div class=sub>Gerado em {E(D['data'])} · cada linha abre numa aba · nada foi gravado no YouTrack, Drive ou e-mail</div>
<div class=grid><div class=m><b>{len(ITENS)+len(PENDENTES)}</b><span>entregas</span></div>
<div class=m><b>{len(ITENS)}</b><span>prontas para revisar</span></div><div class=m><b>{len(PENDENTES)}</b><span>esperando agentes</span></div>
<div class=m><b>{tot_eu}/{tot_a}</b><span>afirmações relidas por mim</span></div>
<div class=m><b>{sum(len(i['alem']) for i in ITENS)}</b><span>itens além do pedido</span></div>
<div class=m><b>{sum(len(i['pend']) for i in ITENS)}</b><span>pendências</span></div></div>
<div class=card><table><tr><th>#</th><th>Ticket</th><th>País</th><th>Entrega</th><th>Perguntas</th><th>Relidas</th><th>Palavras</th><th>Além</th><th>Pend.</th><th>Status</th></tr>{''.join(links)}</table></div>
<div class=card><h2>Como ler</h2><ul><li><b>Relidas</b>: afirmações que eu conferi pessoalmente na fonte primária. As demais só o agente leu e precisam de reconferência antes de gravar.</li>
<li><b>Além</b>: trechos que ninguém pediu. A regra é tirar, salvo decisão sua.</li><li>A decisão em cada aba muda o ícone do título da aba (✅ ✏️ ⛔).</li></ul></div>
</main><script>{JS}</script></body></html>"""
open(os.path.join(OUT,"00-painel.html"),"w",encoding="utf-8").write(painel)
print("\n".join(sorted(os.listdir(OUT))))

if "--abrir" in sys.argv:
    import subprocess
    for f in sorted(os.listdir(OUT)):
        if f.endswith(".html"): os.startfile(os.path.join(OUT, f))
