# UK adaptation: how the gates change for South West England

The blueprint was written for one US state. This build is **funeral directors in South West England**. The site's "state" slot holds the region: `name: "South West England"`, `code: "SW"`, slug `south-west-england`, so URLs are `/directory/south-west-england/<town>/`. User-facing copy says "towns" and "region", never "state" or "cities" (fix any leftover template wording you find at Gate 5).

**Run every gate locally** (Claude Code on Sean's computer). The cloud session this was prepared in cannot reach outside websites.

## Gate 1: scope (pre-answered)
Answers are in `input/01-scope-answers.md`. Confirm them with Sean, one at a time as the intake requires, but don't re-ask from scratch.

### The pull (DataForSEO)
1. Sean saves the DataForSEO login in his own Terminal: `python3 scripts/connect_dataforseo.py`. Never in chat.
2. Find the category id: `python3 scripts/fetch_dataforseo.py --find-category funeral`. Expect something like `funeral_home`. Note any `funeral_director` or `funeral_service` ids and ask Sean whether to include them (max 10).
3. **Probe the region field before estimating.** Google writes UK addresses with the nation (usually "England") in `address_info.region`, not "South West". Run a 30-row estimate with `--region England` and read the `state` column of the rows. If the values differ (county names, for example), adjust `--region` / `--region-op like` and say what you found.
4. Estimate and pull England-wide (the cost is small, about $0.012 per 1,000-row request plus $0.00036 per row):
   ```
   python3 scripts/fetch_dataforseo.py --category <id> --state "South West England" --state-code SW --region England --estimate
   python3 scripts/fetch_dataforseo.py --category <id> --state "South West England" --state-code SW --region England --out input/listings-raw-england.csv
   ```
   Ignore any `VERTICAL FLAG` that is caused by counting all of England; the region count comes next.
5. Narrow to the South West by official ONS region (postcodes.io, free, no key):
   ```
   python3 scripts/uk_region_filter.py input/listings-raw-england.csv --out input/listings-raw.csv
   ```
   It fills `state`, `state_code` (`SW`), `county` and `district`, and writes a report by county. If postcodes.io is unreachable it stops; `--no-lookup` uses a postcode-area fallback (BA BH BS DT EX GL PL SN SP TA TQ TR, minus BH24 BH25 SP6 SP10 SP11 SN7), which is rough at the edges.

## Gate 2: clean
`python3 scripts/clean_listings.py input/listings-raw.csv --state SW --niche "funeral" --category "<Maps category label>" --out output/sw-funeral-directors/02-listings-clean.csv`
Slug: `sw-funeral-directors`. Expect crematoria, cemeteries, monumental masons, florists and coffin makers to come through on secondary categories. **Do not drop them at Gate 2**; the `arranges_funerals` core attribute and a Gate 4 decision handle them.

**Group branches.** Many Co-op, Dignity and Funeral Partners branches trade under an old family name. Keep them; they are real funeral directors. The `group_owned` attribute and the descriptions say who owns them. Families care about that.

## Gate 3: enrich
Start from `scripts/examples/attributes-funeral-directors.json` (15 attributes) and review it with Sean before running. Copy it to `output/sw-funeral-directors/03-attributes.json`.
- `prices_published`: the CMA Funeral Market Investigation Order 2021 requires funeral directors to publish prices online. A `false` here is evidence of non-compliance, so the description must never say a firm breaks the rules. State only what was found ("no price list found on its website").
- `funeral_plans`: never write or imply that a provider is FCA-authorised unless that was checked against the FCA register and recorded in the fact sheet.
- Descriptions: plain, respectful, no superlatives. This is bereavement.

## Gate 4: plan
- Town floor stays 3 listings. `foldMaxKm` 40 is too wide for dense areas (Bristol, Bath) and fine for Cornwall and Devon; propose a value from the data.
- `niche.schemaType`: check schema.org for the closest current subtype of `LocalBusiness` for funeral directors and use `LocalBusiness` if there is none. Record what you checked.
- Service page candidates: direct cremation, green or natural burial, faith traditions, repatriation. These are Sean's decisions.
- `sortAttribute`: recommend none at launch, so the order is the plain published score.

## Gate 5: build
- `site.json` is pre-filled (brand, domain, region, publisher, organisation, disclosure, FAQ). Still needed: `publisher.url`, `publisher.sameAs`, `publisher.email`, `contact.email`, `contact.formEndpoint`, and the photo at `templates/astro/public/images/publisher.jpg`.
- **Fact sheet: UK official sources only.** For example: GOV.UK (registering a death, what to do after a death), the CMA Funeral Market Investigation Order 2021 and its price-display requirements, FCA funeral plan rules (regulated since 29 July 2022), legislation.gov.uk (Cremation (England and Wales) Regulations 2008), and council bereavement-service pages for crematoria and cemeteries in each town. Record the URL and date fetched for each. No prices or timescales unless a source is recorded.
- City copy: about the town in relation to funerals (local crematoria and cemeteries by name from council sources, travel distances, registration office), never a list of what the businesses say.
- Spelling: British English throughout (organise, colour, centre).

## Gate 6: launch (Vercel)
Sean hosts on **Vercel Pro**. The site folder `output/sw-funeral-directors/site/` already contains `vercel.json` (Astro preset, `dist` output, trailing slashes, `X-Robots-Tag: noindex` on any `*.vercel.app` host, long cache on `/_astro/`).

**Recommended: Git integration** (every push to the production branch redeploys, which suits "edit the CSV, rebuild"):
1. Commit the generated site (`output/sw-funeral-directors/site/`, excluding `node_modules` and `dist`, which are already gitignored) and push.
2. Sean, in the Vercel dashboard: **Add New → Project**, import `ai-videos-r-us/funeral-home-marketing`, set **Root Directory** to `output/sw-funeral-directors/site`, and confirm the framework is Astro. Production branch: `main` (merge the working branch into `main` first) or set the working branch as production in Settings → Git.
3. Deploy, then open the `*.vercel.app` address and check it.

**Alternative: CLI from Sean's machine:** in the site folder, `npx vercel link` (once, Sean logs in in his browser), then `npx vercel --prod`.

**Domain** (Sean, in Vercel): Project → Settings → Domains → add `funeraldirectorawards.com` and `www.funeraldirectorawards.com` (redirect www to the apex, or the other way round, but pick one and keep it). Vercel shows the DNS records to set at the domain registrar, or offers to switch the nameservers to Vercel. Add `funeraldirectorawards.co.uk` and `.uk` as redirects once registered. Make sure `site.json` `domain` matches the primary domain exactly.

Then:
- `python3 scripts/check_live.py https://funeraldirectorawards.com --preview https://<project>.vercel.app --expect-urls <n>` must pass.
- **Indexing: Google Search Console only**, with a verified property for funeraldirectorawards.com (DNS TXT record at the registrar or in Vercel DNS), the sitemap submitted, and important pages requested by hand. No paid indexing services (Omega or similar).
- The original launch-lean sitemap rules still apply (strong pages first, thin profiles `noindex`).
- The Cloudflare mail worker in `templates/worker/` is **not used** on Vercel. Claims go to Formspree (`contact.formEndpoint`), and email uses Next Chapter Media's normal mailbox.
