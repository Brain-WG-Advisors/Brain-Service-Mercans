import os, importlib
from build_co_specs import build_workbook, OUTPUT_DIR
TARGETS=[('co_r1_sheets','CO-DIAN-001-NominaElectronica-Spec.xlsx'),
         ('co_r2_sheets','CO-DIAN-002-Formulario350-Spec.xlsx'),
         ('co_r3_sheets','CO-PILA-003-AportesSeguridadSocial-Spec.xlsx'),
         ('co_r4_sheets','CO-DIAN-004-Formulario220-Spec.xlsx'),
         ('co_r5_sheets','CO-DIAN-005-Formato2276-Spec.xlsx'),
         ('co_r6_sheets','CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx')]
for mod,out in TARGETS:
    m=importlib.import_module(mod)
    build_workbook(m.CFG).save(os.path.join(OUTPUT_DIR,out))
    print('saved',out)
