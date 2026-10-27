"""Mede a eficiência das conversas por semana, a partir das conversas do Claude Code (só leitura).

Uso:  python scripts/medir_eficiencia.py            # tabela por semana ISO
      python scripts/medir_eficiencia.py --desde 2026-10-28

Conta só as mensagens do usuário (sem texto injetado, sem retomadas repetidas) e mede o que a análise de
2026-10-27 (revisoes/2026-10-27-padroes-prompts.md) apontou como ida e volta:
  - checagem de confiança ("100%", "tem certeza", "confere de novo");
  - correção ("não entendi", "mais direto", "não era isso", "de novo", "confuso");
  - aprovação pura ("sim", "ok", "pode seguir", "próximo"), que as regras novas devem reduzir.
Meta depois das regras de 27/10: checagem e aprovação pura em queda; mensagens por conversa em queda.
"""
import collections
import datetime
import glob
import io
import json
import os
import re
import sys

PROJ = os.path.join(os.path.expanduser('~'), '.claude', 'projects')
FORA = re.compile(r'Tentencias', re.I)
INJ = re.compile(r'^\s*<(system-reminder|task-notification|agent-message|command-|local-command|browser_instruction)|^\s*\[Request interrupted|^Caveat:|This session is being continued|^\s*Another Claude session')
CHECK = re.compile(r'100\s?%|confian[cç]a|tem certeza|certeza disso|confer(e|iu|ir) (de novo|novamente)|est[aá] (certo|correto)\?', re.I)
CORR = re.compile(r'n[aã]o entendi|n[aã]o era (isso|assim)|mais direto|mais curt|de novo|confus|errad|refa[zç]|n[aã]o (foi|est[aá]) (isso|certo)|encher lingui', re.I)
APROV = re.compile(r'^(sim|ok|okay|pode|pronto|certo|perfeito|isso|siga|segue|beleza|pr[oó]ximo)\b[^?]{0,40}$', re.I)


def main():
    desde = None
    if '--desde' in sys.argv:
        desde = sys.argv[sys.argv.index('--desde') + 1]
    sem = collections.defaultdict(lambda: collections.Counter())
    vistos = set()
    for f in glob.glob(os.path.join(PROJ, '*', '*.jsonl')):
        if FORA.search(f):
            continue
        sid = os.path.basename(f)
        for linha in io.open(f, encoding='utf-8', errors='replace'):
            try:
                r = json.loads(linha)
            except ValueError:
                continue
            if r.get('type') != 'user' or r.get('isMeta') or r.get('isSidechain'):
                continue
            c = r.get('message', {}).get('content')
            if isinstance(c, list):
                if any(isinstance(b, dict) and b.get('type') == 'tool_result' for b in c):
                    continue
                c = '\n'.join(b.get('text', '') for b in c if isinstance(b, dict) and b.get('type') == 'text')
            if not isinstance(c, str):
                continue
            t = re.sub(r'<system-reminder>.*?</system-reminder>', '', c, flags=re.S).strip()
            ts = (r.get('timestamp') or '')[:10]
            if not t or not ts or INJ.search(t) or (desde and ts < desde):
                continue
            chave = (ts, t[:200])
            if chave in vistos:
                continue
            vistos.add(chave)
            y, w, _ = datetime.date.fromisoformat(ts).isocalendar()
            k = '%d-S%02d' % (y, w)
            s = sem[k]
            s['msgs'] += 1
            s['sess:' + sid] = 1
            s['check'] += bool(CHECK.search(t))
            s['corr'] += bool(CORR.search(t))
            s['aprov'] += bool(APROV.match(t))
    sys.stdout.reconfigure(encoding='utf-8')
    print('| Semana | Mensagens | Conversas | Msgs/conversa | Checagem de confiança | Correção | Aprovação pura |')
    print('|---|---|---|---|---|---|---|')
    for k in sorted(sem):
        s = sem[k]
        n = s['msgs']
        ses = sum(1 for x in s if x.startswith('sess:'))
        pc = lambda v: '%d (%d%%)' % (v, round(100 * v / n)) if n else '0'
        print('| %s | %d | %d | %.0f | %s | %s | %s |' % (k, n, ses, n / max(ses, 1), pc(s['check']), pc(s['corr']), pc(s['aprov'])))
    return 0


if __name__ == '__main__':
    sys.exit(main())
