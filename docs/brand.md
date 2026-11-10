# Funeral Director Awards: brand

Source: `docs/brand/fda-brand-guidelines.webp` ("The Modern Crest").

## Palette and where each colour may be used
Contrast is measured against WCAG AA (4.5:1 for body text, 3:1 for large text).

| Colour | Hex | Use | Never |
|---|---|---|---|
| Midnight blue | `#101D30` | Header, hero band, headings, links, body text on light backgrounds (15.1:1 on ivory) | n/a |
| Champagne | `#C5AD78` | Buttons (with midnight text, 7.8:1), gold accents, rules, stars, text **on midnight** (7.8:1) | **Text on ivory or white (1.95:1, unreadable)** |
| Ivory | `#F5F2EA` | Page background, text on midnight | n/a |
| Slate | `#697583` | Decorative only: dividers, icons, borders | Body text (4.2:1 on ivory, fails AA) |
| Body text (derived) | `#2A3646` | Paragraph text on ivory (11:1) | n/a |
| Muted text (derived) | `#5A6573` | Captions and meta on ivory or white (5.3:1) | n/a |
| Soft text on midnight (derived) | `#C9CED6` | Hero subtitles on midnight (10.7:1) | n/a |
| Tint (derived) | `#EDE6D6` | Alternate section background | n/a |

These are set as design tokens in `templates/astro/src/data/site.json`.

## Type
- Headings: **Montserrat** 700/800 (the wordmark style). Self-hosted via @fontsource, SIL OFL.
- Body: **Source Sans 3** 400/600/700. Self-hosted, SIL OFL.
- "AWARDS" in the wordmark is letter-spaced champagne capitals. Use that treatment only in the logo lock-up, not for page text.

## Logo files still needed
The guideline image is a rendered mock-up, not artwork. Before the crest goes on the site or on any badge, get **vector files** (SVG, plus PNG at 512px and 1024px) for:
1. The crest on its own (favicon, social avatar, badges)
2. The horizontal lock-up (crest + wordmark): one version for light backgrounds, one for midnight
3. The winner ribbon badge as an editable template

Until then the site header uses the text wordmark.

## Badge wording (editorial policy)
Badges name the real award, the region and the year, for example **"Families' Choice · South West England · 2027"** or **"Finalist · Price Transparency Award · South West England · 2027"**. No generic "Award of Excellence" and no badge that isn't tied to a real result (`docs/editorial-policy.md`, `docs/awards-programme.md`). The first cycle's results are due about 12 weeks after nominations open, so the first badges will probably carry **2027**, not 2026.
