# -*- coding: utf-8 -*-
"""Pares DRAFT aprovado -> base (versão vigente anterior) -> nome final. Caminhos relativos à pasta da validação (VAL)."""
C = '../'  # Research Pipeline/Colombia/ relativo a VAL
PAIRS = [
 # (artefato, draft, base, final, versao)
 ('CCG', 'revisao/CCG/CO-CCG-001-v1.5-DRAFT-COVAL-2026-10-29.docx', 'revisao/CCG/_base-CO-CCG-001-v1.4.docx', 'CO-CCG-001-v1.5.docx', '1.5'),
 ('WTC', 'revisao/WTC/CO-WTC-001-v1.7-DRAFT-COVAL-2026-10-29.xlsx', 'revisao/WTC/base.xlsx', 'CO-WTC-001-v1.7.xlsx', '1.7'),
 ('DD', 'revisao/DD/CO-DD-001-v1.4-DRAFT-COVAL-2026-10-29.xlsx', C + '2026-10-22-auditoria-lote1/CO-DD-001-v1.3.xlsx', 'CO-DD-001-v1.4.xlsx', '1.4'),
 ('NE', 'revisao/NE/CO-DIAN-001-NominaElectronica-Spec-v1.1-DRAFT-COVAL-2026-10-29.xlsx', C + 'co-report-crosscheck/05-final/CO-DIAN-001-NominaElectronica-Spec.xlsx', 'specs/CO-DIAN-001-NominaElectronica-Spec.xlsx', '1.1'),
 ('F350', 'revisao/FORMS/CO-DIAN-002-Formulario350-Spec-v1.1-DRAFT-COVAL-2026-10-29.xlsx', C + 'co-report-crosscheck/05-final/CO-DIAN-002-Formulario350-Spec.xlsx', 'specs/CO-DIAN-002-Formulario350-Spec.xlsx', '1.1'),
 ('F220', 'revisao/FORMS/CO-DIAN-004-Formulario220-Spec-v1.1-DRAFT-COVAL-2026-10-29.xlsx', C + 'co-report-crosscheck/05-final/CO-DIAN-004-Formulario220-Spec.xlsx', 'specs/CO-DIAN-004-Formulario220-Spec.xlsx', '1.1'),
 ('F2276', 'revisao/FORMS/CO-DIAN-005-Formato2276-Spec-v1.1-DRAFT-COVAL-2026-10-29.xlsx', C + 'co-report-crosscheck/05-final/CO-DIAN-005-Formato2276-Spec.xlsx', 'specs/CO-DIAN-005-Formato2276-Spec.xlsx', '1.1'),
 ('CES006', 'revisao/FORMS/CO-CESANTIAS-006-ConsignacionAnual-Spec-v1.1-DRAFT-COVAL-2026-10-29.xlsx', C + 'co-report-crosscheck/05-final/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx', 'specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx', '1.1'),
 ('PILA003', 'revisao/PILA/CO-PILA-003-AportesSeguridadSocial-Spec-v1.1-DRAFT-COVAL-2026-10-29.xlsx', C + 'co-report-crosscheck/05-final/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx', 'specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx', '1.1'),
 ('PILA007', 'revisao/PILA/CO-PILA-007-AportesPensionados-Spec-v1.1-DRAFT-COVAL-2026-10-29.xlsx', C + 'co-report-crosscheck/05-final/CO-PILA-007-AportesPensionados-Spec.xlsx', 'specs/CO-PILA-007-AportesPensionados-Spec.xlsx', '1.1'),
 ('PAYSLIP', 'revisao/PAYSLIP/CO_Compliance_Payslip_Generator-v1.2-DRAFT-COVAL-2026-10-29.xlsx', 'C:/Users/instituto/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator-v1.1.xlsx', 'CO_Compliance_Payslip_Generator.xlsx', '1.2'),
]
