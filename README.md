# CloudCert Lab — SAP-C02 Practice Website

A personal, responsive React + TypeScript question bank for **674 SAP-C02 questions** from your uploaded PDF. It is a static site: no backend, database, AWS account, or paid hosting required.

## Features

- 674 source questions with original IDs, options and answer keys
- Domain 1–4 filters and 1 / 2 / 3 correct-answer filters
- Search, bookmarks, unanswered/incorrect/correct filters, original/domain/answer-count/random order
- Practice sessions with immediate source-key feedback and available study notes
- 75-question, 180-minute timed mock exam (adjustable), random order and end-of-test results
- Test history and latest accuracy, saved in browser localStorage
- Export/import progress JSON for backups and switching browsers
- Responsive desktop and mobile interface
- Existing preliminary technical review notes for Q101–105 and source wording warnings

**Important:** The question bank comes from a third-party study PDF. Answers are labeled as source keys, **not independently verified**. Detailed explanations from the earlier guide were recoverable for only a subset of Q1–100. The remaining questions show an honest explanation-unavailable message rather than fabricated reasoning. Domain tags are *study estimates* from the earlier PDFs, not official exam categorization. Do not publish the question bank without confirming redistribution rights.

## Run locally

Install Node.js 20.19+ or 22.12+.

```bash
npm install
npm run dev
```

Open the local URL printed by Vite (usually `http://localhost:5173`).

## Production build

```bash
npm run build
npm run preview
```

Vite writes a static website into `dist/`.

## Free hosting — Cloudflare Pages

1. Create a **private GitHub repository** and push this project. Note: **private GitHub source does not make the deployed website private**. Do not deploy copyrighted question content publicly without permission.
2. In Cloudflare, open **Workers & Pages → Create → Pages → Connect to Git**.
3. Choose the repository, select the Vite framework preset, set build command to `npm run build` and output directory to `dist`.
4. Deploy. Your site will get a `*.pages.dev` URL. Static site hosting is available on the Cloudflare Pages free plan, subject to current limits.
5. To restrict access, use Cloudflare Access if available on your plan, or keep the app local until licensing is resolved. A static client-side password is **not** a secure access control mechanism.

Alternative: GitHub Pages or Netlify static hosting. `vite.config.ts` uses `base: '/'`, appropriate for a root-hosted Pages deployment. If deploying under a GitHub Pages repository subpath, update `base` accordingly.

## Data privacy

Progress is stored only in the current browser using `localStorage` keys `sap-c02-practice-v1` and `sap-c02-active-session-v1`. Clearing browser storage removes progress. Use the **Export JSON** button to back it up. No telemetry or server sync is included.

## Source extraction

`extract_questions.py` is included for reproducibility. It reads `/mnt/data/SAP-C02V33.2.pdf` and optional earlier study PDFs in `/mnt/data/`. Install `pymupdf` to rerun it. The exported `src/data/questions.json` is already included, so **you do not need Python to run the React app**.

## Limitations / roadmap

- The real SAP-C02 domain weighting is not reflected in the random mock question mix; it samples across the bank. An official-weighted sampler can be added later.
- Source-answer correctness has not been fully audited. A matching answer is scored against the **supplied source key**, not AWS's official exam key.
- Existing technical reviews are preliminary; add vetted explanations and documentation links to `questions.json` over time.
- Browser-local progress does not sync automatically across devices.
