import csv, json, re, collections
from urllib.parse import urlparse
T = "2026-11-04"
rows = [r for r in csv.DictReader(open('00-official-sources/legal-basis-register.csv', encoding='utf-8')) if r['status'].lower() not in ('superseded', 'withdrawn', 'rejected')]
G = collections.defaultdict(list)
mx = {}
for r in rows:
    g = re.match(r'US-([A-Z]+)', r['id']).group(1)[:2]
    a = r['authority'].strip()
    if not a:
        continue
    G[g].append((a, r))
    mx[g] = max(mx.get(g, ''), r['retrieved_on'])
OK = "fetched and read 2026-11-04: no 2026 item on employer withholding / UI rates or wage base / minimum wage / paid leave in the items visible on the page"
def BL(why):
    return "official page NOT readable by WebFetch (" + why + "); not a clean sweep. Checked instead: local-copy dates in the register (latest retrieved_on {mx}). Open requirement: browser re-read of the agency newsroom before release (Test 0 browser re-verification already pending)"
NA = "no news-page fetch attempted within the ~60-fetch budget (state hosts blocked often: 403/404/refused). Checked instead: local-copy dates in the register (latest retrieved_on {mx}). Open requirement: browser re-read of the agency newsroom before release"
fetched = {
 'AK': ("https://tax.alaska.gov/", OK), 'AL': ("https://www.revenue.alabama.gov/news/", OK), 'AR': ("https://www.dfa.arkansas.gov/news/", OK),
 'AZ': ("https://azdor.gov/news", BL("HTTP 403")), 'CA': ("https://edd.ca.gov/en/about_edd/news_releases_and_announcements/", OK),
 'CO': ("https://tax.colorado.gov/news", BL("HTTP 404")), 'CT': ("https://portal.ct.gov/drs/newsroom", BL("HTTP 404")),
 'DC': ("https://otr.cfo.dc.gov/page/tax-notices", BL("HTTP 404")), 'DE': ("https://revenue.delaware.gov/news/", BL("HTTP 404")),
 'FL': ("https://floridarevenue.com/Pages/news.aspx", OK + " (first 100,000 of 159,832 characters read)"), 'GA': ("https://dor.georgia.gov/news", OK),
 'HI': ("https://tax.hawaii.gov/news/", BL("page returned section headers without items")), 'IA': ("https://revenue.iowa.gov/news", BL("HTTP 404")),
 'ID': ("https://tax.idaho.gov/", BL("connection refused")), 'IL': ("https://tax.illinois.gov/", BL("host not found")),
 'IN': ("https://www.in.gov/dor/", BL("connection refused")), 'KS': ("https://www.ksrevenue.gov/", BL("connection refused")),
 'KY': ("https://revenue.ky.gov/", OK), 'LA': ("https://revenue.louisiana.gov/", BL("HTTP 403")),
 'MA': ("https://www.mass.gov/orgs/massachusetts-department-of-revenue", BL("HTTP 403")),
 'MD': ("https://www.marylandcomptroller.gov/", OK), 'ME': ("https://www.maine.gov/revenue/", BL("HTTP 403")), 'MI': ("https://www.michigan.gov/treasury", BL("HTTP 403")),
 'MN': ("https://www.revenue.state.mn.us/", OK), 'MO': ("https://dor.mo.gov/", BL("HTTP 403")),
 'MS': ("https://www.dor.ms.gov/", OK + " (only 2026 withholding item: gaming-winnings notice of 2026-09-28, not employer payroll withholding)"),
 'NJ': ("https://www.nj.gov/treasury/taxation/", OK), 'NY': ("https://www.tax.ny.gov/", OK), 'OH': ("https://tax.ohio.gov/", BL("HTTP 404")),
 'PA': ("https://www.pa.gov/agencies/revenue.html", OK), 'TX': ("https://www.twc.texas.gov/news", BL("HTTP 403")), 'VA': ("https://www.tax.virginia.gov/", OK),
 'VT': ("https://tax.vermont.gov/", OK), 'WA': ("https://esd.wa.gov/newsroom", OK + " except the hit listed"), 'WI': ("https://www.revenue.wi.gov/", BL("301 redirect not followed")),
 'NC': ("https://www.ncdor.gov/", OK), 'NM': ("https://www.tax.newmexico.gov/", OK),
 'SC': ("https://dor.sc.gov/", OK + " (only item: W-2/1099 upload by 2026-01-31, deadline already passed)"), 'UT': ("https://tax.utah.gov/", BL("HTTP 403")),
}
sweeps = []
def entry(bul, auths, url, res, hits=None, q="2026 payroll news: employer withholding, UI rates/wage base, minimum wage, paid leave, reporting forms"):
    sweeps.append({"bulletin": bul, "authority": " | ".join(sorted(set(auths))), "url": url, "searched_on": T, "period_from": "2026-01-01", "period_to": T, "query": q, "result": res, "hits": hits or []})
for g, lst in sorted(G.items()):
    auths = [a for a, _ in lst]
    m = mx[g]
    if g == 'FE':
        b = {'IRS': [], 'DOL': [], 'SSA': [], 'OTHER': []}
        for a in auths:
            l = a.lower()
            if 'internal revenue' in l or l.startswith('irs') or 'treasury' in l:
                b['IRS'].append(a)
            elif 'labor' in l or 'dol' in l.split() or 'employment and training' in l or 'wage and hour' in l:
                b['DOL'].append(a)
            elif 'social security' in l or 'ssa' in l.split():
                b['SSA'].append(a)
            else:
                b['OTHER'].append(a)
        entry("IRS newsroom / forms and publications pages (federal)", b['IRS'], "https://www.irs.gov/forms-pubs/about-publication-15-t",
              "Pub 15-T page read 2026-11-04: 2026 revision current, 'Recent developments: None at this time', last review 28-Jun-2026; no 2027 edition announced. irs.gov current-month news releases read: no payroll item. The 2027 inflation-adjustment Rev. Proc. is scheduled for October 2026 and was not found published (irs.gov search 2026-11-04); Rev. Proc. 2026-24 (2027 HSA amounts) is published.",
              [{"instrument": "Rev. Proc. 2026-24 (2027 HSA limits)", "published": "2026", "affects": ["US-FED-002"], "action": "not relevant: 2027 amount, outside the 2026 build year; recorded under next_year"}])
        entry("DOL OUI FUTA credit-reduction page and DOL WHD state minimum wage page", b['DOL'], "https://oui.doleta.gov/unemploy/futa_credit.asp",
              "OUI page read 2026-11-04 (last updated 2026-09-11): only 'Potential 2026 Credit Reductions' is published; the final determination is on Nov. 10. WHD state minimum wage page read (last updated 2026-07-01).",
              [{"instrument": "DOL OUI Potential 2026 Credit Reductions", "published": "2026-09-11 (page update)", "affects": ["rspec.fed.futa.credit_reduction.states", "US-FEDS5-009"], "action": "applied: 2026 period added to the fact as a limitation (list not yet published, re-read on or after 2026-11-10); no number stated"},
               {"instrument": "DOL WHD state minimum wage page: Michigan minimum wage scheduled to rise to $15.00 on 2027-01-01", "published": "2026-07-01 (page update)", "affects": ["next_year"], "action": "not relevant to 2026 numbers: 2027 change, lead for next_year; confirm on Michigan LEO before use"}])
        entry("SSA Contribution and Benefit Base page and 2027 COLA announcement", b['SSA'], "https://www.ssa.gov/oact/cola/cbb.html",
              "ssa.gov/oact/cola/cbb.html returned HTTP 403 to WebFetch; read through the ssa.gov entries of the search index (2026-11-04): 2026 base 184,500; 2027 base 192,300 announced 2026-10-14 (COLA 3.6%). Register and facts already carry 184,500 / 192,300 as separate periods.",
              [{"instrument": "SSA 2027 contribution and benefit base 192,300 (announced 2026-10-14)", "published": "2026-10-14", "affects": ["ss.ceiling.annual"], "action": "not relevant: already carried as the 2027 period of the existing fact; no 2026 number changes"}])
        entry("Federal Register / GovInfo / eCFR / other federal bodies (federal)", b['OTHER'], "https://www.federalregister.gov/",
              "No news-page fetch attempted for these publishers within the budget. Checked instead: local-copy dates in the register (latest retrieved_on " + m + "); statute and CFR texts are dated copies, and changes would surface through the IRS and DOL pages swept above. Open requirement: Federal Register search 2026-01-01 to release date for payroll rules.")
        continue
    u, res = fetched.get(g, (None, None))
    if u is None:
        hosts = collections.Counter(urlparse(r['url']).netloc for _, r in lst if not re.search(r'leg|code|statute|law|revisor|iga|ilga|mca|capitol|archive|dol\.gov|govinfo|ecfr', urlparse(r['url']).netloc))
        h = hosts.most_common(1)[0][0] if hosts else urlparse(lst[0][1]['url']).netloc
        u = "https://" + (h or "www.usa.gov") + "/"
        res = NA
    res = res.replace("{mx}", m)
    hits = []
    if g == 'WA':
        hits = [{"instrument": "Paid Family & Medical Leave premium rate rises to 1.2% in 2027 (ESD newsroom)", "published": "2026-10-16", "affects": ["next_year"], "action": "not relevant to 2026 numbers: 2027 rate; recorded under next_year; confirm on paidleave.wa.gov before use"}]
    name = {'FI': 'Mixed authorities (cross-state / financial)', 'MU': 'Multi-state instruments', 'OW': 'Other (no host recorded)'}.get(g, g + " state agencies and legislature")
    entry(name + " newsroom", auths, u, res, hits)
out = {"build_year": 2026, "sweeps": sweeps,
       "next_year": {"year": 2027, "url": "https://www.ssa.gov/news/en/cola/factsheets/2027.html", "searched_on": T,
                     "result": "2027 values published as of 2026-11-04: SSA contribution and benefit base 192,300 (announced 2026-10-14; already carried as the 2027 period); Washington PFML premium 1.2% in 2027 (ESD, 2026-10-16); Michigan minimum wage $15.00 from 2027-01-01 (DOL WHD page, to confirm at Michigan LEO); Rev. Proc. 2026-24 (2027 HSA limits). NOT yet published: IRS 2027 inflation-adjustment Rev. Proc. (scheduled October 2026), 2027 Pub 15-T, DOL final 2026 FUTA credit-reduction list (Nov. 10). Effect on this build: none on 2026 figures; each is a dated requirement for the 2027 refresh.",
                     "checked": ["https://www.ssa.gov/news/en/cola/factsheets/2027.html", "https://www.irs.gov/forms-pubs/about-publication-15-t", "https://esd.wa.gov/newsroom", "https://www.dol.gov/agencies/whd/minimum-wage/state"]},
       "_note": "Written 2026-11-04 by the source hunter (C41 close). One entry per State group; 'authority' lists every register authority of the group. 'result' says what was and was not read; entries whose page could not be fetched say so and are not clean sweeps."}
json.dump(out, open('00-official-sources/bulletin-sweep.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(sweeps), len({a for g in G.values() for a, _ in g}))
