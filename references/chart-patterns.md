# Chart Patterns — Data Chart Builder

Reusable layout and encoding patterns for matplotlib-based charts.

---

## Pattern 1: Ultra-wide multi-metric bar panel

```python
fig = plt.figure(figsize=(28, 6))
gs = gridspec.GridSpec(1, n_metrics + 1)

for i, metric in enumerate(metrics):
    ax = fig.add_subplot(gs[i])
    ax.bar(x, values[metric], color=colors)
    ax.set_ylabel(metric, fontsize=32, labelpad=12)
    ax.set_xticks([])

# Last panel: legend only
ax_leg = fig.add_subplot(gs[-1])
ax_leg.legend(handles, labels, fontsize=28, loc="center", frameon=False)
ax_leg.set_axis_off()
```

Width often 3-4x height. Enables left-to-right narrative scanning.

---

## Pattern 2: Dedicated legend panel

```python
fig, axes = plt.subplots(1, n_data + 1, figsize=(...))
for i, ax in enumerate(axes[:-1]):
    bars = ax.bar(...)
    if i == 0:
        handles, labels = ax.get_legend_handles_labels()

axes[-1].legend(handles, labels, fontsize=28, loc="center", frameon=False)
axes[-1].set_axis_off()
```

---

## Pattern 3: Categorical bars without x-tick labels

```python
ax.set_xticks([])
```

---

## Pattern 4: Dynamic y-axis tightening

```python
margin = (values.max() - values.min()) * 0.1
ax.set_ylim([values.min() - margin, values.max() + margin])
```

---

## Pattern 5: Alpha-graduated ablation bars

```python
blue_rgb = (0.215686, 0.458824, 0.729412)
n_ablations = len(configs)
alphas = np.linspace(0.2, 1.0, n_ablations)
colors = [(blue_rgb[0], blue_rgb[1], blue_rgb[2], a) for a in alphas]
```

---

## Pattern 6: Hatch encoding for print-safe grayscale

```python
hatches = ["/", "\\", ".", "x", "o", "+"]
for bar_container, hatch in zip(grouped_bars, hatches):
    for patch in bar_container:
        patch.set_hatch(hatch)
        patch.set_edgecolor("black")
        patch.set_linewidth(1.5)
```

---

## Pattern 7: Semantic color mapping

```python
method_colors = {
    "Baseline":   PALETTE_PASTEL["baseline_dark"],
    "Variant A":  PALETTE_PASTEL["baseline_mid"],
    "Variant B":  PALETTE_PASTEL["baseline_soft"],
    "Ours-Tiny":  PALETTE_PASTEL["ours_tiny"],
    "Ours-Base":  PALETTE_PASTEL["ours_base"],
    "Ours-Large": PALETTE_PASTEL["ours_large"],
}
```

Reserve green/red only for directional annotations:

```python
ax.scatter(x_gain, y_gain, marker="^", color="#2E9E44", s=90, zorder=6)
ax.scatter(x_drop, y_drop, marker="v", color="#E53935", s=90, zorder=6)
```

---

## Pattern 8: In-bar text with luminance-aware color

```python
def annotate_bars(ax, bars, colors, fmt="{:.2f}", fontsize=32, offset=-0.10):
    for bar, color in zip(bars, colors):
        c = color.lstrip("#")
        r, g, b = int(c[0:2],16)/255, int(c[2:4],16)/255, int(c[4:6],16)/255
        lum = 0.299*r + 0.587*g + 0.114*b
        textcolor = "white" if lum < 0.5 else "black"
        value = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2,
                value + offset,
                fmt.format(value),
                ha="center", va="bottom",
                fontsize=fontsize, color=textcolor)
```

---

## Pattern 9: Fill-between trend with hatch

```python
ax.fill_between(x, 0, cumsum_series,
                color=fill_color,
                hatch="///",
                edgecolor="black",
                label=label_name)
ax.fill_between(x, 0, cumsum_series,
                facecolor="none",
                edgecolor="white",
                linewidth=2)
```

---

## Pattern 10: Annotate events on trend lines

```python
def mark_events(ax, x_labels, y_cumsum, events_dict, dy_fraction=0.1):
    x_index = {label: i for i, label in enumerate(x_labels)}
    y_lo, y_hi = ax.get_ylim()
    dy = dy_fraction * (y_hi - y_lo)
    for date, label in events_dict.items():
        if date not in x_index:
            continue
        i = x_index[date]
        y_data = y_cumsum[i]
        ax.annotate(
            label,
            xy=(i, y_data),
            xytext=(i, y_data + dy),
            ha="center", va="bottom", fontsize=11,
            arrowprops=dict(arrowstyle="-|>", lw=1.3, color="black",
                            shrinkA=0, shrinkB=0, mutation_scale=15)
        )
```

---

## Pattern 11: Grouped bars across multiple datasets

```python
num_methods = len(methods)
xtick_positions = []
for dataset_idx, dataset_name in enumerate(datasets):
    x_start = dataset_idx * (num_methods + 1)
    ax.bar(
        np.arange(num_methods) + x_start,
        values[dataset_name],
        color=method_colors,
        label=methods if dataset_idx == 0 else ["_nolegend_"] * num_methods,
    )
    xtick_positions.append(np.mean(np.arange(num_methods)) + x_start)
ax.set_xticks(xtick_positions)
ax.set_xticklabels(datasets)
```

---

## Pattern 12: Schematic hero panel with supporting quant row

```python
fig = plt.figure(figsize=(7.2, 6.2))
gs = fig.add_gridspec(2, 4, height_ratios=[2.2, 1.0], hspace=0.18, wspace=0.28)

ax_top = fig.add_subplot(gs[0, :])
ax_b = fig.add_subplot(gs[1, 0])
ax_c = fig.add_subplot(gs[1, 1:3])
ax_d = fig.add_subplot(gs[1, 3])
```

---

## Pattern 14: Multi-row grid (parallel layout)

```python
fig = plt.figure(figsize=(7.2, 6.8))
gs = fig.add_gridspec(3, 3, height_ratios=[1.0, 1.35, 0.8], hspace=0.28, wspace=0.32)

axes_top = [fig.add_subplot(gs[0, i]) for i in range(3)]
axes_mid = [fig.add_subplot(gs[1, i]) for i in range(3)]
axes_bot = [fig.add_subplot(gs[2, i]) for i in range(3)]
```

---

## Pattern 15: Asymmetric hero panel

```python
fig = plt.figure(figsize=(7.2, 5.8))
gs = fig.add_gridspec(3, 4, hspace=0.25, wspace=0.28)

ax_a = fig.add_subplot(gs[0, :2])
ax_b = fig.add_subplot(gs[0, 2])
ax_c = fig.add_subplot(gs[1, :2])
ax_d = fig.add_subplot(gs[1, 2])
ax_e = fig.add_subplot(gs[:, 3])
ax_f = fig.add_subplot(gs[2, :2])
```

---

## Pattern 16: Direct labels inside filled regions

```python
for x_text, y_text, text, color in label_specs:
    ax.text(
        x_text, y_text, text,
        color=color,
        ha="center", va="center",
        fontsize=9, fontweight="bold",
    )
```

---

## Style Techniques

### Scientific notation on y-axis

```python
ax.ticklabel_format(axis="y", style="sci", scilimits=(0, 0))
```

### Custom spine positioning

```python
ax.spines["bottom"].set_position(("data", 0))
ax.xaxis.set_ticks_position("bottom")
ax.spines["left"].set_bounds(0, y_max)
```

### GridSpec multi-panel skeleton

```python
from matplotlib import gridspec

fig = plt.figure(figsize=(36, 12))
gs = gridspec.GridSpec(2, 4)

ax_top_left  = fig.add_subplot(gs[0, 0])
ax_top_right = fig.add_subplot(gs[0, 1:3])
ax_legend    = fig.add_subplot(gs[0, 3])
ax_bottom    = fig.add_subplot(gs[1, :])
```