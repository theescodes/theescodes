"""Draws the profile banner in the "Gezeiten" design of thees.codes.

It is the site's share card made wide: the name in Schibsted Grotesk on two
lines, the role behind an orange rule, the coordinates in IBM Plex Mono, and
the contour map, one ring per year of the career with today at the centre.
The sea from the home page drifts behind it.

Two files, one per colour scheme, because the site has both and GitHub can
pick one per theme through <picture>. Everything below is copied from the
site repo and has to follow it by hand; each block names its source.
"""
import math
from datetime import date

from outline import text_to_path

# --- Copy: messages/en.json ------------------------------------------------

NAME = ("Thees", "Hengstermann")                 # hero_name, broken as on the site
ROLE = "Senior Software Engineer"                # hero_role
GEO = "53°24′ N · 8°08′ E — Varel, Friesland"    # geo_coordinates — geo_place
HOST = "thees.codes"
TITLE = "Thees Hengstermann — Senior Software Engineer, Varel, Friesland, Germany"

# --- Colours: src/lib/palette.ts ---------------------------------------------

PALETTE = {
    "light": {"bg": "#eef3f2", "ink": "#0b2230", "muted": "#4a6470", "line": "rgba(11,34,48,.14)",
              "signal": "#ff6b2c", "signal-ink": "#b93a0a"},
    "dark": {"bg": "#0a1c26", "ink": "#e9f0f2", "muted": "#9bb0b8", "line": "rgba(233,240,242,.12)",
             "signal": "#ff6b2c", "signal-ink": "#ff8a55"},
}

# --- Career: src/lib/config/site.ts and experience.ts ------------------------

FIRST_YEAR = 2018                     # EXPERIENCE_START
MILESTONE_YEARS = (2018, 2020, 2022, 2025)
BRANCH_YEAR = 2024                    # Lichio, the ring drawn in orange
# Frozen at the year the banner is built: regenerate once a year and it grows
# its newest ring, as the site does on its own.
CURRENT_YEAR = date.today().year

# --- The mug: MUG_PATHS in src/lib/config/site.ts (viewBox 0 0 64 64) ----------

MUG_PATHS = [
    ("M 10 18 L 10 50 Q 10 58 18 58 L 34 58 Q 42 58 42 50 L 42 18 Z", 4),
    ("M 42 24 Q 54 24 54 38 Q 54 52 42 52", 4),
    ("M 18.5 9.25 Q 22 5.75 18.5 2.25", 3.5),
    ("M 26 9.25 Q 29.5 5.75 26 2.25", 3.5),
    ("M 33.5 9.25 Q 37 5.75 33.5 2.25", 3.5),
    ("M 19.5 32.5 L 14.5 37 L 19.5 41.5", 3.2),
    ("M 23.5 42 L 28.5 32", 3.2),
    ("M 32.5 32.5 L 37.5 37 L 32.5 41.5", 3.2),
]

# --- Layout ------------------------------------------------------------------

W, H = 1200, 400
PAD = 64
GROTESK = "SchibstedGrotesk-Variable.ttf"
MONO = "IBMPlexMono-Regular.ttf"

# The map: centre of the rings in banner pixels, and pixels per unit of the
# site's 0-100 map. The outer rings run off the top, bottom and right edge.
MAP_X, MAP_Y, MAP_SCALE = 992, 208, 4.8
DOT = 7

# --- Contour rings: src/lib/contours.ts ----------------------------------------

CENTER = (50, 52)
STEPS, INNER, SPACING, OUTER = 120, 5, 4.5, 41


def contour_radius(base, index, t):
    return base * (1 + 0.11 * math.sin(3 * t + index * 0.55)
                   + 0.06 * math.sin(5 * t + 1.3 + index * 0.35)
                   + 0.03 * math.sin(8 * t + index))


def contour_rings(first, current):
    """One closed ring per year, oldest (outermost) first, in banner pixels."""
    count = max(1, current - first + 1)
    spacing = min(SPACING, (OUTER - INNER) / (count - 1)) if count > 1 else SPACING
    rings = []
    for year in range(first, current + 1):
        index = current - year
        base = INNER + index * spacing
        points = []
        for k in range(STEPS + 1):
            t = k / STEPS * math.pi * 2
            r = contour_radius(base, index, t)
            points.append((MAP_X + r * math.cos(t) * MAP_SCALE, MAP_Y + r * math.sin(t) * MAP_SCALE))
        d = "".join(f"{'M' if k == 0 else 'L'}{x:.1f} {y:.1f}" for k, (x, y) in enumerate(points)) + "Z"
        rings.append((year, d, min(x for x, _ in points)))
    return rings


# --- The sea: heroWaves in src/lib/components/home/geometry.ts ---------------

def waves():
    """Nine faint sine waves, drawn twice the banner's width.

    Each drifts left by one banner width and every period divides it, so the
    loop has no seam. Periods and swell are the site's, scaled to the banner.
    """
    out = []
    for i in range(9):
        amplitude = 4 + (i % 3) * 3
        period = (200, 300, 400)[i % 3]
        mid = H * (6 + i * 10.5) / 100 + 20
        d = "".join(f"{'M' if x == 0 else 'L'}{x} {mid + amplitude * math.sin(x / period * math.pi * 2 + i):.1f}"
                    for x in range(0, 2 * W + 1, 16))
        out.append((d, round(0.06 + (i % 4) * 0.03, 3), 50 + i * 9))
    return out


# --- Type --------------------------------------------------------------------

d_host, w_host = text_to_path(GROTESK, HOST, 23, PAD + 36 + 14, 70, -0.015 * 23, weight=750)
d_first, w_first = text_to_path(GROTESK, NAME[0], 86, PAD - 3, 176, -0.052 * 86, weight=820)
d_last, w_last = text_to_path(GROTESK, NAME[1], 86, PAD - 3, 253, -0.052 * 86, weight=820)
d_role, w_role = text_to_path(GROTESK, ROLE, 31, PAD + 40 + 16, 312, -0.015 * 31, weight=650)
d_geo, w_geo = text_to_path(MONO, GEO, 16, PAD, 358, 0.03 * 16)

rings = contour_rings(FIRST_YEAR, CURRENT_YEAR)
type_right = max(PAD - 3 + w_last, PAD + 56 + w_role, PAD + w_geo)
ring_left = min(left for *_, left in rings)
for label, w in (("host", w_host), ("first", w_first), ("last", w_last), ("role", w_role), ("geo", w_geo)):
    print(f"{label:5} {w:7.1f}px")
print(f"type ends at x={type_right:.0f}, outermost ring starts at x={ring_left:.0f}")


def ring_path(year, d, scheme):
    c = PALETTE[scheme]
    if year == BRANCH_YEAR:
        stroke, width = c["signal"], 2
    elif year in MILESTONE_YEARS:
        stroke, width = c["ink"], 1.5
    else:
        stroke, width = c["ink"], 1.1
    # Stronger than the site's contour tokens, as on the share card: GitHub
    # shows the banner at about two thirds of its size.
    opacity = "" if year == BRANCH_YEAR else f' stroke-opacity="{.55 if year in MILESTONE_YEARS else .22}"'
    delay = (year - FIRST_YEAR) * 0.16
    return (f'<path class="ring" d="{d}" stroke="{stroke}" stroke-width="{width}"{opacity}'
            f' style="animation-delay:{delay:.2f}s"/>')


def crop_marks(color):
    """The orange corner marks a Bento tile shows on hover, 10px in from each corner."""
    r = []
    for x, y, sx, sy in ((10, 10, 1, 1), (W - 10, 10, -1, 1), (10, H - 10, 1, -1), (W - 10, H - 10, -1, -1)):
        r.append(f'<rect x="{x if sx > 0 else x - 14}" y="{y if sy > 0 else y - 2}" width="14" height="2"/>')
        r.append(f'<rect x="{x if sx > 0 else x - 2}" y="{y if sy > 0 else y - 14}" width="2" height="14"/>')
    return f'<g fill="{color}">{"".join(r)}</g>'


def banner(scheme):
    c = PALETTE[scheme]
    wave_paths = "\n      ".join(
        f'<path class="wave" d="{d}" stroke-opacity="{o}" style="animation-duration:{s}s"/>' for d, o, s in waves())
    ring_paths = "\n      ".join(ring_path(year, d, scheme) for year, d, _ in rings)
    mug = "".join(f'<path d="{d}" stroke-width="{w}"/>' for d, w in MUG_PATHS)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
  <title id="t">{TITLE}</title>
  <style>
    /* All type is outlined: GitHub serves SVG as an image document and never
       fetches a webfont, so nothing here may depend on one. The motion is the
       site's own (src/app.css): rings that draw themselves, a map that
       breathes, a beacon over today, the sea drifting behind. */
    .ring{{animation:draw 2.4s cubic-bezier(.6,0,.2,1) both}}
    @keyframes draw{{from{{stroke-dasharray:0 4000}}to{{stroke-dasharray:4000 0}}}}
    .map{{transform-origin:{MAP_X}px {MAP_Y}px;animation:breathe 26s ease-in-out infinite}}
    @keyframes breathe{{0%,100%{{transform:rotate(-1deg) scale(1)}}50%{{transform:rotate(1deg) scale(1.012)}}}}
    .beacon{{opacity:0;transform-origin:{MAP_X}px {MAP_Y}px;animation:beacon 2.6s ease-out infinite}}
    @keyframes beacon{{0%{{transform:scale(1);opacity:.75}}to{{transform:scale(3.6);opacity:0}}}}
    .wave{{animation:drift 60s linear infinite}}
    @keyframes drift{{to{{transform:translateX(-{W}px)}}}}
    /* Lines stay drawn and the beacon goes out: the last frame, as on the site. */
    @media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
  </style>
  <defs>
    <clipPath id="tile"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>

  <g clip-path="url(#tile)">
    <rect width="{W}" height="{H}" fill="{c["bg"]}"/>

    <g fill="none" stroke="{c["muted"]}" stroke-width="1">
      {wave_paths}
    </g>

    <g class="map" fill="none" stroke-linejoin="round">
      {ring_paths}
    </g>

    <circle class="beacon" cx="{MAP_X}" cy="{MAP_Y}" r="{DOT}" fill="{c["signal"]}"/>
    <circle cx="{MAP_X}" cy="{MAP_Y}" r="{DOT + 5}" fill="{c["bg"]}"/>
    <circle cx="{MAP_X}" cy="{MAP_Y}" r="{DOT}" fill="{c["signal"]}"/>

    <g transform="translate({PAD} 44) scale(.5625)" fill="none" stroke="{c["signal"]}" stroke-linecap="round" stroke-linejoin="round">{mug}</g>
    <path d="{d_host}" fill="{c["ink"]}"/>

    <path d="{d_first}" fill="{c["ink"]}"/>
    <path d="{d_last}" fill="{c["ink"]}"/>

    <rect x="{PAD}" y="300" width="40" height="4" fill="{c["signal"]}"/>
    <path d="{d_role}" fill="{c["signal-ink"]}"/>

    <path d="{d_geo}" fill="{c["muted"]}"/>

    {crop_marks(c["signal"])}
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="17.5" fill="none" stroke="{c["line"]}"/>
</svg>
'''


for scheme in PALETTE:
    path = f"../assets/gezeiten-{scheme}.svg"
    with open(path, "w", encoding="utf-8") as f:
        f.write(banner(scheme))
    print(f"wrote {path}")
