# Global AI Adoption Index — mock dashboard

A static website with two pages:

- `index.html`: the main dashboard (world map, comparisons, country indicators)
- `questions.html`: Stakeholder Questions (eight worked examples for a fictional Country X)

All figures are illustrative. The site needs no build step and no server code. Any static host can serve it, and it makes no requests outside its own folder.

## Folder structure

```
index.html                 main dashboard page
questions.html             Stakeholder Questions page
css/
  fonts.css                @font-face rules (Andes, Open Sans, Loop icons)
  design-system.css        World Bank "Loop" tokens: colours, type, spacing, icons, base styles
  dashboard.css            styles specific to index.html
  questions.css            styles specific to questions.html
js/
  dashboard-engine.js      all dashboard logic and illustrative values (both pages)
  design-system.js         World Bank Group design-system components (generated; do not edit)
  dc-runtime.js            small runtime that renders the page markup and components (generated; do not edit)
  vendor/                  third-party libraries, pinned versions
    react.v18.3.1.production.min.js
    react-dom.v18.3.1.production.min.js
    d3.v7.9.2.min.js
    topojson-client.v3.1.0.min.js
    chart.umd.v4.4.0.min.js
data/
  world-topology.js        country boundaries for the world map (TopoJSON, sets window.WORLD)
fonts/                     Andes, Open Sans (variable, by script subset), Loop icon font
```

## Run it locally

Browsers block some features when a page is opened straight from disk (`file://`), so serve the folder:

```bash
cd global-ai-adoption-index
python3 -m http.server 8000
```

Then open http://localhost:8000.

## Deploy on Render

1. Put this folder in a GitHub repository, with `index.html` at the top level.
2. In Render, choose **New → Static Site** and connect the repository.
3. Set **Build Command** to `echo "no build"` and **Publish Directory** to `.`.
4. Deploy. Every push to the branch redeploys the site.

## Where to edit

| To change | Edit |
|---|---|
| Question text, sub-questions, data lists, limits, "What a decision-maker could do" | `js/dashboard-engine.js`, the `QX` array (search for `// QUESTIONS PAGE`) |
| Illustrative chart values on the Questions page | `build()` inside each question object in `QX` |
| Main-dashboard illustrative values | the top part of `js/dashboard-engine.js` (constants such as `TOPICS`, `IND10`, `BENCH_ENDS`) |
| Page headings, intro text, banner | `index.html` and `questions.html` (the markup inside `<x-dc>`) |
| Page styling | `css/dashboard.css` or `css/questions.css` |
| Brand colours, type scale | `css/design-system.css` |

The illustrative values currently live in `dashboard-engine.js` next to the code that draws them. To replace them with real Index data, move them into JSON files under `data/` and load them before the engine.

## Third-party components

| Component | Version | Licence |
|---|---|---|
| React, React DOM | 18.3.1 | MIT |
| D3 | 7.9.2 | ISC |
| topojson-client | 3.1.0 | ISC |
| Chart.js | 4.4.0 | MIT |
| Open Sans | variable | SIL Open Font License 1.1 |

Check before hosting publicly:

- **Andes** is a commercial typeface licensed for World Bank Group use. Confirm the web-font licence covers the domain you deploy to.
- **Loop icons and design-system components** are World Bank Group brand assets.
- **World map boundaries** (`data/world-topology.js`) came with the mock-up without a recorded source. Before publishing, replace the file with the World Bank's official boundaries, or confirm its source.
