# Marko Dakić — Portfolio & Articles / Lab

Bilingual (EN/HR) personal website for **https://markodakic.github.io/**. Warm editorial design, mobile-friendly, GitHub Pages-ready. No hosting fees or JS framework.

## What's included

- `index.html` — homepage, portrait slot, capabilities, selected work and Articles & Lab preview
- `work.html`, `cases/*.html` — 13 detailed case studies (check public descriptions before first publication)
- `articles.html` — writing and home-lab section with topics in progress
- `content/articles.json` — future articles; first Cloud PC article is delivered **separately as a private draft**, not included in the public repository ZIP
- `content/projects.json` — editable bilingual project data
- `build.py` — build all static HTML plus sitemap/robots (Python standard library only)
- `assets/profile.jpg` — your provided portrait, ready for use in the homepage hero
- `assets/linkedin-banner-v2.png` — matching LinkedIn banner
- `.pages.yml` — optional visual content editor configuration
- `.github/workflows/rebuild-site.yml` — rebuild generated HTML when content changes

## First upload (preferred)

1. Sign in at https://github.com as `markodakic`.
2. Rename the existing public `markodakic/cv` repository to `markodakic.github.io` in Settings → General (Repository name → Rename).
3. You can return to ChatGPT after step 2; the connected GitHub app may upload the prepared files automatically if granted repository write access.
4. Otherwise, upload the **CONTENTS** of this folder to the repository root (not the parent folder). `index.html` must be at the repository root.
5. Go to **Settings → Pages → Source: Deploy from a branch → main → /(root) → Save**.
6. Verify https://markodakic.github.io/ , https://markodakic.github.io/work.html and https://markodakic.github.io/articles.html .

If the GitHub connection cannot see a new repository, check access settings for the connected GitHub App.

## Portrait

The user-provided headshot is saved as `assets/profile.jpg` and displayed in the hero. CSS crops it to fit the portrait frame; no AI-generated likeness is used.

## Publishing your own articles

1. Go to `content/articles.json` (directly on GitHub or via https://app.pagescms.org after authorising Pages CMS).
2. Edit the English and/or Croatian text for the draft article, or duplicate its structure for a new article with a **unique** URL `id`.
3. Review the text, dates, employer information, security details, screenshots and links.
4. Set `published` to `true` when ready; keep drafts outside the public repository until then.
5. The workflow regenerates `articles.html` and `articles/<id>.html` and commits changes. In an offline checkout, run `python3 build.py` and commit the outputs yourself.
6. Share the finished URL on LinkedIn as a short post linking to your website, rather than publishing under LinkedIn Articles.

**Important:** This site is public. Do not include internal employer documents, credentials, IP addresses, technical secrets or private screenshots. Drafts in a public GitHub repository are visible in source control even before the website lists them.

## Build locally

From the root directory:

```bash
python3 build.py
python3 -m http.server 8000
```

Open http://localhost:8000/ and check links. The site is normal HTML/CSS/JS; no build step is needed merely to serve the pre-generated HTML.

## Before publishing

- Confirm email and LinkedIn URLs in `build.py`.
- Review all 13 project descriptions (especially current employer projects and unverified metrics).
- Add your actual portrait when available; do not use someone else's photograph.
- The first Cloud PC article is a separate downloadable draft (not in this public-upload ZIP) until reviewed.
- Read `PUBLISHING-KORACI-HR.md` for Croatian instructions.

## Verified-looking metrics (v4)

The homepage shows **20+ years in IT**, **10+ years in eCommerce**, and **13 documented case studies**. The first two are rounded career durations based on known roles since 2005 and eCommerce since 2015; the third is a count of case pages on this website, not a claimed number of enterprise implementations. No fabricated hours, client numbers, ROI or sales uplift are displayed.
