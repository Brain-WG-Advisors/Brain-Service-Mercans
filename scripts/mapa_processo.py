"""Gera graphify-out/mapa-processo.html: o processo do serviço, país a país, em 3D.

Colunas (da esquerda para a direita) = etapas do serviço:
  Research Pipeline (CCG → WTC → DD → Specs → SIR → Payslip → Skill) → Design → Produção (outro time) → Suporte,
  com Internal Certification ao lado.
Linhas = países (cada um com sua cor), dos mais avançados no processo para os menos.
Ligações: fluxo entre etapas (setas), correções que voltaram do Suporte ao Research (vermelho),
países com o mesmo cliente (dourado).
Fonte: os hubs (paises/*.md: Situação, Artefatos entregues, Suporte, Internal Certification, Entregas),
correcoes.md e o estado dos tickets em graphify-out/.hub_ticket_states.json (se existir).
Uso: python scripts/mapa_processo.py
"""
import re, io, os, glob, json, colorsys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

ARTS = [('CCG', ['ccg', 'configuration guide']), ('WTC', ['wtc', 'wage type']), ('DD', ['dd ', 'data dictionary', 'dd(', 'dd-']),
        ('Specs', ['spec', 'report']), ('SIR', ['sir', 'statutory integration']), ('Payslip', ['payslip']),
        ('Skill', ['skill'])]
BOUND = chr(92) + 'b'
CLIENTS = ['Baker Hughes', 'Mammoet', 'STG', 'Ericsson', 'GSK', 'Henkel', 'Mastercard', 'Accenture', 'Altium',
           'Omnicom', 'Quest Software', 'Sherwin Williams', 'TBWA', 'Excerpta', 'McDermott', 'Mondelez']

def emo(s):
    for e in ('✅', '🔄', '⏳'):
        if e in s:
            return e
    return '—' if '—' in s or not s.strip() else '?'

def section(t, name):
    m = re.search(r'^## ' + re.escape(name) + r'[^\n]*\n(.*?)(?=^## |\Z)', t, re.S | re.M)
    return m.group(1) if m else ''

try:
    TST = json.load(open('graphify-out/.hub_ticket_states.json', encoding='utf-8'))
except Exception:
    TST = {}
CLOSED = ('resolved', 'closed', 'done', 'fixed', 'verified', 'rejected')

cor = io.open('correcoes.md', encoding='utf-8').read()
corr_by = collections.Counter(re.findall(r'^\| [^|]*\| \[\[([^\]|]+)', cor, re.M))

countries = []
for p in sorted(glob.glob('paises/*.md')):
    h = os.path.basename(p)[:-3]
    if h == 'README':
        continue
    t = io.open(p, encoding='utf-8').read()
    title = t.splitlines()[0].lstrip('# ').strip()
    st = {}
    for ln in section(t, 'Situação').splitlines():
        if not ln.startswith('|') or '---' in ln:
            continue
        c = [x.strip() for x in ln.strip('|').split('|')]
        k = c[0].lower()
        key = ('research' if 'research' in k else 'design' if 'design' in k else 'suporte' if 'suporte' in k
               else 'producao' if 'produ' in k else 'ic' if ('certification' in k or 'analise' in k) else None)
        if key:
            st[key] = {'s': emo(c[1]) if len(c) > 1 else '?', 'd': c[2] if len(c) > 2 else '',
                       'o': (c[3] if len(c) > 3 else '')[:300]}
    arts = collections.OrderedDict()
    for ln in section(t, 'Artefatos entregues').splitlines():
        if not ln.startswith('|') or '---' in ln or ln.lower().startswith('| artefato'):
            continue
        c = [x.strip() for x in ln.strip('|').split('|')]
        name = c[0].lower()
        if 'histórico' in name or 'historico' in name:
            continue
        for a, kws in ARTS:
            if any(k in ' ' + name + ' ' for k in kws):
                arts.setdefault(a, []).append({'n': c[0][:90], 'v': (c[1] if len(c) > 1 else '')[:60]})
                break
    sup = section(t, 'Suporte (tickets)')
    tks = sorted(set(re.findall(r'\b((?:HRBS|CT|SR)-\d+)', sup)))
    open_t = [x for x in tks if x in TST and TST[x][0].lower() not in CLOSED]
    ic_sec = section(t, 'Internal Certification')
    ic = bool(ic_sec.strip()) or ('ic' in st)
    ent = len(re.findall(r'\|conferência\]\]', t))
    clients = sorted({c for c in CLIENTS if re.search(BOUND + re.escape(c) + BOUND, t)})
    stage_s = {k: st.get(k, {}).get('s', '?') for k in ('research', 'design', 'producao', 'suporte')}
    score = (sum({'✅': 2, '🔄': 1}.get(stage_s[k], 0) for k in ('research', 'design', 'suporte')) + len(arts) * 0.4
             + min(len(tks), 20) * 0.1 + min(corr_by.get(h, 0), 40) * 0.05 + ent * 0.3)
    countries.append({'id': h, 'name': title.split('(')[0].strip(), 'st': st, 'stages': stage_s,
                      'arts': arts, 'tickets': tks, 'open': open_t, 'ic': ic, 'corr': corr_by.get(h, 0),
                      'ent': ent, 'clients': clients, 'score': round(score, 2), 'file': p.replace(os.sep, '/')})

countries.sort(key=lambda c: (-c['score'], c['name']))
for i, c in enumerate(countries):
    h = (i * 0.61803398875) % 1.0
    r, g, b = colorsys.hls_to_rgb(h, 0.6, 0.7)
    c['color'] = '#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255))

shared = collections.defaultdict(list)
for c in countries:
    for cl in c['clients']:
        shared[cl].append(c['id'])
client_links = [{'client': cl, 'a': ids[i], 'b': ids[j]} for cl, ids in shared.items() if len(ids) > 1
                for i in range(len(ids)) for j in range(i + 1, len(ids))]

data = json.dumps({'arts': [a for a, _ in ARTS], 'countries': countries, 'clientLinks': client_links},
                  ensure_ascii=False)

PAGE = r"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mapa do processo</title>
<style>
:root{--panel:rgba(16,22,34,.9);--ink:#eef3fa;--muted:#9fb0c6;--line:rgba(120,145,180,.28);--accent:#7cb4ff}
html,body{margin:0;height:100%;color:var(--ink);font:14px/1.45 "Segoe UI",system-ui,Roboto,sans-serif;overflow:hidden;
  background:radial-gradient(ellipse at 50% 35%,#16213a 0%,#0a0f1c 60%,#05080f 100%)}
#g{position:fixed;inset:0}
.box{background:var(--panel);border:1px solid var(--line);border-radius:12px;backdrop-filter:blur(6px);box-shadow:0 8px 30px rgba(0,0,0,.35)}
#top{position:fixed;top:14px;left:14px;right:14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap;z-index:3}
#title{font-weight:650;font-size:16px;padding:8px 12px}
#title span{color:var(--muted);font-weight:400;font-size:13px;margin-left:8px}
#q{flex:1;min-width:180px;max-width:320px;padding:10px 12px;border-radius:10px;border:1px solid var(--line);background:var(--panel);color:var(--ink);outline:none}
button{padding:9px 12px;border-radius:10px;border:1px solid var(--line);background:var(--panel);color:var(--ink);cursor:pointer}
button.on{border-color:var(--accent);color:var(--accent)}
#side{position:fixed;top:72px;right:14px;width:360px;max-width:calc(100% - 28px);max-height:calc(100% - 100px);overflow:auto;padding:14px 16px;z-index:3;display:none}
#side h2{font-size:18px;margin:0 0 4px}
#side .m{color:var(--muted);font-size:12px}
#side table{border-collapse:collapse;width:100%;margin:6px 0 10px;font-size:13px}
#side td{border-bottom:1px solid var(--line);padding:4px 4px;vertical-align:top}
#legend{position:fixed;left:14px;bottom:14px;padding:10px 12px;z-index:3;font-size:12.5px;max-width:330px;line-height:1.6}
#legend i{display:inline-block;width:18px;height:3px;vertical-align:middle;margin-right:6px;border-radius:2px}
#labels{position:fixed;inset:0;pointer-events:none;z-index:2}
.lb{position:absolute;white-space:nowrap;color:#fff;text-shadow:0 1px 3px #000}
.col{transform:translate(-50%,-50%);font-size:14px;font-weight:700;letter-spacing:.3px;padding:3px 9px;border-radius:8px;background:rgba(8,12,22,.6);border:1px solid var(--line)}
.col.sub{font-size:11.5px;font-weight:600;color:#cfe0f5}
.col.other{color:#9fb0c6;border-style:dashed}
.row{transform:translate(-100%,-50%);font-size:12.5px;font-weight:600;padding:1px 8px 1px 6px;border-left:4px solid}
@media (max-width:700px){#legend{display:none}#side{top:auto;bottom:14px;max-height:45%}}
</style></head><body>
<div id="g"></div><div id="labels"></div>
<div id="top">
  <div id="title" class="box">Mapa do processo<span id="crumb"></span></div>
  <button id="bTop" class="on">Países com trabalho</button><button id="bAll">Todos os países</button>
  <input id="q" placeholder="Ir para país…" autocomplete="off">
</div>
<div id="side" class="box"></div>
<div id="legend" class="box">
  <b>Como ler</b><br>
  Linha = país (cor própria) · coluna = etapa do serviço<br>
  Esfera cheia = ✅ entregue · menor e clara = 🔄 em andamento · cinza = ⏳ não iniciado<br>
  <i style="background:#cfd8e6"></i>fluxo entre etapas (seta)<br>
  <i style="background:#ff5d5d"></i>correção que voltou do Suporte ao Research<br>
  <i style="background:#f4c542"></i>mesmo cliente em países diferentes<br>
  Clique numa esfera para ver status, artefatos, tickets e correções
</div>
<script src="https://cdn.jsdelivr.net/npm/3d-force-graph@1.73.4/dist/3d-force-graph.min.js"></script>
<script>
const D = __DATA__;
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const el = id => document.getElementById(id);
const COLS = [].concat(D.arts.map(a => ({k: 'a:' + a, label: a, group: 'research'})),
  [{k: 'design', label: 'Design'}, {k: 'producao', label: 'Produção ⟶ outro time', other: true}, {k: 'suporte', label: 'Suporte'}, {k: 'ic', label: 'Internal Certification'}]);
const DX = 46, GAP = 70, DY = 34;
const SX = 165;
const colX = k => { const i = COLS.findIndex(c => c.k === k), na = D.arts.length; return i < na ? i * DX : (na - 1) * DX + GAP + (i - na) * SX + (k === 'ic' ? 30 : 0); };
let mode = 'top';

function mix(hex, t){ const n = parseInt(hex.slice(1), 16), r = n >> 16, g = (n >> 8) & 255, b = n & 255;
  const f = v => Math.round(v + (255 - v) * t).toString(16).padStart(2, '0'); return '#' + f(r) + f(g) + f(b); }

function build(){
  const list = D.countries.filter(c => mode === 'all' || Object.keys(c.arts).length || c.tickets.length || ['✅','🔄'].includes(c.stages.design) || ['✅','🔄'].includes(c.stages.suporte));
  const nodes = [], links = [], rowY = new Map();
  list.forEach((c, i) => {
    const y = -i * DY; rowY.set(c.id, y);
    nodes.push({id: c.id + '|row', c, kind: 'row', fx: -70, fy: y, fz: 0, val: 3 + Math.min(10, c.tickets.length / 2)});
    let prev = null;
    D.arts.forEach(a => {
      if(!c.arts[a]) return;
      const id = c.id + '|a:' + a; const rs = c.stages.research;
      nodes.push({id, c, kind: 'art', art: a, fx: colX('a:' + a), fy: y, fz: 0, val: 2.4, status: rs === '✅' ? '✅' : '🔄'});
      if(prev) links.push({source: prev, target: id, kind: 'flow', c: c.color}); prev = id;
    });
    ['design', 'producao', 'suporte'].forEach(k => {
      const s = c.stages[k]; if(k === 'producao' && s !== '✅' && s !== '🔄') return;
      const id = c.id + '|' + k;
      const v = k === 'suporte' ? 2 + Math.min(8, c.tickets.length / 2) : 3;
      nodes.push({id, c, kind: k, fx: colX(k), fy: y, fz: 0, val: v, status: s});
      if(prev && (s === '✅' || s === '🔄')) links.push({source: prev, target: id, kind: 'flow', c: c.color});
      if(s === '✅' || s === '🔄') prev = id;
    });
    if(c.ic){ const id = c.id + '|ic'; nodes.push({id, c, kind: 'ic', fx: colX('ic'), fy: y, fz: 0, val: 3, status: '✅'}); }
    if(c.corr){ const first = D.arts.find(a => c.arts[a]); const from = c.id + '|suporte';
      if(first && nodes.find(n => n.id === from)) links.push({source: from, target: c.id + '|a:' + first, kind: 'corr', w: c.corr}); }
  });
  D.clientLinks.forEach(l => { if(rowY.has(l.a) && rowY.has(l.b)) links.push({source: l.a + '|row', target: l.b + '|row', kind: 'client', client: l.client}); });
  nodes.forEach(n => { n.x = n.fx; n.y = n.fy; n.z = n.fz; });
  return {nodes, links, list};
}

const G = ForceGraph3D({controlType: 'orbit'})(el('g'))
  .backgroundColor('rgba(0,0,0,0)').showNavInfo(false).nodeResolution(20).nodeRelSize(4.6).nodeOpacity(0.97)
  .nodeVal(n => n.val)
  .nodeColor(n => n.kind === 'row' ? n.c.color : (n.status === '✅' ? n.c.color : n.status === '🔄' ? mix(n.c.color, .55) : '#3a4558'))
  .nodeLabel(n => '<b>' + esc(n.c.name) + '</b> · ' + esc(n.kind === 'art' ? n.art : n.kind === 'row' ? 'país' : n.kind) + (n.status ? ' ' + n.status : ''))
  .linkWidth(l => l.kind === 'flow' ? 2.6 : l.kind === 'corr' ? 1.6 + Math.min(4, l.w / 6) : 1.8)
  .linkColor(l => l.kind === 'flow' ? mix(l.c || '#cfd8e6', .25) : l.kind === 'corr' ? 'rgba(255,93,93,0.9)' : 'rgba(244,197,66,0.75)')
  .linkCurvature(l => l.kind === 'corr' ? 0.35 : l.kind === 'client' ? 0.25 : 0)
  .linkCurveRotation(l => l.kind === 'corr' ? Math.PI / 2 : 0)
  .linkDirectionalArrowLength(l => l.kind === 'flow' ? 4 : l.kind === 'corr' ? 5 : 0)
  .linkDirectionalArrowRelPos(1)
  .linkDirectionalParticles(l => l.kind === 'corr' ? 2 : 0).linkDirectionalParticleWidth(2.2)
  .linkLabel(l => l.kind === 'corr' ? l.w + ' correções registradas' : l.kind === 'client' ? 'Cliente em comum: ' + esc(l.client) : '')
  .onNodeClick(n => info(n.c))
  .onNodeHover(n => { el('g').style.cursor = n ? 'pointer' : null; });
G.d3Force('charge', null); G.d3Force('center', null); G.d3Force('link').strength(0);
G.cooldownTicks(1);

const LB = el('labels'); let items = [];
function labels(list){
  LB.innerHTML = ''; items = [];
  const add = (cls, text, pos, style) => { const d = document.createElement('div'); d.className = 'lb ' + cls; d.textContent = text; if(style) d.style.cssText = style; LB.appendChild(d); items.push({d, pos}); };
  const top = 30;
  add('col', 'Research Pipeline', {x: (colX('a:' + D.arts[0]) + colX('a:' + D.arts[D.arts.length - 1])) / 2, y: top + 34, z: 0});
  COLS.forEach(c => add('col' + (c.group ? ' sub' : '') + (c.other ? ' other' : ''), c.label, {x: colX(c.k), y: top, z: 0}));
  list.forEach((c, i) => add('row', c.name + (c.open.length ? '  ·  ' + c.open.length + ' abertos' : ''), {x: -82, y: -i * DY, z: 0}, 'border-color:' + c.color));
}
(function tick(){ const W = innerWidth, H = innerHeight;
  for(const it of items){ const p = G.graph2ScreenCoords(it.pos.x, it.pos.y, it.pos.z);
    if(p.x < -50 || p.y < 0 || p.x > W + 50 || p.y > H){ it.d.style.display = 'none'; continue; }
    it.d.style.display = ''; it.d.style.left = p.x + 'px'; it.d.style.top = p.y + 'px'; }
  requestAnimationFrame(tick); })();

function info(c){
  const S = (k, n) => { const s = c.st[k] || {}; return '<tr><td>' + n + '</td><td>' + (s.s || '—') + '</td><td class="m">' + esc((s.d || '') + (s.o ? ' · ' + s.o : '')) + '</td></tr>'; };
  const arts = D.arts.filter(a => c.arts[a]).map(a => '<tr><td>' + a + '</td><td colspan="2">' + c.arts[a].map(x => esc(x.n) + (x.v ? ' <span class="m">(' + esc(x.v) + ')</span>' : '')).join('<br>') + '</td></tr>').join('');
  el('side').style.display = 'block';
  el('side').innerHTML = '<h2><span style="color:' + c.color + '">●</span> ' + esc(c.name) + '</h2><div class="m">' + esc(c.file) + '</div>' +
    '<b>Etapas</b><table>' + S('research', 'Research') + S('design', 'Design') + S('producao', 'Produção') + S('suporte', 'Suporte') + '</table>' +
    '<b>Artefatos (Research)</b><table>' + (arts || '<tr><td class="m">nenhum registrado no hub</td></tr>') + '</table>' +
    '<b>Suporte</b><div class="m">' + c.tickets.length + ' tickets no hub · ' + c.open.length + ' abertos (API 27/10)' + (c.open.length ? ': ' + esc(c.open.join(', ')) : '') + '</div>' +
    '<b>Correções registradas</b><div class="m">' + c.corr + ' em correcoes.md</div>' +
    '<b>Entregas com conferência</b><div class="m">' + c.ent + '</div>' +
    (c.ic ? '<b>Internal Certification</b><div class="m">sim (seção no hub)</div>' : '') +
    (c.clients.length ? '<b>Clientes citados</b><div class="m">' + esc(c.clients.join(', ')) + '</div>' : '');
}

function render(){
  const {nodes, links, list} = build();
  G.graphData({nodes, links});
  labels(list);
  el('crumb').textContent = list.length + ' países · ' + (mode === 'top' ? 'só os que têm trabalho registrado' : 'todos');
  const h = list.length * DY, w = colX('ic') + 160;
  const cx = w / 2 - 110, cy = -h / 2 + 95;
  G.cameraPosition({x: cx, y: cy, z: Math.max(h * 1.05, w * 0.75) + 120}, {x: cx, y: cy, z: 0}, 800);
}
el('bTop').onclick = () => { mode = 'top'; el('bTop').classList.add('on'); el('bAll').classList.remove('on'); render(); };
el('bAll').onclick = () => { mode = 'all'; el('bAll').classList.add('on'); el('bTop').classList.remove('on'); render(); };
el('q').onchange = el('q').oninput = () => { const s = el('q').value.trim().toLowerCase(); if(s.length < 3) return;
  const c = D.countries.find(x => x.name.toLowerCase().startsWith(s) || x.id.toLowerCase().startsWith(s)); if(!c) return;
  const n = G.graphData().nodes.find(x => x.id === c.id + '|row'); if(!n) return;
  info(c); G.cameraPosition({x: n.fx + 220, y: n.fy, z: 260}, {x: n.fx + 220, y: n.fy, z: 0}, 900); };
render();
</script></body></html>"""

out = os.path.join(ROOT, 'graphify-out', 'mapa-processo.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(PAGE.replace('__DATA__', data.replace('</', '<\\/')))
top = [c for c in countries if c['arts'] or c['tickets']]
print('ok', len(countries), 'países;', len(top), 'com trabalho;', len(client_links), 'ligações de cliente')
for c in countries[:8]:
    print(' ', c['name'], c['stages'], 'arts', list(c['arts']), 'tickets', len(c['tickets']), 'abertos', len(c['open']), 'corr', c['corr'], 'clientes', c['clients'])
