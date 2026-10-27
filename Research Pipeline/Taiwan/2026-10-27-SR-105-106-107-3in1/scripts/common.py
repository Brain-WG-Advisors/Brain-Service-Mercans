"""Texts shared by the three Taiwan 3-in-1 spec builds (SR-105/106/107), v1.1 2026-10-27."""

VC_DATE_SERIAL = 46322          # 2026-10-27 as Excel serial
VC_BY = "Wallisson Gomes"
VC_STATUS = "Under Review"   # round 2: value of the E13:E23 validation list
ELECTRONIC = "Electronic: Upload online "   # exact text of Options!A16 (list validation on Report Matrix B11)

CMO_HEADER = "C = Conditional, M = Mandatory, O = Optional"
TYPE_HEADER = "Data Type"

LI_ID_8 = ("$legal_entity_hr.labor_insure_id - first 8 characters, as text (keep leading zeros). "
           "DD V3.3 types this field as Number although the 9th character is a letter: "
           "TO BE CONFIRMED BY MOHIT/BA (DD also has insurance_certification_number, '8 digits + 1 text').")
LI_CHECK = "UPPERCASE of the 9th character of $legal_entity_hr.labor_insure_id"
NHI_UNIT = "PREPAD($legal_entity_hr.health_insure_id; 9; '0') - 9 digits as text"
NHI_DIV = "$legal_entity_hr.nhi_authority::key (DD V3.3, option mapper 'NHI Authority', keys 1-6)"

FOREIGN = ("Employee nationality: no field in DD V3.3 -> NEW DD FIELD (proposed): Employee Nationality "
           "(+ permanent-resident foreign professional flag for 'L'); TO BE CONFIRMED BY MOHIT/BA. "
           "Logic: nationality = TW -> blank; permanent-resident foreign professional (永居外專) -> 'L'; "
           "$hr.spouse_nationality = TW and nationality = CN -> '2'; "
           "$hr.spouse_nationality = TW and other nationality (incl. Hong Kong/Macau) -> '1'; otherwise 'Y'. "
           "Do not use $hr.residential_status (tax residency).")
FOREIGN_L_NOTE = ('For "Permanent-resident foreign professional" (永居外專), enter "L". '
                  '"Foreign spouse" ("1") includes Hong Kong/Macau spouses.')

NAME_RULE = ("Chinese names: nationals at least 2 characters, foreigners at least 1. "
             "English names: full name in full-width uppercase letters. Maximum 200 characters.")
NAME_MAP = ("IF(EQUALS(<foreign field>; ''); $hr.name; FULLWIDTH(UPPERCASE($hr.name))) - nationals: Chinese name "
            "($hr.name, DD V3.3 ID Information 'name' 名字); foreigners with English names: full name in full-width "
            "uppercase (e.g. ＤＡＶＩＤ), max. 200 characters. FULLWIDTH: TO BE CONFIRMED BY MOHIT/BA (no such "
            "function known in the formula engine; also confirm that $hr.name holds the English full name of foreigners).")

ID_LI = ("IF(EQUALS($hr.id_type::key; '3'); $hr.passport_number; $hr.id_card_number) - nationals: national ID; "
         "foreigners: ARC unified ID number (id_type 2) or passport (id_type 3), the same ID used at enrolment. "
         "Replaces $hr.residential_status (tax residency).")
ID_NHI = "IF(EQUALS($hr.id_type::key; '2'); $hr.id_card_number; '') - ARC unified ID number; blank for nationals."


def roc(field):
    return ("CONCAT(PREPAD(SUBTRACT(DATE_FORMAT(%s; 'yyyy'); 1911); 3; '0'); DATE_FORMAT(%s; 'MMdd'))"
            % (field, field))


BIRTH = roc("$person.birth_date")


SPECIAL_ID_TBC = ("TO BE CONFIRMED BY MOHIT/BA: DD V3.3 defines special_identity_code twice - ID Information ord. 36 "
                  "(mapper 'Special Identity Code', keys 1-8, A, B, S, T; used here) and Country Fields ord. 46 "
                  "(mapper 'Received Social Insurance Benefits Type (Occupational Accident)', keys 1, 2 only). "
                  "Confirm the field read by the report.")
TBC_LEN = "padding/width TO BE CONFIRMED BY MOHIT/BA"
NOT_PRESCRIBED = "Not prescribed by the official format guide (%s)."
INTRO_CHANNEL = ("The batch can be uploaded in the NHIA multi-certificate system (申報批次勞健合一 EXCEL) or in the BLI "
                 "e-service (合一申報, single and batch) (NHIA East Division flyer; BLI manual ch. 9, FAQ 2 and 6).")
