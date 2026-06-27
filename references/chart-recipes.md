# Chart Recipes — Data Chart Builder

Complete code recipes for all 9 chart families.
Each recipe includes mock data so you can run it immediately.
All use helpers from [api.md](api.md) and patterns from [chart-patterns.md](chart-patterns.md).

---

## 1. Bar Charts

Bar charts are for comparing values across categories — grouped, stacked, horizontal, log-scale, ablation.

### 1.1 Grouped bar (multi-metric comparison)

```python
import os, numpy as np, matplotlib.pyplot as plt
from matplotlib import gridspec

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 24
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.linewidth"] = 3

methods = ["Method A", "Method B", "Method C", "Ours-Tiny", "Ours-Base", "Ours-Large"]
colors  = ["#484878", "#7884B4", "#B4C0E4", "#E4E4F0", "#E4CCD8", "#F0C0CC"]
metrics = ["Metric 1", "Metric 2", "Metric 3"]
mean = {
    "Metric 1": np.array([0.81, 0.83, 0.86, 0.89, 0.91, 0.92]),
    "Metric 2": np.array([0.63, 0.67, 0.71, 0.74, 0.77, 0.79]),
    "Metric 3": np.array([0.41, 0.45, 0.49, 0.53, 0.56, 0.58]),
}
std  = {k: v * 0.03 for k, v in mean.items()}

fig = plt.figure(figsize=(28, 6))
gs = gridspec.GridSpec(1, len(metrics) + 1)

handles, labels = None, None
for col, metric in enumerate(metrics):
    ax = fig.add_subplot(gs[col])
    bars = ax.bar(range(len(methods)), mean[metric], yerr=std[metric],
                  capsize=5, color=colors, label=methods,
                  error_kw={"elinewidth": 2, "capthick": 2})
    if col == 0:
        handles, labels = ax.get_legend_handles_labels()
    ax.set_xticks([])
    y_vals = mean[metric]
    margin = (y_vals.max() - y_vals.min()) * 0.15
    ax.set_ylim([y_vals.min() - margin, y_vals.max() + margin])
    ax.set_ylabel(metric, fontsize=32)

ax_leg = fig.add_subplot(gs[-1])
ax_leg.legend(handles, labels, fontsize=28, loc="center", frameon=False)
ax_leg.set_axis_off()

fig.tight_layout(pad=2)
os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/bars_grouped.svg", bbox_inches="tight")
fig.savefig("./figures/bars_grouped.png", dpi=300)
plt.close(fig)
```

### 1.2 Ablation bar (horizontal, alpha-graduated)

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 24
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.linewidth"] = 3

configs = ["None", "+ Module A", "+ Module B", "+ Module C", "Full"]
values  = np.array([0.72, 0.78, 0.81, 0.84, 0.88])
stds    = np.array([0.02, 0.02, 0.01, 0.01, 0.01])

n = len(configs)
blue_rgb = (0.215686, 0.458824, 0.729412)
alphas = np.linspace(0.2, 1.0, n)
colors = [(blue_rgb[0], blue_rgb[1], blue_rgb[2], a) for a in alphas]

fig, ax = plt.subplots(figsize=(12, 6))
ax.barh(range(n), values, xerr=stds, color=colors, ecolor="k", capsize=5)
ax.set_yticks(range(n))
ax.set_yticklabels(configs)
ax.set_xlim([values.min() - 0.05, values.max() + 0.03])
ax.set_xlabel("Score", fontsize=32)

fig.tight_layout(pad=2)
os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/bars_ablation.svg", bbox_inches="tight")
fig.savefig("./figures/bars_ablation.png", dpi=300)
plt.close(fig)
```

### 1.3 Log-scale bar

```python
ax.set_yscale("log")
ymin, ymax = ax.get_ylim()
ax.set_ylim(ymin, ymax * 20)

for i, val in enumerate(values):
    ax.text(i, val * 1.1, f"{val:.3f}", ha="center", va="bottom", fontsize=16)
```

---

## 2. Line & Trend Charts

Trend lines show change over a continuous variable — time, epoch, dose.

### 2.1 Multi-panel trend with shared legend

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 15
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.linewidth"] = 2

methods = ["Baseline", "Ours-Tiny", "Ours-Base", "Ours-Large"]
colors  = ["#7884B4", "#E4E4F0", "#E4CCD8", "#F0C0CC"]
x = np.arange(0, 100, 5)

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
np.random.seed(42)

for panel_idx, (ax, panel_name) in enumerate(zip(axes[:2], ["Training", "Validation"])):
    for method, color in zip(methods, colors):
        y = 0.48 + 0.42 * (1 - np.exp(-x / 30)) + np.random.randn(len(x)) * 0.01
        if method == "Baseline":
            y -= 0.03
        elif method == "Ours-Tiny":
            y += 0.00
        elif method == "Ours-Base":
            y += 0.02
        elif method == "Ours-Large":
            y += 0.03
        ax.plot(x, y, color=color, lw=2.5, marker="o", markersize=6, label=method)
    ax.set_title(panel_name, fontsize=18)
    ax.set_xlabel("Epoch", fontsize=16)
    ax.set_ylabel("Loss", fontsize=16)
    if panel_idx == 0:
        handles, labels = ax.get_legend_handles_labels()

axes[2].legend(handles, labels, fontsize=14, loc="center", frameon=False)
axes[2].set_axis_off()

fig.tight_layout(pad=2)
os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/trends.svg", bbox_inches="tight")
fig.savefig("./figures/trends.png", dpi=300)
plt.close(fig)
```

### 2.2 Event-annotated trend

```python
def mark_events(ax, x_labels, y_vals, events_dict, dy_fraction=0.1):
    x_index = {label: i for i, label in enumerate(x_labels)}
    y_lo, y_hi = ax.get_ylim()
    dy = dy_fraction * (y_hi - y_lo)
    for date, label in events_dict.items():
        if date not in x_index:
            continue
        i = x_index[date]
        ax.annotate(label, xy=(i, y_vals[i]), xytext=(i, y_vals[i] + dy),
                    ha="center", va="bottom", fontsize=11,
                    arrowprops=dict(arrowstyle="-|>", lw=1.3, color="black",
                                    shrinkA=0, shrinkB=0, mutation_scale=15))

events = {"2020-Q1": "Launch", "2021-Q3": "Pivot", "2023-Q1": "Scale"}
mark_events(ax, quarters, cumulative, events)
```

---

## 3. Heatmaps

Heatmaps show 2D matrices — correlations, z-scores, abundance, confusion matrices.

### 3.1 Dual-colormap heatmap (positive/negative columns)

```python
import os, numpy as np, matplotlib as mpl, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 16
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.linewidth"] = 2

methods = ["Method A", "Method B", "Method C", "Method D"]
metrics = ["Score (+)", "Error (-)", "F1 (+)", "Loss (-)"]
matrix  = np.array([
    [0.88, 0.12, 0.85, 0.20],
    [0.81, 0.18, 0.78, 0.28],
    [0.75, 0.25, 0.72, 0.35],
    [0.70, 0.30, 0.68, 0.40],
])

fig, ax = plt.subplots(figsize=(10, 6))
n_rows, n_cols = matrix.shape
vmin, vmax = matrix.min(0), matrix.max(0)

for j in range(n_cols):
    is_positive = (j % 2 == 0)
    cmap = plt.cm.Reds if is_positive else plt.cm.Blues_r
    norm = mpl.colors.Normalize(
        vmin=0 if is_positive else vmax[j],
        vmax=vmax[j] if is_positive else 0
    )
    ax.imshow(matrix[:, j:j+1], cmap=cmap, norm=norm,
              aspect="auto", extent=[j-0.5, j+0.5, 0, n_rows], origin="lower")

for (i, j), val in np.ndenumerate(matrix):
    is_positive = (j % 2 == 0)
    cmap = plt.cm.Reds if is_positive else plt.cm.Blues_r
    norm = mpl.colors.Normalize(vmin=0 if is_positive else vmax[j],
                                 vmax=vmax[j] if is_positive else 0)
    r, g, b, _ = cmap(norm(val))
    lum = 0.299*r + 0.587*g + 0.114*b
    color = "white" if lum < 0.5 else "black"
    ax.text(j, i + 0.5, f"{val:.2f}", ha="center", va="center", fontsize=13, color=color)

ax.set_xlim(-0.5, n_cols - 0.5)
ax.set_xticks(np.arange(n_cols))
ax.set_xticklabels(metrics, rotation=30, ha="right", fontsize=14)
ax.tick_params(axis="x", bottom=False, top=False, length=0)
ax.set_yticks(np.arange(n_rows) + 0.5)
ax.set_yticklabels(methods, fontsize=14)
ax.set_frame_on(False)
ax.invert_yaxis()

fig.tight_layout(pad=2)
os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/heatmap.svg", bbox_inches="tight")
fig.savefig("./figures/heatmap.png", dpi=300)
plt.close(fig)
```

### 3.2 Z-score deviation heatmap

```python
z = (matrix - matrix.mean(axis=0)) / matrix.std(axis=0)
im = ax.imshow(z, cmap="RdBu_r", aspect="auto", vmin=-2.5, vmax=2.5)
cbar = fig.colorbar(im, ax=ax)
cbar.set_label("Z-score")

for (i, j), val in np.ndenumerate(z):
    ax.text(j, i, f"{val:.1f}", ha="center", va="center", fontsize=10)
```

Red = above mean, blue = below mean. Orthogonal information to absolute-value heatmaps.

---

## 4. Scatter & Bubble Charts

Scatter shows relationships between two continuous variables. Add size or color for a third.

### 4.1 Scatter with color-coded clusters

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 12
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False

np.random.seed(42)

fig, ax = plt.subplots(figsize=(8, 6))

clusters = {"A": "#0F4D92", "B": "#8BCF8B", "C": "#B64342"}
for label, color in clusters.items():
    n = 40
    cx, cy = np.random.randn(2) * 3
    x = np.random.randn(n) * 1.5 + cx
    y = np.random.randn(n) * 1.5 + cy
    ax.scatter(x, y, c=color, s=60, alpha=0.7, edgecolors="none", label=label)

ax.set_xlabel("Dimension 1", fontsize=14)
ax.set_ylabel("Dimension 2", fontsize=14)
ax.legend(frameon=False, fontsize=12)
fig.tight_layout(pad=2)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/scatter_clusters.svg", bbox_inches="tight")
fig.savefig("./figures/scatter_clusters.png", dpi=300)
plt.close(fig)
```

### 4.2 Bubble chart (3-variable encoding)

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 12

np.random.seed(42)
n = 30
x = np.random.uniform(0, 100, n)
y = np.random.uniform(0, 100, n)
size_var = np.random.uniform(10, 500, n)
categories = np.random.choice(["Product A", "Product B", "Product C"], n)
colors = {"Product A": "#0F4D92", "Product B": "#8BCF8B", "Product C": "#B64342"}

fig, ax = plt.subplots(figsize=(9, 7))
for cat in categories:
    mask = categories == cat
    ax.scatter(x[mask], y[mask], s=size_var[mask], c=colors[cat],
               edgecolors="white", linewidth=0.8, alpha=0.85, label=cat)

ax.axvline(np.median(x), lw=1.2, ls="--", color="#767676", alpha=0.6)
ax.axhline(np.median(y), lw=1.2, ls="--", color="#767676", alpha=0.6)

# Quadrant labels
for qx, qy, text in [(0.02, 0.98, "High X, High Y"),
                       (0.98, 0.98, "Low X, High Y"),
                       (0.02, 0.02, "High X, Low Y"),
                       (0.98, 0.02, "Low X, Low Y")]:
    ax.text(qx, qy, text, transform=ax.transAxes, fontsize=7.5,
            color="#888888", style="italic", ha="left" if qx < 0.5 else "right",
            va="top" if qy > 0.5 else "bottom")

ax.set_xlabel("X Variable", fontsize=14)
ax.set_ylabel("Y Variable", fontsize=14)
ax.legend(frameon=False, fontsize=12)
fig.tight_layout(pad=2)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/scatter_bubble.svg", bbox_inches="tight")
fig.savefig("./figures/scatter_bubble.png", dpi=300)
plt.close(fig)
```

---

## 5. Radar & Polar Charts

Radar charts compare multiple metrics across categories simultaneously.

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 14

methods = ["Method A", "Method B", "Method C"]
colors  = ["#0F4D92", "#8BCF8B", "#B64342"]
metrics = ["Speed", "Accuracy", "Memory", "Coverage", "Precision", "Recall"]
values  = np.array([
    [85, 72, 60, 88, 79, 91],
    [70, 88, 75, 65, 92, 78],
    [62, 78, 90, 72, 68, 85],
])

n_metrics = len(metrics)
angles = np.linspace(2 * np.pi, 0, n_metrics, endpoint=False)
angles_closed = np.append(angles, angles[0])

fig = plt.figure(figsize=(10, 9))
ax = fig.add_subplot(111, projection="polar")

for i, (method, color) in enumerate(zip(methods, colors)):
    vals = np.append(values[i], values[i][0])
    ax.plot(angles_closed, vals, color=color, lw=2, label=method)
    ax.fill(angles_closed, vals, color=color, alpha=0.08)
    ax.scatter(angles, values[i], color=color, s=30, zorder=5)

ax.set_theta_zero_location("N")
ax.set_xticks(angles)
ax.set_xticklabels(metrics, fontsize=12)
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20", "40", "60", "80", "100"], fontsize=8, color="#888888")
ax.grid(True, alpha=0.3)

for spine in ax.spines.values():
    spine.set_visible(False)

ax.legend(loc="upper right", bbox_to_anchor=(1.35, 0.05), fontsize=12, frameon=False)

fig.tight_layout(pad=2)
os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/radar.svg", bbox_inches="tight")
fig.savefig("./figures/radar.png", dpi=300)
plt.close(fig)
```

**Key settings:**
- `ax.set_theta_zero_location("N")` — top-start convention
- Remove default spines/grid; the polar projection handles it
- Legend placed outside: `bbox_to_anchor=(1.35, 0.05)`

---

## 6. Distribution Charts

Show how values are spread — histograms, violin plots, boxplots, ridgeline.

### 6.1 Multi-group histogram

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 12
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False

np.random.seed(42)
groups = {
    "Control": np.random.normal(50, 10, 200),
    "Treatment A": np.random.normal(58, 12, 200),
    "Treatment B": np.random.normal(65, 9, 200),
}
colors = {"Control": "#B4C0E4", "Treatment A": "#E4CCD8", "Treatment B": "#F0C0CC"}

fig, ax = plt.subplots(figsize=(10, 6))
for label, data in groups.items():
    ax.hist(data, bins=25, alpha=0.6, color=colors[label], label=label, edgecolor="white")

ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Count", fontsize=14)
ax.legend(frameon=False, fontsize=12)
fig.tight_layout(pad=2)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/dist_histogram.svg", bbox_inches="tight")
fig.savefig("./figures/dist_histogram.png", dpi=300)
plt.close(fig)
```

### 6.2 Violin + box combo

```python
import os, numpy as np, matplotlib.pyplot as plt

np.random.seed(42)
data = [
    np.random.normal(50, 10, 200),
    np.random.normal(55, 15, 200),
    np.random.normal(60, 8, 200),
    np.random.normal(48, 12, 200),
]
labels = ["Q1", "Q2", "Q3", "Q4"]
colors = ["#0F4D92", "#8BCF8B", "#FFD700", "#B64342"]

fig, ax = plt.subplots(figsize=(10, 6))
vp = ax.violinplot(data, positions=range(len(data)), showmeans=True, showmedians=False)
for i, body in enumerate(vp["bodies"]):
    body.set_facecolor(colors[i])
    body.set_alpha(0.6)
    body.set_edgecolor("black")

bp = ax.boxplot(data, positions=range(len(data)), widths=0.15,
                patch_artist=True, showfliers=False)
for i, patch in enumerate(bp["boxes"]):
    patch.set_facecolor("white")
    patch.set_edgecolor(colors[i])
    patch.set_linewidth(1.5)

ax.set_xticks(range(len(data)))
ax.set_xticklabels(labels)
ax.set_ylabel("Value", fontsize=14)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
fig.tight_layout(pad=2)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/dist_violin.svg", bbox_inches="tight")
fig.savefig("./figures/dist_violin.png", dpi=300)
plt.close(fig)
```

### 6.3 Ridgeline (joyplot)

```python
import os, numpy as np, matplotlib.pyplot as plt

np.random.seed(42)
categories = ["Cat A", "Cat B", "Cat C", "Cat D", "Cat E"]
n_cats = len(categories)
data = [np.random.normal(40 + i*5, 6 + i*2, 300) for i in range(n_cats)]
colors = ["#484878", "#7884B4", "#B4C0E4", "#E4CCD8", "#F0C0CC"]

fig, axes = plt.subplots(n_cats, 1, figsize=(10, 8), sharex=True)
plt.subplots_adjust(hspace=-0.5)

for i, (ax, vals, label, color) in enumerate(zip(axes, data, categories, colors)):
    ax.fill_between(np.linspace(vals.min(), vals.max(), 200),
                    np.zeros(200),
                    np.histogram(vals, bins=50, density=True)[0].max() * 1.2,
                    color=color, alpha=0.6)
    ax.hist(vals, bins=50, density=True, color=color, alpha=0.9, edgecolor="white", lw=0.5)
    ax.set_yticks([])
    ax.set_ylabel(label, rotation=0, ha="right", va="center", fontsize=12, fontweight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

axes[-1].set_xlabel("Value", fontsize=14)
fig.tight_layout(pad=2)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/dist_ridgeline.svg", bbox_inches="tight")
fig.savefig("./figures/dist_ridgeline.png", dpi=300)
plt.close(fig)
```

---

## 7. Forest & Interval Charts

Forest plots show effect sizes with confidence intervals — common in comparison studies.

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 12
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False

labels = ["Study A", "Study B", "Study C", "Study D", "Study E", "Overall"]
estimates = [1.2, 0.8, 1.5, 0.9, 1.1, 1.15]
ci_low =    [0.9, 0.5, 1.2, 0.6, 0.8, 1.0]
ci_high =   [1.5, 1.1, 1.8, 1.2, 1.4, 1.3]
colors = ["#0F4D92"] * 5 + ["#B64342"]

fig, ax = plt.subplots(figsize=(8, 5))
y = np.arange(len(labels))[::-1]

for yi, (est, lo, hi, label, color) in enumerate(zip(estimates, ci_low, ci_high, labels, colors)):
    ax.plot([lo, hi], [yi, yi], color=color, lw=2)
    ax.plot(est, yi, marker="o", ms=8, color=color)

ax.axvline(1.0, color="#767676", linestyle="--", linewidth=1.2, alpha=0.8, label="No effect")
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels)
ax.set_xlabel("Effect size (95% CI)", fontsize=14)
ax.legend(frameon=False, fontsize=10)
fig.tight_layout(pad=2)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/forest.svg", bbox_inches="tight")
fig.savefig("./figures/forest.png", dpi=300)
plt.close(fig)
```

---

## 8. Area & Stacked Charts

Area charts show cumulative or compositional change over a continuous axis.

### 8.1 Fill-between stacked area

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 12
plt.rcParams["axes.spines.right"] = False
plt.rcParams["axes.spines.top"] = False

np.random.seed(42)
x = np.arange(0, 48)
y1 = np.cumsum(np.random.uniform(5, 15, 48))
y2 = np.cumsum(np.random.uniform(3, 10, 48))
y3 = np.cumsum(np.random.uniform(2, 8, 48))

fig, ax = plt.subplots(figsize=(12, 5))

ax.fill_between(x, 0, y1, color="#FFA8A6", label="Category A")
ax.fill_between(x, y1, y1 + y2, color="#9BC8FA", label="Category B")
ax.fill_between(x, y1 + y2, y1 + y2 + y3, color="#B9A7E8", label="Category C")

# Overlay trend lines
ax.plot(x, y1, lw=2.5, color="#850C0A")
ax.plot(x, y1 + y2, lw=2.5, color="#13457E")
ax.plot(x, y1 + y2 + y3, lw=2.5, color="#7C6CCF")

ax.set_xlabel("Time", fontsize=14)
ax.set_ylabel("Cumulative Value", fontsize=14)
ax.legend(frameon=False, fontsize=12, loc="upper left")
fig.tight_layout(pad=2)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/area_stacked.svg", bbox_inches="tight")
fig.savefig("./figures/area_stacked.png", dpi=300)
plt.close(fig)
```

### 8.2 Fill-between with uncertainty band

```python
mean = np.sin(np.linspace(0, 4*np.pi, 100)) * 10 + 50
std  = np.abs(np.cos(np.linspace(0, 4*np.pi, 100))) * 5

ax.plot(x, mean, lw=2.5, color="#0F4D92")
ax.fill_between(x, mean - std, mean + std, color="#0F4D92", alpha=0.15)
```

---

## 9. Network & Matrix Charts

Show pairwise relationships — adjacency, correlation, bipartite, node-link.

### 9.1 Bubble matrix (adjacency heatmap)

```python
import os, numpy as np, matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["svg.fonttype"] = "none"
plt.rcParams["font.size"] = 11

np.random.seed(42)
n = 8
labels = [f"Node {chr(65+i)}" for i in range(n)]
matrix = np.random.uniform(0, 1, (n, n))
np.fill_diagonal(matrix, 0)
matrix = (matrix + matrix.T) / 2

fig, ax = plt.subplots(figsize=(8, 7))

for i in range(n):
    for j in range(n):
        val = matrix[i, j]
        if val > 0.05:
            size = val * 400
            color_val = val
            r, g, b, _ = plt.cm.magma(color_val)
            lum = 0.299*r + 0.587*g + 0.114*b
            edge = "white" if lum < 0.5 else "#DDDDDD"
            ax.scatter(j, i, s=size, c=[plt.cm.magma(color_val)],
                       edgecolors=edge, linewidth=1.5, zorder=2)

ax.set_xticks(range(n))
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_yticks(range(n))
ax.set_yticklabels(labels)
ax.set_xlim(-0.8, n - 0.2)
ax.set_ylim(-0.8, n - 0.2)
ax.invert_yaxis()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_frame_on(False)
ax.tick_params(left=False, bottom=False)

fig.tight_layout(pad=2)
os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/network_bubble_matrix.svg", bbox_inches="tight")
fig.savefig("./figures/network_bubble_matrix.png", dpi=300)
plt.close(fig)
```

### 9.2 Node-link diagram

```python
import os, numpy as np, matplotlib.pyplot as plt

np.random.seed(42)
n_nodes = 12
angles = np.linspace(0, 2*np.pi, n_nodes, endpoint=False)
radii = np.random.uniform(0.6, 0.95, n_nodes)
positions = np.column_stack([np.cos(angles) * radii, np.sin(angles) * radii])

n_edges = 18
edges = []
while len(edges) < n_edges:
    i, j = np.random.choice(n_nodes, 2, replace=False)
    if (i, j) not in edges and (j, i) not in edges:
        edges.append((i, j))

groups = np.random.choice(["A", "B", "C"], n_nodes)
group_colors = {"A": "#0F4D92", "B": "#8BCF8B", "C": "#B64342"}

fig, ax = plt.subplots(figsize=(9, 8))

for i, j in edges:
    ax.plot([positions[i, 0], positions[j, 0]],
            [positions[i, 1], positions[j, 1]],
            color="#CFCECE", lw=1, alpha=0.6, zorder=1)

for node in range(n_nodes):
    ax.scatter(positions[node, 0], positions[node, 1],
               s=200, c=group_colors[groups[node]], edgecolors="white",
               linewidth=2, zorder=2)
    ax.text(positions[node, 0], positions[node, 1] + 0.07,
            str(node), ha="center", va="center", fontsize=10, fontweight="bold")

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect("equal")
ax.set_axis_off()

fig.tight_layout(pad=0)
os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/network_node_link.svg", bbox_inches="tight")
fig.savefig("./figures/network_node_link.png", dpi=300)
plt.close(fig)
```

### 9.3 Bipartite layout

```python
import os, numpy as np, matplotlib.pyplot as plt

np.random.seed(42)
left_labels = ["Source A", "Source B", "Source C", "Source D"]
right_labels = ["Target W", "Target X", "Target Y", "Target Z", "Target V"]
left_n = len(left_labels)
right_n = len(right_labels)

links = [(0, 0, 0.8), (0, 1, 0.6), (1, 1, 0.9), (1, 2, 0.4),
         (2, 2, 0.7), (2, 3, 0.5), (3, 3, 0.8), (3, 4, 0.3), (0, 2, 0.5)]
left_colors = ["#0F4D92", "#3775BA", "#7884B4", "#B4C0E4"]
right_colors = ["#E4E4F0", "#E4CCD8", "#F0C0CC", "#8BCF8B", "#FFD700"]

fig, ax = plt.subplots(figsize=(10, 7))
left_x, right_x = 0.1, 0.9

for i, label in enumerate(left_labels):
    y = 0.9 - i * 0.2
    ax.scatter(left_x, y, s=300, c=left_colors[i], edgecolors="white", linewidth=2, zorder=3)
    ax.text(left_x - 0.02, y, label, ha="right", va="center", fontsize=11)

for j, label in enumerate(right_labels):
    y = 0.9 - j * 0.16
    ax.scatter(right_x, y, s=300, c=right_colors[j], edgecolors="white", linewidth=2, zorder=3)
    ax.text(right_x + 0.02, y, label, ha="left", va="center", fontsize=11)

for i, j, w in links:
    ly = 0.9 - i * 0.2
    ry = 0.9 - j * 0.16
    ax.plot([left_x, right_x], [ly, ry], color="#CFCECE", lw=w*5, alpha=0.7, zorder=1)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_axis_off()
fig.tight_layout(pad=0)

os.makedirs("./figures", exist_ok=True)
fig.savefig("./figures/network_bipartite.svg", bbox_inches="tight")
fig.savefig("./figures/network_bipartite.png", dpi=300)
plt.close(fig)
```