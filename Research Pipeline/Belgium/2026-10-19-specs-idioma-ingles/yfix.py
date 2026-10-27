# Review of the 56 yellow rows (2026-10-19): context-based term choices
import re
def fix(fr, en):
    o = en
    # tiers payant: official FR term on first occurrence
    if 'tiers payant' in fr and '(tiers payant)' not in o:
        o = o.replace('third-party payer', 'third-party payer (tiers payant)', 1)
    # accident de droit commun
    if 'droit commun' in fr and '(accident de droit commun)' not in o:
        o = o.replace('non-occupational accident', 'non-occupational accident (accident de droit commun)', 1)
    # consistent Civil Security volunteer
    o = o.replace('a Civil Protection volunteer', 'a Civil Security volunteer (volontaire de la Sécurité Civile)')
    # stray spaces inside quotes
    o = o.replace('" Public-sector employment data"', '"Public-sector employment data"')
    o = o.replace('" Reason for end of the statutory relationship"', '"Reason for end of the statutory relationship"')
    # RCC / RCIC: gloss on first occurrence when the cell has none
    if re.search(r'\bRCC\b', o) and 'company supplement' not in o:
        o = re.sub(r'\bRCC\b', 'RCC (unemployment with company supplement)', o, count=1)
    if re.search(r'\bRCIC\b', o) and 'older workers' not in o:
        o = re.sub(r'\bRCIC\b', 'RCIC (unemployment with supplementary allowance for older workers)', o, count=1)
    if 'étage' in fr and 'étage' not in o:
        o = o.replace('"floor"', '"floor" (étage)', 1)
    o = o.replace('under the administration of a bankruptcy trustee (sous curatelle)', 'under bankruptcy administration (sous curatelle)')
    return o
