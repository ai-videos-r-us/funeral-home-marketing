# Audit log: nextchaptermedia.org

Running log, 10 November 2026, in the order the work was done.

| # | Step | Result |
|---|---|---|
| 1 | First fetch of nextchaptermedia.org | Refused. The session's network policy blocked the host (proxy 403). Search engine returned no indexed result for the domain. |
| 2 | Read `docs/strategy.md`, `brand.md`, `awards-programme.md`, `outreach-compliance.md` | Stated goal: local SEO clients among UK funeral directors, via directory, awards and newsletter. Success measure: 3 paying clients from the funnel in 6 months. |
| 3 | Created a personal cloud environment `funeral-home-marketing` allowing the site's host (approved by Sean) | Site reachable. |
| 4 | Fetched home, robots.txt, sitemap.xml | 200. Hosted on Vercel, Next.js prerendered. Sitemap lists 120 URLs. robots.txt allows search and AI crawlers. |
| 5 | Crawled all 120 sitemap URLs, converted to text | 120 of 120 returned 200. 13 core pages, 64 insight articles, 43 calculators (17 funeral, 26 for stairlift, care home and home adaptation). |
| 6 | Read home, growth-system, funeral-homes, funeral-planning, case study, about, founder, privacy, cookies, terms | No prices anywhere. One conversion action sitewide: a Calendly link. Two guarantees. |
| 7 | Scanned all 120 pages for contact and capture markers | 0 `mailto:`, 0 `tel:`, 0 email input fields, 0 newsletter forms. 43 `<form>` tags, all calculator inputs. |
| 8 | Rendered 7 key pages on desktop (1366px) and phone (iPhone 13) | Fast: load 0.2 to 1.0s, HTML 12 to 30 KB transferred. Phone: header button hidden in the menu; home page first booking button at 706px on a 664px screen. |
| 9 | Checked script bundles and hidden routes | Vercel Web Analytics script present. No `utm_` handling. `/contact` and `/review` redirect (307) to Calendly. `/pricing`, `/newsletter`, `/thank-you`, `/api/review` return 404. |
| 10 | Competitor search (three queries) | Candidates: LOCALiQ, Independent Funeral Marketing (IFM), Fly High Media, Whito, MuchLoved, ProfileTree. No UK specialist in funeral plan appointment setting surfaced. |
| 11 | Calendly and competitor sites refused by the network policy | Added 9 hosts to the environment (approved by Sean). |
| 12 | Opened the Calendly booking page | Event is titled "Funeral Disco", 15 min, host shown as "Sean-harry-John-Munn", no description. Screenshot saved. |
| 13 | Stepped to the booking form (not submitted) | Asks name, email, funerals per year, monthly budget (mandatory, £1,000 to £4,000+ bands), who else decides. No phone, firm name, website or town. Availability shown: 11 to 13 November only. |
| 14 | Gmail search: Next Chapter Media, Calendly notifications | Nothing. No Calendly booking notification in 6 months. |
| 15 | Gmail search: funeral-related sent mail | 30 cold emails sent 1 to 2 September 2026 to US funeral homes from the main domain. 0 replies, 2 bounces, 0 follow-ups. Brevo account suspended 8 October. One client payment visible, probably Compare Funerals. |
| 16 | Read captures of IFM (home, pricing, scorecard, contact), LOCALiQ, Fly High Media, Whito, MuchLoved | IFM publishes prices: £2,500, £4,000, £8,000 a month plus setup. Every competitor has a free audit, scorecard or check, and a phone number or email. |
| 17 | Cross-checked claims across pages and emails | Same client quoted three ways: "~£12M, about 4,500 plans" (funeral directors page), "$9m" (cold email), no figure (case study). "$60M+" in dollars on a UK site. 5 articles written for US funeral homes. |
| 18 | Wrote `REPORT.md` | Ten ranked changes with evidence. |

## What I could not see

- Vercel Analytics, Search Console, the Calendly account, any CRM, proposals or contracts. I have no traffic or booking numbers.
- Any mailbox other than the one connected. If Calendly notifies another address, the "no bookings" reading is wrong.
- Onboarding after a sale. I audited the path from first visit to booked call, and what the site promises about the first 90 days.
- Meta Ads (connector not authorised) and Apify (connector failed to connect). Neither was needed for this audit.

## Changes made outside the repo

- Created the personal cloud environment `funeral-home-marketing` and allowed 11 hosts on it: the site, Calendly, aivideosystems.org and five competitor sites. Nothing was sent, submitted or booked.
