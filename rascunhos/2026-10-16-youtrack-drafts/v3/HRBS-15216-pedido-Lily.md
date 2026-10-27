Hi @lli,

Please update the Ukraine country-level fields to the Data Dictionary for Nataliia's request (DD V4.0; current version V4.2, Country Fields):
- Contract Start Date, Oblast (Region), Street and Building Number, Postal Code, TSB Eligibility: optional
- 1C Personnel Number: removed
- ЄСВ Rate Effective Date: field name changed to SSC Rate Effective Date (code esv_rate_effective_date unchanged)
- Supporting Document Reference (D5): conditional mandatory, only when a D5 labour event is reported for the employee in the period
- SSC Rate: no field (the ESV rate comes from the existing Disability Group field)
- Ukrainian labels added

@vmane1@mercans.com @nahahan FYI.
