# Editorial and conflict-of-interest policy

Funeral Director Awards (funeraldirectorawards.com) is published by **Next Chapter Media, a trading name of AI Video Systems**, a marketing agency that sells local SEO and related services to funeral directors. **Sean Munn** is the named editor. The site's value depends on families and funeral directors trusting that it is fair, so these rules override anything in the original Rank Expand Academy blueprint.

## 1. Nothing on the site is for sale
- No featured slots, premium listings, best-of placements, sponsored positions or paid badges. The template ignores the `featured`, `premium` and `best_of_rank` columns even if they appear in a CSV.
- Listing, claiming and entering the awards are free for every funeral director.
- If advertising is ever added, it lives in a clearly labelled area that is separate from listings and award pages, links with `rel="sponsored"`, and never touches order or results. That needs a written change to this policy first.

## 2. Same treatment for everyone
- Every listing uses the same template, the same link treatment (`site.outboundFollow`, one setting for the whole site) and the same order rule.
- A free, verified claim unlocks owner photos, hours and the map for **any** business. Claiming never changes position.
- Next Chapter Media clients get no extra links, no longer descriptions, no better placement and no editorial favours. The `owned` flag from Gate 2 must never change rendering.

## 3. Published order
Town pages are ordered by Google rating × log10(review count + 1), with an optional confirmed-attribute group first (`site.sortAttribute`). This is published on `/methodology/`. **If the code in `templates/astro/src/lib/load.mjs` changes, the methodology page changes in the same commit.**

## 4. The awards
- Open to every listed funeral director, whether or not they are a client or have claimed their listing.
- Shortlists come from published criteria and verified family nominations (see `awards-programme.md`).
- 3 to 5 independent judges pick winners from an anonymised shortlist. Judges are never told who is a client.
- Scores, nominations and judges' decisions are kept for every cycle.

## 5. Sales firewall
- **No sales pitch to any shortlisted firm between the shortlist being set and the results being announced.**
- Winner and finalist promotion packages (award promotion, schema, press release, badge installation) are offered only after results are public, to every winner and finalist at the same price.
- Buying any Next Chapter Media service has no effect on eligibility, scoring or results, and the site says so.

## 6. Disclosure
- About page, methodology page and footer FAQ name Next Chapter Media as publisher, say it is a marketing agency that works with funeral directors, and say some listed firms are clients.
- Search Console, Google Business, social profiles and registrant details are in the real business name. Nothing about ownership is hidden (the original blueprint's "footprint rules" do not apply here).

## 7. Accuracy
- A listing detail is `true` only when the business's own website says so; otherwise "not enough info". No guessing.
- Facts about law and regulation come from official UK sources (GOV.UK, CMA, FCA, legislation.gov.uk) with the URL and date recorded in the fact sheet.
- Corrections and removal requests are answered within a week and checked by a person before the CSV changes.
