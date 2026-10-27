import re
FR=set("le la les des du une est sont pour avec dans par sur qui que ou si doit être cette ce ces aux au lorsque été pas ne il elle leur nombre montant valeur valeurs voir annexe obligatoire interdit facultatif présent travailleur employeur déclaration jour mois année heures minutes heure semaine trimestre élément entier positif exprimé caractères série moment début selon entre lequel laquelle dont commission paritaire ouvriers employés banques auxiliaire".split())
NL=set("het een van voor met zijn wordt worden niet deze die dat bij aan door naar als ook werkgever werknemer bijdrage jaar maand dag uren verplicht".split())
EN=set("the and of for with is are be to in on by if must when this that which not from or field value values amount mandatory employee employer see annex number date month year day hours code".split())
ISOL={"interdit","obligatoire","facultatif","non présent"}
def clean(s): s=re.sub(r"\([^()]*\)","",s); s=re.sub(r"[«“\"‘'][^»”\"’']*[»”\"’']","",s); return s.lower()
