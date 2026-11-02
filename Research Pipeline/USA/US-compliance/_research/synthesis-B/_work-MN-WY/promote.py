"""After the register_id pattern is loosened in facts.schema.json, move pending facts into facts[].
Usage: python -I promote.py <facts.json> [...]"""
import json, sys
for p in sys.argv[1:]:
    d = json.load(open(p, encoding='utf-8'))
    pend = d.pop('_facts_pending_register_id_pattern', [])
    d['facts'] += pend
    d['unresolved'] = [u for u in d['unresolved'] if not u['key'].endswith('.meta.register_id_pattern')]
    json.dump(d, open(p, 'w', encoding='utf-8', newline='\n'), indent=1, ensure_ascii=False)
    print(p, 'promoted', len(pend))
