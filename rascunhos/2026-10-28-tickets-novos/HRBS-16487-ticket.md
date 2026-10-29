# HRBS-16487 | Omnicom Netherlands- Inquire about "compliance Setup for EU resident who works in Netherlands"

## Descrição
Hi Team

Omnicom Netherlands has one employee who is resident in Austria and work for Omnicom Netherlands and register as per NL payroll tax and SSI. In the Netherland payroll tax calculation and compliance setup we have this setup is available. Client wants to know the Mercans payroll setup is support for this. Kindly check and let me know.

Dutch office site:
https://www.belastingdienst.nl/wps/wcm/connect/nl/personeel-en-loon/content/hulpmiddel-loonbelastingtabellen

For which country of residence do you want a table? - Select
"Another country from group of countries, this is to say another EU contry, Norway, Liechtenstein, Iceland, Switzerland or a BES islands"

## sjalihal 2026-10-26 11:24 UTC
![](image.png){width=70%}

## rfusana 2026-10-26 11:28 UTC
Hi @sjalihal,

Good day! Thank you for contacting the Mercans Support Team. This is to acknowledge receipt of your ticket.

We will proceed with our review and get back to you if we require any additional information or action from your end. You will also be updated on the progress of your ticket, especially if we need to involve our internal teams to complete your request or resolve the issue.

Should you have any further concerns or clarifications, please don’t hesitate to reach out to us.
___
Kind regards,
Romano Fusana
Support Engineer

## rfusana 2026-10-27 05:02 UTC
Client: Omnicom
Country: Netherlands

Hi Team,

The client have one employee who lives in **Austria** and works for an Omnicom NL entity. The employee is registered for Dutch payroll tax and Dutch social security. The client wants to know whether our NL payroll set-up supports the Belastingdienst wage tax table for residence group **“another EU/EEA country, Norway, Liechtenstein, Iceland, Switzerland or a BES island”**:

![](image1.png){width=70%}

As per the NL blueprint, kindly help confirm whether our understanding below is correct before we reply to the client.

**Rules for an Austrian resident (group of countries)**

* The labour credit (*arbeidskorting*) applies in full: tax part and premium part.
* The general credit (*algemene heffingskorting*) applies for the premium part only. The tax part is not given through payroll. Employees who earn 90% or more of their income in NL can claim it back in their income tax return.
* The elderly credits apply for the premium part only, if relevant.
* The tax rates are the same as for residents, because the employee pays Dutch premiums.

**-------------------**

* **No residence condition:** there is no residence-country condition anywhere in the NL design.
* **Credits:** the general credit (9528105/9528108) and the labour credit (9528111/9528114) calculate the full combined amounts (general credit €3,115, labour credit maximum €5,685). The credit bands are selected only by `$58205` (age/AOW category).
* **Credit switch:** `$58207 = 1` switches off both credits entirely (9528123/9528126). The special-rate table 9528087 follows the same flag. So the system only has two states, “full credit” and “no credit”. There is no “labour credit plus premium part of the general credit” state.
* **Tax rates:** the combined tax-plus-premium rates in 9528075 (35.75% / 37.56% / 49.50%) look correct for an insured non-resident.
* **Social security:** ZVW (9528280) and AWF/AOF (9528270) have no residence condition. We believe they calculate correctly under EU Reg. 883/2004 if the employee works only in NL.

**Effect if processed as-is**

* **Credits on (`$58207 = 0`):** the tax part of the general credit is applied when it shouldn’t be, so wage tax is **under-withheld**.
* **Credits off (`$58207 = 1`):** the employee loses the labour credit and all premium parts, so wage tax is **over-withheld**.
* Neither option matches the Belastingdienst calculator.

**Please confirm or correct:**

1. Is our reading of the rules in section 1 correct for 2026?
2. Is our reading of the blueprint correct, so that this case isn’t supported today? Or is there a configuration we’ve missed?

## mjain 2026-10-28 11:28 UTC


@wgomes We want to know the difference in tax calculation for 

1. A Normal Netherlands Resident Employee and 
2. Employee Another country from group of countries, this is to say another EU contry, Norway, Liechtenstein, Iceland, Switzerland or a BES islands




Please let us know the difference in tax calculation steps so we can analyse and provide solution if we can. Kindly refer the existing product structure in Netherlands i.e., we do not have a table software but we follow the tax calculation procedure given by Netherlands Govt.



You can also refer to **netherlands-design-blueprint skill file on claude (**<https://claude.ai/customize/skills/id/plugin_01UKUmQdeH2F3TKe2X1uCrce>)
___
Kind regards

Mohit Jain

Head of Compliance Product
