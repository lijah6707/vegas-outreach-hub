# Vegas Outreach Hub — automatic discovery starter

This version adds a **daily discovery feed** of possible Las Vegas-area cultural heritage events, using public Google News RSS search results. Search results are **leads only**, not verified event dates or confirmed booth/flyer permissions.

## Publish for free using GitHub Pages
1. Create a public GitHub repository and upload all files, including `.github/workflows/discover.yml`.
2. In repository **Settings → Pages**, select **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. In repository **Actions**, run **Discover local events** manually the first time. The workflow will then attempt to run daily.
4. Visit your GitHub Pages address after deployment. The discovered leads appear in the new section.

Note: GitHub may disable scheduled workflows in inactive repositories; free usage and quotas are subject to GitHub's policies. GitHub Pages is public, so do not put private organizer details in the repository. Your manually entered events still live in each browser's local storage, not a shared database. Back them up using the Export button.

## Limitations
- Search queries currently target 2027. Update `QUERIES` in `discover.py` as years change.
- Google News RSS is an unofficial discovery source and can return stale or irrelevant articles. Feeds may change or fail.
- No automatic parsing of event dates, registration deadlines, costs, or permission; verify each lead with official organizers.
- The discovery feed only updates once hosted with the scheduled workflow. Opening `index.html` locally will not run it.
