# Gate 1 answers (agreed with Sean before the build)

1. **Vertical:** funeral directors (Maps category: funeral home; confirm the DataForSEO id with `--find-category funeral`)
2. **"State":** South West England (code `SW`, slug `south-west-england`). UK region, not a US state; see `docs/uk-adaptation.md`
3. **Domain:** funeraldirectorawards.com (owned). Also register funeraldirectorawards.co.uk and .uk and redirect them
4. **Owned microsites:** none. Next Chapter Media clients may appear as ordinary listings; see `docs/editorial-policy.md`
5. **Publisher:** Next Chapter Media, a trading name of AI Video Systems. Named editor: **Sean Munn**
6. **Publisher details:**
   - Bio: pre-filled in `templates/astro/src/data/site.json` (`publisher.bio`); Sean to approve
   - Photo: added at `templates/astro/public/images/publisher.jpg`
   - Logo: `templates/astro/public/images/next-chapter-media-logo.png` (added)
   - Website, LinkedIn and email: still to come from Sean (he'll give the Next Chapter Media email when it's needed)
7. **Look:** default master template unless Sean names a design pointer. Suggest a calmer palette suited to bereavement (the Next Chapter Media navy `#0B284A` and red `#D6103F` used sparingly)
8. **Listings source:** DataForSEO (Sean saves the login in his own Terminal)

## Decisions already made by Sean (2026-11-10)
- **Gate 3 attributes:** the 15 in `scripts/examples/attributes-funeral-directors.json` are approved as they are.
- **Gate 4 exclusions:** crematoria, cemeteries and stonemasons (monumental masons) are **not** listed. Exclude them by what they do, not by Google category alone: a row goes into `04-exclusions.csv` when `arranges_funerals` is `false`, or when its primary type is a crematorium, cemetery or monument maker **and** `arranges_funerals` is not `true`. Funeral directors that also run a crematorium or sell memorials stay in. Show Sean the excluded list and the borderline rows before applying it.
- **Hosting:** Vercel Pro (Sean's existing account), not Cloudflare. Deploy steps: `docs/uk-adaptation.md` § Gate 6.
