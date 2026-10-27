# SR-108: draft comment (EN). NOT posted. For user review.

@mjain Spec review done: v1.2 (Draft), changes highlighted in light blue. Based on the NHIA TXT layout for income type 62 and the Supplementary Premium Regulations.

**Verdict:** the spec is now complete except for the 3 questions below (also in column K of the spec); the February test output would be rejected by NHIA (UBN missing, so all fields shift 8 positions; negative amounts; zero bonus total).

**Changes**
1. Section C totals (21–40, 41–56) = sum of the detail lines in the file, not YTD; Total Entries (12–20) = number of detail lines.
2. UBN (2–9) = company registration number in sections A, B and C; positions 93–101 are the 9-character NHI insured unit code, not the UBN.
3. Dates in ROC format (yyymm / yyymmdd); Income Payment Date (22–28) proposed as the actual payment date (engine variable to confirm).
4. Declaration Number: employer numbering, unique per line (UBN + 62 + payment date + serial), left-aligned and padded with spaces.
5. Frequency monthly with the premium payment (or annual by 31 January); filing electronic; encoding BIG5; names in full-width; numeric fields never negative.

**Please confirm**
1. Does the bonus base feeding 2558 include the 6220x series (Bonus Annual/Referral)? 58009 currently sums 6221x and 6222x only.
2. Insured amount (102–107): PE 58139 is not in WTC V2.8. Should it be 64550?
3. Which fields hold the NHI insured unit code (proposed health_insure_id), the payroll payment date and the contact person name?
