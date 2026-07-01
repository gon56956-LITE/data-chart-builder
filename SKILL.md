---
name: data-chart-builder
description: Create, revise, and polish publication-quality static data charts with Python matplotlib/seaborn. Use for bar charts, line/trend charts, heatmaps, scatter/bubble plots, radar/polar charts, distribution plots, forest/interval plots, area/stacked charts, network/matrix charts, and Chinese chart requests such as 画图, 作图, 柱状图, 折线图, 热图, 散点图, 气泡图, 雷达图, 分布图, 小提琴图, 箱线图, 森林图, 区间图, 面积图, 堆叠图, 网络图, 矩阵图, 数据可视化, or 图表.
---

# Data Chart Builder — Router

Build publication-quality data charts with Python (matplotlib/seaborn).
This skill is a single-file router: start here, then load references as needed.

## Routing protocol

### 1. Quick start: always apply these settings

Before any chart, set the three mandatory rcParams and the export helper:

`python
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans']
plt.rcParams['svg.fonttype'] = 'none'   # editable text in SVG

def save_chart(fig, filename, dpi=300):
    fig.savefig(f"{filename}.svg", bbox_inches='tight')
    fig.savefig(f"{filename}.png", dpi=dpi, bbox_inches='tight')
`

### 2. Choose a chart type

Match the user's request to one of the 9 chart families below.
Load the corresponding section in [references/chart-recipes.md](references/chart-recipes.md).

| # | Chart family | Triggers (Chinese / English) |
|---|---|---|
| 1 | Bar charts | 柱状图、分组柱状图、堆叠柱状图、bar、grouped bar、stacked bar、ablation bar |
| 2 | Line & trend | 折线图、趋势、时间序列、line、trend、time series |
| 3 | Heatmaps | 热图、热力图、heatmap、z-score heatmap |
| 4 | Scatter & bubble | 散点图、气泡图、scatter、bubble、correlation plot |
| 5 | Radar & polar | 雷达图、极坐标、radar、polar、spider chart |
| 6 | Distributions | 分布图、直方图、小提琴图、箱线图、histogram、violin、boxplot、ridgeline |
| 7 | Forest & interval | 森林图、区间图、效应量、forest plot、interval plot、effect size |
| 8 | Area & stacked | 面积图、堆叠图、fill-between、stacked area、cumulative |
| 9 | Network & matrix | 网络图、矩阵图、邻接图、bubble matrix、adjacency、node-link、bipartite |

### 3. Load references on demand

| When you need... | Load... |
|---|---|
| Color palettes (6 families) | [references/palette.md](references/palette.md) |
| Reusable helper functions (apply_chart_style, make_grouped_bar, make_trend, make_heatmap, make_forest_plot, finalize_figure, etc.) | [references/api.md](references/api.md) |
| Layout patterns (multi-panel grids, legend panels, dynamic axes, hatch encoding, etc.) | [references/chart-patterns.md](references/chart-patterns.md) |
| Complete chart recipes with code and mock data | [references/chart-recipes.md](references/chart-recipes.md) |
| Design principles (color strategy, typography, panel hierarchy, export) | [references/design-basics.md](references/design-basics.md) |

### 4. Build the chart

1. Load the matching recipe section from [references/chart-recipes.md](references/chart-recipes.md).
2. Apply design principles from [references/design-basics.md](references/design-basics.md) when choosing colors, typography, and panel layout.
3. Use helpers from [references/api.md](references/api.md) for common patterns (bar grouping, trend lines, heatmaps, forest plots).
4. For multi-panel figures, use layout patterns from [references/chart-patterns.md](references/chart-patterns.md).
5. Export as SVG (primary) + PNG, then close the figure.

The chart serves the data story. Aesthetic polish is subordinate to making the data pattern clear, honest, and readable.

## When NOT to use this skill

- Flowcharts, architecture diagrams, UML, or mind maps — use a diagramming tool.
- Interactive / web-first charts (Plotly, Altair, Bokeh) — this skill is matplotlib-only.
- PowerPoint or Google Slides chart editing.
- Dashboards and BI reports.
- 3D rendering or GIS visualization.
