# Next Chapter Media: website audit

Audited 10 November 2026. Site: https://nextchaptermedia.org/ (120 pages). Working log: `audit/LOG.md`. Screenshots and measurements: `audit/evidence/`.

Confidence tags: **[Certain]** I observed it directly. **[Likely]** a strong inference from what I observed. **[Guessing]** I am filling a gap.

## The answer you probably don't want

**The website is not what is stopping you making money. You have no working way of getting funeral directors to it, and when one does arrive there is exactly one thing they can do: book a 15-minute call that is titled "Funeral Disco".**

- [Certain] Every call to action on all 120 pages goes to one Calendly page. Its public title is "Funeral Disco". Screenshot: `evidence/booking-page.png`.
- [Certain] The connected mailbox holds no Calendly booking notification from the last six months.
- [Certain] The only outbound I can find is 30 cold emails on 1 and 2 September, sent to funeral homes in the United States, from a site that says it only takes UK clients. They got 0 replies and 2 bounces, and no follow-up was sent.
- [Certain] The directory that `docs/strategy.md` names as the funnel is still a holding page in this repo.
- [Likely] There is one paying client, and it is the Spanish expat plan seller the case study describes, not a UK funeral director.

The site itself is well built. It is fast, the copy is clear and honest, the schema is thorough, and the 64 articles are better than anything the competitors publish. I would not rewrite it. I would fix the ten things below, in this order, and stop producing content until the first five are done.

## Ten changes, ranked by likely money

### 1. Fix the booking page today

Evidence, all [Certain]:
- Title shown to prospects: "Funeral Disco". Host shown as "Sean-harry-John-Munn". No description.
- The site sells a "Local Enquiry Review" with "your town's map on screen". The booking page offers 15 minutes and says nothing about a review.
- The form asks for name and email, then funerals per year and monthly budget (both mandatory), then who else decides. It does not ask for a phone number, the firm's name, its website or its town. You cannot prepare a town map from that.
- Only three days showed availability (11 to 13 November).
- `/contact` and `/review` both redirect straight to this page.

Change: rename the event "Local Enquiry Review with Sean Munn", set the length the site promises, add a three-line description of what they get, add firm name, town, website and phone, make budget optional or drop it, open at least two weeks of availability, and create a second event type for funeral plan providers. This takes under an hour. [Likely] it is the highest-return hour available, because every other improvement feeds this page.

### 2. Add a second, smaller ask: a free visibility snapshot and an email sign-up

Evidence:
- [Certain] 0 email fields across 120 pages. The calculators say "Free, no sign-up, nothing you type is stored".
- [Certain] 64 articles and 43 calculators end in the same ask: book a call.
- [Certain] Every competitor I checked has a lower-commitment step. IFM: a free 30-point visibility scorecard. LOCALiQ: a free SEO audit, a webinar and a newsletter. Whito: a free website check and a free email. Fly High Media: an SEO audit request. MuchLoved: a monthly email.
- [Certain] Your own `docs/strategy.md` calls the newsletter "the real moat" and makes the "local visibility snapshot" step 2 of the funnel. Neither exists on the site.
- [Certain] The privacy policy describes a review request form (name, business, work email, phone, consent box, hashed IP address). No such form is on the site and `/api/review` returns 404. It was either removed or never shipped.

Change: restore that form as "Get your town's visibility snapshot": firm name, town, email. Add "email me this result" to the 17 funeral calculators. Add a newsletter sign-up with double opt-in, as your compliance doc already requires. [Likely] most first-time visitors from an article are not ready for a sales call, so today they leave without a trace.

### 3. Put a phone number, an email address and the company's details on the site

Evidence:
- [Certain] 0 `tel:` links and 0 `mailto:` links on 120 pages. The privacy policy tells people to exercise their data rights by booking a Calendly call and mentioning "Privacy".
- [Certain] The site says "Full registered company details are available on request." Stripe receipts in your mailbox name the operator as AI Video Systems Limited.
- [Likely] A UK limited company must show its registered name, number and registered office on its website (Company, Limited Liability Partnership and Business (Names and Trading Disclosures) Regulations 2015), and a business selling online services must give an email address and a geographic address (Electronic Commerce Regulations 2002). Check this with Companies House guidance or a solicitor; I am not giving legal advice.
- [Certain] Your funeral directors page argues that "the family who doesn't get through to you doesn't come back later". Your own site cannot be rung.
- [Certain] LOCALiQ, Fly High Media and MuchLoved show a phone number in the header. Whito shows an email.

[Likely] Funeral directors are phone-first buyers who have "been burned before" (your words). An agency with no number, no address and no company name reads as a risk.

### 4. Publish price ranges, and add a paid entry offer

Evidence:
- [Certain] No price on any page. `/pricing` is a 404. The funeral directors page says "There's no fixed tariff."
- [Certain] Your booking form already reveals the range: "Under £1,000", "£1,000 to £2,000", "£2,000 to £4,000", "Over £4,000 a month".
- [Certain] IFM, your closest competitor, publishes: Foundation from £2,500 a month plus £2,500 setup (3-month minimum); Growth from £4,000 plus £3,500 (6 months); Market Leader from £8,000, setup from £5,000 (12 months). Screenshot: `evidence/competitor-ifm-pricing.png`.
- [Certain] MuchLoved publishes websites "from just £2,095". Whito publishes fixed prices (£280 audit, £280 a month monitor, £680 report).
- [Certain] Your own calculator uses £1,878 contribution per arrangement.

I disagree with hiding the price because the buyer you describe has been burned by agencies and will assume the worst. Here's what I'd do instead: publish "from £X a month plus £Y setup, single location", state the minimum term, and put the break-even next to it in funerals ("under one extra arrangement a month"). The risk in your current approach is that the first number a director hears is on a call they were never willing to book, while IFM's sits in public as the anchor.

[Guessing] on the entry offer: a one-off paid Local Enquiry Audit at a few hundred pounds, credited against setup, gives a cautious director a way to buy something small. Whito's £280 audit shows the price point exists. I have no data on what would convert for you.

### 5. Fix the proof so a UK funeral director sees a UK funeral director

Evidence, all [Certain]:
- The two funeral home results (Liverpool, 390 calls from Google; Southampton, 160 calls) are anonymous, with no screenshot and no named person.
- The only named client, Compare Funerals, sells plans to English-speaking expatriates in Spain. Your own page says "not a UK client result".
- The same client is quoted three ways: "~£12M in funeral plan sales, about 4,500 plans" on the funeral directors page; "$9m generated" in your cold emails; no figure at all in the case study.
- "$60M+ in tracked revenue across 96+ clients" is in US dollars, on the home and founder pages of a UK-only site, with no breakdown. Your About page says "We publish only verified results".
- The case study page has no numbers.

Change: get permission to name the Liverpool and Southampton firms, or at minimum show the Google Business Profile call graphs with the name masked. Pick one Compare Funerals figure, in pounds, and use it everywhere including the case study. Either source the $60M claim or remove it. [Likely] one named UK funeral director with a quote is worth more than every other line of proof on the site.

### 6. Stop the US cold email and build the UK outreach your own docs describe

Evidence, all [Certain]:
- 30 emails on 1 and 2 September, about nine minutes apart, subjects alternating "I just saw X's ad" and "I just clicked X's ad". Recipients were US funeral homes.
- 0 replies. 2 bounces. No second email to anyone.
- Sent from the main business domain. `docs/outreach-compliance.md` says to use secondary domains, include a postal address and an unsubscribe, and check company status first. None of that was in the emails.
- The pitch was funeral plan lead handling. `docs/strategy.md` says the main offer is local SEO for funeral directors.
- The home page FAQ says "Do you work outside the UK? Not at the moment."

Thirty emails is too few to judge the copy. The finding is that the campaign was abandoned after one touch and aimed at a market the site turns away. Change: finish the directory launch, then run the "your listing is live, please check it" sequence to limited companies, with the visibility snapshot from change 2 as the second touch. [Likely] this, not the website, decides whether you hit three clients in six months.

### 7. Make the home page about funeral directors

Evidence, all [Certain]:
- Home page H1: "More Qualified Appointments & Calls. More Sales. For Businesses Serving Over 50 Year Olds." The line above it lists "Funeral Homes · Funeral Plans · Stairlifts · Home Remodellers".
- The FAQ on the same page: "Do you only work in the funeral sector? For now, yes."
- 26 of 43 calculators are for stairlift, care home and home adaptation firms.
- 5 articles address US funeral homes, including one titled "the complete guide for US funeral homes".
- The founder page carries a roadmap to 2031 across five sectors.
- IFM and LOCALiQ both open with "independent funeral directors" in the headline.

Change: lead the home page with the funeral directors headline you already have ("More calls from local families. More of those calls becoming funeral arrangements."), move plans second, and take stairlifts and remodellers off the first screen. [Likely] a specialist converts better than a generalist with funeral pages. The risk in the current approach is that a funeral director sees a lead generation agency for the over-50s and leaves.

### 8. Make the booking button reachable on a phone and earlier in articles

Evidence, all [Certain], measured on an iPhone 13 viewport (664px tall). Data: `evidence/render-measurements.jsonl`.
- The header "Book a Review" button is hidden inside the menu on phones.
- Home page: the first visible booking button sits at 706px, below the first screen. Screenshot: `evidence/home-mobile-first-screen.png`.
- Pillar article "Funeral director marketing in the UK": the first booking link in the content is at 17,816px of 25,013px, about 71% down.
- Nothing sticks to the bottom of the screen.

Change: a slim sticky bar on phones with "Book a review" and "Call", and one contextual box about a third of the way into each article offering the snapshot from change 2.

### 9. State the guarantee terms plainly

Evidence, all [Certain]:
- Home page headline: "Two Guarantees. No Small Print Surprises." Sub-line: "Both apply to every engagement."
- The 180-day guarantee begins "For qualifying clients". The criteria are not published anywhere.
- Terms page: "Nothing on this website is an offer capable of acceptance... any performance guarantee and its eligibility conditions are set out only in a written agreement".
- The parent site, aivideosystems.org, offers only a 30-day guarantee.

"Applies to every engagement" and "for qualifying clients" cannot both be true. Change: publish the three or four qualifying conditions (for example: records which calls became arrangements, gives access within 14 days, minimum number of funerals a year). [Likely] a guarantee with visible conditions is more believable than one with hidden ones.

A caution that is not about conversion: a full refund of 180 days of fees is a real liability for a one-person firm. [Guessing] Cap it in the contract before the first client signs, if you have not already.

### 10. Track where bookings come from

Evidence:
- [Certain] The Calendly links carry no source. The site's scripts contain no `utm_` handling.
- [Certain] Vercel Web Analytics is installed. I cannot see its data.
- [Certain] With 107 content pages and one destination, you cannot currently tell which page produced a booking.

Change: append the page path to each Calendly link as a UTM parameter and add a Calendly question "What prompted you to book?". Then cut or merge the content that produces nothing. This earns nothing by itself; it stops you spending the next three months on the wrong pages.

## What I would not change

- [Certain] Speed. Pages load in 0.2 to 1.0 seconds and transfer 12 to 30 KB of HTML.
- [Certain] The technical SEO base: one H1, titles, descriptions, canonical tags, FAQ and Service schema, a real sitemap, crawlers allowed.
- [Likely] The tone. It is plain and it does not overpromise, which suits this buyer.
- Do not write more articles or calculators yet. You have 107. The constraint is distribution and capture.

## Pricing

| | Next Chapter Media | IFM | LOCALiQ | Fly High Media | Whito | MuchLoved |
|---|---|---|---|---|---|---|
| Public price | None | £2,500 / £4,000 / £8,000 a month, setup £2,500 to £5,000+ | None | None | £29 to £1,280 fixed | Websites from £2,095 |
| Minimum term | Not stated | 3, 6, 12 months | Not stated | Not stated | One-off or monthly | Not stated |
| Guarantee | 30-day refund; 180-day refund "for qualifying clients" | States it cannot guarantee enquiry volume | None shown | None shown | None shown | None shown |
| Exclusivity | None | One firm per town | None | None | None | None |

All rows [Certain] from the pages captured on 10 November 2026. Your guarantee is the strongest commercial claim in this group. IFM's "one firm per town" is the strongest positioning claim and you have no answer to it.

## Onboarding

What a prospect experiences, step by step:

1. [Certain] Clicks "Book a Review" from any page and leaves the site for Calendly.
2. [Certain] Sees "Funeral Disco, 15 min".
3. [Certain] Must state an annual funeral count and a monthly budget before getting a time.
4. [Guessing] Receives Calendly's default confirmation. I could not see the confirmation or reminder emails without booking, and I did not book.
5. [Certain] Nothing on the site says what happens between booking and the call, or what to bring.

After a sale, the site promises a two-week audit and baseline for funeral directors, and a four-stage 90-day plan for plan providers. That is clear. I could not check whether a welcome email, access checklist or kickoff agenda exists, because none is in the repo or the mailbox.

Change, beyond item 1: a confirmation page on your own site that says what the review covers, asks for the Google Business Profile link, and offers one article to read first.

## Emails

- [Certain] No Next Chapter Media email of any kind in the connected mailbox: no welcome, no nurture, no newsletter, no booking confirmation.
- [Certain] The 30 September cold emails, described in change 6.
- [Certain] The Brevo account used for client sending was suspended on 8 October and you asked for a refund. [Likely] you have no email platform set up for Next Chapter Media.
- [Certain] The client campaign that was sending came from a shared Brevo address rather than the client's own domain. That is a deliverability risk for your one paying client, separate from this audit.

There is no email system to audit. There is one to build: snapshot delivery, a three-email follow-up for people who took the snapshot and did not book, and the monthly newsletter your strategy describes.

## Competitors

Chosen from search results for UK funeral director marketing. [Likely] these are the ones a director comparing options would meet; I have no market share data.

| Competitor | What they are | First step they offer | Proof shown | What to take from them |
|---|---|---|---|---|
| Independent Funeral Marketing (independentfuneralmarketing.com) | Funeral-only agency, Orpington. UK and US. | Free 30-point scorecard, or an 11-field form then a 30-minute call | One anonymous quote; one named quote; says case studies are still to come | Public pricing, territory exclusivity, the scorecard. Their proof is weaker than yours. |
| LOCALiQ (localiq.co.uk) | Large general agency with a funeral page | Free SEO audit, 30-minute consultation, webinar, phone | Trustpilot, awards, a funeral case study | Free audit plus webinar plus phone number. Generic copy; you out-write them. |
| Fly High Media (flyhighmedia.co.uk) | Manchester generalist with a funeral landing page | Book a call form, phone, audit request | Case studies from gin, marine and Shopify. Nothing funeral. | Little. A templated sector page. |
| Whito (whito.co.uk) | Research and directory publisher with a funeral industry hub | Free website check with no email, free listing, free email | Its own studies (56 funeral director websites checked, 31 October 2026) | The closest model to your directory plan, already live. Fixed public prices. |
| MuchLoved (funeralprofessionals.muchloved.com) | Tribute pages and websites for funeral directors | Book a call or demo, phone, email | 2,500+ UK branches, named testimonials | Trade credibility and an installed base. A possible partner, not only a rival. |

[Certain] None of the five offers a money-back guarantee. None tracks calls through to arrangements, which is your real difference. [Likely] You are under-using both.

For the funeral plan side, I found no UK specialist selling booked adviser appointments. [Guessing] That may mean an open niche or a small market. The search was three queries, so treat it as unproven.

## Limits of this audit

- No access to analytics, Search Console, Calendly, a CRM, proposals or contracts. I have no traffic, booking or revenue numbers.
- One mailbox only. If bookings notify another address, the "no bookings" finding is wrong.
- Post-sale onboarding was not observable.
- The ranking is my judgement of likely return. Items 1, 3, 8 and 10 rest on direct measurement. Items 2, 4, 5, 6, 7 and 9 rest on measurement plus inference about how funeral directors buy, which I cannot test from here.
