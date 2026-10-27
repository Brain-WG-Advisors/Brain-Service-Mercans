"""Gera graphify-out/mapa-3d.html: mapa 3D do grafo do Graphify.

Nível 1: uma esfera por comunidade, colorida pela área (país ou processo); legenda clicável.
Nível 2: clique numa comunidade para ver os conceitos dela e as ligações internas.
Uso: python scripts/mapa3d.py   (rodar depois de cada `graphify update .` / releitura)
Os dados ficam embutidos no HTML; só a biblioteca 3d-force-graph vem do CDN (jsdelivr).
"""
import json, collections, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = json.load(open(os.path.join(ROOT, 'graphify-out', 'graph.json'), encoding='utf-8'))
nodes, links = G['nodes'], G['links']

# Áreas: (nome, cor, palavras-chave no nome da comunidade ou nas notas de origem)
AREAS = [
    ('Colômbia', '#f4c542', ['colombia', 'colômbia', ' co-', 'pila', 'dian', 'pmi']),
    ('Ucrânia', '#4ea1ff', ['ucrania', 'ucrânia', 'ukraine', ' ua ', '1-pv', 'derzhstat']),
    ('Espanha', '#ff6b6b', ['espanha', 'spain', 'modelo 145', 'stg', 'irpf']),
    ('Taiwan', '#b388ff', ['taiwan', 'snhi']),
    ('Holanda / Mammoet', '#ff9f43', ['holanda', 'netherlands', 'mammoet', 'montage', 'marko']),
    ('Bélgica / França', '#2ed1c4', ['bélgica', 'belgica', 'belgium', 'frança', 'franca', 'france']),
    ('África (Baker Hughes, CI, Congo…)', '#7bd88f', ['baker', 'congo', 'namíbia', 'namibia', 'costa do marfim', 'gabão', 'gabao', 'argélia', 'argelia', 'egito', 'egypt', 'cnps', 'chade', 'moçambique', 'marrocos', 'botsuana']),
    ('Outros países', '#c7a27a', ['hub ', 'hubs ', 'lituânia', 'lituania', 'dinamarca', 'noruega', 'suécia', 'reino unido', 'irlanda', 'chile', 'hungria', 'portugal', 'tchéquia', 'singapura', 'líbano', 'cazaquist', 'ericsson', 'canadá']),
    ('Suporte, tickets e triagens', '#e879f9', ['ticket', 'suporte', 'triage', 'fila', 'rascunho', 'hrbs']),
    ('Processo, regras e método', '#8fa3bf', []),
]

comm = {}
by_comm = collections.defaultdict(list)
for n in nodes:
    c = n.get('community')
    if c is None:
        continue
    comm[n['id']] = c
    by_comm[c].append(n)

deg = collections.Counter()
for e in links:
    deg[e['source']] += 1
    deg[e['target']] += 1

def norm(s):
    return ' ' + (s or '').lower() + ' '

def pick_area(text):
    for i, (_, _, kws) in enumerate(AREAS[:-1]):
        if any(k in text for k in kws):
            return i
    return None

names, area_of = {}, {}
for c, ns in by_comm.items():
    nm = next((n.get('community_name') for n in ns if n.get('community_name')), None)
    names[c] = nm or max(ns, key=lambda n: deg[n['id']]).get('label', str(c))
    a = pick_area(norm(names[c]))
    if a is None:
        a = pick_area(norm(' '.join(n.get('label', '') for n in sorted(ns, key=lambda n: -deg[n['id']])[:5])))
    area_of[c] = len(AREAS) - 1 if a is None else a

inter = collections.Counter()
for e in links:
    a, b = comm.get(e['source']), comm.get(e['target'])
    if a is not None and b is not None and a != b:
        inter[tuple(sorted((a, b)))] += 1

order = sorted(by_comm, key=lambda c: -len(by_comm[c]))
communities = []
for c in order:
    ns = sorted(by_comm[c], key=lambda n: -deg[n['id']])
    files = collections.Counter(n.get('source_file') or '' for n in ns)
    communities.append({
        'id': c, 'name': names[c], 'size': len(ns), 'area': area_of[c],
        'top': [n.get('label', n['id']) for n in ns[:8]],
        'files': [f for f, _ in files.most_common(6) if f],
    })
clinks = [{'source': a, 'target': b, 'w': w} for (a, b), w in inter.items()]
concepts = [{'id': n['id'], 'label': n.get('label', n['id']), 'c': comm[n['id']],
             'file': n.get('source_file') or '', 'deg': deg[n['id']]}
            for n in nodes if n['id'] in comm]
plinks = [{'source': e['source'], 'target': e['target'], 'rel': e.get('relation', ''),
           'conf': e.get('confidence', '')}
          for e in links if e['source'] in comm and e['target'] in comm]
areas = [{'name': a[0], 'color': a[1],
          'count': sum(1 for c in communities if c['area'] == i)} for i, a in enumerate(AREAS)]

data = json.dumps({'areas': areas, 'communities': communities, 'clinks': clinks,
                   'concepts': concepts, 'plinks': plinks}, ensure_ascii=False)

PAGE = r"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mapa 3D do Brain Service</title>
<style>
:root{--panel:rgba(16,22,34,.88);--ink:#eef3fa;--muted:#9fb0c6;--line:rgba(120,145,180,.25);--accent:#7cb4ff}
html,body{margin:0;height:100%;color:var(--ink);font:14px/1.45 "Segoe UI",system-ui,Roboto,sans-serif;overflow:hidden;
  background:radial-gradient(ellipse at 50% 40%,#16213a 0%,#0a0f1c 55%,#05080f 100%)}
#g{position:fixed;inset:0}
.box{background:var(--panel);border:1px solid var(--line);border-radius:12px;backdrop-filter:blur(6px);box-shadow:0 8px 30px rgba(0,0,0,.35)}
#top{position:fixed;top:14px;left:14px;right:14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;z-index:3}
#title{font-weight:650;font-size:16px;letter-spacing:.2px;padding:8px 12px}
#title span{color:var(--muted);font-weight:400;font-size:13px;margin-left:8px}
#q{flex:1;min-width:200px;max-width:440px;padding:10px 12px;border-radius:10px;border:1px solid var(--line);background:var(--panel);color:var(--ink);outline:none}
#q:focus{border-color:var(--accent)}
button{padding:9px 13px;border-radius:10px;border:1px solid var(--line);background:var(--panel);color:var(--ink);cursor:pointer}
button:hover{border-color:var(--accent)}
#res{position:fixed;top:64px;left:14px;width:460px;max-width:calc(100% - 28px);z-index:4;display:none;max-height:55vh;overflow:auto}
#res div{padding:8px 12px;cursor:pointer;border-bottom:1px solid var(--line)}
#res div:hover{background:rgba(124,180,255,.12)}
#side{position:fixed;top:72px;right:14px;width:340px;max-width:calc(100% - 28px);max-height:calc(100% - 100px);overflow:auto;padding:14px 16px;z-index:3;display:none}
#side h2{font-size:17px;margin:0 0 4px}
#side .m{color:var(--muted);font-size:12px}
#side ul{padding-left:18px;margin:6px 0 10px}
#legend{position:fixed;left:14px;bottom:14px;padding:10px 12px;z-index:3;font-size:13px;max-width:300px}
#legend div{display:flex;align-items:center;gap:8px;padding:3px 4px;border-radius:6px;cursor:pointer}
#legend div:hover{background:rgba(255,255,255,.06)}
#legend div.off{opacity:.35}
#legend i{width:11px;height:11px;border-radius:50%;flex:none;box-shadow:0 0 8px currentColor}
#legend b{font-weight:600}
#hint{position:fixed;right:14px;bottom:14px;color:var(--muted);font-size:12px;z-index:3;padding:7px 10px}
#labels{position:fixed;inset:0;pointer-events:none;z-index:2}
.lb{position:absolute;transform:translate(-50%,-150%);white-space:nowrap;color:#fff;font-size:13px;font-weight:600;
  padding:2px 7px;border-radius:6px;background:rgba(8,12,22,.72);border:1px solid rgba(255,255,255,.08);text-shadow:0 1px 2px #000}
.lb.small{font-size:11.5px;font-weight:500}
@media (max-width:700px){#legend{display:none}#side{top:auto;bottom:14px;max-height:40%}}
</style></head><body>
<div id="g"></div>
<div id="labels"></div>
<div id="top">
  <div id="title" class="box">Brain Service<span id="crumb"></span></div>
  <button id="back" style="display:none">← Voltar às comunidades</button>
  <input id="q" placeholder="Buscar país, ticket, assunto…" autocomplete="off">
</div>
<div id="res" class="box"></div>
<div id="side" class="box"></div>
<div id="legend" class="box"></div>
<div id="hint" class="box">Arrastar = girar · roda = zoom · botão direito = mover · clique numa esfera para abrir</div>
<script src="https://cdn.jsdelivr.net/npm/3d-force-graph@1.73.4/dist/3d-force-graph.min.js"></script>
<script>
const D = __DATA__;
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const el = id => document.getElementById(id);
const C = new Map(D.communities.map(c => [c.id, c]));
const conceptsBy = new Map(); D.concepts.forEach(n => { if(!conceptsBy.has(n.c)) conceptsBy.set(n.c, []); conceptsBy.get(n.c).push(n); });
const areaColor = i => D.areas[i].color;
const side = el('side'), crumb = el('crumb'), back = el('back');
let level = 'comm', current = null, hidden = new Set(), fitted = false;

const G = ForceGraph3D({controlType: 'orbit'})(el('g'))
  .backgroundColor('rgba(0,0,0,0)')
  .showNavInfo(false)
  .nodeResolution(24)
  .nodeRelSize(5)
  .nodeOpacity(0.96)
  .linkOpacity(0.35)
  .cooldownTime(7000)
  .onEngineStop(() => {});
function fitCore(ms){
  const ns = G.graphData().nodes.filter(n => n.x !== undefined); if(!ns.length) return;
  const q = (arr, p) => { const s = arr.slice().sort((a, b) => a - b); return s[Math.min(s.length - 1, Math.max(0, Math.floor(p * (s.length - 1))))]; };
  const xs = ns.map(n => n.x), ys = ns.map(n => n.y), zs = ns.map(n => n.z);
  const lo = [q(xs, .05), q(ys, .05), q(zs, .05)], hi = [q(xs, .95), q(ys, .95), q(zs, .95)];
  const c = {x: (lo[0] + hi[0]) / 2, y: (lo[1] + hi[1]) / 2, z: (lo[2] + hi[2]) / 2};
  const span = Math.max(hi[0] - lo[0], hi[1] - lo[1], 40);
  G.cameraPosition({x: c.x, y: c.y, z: c.z + span * 1.7}, c, ms || 900);
}
const fitSoon = () => { fitted = true; setTimeout(() => fitCore(900), 2500); setTimeout(() => fitCore(1200), 6500); };
G.d3Force('charge').strength(-180);
G.d3Force('link').distance(60);

/* rótulos HTML que acompanham as esferas */
const LB = el('labels'); let lbItems = [];
function setLabels(items){ LB.innerHTML = ''; lbItems = items.map(it => { const d = document.createElement('div'); d.className = 'lb' + (it.small ? ' small' : ''); d.textContent = it.text; LB.appendChild(d); return {d, id: it.id}; }); }
(function tick(){
  const byId = new Map(G.graphData().nodes.map(n => [n.id, n])); const W = innerWidth, H = innerHeight; const placed = [];
  for(const it of lbItems){ const n = byId.get(it.id);
    if(!n || n.x === undefined || (level === 'comm' && hidden.has(n.area))){ it.d.style.display = 'none'; continue; }
    const p = G.graph2ScreenCoords(n.x, n.y, n.z);
    if(p.x < 0 || p.y < 0 || p.x > W || p.y > H || placed.some(q => Math.abs(q.x - p.x) < 120 && Math.abs(q.y - p.y) < 22)){ it.d.style.display = 'none'; continue; }
    placed.push(p); it.d.style.display = ''; it.d.style.left = p.x + 'px'; it.d.style.top = p.y + 'px'; }
  requestAnimationFrame(tick);
})();

/* legenda */
const areaOf = x => (typeof x === 'object' ? x.area : (C.get(x) || {}).area);
function applyHidden(){ if(level === 'comm') G.nodeVisibility(n => !hidden.has(n.area)).linkVisibility(l => !hidden.has(areaOf(l.source)) && !hidden.has(areaOf(l.target))); }
function drawLegend(){
  el('legend').innerHTML = '<div style="cursor:default;color:var(--muted)">Cores = área · clique para mostrar/ocultar</div>' +
    D.areas.map((a, i) => a.count ? '<div data-i="' + i + '" class="' + (hidden.has(i) ? 'off' : '') + '"><i style="background:' + a.color + ';color:' + a.color + '"></i><span>' + esc(a.name) + ' <b>' + a.count + '</b></span></div>' : '').join('');
  el('legend').querySelectorAll('div[data-i]').forEach(d => d.onclick = () => { const i = +d.dataset.i; hidden.has(i) ? hidden.delete(i) : hidden.add(i); drawLegend(); applyHidden(); });
}

/* nível 1: comunidades */
function showCommunities(focusId){
  level = 'comm'; current = null; back.style.display = 'none'; fitted = focusId != null;
  crumb.textContent = D.communities.length + ' grupos de assunto · ' + D.concepts.length + ' conceitos';
  const maxw = Math.max(...D.clinks.map(l => l.w), 1);
  const linked = new Set(); D.clinks.forEach(l => { linked.add(l.source); linked.add(l.target); });
  const vis = D.communities.filter(c => linked.has(c.id));
  crumb.textContent = vis.length + ' grupos ligados (' + (D.communities.length - vis.length) + ' isolados, só pela busca) · ' + D.concepts.length + ' conceitos';
  G.graphData({ nodes: vis.map(c => ({...c})), links: D.clinks.map(l => ({...l})) })
    .nodeLabel(n => '<b>' + esc(n.name) + '</b><br>' + n.size + ' conceitos · ' + esc(D.areas[n.area].name))
    .nodeVal(n => 1 + n.size * 0.5)
    .nodeColor(n => areaColor(n.area))
    .linkWidth(l => 0.4 + 3.2 * Math.sqrt(l.w / maxw))
    .linkColor(() => 'rgba(170,195,230,0.55)')
    .onNodeClick(n => openCommunity(n.id))
    .onNodeHover(n => { el('g').style.cursor = n ? 'pointer' : null; if(n) infoCommunity(n); });
  applyHidden();
  setLabels(vis.slice(0, 30).map(c => ({id: c.id, text: c.name, small: c.size < 25})));
  side.style.display = 'none';
  if(focusId != null) setTimeout(() => focusOn(focusId, 260), 600); else fitSoon();
}

function infoCommunity(c){
  side.style.display = 'block';
  side.innerHTML = '<h2>' + esc(c.name) + '</h2><div class="m"><span style="color:' + areaColor(c.area) + '">●</span> ' + esc(D.areas[c.area].name) + ' · ' + c.size + ' conceitos · clique para abrir</div>' +
    '<b>Conceitos principais</b><ul>' + c.top.map(t => '<li>' + esc(t) + '</li>').join('') + '</ul>' +
    (c.files.length ? '<b>Notas de origem</b><ul>' + c.files.map(f => '<li class="m">' + esc(f) + '</li>').join('') + '</ul>' : '');
}

/* nível 2: conceitos de uma comunidade */
function openCommunity(id, focusConcept){
  const c = C.get(id); if(!c) return;
  level = 'concept'; current = id; back.style.display = ''; fitted = !!focusConcept;
  crumb.textContent = c.name + ' · ' + c.size + ' conceitos';
  const ns = conceptsBy.get(id) || [], ids = new Set(ns.map(n => n.id));
  const ls = D.plinks.filter(l => ids.has(l.source) && ids.has(l.target));
  const col = areaColor(c.area);
  G.graphData({ nodes: ns.map(n => ({...n})), links: ls.map(l => ({...l})) })
    .nodeLabel(n => '<b>' + esc(n.label) + '</b><br><span style="color:#9fb0c6">' + esc(n.file) + '</span>')
    .nodeVal(n => 1.5 + n.deg * 0.9)
    .nodeColor(n => n.deg >= 8 ? '#ffffff' : col)
    .nodeVisibility(() => true)
    .linkVisibility(() => true)
    .linkWidth(l => l.conf === 'EXTRACTED' ? 1.4 : 0.6)
    .linkColor(l => l.conf === 'AMBIGUOUS' ? 'rgba(255,120,120,0.8)' : (l.conf === 'EXTRACTED' ? 'rgba(190,210,240,0.75)' : 'rgba(150,170,200,0.45)'))
    .onNodeClick(n => infoConcept(n, ls))
    .onNodeHover(n => { el('g').style.cursor = n ? 'pointer' : null; });
  setLabels(ns.slice().sort((a, b) => b.deg - a.deg).slice(0, 35).map(n => ({id: n.id, text: n.label.length > 46 ? n.label.slice(0, 44) + '…' : n.label, small: n.deg < 8})));
  infoCommunity(c);
  if(focusConcept) setTimeout(() => focusOn(focusConcept, 140), 1500); else fitSoon();
}

function infoConcept(n, ls){
  const lab = id => (D.concepts.find(x => x.id === id) || {}).label || id;
  const rel = ls.filter(l => (l.source.id || l.source) === n.id || (l.target.id || l.target) === n.id);
  side.style.display = 'block';
  side.innerHTML = '<h2>' + esc(n.label) + '</h2><div class="m">' + esc(n.file) + '</div><div class="m">' + n.deg + ' ligações no grafo inteiro</div>' +
    '<b>Ligações neste grupo</b><ul>' + (rel.length ? rel.map(l => { const s = l.source.id || l.source, t = l.target.id || l.target, o = s === n.id ? t : s;
      return '<li>' + esc(l.rel.replace(/_/g, ' ')) + ' → ' + esc(lab(o)) + '</li>'; }).join('') : '<li class="m">nenhuma dentro do grupo</li>') + '</ul>';
  focusOn(n.id, 140);
}

function focusOn(id, d){
  const n = G.graphData().nodes.find(x => x.id === id); if(!n || n.x === undefined) return;
  const r = 1 + d / Math.max(1, Math.hypot(n.x, n.y, n.z));
  G.cameraPosition({x: n.x * r, y: n.y * r, z: n.z * r}, n, 1200);
}

back.onclick = () => showCommunities(current);

/* busca */
const q = el('q'), res = el('res');
q.oninput = () => {
  const s = q.value.trim().toLowerCase(); if(s.length < 2){ res.style.display = 'none'; return; }
  const cm = D.communities.filter(c => c.name.toLowerCase().includes(s)).slice(0, 8)
    .map(c => ({t: '◉ ' + c.name + '  (' + c.size + ')', go: () => openCommunity(c.id)}));
  const cc = D.concepts.filter(n => n.label.toLowerCase().includes(s)).sort((a, b) => b.deg - a.deg).slice(0, 14)
    .map(n => ({t: '· ' + n.label + '  —  ' + (C.get(n.c) || {}).name, go: () => openCommunity(n.c, n.id)}));
  const all = cm.concat(cc); res.innerHTML = '';
  all.forEach(x => { const d = document.createElement('div'); d.textContent = x.t; d.onclick = () => { res.style.display = 'none'; q.value = ''; x.go(); }; res.appendChild(d); });
  res.style.display = all.length ? 'block' : 'none';
};
document.addEventListener('keydown', e => { if(e.key === 'Escape'){ res.style.display = 'none'; if(level === 'concept') showCommunities(current); } });

drawLegend();
showCommunities();
</script></body></html>"""

out = os.path.join(ROOT, 'graphify-out', 'mapa-3d.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(PAGE.replace('__DATA__', data.replace('</', '<\\/')))
print('ok', len(communities), 'comunidades;', ', '.join(f"{a['name']}={a['count']}" for a in areas))
