"""Gera graphify-out/mapa-3d.html: mapa 3D do grafo do Graphify.

Nível 1: uma esfera por comunidade (tamanho = nº de conceitos; linhas = ligações entre comunidades).
Nível 2: clique numa comunidade para ver os conceitos dela e as ligações internas.
Uso: python scripts/mapa3d.py   (rodar depois de cada `graphify update .` / releitura)
Os dados ficam embutidos no HTML; só a biblioteca 3d-force-graph vem do CDN (jsdelivr).
"""
import json, collections, colorsys, html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G = json.load(open(os.path.join(ROOT, 'graphify-out', 'graph.json'), encoding='utf-8'))
nodes, links = G['nodes'], G['links']

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

names = {}
for c, ns in by_comm.items():
    nm = next((n.get('community_name') for n in ns if n.get('community_name')), None)
    names[c] = nm or max(ns, key=lambda n: deg[n['id']]).get('label', str(c))

order = sorted(by_comm, key=lambda c: -len(by_comm[c]))
color = {}
for i, c in enumerate(order):
    h = (i * 0.61803398875) % 1.0
    r, g, b = colorsys.hls_to_rgb(h, 0.58, 0.65)
    color[c] = '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))

inter = collections.Counter()
for e in links:
    a, b = comm.get(e['source']), comm.get(e['target'])
    if a is not None and b is not None and a != b:
        inter[tuple(sorted((a, b)))] += 1

communities = []
for c in order:
    ns = sorted(by_comm[c], key=lambda n: -deg[n['id']])
    files = collections.Counter(n.get('source_file') or '' for n in ns)
    communities.append({
        'id': c, 'name': names[c], 'size': len(ns), 'color': color[c],
        'top': [n.get('label', n['id']) for n in ns[:8]],
        'files': [f for f, _ in files.most_common(6) if f],
    })
clinks = [{'source': a, 'target': b, 'w': w} for (a, b), w in inter.items()]

concepts = [{
    'id': n['id'], 'label': n.get('label', n['id']), 'c': comm[n['id']],
    'file': n.get('source_file') or '', 'deg': deg[n['id']],
} for n in nodes if n['id'] in comm]
plinks = [{'source': e['source'], 'target': e['target'], 'rel': e.get('relation', ''),
           'conf': e.get('confidence', '')}
          for e in links if e['source'] in comm and e['target'] in comm]

data = json.dumps({'communities': communities, 'clinks': clinks,
                   'concepts': concepts, 'plinks': plinks}, ensure_ascii=False)

PAGE = r"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mapa 3D do Brain Service</title>
<style>
:root{--bg:#0b0f17;--panel:#121a26;--ink:#e6edf6;--muted:#93a4b8;--line:#243146;--accent:#6aa9ff}
html,body{margin:0;height:100%;background:var(--bg);color:var(--ink);font:14px/1.45 system-ui,Segoe UI,Roboto,sans-serif;overflow:hidden}
#g{position:fixed;inset:0}
#bar{position:fixed;top:12px;left:12px;right:12px;display:flex;gap:8px;align-items:center;flex-wrap:wrap;z-index:2}
#bar input{flex:1;min-width:180px;max-width:420px;padding:8px 10px;border-radius:8px;border:1px solid var(--line);background:var(--panel);color:var(--ink)}
button{padding:8px 12px;border-radius:8px;border:1px solid var(--line);background:var(--panel);color:var(--ink);cursor:pointer}
button:hover{border-color:var(--accent)}
#crumb{color:var(--muted)}
#side{position:fixed;top:64px;right:12px;width:340px;max-width:calc(100% - 24px);max-height:calc(100% - 80px);overflow:auto;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px;z-index:2;display:none}
#side h2{font-size:16px;margin:0 0 6px}
#side .m{color:var(--muted);font-size:12px}
#side ul{padding-left:18px;margin:6px 0}
#hint{position:fixed;left:12px;bottom:12px;color:var(--muted);font-size:12px;z-index:2;background:rgba(11,15,23,.7);padding:6px 8px;border-radius:6px}
#res{position:fixed;top:56px;left:12px;width:420px;max-width:calc(100% - 24px);background:var(--panel);border:1px solid var(--line);border-radius:8px;z-index:3;display:none;max-height:50vh;overflow:auto}
#res div{padding:6px 10px;cursor:pointer;border-bottom:1px solid var(--line)}
#res div:hover{background:#1a2535}
#labels{position:fixed;inset:0;pointer-events:none;z-index:1}
.lb{position:absolute;transform:translate(-50%,-140%);white-space:nowrap;color:#fff;font-size:12px;padding:1px 5px;border-radius:4px;background:rgba(11,15,23,.6);text-shadow:0 1px 2px #000}
.lb.big{font-size:13px;font-weight:600}
</style></head><body>
<div id="g"></div>
<div id="labels"></div>
<div id="bar">
  <button id="back" style="display:none">← Comunidades</button>
  <input id="q" placeholder="Buscar país, ticket, assunto ou comunidade…" autocomplete="off">
  <span id="crumb"></span>
</div>
<div id="res"></div>
<div id="side"></div>
<div id="hint">Arraste para girar · roda do mouse = zoom · botão direito = mover · clique numa esfera para abrir</div>
<script src="https://cdn.jsdelivr.net/npm/3d-force-graph@1.73.4/dist/3d-force-graph.min.js"></script>
<script>
const D = __DATA__;
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const C = new Map(D.communities.map(c => [c.id, c]));
const conceptsBy = new Map(); D.concepts.forEach(n => { if(!conceptsBy.has(n.c)) conceptsBy.set(n.c, []); conceptsBy.get(n.c).push(n); });
const el = id => document.getElementById(id);
const side = el('side'), crumb = el('crumb'), back = el('back');
let level = 'comm', current = null;

const G = ForceGraph3D()(el('g'))
  .backgroundColor('#0b0f17')
  .showNavInfo(false)
  .nodeOpacity(0.92)
  .linkOpacity(0.45);
G.d3Force('charge').strength(-220);
G.d3Force('link').distance(l => 60);

function showCommunities(focusId){
  level = 'comm'; current = null; back.style.display = 'none';
  crumb.textContent = D.communities.length + ' comunidades · ' + D.concepts.length + ' conceitos';
  const maxw = Math.max(...D.clinks.map(l => l.w), 1);
  G.graphData({
      nodes: D.communities.map(c => ({...c})),
      links: D.clinks.map(l => ({...l}))
    })
    .nodeLabel(n => '<b>' + esc(n.name) + '</b><br>' + n.size + ' conceitos')
    .nodeVal(n => Math.max(1, n.size))
    .nodeColor(n => n.color)
    .linkWidth(l => 0.3 + 3 * l.w / maxw)
    .linkColor(() => '#8ea2bf')
    .onNodeClick(n => openCommunity(n.id))
    .onNodeHover(n => { el('g').style.cursor = n ? 'pointer' : null; if(n) infoCommunity(n); });
  setLabels(D.communities.slice(0, 25).map(c => ({id: c.id, text: c.name, big: c.size >= 30})));
  side.style.display = 'none';
  if(focusId != null) setTimeout(() => focusOn(focusId), 900);
}

function infoCommunity(c){
  side.style.display = 'block';
  side.innerHTML = '<h2>' + esc(c.name) + '</h2><div class="m">' + c.size + ' conceitos · clique para abrir</div>' +
    '<b>Conceitos principais</b><ul>' + c.top.map(t => '<li>' + esc(t) + '</li>').join('') + '</ul>' +
    (c.files.length ? '<b>Notas de origem</b><ul>' + c.files.map(f => '<li class="m">' + esc(f) + '</li>').join('') + '</ul>' : '');
}

function openCommunity(id, focusConcept){
  const c = C.get(id); if(!c) return;
  level = 'concept'; current = id; back.style.display = '';
  crumb.textContent = c.name + ' · ' + c.size + ' conceitos';
  const ns = conceptsBy.get(id) || [];
  const ids = new Set(ns.map(n => n.id));
  const ls = D.plinks.filter(l => ids.has(l.source) && ids.has(l.target));
  G.graphData({ nodes: ns.map(n => ({...n})), links: ls.map(l => ({...l})) })
    .nodeLabel(n => '<b>' + esc(n.label) + '</b><br><span style="color:#93a4b8">' + esc(n.file) + '</span>')
    .nodeVal(n => 1 + n.deg)
    .nodeColor(n => n.deg >= 8 ? '#ffd166' : c.color)
    .linkWidth(l => l.conf === 'EXTRACTED' ? 1.2 : 0.4)
    .linkColor(l => l.conf === 'EXTRACTED' ? '#8fb3ff' : (l.conf === 'AMBIGUOUS' ? '#ff7b7b' : '#6b7a90'))
    .onNodeClick(n => infoConcept(n, ls))
    .onNodeHover(n => { el('g').style.cursor = n ? 'pointer' : null; });
  setLabels(ns.slice().sort((a,b)=>b.deg-a.deg).slice(0, 30).map(n => ({id: n.id, text: n.label.length > 42 ? n.label.slice(0,40)+'…' : n.label, big: n.deg >= 8})));
  infoCommunity(c);
  if(focusConcept) setTimeout(() => focusOn(focusConcept), 900);
}

function infoConcept(n, ls){
  const lab = id => (D.concepts.find(x => x.id === id) || {}).label || id;
  const rel = ls.filter(l => (l.source.id || l.source) === n.id || (l.target.id || l.target) === n.id);
  side.style.display = 'block';
  side.innerHTML = '<h2>' + esc(n.label) + '</h2><div class="m">' + esc(n.file) + '</div>' +
    '<div class="m">' + n.deg + ' ligações no grafo inteiro</div><b>Ligações nesta comunidade</b><ul>' +
    rel.map(l => { const s = l.source.id || l.source, t = l.target.id || l.target; const o = s === n.id ? t : s;
      return '<li>' + esc(l.rel) + ' → ' + esc(lab(o)) + ' <span class="m">(' + esc(l.conf) + ')</span></li>'; }).join('') + '</ul>';
  focusOn(n.id);
}

function focusOn(id){
  const n = G.graphData().nodes.find(x => x.id === id); if(!n || n.x === undefined) return;
  const d = 140, r = 1 + d / Math.hypot(n.x || 1, n.y || 1, n.z || 1);
  G.cameraPosition({x: n.x * r, y: n.y * r, z: n.z * r}, n, 1200);
}

back.onclick = () => showCommunities(current);

const q = el('q'), res = el('res');
q.oninput = () => {
  const s = q.value.trim().toLowerCase(); if(s.length < 2){ res.style.display = 'none'; return; }
  const cm = D.communities.filter(c => c.name.toLowerCase().includes(s)).slice(0, 8)
    .map(c => ({t: '◉ ' + c.name + ' (' + c.size + ')', go: () => openCommunity(c.id)}));
  const cc = D.concepts.filter(n => n.label.toLowerCase().includes(s)).sort((a,b) => b.deg - a.deg).slice(0, 14)
    .map(n => ({t: '· ' + n.label + ' — ' + (C.get(n.c) || {}).name, go: () => openCommunity(n.c, n.id)}));
  const all = cm.concat(cc);
  res.innerHTML = ''; all.forEach(x => { const d = document.createElement('div'); d.textContent = x.t; d.onclick = () => { res.style.display = 'none'; q.value = ''; x.go(); }; res.appendChild(d); });
  res.style.display = all.length ? 'block' : 'none';
};
const LB = el('labels'); let lbItems = [];
function setLabels(items){ LB.innerHTML=''; lbItems = items.map(it => { const d=document.createElement('div'); d.className='lb'+(it.big?' big':''); d.textContent=it.text; LB.appendChild(d); return {d, id: it.id}; }); }
(function tick(){
  const ns = G.graphData().nodes; const byId = new Map(ns.map(n=>[n.id,n]));
  const W = innerWidth, H = innerHeight;
  for(const it of lbItems){ const n = byId.get(it.id); if(!n || n.x===undefined){ it.d.style.display='none'; continue; }
    const p = G.graph2ScreenCoords(n.x, n.y, n.z);
    if(p.x<0||p.y<0||p.x>W||p.y>H){ it.d.style.display='none'; continue; }
    it.d.style.display=''; it.d.style.left=p.x+'px'; it.d.style.top=p.y+'px'; }
  requestAnimationFrame(tick);
})();

showCommunities();
</script></body></html>"""

out = os.path.join(ROOT, 'graphify-out', 'mapa-3d.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(PAGE.replace('__DATA__', data.replace('</', '<\\/')))
print('ok', out, len(communities), 'comunidades', len(concepts), 'conceitos', len(clinks), 'ligações entre comunidades')
