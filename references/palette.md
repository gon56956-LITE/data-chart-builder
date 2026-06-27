# Palettes — Data Chart Builder

Six palette families for different visualization needs.
All color values are hex strings, ready to copy-paste.

---

## PALETTE — General purpose

`python
PALETTE = {
    # Primary method / core series
    'blue_main':      '#0F4D92',
    'blue_secondary': '#3775BA',

    # Positive / improvement gradient
    'green_1': '#DDF3DE',
    'green_2': '#AADCA9',
    'green_3': '#8BCF8B',

    # Baseline / control / negative
    'red_1':      '#F6CFCB',
    'red_2':      '#E9A6A1',
    'red_strong': '#B64342',

    # Neutral support
    'neutral_light': '#CFCECE',
    'neutral_mid':   '#767676',
    'neutral_dark':  '#4D4D4D',
    'neutral_black': '#272727',

    # Accent (use sparingly)
    'gold':    '#FFD700',
    'teal':    '#42949E',
    'violet':  '#9A4D8E',
    'magenta': '#EA84DD',
}

DEFAULT_COLORS = [
    PALETTE['blue_main'],
    PALETTE['green_3'],
    PALETTE['red_strong'],
    PALETTE['teal'],
    PALETTE['violet'],
    PALETTE['neutral_light'],
]
`

Use DEFAULT_COLORS when colors carry explicit semantic meaning (hero, baseline, positive variant).
Green and red should usually be reserved for directional annotations, not primary series identity.

---

## PALETTE_PASTEL — Unified low-saturation for method-family comparison

`python
PALETTE_PASTEL = {
    # Baseline / control family
    'baseline_dark': '#484878',
    'baseline_mid':  '#7884B4',
    'baseline_soft': '#B4C0E4',

    # Ours / treatment family
    'ours_tiny':  '#E4E4F0',
    'ours_base':  '#E4CCD8',
    'ours_large': '#F0C0CC',

    # Overview / concept panel backgrounds
    'bg_lilac': '#E0E0F0',
    'bg_aqua':  '#E0F0F0',
    'bg_peach': '#F0E0D0',

    # Neutral support
    'neutral_light': '#D8D8D8',
    'neutral_mid':   '#A8A8A8',
    'neutral_dark':  '#606060',

    # Directional annotations only
    'delta_up':   '#2E9E44',
    'delta_down': '#E53935',
}

DEFAULT_COLORS_PASTEL = [
    PALETTE_PASTEL['baseline_dark'],
    PALETTE_PASTEL['baseline_mid'],
    PALETTE_PASTEL['baseline_soft'],
    PALETTE_PASTEL['ours_tiny'],
    PALETTE_PASTEL['ours_base'],
    PALETTE_PASTEL['ours_large'],
]
`

Use when several compared categories belong to one or two related families and the page should feel visually unified.
Keep the same hue family for the same method across all panels.

---

## PALETTE_DARK_BG — For dark-background charts

`python
PALETTE_DARK_BG = {
    'bg': '#000000',
    'context': '#B8B8B8',
    'cyan': '#22D7E6',
    'magenta': '#FF2AD4',
    'white': '#FFFFFF',
}
`

For high-contrast charts on dark backgrounds. Not for image plates — use only when dark background serves the data story.

---

## PALETTE_SOFT — Aqua/teal/lilac/violet, gentle contrast

`python
PALETTE_SOFT = {
    'aqua': '#77D7D1',
    'teal': '#33B5A5',
    'lilac': '#B9A7E8',
    'violet': '#7C6CCF',
    'callout_red': '#E53935',
    'neutral': '#D9D9D9',
}
`

Good for categorical data where you want distinct but not aggressive color separation.

---

## PALETTE_TIME_SERIES — Multi-phase temporal coloring

`python
PALETTE_TIME_SERIES = {
    'baseline': '#272727',
    'phase1': '#E28E2C',
    'phase2': '#D24B40',
    'phase3': '#5B8FD6',
    'phase4': '#7BAA5B',
    'phase5': '#C45AD6',
    'group_band': '#F2E6D9',
}
`

For time-series data with distinct phases (weekly, monthly, quarterly).

---

## PALETTE_WAVE — Grouped wave coloring

`python
PALETTE_WAVE = {
    'neutral_light': '#D8D8D8',
    'neutral_mid': '#8F8F8F',
    'wave1': '#D9544D',
    'wave2': '#5B7FCA',
    'wave3': '#B89BD9',
    'outline': '#4D4D4D',
}
`

For data grouped into distinct cohorts or waves.
