# Awards programme (first cycle: South West England)

Built **after** the directory is live (month 2–3). Nothing here is part of the six gates. Every rule is subject to `editorial-policy.md`.

## Categories (first cycle)
| Award | How it's decided |
|---|---|
| **Price Transparency Award** | Mostly from data: how easy the firm's price list or Standardised Price List is to find, and how complete it is (CMA order items). Judges confirm the top 5. |
| **Families' Choice** | Verified family nominations, then a judges' shortlist and decision. |
| **Independent Funeral Director of the Year** | Independent firms only (`independent=true` and `group_owned` not true). Score plus nominations, judges decide. |
| **Green or Natural Funeral Provider** | Firms confirmed for `green_burial`, with nominations and judges' review. |
| **Community Contribution** | Nominations only (bereavement support, charity, community work), judges decide. |

Start with these five. Add categories only when nominations justify them.

## Shortlist score (published on the awards page before nominations open)
For each eligible firm, out of 100:
- 35: review strength (rating × log10(reviews + 1), scaled within the region)
- 20: price transparency (prices published, easy to find, standard items present)
- 15: review recency (share of reviews from the last 24 months, if the data has dates; otherwise left out and re-weighted)
- 15: verified family nominations (capped, so a campaign can't swamp the score)
- 15: services breadth (confirmed attributes from the directory)

The top 5 per category go to the judges, anonymised. **Freeze these weights before the cycle opens; never change them mid-cycle.**

## Nominations
- Form fields: nominator name, email, relationship (family member, friend, colleague), funeral director, town, approximate month of the funeral, and what they did well (free text).
- Checks: confirm the email address, one nomination per person per category, flag duplicate IP addresses or wording, and strike nominations from the firm's own staff.
- Nominator details stay private, used only to check the nomination (state this in the privacy notice).
- Funeral directors may share the nomination link with families. They may not offer incentives for nominations; any found are struck.

## Judges
3–5 people with no commercial tie to Next Chapter Media, for example a celebrant, a hospice bereavement lead, someone from a bereavement charity, or a retired funeral director from outside the region. Each signs a short conflict declaration. They see anonymised shortlists only.

## Timeline (one cycle)
1. Weeks 0–2: publish categories, criteria and score weights; recruit judges.
2. Weeks 2–8: nominations open, and listed firms are told (this is the outreach moment).
3. Weeks 8–9: score, verify nominations, and set shortlists. **Sales firewall starts.**
4. Weeks 9–11: judging.
5. Week 12: results published on the site; winners and finalists notified. **Firewall ends.** Promotion packages are offered to all winners and finalists at one price.

## What winners get (free)
A winner's page on the site, an HTML badge linking to that page (send the snippet, offer to install it), and inclusion in the results announcement and press release. Badges say what was won, for example "Families' Choice, South West England 2027", and nothing else.

## Records to keep
Score sheet, nomination log with the verification outcome, judges' declarations and decisions, and the date each step happened. Keep them in `output/awards/<year>/` (not published).
