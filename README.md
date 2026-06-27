# data-chart-builder

A Python (matplotlib/seaborn) charting skill for everyday work data analysis.
9 chart families, each with ready-to-run recipes and mock data.
Open [SKILL.md](SKILL.md) to start — pick a chart type, load the matching recipe, run it.

## What this skill does

When you say "画个分组柱状图对比三组数据" or "make a heatmap of this matrix",
this skill provides the correct matplotlib boilerplate — rcParams, palette, layout,
export — so you get a clean, publication-quality chart without starting from scratch.

It covers:

- **9 chart families**: bar, line/trend, heatmap, scatter/bubble, radar/polar,
  distribution (histogram/violin/box/ridgeline), forest/interval, area/stacked,
  network/matrix (bubble matrix, node-link, bipartite).
- **6 palette families**: general-purpose, pastel method-family, dark-background,
  soft categorical, time-series multi-phase, wave-grouped.
- **7 reusable helpers**: `apply_chart_style()`, `make_grouped_bar()`, `make_trend()`,
  `make_heatmap()`, `make_forest_plot()`, `add_panel_label()`, `finalize_figure()`.
- **14 layout patterns**: dedicated legend panels, alpha-graduated bars, hatch encoding,
  dynamic y-axis, event-annotated trends, multi-row grids, asymmetric hero panels,
  direct labels, and more.
- **Runnable defaults**: every recipe includes mock data — copy, paste, run.

It does **not** do flowcharts, architecture diagrams, UML, dashboards, interactive
charts (Plotly/Altair/Bokeh), 3D rendering, or GIS.

## Built from nature-figure

This skill is adapted from [nature-figure](https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-figure)
v2.0, a production-grade skill for Nature/Science/Cell-level manuscript figures.

**What we learned and kept:**

| Source in nature-figure | What it is | How we use it |
|---|---|---|
| `references/api.md` | Palette constants + helper function signatures | Kept all 7 helpers, renamed 6 palettes to generic names |
| `references/common-patterns.md` | 16 reusable layout/encoding patterns | Kept 14 (dropped dark image plate, kept multi-row grid) |
| `tutorials.md` + `chart-types.md` | End-to-end chart scripts | Merged into `chart-recipes.md`, expanded with 2 hand-written types |
| `static/core/stance.md` | Color policy, archetype classification | Distilled to `design-basics.md`, dropped archetypes |
| Design-level conventions | SVG-first export, editable text, rcParams | Kept exactly as-is |
| Chart atlas images | Preview grids for each chart family | Downloaded 9 of 10 (skipped image plates) |

**What we intentionally dropped and why:**

| Removed | Why |
|---|---|
| Figure contract (core conclusion, evidence hierarchy, archetype) | Work charts don't need a scientific argument scaffold |
| Backend selection gate (Python or R) | Only Python is needed |
| R backend entirely | Not in scope |
| 4 Nature-specific palette names | Renamed to generic identifiers (PALETTE_SOFT, PALETTE_TIME_SERIES, etc.) |
| Image plates, 3D sphere | Not data-analysis chart types |
| QA contracts, legend conventions, Nature observations | Academic-only overhead |
| `figures4papers` demo scripts | Replaced by runnable recipes with mock data |
| `manifest.yaml` + `static/` split | Unnecessary without backend selection axis |
| Privacy rules for private templates | Not applicable to work context |

**What we wrote from scratch:**

| Added | Why |
|---|---|
| Distribution charts (histogram, violin, box, ridgeline) | In nature-figure's atlas but had no reference code |
| Network & matrix charts (bubble matrix, adjacency, node-link, bipartite) | Same — atlas preview existed, no reference code |
| All recipes include runnable mock data | So every recipe works immediately without user data |

The result: ~51 KB of pure text (no binary assets), 6 files, single-layer routing.
Compare to nature-figure's 2,600+ lines of reference depth across 12 files plus
40+ image assets and 15+ demo scripts.

## Chart Type Atlas

| # | Type | Preview | Common Use |
|---|------|---------|------------|
| 1 | Bar charts | ![bars](assets/chart-atlas/atlas-01-bar-charts.png) | Group comparison, signed differences, stacked composition |
| 2 | Line & trend | ![lines](assets/chart-atlas/atlas-02-line-trends.png) | Time courses, uncertainty bands, intervention markers |
| 3 | Heatmaps | ![heat](assets/chart-atlas/atlas-03-heatmaps.png) | Z-score matrices, abundance, annotated tables |
| 4 | Scatter & bubble | ![scatter](assets/chart-atlas/atlas-04-scatter-bubble.png) | Correlations, clusters, volcano-style, 3-variable encoding |
| 5 | Radar & polar | ![radar](assets/chart-atlas/atlas-05-radar-polar.png) | Multi-axis benchmarking, circular summaries |
| 6 | Distributions | ![dist](assets/chart-atlas/atlas-06-distributions.png) | Histograms, violin, box, ridgeline |
| 7 | Forest & interval | ![forest](assets/chart-atlas/atlas-07-forest-interval.png) | Effect sizes, confidence intervals, point ranges |
| 8 | Area & stacked | ![area](assets/chart-atlas/atlas-08-area-stacked.png) | Filled trajectories, share stacks, cumulative curves |
| 9 | Network & matrix | ![net](assets/chart-atlas/atlas-10-network-matrix.png) | Bubble matrices, adjacency, node-link, bipartite |

## Quick Start

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"

def save_chart(fig, filename, dpi=300):
    fig.savefig(f"{filename}.svg", bbox_inches="tight")
    fig.savefig(f"{filename}.png", dpi=dpi, bbox_inches="tight")
```

Then open [references/chart-recipes.md](references/chart-recipes.md), pick a recipe,
copy the code, and run it.

## File Structure

```
├── SKILL.md                     # Main router
├── README.md                    # This file
├── assets/
│   └── chart-atlas/             # 9 preview images
└── references/
    ├── palette.md               # 6 palette families
    ├── api.md                   # 7 reusable helper functions
    ├── chart-patterns.md         # 14 layout patterns + 3 style techniques
    ├── chart-recipes.md          # 9 chart family recipes
    └── design-basics.md          # Color strategy, typography, panel hierarchy
```