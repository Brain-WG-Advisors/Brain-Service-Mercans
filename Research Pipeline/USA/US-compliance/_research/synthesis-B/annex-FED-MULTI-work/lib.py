# Shared helpers for the Synthesis-B annex_FED / annex_MULTI generator (no fetching).
import csv, json, re, os

BASE = r"C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance"
REG = {r['id']: r for r in csv.DictReader(open(os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv'), encoding='utf-8'))}
OK_STATUS = {'active', 'partial'}
OK_TIER = {'A.1', 'A.2', 'A.3', 'B'}


class Pack:
    def __init__(self, unit):
        self.unit = unit
        self.facts = []
        self.unresolved = []
        self.warnings = []
        self.ids = set()

    def f(self, domain, key, value, rid, ef=None, et=None, uom=None, cur=None, conf='high',
          vm='quoted from authority page', note=None, level=None):
        row = REG.get(rid)
        if row is None:
            raise SystemExit(f'missing register row {rid} for {key}')
        if row['status'] not in OK_STATUS:
            raise SystemExit(f'{rid} status {row["status"]} not citable ({key})')
        if row['tier'] not in OK_TIER:
            raise SystemExit(f'{rid} tier {row["tier"]} outside fact enum ({key})')
        if row['tier'] == 'B' and isinstance(value, (int, float)):
            raise SystemExit(f'tier B number {key}')
        ef_note = None
        if ef is None:
            ef = row['effective_from'] if re.match(r'^\d{4}-\d{2}-\d{2}$', row['effective_from'] or '') else None
        if ef is None:
            ef = '2026-01-01'
            ef_note = 'Register row carries no ISO effective_from; 2026-01-01 = in force for the whole build year (row not dated, rule not changed in 2026 per Stage 5).'
        if et is None:
            et = row['effective_to'] if re.match(r'^\d{4}-\d{2}-\d{2}$', row['effective_to'] or '') else None
        o = {'key': key, 'value': value}
        if uom: o['unit_of_measure'] = uom
        if cur: o['currency'] = cur
        o.update({'effective_from': ef, 'effective_to': et, 'register_id': rid, 'tier': row['tier'],
                  'verification_method': vm, 'authority': row['authority'] or 'n/a', 'url': row['url'] or row['local_file'],
                  'confidence': conf})
        notes = []
        if note: notes.append(note)
        if level: notes.append(f'LEVEL: {level}.')
        if row['status'] == 'partial':
            notes.append('[PARTIAL ROW: register status=partial; carry the partial flag]')
        if notes: o['note'] = ' '.join(notes)
        o['_domain'] = domain
        if ef_note: o['_ef_basis'] = ef_note
        if level: o['_level'] = level
        # number-in-row check
        if isinstance(value, (int, float)) and not isinstance(value, bool) and vm != 'derived arithmetically':
            txt = row['figure_or_rule_carried'].replace(',', '')
            cands = {str(value), f'{value:g}', f'{value:.2f}', f'{value:,.2f}'.replace(',', '')}
            if isinstance(value, float) and value.is_integer(): cands.add(str(int(value)))
            if not any(c in txt for c in cands):
                self.warnings.append(f'{key}={value} not literally in {rid}')
        self.facts.append(o)
        self.ids.add(rid)
        return o

    def u(self, key, why, close, attempted=None, blocking=False, rids=None):
        e = {'key': key, 'why': why, 'attempted': attempted or [], 'what_would_close_it': close, 'blocking': blocking}
        if rids:
            e['_related_register_ids'] = rids
            for r in rids:
                if r in REG: self.ids.add(r)
        self.unresolved.append(e)

    def dump(self, path, extra):
        d = {'schema_version': '1.4.0', 'artifact': 'CCG', 'unit': self.unit, 'code': 'US', 'year': 2026,
             'generated_on': '2026-11-02'}
        d.update(extra)
        pat = re.compile(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$')
        good = [x for x in self.facts if pat.match(x['register_id'])]
        bad = [x for x in self.facts if not pat.match(x['register_id'])]
        self.n_good, self.n_bad = len(good), len(bad)
        if bad:
            d['_note'] = ('Facts whose register_id (e.g. US-XX-P5-1-003) does not match the facts.schema register_id pattern '
                          '^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ are held, in identical fact shape, in _facts_pending_register_id_pattern. '
                          'They rest on active A.1/A.2/A.3 rows; they move into facts[] once the contract pattern accepts the multi-segment ids '
                          '(contract decision for the scaffolder/owner) - not hand-patched here.')
            d['_facts_pending_register_id_pattern'] = bad
        d['facts'] = good
        d['unresolved'] = self.unresolved
        with open(path, 'w', encoding='utf-8', newline='\n') as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
