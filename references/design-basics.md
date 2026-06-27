# Design Basics — Data Chart Builder

Core design principles distilled for everyday data visualization.

---

## Color Strategy

**One neutral family + one signal family + one accent family.**

Do not assign high-saturation blue, green, red, purple just because categories differ.
Coherent hue families make a figure feel integrated, not collaged.

- **Neutral family** — background, reference lines, less important data
- **Signal family** — primary data series, hero comparison
- **Accent family** — sparingly, for callouts or directional cues

**Green and red are reserved for directional meaning** — gains vs drops, above vs below threshold,
not for general category identity.

Keep the same color for the same condition or method across all panels in a multi-panel figure.

---

## Typography

- Default font stack: `Arial, DejaVu Sans, Liberation Sans` — cross-platform consistency
- Always set `svg.fonttype = 'none'` for editable SVG text
- Font size scale:

| Context | font.size |
|---------|-----------|
| Compact multi-panel | 6-8 |
| Standard single chart | 10-12 |
| Presentation / large panel | 16-24 |

- Use bold lowercase `a`, `b`, `c` for panel labels, placed at top-left via `ax.transAxes`

---

## Panel Hierarchy

**Don't equalize panel sizes when evidence importance differs.**

- Hero panel gets the most space and the clearest visual encoding
- Supporting panels should be visually quieter
- Prefer one hero panel + subordinates over equal-sized grid

For multi-panel information structure, follow the three-layer model:

| Layer | Question | Encoding |
|-------|----------|----------|
| Overview | What is the overall pattern? | Stacked bars, composition |
| Deviation | What makes each group unique? | Z-score heatmap, diverging colormap |
| Relationship | How do variables covary? | Scatter, bubble, correlation |

---

## Legend Guidelines

- Use `frameon=False` always
- For multi-panel figures: dedicated legend panel instead of repeating legends
- Prefer direct labels over legends when categories are spatially fixed
- Place large legends below panels: `bbox_to_anchor=(0.5, -0.24), loc="upper center"`

---

## Axis Guidelines

- No right or top spines: `axes.spines.right = False`, `axes.spines.top = False`
- No gridlines by default
- Y-axis range should hug the data — never 0-100 when values are 80-95
- Use sparse `set_yticks` with round numbers

---

## Export

- **SVG is primary output** — editable text, resolution-independent
- PNG is secondary, DPI >= 300
- Always `bbox_inches='tight'`
- Always `plt.close(fig)` after saving
- Default output directory: `./figures/`