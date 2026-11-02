import sys
from lxml import etree
X='{http://www.w3.org/2001/XMLSchema}'
def flat(path,root_name):
    t=etree.parse(path).getroot()
    out=[]
    def walk_el(el,prefix,idx):
        name=el.get('name') or el.get('ref')
        mn=el.get('minOccurs','1'); mx=el.get('maxOccurs','1')
        p=prefix+'/'+name
        typ=el.get('type')
        ct=el.find(X+'complexType')
        out.append(('E',p,idx,mn,mx,typ or ('complex' if ct is not None else ''),''))
        if ct is not None:
            sc=ct.find(X+'simpleContent')
            if sc is not None:
                ex=sc.find(X+'extension'); out[-1]=('E',p,idx,mn,mx,ex.get('base'),'')
                for a in ex.findall(X+'attribute'): out.append(('A',p+'/@'+a.get('name'),0,'1' if a.get('use')=='required' else '0','1',a.get('type'),''))
            for a in ct.findall(X+'attribute'): out.append(('A',p+'/@'+a.get('name'),0,'1' if a.get('use')=='required' else '0','1',a.get('type'),''))
            seq=ct.find(X+'sequence')
            if seq is not None:
                for i,c in enumerate(seq.findall(X+'element')): walk_el(c,p,i+1)
    # root
    ct=t.find(X+'complexType')
    for a in ct.findall(X+'attribute'): out.append(('A','/'+root_name+'/@'+a.get('name'),0,'1' if a.get('use')=='required' else '0','1',a.get('type'),''))
    for i,c in enumerate(ct.find(X+'sequence').findall(X+'element')): walk_el(c,'/'+root_name,i+1)
    return out
if __name__=='__main__':
    base='C:/Users/instituto/Documents/brain-service/Research Pipeline/Colombia/CO-compliance/integration-sources/dian-ne/caja/Caja-de-Herramientas-Nomina-Electronica-V1-0/XSD/'
    for r in flat(base+'NominaIndividualElectronicaXSDV1.0.6.xsd','NominaIndividual'): print('|'.join(map(str,r)))
