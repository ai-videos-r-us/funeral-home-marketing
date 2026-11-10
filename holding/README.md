# Holding page

A one-page, noindexed "launching soon" page so funeraldirectorawards.com can be connected to Vercel (DNS and HTTPS) before the directory exists.

Vercel project settings while this is live: **Root Directory** `holding`, **Framework Preset** Other, no build command.

At Gate 6, change the same project's Root Directory to `output/sw-funeral-directors/site` (framework Astro) and redeploy. The domain stays attached. Then delete this folder.
