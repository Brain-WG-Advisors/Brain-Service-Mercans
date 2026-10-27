"""Gera o pacote do cérebro para o claude.ai: skill pessoal (.zip) + arquivos do Projeto "Brain Service".

Uso:  python scripts/gerar_pacote.py           # gera em publicar/AAAA-MM-DD/ e publicar/skill/
Rodar toda segunda (rotinas.md), depois de atualizar_tickets.py. Uso pessoal do usuário (decidido em 2026-10-27).

Sobe (prompts/publicacao.md): correcoes.md, fronteiras.md, 00-INDEX.md, servicos/*.md, paises/*.md, e um
painel-paises.md gerado das properties dos hubs (o .base do Obsidian não abre no claude.ai).
Não sobe: raw/, extracoes/, inventarios/, testes/ (gabarito), rascunhos/, revisoes/, scripts/, .env.
Checagem: falha se achar padrão de token/chave; lista o tamanho em palavras.

Depois:
  1. claude.ai → Configurações → Capacidades → Skills → "Upload skill" → publicar/skill/brain-service.zip
     (substitui a versão anterior; skill pessoal, só da conta do usuário).
  2. Projeto "Brain Service" → conhecimento: apagar os arquivos antigos e subir publicar/AAAA-MM-DD/*.
"""
import datetime
import glob
import io
import os
import re
import shutil
import sys
import zipfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOJE = datetime.date.today().isoformat()
SEGREDO = re.compile(r'(perm:[A-Za-z0-9._-]{20,}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY)')

SKILL_MD = '''---
name: brain-service
description: Knowledge brain of the payroll compliance service delivered to Mercans (research pipeline, artifacts CCG/WTC/DD/Report Specs/SIR/Payslip, design, support tickets). Use for ANY question about a country's artifacts, current versions, open tickets, past errors and corrections, decisions, or what belongs to other teams, and before drafting any ticket reply, e-mail or message about Mercans payroll compliance. Generated {hoje}.
---

# Brain Service (snapshot of {hoje})

Personal knowledge base of the compliance analyst. Notes are in Portuguese; answer in the user's language.
This is a SNAPSHOT generated on {hoje} from the local brain (Obsidian vault). Ticket states and versions may have
changed since: say "as of {hoje}" when citing them.

## FIRST: use this skill's files, not connectors
Everything needed (current artifact versions, WT classifications recorded in corrections, ticket states,
decisions) is in `references/`. Read `references/correcoes.md`, `references/painel-paises.md` and the country hub
BEFORE any other tool. Do NOT call Google Drive, Gmail or other connectors to look for artifacts (Drive is not
authorized in this account and the call blocks the answer). If the references do not contain the answer, say what
is missing and that it needs the live brain (Claude Code / local "brain" MCP).

## The brain wins over the web
- A correction in `correcoes.md` or a value/decision recorded in a hub beats anything found by web search. If a web
  source contradicts the brain, answer with the brain's version and add one line: "Note: <web source> says <X>; the
  brain's correction of <date> (<source>) says <Y>." Do not switch to the web answer.
- Design questions (Mercans regulation design, reg structure, accumulators, WT codes): answer FIRST with the design
  recorded in the brain (cite hub/correction and version). Alternatives only after that, labelled as suggestions.

## Read in this order
1. `references/correcoes.md` — errors already made and the correct version. ALWAYS read first. If the question
   touches an entry, the "Correto" column wins; "Errado" is the known wrong answer you must not repeat.
2. `references/painel-paises.md` — one line per country: stage, current artifact versions, open tickets.
3. `references/paises/<Country>.md` — the country hub (file names in Portuguese without accents, e.g.
   Espanha, Ucrania, Colombia, Franca, Holanda, Belgica, Costa-do-Marfim, Reino-Unido). Properties at the top
   hold current versions (highest version number = current) and open tickets.
4. The Mercans skill `payroll-compliance-<country>` for exact statutory values; `mercans-compliance-workflow`
   and `mercans-pipeline-methodology` for method.
5. `references/fronteiras.md` (other teams) and `references/servicos/*.md` (how each service works).

## How to answer (rules from the analyst, 2026-10-27)
- Direct answer first, only what was asked. Internal messages (manager, director, team chat): 1–3 sentences.
  Findings outside the question go on a separate line "Outside the request (not included): …".
- **Proof block** at the end of anything meant for third parties (ticket, e-mail, chat, artifact):
  question → answer item by item; each claim → primary source actually read (article/page/cell); mechanical
  check done; "Confidence X% — missing: …". Below 100% it is not presented as ready.
- If the user asks "are you sure?" / "100%?", re-check from scratch against the sources; do not repeat.
- Current artifact version = highest version number (not the newest file date). Cite "<artifact> v<x.y>".
- Never invent ticket numbers, versions, dates, article numbers or form boxes. No personal data of client
  employees.
- If the user says an answer was wrong, end with a CORRECTION CARD (Country | Artifact | Item / Wrong /
  Correct / Source level A-B-C / Where it happened) so it can go back to the brain.
- Live data (current ticket state, Drive files, scripts) is only available in Claude Code / the local "brain"
  MCP on the analyst's machine. If the question needs it, say so instead of guessing.
'''


def ler(p):
    return io.open(p, encoding='utf-8').read()


def props(t):
    if not t.startswith('---'):
        return {}
    out = {}
    for l in t.split('---', 2)[1].splitlines():
        if ':' in l:
            k, v = l.split(':', 1)
            out[k.strip()] = v.strip().strip('"')
    return out


def painel():
    linhas = ['# Painel de países (gerado em %s a partir das properties dos hubs)' % HOJE, '',
              '| País | Research | Design | Suporte | CCG | WTC | DD | Report Specs | SIR | Payslip | Obs. versões |',
              '|---|---|---|---|---|---|---|---|---|---|---|']
    for p in sorted(glob.glob(os.path.join(RAIZ, 'paises', '*.md'))):
        n = os.path.basename(p)[:-3]
        if n == 'README':
            continue
        d = props(ler(p))
        c = lambda k: (d.get(k, '') or '').replace('|', '/')
        linhas.append('| %s (%s) | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            n, c('codigo'), c('etapa_research'), c('etapa_design'), c('etapa_suporte'), c('ccg'), c('wtc'), c('dd'),
            c('report_specs'), c('sir'), c('payslip'), c('obs_versoes')))
    return '\n'.join(linhas) + '\n'


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    fontes = [('correcoes.md', 'correcoes.md'), ('fronteiras.md', 'fronteiras.md'), ('00-INDEX.md', '00-INDEX.md')]
    fontes += [(os.path.relpath(p, RAIZ), 'servicos/' + os.path.basename(p)) for p in sorted(glob.glob(os.path.join(RAIZ, 'servicos', '*.md')))]
    fontes += [(os.path.relpath(p, RAIZ), 'paises/' + os.path.basename(p)) for p in sorted(glob.glob(os.path.join(RAIZ, 'paises', '*.md'))) if not p.endswith('README.md')]
    conteudo = {destino: ler(os.path.join(RAIZ, origem)) for origem, destino in fontes}
    conteudo['painel-paises.md'] = painel()

    ruins = [d for d, t in conteudo.items() if SEGREDO.search(t)]
    if ruins:
        print('❌ padrão de credencial encontrado em: %s. Nada gerado.' % ', '.join(ruins))
        return 1

    proj = os.path.join(RAIZ, 'publicar', HOJE)
    if os.path.isdir(proj):
        shutil.rmtree(proj)
    os.makedirs(proj)
    for d, t in conteudo.items():
        io.open(os.path.join(proj, os.path.basename(d)), 'w', encoding='utf-8', newline='\n').write(t)

    sk = os.path.join(RAIZ, 'publicar', 'skill')
    os.makedirs(sk, exist_ok=True)
    z = os.path.join(sk, 'brain-service.zip')
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('brain-service/SKILL.md', SKILL_MD.format(hoje=HOJE))
        for d, t in conteudo.items():
            zf.writestr('brain-service/references/' + d, t)

    palavras = sum(len(t.split()) for t in conteudo.values())
    print('✅ Pacote de %s: %d arquivos, ~%d mil palavras' % (HOJE, len(conteudo), palavras // 1000))
    print('   Projeto: %s' % os.path.relpath(proj, RAIZ))
    print('   Skill:   %s (%d KB)' % (os.path.relpath(z, RAIZ), os.path.getsize(z) // 1024))
    return 0


if __name__ == '__main__':
    sys.exit(main())
