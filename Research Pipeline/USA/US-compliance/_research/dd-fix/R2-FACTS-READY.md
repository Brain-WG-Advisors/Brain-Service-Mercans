# R2-FACTS-READY (source hunter, 2026-11-03)
Backups: `_research/dd-fix/backup/*.20261103-r2`. validate_contract facts and --all: PASS. No web use.

- dd.oh.municipal.code_list, dd.in.county_code.list, dd.md.county_code.list: trailing clause "; list in 00-official-sources/code-tables/...json" removed from `value`; the path now sits in non-printing `_local_table`. Rest of each value unchanged. Regenerate F338, F344, F347.
- New key dd.ky.locality.lexington_name = "Lexington-Fayette Urban County Government occupational license fee" (US-KYS5-024 copy: "The Lexington-Fayette Urban County Government assesses an occupational license fee"). No rate. Cite it on F107; the rate key dd.ky.locality.lexington stays for the WTC.
- Finding 2 (dd_recon qualifiers) is the builder's.
